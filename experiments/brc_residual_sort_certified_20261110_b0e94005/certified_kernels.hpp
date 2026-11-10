#pragma once

// Include after selection_kernels.hpp. Greedy successes retain the phase-three
// path. A fixed-grid half-mass failure receives a bounded exact feasibility
// repair before the existing majority-gap continuation.

enum class CertifiedMethod : unsigned {
    none, singleton, fractional_reject, dp_accept, dp_reject
};

inline const char* certified_method_name(CertifiedMethod method) {
    switch (method) {
    case CertifiedMethod::singleton: return "singleton";
    case CertifiedMethod::fractional_reject: return "fractional_reject";
    case CertifiedMethod::dp_accept: return "dp_accept";
    case CertifiedMethod::dp_reject: return "dp_reject";
    default: return "none";
    }
}

struct CertifiedTrialStats {
    u64 round = 0, window_begin = 0, window_end = 0, low = 0, high = 0;
    u64 original_sample_size = 0, included_samples = 0, minimum_mass = 0;
    u64 budget = 0, feasible_bins = 0, feasible_samples = 0;
    u128 original_cells = 0;
    bool singleton_checked = false, best_single_found = false;
    u64 best_single_index = 0, best_single_samples = 0, best_single_width = 0;
    bool fractional_checked = false, fractional_rejected = false;
    u64 fractional_prefix_mass = 0, fractional_denominator = 1;
    u128 fractional_numerator = 0;
    u64 fractional_upper_floor = 0;
    bool dp_attempted = false, dp_accepted = false, dp_infeasible = false;
    bool optimal_mass_certified = false, half_mass_infeasible_certified = false;
    u64 dp_mass_limit = 0, dp_items = 0, dp_cell_transitions = 0;
    u64 dp_reachable_transitions = 0, dp_improvements = 0, dp_optimal_mass = 0;
    u64 dp_width_vector_bytes = 0, dp_take_bits_bytes = 0;
    u64 auxiliary_vector_bytes = 0;
    bool selected = false;
    CertifiedMethod method = CertifiedMethod::none;
    u64 retained_samples = 0, retained_bins = 0, retained_cells = 0;
};

struct CertifiedNodeStats {
    // Only proposals after a failed greedy half-mass test appear here. The
    // aligned SelectionNodeStats keeps its original proposal outcome intact.
    std::vector<CertifiedTrialStats> trials;
    CertifiedMethod selected_method = CertifiedMethod::none;
    u64 selected_round = 0;
};

struct CertifiedStats {
    SelectionStats selection;
    std::vector<CertifiedNodeStats> trace;
    u64 singleton_checks = 0, singleton_accepts = 0;
    u64 fractional_checks = 0, fractional_rejects = 0;
    u64 dp_attempts = 0, dp_accepts = 0, dp_rejects = 0;
    u64 dp_cell_transitions_total = 0, dp_reachable_transitions_total = 0;
    u64 dp_improvements_total = 0, repair_auxiliary_bytes_peak = 0;
};

inline const char* certified_node_path_name(const CertifiedNodeStats& certified,
                                           const SelectionNodeStats& selection,
                                           const AdaptiveNodeStats& adaptive) {
    const auto path = adaptive.core.core.path;
    if (certified.selected_method == CertifiedMethod::singleton) {
        switch (path) {
        case SamplePath::recursive_count: return "singleton_count";
        case SamplePath::recursive_spill_merge: return "singleton_spill_merge";
        case SamplePath::recursive_spill_radix: return "singleton_spill_radix";
        default: break;
        }
    }
    if (certified.selected_method == CertifiedMethod::dp_accept) {
        switch (path) {
        case SamplePath::recursive_count: return "exact_mass_count";
        case SamplePath::recursive_spill_merge: return "exact_mass_spill_merge";
        case SamplePath::recursive_spill_radix: return "exact_mass_spill_radix";
        default: break;
        }
    }
    return selection_node_path_name(selection, adaptive);
}

