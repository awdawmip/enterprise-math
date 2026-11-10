#pragma once

// Include after the frozen adaptive_kernels.hpp. The exact membership,
// histogram, radix fallback and recursive cutoffs are reused unchanged.

struct SelectionTrialStats {
    u64 round = 0, window_begin = 0, window_end = 0;
    u64 low = 0, high = 0, included_samples = 0, bucket_slots = 0;
    u128 original_cells = 0, retained_cells = 0, omitted_cells = 0;
    bool compact_selected = false, grid_selected = false;
    bool density_attempted = false, density_selected = false, mass_ok = false;
    bool selected = false, gap_applied = false, kept_lower = false;
    u64 density_order_size = 0, density_work_bytes = 0;
    u64 retained_samples = 0, retained_bins = 0;
    u64 omitted_samples = 0, omitted_bins = 0;
    // index i denotes the gap between original sorted sample[i-1] and [i].
    u64 gap_index = 0, gap_size = 0;
};

struct SelectionNodeStats {
    // Preorder aligns with SelectionStats.adaptive.trace. Fused-only ablation
    // retains its old attempts there; this vector describes the new selector.
    std::vector<SelectionTrialStats> trials;
    bool density_selected = false, gap_selected = false;
    bool sample_sorted = false, fused_output = false, actual_spill_failure = false;
    u64 gap_repairs = 0;
    // Envelope of positive-width selected buckets, including their padding.
    u64 selected_low = 0, selected_high = 0;
    u64 selected_learning_samples = 0, selected_cells = 0;
    // Legacy emitted_values counts histogram-sourced values in either output
    // method. These disjoint write fields account for physical output work.
    u64 prefix_output_writes = 0, direct_output_writes = 0, total_output_writes = 0;
};

struct SelectionStats {
    AdaptiveStats adaptive;
    std::vector<SelectionNodeStats> trace;
    u64 density_attempts = 0, density_accepts = 0;
    u64 density_mass_rejects = 0, density_work_bytes_peak = 0;
    u64 gap_repairs_total = 0, sample_sorts = 0;
    u64 prefix_output_writes_total = 0, direct_output_writes_total = 0;
    u64 total_output_writes_total = 0;
};

inline const char* selection_node_path_name(const SelectionNodeStats& node,
                                           const AdaptiveNodeStats& old) {
    const auto path = old.core.core.path;
    if (node.density_selected || node.gap_selected) {
        const bool both = node.density_selected && node.gap_selected;
        switch (path) {
        case SamplePath::recursive_count:
            return both ? "gap_density_count" : node.density_selected
                ? "density_count" : "gap_count";
        case SamplePath::recursive_spill_merge:
            return both ? "gap_density_spill_merge" : node.density_selected
                ? "density_spill_merge" : "gap_spill_merge";
        case SamplePath::recursive_spill_radix:
            return both ? "gap_density_spill_radix" : node.density_selected
                ? "density_spill_radix" : "gap_spill_radix";
        default: break;
        }
    }
    return adaptive_node_path_name(old);
}

