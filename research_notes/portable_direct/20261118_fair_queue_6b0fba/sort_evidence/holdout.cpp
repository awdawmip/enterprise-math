#define BALANCED_SORT_LIBRARY
#include "bench.cpp"

namespace holdout {
using namespace balance_sort;

// The envelope minus the two largest internal gaps is the least number of
// integer slots occupied by at most three disjoint enclosing intervals.
bool fits(std::array<u64,64> sample, std::size_t size, std::size_t budget) {
    std::sort(sample.begin(), sample.begin()+size);
    u64 largest=0, second=0;
    for(std::size_t j=1;j<size;++j) {
        if(sample[j]==sample[j-1]) continue;
        const u64 gap=sample[j]-sample[j-1]-1;
        if(gap>largest) { second=largest; largest=gap; }
        else second=std::max(second,gap);
    }
    return u128(sample[size-1])-sample[0]+1-largest-second <= budget;
}

bool three(const Values& a,u64 seed) {
    const auto n=a.size(),budget=brc_sampled_detail::cell_budget(n);
    std::array<u64,64> sample{};
    for(unsigned j=0;j<32;++j) sample[j]=a[j*n/32];
    if(!fits(sample,32,budget)) return false;
    brc_probe::Engine draws{seed};
    for(unsigned j=0;j<32;++j) {
        const auto begin=j*n/32, end=(j+1)*n/32;
        auto i=begin+std::size_t(u128(draws())*(end-begin)>>64);
        while (i==begin || brc_probe::training_position(i,n)) {
            if(++i==end) i=begin;
        }
        sample[32+j]=a[i];
    }
    return fits(sample,64,budget);
}

void evaluate_heldout(const std::filesystem::path& dir,bool smoke) {
    std::filesystem::create_directories(dir);
    std::ofstream raw(dir/"holdout.csv"), diag(dir/"holdout_diag.csv");
    if(!raw || !diag) throw std::runtime_error("CSV open");
    raw<<"family,n,bank,round,order,method,ns,input_seed,probe_seed\n";
    diag<<"family,n,bank,one_segment,three_segments,decision_ns\n";
    std::mt19937_64 order(0xd855ef1937f9b83bULL);
    for(unsigned f=0;f<families.size();++f) for(std::size_t n:{16384,65536,262144,1048576}) {
        if(smoke && n!=16384) continue;
        for(unsigned b=0;b<(smoke?1:3);++b) {
            const u64 input_seed=0x3aa2c625a1c88249ULL ^ n ^ (u64(f)<<48) ^ ((b+1)*0xd1b54a32d192ed03ULL);
            const u64 probe_seed=0x964b13fdaa61f8cfULL ^ n ^ (u64(b)<<8) ^ (u64(f)<<32);
            const auto input=make_input(f,n,input_seed);
            auto oracle=input;std::sort(oracle.begin(),oracle.end());
            volatile unsigned total=0;
            const auto start=Clock::now();
            for(unsigned i=0;i<128;++i) total=total+three(input,probe_seed+i);
            const auto decision=ns(Clock::now()-start)/128;
            diag<<families[f]<<','<<n<<','<<b<<','<<pilot(input,probe_seed,true)<<','
                <<three(input,probe_seed)<<','<<decision<<'\n';
            std::array<unsigned,6> methods={0,1,2,3,8,9};
            for(unsigned r=0;r<(smoke?1:3);++r) {
                std::shuffle(methods.begin(),methods.end(),order);
                for(unsigned j=0;j<methods.size();++j) {
                    const unsigned m=methods[j];
                    Clock::time_point sorted,checked;
                    const auto begin=Clock::now();
                    {
                        Values a=input;
                        if(m!=9) run(m,a,probe_seed);
                        else if(three(a,probe_seed)) child_sort<ChildMode::radix>(a,probe_seed);
                        else offset_radix(a,nullptr);
                        sorted=Clock::now();
                        if(a!=oracle) throw std::runtime_error("holdout mismatch");
                        checked=Clock::now();
                    }
                    const auto end=Clock::now();
                    raw<<families[f]<<','<<n<<','<<b<<','<<r<<','<<j<<','
                       <<(m==9?"three_slots":names[m])<<','<<ns((sorted-begin)+(end-checked))
                       <<','<<input_seed<<','<<probe_seed<<'\n';
                }
            }
        }
        raw.flush();diag.flush();
    }
}
}
int main(int argc,char** argv) {
    if(argc<2 || argc>3) return 2;
    holdout::evaluate_heldout(argv[1],argc==3); return 0;
}
