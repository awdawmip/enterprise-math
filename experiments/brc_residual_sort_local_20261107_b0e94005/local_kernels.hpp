#pragma once

// Included after the frozen pure_bench.cpp, which supplies the integer types,
// exact_root, Stats, memory caps, and the offset-radix fallback.
// All parameters below are learned from the current array inside each call.
#include <type_traits>

// Dedicated local-path values extend the fixed-underlying enum without editing
// the frozen baseline. Call this helper for local algorithms' diagnostics.
constexpr Path LOCAL_ADAPTIVE_FLOOR_PATH = static_cast<Path>(unsigned(BRC_VALUE_RADIX) + 1);
constexpr Path LOCAL_ADAPTIVE_CENTER_PATH = static_cast<Path>(unsigned(BRC_VALUE_RADIX) + 2);
inline const char* local_residual_path_name(Path path) {
    if (path == LOCAL_ADAPTIVE_FLOOR_PATH) return "adaptive_floor_count";
    if (path == LOCAL_ADAPTIVE_CENTER_PATH) return "adaptive_center_count";
    if (path == BRC_GRID) return "local_count";
    if (path == BRC_VALUE_RADIX) return "local_value_radix";
    return path_name(path);
}

namespace brc_local_detail {
using i128 = __int128_t;

struct Anchor {
    u64 minimum, maximum, root_minimum, root_maximum, denominator;
    bool same_floor;
};

// With m=K^2+a and x=(K+j)^2+r, p=K+floor((x-m)/(2K)) satisfies
// p-floor_sqrt(x)=floor((j*j+r-a)/(2K)) >= -1. This makes the upward
// branch exact after one residual-threshold test. The downward branch has
// its own exact interval certificate; larger errors use exact_root.
template<bool Wide, bool Collect>
class RootClassifier {
    const Anchor& anchor;
    Stats* stats;
    bool use_anchor;
    unsigned probes = 0, successes = 0;

public:
    RootClassifier(const Anchor& a, Stats* s)
        : anchor(a), stats(s), use_anchor(a.root_minimum != 0) {}

