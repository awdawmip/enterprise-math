// Compile with the pinned phase-five build entry after renaming the holdout CLI.
#include "holdout.cpp"
#include <fstream>

namespace {
using balance_sort::Values;
constexpr unsigned q = 32;
constexpr u64 gap = u64(1) << 32;

unsigned field_product(unsigned a, unsigned b) {
    unsigned out = 0;
    for (unsigned bit=0; bit<5; ++bit) {
        if (b & 1) out ^= a;
        b >>= 1;
        a <<= 1;
        if (a & 32) a ^= 0x25;
    }
    return out;
}

unsigned slot(u64 seed, unsigned x) {
    unsigned y = unsigned(seed >> 60);
    for (int i=11; i>=0; --i)
        y = field_product(y,x) ^ unsigned((seed >> (5*i)) & 31);
    return y;
}

std::size_t training_slot(std::size_t n, unsigned j) {
    auto begin = std::size_t(u128(j)*n/1024);
    auto width = std::size_t(u128(j+1)*n/1024)-begin;
    u64 state = (0xB0E9400520261108ull ^ u64(n) ^ (u64(1024)*0xd1b54a32d192ed03ull))
              + u64(j)*0x9e3779b97f4a7c15ull;
    return begin + std::size_t((u128(brc_sampled_detail::next_mixed(state))*width) >> 64);
}

struct Design {
    std::array<unsigned,3> primes{};
    std::array<unsigned,3> dimensions{};
    std::array<unsigned,3> crt{};
    unsigned count = 0, width;
    explicit Design(unsigned v) : width(v) {
        for (unsigned p=2, rem=v; rem>1; ++p) {
            if (rem%p) continue;
            rem /= p;
            if (rem%p==0 || count>=primes.size()) throw std::runtime_error("unsupported width");
            primes[count]=p;
            dimensions[count]=p>=31 ? 2 : 3;
            unsigned coeff=v/p, inv=1;
            while ((u64(inv)*coeff)%p!=1) ++inv;
            crt[count]=coeff*inv;
            ++count;
        }
    }
};

std::array<std::size_t,32> indices(std::size_t n, u64 seed, const Design& d, bool whole) {
    std::array<std::size_t,32> out{};
    std::array<std::array<unsigned,3>,3> digits{};
    if (whole)
        for (unsigned l=0;l<d.count;++l)
            for (unsigned i=0;i<d.dimensions[l];++i) {
                digits[l][i]=unsigned(seed%d.primes[l]);
                seed/=d.primes[l];
            }
    for (unsigned j=0; j<32; ++j) {
        const auto begin=j*n/32;
        if (!whole) {
            const unsigned k=slot(seed,j);
            out[j]=training_slot(n,32*j+k);
            if (out[j]==begin) out[j]=training_slot(n,32*j+(k+1)%32);
        } else {
            u64 residue=0;
            for (unsigned l=0;l<d.count;++l) {
                const unsigned p=d.primes[l];
                const auto& z=digits[l];
                unsigned value=0;
                if (d.dimensions[l]==3) value=z[0]+(j%p)*z[1]+(j/p)*z[2];
                else value=j==p ? z[1] : z[0]+j*z[1];
                residue+=u64(value%p)*d.crt[l];
            }
            out[j]=begin+1+residue%d.width;
        }
    }
    return out;
}

bool probe(const Values& a, u64 seed, const Design& d, bool whole) {
    std::array<u64,64> sample{};
    for (unsigned j=0;j<32;++j) sample[j]=a[j*a.size()/32];
    auto budget=brc_sampled_detail::cell_budget(a.size());
    if (!holdout::fits(sample,32,budget)) return false;
    auto addresses=indices(a.size(),seed,d,whole);
    for (unsigned j=0;j<32;++j) sample[32+j]=a[addresses[j]];
    return holdout::fits(sample,64,budget);
}

void route(Values& a, u64 seed, bool passed, ProbeStats* stats) {
    if (passed) child_sort<ChildMode::radix>(a,seed,stats);
    else offset_radix(a,nullptr);
}
}

int main(int argc, char** argv) {
    std::ofstream timing;
    if (argc==2) {
        timing.open(argv[1]);
        if (!timing) throw std::runtime_error("clock output");
        timing << "n,case,seed,repeat,method,decision_ns,total_ns\n";
    }
    std::size_t n,k;
    std::string label;
    u64 seed;
    while (std::cin >> n >> label >> seed >> k) {
        const Design d(unsigned(n/32-1));
        auto trained=brc_sampled_detail::sample_indices(n,1024);
        for (unsigned h=0;h<1024;++h)
            if (training_slot(n,h)!=trained[h]) throw std::runtime_error("training address");
        Values input(n);
        for (std::size_t i=0;i<n;++i) input[i]=gap*(i%3);
        for (unsigned j=0;j<32;++j) input[j*n/32]=gap*(j%3);
        for (std::size_t i=0;i<k;++i) {
            std::size_t pos;
            if (!(std::cin>>pos) || pos>=n) throw std::runtime_error("case");
            input[pos]=3*gap;
        }
        auto expected=input;
        std::sort(expected.begin(),expected.end());
        unsigned old=holdout::three(input,seed);
        std::cout<<n<<' '<<label<<' '<<seed;
        for (unsigned mode=0; mode<3; ++mode) {
            const bool pass=mode==0 ? old : probe(input,seed,d,mode==2);
            u64 address_hash=0;
            if (mode!=0)
                for (auto pos: indices(n,seed,d,mode==2)) address_hash=address_hash*1000003+pos;
            ProbeStats stats;
            auto sorted=input;
            route(sorted,seed,pass,&stats);
            if (sorted!=expected) throw std::runtime_error("full output mismatch");
            std::cout<<' '<<pass<<' '<<address_hash;
            if (!pass) std::cout<<" -1 -1 -1";
            else {
                const auto& row=stats.rows.at(0);
                std::cout<<' '<<row.counter_slots<<' '<<row.actual_misses<<' '<<row.scan_visits;
            }
        }
        std::cout<<'\n';
        if (argc==2) {
            // Rotate the five methods over repeats. Copies and comparison lie outside the timer.
            const char* methods[]={"holdout","field","crt","offset_radix","std_sort"};
            for (int rep=0; rep<5; ++rep) for (int order=0; order<5; ++order) {
                const unsigned mode=(order+rep)%5;
                auto sorted=input;
                auto start=std::chrono::steady_clock::now();
                bool pass=mode==0 ? holdout::three(sorted,seed) :
                          mode==1 ? probe(sorted,seed,d,false) :
                          mode==2 ? probe(sorted,seed,Design(unsigned(n/32-1)),true) : false;
                auto decision=std::chrono::steady_clock::now();
                if (mode==4) std::sort(sorted.begin(),sorted.end());
                else route(sorted,seed,pass,nullptr);
                auto finish=std::chrono::steady_clock::now();
                if (sorted!=expected) throw std::runtime_error("timed sort mismatch");
                auto ns=[](auto t){return std::chrono::duration_cast<std::chrono::nanoseconds>(t).count();};
                timing<<n<<','<<label<<','<<seed<<','<<rep<<','<<methods[mode]<<','
                      <<(mode<3?ns(decision-start):0)<<','<<ns(finish-start)<<'\n';
            }
        }
    }
}
