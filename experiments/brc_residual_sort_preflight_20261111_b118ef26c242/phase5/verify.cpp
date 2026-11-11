#define main preceding_entry_for_verification
#include "pure_bench.cpp"
#undef main
#include "local_kernels.hpp"
#include "sampled_kernels.hpp"
#include "robust_kernels.hpp"
#include "adaptive_kernels.hpp"
#include "selection_kernels.hpp"
#include "certified_kernels.hpp"
#include "probe.hpp"

void check(bool ok, const char* message) {
    if (!ok) throw std::runtime_error(message);
}

template<ProbeMode mode>
void check_sort(const std::vector<u64>& a, const std::vector<u64>& expected, u64 seed) {
    ProbeStats trace;
    auto measured = a;
    probe_sort<mode>(measured,seed,&trace);
    check(measured == expected,"diagnostic sort result");
    auto timed = a;
    probe_sort<mode>(timed,seed);
    check(timed == expected,"normal sort result");
    for (const auto& r:trace.rows) {
        if (r.probes) {
            check(r.n >= brc_probe::minimum_node && r.model_selected,"probe call scope");
            check(r.early == (r.probes == 64 && r.misses >= r.threshold),"threshold decision");
        }
        if constexpr (mode != ProbeMode::observe) {
            if (r.early) check(r.counter_slots == 0 && r.scan_visits == 0,"early allocation");
        }
        if (r.scan_visits) {
            check(r.actual_misses <= r.n/2 ? r.scan_visits == r.n
                                          : r.scan_visits >= r.n/2+1,"real contraction check");
        }
        if (r.range_sorted) check(r.range_slots <= r.n,"range budget");
    }
}

int main() {
    std::size_t positions = 0, inputs = 0;
    for(std::size_t n:std::vector<std::size_t>{1024,1025,2047,16383,16384,16385,16417,32769,100000,1000000}) {
        std::vector<bool> seen(n);
        for(auto i:brc_sampled_detail::sample_indices(n,1024)) seen[i]=true;
        for(std::size_t i=0;i<n;++i) check(seen[i]==brc_probe::training_position(i,n),"learner position inversion");
        positions+=n;
    }
    std::mt19937_64 gen(20261111);
    for(std::size_t n:std::vector<std::size_t>{0,1,2,99,100,255,256,257,1023,1024,1025,4097,16383,16384,16385,32769,100000}) {
        for(unsigned family=0;family<10;++family) {
            std::vector<u64> a(n);
            for(std::size_t i=0;i<n;++i) {
                const auto x=gen();
                switch(family) {
                    case 0: a[i]=0; break;
                    case 1: a[i]=MAX_VALUE-(x%97); break;
                    case 2: a[i]=x; break;
                    case 3: a[i]=i; break;
                    case 4: a[i]=n-i; break;
                    case 5: a[i]=(i%7==0?MAX_VALUE:0); break;
                    case 6: a[i]=(x%50==0?x:1000000+x%500); break;
                    case 7: a[i]=(i%3)*(u64(1)<<42)+(x%10000); break;
                    case 8: a[i]=(i%127)*(u64(1)<<23)+(x%19); break;
                    default: a[i]=MAX_VALUE-x%(n+1); break;
                }
            }
            if(family==2 && n>=16384) {
                // Selected on covered training positions, actual residuals exceed half.
                for(auto i:brc_sampled_detail::sample_indices(n,1024)) a[i] = 0;
            }
            auto expected=a;
            std::sort(expected.begin(),expected.end());
            const u64 seed=gen();
            check_sort<ProbeMode::gate>(a,expected,seed);
            check_sort<ProbeMode::gate_range>(a,expected,seed);
            check_sort<ProbeMode::child_range>(a,expected,seed);
            check_sort<ProbeMode::observe>(a,expected,seed);
            ++inputs;
        }
    }
    std::cout<<"inputs="<<inputs<<" full_output_checks="<<inputs*8
             <<" training_position_checks="<<positions<<" PASS\n";
}
