#pragma once

// Include after the frozen sampled_kernels.hpp and its pure-sort definitions.
// The observer is the complete uint64 multiset in numerical order. A learned
// interval is only a counting opportunity; every unrepresented value is kept.

struct RobustNodeStats {
    RecursiveNodeStats core;
    bool sample_bounds_checked = false;
    bool dense_probe = false, dense_accepted = false;
    bool trim_attempted = false, trim_layout_accepted = false;
    u64 sample_minimum = 0, sample_maximum = 0;
    u64 dense_minimum = 0, dense_maximum = 0;
    u64 trim_cut = 0, trim_low = 0, trim_high = 0;
    u64 trim_included_samples = 0;
    u128 sample_span = 0, dense_span = 0;
    u128 original_cells = 0, trimmed_cells = 0;
    // Logical visits and calls, not a claim about nth_element comparisons or
    // the inherited radix sort's internal passes.
    u64 sample_bounds_visits = 0, dense_probe_visits = 0;
    u64 trim_filter_visits = 0, trim_selection_calls = 0;
    u64 initial_bucket_slots = 0, retried_bucket_slots = 0;
};

struct RobustStats {
    // Root fields and standard recursive totals retain the preceding meaning.
    // The chosen dense interval uses full_count and its exact range length.
    SampleStats sample;
    // This preorder trace aligns with sample.recursion_trace. It is diagnostic
    // only; the nullptr timing specialization allocates neither trace.
    std::vector<RobustNodeStats> trace;
    u64 dense_probes = 0, dense_accepts = 0, dense_probe_visits_total = 0;
    u64 trim_attempts = 0, trim_layout_accepts = 0;
    u64 trim_filter_visits_total = 0, trim_selection_calls_total = 0;
    u64 sample_bounds_visits_total = 0, learning_visits_total = 0;
};

inline const char* robust_node_path_name(const RobustNodeStats& node) {
    if (node.dense_accepted) return "dense_count";
    if (node.trim_attempted) {
        switch (node.core.path) {
        case SamplePath::recursive_count: return "trim_count";
        case SamplePath::recursive_spill_merge: return "trim_spill_merge";
        case SamplePath::recursive_cell_radix: return "trim_cell_radix";
        case SamplePath::recursive_spill_radix: return "trim_spill_radix";
        default: break;
        }
    }
    return sample_path_name(node.core.path);
}

