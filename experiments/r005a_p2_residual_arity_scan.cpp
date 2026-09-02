#include <algorithm>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <optional>
#include <sstream>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

struct Factor { uint32_t p; int e; };
struct ResidualExample {
    uint32_t k=0, n=0;
    int omega=0;
    int support_size=0;
    bool has_large=false;
    std::vector<Factor> factors;
    std::vector<uint32_t> support;
};

static std::string factor_json(const std::vector<Factor>& fs) {
    std::ostringstream o; o << "[";
    for (size_t i=0;i<fs.size();++i){ if(i)o<<","; o<<"["<<fs[i].p<<","<<fs[i].e<<"]"; }
    o << "]"; return o.str();
}
static std::string vec_json(const std::vector<uint32_t>& v) {
    std::ostringstream o; o << "[";
    for(size_t i=0;i<v.size();++i){ if(i)o<<","; o<<v[i]; }
    o<<"]"; return o.str();
}
static std::string example_json(const ResidualExample& x) {
    std::ostringstream o;
    o << "{\"k\":"<<x.k<<",\"n\":"<<x.n<<",\"omega\":"<<x.omega
      <<",\"support_size\":"<<x.support_size<<",\"has_large_factor\":"<<(x.has_large?"true":"false")
      <<",\"factorization\":"<<factor_json(x.factors)<<",\"support\":"<<vec_json(x.support)<<"}";
    return o.str();
}

