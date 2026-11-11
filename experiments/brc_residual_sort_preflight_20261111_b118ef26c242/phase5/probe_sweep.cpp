#define main previous_sweep_entry
#include "pure_bench.cpp"
#undef main
#include "local_kernels.hpp"
#include "sampled_kernels.hpp"
#include "robust_kernels.hpp"
#include "adaptive_kernels.hpp"
#include "selection_kernels.hpp"
#include "certified_kernels.hpp"
#include "probe.hpp"

int main() {
    constexpr std::size_t n=100000, repetitions=4096;
    std::vector<std::size_t> eligible;
    for(std::size_t i=0;i<n;++i) if(!brc_probe::training_position(i,n)) eligible.push_back(i);
    std::mt19937_64 ordering(0x88b118ef26c242ULL);
    std::shuffle(eligible.begin(),eligible.end(),ordering);
    std::cout<<"n,training,training_misses,actual_misses,threshold,seeds,triggered,incomplete\n";
    for(std::size_t k: {45000,50000,50001,55000,60000,65000,70000,75000,80000,90000}) {
        std::vector<u64> a(n,0);
        for(std::size_t j=0;j<k;++j) a[eligible[j]]=MAX_VALUE;
        auto layout=brc_sampled_detail::learn_sampled<1024,false>(a,nullptr);
        AdaptiveNodeStats ad; SelectionNodeStats sel; CertifiedNodeStats cert;
        const auto budget=brc_sampled_detail::cell_budget(n);
        brc_robust_detail::select_compact_layout<false>(layout,0,0,1024,budget,false,nullptr,&ad.core);
        if(!brc_certified_detail::select_certified_gap<false>(layout,budget,nullptr,ad,sel,cert,0,0))
            throw std::runtime_error("expected learned one-value model");
        if(!brc_probe::covered(0,layout) || brc_probe::covered(MAX_VALUE,layout))
            throw std::runtime_error("unexpected membership");
        unsigned hits=0, incomplete=0;
        for(std::size_t j=0;j<repetitions;++j) {
            brc_probe::Engine rng{0x25779cd58fd21133ULL+j*0xd1b54a32d192ed03ULL};
            ProbeRow row;
            hits+=brc_probe::precheck(a,layout,rng,row);
            incomplete+=row.probes!=brc_probe::probe_size;
        }
        std::cout<<n<<",1024,0,"<<k<<','<<brc_probe::rejection_threshold(n)<<','
                 <<repetitions<<','<<hits<<','<<incomplete<<'\n';
    }
}