namespace brc_selection_detail {

constexpr unsigned GAP_REPAIR_LIMIT = 3;

struct DensityResult {
    bool accepted = false;
    std::size_t retained_samples = 0, retained_bins = 0;
    std::size_t omitted_bins = 0, omitted_samples = 0;
    u128 retained_cells = 0, omitted_cells = 0;
};

// Whole-bin packing. The proposal is evaluated without changing the layout.
// Order: descending sample mass / padded width, then higher sample mass,
// smaller width and smaller original index. Exact cross-products fit u128.
template<bool Collect>
DensityResult pack_density(brc_sampled_detail::SampledLayout& layout,
                          std::size_t included, std::size_t budget,
                          SampleStats* stats, SelectionTrialStats* trial) {
    std::vector<std::size_t> order;
    order.reserve(layout.buckets.size());
    for (std::size_t q = 0; q < layout.buckets.size(); ++q)
        if (layout.buckets[q].width) order.push_back(q);
    std::sort(order.begin(), order.end(), [&](std::size_t a, std::size_t b) {
        const auto& x = layout.buckets[a];
        const auto& y = layout.buckets[b];
        const u128 left = u128(x.samples) * y.width;
        const u128 right = u128(y.samples) * x.width;
        if (left != right) return left > right;
        if (x.samples != y.samples) return x.samples > y.samples;
        if (x.width != y.width) return x.width < y.width;
        return a < b;
    });
    std::vector<unsigned char> keep(layout.buckets.size(), 0);
    std::size_t cells = 0, samples = 0, bins = 0;
    for (std::size_t q : order) {
        const auto& bucket = layout.buckets[q];
        if (u128(bucket.width) > budget - cells) continue;
        keep[q] = 1;
        cells += std::size_t(bucket.width);
        samples += bucket.samples;
        ++bins;
    }
    const bool mass_ok = u128(2) * samples >= layout.sample.size();
    const bool accepted = bins != 0 && mass_ok;
    const DensityResult result{accepted, samples, bins, order.size() - bins,
        included - samples, u128(cells), layout.cells - cells};
    if constexpr (Collect) {
        trial->density_attempted = true;
        trial->density_selected = accepted;
        trial->mass_ok = mass_ok;
        trial->density_order_size = order.size();
        trial->density_work_bytes = order.capacity() * sizeof(std::size_t)
            + keep.capacity() * sizeof(unsigned char);
        trial->retained_samples = samples;
        trial->retained_bins = bins;
        trial->retained_cells = cells;
        trial->omitted_samples = result.omitted_samples;
        trial->omitted_bins = result.omitted_bins;
        trial->omitted_cells = result.omitted_cells;
    }
    if (accepted) {
        for (std::size_t q = 0; q < layout.buckets.size(); ++q)
            if (!keep[q]) layout.buckets[q].width = 0;
        layout.cells = cells;
        if constexpr (Collect) stats->active_buckets = 0;
        brc_sampled_detail::describe_layout<Collect>(layout.buckets, layout.grid,
                                                    layout.cells, stats);
    }
    return result;
}

struct GapChoice {
    bool found = false;
    std::size_t index = 0;
    u64 gap = 0;
    bool keep_lower = false;
    std::size_t next_begin = 0, next_end = 0;
};

// Windows are half-open. The split index i is between sorted[i-1] and sorted[i].
// Only positive gaps with a side of at least minimum_mass are admissible. Ties
// between gaps use the lower split index; the retained side is the larger one,
// with the lower side winning an equal-mass tie.
inline GapChoice choose_majority_gap(const std::vector<u64>& sorted,
                                    std::size_t begin, std::size_t end,
                                    std::size_t minimum_mass) {
    GapChoice best;
    for (std::size_t i = begin + 1; i < end; ++i) {
        const u64 gap = sorted[i] - sorted[i - 1];
        if (!gap) continue;
        const std::size_t lower = i - begin, upper = end - i;
        const bool keep_lower = lower >= upper;
        if (std::max(lower, upper) < minimum_mass) continue;
        if (!best.found || gap > best.gap) {
            best = {true, i, gap, keep_lower,
                    keep_lower ? begin : i, keep_lower ? i : end};
        }
    }
    return best;
}

// The original sample remains complete and sorted. Positive-gap endpoints
// ensure that ties are never divided between retained and excluded windows.
template<bool Collect>
void rebuild_window(brc_sampled_detail::SampledLayout& layout,
                    std::size_t begin, std::size_t end, SampleStats* stats) {
    layout.grid = brc_sampled_detail::make_grid(layout.sample[begin], layout.sample[end - 1]);
    layout.buckets.assign(layout.grid.bucket_count, brc_sampled_detail::Bucket{});
    for (std::size_t i = begin; i < end; ++i) {
        const u64 x = layout.sample[i];
        const std::size_t q = std::size_t((x - layout.grid.origin) >> layout.grid.shift);
        layout.buckets[q].observe(x);
    }
    layout.cells = brc_sampled_detail::finish_layout(layout.buckets, layout.grid, true);
    if constexpr (Collect) {
        stats->learning_visits += end - begin;
        stats->active_buckets = 0;
    }
    brc_sampled_detail::describe_layout<Collect>(layout.buckets, layout.grid,
                                                layout.cells, stats);
}

// Actual spills from count_sampled are outside every positive-width retained
// bucket interval. These intervals are in increasing numeric order. After
// recursively sorting spills, each bucket can therefore be emitted as a whole.
// Binary search finds a block of preceding spills; block copy and fills write
// exactly values.size() final values, without an additional output buffer.
inline std::size_t emit_fused(std::vector<u64>& values,
                             const std::vector<brc_sampled_detail::Bucket>& buckets,
                             const std::vector<std::size_t>& counts,
                             const std::vector<u64>& spills) {
    if (spills.empty()) {
        brc_sampled_detail::emit_counts(values, buckets, counts);
        return values.size();
    }
    auto out = values.begin();
    auto residual = spills.begin();
    for (const auto& bucket : buckets) {
        if (!bucket.width) continue;
        const auto before = std::lower_bound(residual, spills.end(), bucket.low);
        out = std::copy(residual, before, out);
        residual = before;
        for (std::size_t j = 0; j < bucket.width; ++j) {
            const auto count = counts[bucket.begin + j];
            if (count) out = std::fill_n(out, count, bucket.low + u64(j));
        }
    }
    out = std::copy(residual, spills.end(), out);
    return std::size_t(out - values.begin());
}

// This block is the frozen adaptive_combined selection sequence. Its helpers,
// attempt order, early decisions and diagnostics are reused unchanged so that
// selection_fused_1024 is an output-only ablation.
template<bool Collect>
bool select_previous_combined(brc_sampled_detail::SampledLayout& layout,
                              std::size_t budget, SampleStats* stats,
                              AdaptiveNodeStats& node) {
    bool selected = layout.cells <= budget;
    if constexpr (Collect) {
        if (selected) node.selected_learning_samples = layout.sample.size();
    }
    if (!selected) {
        for (std::size_t k = 0; k < 3; ++k) {
            AdaptiveAttemptStats attempt;
            const std::size_t cut = layout.sample.size()
                / brc_adaptive_detail::LADDER_DENOMINATORS[k];
            const auto trimmed = brc_adaptive_detail::rebuild_quantile_layout<Collect>(
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
            if (!selected) {
                const auto proposal = brc_adaptive_detail::prune_to_budget<Collect>(
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
    return selected;
}

template<bool Collect>
bool select_density_gap(brc_sampled_detail::SampledLayout& layout,
                        std::size_t budget, SampleStats* stats,
                        AdaptiveNodeStats& old, SelectionNodeStats& node,
                        u64 original_low, u64 original_high) {
    const std::size_t original_size = layout.sample.size();
    std::size_t begin = 0, end = original_size;
    SelectionTrialStats initial;
    if constexpr (Collect) {
        initial.window_end = original_size;
        initial.low = original_low;
        initial.high = original_high;
        initial.included_samples = initial.retained_samples = original_size;
        initial.original_cells = old.core.original_cells;
        initial.retained_cells = layout.cells;
        initial.bucket_slots = old.core.initial_bucket_slots;
        initial.compact_selected = old.core.compact_accepted;
        initial.grid_selected = !initial.compact_selected && layout.cells <= budget;
        initial.mass_ok = true;
        for (const auto& bucket : layout.buckets)
            initial.retained_bins += bucket.width != 0;
    }
    bool selected = layout.cells <= budget;
    if (!selected) {
        const auto proposal = pack_density<Collect>(layout, original_size, budget,
                                                    stats, &initial);
        selected = proposal.accepted;
        if constexpr (Collect) node.density_selected = selected;
    }
    if constexpr (Collect) {
        initial.selected = selected;
        node.trials.push_back(initial);
    }
    if (selected) return true;

    std::sort(layout.sample.begin(), layout.sample.end());
    if constexpr (Collect) node.sample_sorted = true;
    const std::size_t minimum_mass = (original_size + 1) / 2;
    for (unsigned round = 1; round <= GAP_REPAIR_LIMIT; ++round) {
        const auto gap = choose_majority_gap(layout.sample, begin, end, minimum_mass);
        if (!gap.found) break;
        begin = gap.next_begin;
        end = gap.next_end;
        rebuild_window<Collect>(layout, begin, end, stats);
        const u64 low = layout.sample[begin], high = layout.sample[end - 1];
        const std::size_t included = end - begin;
        SelectionTrialStats trial;
        if constexpr (Collect) {
            ++node.gap_repairs;
            trial.round = round;
            trial.window_begin = begin;
            trial.window_end = end;
            trial.low = low;
            trial.high = high;
            trial.included_samples = trial.retained_samples = included;
            trial.original_cells = layout.cells;
            trial.bucket_slots = layout.grid.bucket_count;
            trial.gap_applied = true;
            trial.kept_lower = gap.keep_lower;
            trial.gap_index = gap.index;
            trial.gap_size = gap.gap;
            trial.mass_ok = true;
        }
        // This is a gap window, not a quantile trim; the new trial carries it.
        [[maybe_unused]] const bool compact = brc_robust_detail::select_compact_layout<Collect>(
            layout, low, high, included, budget, false, stats, &old.core);
        selected = layout.cells <= budget;
        if constexpr (Collect) {
            trial.compact_selected = compact;
            trial.grid_selected = !compact && selected;
            trial.retained_cells = layout.cells;
            for (const auto& bucket : layout.buckets)
                trial.retained_bins += bucket.width != 0;
        }
        if (!selected) {
            const auto proposal = pack_density<Collect>(layout, included, budget,
                                                        stats, &trial);
            selected = proposal.accepted;
            if constexpr (Collect) node.density_selected = selected;
        }
        if constexpr (Collect) {
            trial.selected = selected;
            node.trials.push_back(trial);
            if (selected) node.gap_selected = true;
        }
        if (selected) return true;
    }
    return false;
}

template<bool Collect>
void describe_selected(const brc_sampled_detail::SampledLayout& layout,
                       AdaptiveNodeStats& old, SelectionNodeStats& node) {
    if constexpr (Collect) {
        bool first = true;
        for (const auto& bucket : layout.buckets) {
            if (!bucket.width) continue;
            if (first) { node.selected_low = bucket.low; first = false; }
            node.selected_high = u64(u128(bucket.low) + bucket.width - 1);
            node.selected_learning_samples += bucket.samples;
        }
        node.selected_cells = u64(layout.cells);
        old.selected_learning_samples = node.selected_learning_samples;
    }
}

template<bool Collect>
void record_node(SelectionStats* total, std::size_t index, const SampleStats* stats,
                 AdaptiveNodeStats& old, SelectionNodeStats& node,
                 std::size_t n, unsigned depth, std::size_t child_size,
                 u64 emitted_values, u64 merge_writes) {
    if constexpr (Collect) {
        brc_adaptive_detail::record_node<true>(&total->adaptive, index, stats,
            old, n, depth, child_size, emitted_values, merge_writes);
        for (const auto& trial : node.trials) {
            total->density_attempts += trial.density_attempted;
            total->density_accepts += trial.density_selected;
            total->density_mass_rejects += trial.density_attempted && !trial.mass_ok;
            total->density_work_bytes_peak = std::max(total->density_work_bytes_peak,
                                                     trial.density_work_bytes);
        }
        total->gap_repairs_total += node.gap_repairs;
        total->sample_sorts += node.sample_sorted;
        total->prefix_output_writes_total += node.prefix_output_writes;
        total->direct_output_writes_total += node.direct_output_writes;
        total->total_output_writes_total += node.total_output_writes;
        total->trace[index] = std::move(node);
    }
}

template<bool NewSelector, bool Fused, bool Collect>
void selection_body(std::vector<u64>& values, SelectionStats* total,
                    unsigned depth, bool root_call) {
    SampleStats child_stats;
    AdaptiveNodeStats old;
    SelectionNodeStats node;
    SampleStats* stats = nullptr;
    std::size_t index = 0, child_size = 0;
    u64 emitted_values = 0, merge_writes = 0;
    const std::size_t n = values.size();
    if constexpr (Collect) {
        stats = root_call ? &total->adaptive.robust.sample : &child_stats;
        index = total->trace.size();
        total->trace.emplace_back();
        total->adaptive.trace.emplace_back();
        total->adaptive.robust.trace.emplace_back();
        auto& summary = total->adaptive.robust.sample;
        summary.recursion_trace.emplace_back();
        ++summary.recursive_nodes;
        summary.recursive_input_total += n;
        summary.recursive_max_depth = std::max<u64>(summary.recursive_max_depth, depth);
    }
    const auto finish = [&] {
        record_node<Collect>(total, index, stats, old, node, n, depth, child_size,
                             emitted_values, merge_writes);
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
        old.core.original_cells = layout.cells;
        old.core.initial_bucket_slots = layout.grid.bucket_count;
        old.core.sample_bounds_checked = true;
        old.core.sample_minimum = minimum;
        old.core.sample_maximum = maximum;
        old.core.sample_span = u128(maximum) - minimum + 1;
        old.core.sample_bounds_visits = layout.sample.size();
    }
    brc_robust_detail::select_compact_layout<Collect>(layout, minimum, maximum,
        layout.sample.size(), budget, false, stats, &old.core);
    const bool selected = [&] {
        if constexpr (NewSelector)
            return select_density_gap<Collect>(layout, budget, stats, old, node,
                                                minimum, maximum);
        else return select_previous_combined<Collect>(layout, budget, stats, old);
    }();
    if (!selected) {
        brc_sampled_detail::radix_fallback<Collect>(values, stats,
                                                   SamplePath::recursive_cell_radix);
        finish();
        return;
    }
    describe_selected<Collect>(layout, old, node);
    brc_sampled_detail::assign_offsets(layout.buckets);
    std::vector<std::size_t> counts(std::size_t(layout.cells), 0);
    std::vector<u64> spills;
    if constexpr (Collect) {
        stats->counter_cells_allocated = u64(layout.cells);
        stats->base.counter_cells = u64(layout.cells);
    }
    if (!brc_sampled_detail::count_sampled<Collect>(values, layout.grid, layout.buckets,
            counts, spills, brc_sampled_detail::recursive_spill_budget(n), stats)) {
        if constexpr (Collect) {
            old.actual_spill_failure = true;
            node.actual_spill_failure = true;
        }
        brc_sampled_detail::radix_fallback<Collect>(values, stats,
                                                   SamplePath::recursive_spill_radix);
        finish();
        return;
    }
    if (!spills.empty()) {
        child_size = spills.size();
        selection_body<NewSelector, Fused, Collect>(spills, total, depth + 1, false);
    }
    emitted_values = n - spills.size();
    if constexpr (Fused) {
        [[maybe_unused]] const auto written = emit_fused(values, layout.buckets, counts, spills);
        if constexpr (Collect) {
            node.fused_output = true;
            node.direct_output_writes = written;
            node.total_output_writes = written;
        }
    } else {
        brc_sampled_detail::emit_counts(values, layout.buckets, counts);
        merge_writes = brc_sampled_detail::merge_spills(values, spills);
        if constexpr (Collect) {
            node.prefix_output_writes = emitted_values;
            node.total_output_writes = emitted_values + merge_writes;
        }
    }
    if constexpr (Collect) {
        stats->path = spills.empty() ? SamplePath::recursive_count
                                    : SamplePath::recursive_spill_merge;
        stats->base.path = AFFINE_COUNT;
    }
    finish();
}

template<bool NewSelector, bool Fused, bool Collect>
void selection_impl(std::vector<u64>& values, SelectionStats* stats,
                    unsigned starting_depth = 0) {
    if constexpr (Collect) {
        const auto capacity = brc_sampled_detail::RECURSION_DEPTH_LIMIT + 1;
        stats->trace.reserve(capacity);
        stats->adaptive.trace.reserve(capacity);
        stats->adaptive.robust.trace.reserve(capacity);
        stats->adaptive.robust.sample.recursion_trace.reserve(capacity);
    }
    selection_body<NewSelector, Fused, Collect>(values, stats, starting_depth, true);
}

} // namespace brc_selection_detail

inline void selection_fused_1024(std::vector<u64>& values, SelectionStats* stats) {
    if (stats) brc_selection_detail::selection_impl<false, true, true>(values, stats);
    else brc_selection_detail::selection_impl<false, true, false>(values, nullptr);
}

inline void selection_density_gap_1024(std::vector<u64>& values, SelectionStats* stats) {
    if (stats) brc_selection_detail::selection_impl<true, false, true>(values, stats);
    else brc_selection_detail::selection_impl<true, false, false>(values, nullptr);
}

inline void selection_combined_1024(std::vector<u64>& values, SelectionStats* stats) {
    if (stats) brc_selection_detail::selection_impl<true, true, true>(values, stats);
    else brc_selection_detail::selection_impl<true, true, false>(values, nullptr);
}
