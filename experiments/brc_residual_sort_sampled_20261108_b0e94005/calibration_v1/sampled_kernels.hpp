#pragma once

// Include after the frozen pure_bench.cpp. The input is a uint64 multiset;
// every accepted counter increment or retained spill preserves one occurrence.

enum class SamplePath {
    trivial,
    small_std_sort,
    sampled_count,
    sampled_spill_merge,
    sample_cell_radix,
    sample_spill_radix,
    full_count,
    full_cell_radix
};

inline const char* sample_path_name(SamplePath path) {
    switch (path) {
    case SamplePath::trivial: return "trivial";
    case SamplePath::small_std_sort: return "small_std_sort";
    case SamplePath::sampled_count: return "sampled_count";
    case SamplePath::sampled_spill_merge: return "sampled_spill_merge";
    case SamplePath::sample_cell_radix: return "sample_cell_radix";
    case SamplePath::sample_spill_radix: return "sample_spill_radix";
    case SamplePath::full_count: return "full_count";
    case SamplePath::full_cell_radix: return "full_cell_radix";
    }
    return "unknown";
}

struct SampleStats {
    Stats base;
    SamplePath path = SamplePath::trivial;
    u64 sample_count = 0;
    u64 learning_visits = 0;
    u64 processed = 0, covered = 0, spills = 0;
    // Whole-input learning/counting visits, excluding sample reads, output,
    // and the inherited radix implementation's internal passes.
    u64 full_data_visits = 0;
    u64 active_buckets = 0, shift = 0, origin = 0;
    u64 sample_vector_bytes = 0, bucket_vector_bytes = 0, spill_vector_bytes = 0;
    u128 counter_cells_demanded = 0; // complete learned L, including rejection
    u64 counter_cells_allocated = 0; // allocated residual table, excluding radix
};

namespace brc_sampled_detail {

constexpr unsigned COARSE_BITS = 10;
constexpr std::size_t SMALL_SORT_LIMIT = 256;

inline std::size_t cell_budget(std::size_t n) {
    return std::min<std::size_t>(COUNTER_CAP, std::max<std::size_t>(4096, n / 2));
}

inline std::size_t spill_budget(std::size_t n) {
    return std::min<std::size_t>(4096, std::max<std::size_t>(64, n / 128));
}

inline u64 next_mixed(u64& state) {
    u64 z = (state += 0x9e3779b97f4a7c15ull);
    z = (z ^ (z >> 30)) * 0xbf58476d1ce4e5b9ull;
    z = (z ^ (z >> 27)) * 0x94d049bb133111ebull;
    return z ^ (z >> 31);
}

// The S contiguous strata partition [0,n); one point is selected in each.
// Their disjointness makes every selected position unique. The sequence depends
// only on n and the requested sample limit, and is identical in all code paths.
template<class Visit>
void for_sample_indices(std::size_t n, std::size_t limit, Visit visit) {
    const std::size_t count = std::min(n, limit);
    if (!count) return;
    const std::size_t step = n / count, remainder = n % count;
    std::size_t begin = 0, error = 0;
    u64 state = 0xB0E9400520261108ull ^ u64(n)
        ^ (u64(limit) * 0xd1b54a32d192ed03ull);
    for (std::size_t i = 0; i < count; ++i) {
        std::size_t width = step;
        if (remainder && error >= count - remainder) {
            ++width;
            error -= count - remainder;
        } else error += remainder;
        const std::size_t offset = std::size_t((u128(next_mixed(state)) * width) >> 64);
        visit(begin + offset);
        begin += width;
    }
}

// Exposed for the harness's positional controls; kernels stream the same indices.
inline std::vector<std::size_t> sample_indices(std::size_t n, std::size_t limit) {
    std::vector<std::size_t> indices;
    indices.reserve(std::min(n, limit));
    for_sample_indices(n, limit, [&](std::size_t i) { indices.push_back(i); });
    return indices;
}

struct Grid {
    u64 origin;
    unsigned shift;
    std::size_t bucket_count;
};

inline Grid make_grid(u64 minimum, u64 maximum) {
    const unsigned bits = unsigned(std::bit_width(maximum - minimum));
    const unsigned shift = bits > COARSE_BITS ? bits - COARSE_BITS : 0;
    const u64 mask = (u64(1) << shift) - 1;
    const u64 origin = minimum & ~mask;
    // shift<=54, and alignment adds at most one extra bucket to 2^COARSE_BITS.
    return {origin, shift, std::size_t(((maximum - origin) >> shift) + 1)};
}

struct Bucket {
    u64 low = 0, width = 0;
    std::size_t begin = 0, samples = 0;

