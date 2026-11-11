#include "build/bench5_frozen.hpp"
#include "child.hpp"

namespace child_bench {
struct Method { const char* name; void (*old)(std::vector<u64>&,Stats*); int kind; };
constexpr const char* new_names[]={"deep_gate","radix","range_radix"};

void run_child(unsigned kind,std::vector<u64>& v,u64 seed,ProbeStats* stats) {
    switch(kind) {
    case 0: child_sort<ChildMode::deep_gate>(v,seed,stats);break;
    case 1: child_sort<ChildMode::radix>(v,seed,stats);break;
    case 2: child_sort<ChildMode::range_radix>(v,seed,stats);break;
    default: throw std::logic_error("unknown child candidate");
    }
}
void call(const Method& m,std::vector<u64>& v,u64 seed,ProbeStats* stats=nullptr) {
    if(m.old) m.old(v,nullptr);
    else if(m.kind<3) run_child(m.kind,v,seed,stats);
    else pilot_bench::run_probe(m.kind-3,v,seed,stats);
}
std::vector<Method> methods() {
    std::vector<Method> v;
    for(const auto& c:certified_experiment::candidates()) v.push_back({c.timing.name,c.timing.run,-1});
    v.push_back({"gate",nullptr,3}); v.push_back({"child_range",nullptr,5});
    for(unsigned i=0;i<3;++i)v.push_back({new_names[i],nullptr,int(i)});
    require(v.size()==32,"phase-six candidate count");return v;
}
void experiment(const std::filesystem::path& path) {
    using Clock=std::chrono::steady_clock;
    std::filesystem::create_directories(path);
    std::ofstream raw(path/"timings.csv"),diag(path/"nodes.csv");
    require(bool(raw)&&bool(diag),"cannot write measurements");
    raw<<"stage,family,n,bank,round,order,algorithm,ns,probe_seed\n";
    diag<<"stage,family,bank,algorithm,probe_seed,depth,n,probes,misses,early,actual_misses,scan_visits,range_slots,counter_slots,model_selected,range_sorted,threshold,range_visits\n";
    auto all=methods();unsigned ntimed=0,ndiagnostic=0;
    for(const auto& c:pilot_bench::plan) {
        if(std::string_view(c.stage)!="fresh")continue;
        std::vector<std::vector<u64>> banks,reference;
        for(unsigned b=0;b<8;++b) {
            unsigned bank_id=b+32;
            banks.push_back(pilot_bench::make_input(c,bank_id));
            reference.push_back(banks.back());std::sort(reference.back().begin(),reference.back().end());
            for(const auto& m:all) {
                if(m.old)continue;
                const auto seed=pilot_bench::probe_seed(c,bank_id);
                auto v=banks.back();ProbeStats st;call(m,v,seed,&st);
                require(v==reference.back(),"phase6 full diagnostic output");++ndiagnostic;
                for(const auto& x:st.rows)
                    diag<<"fresh,"<<c.name<<','<<bank_id<<','<<m.name<<','<<seed<<','<<x.depth<<','<<x.n<<','
                        <<x.probes<<','<<x.misses<<','<<x.early<<','<<x.actual_misses<<','<<x.scan_visits<<','
                        <<x.range_slots<<','<<x.counter_slots<<','<<x.model_selected<<','<<x.range_sorted<<','
                        <<x.threshold<<','<<x.range_visits<<'\n';
            }
        }
        std::mt19937_64 rng(0x5048415345364f52ull+c.tag*30323);
        std::vector<unsigned> bord(8),mord(all.size());
        std::iota(bord.begin(),bord.end(),0);std::iota(mord.begin(),mord.end(),0);
        for(unsigned round=0;round<5;++round) {
            std::shuffle(bord.begin(),bord.end(),rng);
            for(unsigned b:bord) {
                const unsigned bank_id=b+32;
                const auto seed=pilot_bench::probe_seed(c,bank_id);
                std::shuffle(mord.begin(),mord.end(),rng);
                for(unsigned j=0;j<mord.size();++j) {
                    const auto& m=all[mord[j]];
                    Clock::time_point sorted,checked;
                    const auto start=Clock::now();
                    {
                        auto v=banks[b];call(m,v,seed);
                        sorted=Clock::now();
                        if(v!=reference[b])throw std::runtime_error(std::string("phase6 timed output mismatch: ")+m.name);
                        checked=Clock::now();
                    }
                    const auto end=Clock::now();
                    raw<<"fresh,"<<c.name<<','<<c.n<<','<<bank_id<<','<<round<<','<<j<<','<<m.name<<','
                       <<std::chrono::duration_cast<std::chrono::nanoseconds>((sorted-start)+(end-checked)).count()
                       <<','<<seed<<'\n';++ntimed;
                }
            }
        }
        raw.flush();diag.flush();std::cerr<<"completed "<<c.name<<" "<<ntimed<<" checked timings\n";
    }
    require(ntimed==7680&&ndiagnostic==240,"phase6 evaluation complete");
    std::cout<<"checked_timed_outputs="<<ntimed<<" checked_diagnostic_outputs="<<ndiagnostic<<"\n";
}
}
int main(int argc,char** argv) {
    try {
        if(argc!=2)throw std::runtime_error("usage: bench6 OUT_DIR");
        child_bench::experiment(argv[1]);return 0;
    } catch(const std::exception& e) { std::cerr<<e.what()<<"\n";return 1; }
}
