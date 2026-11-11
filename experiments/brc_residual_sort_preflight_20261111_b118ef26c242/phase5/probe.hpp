#pragma once

// Include after the frozen fourth-round certified kernel.
enum class ProbeMode { gate, gate_range, child_range, observe };
struct ProbeRow {
    unsigned depth{};
    std::size_t n{}, probes{}, misses{}, actual_misses{}, scan_visits{};
    std::size_t range_slots{}, counter_slots{}, threshold{}, range_visits{};
    bool model_selected{}, early{}, range_sorted{};
};
struct ProbeStats { std::vector<ProbeRow> rows; };

namespace brc_probe {
constexpr std::size_t minimum_node = 16384;
constexpr std::size_t probe_size = 64;
constexpr std::size_t margin = 13;
constexpr std::size_t sample_limit = brc_robust_detail::SAMPLE_LIMIT;
static_assert(sample_limit == 1024);

// Invert the frozen learner's contiguous strata. Its j-th stratum begins at
// floor(j*n/s). SplitMix allows its j-th draw to be evaluated directly.
inline bool training_position(std::size_t i, std::size_t n) {
    constexpr std::size_t s = sample_limit;
    const std::size_t j = std::size_t(((u128(i) + 1) * s - 1) / n);
    const std::size_t begin = std::size_t(u128(j) * n / s);
    const std::size_t end = std::size_t(u128(j + 1) * n / s);
    u64 state = (0xB0E9400520261108ull ^ u64(n) ^ (u64(s) * 0xd1b54a32d192ed03ull))
              + u64(j) * 0x9e3779b97f4a7c15ull;
    return i == begin + std::size_t((u128(brc_sampled_detail::next_mixed(state)) * (end-begin)) >> 64);
}

inline bool covered(u64 x, const brc_sampled_detail::SampledLayout& layout) {
    if (x < layout.grid.origin) return false;
    const u64 q = (x - layout.grid.origin) >> layout.grid.shift;
    if (q >= layout.buckets.size()) return false;
    const auto& b = layout.buckets[std::size_t(q)];
    return x - b.low < b.width;
}

struct Engine {
    using result_type = u64;
    u64 state;
    static constexpr u64 min() { return 0; }
    static constexpr u64 max() { return std::numeric_limits<u64>::max(); }
    u64 operator()() { return brc_sampled_detail::next_mixed(state); }
};

inline std::size_t rejection_threshold(std::size_t n) {
    const std::size_t eligible = n - sample_limit;
    return std::size_t((u128(probe_size) * (n / 2) + eligible - 1) / eligible) + margin;
}

inline bool precheck(const std::vector<u64>& a, const brc_sampled_detail::SampledLayout& layout,
                     Engine& rng, ProbeRow& row) {
    std::uniform_int_distribution<std::size_t> draw(0, a.size() - 1);
    std::array<std::size_t, probe_size> picked;
    row.threshold = rejection_threshold(a.size());
    // A capped rejection sampler avoids long rejection sequences. At the cap,
    // keep the existing full-scan route. The cap can only suppress a rejection.
    for (unsigned attempt = 0; attempt < 4 * probe_size && row.probes < probe_size; ++attempt) {
        const auto i = draw(rng);
        if (training_position(i, a.size())) continue;
        const auto end = picked.begin() + row.probes;
        if (std::find(picked.begin(), end, i) != end) continue;
        picked[row.probes++] = i;
        row.misses += !covered(a[i], layout);
    }
    return row.probes == probe_size && row.misses >= row.threshold;
}

inline bool sort_narrow(std::vector<u64>& a, ProbeRow& row) {
    const auto [lo, hi] = std::minmax_element(a.begin(),a.end());
    const u64 low = *lo;
    const u128 width = u128(*hi) - low + 1;
    row.range_visits = a.size();
    if (width > std::min<std::size_t>(a.size(),COUNTER_CAP)) return false;
    row.range_sorted = true;
    if (width > 1) {
        row.range_slots = std::size_t(width);
        brc_robust_detail::dense_known_bounds<false>(a, low, row.range_slots, nullptr);
    }
    return true;
}

template<ProbeMode Mode, bool Trace>
void run(std::vector<u64>& a, Engine& rng, unsigned depth, ProbeStats* stats) {
    const std::size_t n = a.size();
    ProbeRow row{};
    row.depth = depth;
    row.n = n;
    std::size_t index = 0;
    if constexpr (Trace) { index = stats->rows.size(); stats->rows.emplace_back(); }
    const auto finish = [&] { if constexpr (Trace) stats->rows[index] = row; };
    if (n <= brc_sampled_detail::SMALL_SORT_LIMIT) {
        std::sort(a.begin(), a.end());
        finish(); return;
    }
    if (depth >= brc_sampled_detail::RECURSION_DEPTH_LIMIT) {
        offset_radix_impl<false>(a,nullptr);
        finish(); return;
    }
    if constexpr (Mode == ProbeMode::child_range) {
        if (depth && n >= minimum_node && sort_narrow(a,row)) { finish(); return; }
    }
    auto layout = brc_sampled_detail::learn_sampled<sample_limit,false>(a,nullptr);
    const auto bounds = std::minmax_element(layout.sample.begin(),layout.sample.end());
    const u64 low = *bounds.first, high = *bounds.second;
    const auto budget = brc_sampled_detail::cell_budget(n);
    AdaptiveNodeStats adaptive;
    SelectionNodeStats selection;
    CertifiedNodeStats certified;
    brc_robust_detail::select_compact_layout<false>(layout,low,high,layout.sample.size(),budget,
                                                     false,nullptr,&adaptive.core);
    if (!brc_certified_detail::select_certified_gap<false>(layout,budget,nullptr,
                                             adaptive,selection,certified,low,high)) {
        offset_radix_impl<false>(a,nullptr);
        finish(); return;
    }
    row.model_selected = true;
    if constexpr (Trace) {
        for (u64 x : a) row.actual_misses += !covered(x,layout);
    }
    if constexpr (Mode != ProbeMode::child_range) {
        if (n >= minimum_node) row.early = precheck(a,layout,rng,row);
        if constexpr (Mode != ProbeMode::observe) {
            if (row.early) {
                bool sorted = false;
                if constexpr (Mode == ProbeMode::gate_range) sorted = sort_narrow(a,row);
                if (!sorted) offset_radix_impl<false>(a,nullptr);
                finish(); return;
            }
        }
    }
    brc_sampled_detail::assign_offsets(layout.buckets);
    row.counter_slots = std::size_t(layout.cells);
    std::vector<std::size_t> counts(row.counter_slots,0);
    std::vector<u64> spills;
    SampleStats visits;
    const bool success = brc_sampled_detail::count_sampled<Trace>(
        a,layout.grid,layout.buckets,counts,spills,brc_sampled_detail::recursive_spill_budget(n), &visits);
    if constexpr (Trace) row.scan_visits = visits.processed;
    if (success) {
        if (!spills.empty()) run<Mode,Trace>(spills,rng,depth+1,stats);
        brc_selection_detail::emit_fused(a,layout.buckets,counts,spills);
    } else offset_radix_impl<false>(a,nullptr);
    finish();
}
} // namespace brc_probe

template<ProbeMode Mode>
void probe_sort(std::vector<u64>& a, u64 seed, ProbeStats* stats=nullptr) {
    brc_probe::Engine rng{seed};
    if (stats) brc_probe::run<Mode,true>(a,rng,0,stats);
    else brc_probe::run<Mode,false>(a,rng,0,nullptr);
}