namespace brc_certified_detail {

struct RepairResult {
    bool accepted = false;
    CertifiedMethod method = CertifiedMethod::none;
    std::size_t retained_samples = 0, retained_bins = 0, retained_cells = 0;
};

// This helper is entered after greedy packing failed the original-sample half
// test, while the original fixed grid remains unchanged. Its production budget
// is cell_budget(n)<=COUNTER_CAP=4Mi, and total positive sample mass<=1024.
template<bool Collect>
RepairResult repair_fixed_grid(brc_sampled_detail::SampledLayout& layout,
                               std::size_t included, std::size_t budget,
                               SampleStats* stats, CertifiedTrialStats* trial) {
    const std::size_t minimum_mass = (layout.sample.size() + 1) / 2;
    std::vector<std::size_t> order;
    order.reserve(layout.buckets.size());
    std::size_t best = layout.buckets.size(), feasible_mass = 0;
    for (std::size_t q = 0; q < layout.buckets.size(); ++q) {
        const auto& bucket = layout.buckets[q];
        if (!bucket.width || !bucket.samples || bucket.width > budget) continue;
        order.push_back(q);
        feasible_mass += bucket.samples;
        if (best == layout.buckets.size()
            || bucket.samples > layout.buckets[best].samples
            || (bucket.samples == layout.buckets[best].samples
                && (bucket.width < layout.buckets[best].width
                    || (bucket.width == layout.buckets[best].width && q < best))))
            best = q;
    }
    if constexpr (Collect) {
        trial->original_sample_size = layout.sample.size();
        trial->included_samples = included;
        trial->minimum_mass = minimum_mass;
        trial->budget = budget;
        trial->original_cells = layout.cells;
        trial->feasible_bins = order.size();
        trial->feasible_samples = feasible_mass;
        trial->singleton_checked = true;
        trial->best_single_found = best != layout.buckets.size();
        trial->auxiliary_vector_bytes = order.capacity() * sizeof(std::size_t);
        if (best != layout.buckets.size()) {
            trial->best_single_index = best;
            trial->best_single_samples = layout.buckets[best].samples;
            trial->best_single_width = layout.buckets[best].width;
        }
    }
    if (best != layout.buckets.size() && layout.buckets[best].samples >= minimum_mass) {
        const std::size_t cells = std::size_t(layout.buckets[best].width);
        const std::size_t samples = layout.buckets[best].samples;
        for (std::size_t q = 0; q < layout.buckets.size(); ++q)
            if (q != best) layout.buckets[q].width = 0;
        layout.cells = cells;
        if constexpr (Collect) {
            trial->selected = true;
            trial->method = CertifiedMethod::singleton;
            trial->retained_samples = samples;
            trial->retained_bins = 1;
            trial->retained_cells = cells;
            stats->active_buckets = 0;
        }
        brc_sampled_detail::describe_layout<Collect>(layout.buckets, layout.grid,
                                                    layout.cells, stats);
        return {true, CertifiedMethod::singleton, samples, 1, cells};
    }

    // Individually infeasible rows cannot occur in an integral solution. The
    // fractional relaxation uses the phase-three exact ratio/tie ordering on
    // the remaining rows. Its floor remains an upper bound for integral mass.
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
    std::size_t remaining_capacity = budget, prefix_mass = 0;
    u128 numerator = 0;
    u64 denominator = 1;
    for (std::size_t q : order) {
        const auto& bucket = layout.buckets[q];
        if (bucket.width <= remaining_capacity) {
            remaining_capacity -= std::size_t(bucket.width);
            prefix_mass += bucket.samples;
        } else {
            numerator = u128(remaining_capacity) * bucket.samples;
            denominator = bucket.width;
            break;
        }
    }
    const std::size_t upper_floor = prefix_mass + std::size_t(numerator / denominator);
    if constexpr (Collect) {
        trial->fractional_checked = true;
        trial->fractional_prefix_mass = prefix_mass;
        trial->fractional_numerator = numerator;
        trial->fractional_denominator = denominator;
        trial->fractional_upper_floor = upper_floor;
    }
    if (upper_floor < minimum_mass) {
        if constexpr (Collect) {
            trial->fractional_rejected = true;
            trial->half_mass_infeasible_certified = true;
            trial->method = CertifiedMethod::fractional_reject;
        }
        return {false, CertifiedMethod::fractional_reject, 0, 0, 0};
    }

    // D[m] is the minimum width of a feasible subset of mass exactly m, with
    // INF=C+1. Descending mass reads the preceding item row. A packed bit row
    // records each strict improvement, allowing reverse reconstruction without
    // retaining a full width table for every item. Equal widths keep the old row.
    const u32 infinity = u32(budget + 1);
    std::vector<u32> dp(feasible_mass + 1, infinity);
    dp[0] = 0;
    const std::size_t words_per_item = (feasible_mass + 64) / 64;
    std::vector<u64> take(order.size() * words_per_item, 0);
    std::size_t prefix_samples = 0;
    if constexpr (Collect) {
        trial->dp_attempted = true;
        trial->dp_mass_limit = feasible_mass;
        trial->dp_items = order.size();
        trial->dp_width_vector_bytes = dp.capacity() * sizeof(u32);
        trial->dp_take_bits_bytes = take.capacity() * sizeof(u64);
        trial->auxiliary_vector_bytes += trial->dp_width_vector_bytes
            + trial->dp_take_bits_bytes;
    }
    for (std::size_t item = 0; item < order.size(); ++item) {
        const auto& bucket = layout.buckets[order[item]];
        const std::size_t mass = bucket.samples;
        const std::size_t next_prefix = prefix_samples + mass;
        if constexpr (Collect) trial->dp_cell_transitions += prefix_samples + 1;
        for (std::size_t m = next_prefix; m >= mass; --m) {
            const u32 previous = dp[m - mass];
            if (previous == infinity) continue;
            if constexpr (Collect) ++trial->dp_reachable_transitions;
            // Both terms are <=C; C<=4Mi makes this sum safe in uint32.
            const u32 candidate = previous + u32(bucket.width);
            if (candidate < dp[m]) {
                dp[m] = candidate;
                take[item * words_per_item + (m >> 6)] |= u64(1) << (m & 63);
                if constexpr (Collect) ++trial->dp_improvements;
            }
        }
        prefix_samples = next_prefix;
    }
    std::size_t optimum = feasible_mass;
    while (dp[optimum] == infinity) --optimum;
    if constexpr (Collect) {
        trial->dp_optimal_mass = optimum;
        trial->optimal_mass_certified = true;
    }
    if (optimum < minimum_mass) {
        if constexpr (Collect) {
            trial->dp_infeasible = true;
            trial->half_mass_infeasible_certified = true;
            trial->method = CertifiedMethod::dp_reject;
        }
        return {false, CertifiedMethod::dp_reject, 0, 0, 0};
    }

    std::vector<unsigned char> keep(layout.buckets.size(), 0);
    std::size_t mass_to_reconstruct = optimum, selected_bins = 0;
    for (std::size_t item = order.size(); item-- > 0;) {
        const bool used = (take[item * words_per_item + (mass_to_reconstruct >> 6)]
                           >> (mass_to_reconstruct & 63)) & 1;
        if (used) {
            const std::size_t q = order[item];
            keep[q] = 1;
            mass_to_reconstruct -= layout.buckets[q].samples;
            ++selected_bins;
        }
    }
    if (mass_to_reconstruct != 0)
        throw std::logic_error("fixed-grid mass DP reconstruction did not reach zero");
    const std::size_t selected_cells = dp[optimum];
    for (std::size_t q = 0; q < layout.buckets.size(); ++q)
        if (!keep[q]) layout.buckets[q].width = 0;
    layout.cells = selected_cells;
    if constexpr (Collect) {
        trial->dp_accepted = true;
        trial->selected = true;
        trial->method = CertifiedMethod::dp_accept;
        trial->retained_samples = optimum;
        trial->retained_bins = selected_bins;
        trial->retained_cells = selected_cells;
        trial->auxiliary_vector_bytes += keep.capacity() * sizeof(unsigned char);
        stats->active_buckets = 0;
    }
    brc_sampled_detail::describe_layout<Collect>(layout.buckets, layout.grid,
                                                layout.cells, stats);
    return {true, CertifiedMethod::dp_accept, optimum, selected_bins, selected_cells};
}

template<bool Collect>
bool density_or_repair(brc_sampled_detail::SampledLayout& layout,
                       std::size_t included, std::size_t budget, SampleStats* stats,
                       SelectionTrialStats& trial, SelectionNodeStats& selection,
                       CertifiedNodeStats& certified) {
    const auto greedy = brc_selection_detail::pack_density<Collect>(
        layout, included, budget, stats, &trial);
    if (greedy.accepted) {
        if constexpr (Collect) {
            selection.density_selected = true;
            trial.selected = true;
        }
        return true;
    }
    CertifiedTrialStats repair;
    if constexpr (Collect) {
        repair.round = trial.round;
        repair.window_begin = trial.window_begin;
        repair.window_end = trial.window_end;
        repair.low = trial.low;
        repair.high = trial.high;
    }
    const auto result = repair_fixed_grid<Collect>(layout, included, budget, stats, &repair);
    if constexpr (Collect) {
        if (result.accepted) {
            certified.selected_method = result.method;
            certified.selected_round = trial.round;
        }
        certified.trials.push_back(repair);
    }
    return result.accepted;
}

// The phase-three original fast path, majority-gap order and one-scan boundary
// remain unchanged. A failed density proposal keeps its original false selected
// field; any successful exact repair is recorded in CertifiedNodeStats instead.
template<bool Collect>
bool select_certified_gap(brc_sampled_detail::SampledLayout& layout,
                          std::size_t budget, SampleStats* stats,
                          AdaptiveNodeStats& old, SelectionNodeStats& selection,
                          CertifiedNodeStats& certified,
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
        initial.selected = layout.cells <= budget;
        for (const auto& bucket : layout.buckets)
            initial.retained_bins += bucket.width != 0;
    }
    bool selected = layout.cells <= budget;
    if (!selected)
        selected = density_or_repair<Collect>(layout, original_size, budget, stats,
                                              initial, selection, certified);
    if constexpr (Collect) selection.trials.push_back(initial);
    if (selected) return true;