    void observe(u64 x) {
        if (!width) { low = x; width = 1; }
        else {
            const u64 high = low + width - 1;
            const u64 next_low = std::min(low, x);
            const u64 next_high = std::max(high, x);
            low = next_low;
            // All observations in this bucket occupy a grid interval <=2^54.
            width = next_high - next_low + 1;
        }
        ++samples;
    }
};

inline u128 finish_layout(std::vector<Bucket>& buckets, const Grid& grid, bool pad) {
    u128 cells = 0;
    for (std::size_t q = 0; q < buckets.size(); ++q) {
        auto& bucket = buckets[q];
        if (!bucket.width) continue;
        if (pad) {
            const u128 padding = std::max<u128>(8, (u128(4) * bucket.width) / (bucket.samples + 1));
            const u128 coarse_low = u128(grid.origin) + (u128(q) << grid.shift);
            const u128 coarse_end = std::min<u128>(u128(1) << 64,
                coarse_low + (u128(1) << grid.shift));
            const u128 low = bucket.low;
            const u128 padded_low = std::max(coarse_low, low > padding ? low - padding : u128(0));
            const u128 padded_end = std::min(coarse_end, low + bucket.width + padding);
            bucket.low = u64(padded_low);
            bucket.width = u64(padded_end - padded_low);
        }
        cells += bucket.width;
    }
    return cells;
}

// Call only after the complete cell demand is accepted within cell_budget().
inline void assign_offsets(std::vector<Bucket>& buckets) {
    std::size_t begin = 0;
    for (auto& bucket : buckets) {
        bucket.begin = begin;
        begin += std::size_t(bucket.width);
    }
}

template<bool Collect>
void describe_layout(const std::vector<Bucket>& buckets, const Grid& grid,
                     u128 cells, SampleStats* stats) {
    if constexpr (Collect) {
        stats->shift = grid.shift;
        stats->origin = grid.origin;
        stats->base.buckets = grid.bucket_count;
        stats->counter_cells_demanded = cells;
        stats->bucket_vector_bytes = buckets.capacity() * sizeof(Bucket);
        stats->base.auxiliary_vector_bytes = stats->sample_vector_bytes + stats->bucket_vector_bytes;
        for (const auto& bucket : buckets) stats->active_buckets += bucket.width != 0;
    }
}

template<bool Collect>
void radix_fallback(std::vector<u64>& values, SampleStats* stats, SamplePath path) {
    if constexpr (Collect) {
        stats->path = path;
        stats->base.path = VALUE_RADIX;
        offset_radix_impl<true>(values, &stats->base);
    } else offset_radix_impl<false>(values, nullptr);
}

// The original values stay untouched. A hit contributes exactly one value count;
// a miss retains that exact input occurrence. A rejected prefix is safely dropped
// because the caller can still sort the complete original array.
template<bool Collect>
bool count_sampled(const std::vector<u64>& values, const Grid& grid,
                   const std::vector<Bucket>& buckets,
                   std::vector<std::size_t>& counts, std::vector<u64>& spills,
                   std::size_t miss_limit, SampleStats* stats) {
    for (u64 x : values) {
        bool hit = false;
        if (x >= grid.origin) {
            const u64 q = (x - grid.origin) >> grid.shift;
            if (q < buckets.size()) {
                const auto& bucket = buckets[std::size_t(q)];
                const u64 offset = x - bucket.low;
                // For a clipped uint64 interval, unsigned subtraction followed
                // by this width test rejects below-low values and empty buckets.
                if (offset < bucket.width) {
                    ++counts[bucket.begin + std::size_t(offset)];
                    hit = true;
                }
            }
        }
        if constexpr (Collect) {
            ++stats->processed;
            ++stats->full_data_visits;
            stats->covered += hit;
        }
        if (!hit) {
            if (spills.empty()) {
                spills.reserve(miss_limit + 1);
                if constexpr (Collect) {
                    stats->spill_vector_bytes = spills.capacity() * sizeof(u64);
                    stats->base.auxiliary_vector_bytes += stats->spill_vector_bytes;
                }
            }
            spills.push_back(x);
            if constexpr (Collect) ++stats->spills;
            if (spills.size() > miss_limit) return false;
        }
    }
    return true;
}

inline void emit_counts(std::vector<u64>& values, const std::vector<Bucket>& buckets,
                        const std::vector<std::size_t>& counts) {
    auto out = values.begin();
    for (const auto& bucket : buckets)
        for (std::size_t j = 0; j < bucket.width; ++j) {
            const auto count = counts[bucket.begin + j];
            if (count) out = std::fill_n(out, count, bucket.low + j);
        }
}

inline void merge_spills(std::vector<u64>& values, const std::vector<u64>& spills) {
    std::size_t known = values.size() - spills.size();
    std::size_t unknown = spills.size(), out = values.size();
    while (unknown) {
        if (known && values[known - 1] > spills[unknown - 1])
            values[--out] = values[--known];
        else values[--out] = spills[--unknown];
    }
}

template<std::size_t SampleLimit, bool Collect>
void sampled_impl(std::vector<u64>& values, SampleStats* stats) {
    const std::size_t n = values.size();
    if (n < 2) return;
    if (n <= SMALL_SORT_LIMIT) {
        std::sort(values.begin(), values.end());
        if constexpr (Collect) {
            stats->path = SamplePath::small_std_sort;
            stats->base.path = STD_SORT;
        }
        return;
    }

    const std::size_t sample_count = std::min(n, SampleLimit);
    std::vector<u64> sample;
    sample.reserve(sample_count);
    u64 minimum = MAX_VALUE, maximum = 0;
    for_sample_indices(n, SampleLimit, [&](std::size_t i) {
        const u64 x = values[i];
        sample.push_back(x);
        minimum = std::min(minimum, x);
        maximum = std::max(maximum, x);
    });
    const Grid grid = make_grid(minimum, maximum);
    std::vector<Bucket> buckets(grid.bucket_count);
    for (u64 x : sample) buckets[std::size_t((x - grid.origin) >> grid.shift)].observe(x);
    const u128 cells = finish_layout(buckets, grid, true);
    if constexpr (Collect) {
        stats->sample_count = sample_count;
        stats->learning_visits = sample_count;
        stats->sample_vector_bytes = sample.capacity() * sizeof(u64);
    }
    describe_layout<Collect>(buckets, grid, cells, stats);
    if (cells > cell_budget(n)) {
        radix_fallback<Collect>(values, stats, SamplePath::sample_cell_radix);
        return;
    }

    assign_offsets(buckets);
    std::vector<std::size_t> counts(std::size_t(cells), 0);
    std::vector<u64> spills;
    if constexpr (Collect) {
        stats->counter_cells_allocated = u64(cells);
        stats->base.counter_cells = u64(cells);
    }
    if (!count_sampled<Collect>(values, grid, buckets, counts, spills, spill_budget(n), stats)) {
        radix_fallback<Collect>(values, stats, SamplePath::sample_spill_radix);
        return;
    }

    std::sort(spills.begin(), spills.end());
    emit_counts(values, buckets, counts);
    merge_spills(values, spills);
    if constexpr (Collect) {
        stats->path = spills.empty() ? SamplePath::sampled_count : SamplePath::sampled_spill_merge;
        stats->base.path = AFFINE_COUNT;
    }
}

template<bool Collect>
void full_impl(std::vector<u64>& values, SampleStats* stats) {
    const std::size_t n = values.size();
    if (n < 2) return;
    if (n <= SMALL_SORT_LIMIT) {
        std::sort(values.begin(), values.end());
        if constexpr (Collect) {
            stats->path = SamplePath::small_std_sort;
            stats->base.path = STD_SORT;
        }
        return;
    }
    const auto bounds = std::minmax_element(values.begin(), values.end());
    const u64 minimum = *bounds.first, maximum = *bounds.second;
    if constexpr (Collect) stats->full_data_visits = n;
    if (minimum == maximum) return;
    const Grid grid = make_grid(minimum, maximum);
    std::vector<Bucket> buckets(grid.bucket_count);
    for (u64 x : values) buckets[std::size_t((x - grid.origin) >> grid.shift)].observe(x);
    const u128 cells = finish_layout(buckets, grid, false);
    if constexpr (Collect) {
        stats->learning_visits = n;
        stats->full_data_visits += n;
    }
    describe_layout<Collect>(buckets, grid, cells, stats);
    if (cells > cell_budget(n)) {
        radix_fallback<Collect>(values, stats, SamplePath::full_cell_radix);
        return;
    }

    assign_offsets(buckets);
    std::vector<std::size_t> counts(std::size_t(cells), 0);
    for (u64 x : values) {
        const auto& bucket = buckets[std::size_t((x - grid.origin) >> grid.shift)];
        ++counts[bucket.begin + std::size_t(x - bucket.low)];
    }
    emit_counts(values, buckets, counts);
    if constexpr (Collect) {
        stats->processed = stats->covered = n;
        stats->full_data_visits += n;
        stats->counter_cells_allocated = u64(cells);
        stats->base.counter_cells = u64(cells);
        stats->path = SamplePath::full_count;
        stats->base.path = AFFINE_COUNT;
    }
}

} // namespace brc_sampled_detail

inline void sampled_shift_1024(std::vector<u64>& values, SampleStats* stats) {
    if (stats) brc_sampled_detail::sampled_impl<1024, true>(values, stats);
    else brc_sampled_detail::sampled_impl<1024, false>(values, nullptr);
}

inline void sampled_shift_4096(std::vector<u64>& values, SampleStats* stats) {
    if (stats) brc_sampled_detail::sampled_impl<4096, true>(values, stats);
    else brc_sampled_detail::sampled_impl<4096, false>(values, nullptr);
}

inline void full_shift_local(std::vector<u64>& values, SampleStats* stats) {
    if (stats) brc_sampled_detail::full_impl<true>(values, stats);
    else brc_sampled_detail::full_impl<false>(values, nullptr);
}
