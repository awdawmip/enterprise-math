#pragma once
// Include after phase5/probe.hpp. All policies keep the fourth-round root.
enum class ChildMode {deep_gate, radix, range_radix};

namespace brc_child {
constexpr std::size_t count = 1024;
constexpr std::size_t table_size = 2*count;
static_assert((table_size & (table_size-1))==0);

inline bool deep_check(const std::vector<u64>& a, const brc_sampled_detail::SampledLayout& layout,
                       brc_probe::Engine& rng, ProbeRow& row) {
    const auto n=a.size(), eligible=n-brc_probe::sample_limit;
    row.threshold=std::size_t((u128(count)*(n/2)+eligible-1)/eligible)+42;
    std::array<std::size_t,table_size> picked;
    constexpr std::size_t empty=std::numeric_limits<std::size_t>::max();
    picked.fill(empty);
    std::uniform_int_distribution<std::size_t> draw(0,n-1);
    for(unsigned attempt=0;attempt<4*count && row.probes<count;++attempt) {
        const auto i=draw(rng);
        if(brc_probe::training_position(i,n)) continue;
        auto slot=std::size_t(i)&(table_size-1);
        while(picked[slot]!=empty && picked[slot]!=i) slot=(slot+1)&(table_size-1);
        if(picked[slot]==i) continue;
        picked[slot]=i;
        ++row.probes;
        row.misses+=!brc_probe::covered(a[i],layout);
    }
    return row.probes==count && row.misses>=row.threshold;
}

template<ChildMode Mode,bool Trace>
void run(std::vector<u64>& a, brc_probe::Engine& rng, unsigned depth, ProbeStats* stats) {
    const auto n=a.size();
    ProbeRow row{};
    row.n=n; row.depth=depth;
    std::size_t index=0;
    if constexpr(Trace) { index=stats->rows.size();stats->rows.emplace_back(); }
    const auto finish=[&]{ if constexpr(Trace) stats->rows[index]=row; };
    if(n<=brc_sampled_detail::SMALL_SORT_LIMIT) {
        std::sort(a.begin(),a.end());finish();return;
    }
    const bool large_child=depth>0 && n>=brc_probe::minimum_node;
    if(depth>=brc_sampled_detail::RECURSION_DEPTH_LIMIT) {
        offset_radix_impl<false>(a,nullptr);finish();return;
    }
    if constexpr(Mode!=ChildMode::deep_gate) {
        if(large_child) {
            bool sorted=false;
            if constexpr(Mode==ChildMode::range_radix) sorted=brc_probe::sort_narrow(a,row);
            if(!sorted) offset_radix_impl<false>(a,nullptr);
            finish();return;
        }
    }
    auto layout=brc_sampled_detail::learn_sampled<brc_probe::sample_limit,false>(a,nullptr);
    const auto bounds=std::minmax_element(layout.sample.begin(),layout.sample.end());
    const u64 low=*bounds.first, high=*bounds.second;
    const auto budget=brc_sampled_detail::cell_budget(n);
    AdaptiveNodeStats adaptive;
    SelectionNodeStats selection;
    CertifiedNodeStats certified;
    brc_robust_detail::select_compact_layout<false>(layout,low,high,layout.sample.size(),
                                                    budget,false,nullptr,&adaptive.core);
    if(!brc_certified_detail::select_certified_gap<false>(layout,budget,nullptr,adaptive,
                                            selection,certified,low,high)) {
        offset_radix_impl<false>(a,nullptr);finish();return;
    }
    row.model_selected=true;
    if constexpr(Trace) for(u64 x:a) row.actual_misses+=!brc_probe::covered(x,layout);
    if constexpr(Mode==ChildMode::deep_gate) {
        if(large_child && deep_check(a,layout,rng,row)) {
            row.early=true;offset_radix_impl<false>(a,nullptr);finish();return;
        }
    }
    brc_sampled_detail::assign_offsets(layout.buckets);
    row.counter_slots=std::size_t(layout.cells);
    std::vector<std::size_t> counts(row.counter_slots,0);
    std::vector<u64> spills;
    SampleStats visits;
    const bool success=brc_sampled_detail::count_sampled<Trace>(
        a,layout.grid,layout.buckets,counts,spills,brc_sampled_detail::recursive_spill_budget(n),&visits);
    if constexpr(Trace) row.scan_visits=visits.processed;
    if(success) {
        if(!spills.empty()) run<Mode,Trace>(spills,rng,depth+1,stats);
        brc_selection_detail::emit_fused(a,layout.buckets,counts,spills);
    } else offset_radix_impl<false>(a,nullptr);
    finish();
}
}
template<ChildMode Mode>
void child_sort(std::vector<u64>& a,u64 seed, ProbeStats* stats=nullptr) {
    brc_probe::Engine rng{seed};
    if(stats) brc_child::run<Mode,true>(a,rng,0,stats);
    else brc_child::run<Mode,false>(a,rng,0,nullptr);
}