    u64 operator()(u64 x) {
        if (anchor.same_floor || x == anchor.minimum) {
            if constexpr (Collect) ++stats->direct;
            return anchor.root_minimum;
        }
        if (x == anchor.maximum) {
            if constexpr (Collect) ++stats->direct;
            return anchor.root_maximum;
        }
        if (!use_anchor) {
            if constexpr (Collect) { ++stats->roots; ++stats->fallback_elements; }
            return exact_root(x);
        }

        const u64 p = anchor.root_minimum + (x - anchor.minimum) / anchor.denominator;
        using Square = std::conditional_t<Wide, u128, u64>;
        const Square square = Square(p) * p;
        bool accepted = true;
        u64 k;
        if constexpr (Collect) { ++stats->predictions; ++stats->quotient_calls; }
        if (square <= x) {
            // This comparison itself establishes p<=UINT32_MAX, even in the
            // wide specialization, so 2*p+1 is safe in uint64 arithmetic.
            if (x - u64(square) >= 2 * p + 1) {
                k = p + 1;
                if constexpr (Collect) ++stats->up;
            } else {
                k = p;
                if constexpr (Collect) ++stats->direct;
            }
        } else if (square - (Square(2) * p - 1) <= x) {
            k = p - 1;
            if constexpr (Collect) ++stats->down;
        } else {
            accepted = false;
            k = exact_root(x);
            if constexpr (Collect) {
                ++stats->roots;
                ++stats->fallback_elements;
                ++stats->failed_predictions;
            }
        }

        // Preserve the preceding experiment's pilot policy: unsuccessful
        // prediction disables later predictions, retaining exact root recovery.
        if (probes < 16) {
            ++probes;
            successes += accepted;
            if (probes == 16 && successes < 12) {
                use_anchor = false;
                if constexpr (Collect) stats->pilot_disabled = true;
            }
        }
        return k;
    }
};

template<bool Centered>
inline u64 bucket_key(u64 x, u64 floor_root) {
    if constexpr (Centered) {
        // Adjacent squares have an odd gap, hence no integer midpoint tie.
        // The center can equal 2^32 at the upper uint64 boundary.
        return floor_root + (x - floor_root * floor_root > floor_root);
    } else return floor_root;
}

struct Bucket {
    u64 low = MAX_VALUE, high = 0;
    std::size_t begin = 0;
    bool occupied() const { return low <= high; }
};

template<bool Collect>
void radix_fallback(std::vector<u64>& values, Stats* stats) {
    if constexpr (Collect) stats->path = BRC_VALUE_RADIX;
    offset_radix_impl<Collect>(values, stats);
}

template<bool Centered, bool Cache, bool Collect, bool Wide>
void local_body(std::vector<u64>& values, const Anchor& anchor,
                u64 first_bucket, std::size_t bucket_count,
                u128 cell_budget, Stats* stats) {
    std::vector<Bucket> buckets(bucket_count);
    std::vector<u32> indices;
    if constexpr (Cache) indices.resize(values.size());

    RootClassifier<Wide, Collect> classify(anchor, stats);
    i128 residual_low = std::numeric_limits<std::int64_t>::max();
    i128 residual_high = std::numeric_limits<std::int64_t>::min();
    for (std::size_t i = 0; i < values.size(); ++i) {
        const u64 x = values[i];
        const u64 k = classify(x);
        const u64 key = bucket_key<Centered>(x, k);
        const auto q = std::size_t(key - first_bucket);
        Bucket& bucket = buckets[q];
        bucket.low = std::min(bucket.low, x);
        bucket.high = std::max(bucket.high, x);
        if constexpr (Cache) indices[i] = u32(q);
        if constexpr (Collect) {
            const i128 residual = i128(x) - i128(key) * key;
            residual_low = std::min(residual_low, residual);
            residual_high = std::max(residual_high, residual);
        }
    }
    if constexpr (Collect) {
        stats->rspan = u64(residual_high - residual_low + 1);
        stats->auxiliary_vector_bytes = buckets.capacity() * sizeof(Bucket)
            + indices.capacity() * sizeof(u32);
    }

    // Ragged rows: L=sum(hi_q-lo_q+1), omitting empty buckets. These local
    // coordinates equal (x-key^2) minus that bucket's minimum residual.
    // Numeric lo/hi avoid materializing signed centered residues on the hot path.
    u128 cells = 0;
    for (auto& bucket : buckets) {
        bucket.begin = std::size_t(cells); // previous prefix is within the cap
        if (bucket.occupied()) cells += u128(bucket.high) - bucket.low + 1;
        if (cells > cell_budget) {
            radix_fallback<Collect>(values, stats);
            return;
        }
    }

    std::vector<std::size_t> counts(std::size_t(cells), 0);
    if constexpr (Cache) {
        for (std::size_t i = 0; i < values.size(); ++i) {
            const Bucket& bucket = buckets[indices[i]];
            ++counts[bucket.begin + std::size_t(values[i] - bucket.low)];
        }
    } else {
        // Repeating the same input order with a fresh pilot reproduces the
        // classification path, while avoiding an n-element index vector.
        RootClassifier<Wide, Collect> count_classify(anchor, stats);
        for (u64 x : values) {
            const u64 key = bucket_key<Centered>(x, count_classify(x));
            const Bucket& bucket = buckets[std::size_t(key - first_bucket)];
            ++counts[bucket.begin + std::size_t(x - bucket.low)];
        }
    }

    // Floor-square cells and nearest-square cells are each disjoint ordered
    // intervals. Ordered local traversal therefore produces numerical order.
    auto out = values.begin();
    for (const auto& bucket : buckets) if (bucket.occupied()) {
        const std::size_t width = std::size_t(bucket.high - bucket.low + 1);
        for (std::size_t j = 0; j < width; ++j)
            out = std::fill_n(out, counts[bucket.begin + j], bucket.low + j);
    }
    if constexpr (Collect) {
        stats->counter_cells = u64(cells);
        stats->path = BRC_GRID; // the harness names this accepted local_count path
    }
}

template<bool Centered, bool Cache, bool Collect>
void local_impl(std::vector<u64>& values, Stats* stats) {
    if (values.size() < 2) return;
    const auto bounds = std::minmax_element(values.begin(), values.end());
    const u64 minimum = *bounds.first, maximum = *bounds.second;
    if (minimum == maximum) {
        if constexpr (Collect) stats->direct = values.size();
        return;
    }
    const u64 root_minimum = exact_root(minimum), root_maximum = exact_root(maximum);
    const Anchor anchor{minimum, maximum, root_minimum, root_maximum,
                        root_minimum ? 2 * root_minimum : 1,
                        root_minimum == root_maximum};
    const u64 first_bucket = bucket_key<Centered>(minimum, root_minimum);
    const u64 last_bucket = bucket_key<Centered>(maximum, root_maximum);
    const u64 B = last_bucket - first_bucket + 1;
    const u128 cell_budget = std::min<u128>(COUNTER_CAP,
        std::max<u128>(4096, u128(values.size()) * 4));
    if constexpr (Collect) {
        stats->roots = 2;
        stats->kspan = B;
        stats->buckets = B;
        stats->same_basin = anchor.same_floor;
    }
    if (B > BUCKET_CAP) {
        radix_fallback<Collect>(values, stats);
        return;
    }

    // A single ordered cell needs no stored/recomputed index. Its endpoints
    // already supply the exact local range from the initial min/max scan.
    if (B == 1) {
        const u128 width = u128(maximum) - minimum + 1;
        if constexpr (Collect) stats->rspan = u64(width);
        if (width > cell_budget) {
            radix_fallback<Collect>(values, stats);
            return;
        }
        std::vector<std::size_t> counts(std::size_t(width), 0);
        for (u64 x : values) ++counts[std::size_t(x - minimum)];
        auto out = values.begin();
        for (std::size_t i = 0; i < counts.size(); ++i)
            out = std::fill_n(out, counts[i], minimum + i);
        if constexpr (Collect) {
            stats->direct = values.size();
            stats->counter_cells = u64(width);
            stats->path = BRC_GRID;
        }
        return;
    }

    // The predictor is monotone in x. One endpoint quotient proves whether
    // every candidate square fits uint64. Wider candidates use u128; even
    // the global maximum possible candidate, 2^63, has a representable square.
    bool wide = false;
    if (root_minimum) {
        const u64 maximum_prediction = root_minimum
            + (maximum - minimum) / anchor.denominator;
        wide = maximum_prediction > std::numeric_limits<u32>::max();
        if constexpr (Collect) ++stats->quotient_calls;
    }
    if (wide) local_body<Centered, Cache, Collect, true>(
        values, anchor, first_bucket, std::size_t(B), cell_budget, stats);
    else local_body<Centered, Cache, Collect, false>(
        values, anchor, first_bucket, std::size_t(B), cell_budget, stats);
}

template<bool Collect, bool Wide>
void adaptive_body(std::vector<u64>& values, const Anchor& anchor,
                   u64 floor_count, u64 center_first, u64 center_count,
                   u128 cell_budget, Stats* stats) {
    const bool floor_eligible = floor_count <= BUCKET_CAP;
    const bool center_eligible = center_count <= BUCKET_CAP;
    std::vector<Bucket> floor_buckets(floor_eligible ? std::size_t(floor_count) : 0);
    std::vector<Bucket> center_buckets(center_eligible ? std::size_t(center_count) : 0);
    std::vector<u32> floor_indices(values.size());
    RootClassifier<Wide, Collect> classify(anchor, stats);
    i128 floor_low = std::numeric_limits<std::int64_t>::max();
    i128 floor_high = std::numeric_limits<std::int64_t>::min();
    i128 center_low = floor_low, center_high = floor_high;

    for (std::size_t i = 0; i < values.size(); ++i) {
        const u64 x = values[i], k = classify(x);
        const u64 c = bucket_key<true>(x, k);
        const u64 floor_index = k - anchor.root_minimum;
        floor_indices[i] = u32(floor_index); // true floor roots are uint32
        if (floor_eligible) {
            Bucket& bucket = floor_buckets[std::size_t(floor_index)];
            bucket.low = std::min(bucket.low, x);
            bucket.high = std::max(bucket.high, x);
        }
        if (center_eligible) {
            Bucket& bucket = center_buckets[std::size_t(c - center_first)];
            bucket.low = std::min(bucket.low, x);
            bucket.high = std::max(bucket.high, x);
        }
        if constexpr (Collect) {
            const i128 r = i128(x) - i128(k) * k;
            const i128 centered = i128(x) - i128(c) * c;
            floor_low = std::min(floor_low, r);
            floor_high = std::max(floor_high, r);
            center_low = std::min(center_low, centered);
            center_high = std::max(center_high, centered);
        }
    }
    // Evaluate both observed local widths. An unselected partition is still
    // charged for learning, allocation, and prefix construction in this call.
    const auto prefix = [](std::vector<Bucket>& buckets) {
        u128 cells = 0;
        for (auto& bucket : buckets) {
            bucket.begin = std::size_t(cells);
            if (bucket.occupied()) cells += u128(bucket.high) - bucket.low + 1;
        }
        return cells;
    };
    const u128 floor_cells = prefix(floor_buckets);
    const u128 center_cells = prefix(center_buckets);
    const bool choose_center = center_eligible
        && (!floor_eligible || center_cells < floor_cells);
    const u128 cells = choose_center ? center_cells : floor_cells;
    const auto& selected = choose_center ? center_buckets : floor_buckets;
    if constexpr (Collect) {
        stats->kspan = choose_center ? center_count : floor_count;
        stats->buckets = stats->kspan;
        stats->rspan = u64(choose_center ? center_high - center_low + 1
                                        : floor_high - floor_low + 1);
        stats->auxiliary_vector_bytes = (floor_buckets.capacity() + center_buckets.capacity())
            * sizeof(Bucket) + floor_indices.capacity() * sizeof(u32);
    }
    if (cells > cell_budget) {
        radix_fallback<Collect>(values, stats);
        return;
    }
    std::vector<std::size_t> counts(std::size_t(cells), 0);
    if (choose_center) {
        for (std::size_t i = 0; i < values.size(); ++i) {
            const u64 x = values[i], k = anchor.root_minimum + floor_indices[i];
            const u64 c = bucket_key<true>(x, k);
            const Bucket& bucket = selected[std::size_t(c - center_first)];
            ++counts[bucket.begin + std::size_t(x - bucket.low)];
        }
    } else {
        for (std::size_t i = 0; i < values.size(); ++i) {
            const Bucket& bucket = selected[floor_indices[i]];
            ++counts[bucket.begin + std::size_t(values[i] - bucket.low)];
        }
    }
    auto out = values.begin();
    for (const auto& bucket : selected) if (bucket.occupied()) {
        const std::size_t width = std::size_t(bucket.high - bucket.low + 1);
        for (std::size_t i = 0; i < width; ++i)
            out = std::fill_n(out, counts[bucket.begin + i], bucket.low + i);
    }
    if constexpr (Collect) {
        stats->counter_cells = u64(cells);
        stats->path = choose_center ? LOCAL_ADAPTIVE_CENTER_PATH : LOCAL_ADAPTIVE_FLOOR_PATH;
    }
}

template<bool Collect>
void adaptive_impl(std::vector<u64>& values, Stats* stats) {
    if (values.size() < 2) return;
    const auto bounds = std::minmax_element(values.begin(), values.end());
    const u64 minimum = *bounds.first, maximum = *bounds.second;
    if (minimum == maximum) {
        if constexpr (Collect) stats->direct = values.size();
        return;
    }
    const u64 root_minimum = exact_root(minimum), root_maximum = exact_root(maximum);
    const Anchor anchor{minimum, maximum, root_minimum, root_maximum,
                        root_minimum ? 2 * root_minimum : 1,
                        root_minimum == root_maximum};
    const u64 floor_count = root_maximum - root_minimum + 1;
    const u64 center_first = bucket_key<true>(minimum, root_minimum);
    const u64 center_count = bucket_key<true>(maximum, root_maximum) - center_first + 1;
    const u128 cell_budget = std::min<u128>(COUNTER_CAP,
        std::max<u128>(4096, u128(values.size()) * 4));
    if constexpr (Collect) {
        stats->roots = 2;
        stats->same_basin = anchor.same_floor;
        stats->kspan = floor_count;
        stats->buckets = floor_count;
    }
    if (floor_count > BUCKET_CAP && center_count > BUCKET_CAP) {
        radix_fallback<Collect>(values, stats);
        return;
    }
    if (floor_count == 1 && center_count == 1) {
        // Both partitions are exactly the same single observed interval.
        // Their cell totals tie; prefer the floor partition without n indices.
        const u128 width = u128(maximum) - minimum + 1;
        if constexpr (Collect) stats->rspan = u64(width);
        if (width > cell_budget) {
            radix_fallback<Collect>(values, stats);
            return;
        }
        std::vector<std::size_t> counts(std::size_t(width), 0);
        for (u64 x : values) ++counts[std::size_t(x - minimum)];
        auto out = values.begin();
        for (std::size_t i = 0; i < counts.size(); ++i)
            out = std::fill_n(out, counts[i], minimum + i);
        if constexpr (Collect) {
            stats->direct = values.size();
            stats->counter_cells = u64(width);
            stats->path = LOCAL_ADAPTIVE_FLOOR_PATH;
        }
        return;
    }
    bool wide = false;
    if (root_minimum) {
        const u64 maximum_prediction = root_minimum
            + (maximum - minimum) / anchor.denominator;
        wide = maximum_prediction > std::numeric_limits<u32>::max();
        if constexpr (Collect) ++stats->quotient_calls;
    }
    if (wide) adaptive_body<Collect, true>(values, anchor, floor_count,
        center_first, center_count, cell_budget, stats);
    else adaptive_body<Collect, false>(values, anchor, floor_count,
        center_first, center_count, cell_budget, stats);
}

} // namespace brc_local_detail

inline void local_floor_cached(std::vector<u64>& values, Stats* stats) {
    if (stats) brc_local_detail::local_impl<false, true, true>(values, stats);
    else brc_local_detail::local_impl<false, true, false>(values, nullptr);
}

inline void local_center_cached(std::vector<u64>& values, Stats* stats) {
    if (stats) brc_local_detail::local_impl<true, true, true>(values, stats);
    else brc_local_detail::local_impl<true, true, false>(values, nullptr);
}

inline void local_center_recompute(std::vector<u64>& values, Stats* stats) {
    if (stats) brc_local_detail::local_impl<true, false, true>(values, stats);
    else brc_local_detail::local_impl<true, false, false>(values, nullptr);
}

inline void local_adaptive_cached(std::vector<u64>& values, Stats* stats) {
    if (stats) brc_local_detail::adaptive_impl<true>(values, stats);
    else brc_local_detail::adaptive_impl<false>(values, nullptr);
}