    std::sort(layout.sample.begin(), layout.sample.end());
    if constexpr (Collect) selection.sample_sorted = true;
    const std::size_t minimum_mass = (original_size + 1) / 2;
    for (unsigned round = 1; round <= brc_selection_detail::GAP_REPAIR_LIMIT; ++round) {
        const auto gap = brc_selection_detail::choose_majority_gap(
            layout.sample, begin, end, minimum_mass);
        if (!gap.found) break;
        begin = gap.next_begin;
        end = gap.next_end;
        brc_selection_detail::rebuild_window<Collect>(layout, begin, end, stats);
        const u64 low = layout.sample[begin], high = layout.sample[end - 1];
        const std::size_t included = end - begin;
        SelectionTrialStats trial;
        if constexpr (Collect) {
            ++selection.gap_repairs;
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
        [[maybe_unused]] const bool compact = brc_robust_detail::select_compact_layout<Collect>(
            layout, low, high, included, budget, false, stats, &old.core);
        selected = layout.cells <= budget;
        if constexpr (Collect) {
            trial.compact_selected = compact;
            trial.grid_selected = !compact && selected;
            trial.retained_cells = layout.cells;
            trial.selected = selected;
            for (const auto& bucket : layout.buckets)
                trial.retained_bins += bucket.width != 0;
        }
        if (!selected)
            selected = density_or_repair<Collect>(layout, included, budget, stats,
                                                  trial, selection, certified);
        if constexpr (Collect) {
            selection.trials.push_back(trial);
            if (selected) selection.gap_selected = true;
        }
        if (selected) return true;
    }
    return false;
}

template<bool Collect>
void record_node(CertifiedStats* total, std::size_t index, const SampleStats* stats,
                 AdaptiveNodeStats& adaptive, SelectionNodeStats& selection,
                 CertifiedNodeStats& certified, std::size_t n, unsigned depth,
                 std::size_t child_size, u64 emitted_values) {
    if constexpr (Collect) {
        brc_selection_detail::record_node<true>(&total->selection, index, stats,
            adaptive, selection, n, depth, child_size, emitted_values, 0);
        for (const auto& trial : certified.trials) {
            total->singleton_checks += trial.singleton_checked;
            total->singleton_accepts += trial.method == CertifiedMethod::singleton;
            total->fractional_checks += trial.fractional_checked;
            total->fractional_rejects += trial.fractional_rejected;
            total->dp_attempts += trial.dp_attempted;
            total->dp_accepts += trial.dp_accepted;
            total->dp_rejects += trial.dp_infeasible;
            total->dp_cell_transitions_total += trial.dp_cell_transitions;
            total->dp_reachable_transitions_total += trial.dp_reachable_transitions;
            total->dp_improvements_total += trial.dp_improvements;
            total->repair_auxiliary_bytes_peak = std::max(
                total->repair_auxiliary_bytes_peak, trial.auxiliary_vector_bytes);
        }
        total->trace[index] = std::move(certified);
    }
}

// The previous controller has no selection-policy hook. This narrow controller
// reuses its exact learner/count/output/fallback helpers with the repaired model
// selector and an aligned diagnostic vector.
template<bool Collect>
void certified_body(std::vector<u64>& values, CertifiedStats* total,
                    unsigned depth, bool root_call) {
    SampleStats child_stats;
    AdaptiveNodeStats adaptive;
    SelectionNodeStats selection;
    CertifiedNodeStats certified;
    SampleStats* stats = nullptr;
    std::size_t index = 0, child_size = 0;
    u64 emitted_values = 0;
    const std::size_t n = values.size();
    if constexpr (Collect) {
        stats = root_call ? &total->selection.adaptive.robust.sample : &child_stats;
        index = total->trace.size();
        total->trace.emplace_back();
        total->selection.trace.emplace_back();
        total->selection.adaptive.trace.emplace_back();
        total->selection.adaptive.robust.trace.emplace_back();
        auto& summary = total->selection.adaptive.robust.sample;
        summary.recursion_trace.emplace_back();
        ++summary.recursive_nodes;
        summary.recursive_input_total += n;
        summary.recursive_max_depth = std::max<u64>(summary.recursive_max_depth, depth);
    }
    const auto finish = [&] {
        record_node<Collect>(total, index, stats, adaptive, selection, certified,
                             n, depth, child_size, emitted_values);
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
        adaptive.core.original_cells = layout.cells;
        adaptive.core.initial_bucket_slots = layout.grid.bucket_count;
        adaptive.core.sample_bounds_checked = true;
        adaptive.core.sample_minimum = minimum;
        adaptive.core.sample_maximum = maximum;
        adaptive.core.sample_span = u128(maximum) - minimum + 1;
        adaptive.core.sample_bounds_visits = layout.sample.size();
    }
    brc_robust_detail::select_compact_layout<Collect>(layout, minimum, maximum,
        layout.sample.size(), budget, false, stats, &adaptive.core);
    if (!select_certified_gap<Collect>(layout, budget, stats, adaptive, selection,
                                       certified, minimum, maximum)) {
        brc_sampled_detail::radix_fallback<Collect>(values, stats,
                                                   SamplePath::recursive_cell_radix);
        finish();
        return;
    }
    brc_selection_detail::describe_selected<Collect>(layout, adaptive, selection);
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
            adaptive.actual_spill_failure = true;
            selection.actual_spill_failure = true;
        }
        brc_sampled_detail::radix_fallback<Collect>(values, stats,
                                                   SamplePath::recursive_spill_radix);
        finish();
        return;
    }
    if (!spills.empty()) {
        child_size = spills.size();
        certified_body<Collect>(spills, total, depth + 1, false);
    }
    emitted_values = n - spills.size();
    [[maybe_unused]] const auto written = brc_selection_detail::emit_fused(
        values, layout.buckets, counts, spills);
    if constexpr (Collect) {
        selection.fused_output = true;
        selection.direct_output_writes = written;
        selection.total_output_writes = written;
        stats->path = spills.empty() ? SamplePath::recursive_count
                                    : SamplePath::recursive_spill_merge;
        stats->base.path = AFFINE_COUNT;
    }
    finish();
}

template<bool Collect>
void certified_impl(std::vector<u64>& values, CertifiedStats* stats,
                    unsigned starting_depth = 0) {
    if constexpr (Collect) {
        const auto capacity = brc_sampled_detail::RECURSION_DEPTH_LIMIT + 1;
        stats->trace.reserve(capacity);
        stats->selection.trace.reserve(capacity);
        stats->selection.adaptive.trace.reserve(capacity);
        stats->selection.adaptive.robust.trace.reserve(capacity);
        stats->selection.adaptive.robust.sample.recursion_trace.reserve(capacity);
    }
    certified_body<Collect>(values, stats, starting_depth, true);
}

} // namespace brc_certified_detail

inline void certified_combined_1024(std::vector<u64>& values, CertifiedStats* stats) {
    if (stats) brc_certified_detail::certified_impl<true>(values, stats);
    else brc_certified_detail::certified_impl<false>(values, nullptr);
}
