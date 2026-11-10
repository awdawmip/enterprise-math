#pragma once

// Include after the frozen phase-one robust_kernels.hpp. Only model selection
// and its diagnostics are new: learning, compact interval selection, exact
// membership, counters, emission, merge and radix fallback use frozen helpers.

struct AdaptiveAttemptStats {
    u64 cut = 0, low = 0, high = 0, included_samples = 0, bucket_slots = 0;
    u128 trimmed_cells = 0;
    bool compact_selected = false, grid_accepted = false;
    bool prune_attempted = false, prune_selected = false, prune_mass_ok = false;
    bool selected = false;
    u64 prune_order_size = 0, prune_order_vector_bytes = 0;
    u64 omitted_bins = 0, omitted_samples = 0, retained_samples = 0;
    u128 omitted_cells = 0, retained_cells = 0;
};

struct AdaptiveNodeStats {
    RobustNodeStats core;
    // At most three entries. This vector exists only in the Collect path.
    std::vector<AdaptiveAttemptStats> attempts;
    bool prune_accepted = false, actual_spill_failure = false;
    // Final failure only; earlier rejected proposals remain in attempts.
    bool selection_rejected_by_mass = false;
    // One-based ladder index; zero means an original model or no model.
    u64 selected_attempt = 0, chosen_cut = 0, selected_learning_samples = 0;
    // These fields describe only the selected pruning proposal.
    u64 omitted_bins = 0, omitted_samples = 0;
    u128 omitted_cells = 0;
};

struct AdaptiveStats {
    RobustStats robust;
    // Preorder-aligned with both robust.trace and robust.sample.recursion_trace.
    std::vector<AdaptiveNodeStats> trace;
    u64 ladder_attempts = 0, prune_attempts = 0, prune_accepts = 0;
    u64 prune_mass_rejects = 0, actual_spill_failures = 0;
    u64 selected_omitted_bins_total = 0, selected_omitted_samples_total = 0;
    u128 selected_omitted_cells_total = 0;
    u64 prune_order_entries_total = 0, prune_order_vector_bytes_peak = 0;
};

inline const char* adaptive_node_path_name(const AdaptiveNodeStats& node) {
    const auto path = node.core.core.path;
    if (node.prune_accepted) {
        switch (path) {
        case SamplePath::recursive_count: return "pruned_count";
        case SamplePath::recursive_spill_merge: return "pruned_spill_merge";
        case SamplePath::recursive_spill_radix: return "pruned_spill_radix";
        default: break;
        }
    }
    if (node.selection_rejected_by_mass && path == SamplePath::recursive_cell_radix)
        return "adaptive_mass_radix";
    return robust_node_path_name(node.core);
}

namespace brc_adaptive_detail {

constexpr std::size_t LADDER_DENOMINATORS[] = {64, 16, 4};

// The phase-one trim helper has a fixed denominator. This narrowly generalized
// version uses the same rank/tie, grid, padding and observation logic, while
// taking an explicit cut and accumulating work over bounded retry attempts.
// layout.sample always remains the complete original sample, only permuted.
template<bool Collect>
brc_robust_detail::TrimmedBounds rebuild_quantile_layout(
        brc_sampled_detail::SampledLayout& layout, std::size_t cut,
        SampleStats* stats, RobustNodeStats* node, AdaptiveAttemptStats* attempt) {
    const std::size_t count = layout.sample.size();
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
        node->trim_filter_visits += count;
        node->trim_selection_calls += 2;
        node->retried_bucket_slots = layout.grid.bucket_count;
        stats->learning_visits += included;
        stats->active_buckets = 0;
        attempt->cut = cut;
        attempt->low = low;
        attempt->high = high;
        attempt->included_samples = attempt->retained_samples = included;
        attempt->bucket_slots = layout.grid.bucket_count;
        attempt->trimmed_cells = attempt->retained_cells = layout.cells;
    }
    brc_sampled_detail::describe_layout<Collect>(layout.buckets, layout.grid,
                                                layout.cells, stats);
    return {low, high, included};
}

struct PruneResult {
    bool accepted;
    std::size_t retained_samples, omitted_bins, omitted_samples;
    u128 omitted_cells;
};

