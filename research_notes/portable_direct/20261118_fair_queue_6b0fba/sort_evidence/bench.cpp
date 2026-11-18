#include "certified_frozen_include.hpp"
#include "probe.hpp"
#include "../phase6/child.hpp"
#include <filesystem>

namespace balance_sort {
using Values = std::vector<u64>;
using Clock = std::chrono::steady_clock;
const std::array<const char*, 9> names = {"full_brc", "child_radix", "offset_radix",
    "pdqsort", "std_sort", "range_or_radix", "flat_frequency", "pilot32", "pilot32_validate"};
const std::array<const char*, 5> families = {"fixed_narrow","scaled_narrow",
    "fixed_three","scaled_three","masked_training"};

bool pilot(const Values& a, u64 seed, bool validate) {
    const std::size_t n = a.size();
    u64 low = a[0], high = a[0];
    for (unsigned j=0; j<32; ++j) {
        const u64 x=a[j*n/32];
        low=std::min(low,x); high=std::max(high,x);
    }
    if (high-low >= n) return false;
    if (!validate) return true;
    brc_probe::Engine draws{seed};
    for (unsigned j=0; j<32; ++j) {
        const auto begin=j*n/32, end=(j+1)*n/32;
        // Exclude both the first pilot point and the frozen model's training set.
        auto i=begin+std::size_t(u128(draws())*(end-begin)>>64);
        while (i==begin || brc_probe::training_position(i,n)) {
            ++i;
            if (i==end) i=begin;
        }
        const u64 x=a[i];
        low=std::min(low,x); high=std::max(high,x);
        if (high-low >= n) return false;
    }
    return true;
}

void run(unsigned method, Values& a, u64 seed) {
    switch(method) {
    case 0: certified_combined_1024(a,nullptr); break;
    case 1: child_sort<ChildMode::radix>(a,seed); break;
    case 2: offset_radix(a,nullptr); break;
    case 3: pdqsort(a.begin(),a.end()); break;
    case 4: std::sort(a.begin(),a.end()); break;
    case 5: dense_range(a,nullptr); break;
    case 6: flat_frequency_sort(a,nullptr); break;
    default:
        if (pilot(a,seed,method==8)) child_sort<ChildMode::radix>(a,seed);
        else offset_radix(a,nullptr);
    }
}

Values make_input(unsigned family, std::size_t n, u64 seed) {
    std::mt19937_64 rng(seed);
    const u64 width = family==1 || family==3 ? n/4 : 4096;
    const u64 base=u64(1)<<44, gap=u64(1)<<33;
    Values a(n);
    for (std::size_t i=0; i<n; ++i) {
        if (family==4) {
            const u64 x=rng();
            a[i]=(i%(n/32)==0 || brc_probe::training_position(i,n)) ?
                base+(x&4095) : x;
        } else {
            // All study sizes and widths are powers of two.
            const u64 g=family>=2 ? rng()%3 : 0;
            a[i]=base+g*gap+(rng()&(width-1));
        }
    }
    return a;
}

long ns(Clock::duration duration) {
    return std::chrono::duration_cast<std::chrono::nanoseconds>(duration).count();
}

void evaluate(const std::filesystem::path& dir,bool smoke) {
    std::filesystem::create_directories(dir);
    std::ofstream raw(dir/"raw.csv"),diag(dir/"diagnostics.csv");
    raw<<"family,n,bank,round,order,method,ns,input_seed,probe_seed\n";
    diag<<"family,n,bank,pilot,validated,pilot_ns,validated_ns,model,exact_residual,scan_visits\n";
    if (!raw || !diag) throw std::runtime_error("CSV open");
    std::mt19937_64 order(0x8f8ff694de9f1161ULL);
    for (unsigned f=0;f<families.size();++f) for (std::size_t n : {16384,65536,262144,1048576}) {
        if (smoke && n>16384) continue;
        for (unsigned b=0;b<(smoke?1:3);++b) {
            const u64 input_seed=0x51c9d7b41a2e3901ULL ^ n ^ (u64(f)<<48) ^ ((b+1)*0x9e3779b97f4a7c15ULL);
            const u64 probe_seed=0x41bfb03aa6e2b1deULL ^ n ^ (u64(b)<<8) ^ (u64(f)<<32);
            const auto input=make_input(f,n,input_seed);
            Values oracle=input; std::sort(oracle.begin(),oracle.end());
            auto traced=input; ProbeStats stats;
            child_sort<ChildMode::radix>(traced,probe_seed,&stats);
            if (traced!=oracle) throw std::runtime_error("diagnostic mismatch");
            const auto& root=stats.rows.at(0);
            // Isolated warm decision cost; volatile result keeps repetitions observable.
            long decision[2]={};
            for(unsigned v=0;v<2;++v) {
                volatile unsigned total=0;
                auto begin=Clock::now();
                for (unsigned i=0;i<128;++i) total=total+pilot(input,probe_seed+i,v);
                decision[v]=ns(Clock::now()-begin)/128;
            }
            diag<<families[f]<<','<<n<<','<<b<<','<<pilot(input,probe_seed,false)<<','
                <<pilot(input,probe_seed,true)<<','<<decision[0]<<','<<decision[1]<<','
                <<root.model_selected<<','<<root.actual_misses<<','<<root.scan_visits<<'\n';
            std::array<unsigned,9> methods={0,1,2,3,4,5,6,7,8};
            for(unsigned r=0;r<(smoke?1:3);++r) {
                std::shuffle(methods.begin(),methods.end(),order);
                for(unsigned j=0;j<methods.size();++j) {
                    const unsigned method=methods[j];
                    Clock::time_point sorted,checked;
                    const auto begin=Clock::now();
                    {
                        Values a=input;
                        run(method,a,probe_seed);
                        sorted=Clock::now();
                        if (a!=oracle) throw std::runtime_error("timed sort mismatch");
                        checked=Clock::now();
                    }
                    const auto end=Clock::now();
                    raw<<families[f]<<','<<n<<','<<b<<','<<r<<','<<j<<','<<names[method]<<','
                       <<ns((sorted-begin)+(end-checked))<<','<<input_seed<<','<<probe_seed<<'\n';
                }
            }
        }
        raw.flush(); diag.flush();
    }
}
}
#ifndef BALANCED_SORT_LIBRARY
int main(int argc,char** argv) {
    if(argc<2 || argc>3) return 2;
    balance_sort::evaluate(argv[1],argc==3);
    return 0;
}
#endif
