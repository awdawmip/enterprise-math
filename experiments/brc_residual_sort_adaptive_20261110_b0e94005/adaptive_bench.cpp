// Phase two: fixed adaptation of the preceding robust policies. The preceding
// twenty implementations, generators and timer are included without source edits.
#ifndef BRC_ROBUST_SOURCE
#define BRC_ROBUST_SOURCE "build/robust_frozen_include.hpp"
#endif
#include BRC_ROBUST_SOURCE
#include "adaptive_kernels.hpp"

namespace adaptive_experiment {

template<void (*Function)(std::vector<u64>&,AdaptiveStats*)>
void time_adaptive(std::vector<u64>& values,Stats*) {Function(values,nullptr);}

struct Candidate {
    Algorithm timing;
    const robust_experiment::Candidate* preceding=nullptr;
    void (*diagnostic)(std::vector<u64>&,AdaptiveStats*)=nullptr;
    bool ladder=false,prune=false;
};

const std::vector<Candidate>& candidates() {
    static const auto result=[] {
        std::vector<Candidate> out;
        for(const auto& c:robust_experiment::all_candidates())out.push_back({c.timing,&c});
        out.push_back({{"adaptive_trim_1024",time_adaptive<adaptive_trim_1024>},nullptr,
                       adaptive_trim_1024,true,false});
        out.push_back({{"adaptive_prune_1024",time_adaptive<adaptive_prune_1024>},nullptr,
                       adaptive_prune_1024,false,true});
        out.push_back({{"adaptive_combined_1024",time_adaptive<adaptive_combined_1024>},nullptr,
                       adaptive_combined_1024,true,true});
        return out;
    }();return result;
}

enum class Mechanism {none,central_poison,budget_plus_one,mass_reject,hidden_majority};
struct Condition {
    robust_experiment::Condition source;
    std::string family,stage,original_stage,regime;
    std::size_t n=0;
    Mechanism mechanism=Mechanism::none;
    bool phase_one=false;
    u64 large_tail_per_100000=0;
};

std::vector<Condition> conditions() {
    const auto old=robust_experiment::conditions();
    std::vector<Condition> out;
    const auto find=[&](const std::string& name)->robust_experiment::Condition {
        for(const auto& c:old)if(c.family==name)return c;
        throw std::runtime_error("missing frozen condition: "+name);
    };
    for(const auto* name:{"fresh_tail_2pct_high","fresh_tail_5pct_both",
        "fresh_interior_contamination","fresh_dense8192_0p3pct_extremes","rare_far_cluster",
        "fresh_uniform_uint64","fresh_narrow_offsets","fresh_128clusters_0p3pct_tail"}) {
        const auto c=find(name);out.push_back({c,c.family,"calibration","phase1_"+c.stage,
            "exact_previously_measured_phase1_banks",c.n,Mechanism::none,true});
    }
    const auto fresh=[&](const char* name,const char* prototype,u64 tag,u64 rate=0,
                         bool both=false,u64 large_rate=0,std::size_t n_override=0) {
        auto c=find(prototype);c.family=name;c.tag=0x4144415000000000ull+tag;
        if(n_override)c.n=n_override;
        c.stage="heldout";c.original_stage="new_phase2";
        if(c.kind==robust_experiment::NewKind::contamination) {
            c.contamination_per_100000=rate;c.two_sided=both;
        }
        out.push_back({c,name,"heldout","new_phase2","independent_adaptive_v1_seed_tags",
                       c.n,Mechanism::none,false,large_rate});
    };
    // All twelve are fresh input banks, not conceptually unseen distributions.
    fresh("adaptive_fresh_narrow_offsets","fresh_narrow_offsets",501,0,false,0,1000000);
    fresh("adaptive_fresh_tail_2p5pct_high","fresh_tail_2pct_high",502,2500,false,0,1000000);
    fresh("adaptive_fresh_tail_7pct_high","fresh_tail_2pct_high",503,7000);
    fresh("adaptive_fresh_tail_20pct_high","fresh_tail_2pct_high",504,20000);
    fresh("adaptive_fresh_tail_30pct_high","fresh_tail_2pct_high",505,30000);
    fresh("adaptive_fresh_tail_12pct_both","fresh_tail_5pct_both",506,12000,true);
    fresh("adaptive_fresh_tail_40pct_both","fresh_tail_5pct_both",507,40000,true);
    fresh("adaptive_fresh_dense8192_extremes","fresh_dense8192_0p3pct_extremes",508);
    fresh("adaptive_fresh_interior_contamination","fresh_interior_contamination",509);
    fresh("adaptive_fresh_heterogeneous_widths","fresh_heterogeneous_widths",510);
    fresh("adaptive_fresh_uniform_uint64","fresh_uniform_uint64",511,0,false,0,1000000);
    fresh("adaptive_fresh_128clusters_8pct_tail","fresh_128clusters_0p3pct_tail",512,0,false,8000);
    const auto mechanism=[&](const char* name,std::size_t n,Mechanism kind) {
        Condition c;c.family=name;c.stage="mechanism";c.original_stage="new_phase2";
        c.regime="constructed_actual_sampler_positions";c.n=n;c.mechanism=kind;out.push_back(c);
    };
    mechanism("witness_central4_poison_prune",100000,Mechanism::central_poison);
    mechanism("witness_original_cells_plus_one",8192,Mechanism::budget_plus_one);
    mechanism("witness_prune_sample_mass_reject",100000,Mechanism::mass_reject);
    mechanism("witness_pruned_actual_majority_reject",100000,Mechanism::hidden_majority);
    require(out.size()==24,"adaptive matrix must contain24 conditions");return out;
}

bool selected(const Condition& c,const std::string& subset) {
    if(subset.empty()||subset=="all")return true;
    if(subset=="evaluation"||subset=="heldout")return c.stage=="heldout";
    if(subset=="calibration"||subset=="mechanism")return c.stage==subset;
    return c.family.find(subset)!=std::string::npos;
}

std::vector<u64> central_poison(std::size_t n,unsigned bank=0,bool hidden=false) {
    auto input=robust_experiment::trim_witness(n,0,0,bank);
    const auto indices=brc_sampled_detail::sample_indices(n,1024);
    const u64 origin=(u64(1)<<48)+u64(bank)*(u64(1)<<30);
    for(std::size_t j=8;j<=11;++j)input[indices[800+j]]=origin+j*(u64(1)<<20)+16384;
    if(hidden)for(auto i:robust_experiment::nonsampled_positions(n))
        input[i]=origin+(u64(8)<<20);
    return input;
}

std::vector<u64> input_bank(const Condition& c,unsigned bank) {
    switch(c.mechanism) {
    case Mechanism::central_poison:return central_poison(c.n,bank);
    case Mechanism::budget_plus_one:return sampled_experiment::cell_budget_witness(1024,true);
    case Mechanism::mass_reject:return robust_experiment::trim_witness(c.n,17,1000,bank);
    case Mechanism::hidden_majority:return central_poison(c.n,bank,true);
    default:break;
    }
    if(!c.large_tail_per_100000)return robust_experiment::input_bank(c.source,bank);
    // Independent phase-two stream; exact far-tail multiplicity, then shuffle.
    std::mt19937_64 rng(0x41444150545F5631ull^(u64(c.n)*0x9e3779b97f4a7c15ull)
        ^(u64(bank)*0xD1B54A32D192ED03ull)^(c.source.tag*0x94D049BB133111EBull));
    std::vector<u64> input(c.n);
    for(auto& x:input)x=(u64(1)<<56)+bounded(rng,128)*(u64(1)<<25)+bounded(rng,8);
    for(std::size_t i=0;i<c.n*c.large_tail_per_100000/100000;++i)
        input[i]=(u64(1)<<60)+bounded(rng,8);
    std::shuffle(input.begin(),input.end(),rng);return input;
}

struct RootOracle {
    brc_sampled_detail::Grid grid{};
    std::vector<brc_sampled_detail::Bucket> bins;
    u128 cells=0;
    u64 included=0,omitted_bins=0,omitted_samples=0;
    u128 omitted_cells=0;
};

RootOracle reconstruct(const std::vector<u64>& sample,u64 low,u64 high) {
    RootOracle o;o.grid=brc_sampled_detail::make_grid(low,high);o.bins.resize(o.grid.bucket_count);
    for(u64 x:sample)if(x>=low&&x<=high) {
        o.bins[std::size_t((x-o.grid.origin)>>o.grid.shift)].observe(x);++o.included;
    }
    o.cells=brc_sampled_detail::finish_layout(o.bins,o.grid,true);return o;
}

void oracle_prune(RootOracle& o,std::size_t budget) {
    std::vector<std::size_t> order;
    for(std::size_t i=0;i<o.bins.size();++i)if(o.bins[i].width)order.push_back(i);
    std::sort(order.begin(),order.end(),[&](auto a,auto b) {
        return o.bins[a].width!=o.bins[b].width?o.bins[a].width>o.bins[b].width:a<b;
    });
    for(auto index:order) {
        if(o.cells<=budget)break;
        auto& bin=o.bins[index];o.cells-=bin.width;o.omitted_cells+=bin.width;
        o.omitted_samples+=bin.samples;++o.omitted_bins;bin.width=0;
    }
}

void check_actual_membership(const std::vector<u64>& input,const AdaptiveNodeStats& node,
                             const std::vector<u64>& sample) {
    const auto& r=node.core;const auto& q=r.core;
    if(!q.counter_cells_allocated)return;
    RootOracle o;
    if(r.compact_accepted) {
        o.grid={r.compact_low,unsigned(std::bit_width(r.compact_width-1)),1};
        o.bins.resize(1);o.bins[0].low=r.compact_low;o.bins[0].width=r.compact_width;
    } else {
        const auto low=node.selected_attempt?r.trim_low:r.sample_minimum;
        const auto high=node.selected_attempt?r.trim_high:r.sample_maximum;
        o=reconstruct(sample,low,high);
        if(node.prune_accepted)oracle_prune(o,brc_sampled_detail::cell_budget(input.size()));
    }
    require(q.origin==o.grid.origin&&q.shift==o.grid.shift,"selected model root geometry oracle");
    u64 processed=0,covered=0,spills=0;
    // An independent membership expression checks omitted bins and below-origin
    // values without calling the kernel's membership/count routine.
    for(u64 x:input) {
        bool hit=false;
        if(x>=o.grid.origin) {
            const u64 bin=(x-o.grid.origin)>>o.grid.shift;
            if(bin<o.bins.size()) {
                const auto& b=o.bins[bin];
                hit=b.width&&x>=b.low&&u128(x)<u128(b.low)+b.width;
            }
        }
        ++processed;if(hit)++covered;else ++spills;
        if(spills>input.size()/2)break;
    }
    require(q.processed==processed&&q.covered==covered&&q.spills==spills,
            "selected model actual prefix membership oracle");
}

std::set<std::string> paths_seen;
u64 checked_inputs=0,checked_outputs=0;

void check_adaptive(const Candidate& candidate,const AdaptiveStats& stats,
                     const std::vector<u64>& input,unsigned starting_depth=0) {
    const auto& robust=stats.robust;const auto& summary=robust.sample;
    require(!stats.trace.empty()&&stats.trace.size()==robust.trace.size()
        &&stats.trace.size()==summary.recursion_trace.size(),"adaptive aligned traces");
    const auto& root=stats.trace.front().core.core;
    require(root.input_size==input.size()&&root.depth==starting_depth&&root.path==summary.path
        &&root.sample_count==summary.sample_count&&root.learning_visits==summary.learning_visits
        &&root.processed==summary.processed&&root.covered==summary.covered&&root.spills==summary.spills
        &&root.counter_cells_demanded==summary.counter_cells_demanded
        &&root.counter_cells_allocated==summary.counter_cells_allocated,"adaptive root fields");
    u64 inputs=0,samples=0,processed=0,spills=0,cells=0,emitted=0,merged=0;
    u64 radix=0,small=0,trivial=0,counted=0,branches=0,learning=0,bounds=0,filters=0,selections=0;
    u64 trim_nodes=0,trim_layouts=0,compact_attempts=0,compact_accepts=0,compact_trim=0,compact_cells=0;
    u64 ladder_attempts=0,prune_attempts=0,prune_accepts=0,mass_rejects=0,spill_failures=0;
    u64 omitted_bins=0,omitted_samples=0,order_entries=0,order_peak=0;u128 omitted_cells=0;
    for(std::size_t i=0;i<stats.trace.size();++i) {
        const auto& node=stats.trace[i];const auto& r=node.core;const auto& q=r.core;
        const auto& mirror=robust.trace[i];const auto& simple=summary.recursion_trace[i];
        const auto budget=brc_sampled_detail::cell_budget(q.input_size);
        const bool early=q.path==SamplePath::trivial||q.path==SamplePath::small_std_sort
            ||q.path==SamplePath::recursive_depth_radix;
        paths_seen.insert(adaptive_node_path_name(node));
        require(q.depth==starting_depth+i&&q.depth<=16&&q.input_size==simple.input_size
            &&q.path==simple.path&&q.processed==simple.processed
            &&q.counter_cells_demanded==simple.counter_cells_demanded
            &&r.trim_cut==mirror.trim_cut&&r.compact_width==mirror.compact_width,"adaptive trace alignment");
        require(q.processed==q.covered+q.spills&&q.processed<=q.input_size
            &&q.full_data_visits==q.processed,"adaptive conservation and input visits");
        require(q.sample_count==(early?0:std::min<u64>(q.input_size,1024))
            &&q.counter_cells_allocated<=budget&&q.shift<=54,"adaptive sample and allocation caps");
        require(!r.dense_probe&&!r.dense_accepted&&!r.dense_probe_visits,"adaptive has no dense minmax scan");
        require(r.sample_bounds_checked==!early&&r.sample_bounds_visits==q.sample_count
            &&r.compact_attempted==!early,"adaptive original sample bounds work");
        if(!early)require(r.sample_minimum<=r.sample_maximum
            &&r.sample_span==u128(r.sample_maximum)-r.sample_minimum+1,"adaptive exact sample span");
        const auto count=node.attempts.size();
        require(count<=(candidate.ladder?3u:1u),"bounded adaptive ladder");
        require(r.trim_attempted==(count>0)&&r.trim_filter_visits==count*q.sample_count
            &&r.trim_selection_calls==2*count&&r.compact_attempts==(early?0:1+count),
                "adaptive bounded retry work");
        if(count)require(r.original_cells>budget&&r.sample_span>budget,
                         "adaptive retry only after original grid and compact rejection");
        u64 observations=q.sample_count;const AdaptiveAttemptStats* chosen=nullptr;
        for(std::size_t j=0;j<count;++j) {
            const auto& a=node.attempts[j];const u64 denominator=j==0?64:j==1?16:4;
            require(a.cut==q.sample_count/denominator&&a.low<=a.high
                &&a.included_samples>=q.sample_count-2*a.cut&&a.included_samples<=q.sample_count,
                    "adaptive rank and inclusive tie policy");
            require(a.grid_accepted==(a.trimmed_cells<=budget)
                &&a.compact_selected==(u128(a.high)-a.low+1<=budget),"adaptive attempt eligibility");
            require(a.prune_attempted==(candidate.prune&&!a.grid_accepted&&!a.compact_selected),
                    "prune only rejected quantile layouts");
            require(a.retained_cells+a.omitted_cells==a.trimmed_cells
                &&a.retained_samples+a.omitted_samples==a.included_samples,
                    "pruning proposal cells and learning mass conserve");
            if(a.prune_attempted) {
                require(a.omitted_bins>0&&a.omitted_bins<=a.prune_order_size
                    &&a.prune_order_size<=a.bucket_slots&&a.omitted_samples>=a.omitted_bins
                    &&a.retained_cells<=budget
                    &&a.prune_order_vector_bytes>=a.prune_order_size*sizeof(std::size_t),
                        "pruning complete proposal fits cells");
                require(a.prune_mass_ok==(2*a.retained_samples>=q.sample_count)
                    &&a.prune_selected==a.prune_mass_ok,"pruning original sample mass gate");
            } else require(!a.omitted_bins&&!a.omitted_samples&&!a.omitted_cells
                &&!a.prune_order_size&&!a.prune_order_vector_bytes&&!a.prune_selected,
                    "absent pruning has no proposal work");
            require(a.selected==(a.grid_accepted||a.compact_selected||a.prune_selected),
                    "first feasible adaptive model");
            if(a.selected){require(j+1==count,"no attempts after model selection");chosen=&a;}
            observations+=a.included_samples;++ladder_attempts;
            prune_attempts+=a.prune_attempted;mass_rejects+=a.prune_attempted&&!a.prune_mass_ok;
            order_entries+=a.prune_order_size;order_peak=std::max(order_peak,a.prune_order_vector_bytes);
        }
        require(q.learning_visits==observations,"all adaptive learning visits charged");
        if(count) {
            const auto& last=node.attempts.back();
            require(r.trim_cut==last.cut&&r.trim_low==last.low&&r.trim_high==last.high
                &&r.trim_included_samples==last.included_samples&&r.trimmed_cells==last.trimmed_cells
                &&r.trim_layout_accepted==last.grid_accepted,"core trim fields describe final attempt");
        }
        const bool model=q.counter_cells_allocated>0;
        require(node.selected_attempt==(chosen?count:0)&&node.chosen_cut==(chosen?chosen->cut:0),
                "selected attempt provenance");
        require(node.prune_accepted==(chosen&&chosen->prune_selected)
            &&node.actual_spill_failure==(q.path==SamplePath::recursive_spill_radix),
                "pruning selection is separate from actual scan failure");
        const bool final_mass_reject=count&&!chosen&&node.attempts.back().prune_attempted
            &&!node.attempts.back().prune_mass_ok;
        require(node.selection_rejected_by_mass==final_mass_reject,"final mass rejection flag");
        if(model) {
            const u64 mass=chosen?(chosen->prune_selected?chosen->retained_samples:chosen->included_samples)
                :q.sample_count;
            require(node.selected_learning_samples==mass&&2*mass>=q.sample_count,
                    "selected model retained learning mass");
            const u128 demand=r.compact_accepted?r.compact_width:chosen?
                (chosen->prune_selected?chosen->retained_cells:chosen->trimmed_cells):r.original_cells;
            require(q.counter_cells_demanded==demand&&q.counter_cells_allocated==demand,
                    "selected model exact counter demand");
        } else require(!node.selected_learning_samples&&!chosen,"no selected mass on layout rejection");
        if(node.prune_accepted)require(node.omitted_bins==chosen->omitted_bins
            &&node.omitted_samples==chosen->omitted_samples&&node.omitted_cells==chosen->omitted_cells,
                "selected omission record");
        else require(!node.omitted_bins&&!node.omitted_samples&&!node.omitted_cells,
                     "unselected proposal is not committed");
        require(r.compact_accepted==(!early&&(r.sample_span<=budget||(chosen&&chosen->compact_selected))),
                "adaptive compact selected eligibility");
        if(r.compact_accepted) {
            const auto low=chosen?chosen->low:r.sample_minimum,high=chosen?chosen->high:r.sample_maximum;
            const u128 padding=std::max<u128>(8,4*(u128(high)-low+1)/(q.sample_count+1));
            require(r.compact_from_trim==bool(chosen)&&r.compact_low<=low&&r.compact_high>=high
                &&u128(low)-r.compact_low<=padding&&u128(r.compact_high)-high<=padding
                &&u128(r.compact_width)==u128(r.compact_high)-r.compact_low+1,
                    "adaptive compact padding and provenance");
        }
        switch(q.path) {
        case SamplePath::recursive_spill_merge:
            require(q.processed==q.input_size&&q.spills>0&&q.spills<=q.input_size/2
                &&q.child_size==q.spills&&q.emitted_values==q.covered
                &&q.merge_writes>=q.spills&&q.merge_writes<=q.input_size,"adaptive actual child contraction");
            ++branches;break;
        case SamplePath::recursive_count:
            require(q.processed==q.input_size&&q.covered==q.input_size&&!q.spills
                &&q.emitted_values==q.input_size&&!q.merge_writes,"adaptive count leaf");++counted;break;
        case SamplePath::recursive_cell_radix:
            require(q.counter_cells_demanded>budget&&!model&&!q.processed
                &&count==(candidate.ladder?3u:1u),"adaptive all layout attempts exhausted");++radix;break;
        case SamplePath::recursive_spill_radix:
            require(q.spills==q.input_size/2+1&&model,"adaptive actual spill abort boundary");++radix;break;
        case SamplePath::recursive_depth_radix:
            require(q.depth==16&&q.input_size>256,"adaptive forced depth leaf");++radix;break;
        case SamplePath::small_std_sort:
            require(q.input_size>=2&&q.input_size<=256,"adaptive small leaf");++small;break;
        case SamplePath::trivial:require(q.input_size<2,"adaptive trivial leaf");++trivial;break;
        default:throw std::runtime_error("unexpected adaptive core path");
        }
        if(q.path==SamplePath::recursive_spill_merge)
            require(i+1<stats.trace.size()&&stats.trace[i+1].core.core.input_size==q.child_size,
                    "adaptive exact retained child");
        else {
            require(!q.child_size&&i+1==stats.trace.size(),"adaptive single terminal");
            if(q.path!=SamplePath::recursive_count)require(!q.emitted_values&&!q.merge_writes,
                "fallback writes excluded from counted outputs");
        }
        inputs+=q.input_size;samples+=q.sample_count;processed+=q.processed;spills+=q.spills;
        cells+=q.counter_cells_allocated;emitted+=q.emitted_values;merged+=q.merge_writes;
        learning+=q.learning_visits;bounds+=r.sample_bounds_visits;filters+=r.trim_filter_visits;
        selections+=r.trim_selection_calls;trim_nodes+=r.trim_attempted;trim_layouts+=r.trim_layout_accepted;
        compact_attempts+=r.compact_attempts;compact_accepts+=r.compact_accepted;
        compact_trim+=r.compact_from_trim;compact_cells+=r.compact_width;
        prune_accepts+=node.prune_accepted;spill_failures+=node.actual_spill_failure;
        omitted_bins+=node.omitted_bins;omitted_samples+=node.omitted_samples;omitted_cells+=node.omitted_cells;
    }
    require(summary.recursive_nodes==stats.trace.size()&&summary.recursive_input_total==inputs
        &&summary.recursive_sample_total==samples&&summary.recursive_processed_total==processed
        &&summary.recursive_spill_total==spills&&summary.recursive_counter_cells_total==cells
        &&summary.recursive_emitted_total==emitted&&summary.recursive_merge_writes_total==merged
        &&summary.recursive_radix_leaves==radix&&summary.recursive_small_leaves==small
        &&summary.recursive_trivial_leaves==trivial&&summary.recursive_count_leaves==counted
        &&summary.recursive_max_depth==stats.trace.back().core.core.depth,"adaptive recursive aggregate identities");
    require(robust.learning_visits_total==learning&&robust.sample_bounds_visits_total==bounds
        &&robust.trim_filter_visits_total==filters&&robust.trim_selection_calls_total==selections
        &&robust.trim_attempts==trim_nodes&&robust.trim_layout_accepts==trim_layouts
        &&robust.compact_attempts==compact_attempts&&robust.compact_accepts==compact_accepts
        &&robust.compact_trim_accepts==compact_trim&&robust.compact_counter_cells_total==compact_cells,
            "adaptive robust aggregates");
    require(stats.ladder_attempts==ladder_attempts&&stats.prune_attempts==prune_attempts
        &&stats.prune_accepts==prune_accepts&&stats.prune_mass_rejects==mass_rejects
        &&stats.actual_spill_failures==spill_failures&&stats.selected_omitted_bins_total==omitted_bins
        &&stats.selected_omitted_samples_total==omitted_samples&&stats.selected_omitted_cells_total==omitted_cells
        &&stats.prune_order_entries_total==order_entries&&stats.prune_order_vector_bytes_peak==order_peak,
            "adaptive extension aggregates");
    require(radix+small+trivial+counted==1&&branches+1==summary.recursive_nodes
        &&emitted==input.size()-(counted?0:stats.trace.back().core.core.input_size),
            "adaptive emissions telescope");
    require(u128(inputs)<=u128(input.size())*2&&processed<=inputs&&samples<=inputs
        &&spills<=input.size()&&merged<=inputs&&learning<=4*samples&&filters<=3*samples
        &&u128(cells)<=u128(input.size())+u128(4096)*stats.trace.size(),"adaptive bounded total work");
    if(root.sample_count) {
        std::vector<u64> sample;for(auto index:brc_sampled_detail::sample_indices(input.size(),1024))
            sample.push_back(input[index]);
        auto sorted=sample;std::sort(sorted.begin(),sorted.end());
        const auto& node=stats.trace.front();const auto& r=node.core;
        require(r.sample_minimum==sorted.front()&&r.sample_maximum==sorted.back(),"root raw sample oracle");
        auto original=reconstruct(sample,sorted.front(),sorted.back());
        require(r.original_cells==original.cells,"root original grid oracle");
        for(const auto& a:node.attempts) {
            require(a.low==sorted[a.cut]&&a.high==sorted[sorted.size()-a.cut-1],"independent exact rank oracle");
            auto proposal=reconstruct(sample,a.low,a.high);
            require(proposal.cells==a.trimmed_cells&&proposal.included==a.included_samples
                &&proposal.bins.size()==a.bucket_slots,"independent trimmed layout oracle");
            if(a.prune_attempted) {
                const auto active=std::count_if(proposal.bins.begin(),proposal.bins.end(),
                    [](const auto& bin){return bin.width>0;});
                oracle_prune(proposal,brc_sampled_detail::cell_budget(input.size()));
                require(a.prune_order_size==u64(active)&&a.omitted_bins==proposal.omitted_bins
                    &&a.omitted_samples==proposal.omitted_samples&&a.omitted_cells==proposal.omitted_cells
                    &&a.retained_cells==proposal.cells&&a.retained_samples==proposal.included-proposal.omitted_samples,
                        "independent width order and sample-mass proposal oracle");
            }
        }
        check_actual_membership(input,node,sample);
    }
}

AdaptiveStats check_one(const Candidate& c,const std::vector<u64>& input,
                        const std::vector<u64>& expected,const sampled_experiment::InputShape& shape,
                        const Condition* condition=nullptr) {
    AdaptiveStats s;
    if(c.preceding)s.robust=robust_experiment::check_one(*c.preceding,input,expected,shape,
        condition&&condition->mechanism==Mechanism::none?&condition->source:nullptr);
    else {
        auto actual=input;c.diagnostic(actual,&s);
        if(actual!=expected)throw std::runtime_error(std::string("adaptive diagnostic mismatch: ")+c.timing.name);
        check_adaptive(c,s,input);
        actual=input;c.timing.run(actual,nullptr);
        if(actual!=expected)throw std::runtime_error(std::string("adaptive nullptr mismatch: ")+c.timing.name);
    }
    checked_outputs+=2;return s;
}

std::vector<AdaptiveStats> check_input(const std::vector<u64>& input) {
    auto expected=input;std::sort(expected.begin(),expected.end());const auto shape=sampled_experiment::input_shape(expected);
    std::vector<AdaptiveStats> result;
    for(const auto& c:candidates())if(c.diagnostic)result.push_back(check_one(c,input,expected,shape));
    ++checked_inputs;return result;
}

template<bool Ladder,bool Prune>
void check_forced(const Candidate& c,const std::vector<u64>& input) {
    auto expected=input;std::sort(expected.begin(),expected.end());auto actual=input;AdaptiveStats s;
    brc_adaptive_detail::adaptive_impl<Ladder,Prune,true>(actual,&s,16);
    require(actual==expected,"adaptive forced-depth diagnostic output");check_adaptive(c,s,input,16);
    actual=input;brc_adaptive_detail::adaptive_impl<Ladder,Prune,false>(actual,nullptr,16);
    require(actual==expected,"adaptive forced-depth nullptr output");checked_outputs+=2;
}

void verify() {
    u64 exhaustive=0,lifted=0,random=0,focused=0;
    constexpr std::array<u64,4> alphabet{0,1,MAX_VALUE-1,MAX_VALUE};
    for(unsigned length=0;length<=4;++length)for(u64 code=0;code<(u64(1)<<(2*length));++code) {
        std::vector<u64> word(length);auto value=code;for(auto& x:word){x=alphabet[value%4];value/=4;}
        check_input(word);++exhaustive;
        if(length){std::vector<u64> a(257+length);for(std::size_t i=0;i<a.size();++i)a[i]=word[i%length];
            check_input(a);++lifted;}
    }
    std::mt19937_64 rng(0x4144415054564552ull);
    for(std::size_t n:{std::size_t(255),std::size_t(256),std::size_t(257),std::size_t(1023),
        std::size_t(1024),std::size_t(1025),std::size_t(8192),std::size_t(16384)})
        for(unsigned mode=0;mode<4;++mode) {
            std::vector<u64> a(n);for(auto& x:a)x=mode==0?rng():mode==1?MAX_VALUE-bounded(rng,8192)
                :mode==2?bounded(rng,4096):(u64(1)<<48)+bounded(rng,20)*(u64(1)<<20)+bounded(rng,8);
            check_input(a);++random;
        }
    for(unsigned tails:{16u,17u,64u,65u,256u,257u}) {
        const auto stats=check_input(robust_experiment::trim_witness(100000,tails,std::max(1000u,tails)));++focused;
        const auto& root=stats[0].trace.front();
        const u64 expected=tails<=16?16:tails<=64?64:tails<=256?256:0;
        require(root.chosen_cut==expected,"ladder exact16/64/256 tail-tie boundaries");
    }
    for(std::size_t n:{std::size_t(8192),std::size_t(100000)})for(bool hidden:{false,true}) {
        const auto stats=check_input(central_poison(n,0,hidden));++focused;
        for(auto index:{1u,2u}) {
            const auto& root=stats[index].trace.front();
            require(root.prune_accepted&&root.omitted_bins>0,"central poison actually selects pruning");
            require(root.core.core.path==(hidden?SamplePath::recursive_spill_radix:SamplePath::recursive_spill_merge),
                    "pruned actual support controls recursion");
            if(hidden)require(root.core.core.spills==n/2+1&&root.core.core.child_size==0
                &&root.attempts.size()==1,"no quantile retry after an actual scan failure");
        }
    }
    {
        const auto stats=check_input(robust_experiment::trim_witness(100000,17,1000));++focused;
        require(stats[1].trace.front().selection_rejected_by_mass
            &&stats[1].trace.front().core.core.processed==0,"sample-mass rejection precedes scan");
        require(stats[2].trace.front().chosen_cut==64,"later quantile rescues earlier mass rejection");
    }
    {
        constexpr std::array<u64,4> support{0,u64(1)<<32,MAX_VALUE-(u64(1)<<32),MAX_VALUE};
        std::vector<u64> a(8192);for(std::size_t i=0;i<a.size();++i)a[i]=support[i%4];
        const auto idx=brc_sampled_detail::sample_indices(a.size(),1024);
        for(std::size_t i=0;i<idx.size();++i)a[idx[i]]=support[i%4];
        const auto stats=check_input(a);++focused;
        const auto& first=stats[1].trace.front().attempts.front();
        require(first.prune_attempted&&!first.prune_mass_ok&&first.retained_samples==0
            &&first.retained_cells==0&&!first.selected,"empty pruning proposal cannot commit");
        require(stats[2].trace.front().chosen_cut==256,"inclusive boundary ties reach third ladder scale");
    }
    for(bool above:{false,true}){check_input(sampled_experiment::cell_budget_witness(1024,above));++focused;}
    for(std::size_t hidden:{std::size_t(4096),std::size_t(4097)}) {
        std::vector<u64> a(8192,42);const auto idx=brc_sampled_detail::sample_indices(a.size(),1024);
        for(std::size_t i=0;i<16;++i)a[idx[i]]=i%2?MAX_VALUE:MAX_VALUE-(u64(1)<<32);
        const auto free=robust_experiment::nonsampled_positions(a.size());
        for(std::size_t i=0;i<hidden-16;++i)a[free[i]]=i%2?MAX_VALUE:MAX_VALUE-(u64(1)<<32);
        const auto stats=check_input(a);++focused;
        for(const auto& s:stats)require(s.trace.front().core.compact_from_trim
            &&s.trace.front().core.core.spills==hidden,"trimmed compact actual half boundary");
    }
    {
        const auto child=central_poison(8192);
        const auto stats=check_input(sampled_experiment::embed_hidden_child(16384,MAX_VALUE,child));++focused;
        for(auto index:{1u,2u})require(stats[index].trace.size()>1&&stats[index].trace[1].prune_accepted,
                                      "child independently prunes after root compact split");
    }
    check_input(sampled_experiment::hidden_chain(131072,4,0,3));++focused;
    std::vector<u64> depth(500);for(auto& x:depth)x=rng();
    check_forced<true,false>(candidates()[20],depth);check_forced<false,true>(candidates()[21],depth);
    check_forced<true,true>(candidates()[22],depth);++checked_inputs;++focused;
    for(const auto* path:{"trivial","small_std_sort","recursive_depth_radix","adaptive_mass_radix",
        "pruned_spill_merge","pruned_spill_radix","compact_count","compact_spill_merge",
        "trim_compact_spill_merge","trim_compact_spill_radix"})
        if(!paths_seen.contains(path))throw std::runtime_error(std::string("adaptive route unexercised: ")+path);
    std::cout<<"{\"result\":\"PASS\",\"algorithm_candidates\":23,\"new_variants_checked\":3"
        <<",\"verified_input_arrays\":"<<checked_inputs<<",\"verified_algorithm_outputs\":"<<checked_outputs
        <<",\"exhaustive_short_arrays\":"<<exhaustive<<",\"lifted_arrays\":"<<lifted
        <<",\"random_boundary_arrays\":"<<random<<",\"focused_cases\":"<<focused
        <<",\"paths_exercised\":"<<paths_seen.size()
        <<",\"exact_ladder_ties_checked\":true,\"independent_pruning_order_oracle_checked\":true"
        <<",\"actual_prefix_membership_oracle_checked\":true,\"sample_mass_rejection_checked\":true"
        <<",\"empty_pruning_proposal_checked\":true,\"actual_half_contraction_checked\":true"
        <<",\"child_pruning_checked\":true,\"forced_depth_checked\":true"
        <<",\"instrumented_and_nullptr_checked\":true,\"unchanged_baseline_receipts_reused\":true"
        <<",\"fresh_heldout_banks_evaluated\":false}\n";
}

robust_experiment::Metrics metrics(const AdaptiveStats& s) {
    auto m=robust_experiment::metrics(s.robust);
#define ADD(field) m[#field]=s.field
    ADD(ladder_attempts);ADD(prune_attempts);ADD(prune_accepts);ADD(prune_mass_rejects);
    ADD(actual_spill_failures);ADD(selected_omitted_bins_total);ADD(selected_omitted_samples_total);
    ADD(selected_omitted_cells_total);ADD(prune_order_entries_total);ADD(prune_order_vector_bytes_peak);
#undef ADD
    m["selected_attempt_total"]=0;m["chosen_cut_total"]=0;m["selected_learning_samples_total"]=0;
    for(const auto& n:s.trace){m["selected_attempt_total"]+=n.selected_attempt;
        m["chosen_cut_total"]+=n.chosen_cut;m["selected_learning_samples_total"]+=n.selected_learning_samples;}
    return m;
}

std::string root_path(const Candidate& c,const AdaptiveStats& s) {
    return c.preceding?robust_experiment::root_path(*c.preceding,s.robust):adaptive_node_path_name(s.trace.front());
}

std::string terminal_path(const Candidate& c,const AdaptiveStats& s) {
    if(!s.trace.empty())return adaptive_node_path_name(s.trace.back());
    if(!s.robust.trace.empty())return robust_node_path_name(s.robust.trace.back());
    if(!s.robust.sample.recursion_trace.empty())return sample_path_name(s.robust.sample.recursion_trace.back().path);
    return root_path(c,s);
}

void write_node(std::ostream& out,const Condition& c,unsigned bank,const Candidate& candidate,
                const AdaptiveNodeStats& node,bool adaptive) {
    const auto& r=node.core;const auto& q=r.core;
    out<<c.stage<<','<<c.original_stage<<','<<c.family<<','<<c.n<<','<<bank<<','<<candidate.timing.name
        <<','<<q.depth<<','<<q.input_size<<','<<q.sample_count<<','<<q.learning_visits
        <<','<<q.processed<<','<<q.covered<<','<<q.spills<<','<<q.full_data_visits
        <<','<<q.child_size<<','<<q.shift<<','<<q.origin<<','<<q.buckets<<','<<q.active_buckets
        <<','<<sampled_experiment::decimal128(q.counter_cells_demanded)<<','<<q.counter_cells_allocated
        <<','<<q.emitted_values<<','<<q.merge_writes<<','<<q.radix_passes
        <<','<<(adaptive?adaptive_node_path_name(node):robust_node_path_name(r))<<','<<adaptive
        <<','<<r.compact_accepted<<','<<r.compact_from_trim<<','<<r.compact_width<<','<<r.trim_attempted
        <<','<<r.trim_cut<<','<<r.trim_low<<','<<r.trim_high<<','<<r.trim_included_samples
        <<','<<sampled_experiment::decimal128(r.original_cells)<<','<<sampled_experiment::decimal128(r.trimmed_cells)
        <<','<<r.trim_filter_visits<<','<<r.trim_selection_calls<<','<<node.selected_attempt<<','<<node.chosen_cut
        <<','<<node.selected_learning_samples<<','<<node.prune_accepted<<','<<node.actual_spill_failure
        <<','<<node.selection_rejected_by_mass<<','<<node.omitted_bins<<','<<node.omitted_samples
        <<','<<sampled_experiment::decimal128(node.omitted_cells)<<','<<node.attempts.size()<<'\n';
}

void write_attempts(std::ostream& out,const Condition& c,unsigned bank,const Candidate& candidate,
                    const AdaptiveNodeStats& node) {
    for(std::size_t i=0;i<node.attempts.size();++i) {
        const auto& a=node.attempts[i];
        out<<c.stage<<','<<c.original_stage<<','<<c.family<<','<<c.n<<','<<bank<<','<<candidate.timing.name
            <<','<<node.core.core.depth<<','<<i+1<<','<<node.core.core.sample_count<<','<<a.cut
            <<','<<a.low<<','<<a.high<<','<<a.included_samples<<','<<a.bucket_slots
            <<','<<sampled_experiment::decimal128(a.trimmed_cells)<<','<<a.compact_selected<<','<<a.grid_accepted
            <<','<<a.prune_attempted<<','<<a.prune_selected<<','<<a.prune_mass_ok<<','<<a.selected
            <<','<<a.prune_order_size<<','<<a.prune_order_vector_bytes<<','<<a.omitted_bins<<','<<a.omitted_samples
            <<','<<sampled_experiment::decimal128(a.omitted_cells)<<','<<a.retained_samples
            <<','<<sampled_experiment::decimal128(a.retained_cells)<<'\n';
    }
}

void check_mechanism(const Condition& c,const Candidate& candidate,const AdaptiveStats& stats) {
    if(!candidate.diagnostic||c.mechanism==Mechanism::none)return;
    const auto& root=stats.trace.front();
    if((c.mechanism==Mechanism::central_poison||c.mechanism==Mechanism::hidden_majority)&&candidate.prune) {
        require(root.prune_accepted&&root.omitted_bins>0,"benchmark poison must select pruning");
        require(root.core.core.path==(c.mechanism==Mechanism::central_poison?
            SamplePath::recursive_spill_merge:SamplePath::recursive_spill_radix),
                "benchmark actual support distinguishes success from spill rejection");
    }
    if(c.mechanism==Mechanism::mass_reject) {
        if(candidate.prune&&!candidate.ladder)require(root.selection_rejected_by_mass
            &&root.core.core.processed==0,"benchmark mass gate fallback");
        if(candidate.ladder)require(root.chosen_cut==64,"benchmark stronger quantile recovery");
    }
    if(c.mechanism==Mechanism::budget_plus_one)
        require(root.core.original_cells==4097,"benchmark exact original one-above demand");
}

void benchmark(const std::string& output_path,std::size_t max_n,double target_seconds,const std::string& subset) {
    constexpr unsigned BANKS=8,ROUNDS=7;const auto& all=candidates();const auto A=all.size();
    require(target_seconds>0&&target_seconds<=1,"target_seconds must be in (0,1]");
    std::ofstream file(output_path),nodes(output_path+".adaptive_nodes.csv"),attempts(output_path+".adaptive_attempts.csv");
    require(bool(file)&&bool(nodes)&&bool(attempts),"cannot open adaptive outputs");
    nodes<<"stage,original_stage,family,n,bank,algorithm,depth,input_size,sample_count,learning_visits,processed,covered,"
        <<"spills,full_data_visits,child_size,shift,origin,buckets,active_buckets,counter_cells_demanded,"
        <<"counter_cells_allocated,emitted_values,merge_writes,radix_passes,path,adaptive,compact_accepted,"
        <<"compact_from_trim,compact_width,trim_attempted,trim_cut,trim_low,trim_high,trim_included_samples,"
        <<"original_cells,trimmed_cells,trim_filter_visits,trim_selection_calls,selected_attempt,chosen_cut,"
        <<"selected_learning_samples,prune_accepted,actual_spill_failure,selection_rejected_by_mass,"
        <<"omitted_bins,omitted_samples,omitted_cells,attempt_count\n";
    attempts<<"stage,original_stage,family,n,bank,algorithm,depth,attempt,sample_count,cut,low,high,included_samples,"
        <<"bucket_slots,trimmed_cells,compact_selected,grid_accepted,prune_attempted,prune_selected,prune_mass_ok,"
        <<"selected,prune_order_size,prune_order_vector_bytes,omitted_bins,omitted_samples,omitted_cells,"
        <<"retained_samples,retained_cells\n";
    const auto names=metrics(AdaptiveStats{});
    file<<"stage,original_stage,family,n,seed_regime,algorithm,value_bytes,banks,rounds,median_us,p10_us,p90_us,"
        <<"min_us,max_us,calls_per_round,mean_distinct,mean_min,mean_max,mean_numeric_span";
    for(const auto& [name,value]:names)file<<','<<name;
    file<<",path,path_mix,terminal_path,terminal_path_mix";
    for(unsigned round=1;round<=ROUNDS;++round)file<<",round"<<round<<"_us";
    file<<'\n'<<std::setprecision(21);nodes<<std::setprecision(21);attempts<<std::setprecision(21);
    u64 completed=0,rows=0,banks_checked=0,node_rows=0,attempt_rows=0;
    for(const auto& c:conditions()) {
        if(c.n>max_n||!selected(c,subset))continue;
        std::vector<std::vector<u64>> banks;
        for(unsigned bank=0;bank<BANKS;++bank)banks.push_back(input_bank(c,bank));
        std::vector<std::vector<AdaptiveStats>> diagnostics(A);
        long double distinct=0,minimum=0,maximum=0,span=0;
        for(unsigned bank=0;bank<BANKS;++bank) {
            const auto& input=banks[bank];auto expected=input;std::sort(expected.begin(),expected.end());
            const auto shape=sampled_experiment::input_shape(expected);
            distinct+=shape.distinct;minimum+=shape.minimum;maximum+=shape.maximum;span+=shape.span;
            for(std::size_t ai=0;ai<A;++ai) {
                auto s=check_one(all[ai],input,expected,shape,&c);check_mechanism(c,all[ai],s);
                if(!s.trace.empty())for(const auto& node:s.trace) {
                    write_node(nodes,c,bank,all[ai],node,true);write_attempts(attempts,c,bank,all[ai],node);
                    ++node_rows;attempt_rows+=node.attempts.size();
                } else if(!s.robust.trace.empty())for(const auto& node:s.robust.trace) {
                    AdaptiveNodeStats wrapper;wrapper.core=node;write_node(nodes,c,bank,all[ai],wrapper,false);++node_rows;
                } else for(const auto& node:s.robust.sample.recursion_trace) {
                    AdaptiveNodeStats wrapper;wrapper.core.core=node;write_node(nodes,c,bank,all[ai],wrapper,false);++node_rows;
                }
                diagnostics[ai].push_back(std::move(s));
            }
            ++banks_checked;
        }
        std::vector<std::size_t> cycles(A),order(A);std::vector<std::vector<double>> times(A);
        for(std::size_t ai=0;ai<A;++ai) {
            const auto one=timed(all[ai].timing,banks,1,0);
            cycles[ai]=std::clamp<std::size_t>(std::size_t(target_seconds/std::max(one,1e-9)+.999),1,100000);
        }
        std::mt19937_64 order_rng(0x5A6D1EDB0E94005ull+c.n+completed*31337);
        for(unsigned round=0;round<ROUNDS;++round) {
            std::iota(order.begin(),order.end(),0);std::shuffle(order.begin(),order.end(),order_rng);
            for(auto ai:order)times[ai].push_back(timed(all[ai].timing,banks,cycles[ai],round)*1e6/(cycles[ai]*BANKS));
        }
        for(std::size_t ai=0;ai<A;++ai) {
            robust_experiment::Metrics totals;std::map<std::string,unsigned> paths,terminals;
            for(const auto& s:diagnostics[ai]) {
                for(const auto& [name,value]:metrics(s))totals[name]+=value;
                ++paths[root_path(all[ai],s)];++terminals[terminal_path(all[ai],s)];
            }
            file<<c.stage<<','<<c.original_stage<<','<<c.family<<','<<c.n<<','<<c.regime<<','<<all[ai].timing.name
                <<','<<sizeof(u64)<<','<<BANKS<<','<<ROUNDS<<','<<quantile(times[ai],.5)<<','<<quantile(times[ai],.1)
                <<','<<quantile(times[ai],.9)<<','<<*std::min_element(times[ai].begin(),times[ai].end())
                <<','<<*std::max_element(times[ai].begin(),times[ai].end())<<','<<cycles[ai]*BANKS
                <<','<<distinct/BANKS<<','<<minimum/BANKS<<','<<maximum/BANKS<<','<<span/BANKS;
            for(const auto& [name,value]:names)file<<','<<totals[name]/BANKS;
            file<<','<<(paths.size()==1?paths.begin()->first:"mixed")<<','<<robust_experiment::mix_string(paths)
                <<','<<(terminals.size()==1?terminals.begin()->first:"mixed")<<','<<robust_experiment::mix_string(terminals);
            for(auto value:times[ai])file<<','<<value;
            file<<'\n';++rows;
        }
        ++completed;file.flush();nodes.flush();attempts.flush();
        std::cerr<<"completed "<<c.stage<<' '<<c.family<<" n="<<c.n<<'\n';
    }
    require(completed>0,"no selected adaptive conditions");
    std::cout<<"{\"result\":\"PASS\",\"conditions\":"<<completed<<",\"rows\":"<<rows
        <<",\"validated_input_banks\":"<<banks_checked<<",\"algorithms\":"<<A
        <<",\"banks\":8,\"rounds\":7,\"trace_nodes\":"<<node_rows<<",\"trace_attempts\":"<<attempt_rows
        <<",\"validated_algorithm_outputs\":"<<checked_outputs
        <<",\"target_seconds_per_algorithm_round\":"<<target_seconds
        <<",\"copy_setup_allocation_output_destruction_included\":true,\"observable_sink\":"<<observed<<"}\n";
}

} // namespace adaptive_experiment

int main(int argc,char** argv) {
    try {
        if(argc==2&&std::string_view(argv[1])=="--verify")adaptive_experiment::verify();
        else if(argc==2&&std::string_view(argv[1])=="--list") {
            std::cout<<"stage,original_stage,family,n,seed_regime\n";
            for(const auto& c:adaptive_experiment::conditions())std::cout<<c.stage<<','<<c.original_stage<<','
                <<c.family<<','<<c.n<<','<<c.regime<<'\n';
        } else if(argc>=3&&std::string_view(argv[1])=="--bench")
            adaptive_experiment::benchmark(argv[2],argc>3?std::stoull(argv[3]):1000000,
                argc>4?std::stod(argv[4]):.012,argc>5?argv[5]:"all");
        else {std::cerr<<"usage: adaptive_bench --verify | --list | --bench output.csv "
            <<"[max_n=1000000] [target_seconds=.012] [subset=all]\n";return 2;}
    } catch(const std::exception& error){std::cerr<<error.what()<<'\n';return 1;}
    return 0;
}