// Propose omissions without modifying the layout. Positive-width rows are
// ordered by descending padded width, then ascending row index. Stop at the
// first budget fit, even if more rows could be omitted. The mass denominator
// is the ORIGINAL sample size, not the already-trimmed observation count.
template<bool Collect>
PruneResult prune_to_budget(brc_sampled_detail::SampledLayout& layout,
                            std::size_t included, std::size_t budget,
                            SampleStats* stats, AdaptiveAttemptStats* attempt) {
    std::vector<std::size_t> order;
    order.reserve(layout.buckets.size());
    for (std::size_t q = 0; q < layout.buckets.size(); ++q)
        if (layout.buckets[q].width) order.push_back(q);
    std::sort(order.begin(), order.end(), [&](std::size_t a, std::size_t b) {
        const auto aw = layout.buckets[a].width, bw = layout.buckets[b].width;
        return aw != bw ? aw > bw : a < b;
    });
    u128 remaining_cells = layout.cells;
    std::size_t remaining_samples = included, omitted = 0;
    for (std::size_t q : order) {
        if (remaining_cells <= budget) break;
        remaining_cells -= layout.buckets[q].width;
        remaining_samples -= layout.buckets[q].samples;
        ++omitted;
    }
    const bool mass_ok = u128(2) * remaining_samples >= layout.sample.size();
    const bool accepted = remaining_cells <= budget && mass_ok;
    const u128 omitted_cells = layout.cells - remaining_cells;
    if constexpr (Collect) {
        attempt->prune_attempted = true;
        attempt->prune_selected = accepted;
        attempt->prune_mass_ok = mass_ok;
        attempt->prune_order_size = order.size();
        attempt->prune_order_vector_bytes = order.capacity() * sizeof(std::size_t);
        attempt->omitted_bins = omitted;
        attempt->omitted_samples = included - remaining_samples;
        attempt->retained_samples = remaining_samples;
        attempt->omitted_cells = omitted_cells;
        attempt->retained_cells = remaining_cells;
    }
    if (accepted) {
        for (std::size_t i = 0; i < omitted; ++i) layout.buckets[order[i]].width = 0;
        layout.cells = remaining_cells;
        if constexpr (Collect) stats->active_buckets = 0;
        brc_sampled_detail::describe_layout<Collect>(layout.buckets, layout.grid,
                                                    layout.cells, stats);
    }
    // The temporary order is destroyed before any table allocation or descent.
    // A rejected proposal has not changed a width, offset, grid, or cell demand.
    return {accepted, remaining_samples, omitted, included - remaining_samples,
            omitted_cells};
}

template<bool Collect>
void record_node(AdaptiveStats* total, std::size_t index, const SampleStats* stats,
                 AdaptiveNodeStats& node, std::size_t n, unsigned depth,
                 std::size_t child_size, u64 emitted_values, u64 merge_writes) {
    if constexpr (Collect) {
        brc_robust_detail::record_node<true>(&total->robust, index, stats, node.core,
            n, depth, child_size, emitted_values, merge_writes);
        total->ladder_attempts += node.attempts.size();
        for (const auto& attempt : node.attempts) {
            total->prune_attempts += attempt.prune_attempted;
            total->prune_accepts += attempt.prune_selected;
            total->prune_mass_rejects += attempt.prune_attempted && !attempt.prune_mass_ok;
            total->prune_order_entries_total += attempt.prune_order_size;
            total->prune_order_vector_bytes_peak = std::max(
                total->prune_order_vector_bytes_peak, attempt.prune_order_vector_bytes);
        }
        total->actual_spill_failures += node.actual_spill_failure;
        total->selected_omitted_bins_total += node.omitted_bins;
        total->selected_omitted_samples_total += node.omitted_samples;
        total->selected_omitted_cells_total += node.omitted_cells;
        // No vector reference is retained across a recursive child call.
        total->trace[index] = std::move(node);
    }
}

