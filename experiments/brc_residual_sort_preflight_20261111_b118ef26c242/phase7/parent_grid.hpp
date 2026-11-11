#pragma once
// Include after phase6/child.hpp. Root predictions and exact contraction stay frozen.
namespace brc_inherited {
struct Span {
    u64 low=MAX_VALUE, high=0;
    std::size_t begin=0;
};

inline bool count_with_parent_grid(std::vector<u64>& a,
                                   const brc_sampled_detail::Grid& parent, ProbeRow& row) {
    const u64 first=parent.origin>>parent.shift;
    std::vector<Span> bands(parent.bucket_count);
    std::size_t used=0;
    Span* single=nullptr;
    for(u64 x:a) {
        ++row.range_visits;
        const u64 prefix=x>>parent.shift;
        if(prefix<first) return false;
        const u64 q=prefix-first;
        if(q>=bands.size()) return false;
        auto& b=bands[std::size_t(q)];
        if(b.low>b.high) { ++used; single=&b; }
        b.low=std::min(b.low,x);
        b.high=std::max(b.high,x);
    }
    const auto budget=std::min<std::size_t>(a.size(),COUNTER_CAP);
    std::size_t slots=0;
    for(auto& b:bands) {
        if(b.low>b.high) continue;
        const u128 width=u128(b.high)-b.low+1;
        if(width>budget-slots) return false;
        b.begin=slots;
        slots+=std::size_t(width);
    }
    row.range_sorted=true;
    if(used==1) {
        if(slots>1) {
            row.range_slots=slots;
            brc_robust_detail::dense_known_bounds<false>(a,single->low,slots,nullptr);
        }
        return true;
    }
    row.range_slots=slots;
    std::vector<std::size_t> counts(slots,0);
    for(u64 x:a) {
        const auto& b=bands[std::size_t((x>>parent.shift)-first)];
        ++counts[b.begin+std::size_t(x-b.low)];
    }
    auto out=a.begin();
    for(const auto& b:bands) {
        if(b.low>b.high) continue;
        const std::size_t width=std::size_t(b.high-b.low)+1;
        for(std::size_t j=0;j<width;++j) {
            const auto k=counts[b.begin+j];
            if(k) out=std::fill_n(out,k,b.low+j);
        }
    }
    return true;
}

template<bool Trace>
void run(std::vector<u64>& a,u64 seed,ProbeStats* stats) {
    // Below twice the child threshold, a successful root cannot yield a qualifying child.
    if(a.size()<2*brc_probe::minimum_node) {
        brc_probe::Engine rng{seed};
        brc_child::run<ChildMode::radix,Trace>(a,rng,0,stats);
        return;
    }
    ProbeRow root{};
    root.n=a.size();
    std::size_t root_index=0;
    if constexpr(Trace) {root_index=stats->rows.size();stats->rows.emplace_back();}
    const auto finish=[&]{if constexpr(Trace) stats->rows[root_index]=root;};
    auto layout=brc_sampled_detail::learn_sampled<1024,false>(a,nullptr);
    const auto bounds=std::minmax_element(layout.sample.begin(),layout.sample.end());
    const u64 low=*bounds.first,high=*bounds.second;
    const auto budget=brc_sampled_detail::cell_budget(a.size());
    AdaptiveNodeStats adaptive;
    SelectionNodeStats selection;
    CertifiedNodeStats certified;
    brc_robust_detail::select_compact_layout<false>(layout,low,high,layout.sample.size(),
                                                    budget,false,nullptr,&adaptive.core);
    if(!brc_certified_detail::select_certified_gap<false>(layout,budget,nullptr,adaptive,
                                            selection,certified,low,high)) {
        offset_radix_impl<false>(a,nullptr);finish();return;
    }
    root.model_selected=true;
    if constexpr(Trace) for(u64 x:a) root.actual_misses+=!brc_probe::covered(x,layout);
    brc_sampled_detail::assign_offsets(layout.buckets);
    root.counter_slots=std::size_t(layout.cells);
    std::vector<std::size_t> counts(root.counter_slots,0);
    std::vector<u64> spills;
    SampleStats visits;
    const bool success=brc_sampled_detail::count_sampled<Trace>(a,layout.grid,layout.buckets,
        counts,spills,brc_sampled_detail::recursive_spill_budget(a.size()),&visits);
    if constexpr(Trace) root.scan_visits=visits.processed;
    if(!success) { offset_radix_impl<false>(a,nullptr);finish();return; }
    if(spills.size()>=brc_probe::minimum_node) {
        ProbeRow child{};
        child.n=spills.size();child.depth=1;
        if(!count_with_parent_grid(spills,layout.grid,child)) offset_radix_impl<false>(spills,nullptr);
        if constexpr(Trace) stats->rows.push_back(child);
    } else if(!spills.empty()) {
        brc_probe::Engine rng{seed};
        brc_child::run<ChildMode::radix,Trace>(spills,rng,1,stats);
    }
    brc_selection_detail::emit_fused(a,layout.buckets,counts,spills);
    finish();
}
}
inline void parent_grid_sort(std::vector<u64>& a,u64 seed,ProbeStats* stats=nullptr) {
    if(stats) brc_inherited::run<true>(a,seed,stats);
    else brc_inherited::run<false>(a,seed,nullptr);
}
