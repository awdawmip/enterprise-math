// Robust sample-learned residual sorting. This harness extends, rather than
// copies or edits, the preceding pinned experiment. See prepare_frozen_include.py.
#ifndef BRC_SAMPLED_SOURCE
#define BRC_SAMPLED_SOURCE "build/sampled_frozen_include.hpp"
#endif
#include BRC_SAMPLED_SOURCE
#include "robust_kernels.hpp"
#include "vendor/pdqsort.h"
#include <functional>

namespace robust_experiment {

template<void (*Function)(std::vector<u64>&, RobustStats*)>
void time_robust(std::vector<u64>& values, Stats*) { Function(values, nullptr); }

void time_pdqsort(std::vector<u64>& values, Stats* stats) {
    pdqsort(values.begin(), values.end());
    if (stats) stats->path = STD_SORT;
}

struct Candidate {
    Algorithm timing;
    const sampled_experiment::Candidate* preceding = nullptr;
    void (*diagnostic)(std::vector<u64>&, RobustStats*) = nullptr;
    bool dense = false, trim = false;
};

const std::vector<Candidate>& all_candidates() {
    static const auto result = [] {
        std::vector<Candidate> c;
        for (const auto& old : sampled_experiment::candidates)
            c.push_back({old.timing, &old});
        c.push_back({{"robust_dense_1024", time_robust<robust_dense_1024>}, nullptr,
                     robust_dense_1024, true, false});
        c.push_back({{"robust_trim_1024", time_robust<robust_trim_1024>}, nullptr,
                     robust_trim_1024, false, true});
        c.push_back({{"robust_combined_1024", time_robust<robust_combined_1024>}, nullptr,
                     robust_combined_1024, true, true});
        c.push_back({{"pdqsort", time_pdqsort}});
        return c;
    }();
    return result;
}

enum class NewKind {
    none, narrow_offsets, contamination, dense4096_outliers, dense8192_outliers,
    interior_contamination, heterogeneous, skew97, uniform64, sample_trap,
    large_cluster_tail, dense_exact, dense_one_above, trim16, trim17, sample_constant
};

struct Condition {
    std::string family, stage, original_stage, regime;
    std::size_t n = 0;
    bool legacy = false;
    sampled_experiment::ExperimentCondition preceding{};
    NewKind kind = NewKind::none;
    u64 tag = 0, contamination_per_100000 = 0;
    bool two_sided = false;
};

std::vector<Condition> conditions() {
    const std::set<std::pair<std::string, std::size_t>> calibration{
        {"uniform_1e6", 100}, {"jitter1e6_B20_D8", 100000},
        {"square1e6_B256_D8", 100000}, {"rare_far_cluster", 100000},
        {"uniform_4096", 100000}, {"two_uint64_outliers", 100000},
        {"uniform_uint64", 100000}, {"uint64_top_window", 100000}};
    std::vector<Condition> result;
    for (const auto& old : sampled_experiment::selected_conditions()) {
        Condition c;
        c.family = old.base.name; c.n = old.base.n; c.legacy = true; c.preceding = old;
        c.stage = calibration.contains({c.family, c.n}) ? "calibration" : "regression";
        c.original_stage = old.stage;
        c.regime = sampled_experiment::seed_regime(old);
        result.push_back(c);
    }
    const auto add = [&](const char* name, std::size_t n, NewKind kind, u64 tag,
                         u64 rate = 0, bool two_sided = false,
                         const char* stage = "heldout") {
        Condition c;
        c.family = name; c.stage = stage; c.original_stage = "new_20261110";
        c.regime = kind == NewKind::sample_trap ? "actual_sampler_position_adversary"
            : std::string_view(stage) == "mechanism" ? "deterministic_mechanism_banks"
            : "independent_robust_v1_seed_banks";
        c.n = n; c.kind = kind; c.tag = tag;
        c.contamination_per_100000 = rate; c.two_sided = two_sided;
        result.push_back(c);
    };
    // Freeze recipes before timing. These are fresh input banks, not a claim
    // that every family is conceptually unseen. Rates are exact multiplicities.
    add("fresh_narrow_offsets", 131072, NewKind::narrow_offsets, 101);
    add("fresh_tail_0p01pct_high", 100000, NewKind::contamination, 102, 10);
    add("fresh_tail_0p3pct_both", 100000, NewKind::contamination, 103, 300, true);
    add("fresh_tail_1pct_high", 100000, NewKind::contamination, 104, 1000);
    add("fresh_tail_2pct_high", 100000, NewKind::contamination, 105, 2000);
    add("fresh_tail_5pct_both", 100000, NewKind::contamination, 106, 5000, true);
    add("fresh_dense4096_two_extremes", 100000, NewKind::dense4096_outliers, 107);
    add("fresh_dense8192_0p3pct_extremes", 131072, NewKind::dense8192_outliers, 108);
    add("fresh_interior_contamination", 100000, NewKind::interior_contamination, 109);
    add("fresh_heterogeneous_widths", 100000, NewKind::heterogeneous, 110);
    add("fresh_skew97_24clusters", 100000, NewKind::skew97, 111);
    add("fresh_uniform_uint64", 131072, NewKind::uniform64, 112);
    add("fresh_actual_sampler_trap", 131072, NewKind::sample_trap, 113);
    add("fresh_128clusters_0p3pct_tail", 250000, NewKind::large_cluster_tail, 114);
    add("witness_dense_budget_exact", 8192, NewKind::dense_exact, 201, 0, false, "mechanism");
    add("witness_dense_budget_plus_one", 8192, NewKind::dense_one_above, 202, 0, false, "mechanism");
    add("witness_trim16_tail_success", 100000, NewKind::trim16, 203, 0, false, "mechanism");
    add("witness_trim17_tie_reject", 100000, NewKind::trim17, 204, 0, false, "mechanism");
    add("witness_sample_constant_extremes", 16384, NewKind::sample_constant, 205, 0, false, "mechanism");
    require(result.size() == 58, "frozen robust matrix must contain 58 conditions");
    return result;
}

bool selected(const Condition& c, const std::string& subset) {
    if (subset.empty() || subset == "all") return true;
    if (subset == "evaluation") return c.stage == "regression" || c.stage == "heldout";
    if (subset == "calibration" || subset == "regression" || subset == "heldout"
        || subset == "mechanism") return c.stage == subset;
    return c.family.find(subset) != std::string::npos;
}

std::vector<std::size_t> nonsampled_positions(std::size_t n) {
    std::vector<bool> sampled(n, false);
    for (auto i : brc_sampled_detail::sample_indices(n, 1024)) sampled[i] = true;
    std::vector<std::size_t> result;
    for (std::size_t i = 0; i < n; ++i) if (!sampled[i]) result.push_back(i);
    return result;
}

std::vector<u64> trim_witness(std::size_t n, unsigned sample_high,
                              std::size_t total_high, unsigned bank = 0,
                              unsigned sample_low = 0, std::size_t total_low = 0) {
    const u64 origin = (u64(1) << 48) + u64(bank) * (u64(1) << 30);
    const u64 high = MAX_VALUE - bank;
    const auto ordinary = [&](std::size_t i) {
        return origin + u64((i % 160) / 8) * (u64(1) << 20) + u64(i % 8);
    };
    std::vector<u64> input(n);
    for (std::size_t i = 0; i < n; ++i) input[i] = ordinary(i);
    const auto indices = brc_sampled_detail::sample_indices(n, 1024);
    require(indices.size() == 1024 && sample_high + sample_low < 1024,
            "trim witness requires full sample");
    require(total_high >= sample_high && total_low >= sample_low,
            "trim witness actual tails contain sampled tails");
    for (std::size_t i = 0; i < indices.size(); ++i)
        input[indices[i]] = i < sample_high ? high
            : i < sample_high + sample_low ? u64(bank)
            : ordinary(i - sample_high - sample_low);
    const auto free = nonsampled_positions(n);
    const auto high_extra = total_high - sample_high, low_extra = total_low - sample_low;
    require(high_extra + low_extra <= free.size(), "trim witness tail count capacity");
    for (std::size_t i = 0; i < high_extra; ++i) input[free[i]] = high;
    for (std::size_t i = 0; i < low_extra; ++i) input[free[high_extra + i]] = bank;
    return input;
}

std::vector<u64> dense_witness(bool one_above, bool at_top = false) {
    constexpr std::size_t n = 8192;
    const u64 origin = at_top ? MAX_VALUE - 4096 : 0;
    std::vector<u64> input(n);
    for (std::size_t i = 0; i < n; ++i) input[i] = origin + i % 4096;
    const auto indices = brc_sampled_detail::sample_indices(n, 1024);
    input[indices.front()] = origin;
    input[indices.back()] = origin + 4095;
    if (one_above) input[nonsampled_positions(n).front()] = origin + 4096;
    return input;
}

std::vector<u64> input_bank(const Condition& c, unsigned bank) {
    if (c.legacy) return sampled_experiment::input_bank(c.preceding, bank);
    if (c.kind == NewKind::dense_exact) return dense_witness(false);
    if (c.kind == NewKind::dense_one_above) return dense_witness(true);
    if (c.kind == NewKind::trim16) return trim_witness(c.n, 16, 1000, bank);
    if (c.kind == NewKind::trim17) return trim_witness(c.n, 17, 1000, bank);
    if (c.kind == NewKind::sample_constant) {
        std::vector<u64> input(c.n, 42 + bank);
        const auto free = nonsampled_positions(c.n);
        input[free.front()] = 0; input[free.back()] = MAX_VALUE;
        return input;
    }
    // No distribution labels or generator metadata reach the algorithm.
    const u64 seed = 0x524F425553543130ull ^ (u64(c.n) * 0x9e3779b97f4a7c15ull)
        ^ (u64(bank) * 0xD1B54A32D192ED03ull) ^ (c.tag * 0x94D049BB133111EBull);
    std::mt19937_64 rng(seed);
    const u64 origin = (u64(1) << 48) + bounded(rng, u64(1) << 28);
    std::vector<u64> input(c.n);
    std::array<u64, 24> offsets{};
    for (auto& x : offsets) x = bounded(rng, u64(1) << 18);
    const auto clustered = [&]() {
        const u64 label = bounded(rng, 20);
        return origin + label * (u64(1) << 20) + offsets[label] + bounded(rng, 8);
    };
    switch (c.kind) {
    case NewKind::narrow_offsets:
    case NewKind::contamination:
        for (auto& x : input) x = clustered();
        if (c.kind == NewKind::contamination) {
            const std::size_t count = c.n * c.contamination_per_100000 / 100000;
            for (std::size_t i = 0; i < count; ++i)
                input[i] = c.two_sided && i % 2 ? bounded(rng, 4096)
                    : MAX_VALUE - bounded(rng, 4096);
            std::shuffle(input.begin(), input.end(), rng);
        }
        break;
    case NewKind::dense4096_outliers:
    case NewKind::dense8192_outliers: {
        const u64 width = c.kind == NewKind::dense4096_outliers ? 4096 : 8192;
        for (auto& x : input) x = (u64(1) << 50) + bounded(rng, width);
        const std::size_t count = width == 4096 ? 2 : c.n * 3 / 1000;
        for (std::size_t i = 0; i < count; ++i)
            input[i] = i % 2 ? MAX_VALUE - bounded(rng, 1024) : bounded(rng, 1024);
        input[0] = 0; input[1] = MAX_VALUE;
        std::shuffle(input.begin(), input.end(), rng);
        break;
    }
    case NewKind::interior_contamination:
        for (auto& x : input)
            x = origin + bounded(rng, 2) * (u64(1) << 40) + bounded(rng, 8);
        for (std::size_t i = 0; i < c.n * 3 / 1000; ++i)
            input[i] = origin + (u64(1) << 39) + bounded(rng, u64(1) << 30);
        std::shuffle(input.begin(), input.end(), rng);
        break;
    case NewKind::heterogeneous: {
        constexpr std::array<u64,16> widths{1,2,4,8,16,32,64,128,256,512,1024,2048,2048,2048,2048,2048};
        for (auto& x : input) {
            const auto j = bounded(rng, widths.size());
            x = origin + j * 4096 + bounded(rng, widths[j]);
        }
        break;
    }
    case NewKind::skew97:
        for (auto& x : input) {
            const auto j = bounded(rng, 100) < 97 ? 0 : 1 + bounded(rng, 23);
            x = origin + j * (u64(1) << 23) + offsets[j] + bounded(rng, 8);
        }
        break;
    case NewKind::uniform64:
        for (auto& x : input) x = rng();
        break;
    case NewKind::sample_trap:
        for (auto& x : input) x = rng();
        for (std::size_t limit : {std::size_t(1024), std::size_t(4096)})
            for (auto i : brc_sampled_detail::sample_indices(c.n, limit))
                input[i] = (u64(1) << 50) + 5 + bank;
        break;
    case NewKind::large_cluster_tail:
        for (auto& x : input)
            x = (u64(1) << 56) + bounded(rng, 128) * (u64(1) << 25) + bounded(rng, 8);
        for (std::size_t i = 0; i < c.n * 3 / 1000; ++i)
            input[i] = (u64(1) << 60) + bounded(rng, 8);
        std::shuffle(input.begin(), input.end(), rng);
        break;
    default: throw std::runtime_error("unhandled new condition recipe");
    }
    return input;
}

std::set<std::string> paths_seen;
u64 verified_inputs = 0, verified_outputs = 0;

// This intentionally differs from the preceding checker only where the new
// dense probe, dense leaf, and trimmed learning add work. Baseline diagnostics
// continue to use the preceding checker unchanged.
void check_robust(const Candidate& candidate, const RobustStats& stats,
                  const std::vector<u64>& input,
                  const sampled_experiment::InputShape& shape,
                  unsigned starting_depth = 0) {
    const auto& summary = stats.sample;
    const auto n = input.size();
    require(!stats.trace.empty() && stats.trace.size() == summary.recursion_trace.size(),
            "robust aligned traces missing");
    const auto& root = stats.trace.front().core;
    require(root.input_size == n && root.depth == starting_depth, "robust root identity");
    require(root.path == summary.path && root.sample_count == summary.sample_count
        && root.learning_visits == summary.learning_visits && root.processed == summary.processed
        && root.covered == summary.covered && root.spills == summary.spills
        && root.full_data_visits == summary.full_data_visits && root.shift == summary.shift
        && root.origin == summary.origin && root.buckets == summary.base.buckets
        && root.active_buckets == summary.active_buckets
        && root.counter_cells_demanded == summary.counter_cells_demanded
        && root.counter_cells_allocated == summary.counter_cells_allocated
        && root.auxiliary_vector_bytes == summary.base.auxiliary_vector_bytes
        && root.radix_passes == summary.base.radix_passes, "robust root-only fields");
    u64 inputs=0, samples=0, processed=0, spills=0, cells=0, emitted=0, merged=0;
    u64 radix=0, small=0, trivial=0, counted=0, branches=0;
    u64 probes=0, accepts=0, probe_visits=0, trims=0, trim_accepts=0;
    u64 filter_visits=0, selection_calls=0, bounds_visits=0, learning_visits=0;
    for (std::size_t i=0; i<stats.trace.size(); ++i) {
        const auto& r=stats.trace[i]; const auto& q=r.core;
        const auto& mirror=summary.recursion_trace[i];
        const auto budget=brc_sampled_detail::cell_budget(q.input_size);
        const bool early=q.path==SamplePath::trivial || q.path==SamplePath::small_std_sort
            || q.path==SamplePath::recursive_depth_radix;
        paths_seen.insert(robust_node_path_name(r));
        require(q.depth==starting_depth+i && q.depth<=brc_sampled_detail::RECURSION_DEPTH_LIMIT,
                "robust depth cap");
        require(q.input_size==mirror.input_size && q.path==mirror.path
            && q.processed==mirror.processed && q.full_data_visits==mirror.full_data_visits
            && q.counter_cells_demanded==mirror.counter_cells_demanded,
                "robust core trace alignment");
        require(q.processed==q.covered+q.spills && q.processed<=q.input_size,
                "robust multiplicity conservation");
        require(q.full_data_visits==q.processed+r.dense_probe_visits,
                "robust full input visit identity");
        require(q.sample_count==(early?0:std::min<u64>(q.input_size,1024)),
                "robust sample count");
        require(q.learning_visits==q.sample_count+(r.trim_attempted?r.trim_included_samples:0),
                "robust original plus retried learning visits");
        require(q.shift<=54 && q.counter_cells_allocated<=budget, "robust shift and allocation cap");
        if(q.counter_cells_allocated)
            require(q.counter_cells_allocated==q.counter_cells_demanded, "robust exact allocation");
        require(r.sample_bounds_checked==(candidate.dense&&!early), "robust sample bounds gate");
        if(r.sample_bounds_checked) {
            require(r.sample_minimum<=r.sample_maximum
                && r.sample_span==u128(r.sample_maximum)-r.sample_minimum+1
                && r.sample_bounds_visits==q.sample_count, "robust exact sample span");
            require(r.dense_probe==(r.sample_span<=budget), "robust probe decision");
        } else require(!r.dense_probe&&!r.sample_bounds_visits&&!r.sample_span,
                       "disabled dense gate adds no sample range pass");
        if(r.dense_probe) {
            require(r.dense_probe_visits==q.input_size && r.dense_minimum<=r.dense_maximum
                && r.dense_span==u128(r.dense_maximum)-r.dense_minimum+1,
                    "robust exact actual span");
            require(r.dense_accepted==(r.dense_span<=budget), "robust dense acceptance");
            if(i==0) require(r.dense_minimum==shape.minimum && r.dense_maximum==shape.maximum
                && r.dense_span==shape.span, "robust actual root bounds oracle");
        } else require(!r.dense_accepted&&!r.dense_probe_visits&&!r.dense_span,
                       "absent dense probe work");
        require(r.trim_attempted==(candidate.trim&&!early&&!r.dense_accepted&&r.original_cells>budget),
                "robust retry only after original cell rejection");
        if(r.trim_attempted) {
            require(r.trim_cut==q.sample_count/64 && r.trim_low<=r.trim_high
                && r.trim_included_samples>=q.sample_count-2*r.trim_cut
                && r.trim_included_samples<=q.sample_count
                && r.trim_filter_visits==q.sample_count && r.trim_selection_calls==2,
                    "robust inclusive trim ranks and work");
            require(r.trim_layout_accepted==(r.trimmed_cells<=budget)
                && q.counter_cells_demanded==r.trimmed_cells, "robust retried cell gate");
        } else {
            require(!r.trim_layout_accepted&&!r.trim_filter_visits&&!r.trim_selection_calls
                &&!r.trim_included_samples&&!r.retried_bucket_slots, "absent retry work");
            if(!r.dense_accepted)
                require(q.counter_cells_demanded==r.original_cells, "robust original cells preserved");
        }
        if(early) require(!q.processed&&!q.counter_cells_demanded&&!r.initial_bucket_slots,
                          "robust early terminal does not learn");
        switch(q.path) {
        case SamplePath::full_count:
            require(r.dense_accepted && q.counter_cells_demanded==r.dense_span,
                    "robust dense leaf actual interval");
            [[fallthrough]];
        case SamplePath::recursive_count:
            require(q.processed==q.input_size && q.covered==q.input_size && !q.spills
                && q.emitted_values==q.input_size && !q.merge_writes, "robust count leaf");
            ++counted; break;
        case SamplePath::recursive_spill_merge:
            require(q.processed==q.input_size && q.spills>0 && q.spills<=q.input_size/2
                && q.child_size==q.spills && q.emitted_values==q.covered
                && q.merge_writes>=q.spills && q.merge_writes<=q.input_size,
                    "robust contraction and merge");
            ++branches; break;
        case SamplePath::recursive_cell_radix:
            require(q.counter_cells_demanded>budget && !q.counter_cells_allocated&&!q.processed,
                    "robust early radix rejection"); ++radix; break;
        case SamplePath::recursive_spill_radix:
            require(q.spills==q.input_size/2+1 && q.counter_cells_allocated>0,
                    "robust half plus one rejection"); ++radix; break;
        case SamplePath::recursive_depth_radix:
            require(q.depth==brc_sampled_detail::RECURSION_DEPTH_LIMIT
                && q.input_size>brc_sampled_detail::SMALL_SORT_LIMIT,
                    "robust forced depth terminal"); ++radix; break;
        case SamplePath::small_std_sort:
            require(q.input_size>=2 && q.input_size<=brc_sampled_detail::SMALL_SORT_LIMIT,
                    "robust small cutoff"); ++small; break;
        case SamplePath::trivial:
            require(q.input_size<2,"robust trivial cutoff"); ++trivial; break;
        default: throw std::runtime_error("unexpected robust trace path");
        }
        if(q.path==SamplePath::recursive_spill_merge)
            require(i+1<stats.trace.size() && stats.trace[i+1].core.input_size==q.child_size,
                    "robust retained spill child");
        else {
            require(!q.child_size && i+1==stats.trace.size(), "robust single terminal trace");
            if(q.path!=SamplePath::recursive_count && q.path!=SamplePath::full_count)
                require(!q.emitted_values&&!q.merge_writes,"robust fallback counter write exclusion");
        }
        inputs+=q.input_size; samples+=q.sample_count; processed+=q.processed;
        spills+=q.spills; cells+=q.counter_cells_allocated; emitted+=q.emitted_values;
        merged+=q.merge_writes; probes+=r.dense_probe; accepts+=r.dense_accepted;
        probe_visits+=r.dense_probe_visits; trims+=r.trim_attempted;
        trim_accepts+=r.trim_layout_accepted; filter_visits+=r.trim_filter_visits;
        selection_calls+=r.trim_selection_calls; bounds_visits+=r.sample_bounds_visits;
        learning_visits+=q.learning_visits;
    }
    require(summary.recursive_nodes==stats.trace.size() && summary.recursive_input_total==inputs
        && summary.recursive_sample_total==samples && summary.recursive_processed_total==processed
        && summary.recursive_spill_total==spills && summary.recursive_counter_cells_total==cells
        && summary.recursive_emitted_total==emitted && summary.recursive_merge_writes_total==merged
        && summary.recursive_radix_leaves==radix && summary.recursive_small_leaves==small
        && summary.recursive_trivial_leaves==trivial && summary.recursive_count_leaves==counted
        && summary.recursive_max_depth==stats.trace.back().core.depth, "robust trace aggregates");
    require(stats.dense_probes==probes && stats.dense_accepts==accepts
        && stats.dense_probe_visits_total==probe_visits && stats.trim_attempts==trims
        && stats.trim_layout_accepts==trim_accepts && stats.trim_filter_visits_total==filter_visits
        && stats.trim_selection_calls_total==selection_calls && stats.sample_bounds_visits_total==bounds_visits
        && stats.learning_visits_total==learning_visits, "robust extension aggregates");
    require(radix+small+trivial+counted==1 && branches+1==summary.recursive_nodes,
            "robust exactly one terminal");
    const u64 baseline_terminal=counted?0:stats.trace.back().core.input_size;
    require(emitted==n-baseline_terminal, "robust counter emissions telescope");
    require(summary.recursive_nodes<=brc_sampled_detail::RECURSION_DEPTH_LIMIT+1-starting_depth
        &&u128(inputs)<=u128(n)*2&&processed<=inputs&&samples<=inputs&&spills<=n&&merged<=inputs,
            "robust geometric core work bounds");
    require(u128(cells)<=u128(n)+u128(4096)*summary.recursive_nodes
        && probe_visits<=inputs && bounds_visits<=samples && filter_visits<=samples
        && learning_visits<=2*samples, "robust new work and allocation bounds");
    const auto& r=stats.trace.front();
    if(r.sample_bounds_checked || r.trim_attempted) {
        std::vector<u64> observations;
        for(auto index:brc_sampled_detail::sample_indices(n,1024)) observations.push_back(input[index]);
        std::sort(observations.begin(),observations.end());
        if(r.sample_bounds_checked)
            require(r.sample_minimum==observations.front()&&r.sample_maximum==observations.back(),
                    "robust independent root sample bounds oracle");
        if(r.trim_attempted) {
            const auto cut=observations.size()/64;
            const auto low=observations[cut], high=observations[observations.size()-cut-1];
            const auto retained=std::count_if(observations.begin(),observations.end(),
                [&](u64 x){return x>=low&&x<=high;});
            require(r.trim_low==low&&r.trim_high==high&&r.trim_included_samples==u64(retained),
                    "robust independent inclusive quantile oracle");
        }
    }
}

void run_diagnostic(const Candidate& c,std::vector<u64>& values,RobustStats& stats) {
    if(c.preceding) c.preceding->diagnostic(values,&stats.sample);
    else if(c.diagnostic) c.diagnostic(values,&stats);
    else time_pdqsort(values,&stats.sample.base);
}

std::string root_path(const Candidate& c,const RobustStats& stats) {
    if(c.preceding) return sampled_experiment::observed_path(*c.preceding,stats.sample);
    return c.diagnostic?robust_node_path_name(stats.trace.front()):"pdqsort";
}

void check_new_witness(const Condition& condition,const Candidate& c,const RobustStats& s) {
    if(!c.diagnostic || condition.legacy || condition.stage!="mechanism") return;
    const auto& r=s.trace.front();
    if(condition.kind==NewKind::dense_exact && c.dense)
        require(r.dense_accepted&&r.dense_span==4096,"dense exact budget witness");
    if(condition.kind==NewKind::dense_one_above && c.dense)
        require(r.dense_probe&&!r.dense_accepted&&r.sample_span==4096&&r.dense_span==4097,
                "dense one above witness");
    if(condition.kind==NewKind::trim16 && c.trim)
        require(r.trim_attempted&&r.trim_layout_accepted&&r.trimmed_cells<=800
            &&r.core.path==SamplePath::recursive_spill_merge&&r.core.spills==1000,
                "trim sixteen inclusive rank witness");
    if(condition.kind==NewKind::trim17 && c.trim)
        require(r.trim_attempted&&!r.trim_layout_accepted&&r.trim_high>=MAX_VALUE-7
            &&r.core.path==SamplePath::recursive_cell_radix,
                "trim seventeen tied rank witness");
    if(condition.kind==NewKind::sample_constant && c.dense)
        require(r.dense_probe&&!r.dense_accepted&&r.dense_span==(u128(1)<<64)
            &&r.core.path==SamplePath::recursive_spill_merge&&r.core.spills==2,
                "sample constant actual full span witness");
}

RobustStats check_one(const Candidate& c,const std::vector<u64>& input,
                     const std::vector<u64>& expected,
                     const sampled_experiment::InputShape& shape,
                     const Condition* condition=nullptr) {
    auto actual=input; RobustStats stats;
    run_diagnostic(c,actual,stats);
    if(actual!=expected) throw std::runtime_error(std::string("instrumented mismatch: ")+c.timing.name);
    if(c.preceding) {
        sampled_experiment::check_diagnostics(*c.preceding,stats.sample,input,shape);
        if(condition&&condition->legacy) {
            sampled_experiment::check_constructive_family(condition->preceding,*c.preceding,stats.sample,input);
            sampled_experiment::check_mechanism_family(condition->preceding,*c.preceding,stats.sample);
        }
    } else if(c.diagnostic) {
        check_robust(c,stats,input,shape);
        if(condition) check_new_witness(*condition,c,stats);
    }
    actual=input; c.timing.run(actual,nullptr);
    if(actual!=expected) throw std::runtime_error(std::string("nullptr mismatch: ")+c.timing.name);
    verified_outputs+=2;
    return stats;
}

std::vector<RobustStats> check_input(const std::vector<u64>& input) {
    auto expected=input; std::sort(expected.begin(),expected.end());
    const auto shape=sampled_experiment::input_shape(expected);
    std::vector<RobustStats> result;
    for(const auto& c:all_candidates()) if(!c.preceding)
        result.push_back(check_one(c,input,expected,shape));
    ++verified_inputs;
    return result;
}

template<bool Dense,bool Trim>
void check_forced_depth(const Candidate& c,const std::vector<u64>& input) {
    auto expected=input;std::sort(expected.begin(),expected.end());
    auto actual=input;RobustStats s;
    brc_robust_detail::robust_impl<Dense,Trim,true>(actual,&s,16);
    require(actual==expected,"forced depth instrumented output");
    check_robust(c,s,input,sampled_experiment::input_shape(expected),16);
    actual=input;
    brc_robust_detail::robust_impl<Dense,Trim,false>(actual,nullptr,16);
    require(actual==expected,"forced depth nullptr output");
    verified_outputs+=2;
}

void verify() {
    u64 exhaustive=0,lifted=0,random_cases=0,focused=0;
    constexpr std::array<u64,4> alphabet{0,1,MAX_VALUE-1,MAX_VALUE};
    // Finite exhaustive words plus lifts across the inherited small-sort cutoff.
    for(std::size_t length=0;length<=5;++length) {
        std::size_t count=std::size_t(1)<<(2*length);
        for(std::size_t code=0;code<count;++code) {
            std::vector<u64> word(length);auto x=code;
            for(auto& v:word){v=alphabet[x%4];x/=4;}
            check_input(word);++exhaustive;
            if(length) {
                std::vector<u64> large(257+length);
                for(std::size_t i=0;i<large.size();++i) large[i]=word[i%length];
                check_input(large);++lifted;
            }
        }
    }
    std::mt19937_64 rng(0x5645524946595231ull);
    for(std::size_t n:{std::size_t(0),std::size_t(1),std::size_t(2),std::size_t(255),
        std::size_t(256),std::size_t(257),std::size_t(511),std::size_t(512),std::size_t(1023),
        std::size_t(1024),std::size_t(1025),std::size_t(2048),std::size_t(8192),std::size_t(16384)}) {
        for(unsigned mode=0;mode<5;++mode) {
            std::vector<u64> a(n);
            for(auto& x:a) x=mode==0?rng():mode==1?MAX_VALUE-bounded(rng,8192)
                :mode==2?bounded(rng,4096):mode==3?
                (u64(1)<<48)+bounded(rng,20)*(u64(1)<<20)+bounded(rng,8):42;
            if(mode==4&&n>1){a.front()=0;a.back()=MAX_VALUE;}
            check_input(a);++random_cases;
        }
    }
    for(bool above:{false,true})for(bool top:{false,true}) {
        const auto stats=check_input(dense_witness(above,top));++focused;
        for(auto index:{0u,2u}) {
            const auto& r=stats[index].trace.front();
            require(r.dense_probe&&r.dense_accepted==!above&&r.dense_span==4096+unsigned(above),
                    "focused exact dense threshold");
        }
    }
    for(unsigned tails:{16u,17u}) {
        auto input=trim_witness(100000,tails,1000);
        const auto stats=check_input(input);++focused;
        for(auto index:{1u,2u}) {
            const auto& r=stats[index].trace.front();
            require(r.trim_attempted&&r.trim_layout_accepted==(tails==16),"trim 16 versus 17 ties");
            require(tails==16?r.trim_high<MAX_VALUE:r.trim_high==MAX_VALUE,
                    "trim upper rank inclusion");
            if(tails==16) require(r.core.spills==1000&&r.trimmed_cells<=800,
                                 "trim tails preserved in actual spills");
        }
    }
    for(std::size_t hidden:{std::size_t(4095),std::size_t(4096),std::size_t(4097)}) {
        const auto stats=check_input(trim_witness(8192,16,hidden));++focused;
        for(auto index:{1u,2u}) {
            const auto& r=stats[index].trace.front();
            require(r.trim_attempted&&r.trim_layout_accepted&&r.core.spills==hidden,
                    "trim actual half boundary multiplicity");
            require(r.core.path==(hidden<=4096?SamplePath::recursive_spill_merge
                                                :SamplePath::recursive_spill_radix),
                    "trim actual half boundary route");
        }
    }
    {
        const auto stats=check_input(trim_witness(100000,16,100,0,16,100));++focused;
        for(auto index:{1u,2u}) {
            const auto& r=stats[index].trace.front();
            require(r.trim_attempted&&r.trim_layout_accepted&&r.core.spills==200
                &&r.trim_low>0&&r.trim_high<MAX_VALUE,"two sided trim preserves both tails");
        }
    }
    {
        std::vector<u64> input(8192,42);
        const auto indices=brc_sampled_detail::sample_indices(input.size(),1024);
        for(std::size_t i=0;i<16;++i) input[indices[i]]=i%2?MAX_VALUE:MAX_VALUE-(u64(1)<<32);
        const auto stats=check_input(input);++focused;
        for(auto index:{1u,2u}) {
            const auto& r=stats[index].trace.front();
            require(r.trim_attempted&&r.trim_layout_accepted&&r.trim_low==42&&r.trim_high==42
                &&r.trim_included_samples==1008&&r.core.spills==16,
                    "actual trim to constant preserves nonsample values");
        }
    }
    {
        std::vector<u64> input(16384,42);const auto free=nonsampled_positions(input.size());
        input[free.front()]=0;input[free.back()]=MAX_VALUE;
        const auto stats=check_input(input);++focused;
        for(auto index:{0u,2u}) {
            const auto& r=stats[index].trace.front();
            require(r.dense_probe&&!r.dense_accepted&&r.dense_span==(u128(1)<<64)
                &&r.core.spills==2,"constant sample actual uint64 full span");
        }
    }
    {
        std::vector<u64> input(8192,42);
        for(auto index:nonsampled_positions(input.size()))input[index]=(u64(1)<<48)+index;
        const auto stats=check_input(input);++focused;
        for(auto index:{0u,1u,2u})require(stats[index].trace.front().core.path
            ==SamplePath::recursive_spill_radix&&stats[index].trace.front().core.spills==4097,
                "actual sampler hidden majority triggers original-layout spill cap");
    }
    {
        std::vector<u64> child(16384);
        for(std::size_t i=0;i<child.size();++i)child[i]=(u64(1)<<44)+i%4096;
        const auto stats=check_input(sampled_experiment::embed_hidden_child(32768,MAX_VALUE,child));++focused;
        for(auto index:{0u,2u}) require(stats[index].trace.size()==2
            &&stats[index].trace[1].dense_accepted,"independent dense route in child");
    }
    {
        const auto child=trim_witness(100000,16,100);
        const auto stats=check_input(sampled_experiment::embed_hidden_child(200000,0,child));++focused;
        for(auto index:{1u,2u})require(stats[index].trace.size()>=2
            &&stats[index].trace[1].trim_attempted&&stats[index].trace[1].trim_layout_accepted,
                "independent trimmed retry in child");
    }
    {
        auto input=trim_witness(100000,0,0);
        const auto indices=brc_sampled_detail::sample_indices(input.size(),1024);
        for(std::size_t j=8;j<=11;++j)
            input[indices[800+j]]=(u64(1)<<48)+j*(u64(1)<<20)+16384;
        const auto stats=check_input(input);++focused;
        for(auto index:{1u,2u})require(stats[index].trace.front().trim_attempted
            &&!stats[index].trace.front().trim_layout_accepted,
                "central contaminants survive global rank trim");
    }
    for(bool above:{false,true}) {
        check_input(sampled_experiment::cell_budget_witness(1024,above));++focused;
    }
    check_input(sampled_experiment::hidden_chain(131072,4,0,3));++focused;
    std::vector<u64> depth_input(500);for(auto& x:depth_input)x=rng();
    const auto& c=all_candidates();
    check_forced_depth<true,false>(c[15],depth_input);
    check_forced_depth<false,true>(c[16],depth_input);
    check_forced_depth<true,true>(c[17],depth_input);
    ++verified_inputs;++focused;
    for(const auto* path:{"trivial","small_std_sort","recursive_count","recursive_spill_merge",
        "recursive_cell_radix","recursive_spill_radix","recursive_depth_radix","dense_count",
        "trim_spill_merge","trim_cell_radix","trim_spill_radix"})
        if(!paths_seen.contains(path))throw std::runtime_error(std::string("declared robust route never exercised: ")+path);
    std::cout<<"{\"result\":\"PASS\",\"domain\":\"full uint64\",\"value_bytes\":"<<sizeof(u64)
        <<",\"algorithm_candidates\":"<<c.size()<<",\"new_variants_checked\":3,\"pdqsort_checked\":true"
        <<",\"verified_input_arrays\":"<<verified_inputs<<",\"verified_algorithm_outputs\":"<<verified_outputs
        <<",\"exhaustive_short_arrays\":"<<exhaustive<<",\"lifted_above_cutoff_arrays\":"<<lifted
        <<",\"random_boundary_arrays\":"<<random_cases<<",\"focused_cases\":"<<focused
        <<",\"paths_exercised\":"<<paths_seen.size()
        <<",\"dense_exact_and_one_above_checked\":true,\"full_span_overflow_checked\":true"
        <<",\"sample_actual_range_mismatch_checked\":true,\"trim_constant_checked\":true"
        <<",\"trim_rank_ties_checked\":true,\"trimmed_keys_preserved_checked\":true"
        <<",\"below_and_above_origin_checked\":true,\"trim_actual_half_boundary_checked\":true"
        <<",\"child_dense_and_trim_routes_checked\":true,\"central_contaminant_limit_checked\":true"
        <<",\"forced_depth_cap_checked\":true,\"trace_conservation_checked\":true"
        <<",\"geometric_work_bounds_checked\":true,\"instrumented_and_nullptr_checked\":true"
        <<",\"unchanged_root_divider_checks_reused\":true,\"fresh_heldout_banks_evaluated\":false}\n";
}

using Metrics=std::map<std::string,long double>;
Metrics metrics(const RobustStats& r) {
    const auto& s=r.sample;const auto& b=s.base;Metrics m;
#define ADD_BASE(name,field) m[name]=b.field
    ADD_BASE("roots",roots);ADD_BASE("predictions",predictions);ADD_BASE("direct_hits",direct);
    ADD_BASE("up_corrections",up);ADD_BASE("down_corrections",down);
    ADD_BASE("fallback_elements",fallback_elements);ADD_BASE("failed_predictions",failed_predictions);
    ADD_BASE("quotient_calls",quotient_calls);ADD_BASE("counter_cells",counter_cells);
    ADD_BASE("auxiliary_vector_bytes",auxiliary_vector_bytes);ADD_BASE("buckets",buckets);
    ADD_BASE("radix_passes",radix_passes);
#undef ADD_BASE
#define ADD_SAMPLE(field) m[#field]=s.field
    ADD_SAMPLE(sample_count);ADD_SAMPLE(learning_visits);ADD_SAMPLE(processed);ADD_SAMPLE(covered);
    ADD_SAMPLE(spills);ADD_SAMPLE(full_data_visits);ADD_SAMPLE(active_buckets);ADD_SAMPLE(shift);
    ADD_SAMPLE(origin);ADD_SAMPLE(counter_cells_demanded);ADD_SAMPLE(counter_cells_allocated);
    ADD_SAMPLE(sample_vector_bytes);ADD_SAMPLE(bucket_vector_bytes);ADD_SAMPLE(spill_vector_bytes);
    ADD_SAMPLE(recursive_nodes);ADD_SAMPLE(recursive_max_depth);ADD_SAMPLE(recursive_input_total);
    ADD_SAMPLE(recursive_sample_total);ADD_SAMPLE(recursive_processed_total);ADD_SAMPLE(recursive_spill_total);
    ADD_SAMPLE(recursive_counter_cells_total);ADD_SAMPLE(recursive_emitted_total);ADD_SAMPLE(recursive_merge_writes_total);
    ADD_SAMPLE(recursive_radix_leaves);ADD_SAMPLE(recursive_small_leaves);ADD_SAMPLE(recursive_trivial_leaves);
    ADD_SAMPLE(recursive_count_leaves);
#undef ADD_SAMPLE
#define ADD_ROBUST(field) m[#field]=r.field
    ADD_ROBUST(dense_probes);ADD_ROBUST(dense_accepts);ADD_ROBUST(dense_probe_visits_total);
    ADD_ROBUST(trim_attempts);ADD_ROBUST(trim_layout_accepts);ADD_ROBUST(trim_filter_visits_total);
    ADD_ROBUST(trim_selection_calls_total);ADD_ROBUST(sample_bounds_visits_total);ADD_ROBUST(learning_visits_total);
#undef ADD_ROBUST
    m["initial_bucket_slots_total"]=0;m["retried_bucket_slots_total"]=0;
    m["recursive_full_data_visits_total"]=0;
    for(const auto& node:r.sample.recursion_trace)m["recursive_full_data_visits_total"]+=node.full_data_visits;
    for(const auto& node:r.trace){m["initial_bucket_slots_total"]+=node.initial_bucket_slots;
        m["retried_bucket_slots_total"]+=node.retried_bucket_slots;}
    return m;
}

void write_node(std::ostream& out,const Condition& c,unsigned bank,const Candidate& a,
                const RobustNodeStats& r,bool extended) {
    const auto& q=r.core;
    out<<c.stage<<','<<c.original_stage<<','<<c.family<<','<<c.n<<','<<bank<<','<<a.timing.name
       <<','<<q.depth<<','<<q.input_size<<','<<q.sample_count<<','<<q.learning_visits
       <<','<<q.processed<<','<<q.covered<<','<<q.spills<<','<<q.full_data_visits
       <<','<<q.child_size<<','<<q.shift<<','<<q.origin<<','<<q.buckets<<','<<q.active_buckets
       <<','<<sampled_experiment::decimal128(q.counter_cells_demanded)<<','<<q.counter_cells_allocated
       <<','<<q.auxiliary_vector_bytes<<','<<q.radix_passes<<','<<q.emitted_values<<','<<q.merge_writes
       <<','<<(extended?robust_node_path_name(r):sample_path_name(q.path))<<','<<extended
       <<','<<r.sample_bounds_checked<<','<<r.dense_probe<<','<<r.dense_accepted
       <<','<<r.trim_attempted<<','<<r.trim_layout_accepted
       <<','<<r.sample_minimum<<','<<r.sample_maximum<<','<<sampled_experiment::decimal128(r.sample_span)
       <<','<<r.dense_minimum<<','<<r.dense_maximum<<','<<sampled_experiment::decimal128(r.dense_span)
       <<','<<sampled_experiment::decimal128(r.original_cells)<<','<<sampled_experiment::decimal128(r.trimmed_cells)
       <<','<<r.trim_cut<<','<<r.trim_low<<','<<r.trim_high<<','<<r.trim_included_samples
       <<','<<r.sample_bounds_visits<<','<<r.dense_probe_visits<<','<<r.trim_filter_visits
       <<','<<r.trim_selection_calls<<','<<r.initial_bucket_slots<<','<<r.retried_bucket_slots<<'\n';
}

std::string mix_string(const std::map<std::string,unsigned>& mix) {
    std::string result;for(const auto& [name,count]:mix){if(!result.empty())result+='|';
        result+=name+":"+std::to_string(count);}return result;
}

void benchmark_robust(const std::string& output_path,std::size_t max_n,double target_seconds,
                      const std::string& subset) {
    constexpr unsigned BANKS=8,ROUNDS=7;
    const auto& candidates=all_candidates();const auto A=candidates.size();
    require(target_seconds>0&&target_seconds<=1,"target_seconds must be in (0,1]");
    std::ofstream file(output_path),trace_file(output_path+".robust_nodes.csv");
    require(bool(file)&&bool(trace_file),"cannot open robust benchmark outputs");
    trace_file<<"stage,original_stage,family,n,bank,algorithm,depth,input_size,sample_count,learning_visits,"
        <<"processed,covered,spills,full_data_visits,child_size,shift,origin,buckets,active_buckets,"
        <<"counter_cells_demanded,counter_cells_allocated,auxiliary_vector_bytes,radix_passes,emitted_values,"
        <<"merge_writes,path,extended,sample_bounds_checked,dense_probe,dense_accepted,trim_attempted,"
        <<"trim_layout_accepted,sample_minimum,sample_maximum,sample_span,dense_minimum,dense_maximum,dense_span,"
        <<"original_cells,trimmed_cells,trim_cut,trim_low,trim_high,trim_included_samples,sample_bounds_visits,"
        <<"dense_probe_visits,trim_filter_visits,trim_selection_calls,initial_bucket_slots,retried_bucket_slots\n";
    const auto metric_names=metrics(RobustStats{});
    file<<"stage,original_stage,family,n,seed_regime,algorithm,value_bytes,banks,rounds,median_us,p10_us,p90_us,"
        <<"min_us,max_us,calls_per_round,mean_distinct,mean_min,mean_max,mean_numeric_span";
    for(const auto& [name,value]:metric_names)file<<','<<name;
    file<<",path,path_mix,terminal_path,terminal_path_mix";
    for(unsigned i=1;i<=ROUNDS;++i)file<<",round"<<i<<"_us";
    file<<'\n'<<std::setprecision(21);trace_file<<std::setprecision(21);
    u64 completed=0,rows=0,validated_banks=0,trace_nodes=0;
    for(const auto& condition:conditions()) {
        if(condition.n>max_n||!selected(condition,subset))continue;
        std::vector<std::vector<u64>> banks;
        for(unsigned bank=0;bank<BANKS;++bank)banks.push_back(input_bank(condition,bank));
        std::vector<std::vector<RobustStats>> diagnostics(A);
        long double distinct=0,minimum=0,maximum=0,span=0;
        for(unsigned bank=0;bank<BANKS;++bank) {
            const auto& input=banks[bank];auto expected=input;
            std::sort(expected.begin(),expected.end());const auto shape=sampled_experiment::input_shape(expected);
            distinct+=shape.distinct;minimum+=shape.minimum;maximum+=shape.maximum;span+=shape.span;
            for(std::size_t ai=0;ai<A;++ai) {
                auto stats=check_one(candidates[ai],input,expected,shape,&condition);
                if(!stats.trace.empty())for(const auto& node:stats.trace){write_node(trace_file,condition,bank,
                    candidates[ai],node,true);++trace_nodes;}
                else for(const auto& node:stats.sample.recursion_trace){RobustNodeStats r;r.core=node;
                    write_node(trace_file,condition,bank,candidates[ai],r,false);++trace_nodes;}
                diagnostics[ai].push_back(std::move(stats));
            }
            ++validated_banks;
        }
        // This is the preceding timer unchanged: includes input copy, all setup,
        // allocation, output consumption, and vector destruction on every call.
        std::vector<std::size_t> cycles(A),order(A);
        std::vector<std::vector<double>> timings(A);
        for(std::size_t ai=0;ai<A;++ai) {
            const double one=timed(candidates[ai].timing,banks,1,0);
            cycles[ai]=std::clamp<std::size_t>(std::size_t(target_seconds/std::max(one,1e-9)+.999),1,100000);
        }
        std::mt19937_64 order_rng(0x5A6D1EDB0E94005ull+condition.n+completed*31337);
        for(unsigned round=0;round<ROUNDS;++round) {
            std::iota(order.begin(),order.end(),0);
            std::shuffle(order.begin(),order.end(),order_rng);
            for(auto ai:order)timings[ai].push_back(timed(candidates[ai].timing,banks,cycles[ai],round)
                *1e6/(cycles[ai]*BANKS));
        }
        for(std::size_t ai=0;ai<A;++ai) {
            Metrics total;std::map<std::string,unsigned> paths,terminals;
            for(const auto& r:diagnostics[ai]) {
                for(const auto& [name,value]:metrics(r))total[name]+=value;
                ++paths[root_path(candidates[ai],r)];
                const std::string terminal=!r.trace.empty()?robust_node_path_name(r.trace.back())
                    :!r.sample.recursion_trace.empty()?sample_path_name(r.sample.recursion_trace.back().path)
                    :root_path(candidates[ai],r);
                ++terminals[terminal];
            }
            file<<condition.stage<<','<<condition.original_stage<<','<<condition.family<<','<<condition.n
                <<','<<condition.regime<<','<<candidates[ai].timing.name<<','<<sizeof(u64)<<','<<BANKS<<','<<ROUNDS
                <<','<<quantile(timings[ai],.5)<<','<<quantile(timings[ai],.1)<<','<<quantile(timings[ai],.9)
                <<','<<*std::min_element(timings[ai].begin(),timings[ai].end())
                <<','<<*std::max_element(timings[ai].begin(),timings[ai].end())<<','<<cycles[ai]*BANKS
                <<','<<distinct/BANKS<<','<<minimum/BANKS<<','<<maximum/BANKS<<','<<span/BANKS;
            for(const auto& [name,value]:metric_names)file<<','<<total[name]/BANKS;
            file<<','<<(paths.size()==1?paths.begin()->first:"mixed")<<','<<mix_string(paths)
                <<','<<(terminals.size()==1?terminals.begin()->first:"mixed")<<','<<mix_string(terminals);
            for(auto value:timings[ai])file<<','<<value;
            file<<'\n';++rows;
        }
        ++completed;file.flush();trace_file.flush();
        std::cerr<<"completed "<<condition.stage<<' '<<condition.family<<" n="<<condition.n<<'\n';
    }
    require(completed>0,"no selected benchmark conditions");
    std::cout<<"{\"result\":\"PASS\",\"conditions\":"<<completed<<",\"rows\":"<<rows
        <<",\"validated_input_banks\":"<<validated_banks<<",\"algorithms\":"<<A
        <<",\"banks\":"<<BANKS<<",\"rounds\":"<<ROUNDS<<",\"trace_nodes\":"<<trace_nodes
        <<",\"validated_algorithm_outputs\":"<<verified_outputs
        <<",\"target_seconds_per_algorithm_round\":"<<target_seconds
        <<",\"copy_setup_allocation_output_destruction_included\":true,\"observable_sink\":"<<observed<<"}\n";
}

} // namespace robust_experiment

int main(int argc,char** argv) {
    try {
        if(argc==2&&std::string_view(argv[1])=="--verify")robust_experiment::verify();
        else if(argc==2&&std::string_view(argv[1])=="--list") {
            std::cout<<"stage,original_stage,family,n,seed_regime\n";
            for(const auto& c:robust_experiment::conditions())std::cout<<c.stage<<','<<c.original_stage<<','
                <<c.family<<','<<c.n<<','<<c.regime<<'\n';
        } else if(argc>=3&&std::string_view(argv[1])=="--bench")
            robust_experiment::benchmark_robust(argv[2],argc>3?std::stoull(argv[3]):1000000,
                argc>4?std::stod(argv[4]):.012,argc>5?argv[5]:"all");
        else {
            std::cerr<<"usage: robust_bench --verify | --list | --bench output.csv "
                <<"[max_n=1000000] [target_seconds=.012] [subset=all]\n";return 2;
        }
    } catch(const std::exception& error){std::cerr<<error.what()<<'\n';return 1;}
    return 0;
}
