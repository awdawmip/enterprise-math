#define main preceding_verify6_entry
#include "pure_bench.cpp"
#undef main
#include "local_kernels.hpp"
#include "sampled_kernels.hpp"
#include "robust_kernels.hpp"
#include "adaptive_kernels.hpp"
#include "selection_kernels.hpp"
#include "certified_kernels.hpp"
#include "../phase5/probe.hpp"
#include "child.hpp"
#include <set>

void demand(bool ok) { if(!ok) throw std::runtime_error("verification failed"); }
template<ChildMode Mode>
void verify_case(const std::vector<u64>& input, const std::vector<u64>& expected, u64 seed,
                 unsigned start_depth=0) {
    for(bool trace:{false,true}) {
        auto copy=input;
        ProbeStats stats;
        brc_probe::Engine rng{seed};
        if(trace) brc_child::run<Mode,true>(copy,rng,start_depth,&stats);
        else brc_child::run<Mode,false>(copy,rng,start_depth,nullptr);
        demand(copy==expected);
        for(auto& r:stats.rows) {
            if(r.probes) demand(r.depth>0 && r.n>=16384 && r.probes==1024);
            if(r.early) demand(r.counter_slots==0 && r.scan_visits==0 && r.misses>=r.threshold);
            if(r.range_sorted) demand(r.range_slots<=r.n && r.depth>0);
        }
    }
}
int main() {
    std::mt19937_64 rng(0x65c163c6);
    std::size_t checks=0, oracle_checks=0;
    for(std::size_t n:std::vector<std::size_t>{0,1,100,256,257,4095,16383,16384,16385,32769,100000}) {
        for(int family=0;family<8;++family) {
            std::vector<u64> a(n);
            for(std::size_t i=0;i<n;++i) {
                u64 x=rng();
                switch(family) {
                    case 0:a[i]=0;break;
                    case 1:a[i]=MAX_VALUE-x%71;break;
                    case 2:a[i]=x;break;
                    case 3:a[i]=i%2?0:MAX_VALUE;break;
                    case 4:a[i]=(x%4)*(1ull<<42)+x%10000;break;
                    case 5:a[i]=n-i;break;
                    case 6:a[i]=i%16?i%511:x;break;
                    default:a[i]=x;break;
                }
            }
            if(n>=16384 && family==7) {
                auto train=brc_sampled_detail::sample_indices(n,1024);
                for(auto i:train) a[i]=0;
            }
            auto expected=a;std::sort(expected.begin(),expected.end());
            const auto seed=rng();
            for(unsigned depth:{0u,1u}) {
                verify_case<ChildMode::deep_gate>(a,expected,seed,depth);
                verify_case<ChildMode::radix>(a,expected,seed,depth);
                verify_case<ChildMode::range_radix>(a,expected,seed,depth);
                checks+=6;
            }
            if(n>=16384) {
                // Independent storage/iteration oracle uses the frozen learner's explicit indices.
                auto layout=brc_sampled_detail::learn_sampled<1024,false>(a,nullptr);
                auto train=brc_sampled_detail::sample_indices(n,1024);
                for(unsigned j=0;j<8;++j) {
                    brc_probe::Engine fast{seed+j}, ref{seed+j};
                    ProbeRow row;
                    const bool observed=brc_child::deep_check(a,layout,fast,row);
                    std::set<std::size_t> used(train.begin(),train.end());
                    std::uniform_int_distribution<std::size_t> draw(0,n-1);
                    std::size_t picked=0, misses=0;
                    for(unsigned t=0;t<4096 && picked<1024;++t) {
                        auto i=draw(ref);
                        if(!used.insert(i).second) continue;
                        ++picked;misses+=!brc_probe::covered(a[i],layout);
                    }
                    const auto threshold=(1024*(n/2)+n-1024-1)/(n-1024)+42;
                    demand(row.threshold==threshold && row.misses==misses && picked==row.probes
                        && observed==(picked==1024 && misses>=threshold) && fast.state==ref.state);
                    ++oracle_checks;
                }
            }
        }
    }
    std::cout<<"full_output_checks="<<checks<<" independent_precheck_replays="<<oracle_checks<<" PASS\n";
}