int main(int argc, char** argv){
    uint32_t K = 10000;
    if(argc>1) K = static_cast<uint32_t>(std::stoul(argv[1]));
    uint64_t N64 = uint64_t(K+1)*(K+1)-1;
    if(N64 > UINT32_MAX){ std::cerr << "N too large\n"; return 2; }
    uint32_t N = static_cast<uint32_t>(N64);

    // Linear sieve: exact SPF table through the entire scanned square-basin range.
    std::vector<uint32_t> spf(size_t(N)+1, 0);
    std::vector<uint32_t> primes;
    primes.reserve(size_t(N / std::max(2.0, std::log(double(N)))) + 1000);
    for(uint32_t i=2;i<=N;++i){
        if(spf[i]==0){ spf[i]=i; primes.push_back(i); }
        for(uint32_t p: primes){
            uint64_t v=uint64_t(p)*i;
            if(v>N || p>spf[i]) break;
            spf[uint32_t(v)]=p;
        }
    }

    auto factor = [&](uint32_t n){
        std::vector<Factor> fs;
        while(n>1){
            uint32_t p=spf[n]; int e=0;
            do { n/=p; ++e; } while(n>1 && spf[n]==p);
            fs.push_back({p,e});
        }
        return fs;
    };

    std::vector<uint8_t> forced(size_t(K)+1, 0);
    std::vector<uint32_t> touched;
    touched.reserve(2000);

    uint64_t total_residual=0;
    uint64_t residual_basins=0;
    uint32_t max_residual_per_basin=0;
    uint32_t first_bad_k=0;
    std::map<int,uint64_t> omega_counts;
    std::map<int,uint64_t> support_counts;
    uint64_t residual_large_factor_count=0;
    std::optional<ResidualExample> first_omega4;
    std::optional<ResidualExample> first_large;
    uint64_t quartic_core_failure_count=0;
    uint32_t first_quartic_core_failure_k=0, first_quartic_core_failure_q=0;
    std::optional<ResidualExample> first_residual;
    std::vector<uint32_t> bad_k_first_100;
    std::vector<ResidualExample> residual_examples;

    // Regression packet for the previously exact K<=2000 scan.
    const std::vector<uint32_t> expected_bad_2000 = {
        25,47,62,123,130,151,157,162,196,217,308,364,365,479,556,888,924,935,
        1008,1056,1078,1162,1290,1345,1454,1511,1541,1577,1612,1627,1679,1781,
        1790,1865,1897
    };
    std::vector<uint32_t> observed_bad_2000;
    uint64_t residual_2000=0;

    for(uint32_t k=2;k<=K;++k){
        uint32_t A=k*k;
        uint32_t U=(k+1)*(k+1)-1;
        touched.clear();

        // Pass 1: singleton candidate support forces that witness.
        for(uint32_t n=A+1;n<=U;++n){
            if(spf[n]==n) continue; // prime basin state
            auto fs=factor(n);
            uint32_t only=0; int cnt=0;
            for(auto &f:fs){
                if(f.p<=k){ only=f.p; ++cnt; if(cnt>1) break; }
            }
            if(cnt==1 && !forced[only]){ forced[only]=1; touched.push_back(only); }
        }

        // Quartic-root core check: if all primes q<=floor(U^(1/4)) are forced,
        // every residual must have exact total prime-factor arity 3.
        uint32_t Q4 = static_cast<uint32_t>(std::sqrt(std::sqrt((long double)U)));
        while(uint64_t(Q4+1)*(Q4+1)*(Q4+1)*(Q4+1) <= U) ++Q4;
        while(uint64_t(Q4)*Q4*Q4*Q4 > U) --Q4;
        for(uint32_t q: primes){
            if(q>Q4) break;
            if(!forced[q]){
                ++quartic_core_failure_count;
                if(!first_quartic_core_failure_k){ first_quartic_core_failure_k=k; first_quartic_core_failure_q=q; }
            }
        }

        uint32_t residual_here=0;
        for(uint32_t n=A+1;n<=U;++n){
            if(spf[n]==n) continue;
            auto fs=factor(n);
            std::vector<uint32_t> support;
            int omega=0; bool has_large=false;
            for(auto &f:fs){
                omega += f.e;
                if(f.p<=k) support.push_back(f.p); else has_large=true;
            }
            if(support.empty()) continue;
            bool hit=false;
            for(uint32_t q:support){ if(forced[q]){ hit=true; break; } }
            if(hit) continue;

            ++residual_here; ++total_residual;
            ++omega_counts[omega]; ++support_counts[int(support.size())];
            if(has_large) ++residual_large_factor_count;
            ResidualExample ex{k,n,omega,int(support.size()),has_large,fs,support};
            if(!first_residual) first_residual=ex;
            if(residual_examples.size()<200) residual_examples.push_back(ex);
            if(omega>=4 && !first_omega4) first_omega4=ex;
            if(has_large && !first_large) first_large=ex;
            if(k<=2000) ++residual_2000;
        }

        if(residual_here){
            ++residual_basins;
            if(!first_bad_k) first_bad_k=k;
            max_residual_per_basin=std::max(max_residual_per_basin,residual_here);
            if(bad_k_first_100.size()<100) bad_k_first_100.push_back(k);
            if(k<=2000) observed_bad_2000.push_back(k);
        }
        for(uint32_t q:touched) forced[q]=0;
    }

    if(K>=2000){
        if(observed_bad_2000!=expected_bad_2000){
            std::cerr << "Regression mismatch in bad k<=2000\n"; return 3;
        }
        if(residual_2000!=36){
            std::cerr << "Regression mismatch residual count<=2000: "<<residual_2000<<"\n"; return 4;
        }
    }

    std::cout << "{\n";
    std::cout << "  \"status\": \"EXACT_P2_RESIDUAL_ARITY_SCAN\",\n";
    std::cout << "  \"max_k\": "<<K<<",\n";
    std::cout << "  \"max_n\": "<<N<<",\n";
    std::cout << "  \"residual_basin_count\": "<<residual_basins<<",\n";
    std::cout << "  \"total_residual_composites\": "<<total_residual<<",\n";
    std::cout << "  \"first_bad_k\": "<<first_bad_k<<",\n";
    std::cout << "  \"max_residual_per_basin\": "<<max_residual_per_basin<<",\n";
    std::cout << "  \"residual_large_factor_count\": "<<residual_large_factor_count<<",\n";
    std::cout << "  \"quartic_core_failure_count\": "<<quartic_core_failure_count<<",\n";
    std::cout << "  \"first_quartic_core_failure\": ";
    if(first_quartic_core_failure_k) std::cout << "{\"k\":"<<first_quartic_core_failure_k<<",\"q\":"<<first_quartic_core_failure_q<<"}"; else std::cout<<"null";
    std::cout << ",\n";
    std::cout << "  \"omega_counts\": {";
    { bool first=true; for(auto [o,c]:omega_counts){ if(!first)std::cout<<","; first=false; std::cout<<"\""<<o<<"\":"<<c; } }
    std::cout << "},\n  \"support_size_counts\": {";
    { bool first=true; for(auto [o,c]:support_counts){ if(!first)std::cout<<","; first=false; std::cout<<"\""<<o<<"\":"<<c; } }
    std::cout << "},\n  \"bad_k_first_100\": "<<vec_json(bad_k_first_100)<<",\n";
    std::cout << "  \"residual_examples\": [";
    for(size_t i=0;i<residual_examples.size();++i){ if(i)std::cout<<","; std::cout<<example_json(residual_examples[i]); }
    std::cout << "],\n";
    std::cout << "  \"first_residual\": "<<(first_residual?example_json(*first_residual):"null")<<",\n";
    std::cout << "  \"first_omega_ge_4\": "<<(first_omega4?example_json(*first_omega4):"null")<<",\n";
    std::cout << "  \"first_large_factor_residual\": "<<(first_large?example_json(*first_large):"null")<<",\n";
    std::cout << "  \"regression_k_le_2000\": {\"bad_k_match\": true, \"residual_count\": "<<residual_2000<<"}\n";
    std::cout << "}\n";
    return 0;
}
