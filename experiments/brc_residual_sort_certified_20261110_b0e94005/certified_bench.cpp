// Phase four: fixed-grid feasibility repair with twenty-six frozen controls.
#ifndef BRC_SELECTION_SOURCE
#define BRC_SELECTION_SOURCE "build/selection_frozen_include.hpp"
#endif
#include BRC_SELECTION_SOURCE
#include "certified_kernels.hpp"
#include <tuple>

namespace certified_experiment {

void time_certified(std::vector<u64>& values,Stats*) {certified_combined_1024(values,nullptr);}
struct Candidate {
    Algorithm timing;
    const selection_experiment::Candidate* preceding=nullptr;
};
const std::vector<Candidate>& candidates() {
    static const auto all=[] {
        std::vector<Candidate> out;
        for(const auto& c:selection_experiment::candidates())out.push_back({c.timing,&c});
        out.push_back({{"certified_combined_1024",time_certified}});return out;
    }();return all;
}

enum class Kind {old,balanced,shifted,low_dominant,high_dominant,many_infeasible,large_balanced,
                 dp_witness,hidden_majority,singleton_witness,fractional_witness};
struct Condition {
    selection_experiment::Condition source;
    std::string family,stage,original_stage,regime;
    std::size_t n=0;
    Kind kind=Kind::old;
    u64 tag=0;
};

std::vector<Condition> conditions() {
    const auto preceding=selection_experiment::conditions();std::vector<Condition> out;
    for(const auto* name:{"selection_fresh_popular_wide","selection_fresh_rare_wide",
        "selection_fresh_tail_12pct_asymmetric","selection_fresh_tail_15pct_high",
        "selection_fresh_tail_15pct_low","selection_fresh_uniform_uint64",
        "selection_fresh_narrow_offsets","selection_fresh_interior_contamination",
        "selection_fresh_128clusters_12pct_tail","witness_density_mass_width"}) {
        const auto found=std::find_if(preceding.begin(),preceding.end(),
                                     [&](const auto& c){return c.family==name;});
        require(found!=preceding.end(),"missing phase-three known condition");
        out.push_back({*found,name,"calibration","phase3_"+found->stage,
                       "exact_previously_measured_phase3_banks",found->n,Kind::old,found->tag});
    }
    const auto fresh=[&](const char* name,std::size_t n,Kind kind,u64 tag) {
        out.push_back({{},name,"heldout","new_phase4",
                       "new_certified_v1_random_samples_exact_population",n,kind,tag});
    };
    // Natural sample positions: exact population counts, random values, shuffle.
    // No sample-location overwrite occurs in these six fresh families.
    fresh("certified_fresh_three_bins_balanced",100000,Kind::balanced,701);
    fresh("certified_fresh_three_bins_shifted",100000,Kind::shifted,702);
    fresh("certified_fresh_three_bins_low_dominant",100000,Kind::low_dominant,703);
    fresh("certified_fresh_three_bins_high_dominant",100000,Kind::high_dominant,704);
    fresh("certified_fresh_eight_bins_infeasible",100000,Kind::many_infeasible,705);
    fresh("certified_fresh_three_bins_million",1000000,Kind::large_balanced,706);
    const auto mechanism=[&](const char* name,Kind kind) {
        out.push_back({{},name,"mechanism","new_phase4",
                       "constructed_actual_sampler_positions",100000,kind});
    };
    mechanism("witness_exact_mass_dp",Kind::dp_witness);
    mechanism("witness_exact_mass_hidden_majority",Kind::hidden_majority);
    mechanism("witness_best_singleton",Kind::singleton_witness);
    mechanism("witness_fractional_mass_reject",Kind::fractional_witness);
    require(out.size()==20,"certified matrix contains20 conditions");return out;
}

bool selected(const Condition& c,const std::string& subset) {
    if(subset.empty()||subset=="all")return true;
    if(subset=="evaluation"||subset=="heldout")return c.stage=="heldout";
    if(subset=="calibration"||subset=="mechanism")return c.stage==subset;
    return c.family.find(subset)!=std::string::npos;
}

std::vector<u64> mechanism_input(Kind kind,std::size_t n,unsigned bank=0) {
    const u64 a=(u64(1)<<48)+u64(bank)*(u64(1)<<36);
    std::vector<u64> lows{a,a+(u64(256)<<16),a+(u64(512)<<16)};
    std::vector<u64> widths{29711,24680,24680},mass{410,307,307},percent{40,30,30};
    if(kind==Kind::singleton_witness) {
        lows={a,a+(u64(512)<<16)};widths={49801,1};mass={1000,24};percent={98,2};
    } else if(kind==Kind::fractional_witness) {
        widths={49422,49422,49424};mass={341,341,342};percent={34,33,33};
    }
    std::vector<u64> input(n);std::size_t begin=0;
    for(std::size_t j=0;j<widths.size();++j) {
        const auto end=j+1==widths.size()?n:begin+n*percent[j]/100;
        for(std::size_t i=begin;i<end;++i)input[i]=lows[j]+((i-begin+bank*101)%widths[j]);
        begin=end;
    }
    const auto indices=brc_sampled_detail::sample_indices(n,1024);
    require(indices.size()==1024,"mechanism has1024 actual sample positions");
    begin=0;
    for(std::size_t j=0;j<mass.size();++j) {
        for(std::size_t k=0;k<mass[j];++k)
            input[indices[begin+k]]=lows[j]+((k+mass[j]%2)%2?widths[j]-1:0);
        begin+=mass[j];
    }
    require(begin==1024,"mechanism sample population");
    if(kind==Kind::hidden_majority)
        for(auto i:robust_experiment::nonsampled_positions(n))input[i]=lows[0];
    return input;
}

std::vector<u64> input_bank(const Condition& c,unsigned bank) {
    if(c.kind==Kind::old)return selection_experiment::input_bank(c.source,bank);
    if(c.stage=="mechanism")return mechanism_input(c.kind,c.n,bank);
    std::mt19937_64 rng(0x4345525449465631ull^(u64(c.n)*0x9e3779b97f4a7c15ull)
        ^(u64(bank)*0xD1B54A32D192ED03ull)^(c.tag*0x94D049BB133111EBull));
    const unsigned shift=c.kind==Kind::large_balanced?20:16;
    const u64 a=(u64(1)<<48)+(bounded(rng,u64(1)<<20)<<shift);
    std::vector<u64> widths{29711,24680,24680},percent{40,30,30};
    std::vector<u64> lows{a,a+(u64(256)<<shift),a+(u64(512)<<shift)};
    if(c.kind==Kind::shifted)for(auto& x:lows)x+=2048;
    if(c.kind==Kind::low_dominant)percent={20,40,40};
    if(c.kind==Kind::high_dominant)percent={44,28,28};
    if(c.kind==Kind::large_balanced)for(auto& x:widths)x*=10;
    if(c.kind==Kind::many_infeasible) {
        widths={40000,11000,11000,11000,11000,11000,11000,11000};
        lows.clear();for(unsigned j=0;j<8;++j)lows.push_back(a+(u64(j*128)<<16));
        // Exact counts below allocate45% to the first bin, the remainder equally
        // to seven bins, with deterministic remainder allocation to earlier bins.
    }
    std::vector<std::size_t> population(widths.size());
    if(c.kind==Kind::many_infeasible) {
        population[0]=c.n*45/100;const auto rest=c.n-population[0];
        for(std::size_t j=1;j<8;++j)population[j]=rest/7+(j-1<rest%7);
    } else {
        std::size_t used=0;
        for(std::size_t j=0;j<widths.size();++j) {
            population[j]=j+1==widths.size()?c.n-used:c.n*percent[j]/100;used+=population[j];
        }
    }
    std::vector<u64> input;input.reserve(c.n);
    for(std::size_t j=0;j<widths.size();++j)
        for(std::size_t i=0;i<population[j];++i)input.push_back(lows[j]+bounded(rng,widths[j]));
    std::shuffle(input.begin(),input.end(),rng);return input;
}

struct RepairOracle {
    CertifiedMethod method=CertifiedMethod::none;
    std::vector<unsigned char> keep;
    u64 feasible_bins=0,feasible_samples=0,best_index=0,best_samples=0,best_width=0;
    bool best_found=false;
    u64 prefix_mass=0,denominator=1,upper_floor=0,optimal_mass=0;
    u128 numerator=0;
    u64 retained_samples=0,retained_cells=0,retained_bins=0;
    u64 transitions=0,reachable=0,improvements=0;
};

RepairOracle repair_oracle(const std::vector<brc_sampled_detail::Bucket>& bins,
                           std::size_t original_sample,std::size_t budget) {
    RepairOracle o;o.keep.assign(bins.size(),0);std::vector<std::size_t> order;
    const auto target=(original_sample+1)/2;
    for(std::size_t i=0;i<bins.size();++i)if(bins[i].width&&bins[i].samples&&bins[i].width<=budget) {
        order.push_back(i);o.feasible_samples+=bins[i].samples;
        if(!o.best_found||std::tuple{bins[i].samples,MAX_VALUE-bins[i].width,MAX_VALUE-i}
            >std::tuple{o.best_samples,MAX_VALUE-o.best_width,MAX_VALUE-o.best_index}) {
            o.best_found=true;o.best_index=i;o.best_samples=bins[i].samples;o.best_width=bins[i].width;
        }
    }
    o.feasible_bins=order.size();
    if(o.best_found&&o.best_samples>=target) {
        o.method=CertifiedMethod::singleton;o.keep[o.best_index]=1;
        o.retained_samples=o.best_samples;o.retained_cells=o.best_width;o.retained_bins=1;return o;
    }
    std::sort(order.begin(),order.end(),[&](auto a,auto b) {
        const auto& x=bins[a];const auto& y=bins[b];
        const u128 left=u128(x.samples)*y.width,right=u128(y.samples)*x.width;
        if(left!=right)return left>right;
        if(x.samples!=y.samples)return x.samples>y.samples;
        if(x.width!=y.width)return x.width<y.width;
        return a<b;
    });
    u64 capacity=budget;
    for(auto j:order) {
        if(bins[j].width<=capacity){capacity-=bins[j].width;o.prefix_mass+=bins[j].samples;}
        else {o.numerator=u128(capacity)*bins[j].samples;o.denominator=bins[j].width;break;}
    }
    o.upper_floor=o.prefix_mass+u64(o.numerator/o.denominator);
    if(o.upper_floor<target){o.method=CertifiedMethod::fractional_reject;return o;}
    // Independent full-row DP: every transition reads a separate immutable
    // preceding row. uint64 widths and full rows avoid the kernel's in-place
    // descending updates and packed reconstruction bits.
    const u64 inf=budget+1;const std::size_t M=o.feasible_samples;
    std::vector<std::vector<u64>> table(order.size()+1,std::vector<u64>(M+1,inf));
    table[0][0]=0;u64 prefix=0;
    for(std::size_t i=0;i<order.size();++i) {
        table[i+1]=table[i];const auto& b=bins[order[i]];o.transitions+=prefix+1;
        for(std::size_t mass=0;mass<=prefix;++mass)if(table[i][mass]<=budget) {
            ++o.reachable;
            if(table[i][mass]+b.width<table[i+1][mass+b.samples]) {
                table[i+1][mass+b.samples]=table[i][mass]+b.width;++o.improvements;
            }
        }
        prefix+=b.samples;
    }
    for(std::size_t m=0;m<=M;++m)if(table.back()[m]<=budget)o.optimal_mass=m;
    if(o.optimal_mass<target){o.method=CertifiedMethod::dp_reject;return o;}
    o.method=CertifiedMethod::dp_accept;o.retained_samples=o.optimal_mass;
    o.retained_cells=table.back()[o.optimal_mass];auto remaining=o.optimal_mass;
    for(std::size_t i=order.size();i>0;--i)if(table[i][remaining]<table[i-1][remaining]) {
        o.keep[order[i-1]]=1;remaining-=bins[order[i-1]].samples;++o.retained_bins;
    }
    require(remaining==0,"independent DP row reconstruction");return o;
}

void check_repair(const CertifiedTrialStats& t,const RepairOracle& o,
                  const selection_experiment::Model& model,std::size_t original_sample,std::size_t budget) {
    const bool accepted=o.method==CertifiedMethod::singleton||o.method==CertifiedMethod::dp_accept;
    const bool dp=o.method==CertifiedMethod::dp_accept||o.method==CertifiedMethod::dp_reject;
    require(t.original_sample_size==original_sample&&t.minimum_mass==(original_sample+1)/2
        &&t.included_samples==model.included&&t.original_cells==model.cells&&t.budget==budget
        &&t.feasible_bins==o.feasible_bins&&t.feasible_samples==o.feasible_samples,
            "repair source population and fixed-grid budget");
    require(t.singleton_checked&&t.best_single_found==o.best_found
        &&(!o.best_found||(t.best_single_index==o.best_index&&t.best_single_samples==o.best_samples
                         &&t.best_single_width==o.best_width)),"independent best singleton oracle");
    require(t.method==o.method&&t.selected==accepted&&t.dp_attempted==dp
        &&t.dp_accepted==(o.method==CertifiedMethod::dp_accept)
        &&t.dp_infeasible==(o.method==CertifiedMethod::dp_reject)
        &&t.fractional_rejected==(o.method==CertifiedMethod::fractional_reject)
        &&t.half_mass_infeasible_certified==!accepted&&t.optimal_mass_certified==dp,
            "certificate outcomes and exact scope");
    require(t.fractional_checked==(o.method!=CertifiedMethod::singleton),"fractional gate sequence");
    if(t.fractional_checked)require(t.fractional_prefix_mass==o.prefix_mass
        &&t.fractional_numerator==o.numerator&&t.fractional_denominator==o.denominator
        &&t.fractional_upper_floor==o.upper_floor,"exact rational fractional upper bound");
    if(dp)require(t.dp_items==o.feasible_bins&&t.dp_mass_limit==o.feasible_samples
        &&t.dp_optimal_mass==o.optimal_mass&&t.dp_cell_transitions==o.transitions
        &&t.dp_reachable_transitions==o.reachable&&t.dp_improvements==o.improvements,
            "independent full-row DP optimum and work accounting");
    require(t.retained_samples==o.retained_samples&&t.retained_cells==o.retained_cells
        &&t.retained_bins==o.retained_bins,"repair reconstructed selected mass and width");
    if(dp)require(t.dp_width_vector_bytes>=(o.feasible_samples+1)*sizeof(u32)
        &&t.dp_take_bits_bytes>=o.feasible_bins*((o.feasible_samples+64)/64)*sizeof(u64)
        &&t.auxiliary_vector_bytes>=t.dp_width_vector_bytes+t.dp_take_bits_bytes,
            "DP allocation contains width and packed predecessor storage");
}

using Model=selection_experiment::Model;
std::set<std::string> paths_seen;
std::set<CertifiedMethod> repair_methods_seen;
u64 checked_inputs=0,checked_outputs=0,parity_reference_outputs=0,parity_decisions=0;

Model selected_model(const CertifiedStats& stats,std::size_t index,const std::vector<u64>& input) {
    const auto& s=stats.selection;const auto& old=s.adaptive.trace[index];
    const auto& r=old.core;const auto& q=r.core;const auto& node=s.trace[index];
    const auto& certified=stats.trace[index];const auto budget=brc_sampled_detail::cell_budget(input.size());
    std::vector<u64> sample;
    for(auto i:brc_sampled_detail::sample_indices(input.size(),1024))sample.push_back(input[i]);
    auto sorted=sample;std::sort(sorted.begin(),sorted.end());
    require(q.sample_count==sample.size()&&r.sample_minimum==sorted.front()
        &&r.sample_maximum==sorted.back(),"certified actual sample and bounds");
    const auto original=adaptive_experiment::reconstruct(sample,sorted.front(),sorted.back());
    require(r.original_cells==original.cells&&r.initial_bucket_slots==original.bins.size(),
            "certified original grid reconstruction");
    require(!node.trials.empty()&&node.trials.size()<=4&&node.trials.size()==node.gap_repairs+1,
            "certified bounded gap continuation");
    std::size_t begin=0,end=sample.size(),repair_index=0;Model chosen;bool found=false,initial_selected=false;
    CertifiedMethod selected_method=CertifiedMethod::none;u64 selected_round=0;
    for(std::size_t i=0;i<node.trials.size();++i) {
        const auto& t=node.trials[i];require(t.round==i,"certified proposal round sequence");
        if(i) {
            const auto g=selection_experiment::gap_oracle(sorted,begin,end,(sample.size()+1)/2);
            require(g.found&&t.gap_applied&&t.gap_index==g.index&&t.gap_size==g.gap
                &&t.kept_lower==g.keep_lower,"certified independent admissible gap choice");
            begin=g.next_begin;end=g.next_end;
        } else require(!t.gap_applied&&!t.gap_index&&!t.gap_size,"initial proposal has no gap");
        require(t.window_begin==begin&&t.window_end==end&&t.low==sorted[begin]
            &&t.high==sorted[end-1]&&t.included_samples==end-begin,"certified sample window mass");
        auto proposal=adaptive_experiment::reconstruct(sample,t.low,t.high);
        require(t.original_cells==proposal.cells&&t.bucket_slots==proposal.bins.size()
            &&proposal.included==t.included_samples,"certified fixed-grid source reconstruction");
        const bool compact=u128(t.high)-t.low+1<=budget;
        const bool grid=!compact&&proposal.cells<=budget;
        require(t.compact_selected==compact&&t.grid_selected==grid
            &&t.density_attempted==(!compact&&!grid),"unchanged compact/grid/density proposal order");
        if(compact)proposal=selection_experiment::compact_model(t.low,t.high,sample.size(),end-begin,budget);
        bool accepted=compact||grid;
        if(t.density_attempted) {
            const auto d=selection_experiment::density_oracle(proposal.bins,sample.size(),budget);
            require(t.retained_cells==d.cells&&t.retained_samples==d.samples
                &&t.retained_bins==d.bins&&t.density_order_size==d.order_size
                &&t.omitted_cells==proposal.cells-d.cells
                &&t.omitted_samples==proposal.included-d.samples
                &&t.omitted_bins==d.order_size-d.bins&&t.mass_ok==d.mass_ok
                &&t.density_selected==d.accepted&&t.selected==d.accepted,
                    "greedy proposal diagnostics remain truthful before certified repair");
            if(d.accepted) {
                for(std::size_t j=0;j<proposal.bins.size();++j)if(!d.keep[j])proposal.bins[j].width=0;
                proposal.cells=d.cells;accepted=true;
            } else {
                require(repair_index<certified.trials.size(),"every greedy failure invokes a repair");
                const auto& ct=certified.trials[repair_index++];
                require(ct.round==i&&ct.window_begin==begin&&ct.window_end==end
                    &&ct.low==t.low&&ct.high==t.high,"repair and failed greedy window alignment");
                const auto oracle=repair_oracle(proposal.bins,sample.size(),budget);
                check_repair(ct,oracle,proposal,sample.size(),budget);
                repair_methods_seen.insert(ct.method);
                if(ct.selected) {
                    for(std::size_t j=0;j<proposal.bins.size();++j)
                        if(!oracle.keep[j])proposal.bins[j].width=0;
                    proposal.cells=oracle.retained_cells;accepted=true;
                    selected_method=ct.method;selected_round=ct.round;
                }
            }
        } else {
            const auto bins=std::count_if(proposal.bins.begin(),proposal.bins.end(),
                                          [](const auto& b){return b.width>0;});
            require(t.selected&&t.retained_cells==proposal.cells&&t.retained_samples==end-begin
                &&t.retained_bins==u64(bins)&&t.mass_ok&&!t.density_selected
                &&!t.density_order_size&&!t.density_work_bytes&&!t.omitted_cells
                &&!t.omitted_samples&&!t.omitted_bins,"ordinary representation bypasses repair");
        }
        if(!i)initial_selected=accepted;
        if(accepted) {
            require(i+1==node.trials.size(),"first effective model gets the only actual scan");
            chosen=std::move(proposal);found=true;
        }
    }
    require(repair_index==certified.trials.size()&&certified.selected_method==selected_method
        &&certified.selected_round==selected_round,"complete repair sequence and selected method");
    require(node.sample_sorted==!initial_selected
        &&node.gap_selected==(found&&node.trials.back().round>0)
        &&node.density_selected==(found&&node.trials.back().density_selected),
            "effective selection controls work, without relabeling greedy failure");
    require(found==(q.counter_cells_allocated>0),"selected model precedes actual scan decision");
    return chosen;
}

void check_certified(const CertifiedStats& stats,const std::vector<u64>& input,unsigned starting_depth=0) {
    const auto& s=stats.selection;const auto& a=s.adaptive;const auto& sum=a.robust.sample;
    require(!stats.trace.empty()&&stats.trace.size()==s.trace.size()&&s.trace.size()==a.trace.size()
        &&s.trace.size()==a.robust.trace.size()&&s.trace.size()==sum.recursion_trace.size(),
            "aligned certified traces");
    u64 inputs=0,samples=0,processed=0,spills=0,cells=0,emitted=0,merged=0;
    u64 direct=0,prefix=0,writes=0,density_attempts=0,density_accepts=0,mass_rejects=0;
    u64 gap_repairs=0,sorts=0,work_peak=0,radix=0,small=0,trivial=0,counted=0;
    CertifiedStats totals;std::vector<u64> actual_node=input;
    for(std::size_t i=0;i<s.trace.size();++i) {
        const auto& old=a.trace[i];const auto& q=old.core.core;const auto& node=s.trace[i];
        const auto& cn=stats.trace[i];const auto& mirror=sum.recursion_trace[i];
        const auto budget=brc_sampled_detail::cell_budget(q.input_size);
        paths_seen.insert(certified_node_path_name(cn,node,old));
        require(q.depth==starting_depth+i&&q.depth<=16&&q.input_size==actual_node.size()
            &&q.input_size==mirror.input_size&&q.path==mirror.path,"certified actual recursive descent");
        require(q.processed==q.covered+q.spills&&q.processed<=q.input_size
            &&q.full_data_visits==q.processed&&q.counter_cells_allocated<=budget,
                "certified actual population and counter budget");
        const bool early=q.path==SamplePath::trivial||q.path==SamplePath::small_std_sort
            ||q.path==SamplePath::recursive_depth_radix;
        require(q.sample_count==(early?0:std::min<u64>(q.input_size,1024)),"certified sample and leaf cutoff");
        std::vector<u64> next;
        if(!early) {
            auto model=selected_model(stats,i,actual_node);
            if(q.counter_cells_allocated) {
                require(model.cells==q.counter_cells_allocated&&model.cells==q.counter_cells_demanded
                    &&model.grid.origin==q.origin&&model.grid.shift==q.shift,"certified selected geometry");
                u64 retained=0,lo=MAX_VALUE,hi=0;
                for(const auto& b:model.bins)if(b.width) {
                    retained+=b.samples;lo=std::min(lo,b.low);hi=std::max(hi,u64(u128(b.low)+b.width-1));
                }
                require(node.selected_cells==model.cells&&node.selected_learning_samples==retained
                    &&old.selected_learning_samples==retained&&u128(2)*retained>=q.sample_count
                    &&node.selected_low==lo&&node.selected_high==hi,"certified selected mask mass and envelope");
                u64 seen=0,hit=0;
                for(u64 x:actual_node) {
                    bool covered=false;
                    if(x>=model.grid.origin) {
                        const auto j=(x-model.grid.origin)>>model.grid.shift;
                        if(j<model.bins.size()) {const auto& b=model.bins[j];
                            covered=b.width&&x>=b.low&&u128(x)<u128(b.low)+b.width;}
                    }
                    ++seen;if(covered)++hit;else next.push_back(x);
                    if(next.size()>actual_node.size()/2)break;
                }
                require(q.processed==seen&&q.covered==hit&&q.spills==next.size(),
                        "all-node certified actual prefix membership oracle");
            } else require(!q.processed&&!node.selected_cells&&!node.selected_learning_samples,
                            "rejected fixed-grid proposals never scan the population");
        } else require(node.trials.empty()&&cn.trials.empty()&&!node.sample_sorted&&!node.gap_repairs
            &&!node.selected_cells&&!node.selected_learning_samples&&cn.selected_method==CertifiedMethod::none,
                "certified early leaf has no model work");
        const bool output=q.path==SamplePath::recursive_count||q.path==SamplePath::recursive_spill_merge;
        if(output)require(q.processed==q.input_size&&q.spills<=q.input_size/2&&q.emitted_values==q.covered
            &&node.fused_output&&node.direct_output_writes==q.input_size&&!node.prefix_output_writes
            &&!q.merge_writes,"successful certified fused output writes exactly n values");
        else require(!q.emitted_values&&!q.merge_writes&&!node.prefix_output_writes
            &&!node.direct_output_writes&&!node.fused_output,"certified fallback output counted separately");
        require(node.total_output_writes==node.prefix_output_writes+node.direct_output_writes+q.merge_writes,
                "certified physical writes disjoint from semantic emitted count");
        require(node.actual_spill_failure==(q.path==SamplePath::recursive_spill_radix)
            &&old.actual_spill_failure==node.actual_spill_failure,"repair acceptance versus real majority gate");
        switch(q.path) {
        case SamplePath::recursive_spill_merge:
            require(q.spills>0&&q.child_size==q.spills&&i+1<s.trace.size(),"certified actual half child");
            actual_node=std::move(next);break;
        case SamplePath::recursive_count:require(!q.spills&&!q.child_size,"certified count leaf");++counted;break;
        case SamplePath::recursive_spill_radix:
            require(q.spills==q.input_size/2+1&&!q.child_size,"certified half-plus-one abort");++radix;break;
        case SamplePath::recursive_cell_radix:require(!q.processed&&!q.child_size,"certified model fallback");++radix;break;
        case SamplePath::recursive_depth_radix:require(q.depth==16&&q.input_size>256,"certified depth fallback");++radix;break;
        case SamplePath::small_std_sort:require(q.input_size>=2&&q.input_size<=256,"certified small cutoff");++small;break;
        case SamplePath::trivial:require(q.input_size<2,"certified trivial cutoff");++trivial;break;
        default:throw std::runtime_error("unexpected certified node path");
        }
        if(q.path!=SamplePath::recursive_spill_merge)require(i+1==s.trace.size(),"single certified terminal node");
        for(const auto& t:node.trials) {
            density_attempts+=t.density_attempted;density_accepts+=t.density_selected;
            mass_rejects+=t.density_attempted&&!t.mass_ok;work_peak=std::max(work_peak,t.density_work_bytes);
        }
        for(const auto& t:cn.trials) {
            totals.singleton_checks+=t.singleton_checked;totals.singleton_accepts+=t.method==CertifiedMethod::singleton;
            totals.fractional_checks+=t.fractional_checked;totals.fractional_rejects+=t.fractional_rejected;
            totals.dp_attempts+=t.dp_attempted;totals.dp_accepts+=t.dp_accepted;totals.dp_rejects+=t.dp_infeasible;
            totals.dp_cell_transitions_total+=t.dp_cell_transitions;
            totals.dp_reachable_transitions_total+=t.dp_reachable_transitions;
            totals.dp_improvements_total+=t.dp_improvements;
            totals.repair_auxiliary_bytes_peak=std::max(totals.repair_auxiliary_bytes_peak,t.auxiliary_vector_bytes);
        }
        gap_repairs+=node.gap_repairs;sorts+=node.sample_sorted;
        inputs+=q.input_size;samples+=q.sample_count;processed+=q.processed;spills+=q.spills;
        cells+=q.counter_cells_allocated;emitted+=q.emitted_values;merged+=q.merge_writes;
        direct+=node.direct_output_writes;prefix+=node.prefix_output_writes;writes+=node.total_output_writes;
    }
    require(sum.recursive_nodes==s.trace.size()&&sum.recursive_input_total==inputs
        &&sum.recursive_sample_total==samples&&sum.recursive_processed_total==processed
        &&sum.recursive_spill_total==spills&&sum.recursive_counter_cells_total==cells
        &&sum.recursive_emitted_total==emitted&&sum.recursive_merge_writes_total==merged
        &&sum.recursive_radix_leaves==radix&&sum.recursive_small_leaves==small
        &&sum.recursive_trivial_leaves==trivial&&sum.recursive_count_leaves==counted,
            "certified recursive aggregates");
    require(s.density_attempts==density_attempts&&s.density_accepts==density_accepts
        &&s.density_mass_rejects==mass_rejects&&s.density_work_bytes_peak==work_peak
        &&s.gap_repairs_total==gap_repairs&&s.sample_sorts==sorts
        &&s.prefix_output_writes_total==prefix&&s.direct_output_writes_total==direct
        &&s.total_output_writes_total==writes,"certified inherited selection aggregates");
#define SAME(field) require(stats.field==totals.field,"certified aggregate " #field)
    SAME(singleton_checks);SAME(singleton_accepts);SAME(fractional_checks);SAME(fractional_rejects);
    SAME(dp_attempts);SAME(dp_accepts);SAME(dp_rejects);SAME(dp_cell_transitions_total);
    SAME(dp_reachable_transitions_total);SAME(dp_improvements_total);SAME(repair_auxiliary_bytes_peak);
#undef SAME
    require(radix+small+trivial+counted==1&&u128(inputs)<=u128(input.size())*2
        &&u128(cells)<=u128(input.size())+u128(4096)*s.trace.size(),"certified half contraction totals");
}

CertifiedStats check_one(const Candidate& c,const std::vector<u64>& input,
                         const std::vector<u64>& expected,const sampled_experiment::InputShape& shape) {
    CertifiedStats s;
    if(c.preceding)s.selection=selection_experiment::check_one(*c.preceding,input,expected,shape);
    else {
        auto actual=input;certified_combined_1024(actual,&s);
        require(actual==expected,"certified diagnostic full sorted output");check_certified(s,input);
        actual=input;c.timing.run(actual,nullptr);
        require(actual==expected,"certified nullptr full sorted output");
    }
    checked_outputs+=2;return s;
}

void check_parity(const CertifiedStats& s,const SelectionStats& preceding) {
    if(!s.singleton_accepts&&!s.dp_accepts) {
        selection_experiment::compare_decisions(preceding.adaptive,s.selection.adaptive);
        require(preceding.direct_output_writes_total==s.selection.direct_output_writes_total
            &&preceding.total_output_writes_total==s.selection.total_output_writes_total,
                "no accepted repair preserves frozen output work");++parity_decisions;
    }
}

CertifiedStats check_input(const std::vector<u64>& input,bool compare_previous=false) {
    auto expected=input;std::sort(expected.begin(),expected.end());
    auto result=check_one(candidates().back(),input,expected,sampled_experiment::input_shape(expected));
    if(compare_previous) {
        auto actual=input;SelectionStats previous;selection_combined_1024(actual,&previous);
        require(actual==expected,"frozen phase-three parity reference output");
        check_parity(result,previous);++parity_reference_outputs;++checked_outputs;
    }
    ++checked_inputs;return result;
}

u64 verify_repair_helpers() {
    struct Test {std::vector<u64> widths,mass;std::size_t budget,sample;};
    std::vector<Test> tests={
        {{6,5,5},{12,9,9},10,30},
        {{1,50},{5,100},50,105},
        {{6,6,6},{4,4,4},10,12},
        {{10,10},{4,4},10,30},
        {{11,6,6},{11,4,4},10,19},
        {{30000,25000,25000},{410,307,307},50000,1024},
        {{31,7,8,8,9},{1,5,5,5,5},16,21},
        {{0,50001,2,3},{0,800,100,124},50000,1024}
    };
    std::mt19937_64 rng(0x434552544f524143ull);
    for(unsigned trial=0;trial<512;++trial) {
        Test t;const auto count=3+bounded(rng,6);u64 mass=0;
        for(std::size_t j=0;j<count;++j) {
            t.widths.push_back(1+bounded(rng,31));t.mass.push_back(1+bounded(rng,9));mass+=t.mass.back();
        }
        t.budget=1+bounded(rng,40);t.sample=mass+bounded(rng,5);tests.push_back(std::move(t));
    }
    u64 checked=0;std::set<CertifiedMethod> methods;
    for(const auto& t:tests) {
        brc_sampled_detail::SampledLayout model;model.sample.resize(t.sample);
        model.grid={0,20,t.widths.size()};model.buckets.resize(t.widths.size());u64 included=0;
        for(std::size_t i=0;i<t.widths.size();++i) {
            auto& b=model.buckets[i];b.low=i*(u64(1)<<20);b.width=t.widths[i];b.samples=t.mass[i];
            model.cells+=b.width;included+=b.samples;
        }
        // Respect the production helper's entry condition: a failed greedy
        // proposal on an over-budget fixed grid. These are abstract helper
        // fixtures, not natural-sampling performance populations.
        if(model.cells<=t.budget||selection_experiment::density_oracle(model.buckets,t.sample,t.budget).accepted)
            continue;
        const auto before=model;const auto oracle=repair_oracle(model.buckets,t.sample,t.budget);
        SampleStats stats;CertifiedTrialStats trial;
        const auto result=brc_certified_detail::repair_fixed_grid<true>(model,included,t.budget,&stats,&trial);
        Model source;source.bins=before.buckets;source.cells=before.cells;source.included=included;
        check_repair(trial,oracle,source,t.sample,t.budget);methods.insert(trial.method);
        require(result.method==oracle.method&&result.accepted==trial.selected
            &&result.retained_samples==oracle.retained_samples&&result.retained_cells==oracle.retained_cells
            &&result.retained_bins==oracle.retained_bins,"direct repair helper result");
        u64 exact_mass=0,exact_width=0;
        for(u64 mask=0;mask<(u64(1)<<before.buckets.size());++mask) {
            u64 mass=0,width=0;bool eligible=true;
            for(std::size_t j=0;j<before.buckets.size();++j)if(mask&(u64(1)<<j)) {
                const auto& b=before.buckets[j];
                eligible&=b.width>0&&b.samples>0&&b.width<=t.budget;
                mass+=b.samples;width+=b.width;
            }
            if(eligible&&width<=t.budget&&(mass>exact_mass||(mass==exact_mass&&width<exact_width))) {
                exact_mass=mass;exact_width=width;
            }
        }
        if(trial.fractional_checked)require(trial.fractional_upper_floor>=exact_mass,
                                            "fractional certificate bounds every enumerated subset");
        if(trial.dp_attempted)require(trial.dp_optimal_mass==exact_mass,
                                      "exact subset enumeration independently certifies DP optimum");
        if(trial.dp_accepted)require(trial.retained_cells==exact_width,
                                     "DP reconstruction has minimum width at maximum sample mass");
        if(trial.half_mass_infeasible_certified)require(exact_mass<(t.sample+1)/2,
                                                       "every negative certificate is independently valid");
        u64 kept_mass=0,kept_cells=0;
        for(std::size_t j=0;j<model.buckets.size();++j) {
            const auto wanted=result.accepted&&!oracle.keep[j]?0:before.buckets[j].width;
            require(model.buckets[j].width==wanted&&model.buckets[j].low==before.buckets[j].low
                &&model.buckets[j].samples==before.buckets[j].samples,
                    "repair commits precisely the independently reconstructed selected mask");
            if(model.buckets[j].width){kept_mass+=model.buckets[j].samples;kept_cells+=model.buckets[j].width;}
        }
        require(model.cells==(result.accepted?oracle.retained_cells:before.cells),
                "rejected repair leaves fixed-grid cells unchanged");
        if(result.accepted)require(kept_mass>=u64((t.sample+1)/2)&&kept_cells<=t.budget,
                                    "accepted repair meets original-sample mass and width budget");
        auto plain_model=before;
        const auto plain=brc_certified_detail::repair_fixed_grid<false>(plain_model,included,t.budget,nullptr,nullptr);
        require(plain.method==result.method&&plain.accepted==result.accepted&&plain_model.cells==model.cells,
                "direct repair nullptr decision parity");
        for(std::size_t j=0;j<model.buckets.size();++j)
            require(plain_model.buckets[j].width==model.buckets[j].width,"direct repair nullptr mask parity");
        ++checked;
    }
    for(auto method:{CertifiedMethod::singleton,CertifiedMethod::fractional_reject,
                     CertifiedMethod::dp_accept,CertifiedMethod::dp_reject})
        require(methods.contains(method),"all certificate helper outcomes exercised");
    repair_methods_seen.insert(methods.begin(),methods.end());return checked;
}

void check_mechanism(const Condition& c,const Candidate& candidate,const CertifiedStats& s) {
    if(candidate.preceding||c.stage!="mechanism")return;
    const auto& q=s.selection.adaptive.trace.front().core.core;
    const auto& node=s.selection.trace.front();const auto& certified=s.trace.front();
    require(!certified.trials.empty(),"mechanism reaches a failed greedy repair");
    const auto& t=certified.trials.front();
    if(c.kind==Kind::dp_witness||c.kind==Kind::hidden_majority) {
        require(certified.selected_method==CertifiedMethod::dp_accept&&!certified.selected_round
            &&t.original_cells==80000&&t.best_single_samples==410&&t.fractional_upper_floor==655
            &&t.dp_optimal_mass==614&&node.selected_learning_samples==614&&node.selected_cells==50000
            &&!node.density_selected&&!node.trials.front().selected&&!node.trials.front().mass_ok,
                "realizable exact-mass repair and truthful greedy failure");
        if(c.kind==Kind::dp_witness)require(q.path==SamplePath::recursive_spill_merge
            &&q.child_size>0&&q.child_size<=41024,"exact repair real population majority");
        else require(q.path==SamplePath::recursive_spill_radix&&q.spills==c.n/2+1&&!q.child_size
            &&certified.trials.size()==1,"sample certificate never bypasses actual majority rejection");
    } else if(c.kind==Kind::singleton_witness) {
        require(certified.selected_method==CertifiedMethod::singleton&&t.retained_samples==1000
            &&t.retained_cells==50000&&!t.fractional_checked&&!t.dp_attempted
            &&q.path==SamplePath::recursive_spill_merge&&q.child_size<=3024,
                "best singleton repairs density packing without DP");
    } else if(c.kind==Kind::fractional_witness) {
        require(t.method==CertifiedMethod::fractional_reject&&t.fractional_upper_floor==342
            &&!t.dp_attempted&&t.half_mass_infeasible_certified,
                "fractional certificate rejects the fixed grid before DP");
    }
}

void verify() {
    u64 exhaustive=0,lifted=0,random=0,focused=0,frozen_outputs=0;
    constexpr std::array<u64,4> alphabet{0,1,MAX_VALUE-1,MAX_VALUE};
    for(unsigned length=0;length<=4;++length)for(u64 code=0;code<(u64(1)<<(2*length));++code) {
        std::vector<u64> word(length);auto value=code;
        for(auto& x:word){x=alphabet[value%4];value/=4;}
        check_input(word);++exhaustive;
        if(length) {std::vector<u64> a(257+length);
            for(std::size_t i=0;i<a.size();++i)a[i]=word[i%length];
            check_input(a);++lifted;}
    }
    std::mt19937_64 rng(0x4345525449465645ull);
    for(std::size_t n:{std::size_t(255),std::size_t(256),std::size_t(257),std::size_t(1023),
        std::size_t(1024),std::size_t(1025),std::size_t(8192),std::size_t(16384)})
        for(unsigned mode=0;mode<4;++mode) {
            std::vector<u64> a(n);for(auto& x:a)x=mode==0?rng():mode==1?MAX_VALUE-bounded(rng,8192)
                :mode==2?bounded(rng,4096):(u64(1)<<48)+bounded(rng,20)*(u64(1)<<20)+bounded(rng,8);
            check_input(a,true);++random;
        }
    const auto helper_cases=verify_repair_helpers();
    for(const auto& c:conditions())if(c.stage=="mechanism")for(unsigned bank:{0u,1u}) {
        const auto stats=check_input(input_bank(c,bank),true);check_mechanism(c,candidates().back(),stats);++focused;
    }
    // These ten exact banks were already measured in phase three. No new
    // phase-four held-out generator is invoked anywhere in --verify.
    for(const auto& c:conditions())if(c.stage=="calibration") {check_input(input_bank(c,0),true);++focused;}
    for(std::size_t hidden:{std::size_t(4096),std::size_t(4097)}) {
        std::vector<u64> a(8192,42);const auto free=robust_experiment::nonsampled_positions(a.size());
        for(std::size_t i=0;i<hidden;++i)a[free[i]]=MAX_VALUE;
        const auto s=check_input(a,true);require(s.selection.adaptive.trace.front().core.core.spills==hidden,
                                               "certified exact half / half-plus-one boundary");++focused;
    }
    {
        const auto child=mechanism_input(Kind::dp_witness,100000);
        const auto s=check_input(sampled_experiment::embed_hidden_child(250000,MAX_VALUE,child),true);
        require(s.trace.size()>1&&s.trace[1].selected_method==CertifiedMethod::dp_accept,
                "exact repair independently checked below the root");++focused;
    }
    check_input(sampled_experiment::hidden_chain(131072,4,0,3),true);++focused;
    {
        std::vector<u64> depth(500);for(auto& x:depth)x=rng();auto expected=depth;
        std::sort(expected.begin(),expected.end());auto actual=depth;CertifiedStats s;
        brc_certified_detail::certified_impl<true>(actual,&s,16);
        require(actual==expected,"certified forced-depth output");check_certified(s,depth,16);
        actual=depth;brc_certified_detail::certified_impl<false>(actual,nullptr,16);
        require(actual==expected,"certified forced-depth nullptr output");checked_outputs+=2;++checked_inputs;++focused;
    }
    // Exercise every frozen wrapper through both its real diagnostic function
    // and its actual timing function; older exhaustive receipts remain intact.
    std::vector<std::vector<u64>> controls{{},std::vector<u64>(257),mechanism_input(Kind::dp_witness,100000)};
    for(std::size_t i=0;i<controls[1].size();++i)controls[1][i]=i%2?MAX_VALUE:0;
    controls.emplace_back(4096);for(auto& x:controls.back())x=rng();
    for(const auto& input:controls) {
        auto expected=input;std::sort(expected.begin(),expected.end());
        const auto shape=sampled_experiment::input_shape(expected);
        for(const auto& c:candidates())if(c.preceding) {check_one(c,input,expected,shape);frozen_outputs+=2;}
        ++checked_inputs;++focused;
    }
    for(const auto* path:{"trivial","small_std_sort","recursive_depth_radix",
                         "exact_mass_spill_merge","exact_mass_spill_radix","singleton_spill_merge"})
        if(!paths_seen.contains(path))throw std::runtime_error(std::string("missing certified route: ")+path);
    std::cout<<"{\"result\":\"PASS\",\"algorithm_candidates\":27,\"new_variants_checked\":1"
        <<",\"verified_input_arrays\":"<<checked_inputs<<",\"verified_algorithm_outputs\":"<<checked_outputs
        <<",\"exhaustive_short_arrays\":"<<exhaustive<<",\"lifted_arrays\":"<<lifted
        <<",\"random_boundary_arrays\":"<<random<<",\"focused_cases\":"<<focused
        <<",\"frozen_control_outputs\":"<<frozen_outputs
        <<",\"frozen_parity_reference_outputs\":"<<parity_reference_outputs
        <<",\"no_accepted_repair_parity_cases\":"<<parity_decisions
        <<",\"repair_helper_cases\":"<<helper_cases<<",\"repair_methods_exercised\":"<<repair_methods_seen.size()
        <<",\"paths_exercised\":"<<paths_seen.size()
        <<",\"independent_exact_subset_oracle_checked\":true,\"independent_full_row_reconstruction_checked\":true"
        <<",\"all_node_membership_oracle_checked\":true,\"actual_half_gate_checked\":true"
        <<",\"greedy_diagnostics_remain_truthful\":true,\"fresh_heldout_banks_evaluated\":false}\n";
}

robust_experiment::Metrics metrics(const CertifiedStats& s) {
    auto m=selection_experiment::metrics(s.selection);
#define ADD(field) m[#field]=s.field
    ADD(singleton_checks);ADD(singleton_accepts);ADD(fractional_checks);ADD(fractional_rejects);
    ADD(dp_attempts);ADD(dp_accepts);ADD(dp_rejects);ADD(dp_cell_transitions_total);
    ADD(dp_reachable_transitions_total);ADD(dp_improvements_total);ADD(repair_auxiliary_bytes_peak);
#undef ADD
    m["certified_trials"]=0;m["certified_selected_sample_mass_total"]=0;
    for(const auto& node:s.trace)for(const auto& t:node.trials) {
        ++m["certified_trials"];m["certified_selected_sample_mass_total"]+=t.retained_samples;
    }
    return m;
}

std::string root_path(const Candidate& c,const CertifiedStats& s) {
    return c.preceding?selection_experiment::root_path(*c.preceding,s.selection)
        :certified_node_path_name(s.trace.front(),s.selection.trace.front(),s.selection.adaptive.trace.front());
}
std::string terminal_path(const Candidate& c,const CertifiedStats& s) {
    return c.preceding?selection_experiment::terminal_path(*c.preceding,s.selection)
        :certified_node_path_name(s.trace.back(),s.selection.trace.back(),s.selection.adaptive.trace.back());
}

void write_node(std::ostream& out,const Condition& c,unsigned bank,const Candidate& candidate,
                const AdaptiveNodeStats& old,const SelectionNodeStats* selection,const CertifiedNodeStats* certified) {
    const auto& r=old.core;const auto& q=r.core;SelectionNodeStats fallback;
    fallback.prefix_output_writes=q.emitted_values;fallback.total_output_writes=q.emitted_values+q.merge_writes;
    const auto& node=selection?*selection:fallback;
    const auto path=certified?certified_node_path_name(*certified,node,old)
        :selection?selection_node_path_name(node,old):adaptive_node_path_name(old);
    const bool selector=candidate.preceding?candidate.preceding->selector:true;
    const bool fused=candidate.preceding?candidate.preceding->fused:true;
    out<<c.stage<<','<<c.original_stage<<','<<c.family<<','<<c.n<<','<<bank<<','<<candidate.timing.name
        <<','<<q.depth<<','<<q.input_size<<','<<q.sample_count<<','<<q.learning_visits
        <<','<<q.processed<<','<<q.covered<<','<<q.spills<<','<<q.full_data_visits<<','<<q.child_size
        <<','<<q.shift<<','<<q.origin<<','<<q.buckets<<','<<q.active_buckets
        <<','<<sampled_experiment::decimal128(q.counter_cells_demanded)<<','<<q.counter_cells_allocated
        <<','<<q.emitted_values<<','<<q.merge_writes<<','<<q.radix_passes<<','<<path
        <<','<<bool(certified)<<','<<selector<<','<<fused
        <<','<<r.compact_accepted<<','<<r.compact_from_trim<<','<<r.compact_low<<','<<r.compact_high
        <<','<<r.compact_width<<','<<r.trim_attempted<<','<<r.trim_cut<<','<<r.trim_low<<','<<r.trim_high
        <<','<<sampled_experiment::decimal128(r.original_cells)
        <<','<<sampled_experiment::decimal128(r.trimmed_cells)
        <<','<<old.selected_attempt<<','<<old.chosen_cut<<','<<old.prune_accepted
        <<','<<node.density_selected<<','<<node.gap_selected<<','<<node.gap_repairs<<','<<node.sample_sorted
        <<','<<node.selected_low<<','<<node.selected_high<<','<<node.selected_learning_samples
        <<','<<node.selected_cells<<','<<node.fused_output<<','<<node.prefix_output_writes
        <<','<<node.direct_output_writes<<','<<node.total_output_writes<<','<<old.actual_spill_failure
        <<','<<node.trials.size()<<','<<old.attempts.size()
        <<','<<certified_method_name(certified?certified->selected_method:CertifiedMethod::none)
        <<','<<(certified?certified->selected_round:0)<<','<<(certified?certified->trials.size():0)<<'\n';
}

void write_certified_trial(std::ostream& out,const Condition& c,unsigned bank,const Candidate& candidate,
                           unsigned depth,const CertifiedTrialStats& t,const Model& source,
                           const RepairOracle& repair) {
    out<<c.stage<<','<<c.original_stage<<','<<c.family<<','<<c.n<<','<<bank<<','<<candidate.timing.name
        <<','<<depth<<','<<t.round<<','<<t.window_begin<<','<<t.window_end<<','<<t.low<<','<<t.high
        <<','<<t.original_sample_size<<','<<t.included_samples<<','<<t.minimum_mass<<','<<t.budget
        <<','<<t.feasible_bins<<','<<t.feasible_samples<<','<<sampled_experiment::decimal128(t.original_cells)
        <<','<<t.singleton_checked<<','<<t.best_single_found<<','<<t.best_single_index
        <<','<<t.best_single_samples<<','<<t.best_single_width<<','<<t.fractional_checked
        <<','<<t.fractional_rejected<<','<<t.fractional_prefix_mass
        <<','<<sampled_experiment::decimal128(t.fractional_numerator)<<','<<t.fractional_denominator
        <<','<<t.fractional_upper_floor<<','<<t.dp_attempted<<','<<t.dp_accepted<<','<<t.dp_infeasible
        <<','<<t.optimal_mass_certified<<','<<t.half_mass_infeasible_certified
        <<','<<t.dp_mass_limit<<','<<t.dp_items<<','<<t.dp_cell_transitions<<','<<t.dp_reachable_transitions
        <<','<<t.dp_improvements<<','<<t.dp_optimal_mass<<','<<t.dp_width_vector_bytes<<','<<t.dp_take_bits_bytes
        <<','<<t.auxiliary_vector_bytes<<','<<t.selected<<','<<certified_method_name(t.method)
        <<','<<t.retained_samples<<','<<t.retained_bins<<','<<t.retained_cells
        <<','<<source.grid.origin<<','<<source.grid.shift<<','<<source.bins.size()<<',';
    // Sparse bin records use index:low:width:sample_mass separated by semicolons.
    // Empty grid slots are recoverable from bucket_slots and these indices.
    bool first=true;
    for(std::size_t j=0;j<source.bins.size();++j)if(source.bins[j].width) {
        if(!first)out<<';';
        first=false;const auto& b=source.bins[j];
        out<<j<<':'<<b.low<<':'<<b.width<<':'<<b.samples;
    }
    out<<',';first=true;
    // A negative repair commits no change. An accepted repair uses the unique
    // declared tie policy, independently reconstructed by the full-row oracle.
    for(std::size_t j=0;j<source.bins.size();++j)
        if(source.bins[j].width&&(!t.selected||repair.keep[j])) {
            if(!first)out<<';';
            first=false;out<<j;
        }
    out<<",independent_full_row_reconstruction\n";
}

void write_headers(std::ostream& file,std::ostream& nodes,std::ostream& attempts,std::ostream& selection_attempts) {
    nodes<<"stage,original_stage,family,n,bank,algorithm,depth,input_size,sample_count,learning_visits,processed,"
        <<"covered,spills,full_data_visits,child_size,shift,origin,buckets,active_buckets,counter_cells_demanded,"
        <<"counter_cells_allocated,emitted_values,merge_writes,radix_passes,path,repair_enabled,selector_enabled,"
        <<"fused_enabled,compact_accepted,compact_from_trim,compact_low,compact_high,compact_width,trim_attempted,"
        <<"trim_cut,trim_low,trim_high,original_cells,trimmed_cells,selected_attempt,chosen_cut,prune_accepted,"
        <<"density_selected,gap_selected,gap_repairs,sample_sorted,selected_low,selected_high,selected_learning_samples,"
        <<"selected_cells,fused_output,prefix_output_writes,direct_output_writes,total_output_writes,"
        <<"actual_spill_failure,selection_trial_count,quantile_attempt_count,selected_method,selected_round,certified_trial_count\n";
    attempts<<"stage,original_stage,family,n,bank,algorithm,depth,round,window_begin,window_end,low,high,"
        <<"original_sample_size,included_samples,minimum_mass,budget,feasible_bins,feasible_samples,original_cells,"
        <<"singleton_checked,best_single_found,best_single_index,best_single_samples,best_single_width,"
        <<"fractional_checked,fractional_rejected,fractional_prefix_mass,fractional_numerator,fractional_denominator,"
        <<"fractional_upper_floor,dp_attempted,dp_accepted,dp_infeasible,optimal_mass_certified,"
        <<"half_mass_infeasible_certified,dp_mass_limit,dp_items,dp_cell_transitions,dp_reachable_transitions,"
        <<"dp_improvements,dp_optimal_mass,dp_width_vector_bytes,dp_take_bits_bytes,auxiliary_vector_bytes,selected,method,"
        <<"retained_samples,retained_bins,retained_cells,grid_origin,grid_shift,bucket_slots,"
        <<"original_nonempty_bins,committed_bin_indices,layout_reconstruction\n";
    selection_attempts<<"stage,original_stage,family,n,bank,algorithm,depth,attempt_kind,round,window_begin,window_end,"
        <<"low,high,included_samples,bucket_slots,original_cells,retained_cells,compact_selected,grid_selected,"
        <<"density_attempted,density_selected,mass_ok,selected,density_order_size,density_work_bytes,"
        <<"retained_samples,retained_bins,omitted_samples,omitted_bins,omitted_cells,gap_applied,kept_lower,"
        <<"gap_index,gap_size,quantile_cut,old_prune_attempted,old_prune_selected,old_prune_mass_ok,"
        <<"old_prune_order_size,old_prune_order_vector_bytes\n";
    file<<"stage,original_stage,family,n,seed_regime,seed_tag,algorithm,value_bytes,banks,rounds,median_us,p10_us,p90_us,"
        <<"min_us,max_us,calls_per_round,mean_distinct,mean_min,mean_max,mean_numeric_span";
    for(const auto& [name,value]:metrics(CertifiedStats{}))file<<','<<name;
    file<<",path,path_mix,terminal_path,terminal_path_mix";
    for(unsigned round=1;round<=7;++round)file<<",round"<<round<<"_us";
    file<<'\n';
}

struct TraceRows {u64 nodes=0,repairs=0,selection=0;};
TraceRows write_traces(std::ostream& nodes,std::ostream& attempts,std::ostream& selection_attempts,
                       const Condition& c,unsigned bank,const Candidate& candidate,
                       const CertifiedStats& stats,const std::vector<u64>& input) {
    TraceRows rows;const auto& s=stats.selection;
    selection_experiment::Condition old_condition;
    old_condition.family=c.family;old_condition.stage=c.stage;old_condition.original_stage=c.original_stage;
    old_condition.regime=c.regime;old_condition.n=c.n;
    selection_experiment::Candidate proxy{candidate.timing,nullptr,nullptr,true,true};
    const auto& old_candidate=candidate.preceding?*candidate.preceding:proxy;
    if(!s.adaptive.trace.empty()) {
        std::vector<u64> current;if(!candidate.preceding)current=input;
        for(std::size_t i=0;i<s.adaptive.trace.size();++i) {
            const auto& old=s.adaptive.trace[i];const auto& q=old.core.core;
            const auto* node=s.trace.empty()?nullptr:&s.trace[i];
            const auto* certified=stats.trace.empty()?nullptr:&stats.trace[i];
            write_node(nodes,c,bank,candidate,old,node,certified);++rows.nodes;
            rows.selection+=selection_experiment::write_attempts(selection_attempts,old_condition,bank,old_candidate,old,node);
            if(certified) {
                if(!certified->trials.empty()) {
                    std::vector<u64> sample;
                    for(auto pos:brc_sampled_detail::sample_indices(current.size(),1024))sample.push_back(current[pos]);
                    for(const auto& t:certified->trials) {
                        const auto source=adaptive_experiment::reconstruct(sample,t.low,t.high);
                        const auto repair=repair_oracle(source.bins,sample.size(),brc_sampled_detail::cell_budget(current.size()));
                        write_certified_trial(attempts,c,bank,candidate,unsigned(q.depth),t,source,repair);++rows.repairs;
                    }
                }
                if(q.child_size) {
                    const auto model=selected_model(stats,i,current);std::vector<u64> next;next.reserve(q.child_size);
                    for(u64 x:current) {
                        bool covered=false;
                        if(x>=model.grid.origin) {
                            const auto j=(x-model.grid.origin)>>model.grid.shift;
                            if(j<model.bins.size()) {const auto& b=model.bins[j];
                                covered=b.width&&x>=b.low&&u128(x)<u128(b.low)+b.width;}
                        }
                        if(!covered)next.push_back(x);
                    }
                    require(next.size()==q.child_size,"raw trace child input reconstruction");current=std::move(next);
                }
            }
        }
    } else if(!s.adaptive.robust.trace.empty())for(const auto& r:s.adaptive.robust.trace) {
        AdaptiveNodeStats wrapper;wrapper.core=r;write_node(nodes,c,bank,candidate,wrapper,nullptr,nullptr);++rows.nodes;
    } else for(const auto& r:s.adaptive.robust.sample.recursion_trace) {
        AdaptiveNodeStats wrapper;wrapper.core.core=r;write_node(nodes,c,bank,candidate,wrapper,nullptr,nullptr);++rows.nodes;
    }
    return rows;
}

void benchmark(const std::string& output_path,std::size_t max_n,double target_seconds,const std::string& subset) {
    constexpr unsigned BANKS=8,ROUNDS=7;const auto& all=candidates();const auto A=all.size();
    require(A==27&&target_seconds>0&&target_seconds<=1,"valid certified candidates and target seconds");
    std::ofstream file(output_path),nodes(output_path+".certified_nodes.csv"),attempts(output_path+".certified_attempts.csv"),
        selection_attempts(output_path+".selection_attempts.csv");
    require(bool(file)&&bool(nodes)&&bool(attempts)&&bool(selection_attempts),"cannot open certified outputs");
    write_headers(file,nodes,attempts,selection_attempts);const auto names=metrics(CertifiedStats{});
    file<<std::setprecision(21);nodes<<std::setprecision(21);attempts<<std::setprecision(21);
    selection_attempts<<std::setprecision(21);
    u64 completed=0,rows=0,banks_checked=0,node_rows=0,repair_rows=0,selection_rows=0;
    for(const auto& c:conditions()) {
        if(c.n>max_n||!selected(c,subset))continue;
        std::vector<std::vector<u64>> banks;
        for(unsigned bank=0;bank<BANKS;++bank)banks.push_back(input_bank(c,bank));
        std::vector<std::vector<CertifiedStats>> diagnostics(A);
        long double distinct=0,minimum=0,maximum=0,span=0;
        for(unsigned bank=0;bank<BANKS;++bank) {
            const auto& input=banks[bank];auto expected=input;std::sort(expected.begin(),expected.end());
            const auto shape=sampled_experiment::input_shape(expected);
            distinct+=shape.distinct;minimum+=shape.minimum;maximum+=shape.maximum;span+=shape.span;
            for(std::size_t ai=0;ai<A;++ai) {
                auto s=check_one(all[ai],input,expected,shape);check_mechanism(c,all[ai],s);
                const auto counts=write_traces(nodes,attempts,selection_attempts,c,bank,all[ai],s,input);
                node_rows+=counts.nodes;repair_rows+=counts.repairs;selection_rows+=counts.selection;
                diagnostics[ai].push_back(std::move(s));
            }
            selection_experiment::compare_decisions(diagnostics[22].back().selection.adaptive,
                                                     diagnostics[23].back().selection.adaptive);
            selection_experiment::compare_decisions(diagnostics[24].back().selection.adaptive,
                                                     diagnostics[25].back().selection.adaptive);
            check_parity(diagnostics[26].back(),diagnostics[25].back().selection);++banks_checked;
        }
        std::vector<std::size_t> cycles(A),order(A);std::vector<std::vector<double>> times(A);
        for(std::size_t ai=0;ai<A;++ai) {
            const auto one=timed(all[ai].timing,banks,1,0);
            cycles[ai]=std::clamp<std::size_t>(std::size_t(target_seconds/std::max(one,1e-9)+.999),1,100000);
        }
        std::mt19937_64 order_rng(0x4345525449464f52ull+c.n+completed*31337);
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
            file<<c.stage<<','<<c.original_stage<<','<<c.family<<','<<c.n<<','<<c.regime<<','<<c.tag
                <<','<<all[ai].timing.name<<','<<sizeof(u64)<<','<<BANKS<<','<<ROUNDS
                <<','<<quantile(times[ai],.5)<<','<<quantile(times[ai],.1)<<','<<quantile(times[ai],.9)
                <<','<<*std::min_element(times[ai].begin(),times[ai].end())
                <<','<<*std::max_element(times[ai].begin(),times[ai].end())<<','<<cycles[ai]*BANKS
                <<','<<distinct/BANKS<<','<<minimum/BANKS<<','<<maximum/BANKS<<','<<span/BANKS;
            for(const auto& [name,value]:names)file<<','<<totals[name]/BANKS;
            file<<','<<(paths.size()==1?paths.begin()->first:"mixed")<<','<<robust_experiment::mix_string(paths)
                <<','<<(terminals.size()==1?terminals.begin()->first:"mixed")<<','<<robust_experiment::mix_string(terminals);
            for(auto value:times[ai])file<<','<<value;
            file<<'\n';++rows;
        }
        ++completed;file.flush();nodes.flush();attempts.flush();selection_attempts.flush();
        std::cerr<<"completed "<<c.stage<<' '<<c.family<<" n="<<c.n<<'\n';
    }
    require(completed>0,"no selected certified conditions");
    std::cout<<"{\"result\":\"PASS\",\"conditions\":"<<completed<<",\"rows\":"<<rows
        <<",\"validated_input_banks\":"<<banks_checked<<",\"algorithms\":"<<A
        <<",\"banks\":8,\"rounds\":7,\"trace_nodes\":"<<node_rows<<",\"trace_attempts\":"<<repair_rows
        <<",\"selection_trace_attempts\":"<<selection_rows
        <<",\"validated_algorithm_outputs\":"<<checked_outputs<<",\"no_accepted_repair_parity_cases\":"<<parity_decisions
        <<",\"target_seconds_per_algorithm_round\":"<<target_seconds
        <<",\"copy_setup_allocation_output_destruction_included\":true"
        <<",\"all_bank_unchanged_policy_decisions_checked\":true,\"observable_sink\":"<<observed<<"}\n";
}

} // namespace certified_experiment

int main(int argc,char** argv) {
    try {
        if(argc==2&&std::string_view(argv[1])=="--verify")certified_experiment::verify();
        else if(argc==2&&std::string_view(argv[1])=="--list") {
            std::cout<<"stage,original_stage,family,n,seed_regime,seed_tag\n";
            for(const auto& c:certified_experiment::conditions())std::cout<<c.stage<<','<<c.original_stage<<','
                <<c.family<<','<<c.n<<','<<c.regime<<','<<c.tag<<'\n';
        } else if(argc>=3&&std::string_view(argv[1])=="--bench")
            certified_experiment::benchmark(argv[2],argc>3?std::stoull(argv[3]):1000000,
                argc>4?std::stod(argv[4]):.012,argc>5?argv[5]:"all");
        else {std::cerr<<"usage: certified_bench --verify | --list | --bench output.csv "
            <<"[max_n=1000000] [target_seconds=.012] [subset=all]\n";return 2;}
    } catch(const std::exception& error){std::cerr<<error.what()<<'\n';return 1;}
    return 0;
}