// The frozen recursive body has no model-selection policy hook. This small
// controller preserves its cutoffs and exact count/spill/descent/emit sequence,
// replacing only the pre-scan selection block with bounded candidate policies.
template<bool Ladder, bool Prune, bool Collect>
void adaptive_body(std::vector<u64>& values, AdaptiveStats* total,
                   unsigned depth, bool root_call) {
    SampleStats child_stats;
    AdaptiveNodeStats node;
    SampleStats* stats = nullptr;
    std::size_t index = 0, child_size = 0;
    u64 emitted_values = 0, merge_writes = 0;
    const std::size_t n = values.size();
    if constexpr (Collect) {
        stats = root_call ? &total->robust.sample : &child_stats;
        index = total->trace.size();
        total->trace.emplace_back();
        total->robust.trace.emplace_back();
        auto& summary = total->robust.sample;
        summary.recursion_trace.emplace_back();
        ++summary.recursive_nodes;
        summary.recursive_input_total += n;
        summary.recursive_max_depth = std::max<u64>(summary.recursive_max_depth, depth);
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
    auto layout = brc_sampled_detail::learn_sampled<brc_robust_detail::SAMPLE_LIMIT, Collect>(
        values, stats);
    const auto bounds = std::minmax_element(layout.sample.begin(), layout.sample.end());
    const u64 minimum = *bounds.first, maximum = *bounds.second;
    if constexpr (Collect) {
        node.core.original_cells = layout.cells;
        node.core.initial_bucket_slots = layout.grid.bucket_count;
        node.core.sample_bounds_checked = true;
        node.core.sample_minimum = minimum;
        node.core.sample_maximum = maximum;
        node.core.sample_span = u128(maximum) - minimum + 1;
        node.core.sample_bounds_visits = layout.sample.size();
    }
    brc_robust_detail::select_compact_layout<Collect>(layout, minimum, maximum,
        layout.sample.size(), budget, false, stats, &node.core);
    bool selected = layout.cells <= budget;
    if constexpr (Collect) {
        if (selected) node.selected_learning_samples = layout.sample.size();
    }

    if (!selected) {
        constexpr std::size_t attempt_limit = Ladder ? 3 : 1;
        for (std::size_t k = 0; k < attempt_limit; ++k) {
            AdaptiveAttemptStats attempt;
            const std::size_t cut = layout.sample.size() / LADDER_DENOMINATORS[k];
            const auto trimmed = rebuild_quantile_layout<Collect>(
                layout, cut, stats, &node.core, &attempt);
            if constexpr (Collect) {
                attempt.grid_accepted = layout.cells <= budget;
                node.core.trim_layout_accepted = attempt.grid_accepted;
            }
            [[maybe_unused]] const bool compact = brc_robust_detail::select_compact_layout<Collect>(
                layout, trimmed.low, trimmed.high, trimmed.included, budget, true,
                stats, &node.core);
            selected = layout.cells <= budget;
            [[maybe_unused]] std::size_t selected_samples = trimmed.included;
            [[maybe_unused]] bool last_mass_rejection = false;
            if constexpr (Collect) attempt.compact_selected = compact;
            if constexpr (Prune) {
                if (!selected) {
                    const auto proposal = prune_to_budget<Collect>(
                        layout, trimmed.included, budget, stats, &attempt);
                    selected = proposal.accepted;
                    last_mass_rejection = !proposal.accepted;
                    selected_samples = proposal.retained_samples;
                    if constexpr (Collect) {
                        if (selected) {
                            node.prune_accepted = true;
                            node.omitted_bins = proposal.omitted_bins;
                            node.omitted_samples = proposal.omitted_samples;
                            node.omitted_cells = proposal.omitted_cells;
                        }
                    }
                }
            }
            if constexpr (Collect) {
                attempt.selected = selected;
                node.attempts.push_back(attempt);
                node.selection_rejected_by_mass = !selected && last_mass_rejection;
                if (selected) {
                    node.selected_attempt = k + 1;
                    node.chosen_cut = cut;
                    node.selected_learning_samples = selected_samples;
                }
            }
            if (selected) break;
        }
    }
    if (!selected) {
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
    if (!brc_sampled_detail::count_sampled<Collect>(values, layout.grid, layout.buckets,
            counts, spills, brc_sampled_detail::recursive_spill_budget(n), stats)) {
        if constexpr (Collect) node.actual_spill_failure = true;
        brc_sampled_detail::radix_fallback<Collect>(values, stats,
                                                   SamplePath::recursive_spill_radix);
        finish();
        return;
    }
    // First viable model gets exactly one input scan. Only actual retained
    // spills descend; there is no model retry after this contraction test.
    if (!spills.empty()) {
        child_size = spills.size();
        adaptive_body<Ladder, Prune, Collect>(spills, total, depth + 1, false);
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

template<bool Ladder, bool Prune, bool Collect>
void adaptive_impl(std::vector<u64>& values, AdaptiveStats* stats,
                   unsigned starting_depth = 0) {
    if constexpr (Collect) {
        const auto capacity = brc_sampled_detail::RECURSION_DEPTH_LIMIT + 1;
        stats->trace.reserve(capacity);
        stats->robust.trace.reserve(capacity);
        stats->robust.sample.recursion_trace.reserve(capacity);
    }
    adaptive_body<Ladder, Prune, Collect>(values, stats, starting_depth, true);
}

} // namespace brc_adaptive_detail

inline void adaptive_trim_1024(std::vector<u64>& values, AdaptiveStats* stats) {
    if (stats) brc_adaptive_detail::adaptive_impl<true, false, true>(values, stats);
    else brc_adaptive_detail::adaptive_impl<true, false, false>(values, nullptr);
}

inline void adaptive_prune_1024(std::vector<u64>& values, AdaptiveStats* stats) {
    if (stats) brc_adaptive_detail::adaptive_impl<false, true, true>(values, stats);
    else brc_adaptive_detail::adaptive_impl<false, true, false>(values, nullptr);
}

inline void adaptive_combined_1024(std::vector<u64>& values, AdaptiveStats* stats) {
    if (stats) brc_adaptive_detail::adaptive_impl<true, true, true>(values, stats);
    else brc_adaptive_detail::adaptive_impl<true, true, false>(values, nullptr);
}
