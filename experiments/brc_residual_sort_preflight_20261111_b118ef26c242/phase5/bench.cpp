#include "certified_frozen_include.hpp"
#include "probe.hpp"
#include <filesystem>

namespace pilot_bench {
constexpr unsigned bank_count=8, round_count=5;
enum class Family {known_million, new_million, imbalance, shift, narrow, pollution, uniform, mechanism};
struct Case {const char* name; const char* stage; std::size_t n; Family kind; u64 tag;};
const std::vector<Case> plan{
    {"previous_million","known",1000000,Family::known_million,706},
    {"new_balanced_million","fresh",1000000,Family::new_million,910221},
    {"new_three_37_33_30","fresh",125000,Family::imbalance,910222},
    {"new_wider_shifted","fresh",150000,Family::shift,910223},
    {"new_narrow_offset","fresh",131072,Family::narrow,910224},
    {"new_seven_percent_high","fresh",100000,Family::pollution,910225},
    {"new_uniform64","fresh",100000,Family::uniform,910226},
    {"hidden_population","mechanism",100000,Family::mechanism,0}
};
const char* phase5_names[]={"gate","gate_range","child_range","observe"};

std::vector<u64> make_input(const Case& c,unsigned bank) {
    using namespace certified_experiment;
    if(c.kind==Family::known_million || c.kind==Family::new_million) {
        certified_experiment::Condition previous{{},"certified_fresh_three_bins_million","heldout","new_phase4","",c.n,Kind::large_balanced,c.tag};
        return input_bank(previous,bank);
    }
    if(c.kind==Family::mechanism) return mechanism_input(Kind::hidden_majority,c.n,bank);
    std::mt19937_64 rng(0x4a494e5155414e35ull ^ c.tag*0x9e3779b97f4a7c15ull
                         ^ (u64(bank)+1)*0xD1B54A32D192ED03ull);
    std::vector<u64> v(c.n);
    const u64 base=(u64(1)<<48)+(bounded(rng,u64(1)<<16)<<16);
    for(std::size_t i=0;i<v.size();++i) {
        switch(c.kind) {
        case Family::imbalance: {
            unsigned g=i<c.n*37/100?0:i<c.n*70/100?1:2;
            constexpr u64 widths[]={36512,30853,29221};
            v[i]=base+(u64(g*256)<<16)+bounded(rng,widths[g]);break;
        }
        case Family::shift: {
            unsigned g=i<c.n*43/100?0:i<c.n*69/100?1:2;
            constexpr u64 widths[]={48123,34712,36800};
            v[i]=base+1091+(u64(g*256)<<16)+bounded(rng,widths[g]);break;
        }
        case Family::narrow: v[i]=base+bounded(rng,4093);break;
        case Family::pollution: v[i]=i<c.n*93/100?base+bounded(rng,4093):base+(u64(1)<<42)+bounded(rng,1ull<<28);break;
        case Family::uniform: v[i]=rng();break;
        default: throw std::logic_error("unexpected family");
        }
    }
    std::shuffle(v.begin(),v.end(),rng);
    return v;
}

u64 probe_seed(const Case& c,unsigned bank) {
    // PRNG domain separate from the input generator and round-order generator.
    return 0x394761383775167bull+(c.tag*0xc2b2ae3d27d4eb4full)+u64(bank)*0x165667b19e3779f9ull;
}
void run_probe(unsigned index,std::vector<u64>& v,u64 seed,ProbeStats* stats) {
    switch(index) {
    case 0: probe_sort<ProbeMode::gate>(v,seed,stats);break;
    case 1: probe_sort<ProbeMode::gate_range>(v,seed,stats);break;
    case 2: probe_sort<ProbeMode::child_range>(v,seed,stats);break;
    case 3: probe_sort<ProbeMode::observe>(v,seed,stats);break;
    default: throw std::logic_error("unknown candidate");
    }
}

void run(const std::filesystem::path& dir,bool smoke) {
    using Clock=std::chrono::steady_clock;
    const auto& old=certified_experiment::candidates();
    require(old.size()==27,"phase-four candidate count");
    const auto count=old.size()+3;
    std::filesystem::create_directories(dir);
    std::ofstream times(dir/"timings.csv"),nodes(dir/"nodes.csv");
    require(bool(times)&&bool(nodes),"write result CSV");
    times<<"stage,family,n,bank,round,order,algorithm,ns,probe_seed\n";
    nodes<<"stage,family,bank,algorithm,probe_seed,depth,n,probes,misses,early,actual_misses,scan_visits,range_slots,counter_slots,model_selected,range_sorted,threshold,range_visits\n";
    auto active=smoke?std::vector<Case>{{"smoke","smoke",3000,Family::imbalance,7111}}:plan;
    const unsigned banks=smoke?1:bank_count,rounds=smoke?1:round_count;
    std::size_t num_timings=0,num_diag=0;
    for(const auto& c:active) {
        std::vector<std::vector<u64>> inputs,reference;
        for(unsigned bank=0;bank<banks;++bank) {
            inputs.push_back(make_input(c,bank));
            reference.push_back(inputs.back());
            std::sort(reference.back().begin(),reference.back().end());
            for(unsigned a=0;a<4;++a) {
                auto v=inputs.back();ProbeStats stats;const auto seed=probe_seed(c,bank);
                run_probe(a,v,seed,&stats);
                require(v==reference.back(),"full diagnostic output mismatch");++num_diag;
                for(const auto& node:stats.rows)
                    nodes<<c.stage<<','<<c.name<<','<<bank<<','<<phase5_names[a]<<','<<seed<<','
                         <<node.depth<<','<<node.n<<','<<node.probes<<','<<node.misses<<','<<node.early<<','
                         <<node.actual_misses<<','<<node.scan_visits<<','<<node.range_slots<<','<<node.counter_slots<<','
                         <<node.model_selected<<','<<node.range_sorted<<','<<node.threshold<<','<<node.range_visits<<'\n';
            }
        }
        // Every algorithm sees the identical input bank. Methods and banks are
        // shuffled within rounds; a measured invocation includes the input copy.
        std::mt19937_64 order_rng(0x4f52444552353035ull+c.tag*30323);
        std::vector<unsigned> bank_order(banks),methods(count);
        std::iota(bank_order.begin(),bank_order.end(),0);
        std::iota(methods.begin(),methods.end(),0);
        for(unsigned r=0;r<rounds;++r) {
            std::shuffle(bank_order.begin(),bank_order.end(),order_rng);
            for(unsigned bank:bank_order) {
                std::shuffle(methods.begin(),methods.end(),order_rng);
                for(unsigned j=0;j<count;++j) {
                    const unsigned m=methods[j];
                    const auto seed=probe_seed(c,bank);
                    const char* name=m<old.size()?old[m].timing.name:phase5_names[m-old.size()];
                    Clock::time_point sorted,checked;
                    const auto start=Clock::now();
                    {
                        auto v=inputs[bank];
                        if(m<old.size()) old[m].timing.run(v,nullptr);
                        else run_probe(m-old.size(),v,seed,nullptr);
                        sorted=Clock::now();
                        if(v!=reference[bank]) throw std::runtime_error(std::string("timed output mismatch: ")+name);
                        checked=Clock::now();
                    }
                    const auto end=Clock::now();
                    const auto elapsed=(sorted-start)+(end-checked);
                    times<<c.stage<<','<<c.name<<','<<c.n<<','<<bank<<','<<r<<','<<j<<','<<name<<','
                         <<std::chrono::duration_cast<std::chrono::nanoseconds>(elapsed).count()<<','<<seed<<'\n';
                    ++num_timings;
                }
            }
        }
        times.flush();nodes.flush();
        std::cerr<<"completed "<<c.name<<" "<<num_timings<<" checked timings\n";
    }
    std::cout<<"checked_timed_outputs="<<num_timings<<" checked_diagnostic_outputs="<<num_diag<<"\n";
}
}
int main(int argc,char** argv) {
    try {
        if(argc<2 || argc>3 || (argc==3&&std::string_view(argv[2])!="--smoke"))
            throw std::runtime_error("usage: bench OUT_DIR [--smoke]");
        pilot_bench::run(argv[1],argc==3);return 0;
    } catch(const std::exception& e) {std::cerr<<e.what()<<"\n";return 1;}
}
