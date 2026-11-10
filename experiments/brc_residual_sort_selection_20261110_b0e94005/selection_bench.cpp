// Phase three: retain all twenty-three frozen candidates and add three policies.
#ifndef BRC_ADAPTIVE_SOURCE
#define BRC_ADAPTIVE_SOURCE "build/adaptive_frozen_include.hpp"
#endif
#include BRC_ADAPTIVE_SOURCE
#include "selection_kernels.hpp"

namespace selection_experiment {

template<void (*Function)(std::vector<u64>&,SelectionStats*)>
void time_selection(std::vector<u64>& values,Stats*) { Function(values,nullptr); }

struct Candidate {
    Algorithm timing;
    const adaptive_experiment::Candidate* preceding=nullptr;
    void (*diagnostic)(std::vector<u64>&,SelectionStats*)=nullptr;
    bool selector=false,fused=false;
};

const std::vector<Candidate>& candidates() {
    static const auto result=[] {
        std::vector<Candidate> out;
        for(const auto& c:adaptive_experiment::candidates())out.push_back({c.timing,&c});
        out.push_back({{"selection_fused_1024",time_selection<selection_fused_1024>},
                       nullptr,selection_fused_1024,false,true});
        out.push_back({{"selection_density_gap_1024",time_selection<selection_density_gap_1024>},
                       nullptr,selection_density_gap_1024,true,false});
        out.push_back({{"selection_combined_1024",time_selection<selection_combined_1024>},
                       nullptr,selection_combined_1024,true,true});
        return out;
    }();return result;
}

enum class Kind {old,tails,popular_wide,rare_wide,interior,many_clusters,narrow,uniform,
                 density_witness,gap_witness,hidden_majority,output_positions};
struct Condition {
    adaptive_experiment::Condition source;
    std::string family,stage,original_stage,regime;
    std::size_t n=0;
    Kind kind=Kind::old;
    u64 tag=0,low_per_100000=0,high_per_100000=0;
    bool mirror=false;
};

std::vector<Condition> conditions() {
    const auto old=adaptive_experiment::conditions();
    std::vector<Condition> out;
    for(const auto* name:{"adaptive_fresh_tail_2p5pct_high","adaptive_fresh_tail_7pct_high",
        "adaptive_fresh_tail_20pct_high","adaptive_fresh_tail_30pct_high",
        "adaptive_fresh_tail_12pct_both","adaptive_fresh_tail_40pct_both",
        "adaptive_fresh_interior_contamination","adaptive_fresh_128clusters_8pct_tail"}) {
        auto it=std::find_if(old.begin(),old.end(),[&](const auto& c){return c.family==name;});
        require(it!=old.end(),"missing exact phase-two calibration");
        out.push_back({*it,name,"calibration","phase2_"+it->stage,
            "exact_previously_measured_phase2_banks",it->n});
    }
    const auto fresh=[&](const char* name,std::size_t n,Kind kind,u64 tag,
                         u64 low=0,u64 high=0,bool mirror=false) {
        out.push_back({{},name,"heldout","new_phase3",
            kind==Kind::tails&&(tag==601||tag==604)?"new_seed_banks_matched_value_mirror":
                "new_selection_v1_seed_banks",n,kind,tag,low,high,mirror});
    };
    // These recipes are frozen before any fresh bank is generated or timed.
    // Mirrored pairs intentionally share a stream and differ by MAX_VALUE-x.
    fresh("selection_fresh_tail_8pct_high",1000000,Kind::tails,601,0,8000);
    fresh("selection_fresh_tail_8pct_low",1000000,Kind::tails,601,0,8000,true);
    fresh("selection_fresh_tail_12pct_asymmetric",1000000,Kind::tails,602,2000,10000);
    fresh("selection_fresh_tail_15pct_high",100000,Kind::tails,604,0,15000);
    fresh("selection_fresh_tail_15pct_low",100000,Kind::tails,604,0,15000,true);
    fresh("selection_fresh_popular_wide",100000,Kind::popular_wide,606);
    fresh("selection_fresh_rare_wide",100000,Kind::rare_wide,607);
    fresh("selection_fresh_interior_contamination",100000,Kind::interior,608);
    fresh("selection_fresh_128clusters_12pct_tail",250000,Kind::many_clusters,609);
    fresh("selection_fresh_narrow_offsets",1000000,Kind::narrow,610);
    fresh("selection_fresh_uniform_uint64",1000000,Kind::uniform,611);
    fresh("selection_fresh_tail_40pct_asymmetric",100000,Kind::tails,612,5000,35000);
    const auto witness=[&](const char* name,std::size_t n,Kind kind) {
        out.push_back({{},name,"mechanism","new_phase3",
            "constructed_actual_sampler_positions",n,kind});
    };
    witness("witness_density_mass_width",100000,Kind::density_witness);
    witness("witness_gap_300_sample_tails",100000,Kind::gap_witness);
    witness("witness_density_hidden_majority",100000,Kind::hidden_majority);
    witness("witness_fused_tail_position",100000,Kind::output_positions);
    require(out.size()==24,"selection matrix contains24 conditions");return out;
}

bool selected(const Condition& c,const std::string& subset) {
    if(subset.empty()||subset=="all")return true;
    if(subset=="heldout"||subset=="evaluation")return c.stage=="heldout";
    if(subset=="calibration"||subset=="mechanism")return c.stage==subset;
    return c.family.find(subset)!=std::string::npos;
}

std::vector<u64> density_witness(std::size_t n,unsigned bank=0,bool hidden=false) {
    const u64 a=(u64(1)<<48)+u64(bank)*(u64(1)<<36);
    const std::array<u64,3> lo{a,a+(u64(256)<<16),a+(u64(512)<<16)};
    const std::array<u64,3> width{37539,44802,18841};
    std::vector<u64> input(n);
    for(std::size_t i=0;i<n;++i) {
        const auto j=i%100<90?1u:i%100<95?0u:2u;
        input[i]=lo[j]+((i*7919+bank*101)%width[j]);
    }
    const auto idx=brc_sampled_detail::sample_indices(n,1024);
    require(idx.size()==1024,"density witness has1024 actual sample positions");
    for(std::size_t i=0;i<idx.size();++i) {
        const auto j=i<60?0u:i<960?1u:2u;
        input[idx[i]]=lo[j]+(i%2?width[j]-1:0);
    }
    if(hidden)for(auto i:robust_experiment::nonsampled_positions(n))input[i]=lo[0];
    return input;
}

std::vector<u64> output_witness(std::size_t n,unsigned bank=0) {
    const u64 a=(u64(1)<<48)+u64(bank)*(u64(1)<<30);
    const u64 tail=bank%2?0:MAX_VALUE;
    std::vector<u64> input(n);for(std::size_t i=0;i<n;++i)input[i]=a+i%1024;
    const auto idx=brc_sampled_detail::sample_indices(n,1024);
    for(std::size_t i=0;i<idx.size();++i)input[idx[i]]=a+i;
    const auto free=robust_experiment::nonsampled_positions(n);
    for(std::size_t i=0;i<n*8/100;++i)input[free[i]]=tail;
    return input;
}

std::vector<u64> input_bank(const Condition& c,unsigned bank) {
    if(c.kind==Kind::old)return adaptive_experiment::input_bank(c.source,bank);
    if(c.kind==Kind::density_witness||c.kind==Kind::hidden_majority)
        return density_witness(c.n,bank,c.kind==Kind::hidden_majority);
    if(c.kind==Kind::gap_witness)return robust_experiment::trim_witness(c.n,300,c.n*3/10,bank);
    if(c.kind==Kind::output_positions)return output_witness(c.n,bank);
    std::mt19937_64 rng(0x53454C4543545631ull^(u64(c.n)*0x9e3779b97f4a7c15ull)
        ^(u64(bank)*0xD1B54A32D192ED03ull)^(c.tag*0x94D049BB133111EBull));
    const u64 origin=(u64(1)<<62)+bounded(rng,u64(1)<<28);
    std::array<u64,20> offsets{};for(auto& x:offsets)x=bounded(rng,u64(1)<<18);
    const auto core=[&] {const auto j=bounded(rng,20);
        return origin+j*(u64(1)<<20)+offsets[j]+bounded(rng,8);};
    std::vector<u64> input(c.n);
    switch(c.kind) {
    case Kind::tails:
    case Kind::narrow:
        for(auto& x:input)x=core();
        if(c.kind==Kind::tails) {
            const auto low=c.n*c.low_per_100000/100000;
            const auto high=c.n*c.high_per_100000/100000;
            for(std::size_t i=0;i<low;++i)input[i]=bounded(rng,4096);
            for(std::size_t i=low;i<low+high;++i)input[i]=MAX_VALUE-bounded(rng,4096);
            std::shuffle(input.begin(),input.end(),rng);
        }
        if(c.mirror)for(auto& x:input)x=MAX_VALUE-x;
        break;
    case Kind::popular_wide:
    case Kind::rare_wide:
        for(auto& x:input) {
            const auto chance=c.kind==Kind::popular_wide?80u:2u;
            const auto j=bounded(rng,100)<chance?0:1+bounded(rng,19);
            x=origin+j*(u64(1)<<25)+bounded(rng,j==0?24000:12000);
        }break;
    case Kind::interior:
        for(auto& x:input)x=origin+bounded(rng,2)*(u64(1)<<40)+bounded(rng,8);
        for(std::size_t i=0;i<c.n*7/1000;++i)
            input[i]=origin+(u64(1)<<39)+bounded(rng,u64(1)<<30);
        std::shuffle(input.begin(),input.end(),rng);break;
    case Kind::many_clusters:
        for(auto& x:input)x=(u64(1)<<56)+bounded(rng,128)*(u64(1)<<25)+bounded(rng,8);
        for(std::size_t i=0;i<c.n*12/100;++i)input[i]=(u64(1)<<60)+bounded(rng,8);
        std::shuffle(input.begin(),input.end(),rng);break;
    case Kind::uniform:for(auto& x:input)x=rng();break;
    default:throw std::runtime_error("unhandled phase-three generator");
    }
    return input;
}

std::set<std::string> paths_seen;
u64 checked_inputs=0,checked_outputs=0;

std::string node_path(const Candidate& c,const SelectionStats& s,std::size_t i) {
    (void)c;return selection_node_path_name(s.trace[i],s.adaptive.trace[i]);
}

struct DensityOracle {
    std::vector<unsigned char> keep;
    u64 samples=0,bins=0,order_size=0;
    u128 cells=0;
    bool mass_ok=false,accepted=false;
};

DensityOracle density_oracle(const std::vector<brc_sampled_detail::Bucket>& bins,
                             std::size_t original_sample,std::size_t budget) {
    // Independent order construction: repeatedly choose the greatest rational
    // density from all unvisited rows, instead of sorting the kernel's order.
    DensityOracle result;result.keep.assign(bins.size(),0);
    std::vector<unsigned char> visited(bins.size(),0);
    for(const auto& b:bins)result.order_size+=b.width!=0;
    const auto better=[&](std::size_t a,std::size_t b) {
        const auto& x=bins[a];const auto& y=bins[b];
        if(u128(x.samples)*y.width!=u128(y.samples)*x.width)
            return u128(x.samples)*y.width>u128(y.samples)*x.width;
        if(x.samples!=y.samples)return x.samples>y.samples;
        if(x.width!=y.width)return x.width<y.width;
        return a<b;
    };
    for(std::size_t round=0;round<result.order_size;++round) {
        std::size_t best=bins.size();
        for(std::size_t j=0;j<bins.size();++j)
            if(bins[j].width&&!visited[j]&&(best==bins.size()||better(j,best)))best=j;
        require(best<bins.size(),"density oracle remaining row");visited[best]=1;
        if(result.cells+bins[best].width<=budget) {
            result.keep[best]=1;result.cells+=bins[best].width;
            result.samples+=bins[best].samples;++result.bins;
        }
    }
    result.mass_ok=u128(2)*result.samples>=original_sample;
    result.accepted=result.bins&&result.mass_ok;return result;
}

brc_selection_detail::GapChoice gap_oracle(const std::vector<u64>& sorted,
                                          std::size_t begin,std::size_t end,
                                          std::size_t minimum_mass) {
    // Enumerate admissible splits, then select their explicit (gap,-index) key.
    struct Option {u64 width;std::size_t index,low_mass,high_mass;};
    std::vector<Option> options;
    for(std::size_t i=begin+1;i<end;++i) {
        const auto lo=i-begin,hi=end-i;
        if(sorted[i]!=sorted[i-1]&&(lo>=minimum_mass||hi>=minimum_mass))
            options.push_back({sorted[i]-sorted[i-1],i,lo,hi});
    }
    if(options.empty())return {};
    std::sort(options.begin(),options.end(),[](const auto& a,const auto& b) {
        return a.width!=b.width?a.width>b.width:a.index<b.index;
    });
    const auto& x=options.front();const bool lower=x.low_mass>=x.high_mass;
    return {true,x.index,x.width,lower,lower?begin:x.index,lower?x.index:end};
}

using Model=adaptive_experiment::RootOracle;

Model compact_model(u64 low,u64 high,std::size_t sample_size,std::size_t included,
                    std::size_t budget) {
    const u128 span=u128(high)-low+1;
    require(span<=budget,"compact oracle width fits");
    const u128 pad=std::max<u128>(8,4*span/(sample_size+1));
    const u128 left_max=std::min<u128>(low,pad),right_max=std::min<u128>(MAX_VALUE-high,pad);
    const u128 spare=budget-span;
    u128 left=std::min(left_max,spare/2),right=std::min(right_max,spare-left);
    const auto left_extra=std::min(left_max-left,spare-left-right);left+=left_extra;
    right+=std::min(right_max-right,spare-left-right);
    Model o;o.cells=span+left+right;o.included=included;
    o.grid={u64(u128(low)-left),unsigned(std::bit_width(u64(o.cells)-1)),1};
    o.bins.resize(1);o.bins[0].low=o.grid.origin;o.bins[0].width=u64(o.cells);
    o.bins[0].samples=included;return o;
}

Model selected_model(const Candidate& c,const SelectionStats& s,std::size_t index,
                     const std::vector<u64>& input) {
    const auto& old=s.adaptive.trace[index];const auto& r=old.core;const auto& q=r.core;
    const auto& node=s.trace[index];const auto budget=brc_sampled_detail::cell_budget(input.size());
    std::vector<u64> sample;
    for(auto i:brc_sampled_detail::sample_indices(input.size(),1024))sample.push_back(input[i]);
    auto sorted=sample;std::sort(sorted.begin(),sorted.end());
    require(q.sample_count==sample.size()&&r.sample_minimum==sorted.front()
        &&r.sample_maximum==sorted.back(),"actual node sample and bounds oracle");
    auto original=adaptive_experiment::reconstruct(sample,sorted.front(),sorted.back());
    require(r.original_cells==original.cells&&r.initial_bucket_slots==original.bins.size(),
            "original grid oracle");
    if(!c.selector) {
        require(node.trials.empty()&&!node.sample_sorted&&!node.gap_repairs
            &&!node.density_selected&&!node.gap_selected,"fused ablation has no new selector work");
        for(const auto& a:old.attempts)require(a.low==sorted[a.cut]
            &&a.high==sorted[sorted.size()-a.cut-1],"unchanged quantile rank oracle");
        if(!q.counter_cells_allocated)return {};
        if(r.compact_accepted) {
            const auto low=old.selected_attempt?r.trim_low:r.sample_minimum;
            const auto high=old.selected_attempt?r.trim_high:r.sample_maximum;
            const auto included=old.selected_attempt?r.trim_included_samples:sample.size();
            auto o=compact_model(low,high,sample.size(),included,budget);
            require(r.compact_low==o.bins[0].low&&r.compact_width==o.bins[0].width,
                    "fused ablation compact oracle");return o;
        }
        auto o=adaptive_experiment::reconstruct(sample,old.selected_attempt?r.trim_low:r.sample_minimum,
                                               old.selected_attempt?r.trim_high:r.sample_maximum);
        if(old.prune_accepted)adaptive_experiment::oracle_prune(o,budget);
        return o;
    }
    require(!node.trials.empty()&&node.trials.size()<=4&&node.trials.size()==node.gap_repairs+1,
            "bounded selector trial count");
    std::size_t begin=0,end=sample.size();Model chosen;bool found=false;
    for(std::size_t i=0;i<node.trials.size();++i) {
        const auto& t=node.trials[i];
        require(t.round==i,"trial round sequence");
        if(i) {
            const auto g=gap_oracle(sorted,begin,end,(sample.size()+1)/2);
            require(g.found&&t.gap_applied&&t.gap_index==g.index&&t.gap_size==g.gap
                &&t.kept_lower==g.keep_lower,"independent admissible gap and tie oracle");
            begin=g.next_begin;end=g.next_end;
        } else require(!t.gap_applied&&!t.gap_index&&!t.gap_size,"original trial has no gap");
        require(t.window_begin==begin&&t.window_end==end&&t.low==sorted[begin]
            &&t.high==sorted[end-1]&&t.included_samples==end-begin,
                "gap window preserves original-sample observation mass");
        auto proposal=adaptive_experiment::reconstruct(sample,t.low,t.high);
        require(t.original_cells==proposal.cells&&t.bucket_slots==proposal.bins.size()
            &&proposal.included==t.included_samples,"trial raw grid oracle");
        const bool compact=u128(t.high)-t.low+1<=budget;
        const bool grid=!compact&&proposal.cells<=budget;
        require(t.compact_selected==compact&&t.grid_selected==grid
            &&t.density_attempted==(!compact&&!grid),"first feasible representation order");
        if(compact)proposal=compact_model(t.low,t.high,sample.size(),end-begin,budget);
        if(t.density_attempted) {
            const auto d=density_oracle(proposal.bins,sample.size(),budget);
            require(t.retained_cells==d.cells&&t.retained_samples==d.samples
                &&t.retained_bins==d.bins&&t.density_order_size==d.order_size
                &&t.omitted_cells==proposal.cells-d.cells
                &&t.omitted_samples==proposal.included-d.samples
                &&t.omitted_bins==d.order_size-d.bins&&t.mass_ok==d.mass_ok
                &&t.density_selected==d.accepted,"independent density packing oracle");
            if(d.accepted) {
                for(std::size_t j=0;j<proposal.bins.size();++j)
                    if(!d.keep[j])proposal.bins[j].width=0;
                proposal.cells=d.cells;
            }
        } else {
            const auto bins=std::count_if(proposal.bins.begin(),proposal.bins.end(),
                                          [](const auto& b){return b.width>0;});
            require(t.retained_cells==proposal.cells&&t.retained_samples==end-begin
                &&t.retained_bins==u64(bins)&&t.mass_ok&&!t.density_selected
                &&!t.density_order_size&&!t.density_work_bytes&&!t.omitted_cells
                &&!t.omitted_samples&&!t.omitted_bins,"ordinary trial mass and cells");
        }
        const bool accepted=compact||grid||t.density_selected;
        require(t.selected==accepted,"model acceptance decision");
        if(accepted) {
            require(i+1==node.trials.size(),"first viable model receives sole actual scan");
            chosen=std::move(proposal);found=true;
        }
    }
    require(node.sample_sorted==!node.trials.front().selected,"sample sort work trigger");
    require(node.gap_selected==(found&&node.trials.back().round>0)
        &&node.density_selected==(found&&node.trials.back().density_selected),"selected model flags");
    require(found==(q.counter_cells_allocated>0),"model choice separate from scan result");
    return chosen;
}

void check_selection(const Candidate& c,const SelectionStats& s,const std::vector<u64>& input,
                     unsigned starting_depth=0) {
    const auto& a=s.adaptive;const auto& sum=a.robust.sample;
    require(!s.trace.empty()&&s.trace.size()==a.trace.size()&&s.trace.size()==a.robust.trace.size()
        &&s.trace.size()==sum.recursion_trace.size(),"aligned selection traces");
    require(a.trace.front().core.core.input_size==input.size()
        &&a.trace.front().core.core.depth==starting_depth,"selection root");
    u64 inputs=0,samples=0,processed=0,spills=0,cells=0,emitted=0,merged=0;
    u64 direct=0,prefix=0,writes=0,density_attempts=0,density_accepts=0,mass_rejects=0;
    u64 gap_repairs=0,sorts=0,work_peak=0,radix=0,small=0,trivial=0,counted=0;
    std::vector<u64> actual_node=input;
    for(std::size_t i=0;i<s.trace.size();++i) {
        const auto& old=a.trace[i];const auto& q=old.core.core;const auto& node=s.trace[i];
        const auto& mirror=sum.recursion_trace[i];const auto budget=brc_sampled_detail::cell_budget(q.input_size);
        paths_seen.insert(node_path(c,s,i));
        require(q.depth==starting_depth+i&&q.depth<=16&&q.input_size==actual_node.size()
            &&q.input_size==mirror.input_size&&q.path==mirror.path,"trace actual descent");
        require(q.processed==q.covered+q.spills&&q.processed<=q.input_size
            &&q.full_data_visits==q.processed&&q.counter_cells_allocated<=budget,
                "actual population and counter budget");
        const bool early=q.path==SamplePath::trivial||q.path==SamplePath::small_std_sort
            ||q.path==SamplePath::recursive_depth_radix;
        require(q.sample_count==(early?0:std::min<u64>(q.input_size,1024)),"sample size and leaf cutoff");
        std::vector<u64> next;
        if(!early) {
            auto model=selected_model(c,s,i,actual_node);
            if(q.counter_cells_allocated) {
                require(model.cells==q.counter_cells_allocated&&model.cells==q.counter_cells_demanded
                    &&model.grid.origin==q.origin&&model.grid.shift==q.shift,"selected geometry");
                u64 retained=0,lo=MAX_VALUE,hi=0;
                for(const auto& b:model.bins)if(b.width) {
                    retained+=b.samples;lo=std::min(lo,b.low);hi=std::max(hi,u64(u128(b.low)+b.width-1));
                }
                require(node.selected_cells==model.cells&&node.selected_learning_samples==retained
                    &&old.selected_learning_samples==retained&&u128(2)*retained>=q.sample_count
                    &&node.selected_low==lo&&node.selected_high==hi,"selected mass and envelope");
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
                        "all-node actual prefix membership oracle");
            } else require(!q.processed&&!node.selected_cells&&!node.selected_learning_samples,
                            "unselected layout never scans input");
        } else require(node.trials.empty()&&!node.sample_sorted&&!node.gap_repairs
            &&!node.selected_cells&&!node.selected_learning_samples,"early leaf has no model work");
        const bool output=q.path==SamplePath::recursive_count||q.path==SamplePath::recursive_spill_merge;
        if(output) {
            require(q.processed==q.input_size&&q.spills<=q.input_size/2
                &&q.emitted_values==q.covered,"successful exact count/spill partition");
            if(c.fused)require(node.fused_output&&node.direct_output_writes==q.input_size
                &&!node.prefix_output_writes&&!q.merge_writes,"fused output writes exactlyn");
            else require(!node.fused_output&&!node.direct_output_writes
                &&node.prefix_output_writes==q.covered&&q.merge_writes>=q.spills
                &&q.merge_writes<=q.input_size,"legacy prefix and merge accounting");
        } else require(!q.emitted_values&&!q.merge_writes&&!node.prefix_output_writes
            &&!node.direct_output_writes&&!node.fused_output,"fallback output tracked separately");
        require(node.total_output_writes==node.prefix_output_writes+node.direct_output_writes+q.merge_writes,
                "disjoint output write accounting");
        require(node.actual_spill_failure==(q.path==SamplePath::recursive_spill_radix)
            &&old.actual_spill_failure==node.actual_spill_failure,"model accepted versus scan accepted");
        switch(q.path) {
        case SamplePath::recursive_spill_merge:
            require(q.spills>0&&q.child_size==q.spills&&i+1<s.trace.size(),"actual half child");
            actual_node=std::move(next);break;
        case SamplePath::recursive_count:require(!q.spills&&!q.child_size,"count leaf");++counted;break;
        case SamplePath::recursive_spill_radix:
            require(q.spills==q.input_size/2+1&&!q.child_size,"half-plus-one abort");++radix;break;
        case SamplePath::recursive_cell_radix:require(!q.processed&&!q.child_size,"model fallback");++radix;break;
        case SamplePath::recursive_depth_radix:require(q.depth==16&&q.input_size>256,"depth fallback");++radix;break;
        case SamplePath::small_std_sort:require(q.input_size>=2&&q.input_size<=256,"small cutoff");++small;break;
        case SamplePath::trivial:require(q.input_size<2,"trivial cutoff");++trivial;break;
        default:throw std::runtime_error("unexpected selection node path");
        }
        if(q.path!=SamplePath::recursive_spill_merge)require(i+1==s.trace.size(),"single terminal node");
        for(const auto& t:node.trials) {
            density_attempts+=t.density_attempted;density_accepts+=t.density_selected;
            mass_rejects+=t.density_attempted&&!t.mass_ok;work_peak=std::max(work_peak,t.density_work_bytes);
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
            "recursive aggregates");
    require(s.density_attempts==density_attempts&&s.density_accepts==density_accepts
        &&s.density_mass_rejects==mass_rejects&&s.density_work_bytes_peak==work_peak
        &&s.gap_repairs_total==gap_repairs&&s.sample_sorts==sorts
        &&s.prefix_output_writes_total==prefix&&s.direct_output_writes_total==direct
        &&s.total_output_writes_total==writes,"selection aggregates");
    require(radix+small+trivial+counted==1&&u128(inputs)<=u128(input.size())*2
        &&u128(cells)<=u128(input.size())+u128(4096)*s.trace.size(),"half contraction totals");
}

void compare_decisions(const AdaptiveStats& a,const AdaptiveStats& b) {
    require(a.trace.size()==b.trace.size(),"ablation recursion length");
    for(std::size_t i=0;i<a.trace.size();++i) {
        const auto& x=a.trace[i];const auto& y=b.trace[i];
        const auto& p=x.core.core;const auto& q=y.core.core;
        require(p.path==q.path&&p.input_size==q.input_size&&p.depth==q.depth
            &&p.sample_count==q.sample_count&&p.learning_visits==q.learning_visits
            &&p.processed==q.processed&&p.covered==q.covered&&p.spills==q.spills
            &&p.child_size==q.child_size&&p.origin==q.origin&&p.shift==q.shift
            &&p.counter_cells_demanded==q.counter_cells_demanded
            &&p.counter_cells_allocated==q.counter_cells_allocated
            &&x.selected_attempt==y.selected_attempt&&x.chosen_cut==y.chosen_cut
            &&x.selected_learning_samples==y.selected_learning_samples
            &&x.prune_accepted==y.prune_accepted&&x.actual_spill_failure==y.actual_spill_failure
            &&x.core.compact_low==y.core.compact_low&&x.core.compact_width==y.core.compact_width
            &&x.omitted_bins==y.omitted_bins&&x.omitted_samples==y.omitted_samples
            &&x.omitted_cells==y.omitted_cells&&x.attempts.size()==y.attempts.size(),
                "ablation preserves model and actual residual decisions");
        for(std::size_t j=0;j<x.attempts.size();++j) {
            const auto& u=x.attempts[j];const auto& v=y.attempts[j];
            require(u.cut==v.cut&&u.low==v.low&&u.high==v.high&&u.selected==v.selected
                &&u.prune_selected==v.prune_selected&&u.retained_samples==v.retained_samples
                &&u.retained_cells==v.retained_cells,"ablation retains old attempt decisions");
        }
    }
}

SelectionStats check_one(const Candidate& c,const std::vector<u64>& input,
                         const std::vector<u64>& expected,const sampled_experiment::InputShape& shape) {
    SelectionStats s;
    if(c.preceding)s.adaptive=adaptive_experiment::check_one(*c.preceding,input,expected,shape,nullptr);
    else {
        auto actual=input;c.diagnostic(actual,&s);
        if(actual!=expected)throw std::runtime_error(std::string("selection diagnostic output: ")+c.timing.name);
        check_selection(c,s,input);
        actual=input;c.timing.run(actual,nullptr);
        if(actual!=expected)throw std::runtime_error(std::string("selection nullptr output: ")+c.timing.name);
    }
    checked_outputs+=2;return s;
}

u64 frozen_ablation_outputs=0;
std::vector<SelectionStats> check_input(const std::vector<u64>& input,bool compare_previous=false) {
    auto expected=input;std::sort(expected.begin(),expected.end());
    const auto shape=sampled_experiment::input_shape(expected);std::vector<SelectionStats> result;
    for(const auto& c:candidates())if(c.diagnostic)result.push_back(check_one(c,input,expected,shape));
    compare_decisions(result[1].adaptive,result[2].adaptive);
    if(compare_previous) {
        auto actual=input;AdaptiveStats old;adaptive_combined_1024(actual,&old);
        require(actual==expected,"frozen ablation reference output");
        compare_decisions(old,result[0].adaptive);++frozen_ablation_outputs;++checked_outputs;
    }
    ++checked_inputs;return result;
}

u64 verify_density_helpers() {
    struct Test {std::vector<u64> widths,mass;std::size_t budget,sample;};
    const std::vector<Test> tests={
        {{60000,40000,20000},{900,60,64},60000,1024},
        {{45000,40000,20000},{900,60,64},50000,1024},
        {{10,20,10,20},{1,2,1,2},30,6},{{10,10,10},{2,2,2},10,6},
        {{u64(1)<<54,1,2},{1000,12,12},3,1024},{{0,0},{0,0},0,1024},
        {{4096,1},{512,512},4096,1024},{{50001,2},{800,224},50000,1024}};
    for(const auto& t:tests) {
        brc_sampled_detail::SampledLayout model;model.sample.resize(t.sample);
        model.grid={0,16,t.widths.size()};model.buckets.resize(t.widths.size());u64 included=0;
        for(std::size_t i=0;i<t.widths.size();++i) {
            auto& b=model.buckets[i];b.low=i*(u64(1)<<16);b.width=t.widths[i];b.samples=t.mass[i];
            model.cells+=b.width;included+=b.samples;
        }
        const auto before=model;const auto expected=density_oracle(model.buckets,t.sample,t.budget);
        SampleStats stats;SelectionTrialStats trial;
        const auto actual=brc_selection_detail::pack_density<true>(model,included,t.budget,&stats,&trial);
        require(actual.accepted==expected.accepted&&actual.retained_cells==expected.cells
            &&actual.retained_samples==expected.samples&&actual.retained_bins==expected.bins,
                "direct density helper independent oracle");
        for(std::size_t i=0;i<model.buckets.size();++i) {
            const auto wanted=expected.accepted&&!expected.keep[i]?0:before.buckets[i].width;
            require(model.buckets[i].width==wanted&&model.buckets[i].low==before.buckets[i].low
                &&model.buckets[i].samples==before.buckets[i].samples,
                    "density commits exactly accepted keep set; rejected proposal unchanged");
        }
        auto uninstrumented=before;
        const auto plain=brc_selection_detail::pack_density<false>(uninstrumented,included,t.budget,nullptr,nullptr);
        require(plain.accepted==actual.accepted&&uninstrumented.cells==model.cells,"density nullptr parity");
        for(std::size_t i=0;i<model.buckets.size();++i)
            require(uninstrumented.buckets[i].width==model.buckets[i].width,"density nullptr keep set");
    }
    return tests.size();
}

u64 verify_gap_helpers() {
    u64 checks=0;
    constexpr std::array<u64,4> alphabet{0,1,10,MAX_VALUE};
    for(std::size_t size=1;size<=6;++size)for(u64 code=0;code<(u64(1)<<(2*size));++code) {
        std::vector<u64> sample(size);u64 word=code;
        for(auto& x:sample){x=alphabet[word%4];word/=4;}std::sort(sample.begin(),sample.end());
        const auto minimum=(size+1)/2;
        for(std::size_t begin=0;begin<size;++begin)for(std::size_t end=begin+minimum;end<=size;++end) {
            const auto actual=brc_selection_detail::choose_majority_gap(sample,begin,end,minimum);
            const auto expected=gap_oracle(sample,begin,end,minimum);
            require(actual.found==expected.found&&actual.index==expected.index&&actual.gap==expected.gap
                &&actual.keep_lower==expected.keep_lower&&actual.next_begin==expected.next_begin
                &&actual.next_end==expected.next_end,"exhaustive finite gap helper oracle");++checks;
        }
    }
    return checks;
}

u64 verify_fused_helper() {
    using B=brc_sampled_detail::Bucket;
    struct Test {std::vector<B> bins;std::vector<std::size_t> counts;std::vector<u64> spills;};
    const std::vector<Test> tests={
        {{{100,3,0,1}},{2,0,3},{}},
        {{{100,3,0,1}},{2,0,3},{0,99}},
        {{{100,3,0,1}},{2,0,3},{103,MAX_VALUE}},
        {{{100,3,0,1}},{2,0,3},{0,99,103,MAX_VALUE}},
        {{{10,2,0,1},{15,0,2,1},{20,1,2,1}},{1,2,3},{0,12,15,19,21,MAX_VALUE}},
        {{{0,1,0,1},{MAX_VALUE,1,1,1}},{2,1},{1,MAX_VALUE-1}}};
    for(const auto& t:tests) {
        std::vector<u64> expected=t.spills;
        for(const auto& b:t.bins)for(std::size_t j=0;j<b.width;++j)
            expected.insert(expected.end(),t.counts[b.begin+j],b.low+j);
        std::sort(expected.begin(),expected.end());std::vector<u64> actual(expected.size(),777);
        const auto writes=brc_selection_detail::emit_fused(actual,t.bins,t.counts,t.spills);
        require(actual==expected&&writes==expected.size(),"direct fused output multiplicity and exact writes");
    }
    return tests.size();
}

template<bool Selector,bool Fused>
void check_forced(const Candidate& c,const std::vector<u64>& input) {
    auto expected=input;std::sort(expected.begin(),expected.end());auto actual=input;SelectionStats stats;
    brc_selection_detail::selection_impl<Selector,Fused,true>(actual,&stats,16);
    require(actual==expected,"selection forced-depth diagnostic");check_selection(c,stats,input,16);
    actual=input;brc_selection_detail::selection_impl<Selector,Fused,false>(actual,nullptr,16);
    require(actual==expected,"selection forced-depth nullptr");checked_outputs+=2;
}

void check_mechanism(const Condition& c,const Candidate& candidate,const SelectionStats& s) {
    if(!candidate.diagnostic||c.stage!="mechanism")return;
    const auto& q=s.adaptive.trace.front().core.core;const auto& r=s.trace.front();
    if((c.kind==Kind::density_witness||c.kind==Kind::hidden_majority)&&candidate.selector) {
        require(r.density_selected&&!r.gap_selected&&r.selected_cells==45000
            &&r.selected_learning_samples==900,"realizable density mass-width mechanism");
        if(c.kind==Kind::density_witness)require(q.child_size<=11024&&q.child_size>0
            &&q.path==SamplePath::recursive_spill_merge,"density actual population bound");
        else require(q.spills==c.n/2+1&&!q.child_size
            &&q.path==SamplePath::recursive_spill_radix,"hidden majority actual rejection");
    }
    if(c.kind==Kind::gap_witness&&candidate.selector)
        require(r.gap_selected&&r.gap_repairs==1&&r.selected_learning_samples==724
            &&q.spills==c.n*3/10&&q.path==SamplePath::recursive_spill_merge,
                "largest gap removes300sampletails retaining724core observations");
    if(c.kind==Kind::output_positions)require(q.spills==c.n*8/100
        &&q.path==SamplePath::recursive_spill_merge,"fixed actual tail count output witness");
}

void verify() {
    u64 exhaustive=0,lifted=0,random=0,focused=0;
    constexpr std::array<u64,4> alphabet{0,1,MAX_VALUE-1,MAX_VALUE};
    for(unsigned length=0;length<=4;++length)for(u64 code=0;code<(u64(1)<<(2*length));++code) {
        std::vector<u64> word(length);auto value=code;for(auto& x:word){x=alphabet[value%4];value/=4;}
        check_input(word);++exhaustive;
        if(length) {std::vector<u64> a(257+length);for(std::size_t i=0;i<a.size();++i)a[i]=word[i%length];
            check_input(a);++lifted;}
    }
    std::mt19937_64 rng(0x53454c4543545645ull);
    for(std::size_t n:{std::size_t(255),std::size_t(256),std::size_t(257),std::size_t(1023),
        std::size_t(1024),std::size_t(1025),std::size_t(8192),std::size_t(16384)})
        for(unsigned mode=0;mode<4;++mode) {
            std::vector<u64> a(n);for(auto& x:a)x=mode==0?rng():mode==1?MAX_VALUE-bounded(rng,8192)
                :mode==2?bounded(rng,4096):(u64(1)<<48)+bounded(rng,20)*(u64(1)<<20)+bounded(rng,8);
            check_input(a,true);++random;
        }
    const auto density_checks=verify_density_helpers();const auto gap_checks=verify_gap_helpers();
    const auto fused_checks=verify_fused_helper();
    for(const auto& c:conditions())if(c.stage=="mechanism")for(unsigned bank:{0u,1u}) {
        const auto stats=check_input(input_bank(c,bank),true);
        for(std::size_t i=0;i<stats.size();++i)check_mechanism(c,candidates()[23+i],stats[i]);
        ++focused;
    }
    // Known calibration only; fresh generation remains outside --verify.
    for(const auto& c:conditions())if(c.stage=="calibration") {check_input(input_bank(c,0),true);++focused;}
    for(std::size_t hidden:{std::size_t(4096),std::size_t(4097)}) {
        std::vector<u64> a(8192,42);const auto free=robust_experiment::nonsampled_positions(a.size());
        for(std::size_t i=0;i<hidden;++i)a[free[i]]=MAX_VALUE;
        const auto stats=check_input(a,true);++focused;
        for(const auto& s:stats)require(s.adaptive.trace.front().core.core.spills==hidden,
                                       "actual exact-half / half-plus-one boundary");
    }
    {
        const auto child=density_witness(100000);
        check_input(sampled_experiment::embed_hidden_child(250000,MAX_VALUE,child),true);++focused;
    }
    check_input(sampled_experiment::hidden_chain(131072,4,0,3),true);++focused;
    std::vector<u64> depth(500);for(auto& x:depth)x=rng();
    check_forced<false,true>(candidates()[23],depth);check_forced<true,false>(candidates()[24],depth);
    check_forced<true,true>(candidates()[25],depth);++checked_inputs;++focused;
    for(const auto* name:{"trivial","small_std_sort","recursive_depth_radix",
                         "density_spill_merge","density_spill_radix","gap_spill_merge"})
        if(!paths_seen.contains(name))throw std::runtime_error(std::string("missing selection route: ")+name);
    std::cout<<"{\"result\":\"PASS\",\"algorithm_candidates\":26,\"new_variants_checked\":3"
        <<",\"verified_input_arrays\":"<<checked_inputs<<",\"verified_algorithm_outputs\":"<<checked_outputs
        <<",\"exhaustive_short_arrays\":"<<exhaustive<<",\"lifted_arrays\":"<<lifted
        <<",\"random_boundary_arrays\":"<<random<<",\"focused_cases\":"<<focused
        <<",\"frozen_ablation_reference_outputs\":"<<frozen_ablation_outputs
        <<",\"density_helper_cases\":"<<density_checks<<",\"gap_helper_cases\":"<<gap_checks
        <<",\"fused_helper_cases\":"<<fused_checks<<",\"paths_exercised\":"<<paths_seen.size()
        <<",\"all_node_membership_oracle_checked\":true,\"output_ablation_decisions_checked\":true"
        <<",\"new_selector_output_parity_checked\":true,\"fresh_heldout_banks_evaluated\":false}\n";
}

robust_experiment::Metrics metrics(const SelectionStats& s) {
    auto m=adaptive_experiment::metrics(s.adaptive);
#define ADD(field) m[#field]=s.field
    ADD(density_attempts);ADD(density_accepts);ADD(density_mass_rejects);ADD(density_work_bytes_peak);
    ADD(gap_repairs_total);ADD(sample_sorts);ADD(prefix_output_writes_total);
    ADD(direct_output_writes_total);ADD(total_output_writes_total);
#undef ADD
    if(s.trace.empty()) {
        m["prefix_output_writes_total"]=s.adaptive.robust.sample.recursive_emitted_total;
        m["total_output_writes_total"]=m["prefix_output_writes_total"]
            +s.adaptive.robust.sample.recursive_merge_writes_total;
    }
    m["selection_trials"]=0;m["selection_retained_samples_total"]=0;m["selection_selected_cells_total"]=0;
    for(const auto& n:s.trace) {
        m["selection_trials"]+=n.trials.size();
        m["selection_retained_samples_total"]+=n.selected_learning_samples;
        m["selection_selected_cells_total"]+=n.selected_cells;
    }
    return m;
}

std::string root_path(const Candidate& c,const SelectionStats& s) {
    return c.preceding?adaptive_experiment::root_path(*c.preceding,s.adaptive):node_path(c,s,0);
}
std::string terminal_path(const Candidate& c,const SelectionStats& s) {
    return c.preceding?adaptive_experiment::terminal_path(*c.preceding,s.adaptive)
        :node_path(c,s,s.trace.size()-1);
}

void write_node(std::ostream& out,const Condition& c,unsigned bank,const Candidate& candidate,
                const AdaptiveNodeStats& old,const SelectionNodeStats* selected_node) {
    const auto& r=old.core;const auto& q=r.core;SelectionNodeStats fallback;
    fallback.prefix_output_writes=q.emitted_values;
    fallback.total_output_writes=q.emitted_values+q.merge_writes;
    const auto& node=selected_node?*selected_node:fallback;
    const auto path=selected_node?selection_node_path_name(node,old):adaptive_node_path_name(old);
    out<<c.stage<<','<<c.original_stage<<','<<c.family<<','<<c.n<<','<<bank<<','<<candidate.timing.name
        <<','<<q.depth<<','<<q.input_size<<','<<q.sample_count<<','<<q.learning_visits
        <<','<<q.processed<<','<<q.covered<<','<<q.spills<<','<<q.full_data_visits<<','<<q.child_size
        <<','<<q.shift<<','<<q.origin<<','<<q.buckets<<','<<q.active_buckets
        <<','<<sampled_experiment::decimal128(q.counter_cells_demanded)<<','<<q.counter_cells_allocated
        <<','<<q.emitted_values<<','<<q.merge_writes<<','<<q.radix_passes<<','<<path
        <<','<<bool(selected_node)<<','<<candidate.selector<<','<<candidate.fused
        <<','<<r.compact_accepted<<','<<r.compact_from_trim<<','<<r.compact_low<<','<<r.compact_high
        <<','<<r.compact_width<<','<<r.trim_attempted<<','<<r.trim_cut<<','<<r.trim_low<<','<<r.trim_high
        <<','<<sampled_experiment::decimal128(r.original_cells)
        <<','<<sampled_experiment::decimal128(r.trimmed_cells)
        <<','<<old.selected_attempt<<','<<old.chosen_cut<<','<<old.prune_accepted
        <<','<<node.density_selected<<','<<node.gap_selected<<','<<node.gap_repairs<<','<<node.sample_sorted
        <<','<<node.selected_low<<','<<node.selected_high<<','<<node.selected_learning_samples
        <<','<<node.selected_cells<<','<<node.fused_output<<','<<node.prefix_output_writes
        <<','<<node.direct_output_writes<<','<<node.total_output_writes
        <<','<<old.actual_spill_failure<<','<<node.trials.size()<<','<<old.attempts.size()<<'\n';
}

void write_trial(std::ostream& out,const Condition& c,unsigned bank,const Candidate& candidate,
                 unsigned depth,const char* kind,const SelectionTrialStats& t,
                 const AdaptiveAttemptStats* old=nullptr) {
    out<<c.stage<<','<<c.original_stage<<','<<c.family<<','<<c.n<<','<<bank<<','<<candidate.timing.name
        <<','<<depth<<','<<kind<<','<<t.round<<','<<t.window_begin<<','<<t.window_end
        <<','<<t.low<<','<<t.high<<','<<t.included_samples<<','<<t.bucket_slots
        <<','<<sampled_experiment::decimal128(t.original_cells)
        <<','<<sampled_experiment::decimal128(t.retained_cells)
        <<','<<t.compact_selected<<','<<t.grid_selected<<','<<t.density_attempted<<','<<t.density_selected
        <<','<<t.mass_ok<<','<<t.selected<<','<<t.density_order_size<<','<<t.density_work_bytes
        <<','<<t.retained_samples<<','<<t.retained_bins<<','<<t.omitted_samples<<','<<t.omitted_bins
        <<','<<sampled_experiment::decimal128(t.omitted_cells)<<','<<t.gap_applied<<','<<t.kept_lower
        <<','<<t.gap_index<<','<<t.gap_size<<','<<(old?old->cut:0)
        <<','<<(old?old->prune_attempted:false)<<','<<(old?old->prune_selected:false)
        <<','<<(old?old->prune_mass_ok:false)<<','<<(old?old->prune_order_size:0)
        <<','<<(old?old->prune_order_vector_bytes:0)<<'\n';
}

u64 write_attempts(std::ostream& out,const Condition& c,unsigned bank,const Candidate& candidate,
                  const AdaptiveNodeStats& old,const SelectionNodeStats* node) {
    u64 rows=0;
    for(std::size_t i=0;i<old.attempts.size();++i) {
        const auto& a=old.attempts[i];SelectionTrialStats t;
        t.round=i+1;t.low=a.low;t.high=a.high;t.included_samples=a.included_samples;
        t.bucket_slots=a.bucket_slots;t.original_cells=a.trimmed_cells;t.retained_cells=a.retained_cells;
        t.compact_selected=a.compact_selected;t.grid_selected=a.grid_accepted;
        t.mass_ok=a.prune_attempted?a.prune_mass_ok:true;t.selected=a.selected;
        t.retained_samples=a.retained_samples;t.omitted_samples=a.omitted_samples;
        t.omitted_bins=a.omitted_bins;t.omitted_cells=a.omitted_cells;
        write_trial(out,c,bank,candidate,unsigned(old.core.core.depth),"quantile",t,&a);++rows;
    }
    if(node)for(const auto& t:node->trials) {
        write_trial(out,c,bank,candidate,unsigned(old.core.core.depth),"density_gap",t);++rows;
    }
    return rows;
}

void benchmark(const std::string& output_path,std::size_t max_n,double target_seconds,const std::string& subset) {
    constexpr unsigned BANKS=8,ROUNDS=7;const auto& all=candidates();const auto A=all.size();
    require(A==26&&target_seconds>0&&target_seconds<=1,"valid candidates and target_seconds");
    std::ofstream file(output_path),nodes(output_path+".selection_nodes.csv"),attempts(output_path+".selection_attempts.csv");
    require(bool(file)&&bool(nodes)&&bool(attempts),"cannot open selection outputs");
    nodes<<"stage,original_stage,family,n,bank,algorithm,depth,input_size,sample_count,learning_visits,processed,"
        <<"covered,spills,full_data_visits,child_size,shift,origin,buckets,active_buckets,counter_cells_demanded,"
        <<"counter_cells_allocated,emitted_values,merge_writes,radix_passes,path,new_variant,selector_enabled,"
        <<"fused_enabled,compact_accepted,compact_from_trim,compact_low,compact_high,compact_width,trim_attempted,"
        <<"trim_cut,trim_low,trim_high,original_cells,trimmed_cells,selected_attempt,chosen_cut,prune_accepted,"
        <<"density_selected,gap_selected,gap_repairs,sample_sorted,selected_low,selected_high,selected_learning_samples,"
        <<"selected_cells,fused_output,prefix_output_writes,direct_output_writes,total_output_writes,"
        <<"actual_spill_failure,selection_trial_count,quantile_attempt_count\n";
    attempts<<"stage,original_stage,family,n,bank,algorithm,depth,attempt_kind,round,window_begin,window_end,"
        <<"low,high,included_samples,bucket_slots,original_cells,retained_cells,compact_selected,grid_selected,"
        <<"density_attempted,density_selected,mass_ok,selected,density_order_size,density_work_bytes,"
        <<"retained_samples,retained_bins,omitted_samples,omitted_bins,omitted_cells,gap_applied,kept_lower,"
        <<"gap_index,gap_size,quantile_cut,old_prune_attempted,old_prune_selected,old_prune_mass_ok,"
        <<"old_prune_order_size,old_prune_order_vector_bytes\n";
    const auto names=metrics(SelectionStats{});
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
        std::vector<std::vector<SelectionStats>> diagnostics(A);
        long double distinct=0,minimum=0,maximum=0,span=0;
        for(unsigned bank=0;bank<BANKS;++bank) {
            const auto& input=banks[bank];auto expected=input;std::sort(expected.begin(),expected.end());
            const auto shape=sampled_experiment::input_shape(expected);
            distinct+=shape.distinct;minimum+=shape.minimum;maximum+=shape.maximum;span+=shape.span;
            for(std::size_t ai=0;ai<A;++ai) {
                auto s=check_one(all[ai],input,expected,shape);check_mechanism(c,all[ai],s);
                if(!s.adaptive.trace.empty())for(std::size_t i=0;i<s.adaptive.trace.size();++i) {
                    const auto* node=s.trace.empty()?nullptr:&s.trace[i];
                    write_node(nodes,c,bank,all[ai],s.adaptive.trace[i],node);
                    attempt_rows+=write_attempts(attempts,c,bank,all[ai],s.adaptive.trace[i],node);++node_rows;
                } else if(!s.adaptive.robust.trace.empty())for(const auto& r:s.adaptive.robust.trace) {
                    AdaptiveNodeStats wrapper;wrapper.core=r;write_node(nodes,c,bank,all[ai],wrapper,nullptr);++node_rows;
                } else for(const auto& r:s.adaptive.robust.sample.recursion_trace) {
                    AdaptiveNodeStats wrapper;wrapper.core.core=r;write_node(nodes,c,bank,all[ai],wrapper,nullptr);++node_rows;
                }
                diagnostics[ai].push_back(std::move(s));
            }
            compare_decisions(diagnostics[22].back().adaptive,diagnostics[23].back().adaptive);
            compare_decisions(diagnostics[24].back().adaptive,diagnostics[25].back().adaptive);
            ++banks_checked;
        }
        std::vector<std::size_t> cycles(A),order(A);std::vector<std::vector<double>> times(A);
        for(std::size_t ai=0;ai<A;++ai) {
            const auto one=timed(all[ai].timing,banks,1,0);
            cycles[ai]=std::clamp<std::size_t>(std::size_t(target_seconds/std::max(one,1e-9)+.999),1,100000);
        }
        std::mt19937_64 order_rng(0x53454c4543544f52ull+c.n+completed*31337);
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
    require(completed>0,"no selected conditions");
    std::cout<<"{\"result\":\"PASS\",\"conditions\":"<<completed<<",\"rows\":"<<rows
        <<",\"validated_input_banks\":"<<banks_checked<<",\"algorithms\":"<<A
        <<",\"banks\":8,\"rounds\":7,\"trace_nodes\":"<<node_rows<<",\"trace_attempts\":"<<attempt_rows
        <<",\"validated_algorithm_outputs\":"<<checked_outputs
        <<",\"target_seconds_per_algorithm_round\":"<<target_seconds
        <<",\"copy_setup_allocation_output_destruction_included\":true"
        <<",\"all_bank_ablation_decisions_checked\":true,\"observable_sink\":"<<observed<<"}\n";
}

} // namespace selection_experiment

int main(int argc,char** argv) {
    try {
        if(argc==2&&std::string_view(argv[1])=="--verify")selection_experiment::verify();
        else if(argc==2&&std::string_view(argv[1])=="--list") {
            std::cout<<"stage,original_stage,family,n,seed_regime\n";
            for(const auto& c:selection_experiment::conditions())std::cout<<c.stage<<','<<c.original_stage<<','
                <<c.family<<','<<c.n<<','<<c.regime<<'\n';
        } else if(argc>=3&&std::string_view(argv[1])=="--bench")
            selection_experiment::benchmark(argv[2],argc>3?std::stoull(argv[3]):1000000,
                argc>4?std::stod(argv[4]):.012,argc>5?argv[5]:"all");
        else {std::cerr<<"usage: selection_bench --verify | --list | --bench output.csv "
            <<"[max_n=1000000] [target_seconds=.012] [subset=all]\n";return 2;}
    } catch(const std::exception& error){std::cerr<<error.what()<<'\n';return 1;}
    return 0;
}