namespace brc_robust_detail {

constexpr std::size_t SAMPLE_LIMIT = 1024;
constexpr std::size_t TRIM_DENOMINATOR = 64;

// The range has already been checked against the exact full-input extrema and
// the current counter budget. No second min/max scan is performed here.
template<bool Collect>
void dense_known_bounds(std::vector<u64>& values, u64 minimum,
                        std::size_t width, SampleStats* stats) {
    std::vector<std::size_t> counts(width, 0);
    for (u64 x : values) ++counts[std::size_t(x - minimum)];
    auto output = values.begin();
    for (std::size_t i = 0; i < width; ++i)
        output = std::fill_n(output, counts[i], minimum + u64(i));
    if constexpr (Collect) {
        stats->processed = stats->covered = values.size();
        stats->spills = 0;
        stats->full_data_visits += values.size();
        stats->counter_cells_demanded = width;
        stats->counter_cells_allocated = width;
        stats->base.counter_cells = width;
        stats->base.buckets = stats->active_buckets = 1;
        stats->origin = minimum;
        stats->shift = 0; // dense offsets, not the preceding coarse-grid shift
        stats->path = SamplePath::full_count;
        stats->base.path = RANGE_COUNT;
    }
}

// Rebuild only a previously rejected layout. The sample vector is a copy, so
// its order may change without changing the original input or any spill order.
// Bounds use ranks t and S-t-1; retaining all boundary ties can keep more than
// S-2*t samples. Values outside these bounds remain ordinary exact input spills.
template<bool Collect>
void retry_trimmed_layout(brc_sampled_detail::SampledLayout& layout,
                          SampleStats* stats, RobustNodeStats* node) {
    const std::size_t count = layout.sample.size();
    const std::size_t cut = count / TRIM_DENOMINATOR;
    const std::size_t high_index = count - cut - 1;
    auto begin = layout.sample.begin(), end = layout.sample.end();
    std::nth_element(begin, begin + cut, end);
    const u64 low = layout.sample[cut];
    std::nth_element(begin + cut, begin + high_index, end);
    const u64 high = layout.sample[high_index];

    layout.grid = brc_sampled_detail::make_grid(low, high);
    layout.buckets.assign(layout.grid.bucket_count, brc_sampled_detail::Bucket{});
    std::size_t included = 0;
    for (u64 x : layout.sample) if (x >= low && x <= high) {
        const std::size_t q = std::size_t((x - layout.grid.origin) >> layout.grid.shift);
        layout.buckets[q].observe(x);
        ++included;
    }
    layout.cells = brc_sampled_detail::finish_layout(layout.buckets, layout.grid, true);
    if constexpr (Collect) {
        node->trim_attempted = true;
        node->trim_cut = cut;
        node->trim_low = low;
        node->trim_high = high;
        node->trim_included_samples = included;
        node->trimmed_cells = layout.cells;
        node->trim_filter_visits = count;
        node->trim_selection_calls = 2;
        node->retried_bucket_slots = layout.grid.bucket_count;
        // As in the frozen learner, learning_visits counts observations passed
        // to bucket learning. Filtering and bounds scans are separately exposed.
        stats->learning_visits += included;
        stats->active_buckets = 0;
    }
    brc_sampled_detail::describe_layout<Collect>(layout.buckets, layout.grid,
                                                layout.cells, stats);
}

template<bool Collect>
void record_node(RobustStats* total, std::size_t index, const SampleStats* stats,
                 RobustNodeStats& node, std::size_t n, unsigned depth,
                 std::size_t child_size, u64 emitted_values, u64 merge_writes) {
    if constexpr (Collect) {
        auto& core = node.core;
        core.depth = depth;
        core.input_size = n;
        core.sample_count = stats->sample_count;
        core.learning_visits = stats->learning_visits;
        core.processed = stats->processed;
        core.covered = stats->covered;
        core.spills = stats->spills;
        core.full_data_visits = stats->full_data_visits;
        core.child_size = child_size;
        core.shift = stats->shift;
        core.origin = stats->origin;
        core.buckets = stats->base.buckets;
        core.active_buckets = stats->active_buckets;
        core.counter_cells_demanded = stats->counter_cells_demanded;
        core.counter_cells_allocated = stats->counter_cells_allocated;
        core.auxiliary_vector_bytes = stats->base.auxiliary_vector_bytes;
        core.radix_passes = stats->base.radix_passes;
        core.emitted_values = emitted_values;
        core.merge_writes = merge_writes;
        core.path = stats->path;
        // Child calls may grow either vector; no reference into them survives
        // a descent. The index preserves preorder alignment.
        total->trace[index] = node;
        total->sample.recursion_trace[index] = core;

        auto& summary = total->sample;
        summary.recursive_sample_total += core.sample_count;
        summary.recursive_processed_total += core.processed;
        summary.recursive_spill_total += core.spills;
        summary.recursive_counter_cells_total += core.counter_cells_allocated;
        summary.recursive_emitted_total += core.emitted_values;
        summary.recursive_merge_writes_total += core.merge_writes;
        switch (core.path) {
        case SamplePath::recursive_cell_radix:
        case SamplePath::recursive_spill_radix:
        case SamplePath::recursive_depth_radix:
            ++summary.recursive_radix_leaves; break;
        case SamplePath::small_std_sort:
            ++summary.recursive_small_leaves; break;
        case SamplePath::trivial:
            ++summary.recursive_trivial_leaves; break;
        case SamplePath::recursive_count:
        case SamplePath::full_count:
            ++summary.recursive_count_leaves; break;
        default: break;
        }
        total->dense_probes += node.dense_probe;
        total->dense_accepts += node.dense_accepted;
        total->dense_probe_visits_total += node.dense_probe_visits;
        total->trim_attempts += node.trim_attempted;
        total->trim_layout_accepts += node.trim_layout_accepted;
        total->trim_filter_visits_total += node.trim_filter_visits;
        total->trim_selection_calls_total += node.trim_selection_calls;
        total->sample_bounds_visits_total += node.sample_bounds_visits;
        total->learning_visits_total += core.learning_visits;
    }
}

template<bool DenseGate, bool TrimRetry, bool Collect>
void robust_body(std::vector<u64>& values, RobustStats* total,
                 unsigned depth, bool root_call) {
    SampleStats child_stats;
    RobustNodeStats node;
    SampleStats* stats = nullptr;
    std::size_t index = 0, child_size = 0;
    u64 emitted_values = 0, merge_writes = 0;
    const std::size_t n = values.size();
    if constexpr (Collect) {
        stats = root_call ? &total->sample : &child_stats;
        index = total->trace.size();
        total->trace.emplace_back();
        total->sample.recursion_trace.emplace_back();
        ++total->sample.recursive_nodes;
        total->sample.recursive_input_total += n;
        total->sample.recursive_max_depth = std::max<u64>(
            total->sample.recursive_max_depth, depth);
    }
    const auto finish = [&] {
        record_node<Collect>(total, index, stats, node, n, depth,
                             child_size, emitted_values, merge_writes);
    };
    if (n < 2) { finish(); return; }
    if (n <= brc_sampled_detail::SMALL_SORT_LIMIT) {
        std::sort(values.begin(), values.end());
        if constexpr (Collect) {
            stats->path = SamplePath::small_std_sort;
            stats->base.path = STD_SORT;
        }
        finish();
        return;
    }
    if (depth >= brc_sampled_detail::RECURSION_DEPTH_LIMIT) {
        brc_sampled_detail::radix_fallback<Collect>(values, stats,
                                                   SamplePath::recursive_depth_radix);
        finish();
        return;
    }

    const std::size_t budget = brc_sampled_detail::cell_budget(n);
    auto layout = brc_sampled_detail::learn_sampled<SAMPLE_LIMIT, Collect>(values, stats);
    if constexpr (Collect) {
        node.original_cells = layout.cells;
        node.initial_bucket_slots = layout.grid.bucket_count;
    }

    if constexpr (DenseGate) {
        const auto sample_bounds = std::minmax_element(layout.sample.begin(), layout.sample.end());
        const u64 sample_minimum = *sample_bounds.first, sample_maximum = *sample_bounds.second;
        const u128 sample_span = u128(sample_maximum) - sample_minimum + 1;
        if constexpr (Collect) {
            node.sample_bounds_checked = true;
            node.sample_minimum = sample_minimum;
            node.sample_maximum = sample_maximum;
            node.sample_span = sample_span;
            node.sample_bounds_visits = layout.sample.size();
        }
        if (sample_span <= budget) {
            const auto bounds = std::minmax_element(values.begin(), values.end());
            const u64 minimum = *bounds.first, maximum = *bounds.second;
            const u128 span = u128(maximum) - minimum + 1;
            if constexpr (Collect) {
                node.dense_probe = true;
                node.dense_minimum = minimum;
                node.dense_maximum = maximum;
                node.dense_span = span;
                node.dense_probe_visits = n;
                stats->full_data_visits += n;
            }
            if (span <= budget) {
                dense_known_bounds<Collect>(values, minimum, std::size_t(span), stats);
                if constexpr (Collect) node.dense_accepted = true;
                emitted_values = n;
                finish();
                return;
            }
            // A misleading sample only cost this exact bounds scan. The
            // original learned layout is still available and input untouched.
        }
    }

    if constexpr (TrimRetry) {
        if (layout.cells > budget) {
            retry_trimmed_layout<Collect>(layout, stats, &node);
            if constexpr (Collect) node.trim_layout_accepted = layout.cells <= budget;
        }
    }
    if (layout.cells > budget) {
        brc_sampled_detail::radix_fallback<Collect>(values, stats,
                                                   SamplePath::recursive_cell_radix);
        finish();
        return;
    }
    brc_sampled_detail::assign_offsets(layout.buckets);
    std::vector<std::size_t> counts(std::size_t(layout.cells), 0);
    std::vector<u64> spills;
    if constexpr (Collect) {
        stats->counter_cells_allocated = u64(layout.cells);
        stats->base.counter_cells = u64(layout.cells);
    }
    if (!brc_sampled_detail::count_sampled<Collect>(
            values, layout.grid, layout.buckets, counts, spills,
            brc_sampled_detail::recursive_spill_budget(n), stats)) {
        brc_sampled_detail::radix_fallback<Collect>(values, stats,
                                                   SamplePath::recursive_spill_radix);
        finish();
        return;
    }

    // Only actual retained spills descend, after the measured half-size test.
    if (!spills.empty()) {
        child_size = spills.size();
        robust_body<DenseGate, TrimRetry, Collect>(spills, total, depth + 1, false);
    }
    brc_sampled_detail::emit_counts(values, layout.buckets, counts);
    emitted_values = n - spills.size();
    merge_writes = brc_sampled_detail::merge_spills(values, spills);
    if constexpr (Collect) {
        stats->path = spills.empty() ? SamplePath::recursive_count
                                    : SamplePath::recursive_spill_merge;
        stats->base.path = AFFINE_COUNT;
    }
    finish();
}

// The explicit starting depth is for honest branch coverage of the depth cap.
template<bool DenseGate, bool TrimRetry, bool Collect>
void robust_impl(std::vector<u64>& values, RobustStats* stats, unsigned starting_depth) {
    if constexpr (Collect) {
        stats->trace.reserve(brc_sampled_detail::RECURSION_DEPTH_LIMIT + 1);
        stats->sample.recursion_trace.reserve(brc_sampled_detail::RECURSION_DEPTH_LIMIT + 1);
    }
    robust_body<DenseGate, TrimRetry, Collect>(values, stats, starting_depth, true);
}

} // namespace brc_robust_detail

inline void robust_dense_1024(std::vector<u64>& values, RobustStats* stats) {
    if (stats) brc_robust_detail::robust_impl<true, false, true>(values, stats, 0);
    else brc_robust_detail::robust_impl<true, false, false>(values, nullptr, 0);
}

inline void robust_trim_1024(std::vector<u64>& values, RobustStats* stats) {
    if (stats) brc_robust_detail::robust_impl<false, true, true>(values, stats, 0);
    else brc_robust_detail::robust_impl<false, true, false>(values, nullptr, 0);
}

inline void robust_combined_1024(std::vector<u64>& values, RobustStats* stats) {
    if (stats) brc_robust_detail::robust_impl<true, true, true>(values, stats, 0);
    else brc_robust_detail::robust_impl<true, true, false>(values, nullptr, 0);
}
