// BRC residual classification -> stable numerical order.
// Domain: uint32 values in [0, 1,000,000], records carry original positions.
// All roots and certificates use integer arithmetic. No persistent key/table cache.
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <numeric>
#include <random>
#include <stdexcept>
#include <string>
#include <vector>

using u32 = std::uint32_t;
using u64 = std::uint64_t;
constexpr u32 U = 1000000, RBITS = 11, RMASK = (1u<<RBITS)-1;
struct Record { u32 value, id; bool operator==(const Record&) const = default; };
static_assert(sizeof(Record)==8);
struct RootTrace { u32 radicand, k, collapse, residual, next; };
struct Stats {
    u64 roots=0, divisions=0, reciprocal_quotients=0, hits=0, misses=0;
    u64 corrected_up=0, corrected_down=0;
    u32 kspan=0, rspan=0;
    bool pilot_disabled=false, same_basin=false, equal_input=false, fused_grid=false;
};

// Integer bisection specialized to the declared finite input domain.
inline u32 exact_root(u32 x) {
    u32 lo=0, hi=1001;
    while (lo+1<hi) {
        u32 mid=(lo+hi)>>1;
        if (u64(mid)*mid<=x) lo=mid; else hi=mid;
    }
    return lo;
}
inline RootTrace root_trace(u32 x) {
    const u32 k=exact_root(x), c=k*k;
    return {x,k,c,x-c,(k+1)*(k+1)};
}
inline bool certified_root(u32 x, u32 candidate) {
    const u64 c=u64(candidate)*candidate;
    return c<=x && u64(x)-c<2ull*candidate+1;
}

// inv=floor(2^32/d), d>=2. The product estimate is exact or one too small
// for every uint32 numerator; one remainder comparison makes it exact.
inline u32 reciprocal_quotient(u32 numerator,u32 d,u64 inv) {
    const u32 q=u32((u64(numerator)*inv)>>32);
    return q+(numerator-q*d>=d);
}

// Stable counting of a selected key component. Work memory is per invocation.
template<class Key>
void count_pass(std::vector<Record>& a, std::vector<Record>& tmp,
                std::vector<std::size_t>& counts, u32 low, u32 span, Key key) {
    if (span<=1) return;
    counts.assign(span,0);
    for (const auto& r:a) ++counts[key(r)-low];
    std::size_t total=0;
    for (auto& count:counts) { const auto c=count; count=total; total+=c; }
    for (const auto& r:a) tmp[counts[key(r)-low]++]=r;
    a.swap(tmp);
}

// Mode 0: full root for each record.
// Mode 1: minimum-root anchor, exact quotient prediction, exact fallback.
// Mode 2: adds a single-basin certificate and a fixed 16-probe pilot.
//         The pilot keeps prediction when at least 12 of its 16 probes hit.
// Mode 3: exact reciprocal quotient; fuse (root,residual) counting when B*D<=n.
//         Every mode finishes with BRC residual/root counting; no std-sort fallback.
template<int Mode, bool Collect>
void brc_impl(std::vector<Record>& a, Stats* stats) {
    if (a.size()<2) return;
    u32 minv=0, maxv=0, K=0, base=0, denominator=0;
    u64 inverse=0;
    bool single=false, use_anchor=false;
    unsigned probes=0, successes=0;
    bool pilot_done=false;
    if constexpr (Mode>0) {
        minv=U; maxv=0;
        for (const auto& r:a) { minv=std::min(minv,r.value); maxv=std::max(maxv,r.value); }
        if (minv==maxv) { if constexpr(Collect) stats->equal_input=true; return; }
        const auto anchor=root_trace(minv);
        K=anchor.k; base=anchor.collapse; denominator=2*K;
        if constexpr(Collect) ++stats->roots;
        use_anchor=K>0;
        if constexpr(Mode>=2) {
            single=maxv<anchor.next;
            if constexpr(Collect) stats->same_basin=single;
        }
        if constexpr(Mode==3) {
            if(use_anchor && !single) {
                inverse=(1ull<<32)/denominator;
                if constexpr(Collect) ++stats->divisions;
            }
        }
    }
    u32 kmin=1001,kmax=0,rmin=2048,rmax=0;
    for (auto& item:a) {
        const u32 x=item.value;
        u32 k;
        if constexpr(Mode==0) {
            k=exact_root(x);
            if constexpr(Collect) ++stats->roots;
        } else {
            if (single || x==minv) k=K;
            else if (use_anchor) {
                u32 quotient;
                if constexpr(Mode==3) {
                    quotient=reciprocal_quotient(x-base,denominator,inverse);
                    if constexpr(Collect) ++stats->reciprocal_quotients;
                } else {
                    quotient=(x-base)/denominator;
                    if constexpr(Collect) ++stats->divisions;
                }
                const u32 candidate=K+quotient;
                const bool hit=certified_root(x,candidate);
                if constexpr(Collect) {
                    if (hit) ++stats->hits; else ++stats->misses;
                }
                if (hit) k=candidate;
                else {
                    k=exact_root(x);
                    if constexpr(Collect) ++stats->roots;
                }
                if constexpr(Mode>=2) {
                    if (!pilot_done) {
                        ++probes; successes+=hit;
                        if (probes==16) {
                            pilot_done=true;
                            if (successes<12) {
                                use_anchor=false;
                                if constexpr(Collect) stats->pilot_disabled=true;
                            }
                        }
                    }
                }
            } else {
                k=exact_root(x);
                if constexpr(Collect) ++stats->roots;
            }
        }
        const u32 residual=x-k*k;
        kmin=std::min(kmin,k); kmax=std::max(kmax,k);
        rmin=std::min(rmin,residual); rmax=std::max(rmax,residual);
        // Lossless bounded BRC state: k and residual. Original x is reconstructed below.
        item.value=(k<<RBITS)|residual;
    }
    if constexpr(Collect) { stats->kspan=kmax-kmin+1; stats->rspan=rmax-rmin+1; }
    std::vector<Record> tmp(a.size());
    std::vector<std::size_t> counts;
    bool fused=false;
    if constexpr(Mode==3) {
        const u32 width=rmax-rmin+1;
        const u64 cells=u64(kmax-kmin+1)*width;
        fused=cells<=a.size();
        if(fused) {
            if constexpr(Collect) stats->fused_grid=true;
            count_pass(a,tmp,counts,0,u32(cells),[=](const Record& r){
                return ((r.value>>RBITS)-kmin)*width+(r.value&RMASK)-rmin;
            });
        }
    }
    if(!fused) {
        count_pass(a,tmp,counts,rmin,rmax-rmin+1,[](const Record& r){return r.value&RMASK;});
        count_pass(a,tmp,counts,kmin,kmax-kmin+1,[](const Record& r){return r.value>>RBITS;});
    }
    for (auto& r:a) { const u32 k=r.value>>RBITS; r.value=k*k+(r.value&RMASK); }
}
template<int Mode>
void brc(std::vector<Record>& a, Stats* s) {
    if(s) brc_impl<Mode,true>(a,s); else brc_impl<Mode,false>(a,nullptr);
}
void radix20(std::vector<Record>& a, Stats*) {
    if(a.size()<2) return;
    std::vector<Record> tmp(a.size());
    std::vector<std::size_t> counts;
    count_pass(a,tmp,counts,0,1024,[](const Record& r){return r.value&1023u;});
    count_pass(a,tmp,counts,0,1024,[](const Record& r){return r.value>>10;});
}
void range_count(std::vector<Record>& a, Stats*) {
    if(a.size()<2) return;
    u32 low=U,high=0;
    for(const auto& r:a) { low=std::min(low,r.value); high=std::max(high,r.value); }
    if(low==high) return;
    std::vector<Record> tmp(a.size());
    std::vector<std::size_t> counts;
    count_pass(a,tmp,counts,low,high-low+1,[](const Record& r){return r.value;});
}
void standard_sort(std::vector<Record>& a,Stats*) {
    std::sort(a.begin(),a.end(),[](const auto& x,const auto& y){return x.value<y.value;});
}
void standard_stable(std::vector<Record>& a,Stats*) {
    std::stable_sort(a.begin(),a.end(),[](const auto& x,const auto& y){return x.value<y.value;});
}

// Full minimum m, rather than floor_sqrt(m)^2, is the predictor origin.
// The old brc_impl<3> above is retained verbatim apart from Stats' extra fields.
// For m=K^2+a and x=(K+j)^2+r, candidate-(K+j)
// = floor((j^2+r-a)/(2K)) >= -1.  Thus if the candidate square is <=x,
// testing its next square by a difference permits exactly one upward correction.
// If its square is >x, a checked one-step decrement is exact or we use bisection.
// Correct=false is a controlled formula-only change. Correct=true adds correction.
template<bool Correct, bool Collect>
void residual_impl(std::vector<Record>& a, Stats* stats) {
    if (a.size()<2) return;
    u32 minv=U,maxv=0;
    for (const auto& item:a) {
        minv=std::min(minv,item.value);
        maxv=std::max(maxv,item.value);
    }
    if (minv==maxv) {
        if constexpr(Collect) stats->equal_input=true;
        return;
    }
    const auto anchor=root_trace(minv);
    const u32 K=anchor.k, denominator=2*K;
    if constexpr(Collect) ++stats->roots;
    const bool single=maxv<anchor.next;
    if constexpr(Collect) stats->same_basin=single;
    bool use_anchor=K>0;
    u64 inverse=0;
    if(use_anchor && !single) {
        inverse=(1ull<<32)/denominator;
        if constexpr(Collect) ++stats->divisions;
    }
    unsigned probes=0,successes=0;
    bool pilot_done=false;
    u32 kmin=1001,kmax=0,rmin=2048,rmax=0;
    for(auto& item:a) {
        const u32 x=item.value;
        u32 k;
        if(single || x==minv) k=K;
        else if(use_anchor) {
            const u32 candidate=K+reciprocal_quotient(x-minv,denominator,inverse);
            if constexpr(Collect) ++stats->reciprocal_quotients;
            const u64 square=u64(candidate)*candidate;
            const bool hit=square<=x && u64(x)-square<2ull*candidate+1;
            bool resolved=hit;
            k=candidate;
            if constexpr(Collect) {
                if(hit) ++stats->hits; else ++stats->misses;
            }
            if constexpr(Correct) {
                if(!hit) {
                    if(square<=x) {
                        // Exact formula ensures candidate is at most one too small.
                        ++k;
                        resolved=true;
                        if constexpr(Collect) ++stats->corrected_up;
                    } else if(square-(2ull*candidate-1)<=x) {
                        // x<candidate^2 supplies the upper endpoint certificate.
                        --k;
                        resolved=true;
                        if constexpr(Collect) ++stats->corrected_down;
                    }
                }
            }
            if(!resolved) {
                k=exact_root(x);
                if constexpr(Collect) ++stats->roots;
            }
            if(!pilot_done) {
                ++probes; successes+=resolved;
                if(probes==16) {
                    pilot_done=true;
                    if(successes<12) {
                        use_anchor=false;
                        if constexpr(Collect) stats->pilot_disabled=true;
                    }
                }
            }
        } else {
            k=exact_root(x);
            if constexpr(Collect) ++stats->roots;
        }
        const u32 residual=x-k*k;
        kmin=std::min(kmin,k); kmax=std::max(kmax,k);
        rmin=std::min(rmin,residual); rmax=std::max(rmax,residual);
        item.value=(k<<RBITS)|residual;
    }
    if constexpr(Collect) {stats->kspan=kmax-kmin+1;stats->rspan=rmax-rmin+1;}
    std::vector<Record> tmp(a.size());
    std::vector<std::size_t> counts;
    const u32 width=rmax-rmin+1;
    const u64 cells=u64(kmax-kmin+1)*width;
    const bool fused=cells<=a.size();
    if(fused) {
        if constexpr(Collect) stats->fused_grid=true;
        count_pass(a,tmp,counts,0,u32(cells),[=](const Record& item){
            return ((item.value>>RBITS)-kmin)*width+(item.value&RMASK)-rmin;
        });
    } else {
        count_pass(a,tmp,counts,rmin,rmax-rmin+1,[](const Record& item){return item.value&RMASK;});
        count_pass(a,tmp,counts,kmin,kmax-kmin+1,[](const Record& item){return item.value>>RBITS;});
    }
    for(auto& item:a) {const u32 k=item.value>>RBITS;item.value=k*k+(item.value&RMASK);}
}
template<bool Correct>
void residual(std::vector<Record>& a,Stats* stats) {
    if(stats) residual_impl<Correct,true>(a,stats);
    else residual_impl<Correct,false>(a,nullptr);
}

struct Algorithm {const char* name;void(*run)(std::vector<Record>&,Stats*);bool stable;};
const std::array<Algorithm,6> algorithms{{
    {"std_sort",standard_sort,false},
    {"radix20",radix20,true},
    {"range_count",range_count,true},
    {"brc_fused_old",brc<3>,true},
    {"brc_residual_direct",residual<false>,true},
    {"brc_residual_correct",residual<true>,true}
}};
u64 bounded(std::mt19937_64& rng,u64 bound) {
    const u64 threshold=(u64(0)-bound)%bound;
    u64 x; do {x=rng();} while(x<threshold);
    return x%bound;
}
std::vector<Record> records(const std::vector<u32>& v) {
    std::vector<Record> a; a.reserve(v.size());
    for(std::size_t i=0;i<v.size();++i) a.push_back({v[i],u32(i)});
    return a;
}
const std::vector<u32> original100={776669,662511,219200,338659,388826,523002,620061,21207,239119,406150,6832,680904,903234,567856,614522,854859,983043,649315,726747,77213,479627,393880,918633,29715,470043,911431,716362,168020,904033,573868,494099,740040,250943,876000,881624,852793,898562,120952,815627,299640,722386,305300,223078,116502,807433,715643,335088,577156,528271,522144,861438,551401,819148,517371,404338,557580,473827,328238,190261,775183,436400,784253,221317,160791,633460,231052,712313,38027,999249,941354,558476,330879,757660,516141,542427,12511,853348,536321,368551,517871,399456,458655,203314,259040,867863,691595,890000,846822,545134,827510,816750,13005,552596,784689,482193,559888,233389,578371,325011,802462};
std::vector<u32> scattered_pool() {
    std::mt19937_64 rng(0x160B0E94005ull);
    std::vector<u32> pool;
    while(pool.size()<160) {
        u32 x=u32(bounded(rng,U+1ull));
        if(std::find(pool.begin(),pool.end(),x)==pool.end()) pool.push_back(x);
    }
    std::sort(pool.begin(),pool.end());
    return pool;
}

struct Case {std::string family;std::size_t n;};
std::vector<Case> all_cases() {
    std::vector<Case> out;
    for(std::size_t n:{100u,1000u,10000u,100000u,1000000u}) out.push_back({"uniform",n});
    for(const char* family:{"square_shift0","square_shift900","square_shift1790"})
        for(std::size_t n:{100u,1000u,10000u,100000u}) out.push_back({family,n});
    for(const char* family:{"square_shift0","square_shift1790"}) out.push_back({family,1000000});
    for(const char* family:{"square_B60","square_B100","full_basin20","single_basin",
                            "zero_anchor","matched_scattered","reverse_square1790"})
        out.push_back({family,100000});
    return out;
}
std::vector<Record> make_data(const std::string& family,std::size_t n,unsigned bank) {
    // Family-independent seeds make shifts preserve each bank's label sequence.
    const u64 seed=0xB0E94005ull+u64(n)*0x9e3779b97f4a7c15ull+u64(bank)*0xD1B54A32D192ED03ull;
    std::mt19937_64 rng(seed);
    std::vector<u32> v(n);
    if(family.starts_with("square_") || family=="reverse_square1790") {
        u32 B=20,D=8,shift=0;
        if(family=="square_shift900") shift=900;
        if(family=="square_shift1790" || family=="reverse_square1790") shift=1790;
        if(family=="square_B60") B=60;
        if(family=="square_B100") B=100;
        for(auto& x:v) {
            const u32 label=u32(bounded(rng,u64(B)*D));
            const u32 k=900+label/D;
            x=k*k+label%D+shift;
        }
        if(family=="reverse_square1790") std::sort(v.begin(),v.end(),std::greater<u32>());
    } else if(family=="matched_scattered") {
        const auto pool=scattered_pool();
        for(auto& x:v) x=pool[bounded(rng,pool.size())];
    } else if(family=="single_basin") {
        for(auto& x:v) x=810000+u32(bounded(rng,1801));
    } else if(family=="full_basin20") {
        for(auto& x:v) x=810000+u32(bounded(rng,36400));
    } else if(family=="uniform" || family=="zero_anchor") {
        if(n==100 && bank==0) v=original100;
        else for(auto& x:v) x=u32(bounded(rng,U+1ull));
        if(family=="zero_anchor" && !v.empty()) v[0]=0;
    } else throw std::runtime_error("unknown data family: "+family);
    return records(v);
}

void require(bool condition,const char* message) {
    if(!condition) throw std::runtime_error(message);
}
void check_output(const std::vector<Record>& in,const std::vector<Record>& out,
                  const std::vector<Record>& expected,bool stable) {
    require(out.size()==in.size(),"size mismatch");
    if(stable) {require(out==expected,"stable output mismatch");return;}
    std::vector<bool> seen(in.size(),false);
    for(std::size_t i=0;i<out.size();++i) {
        const auto& item=out[i];
        require(item.id<in.size() && !seen[item.id],"lost or duplicate record ID");
        require(item.value==in[item.id].value,"record payload mismatch");
        require(i==0 || out[i-1].value<=item.value,"nonascending output");
        seen[item.id]=true;
    }
}
u64 verified_arrays=0;
void check_case(const std::vector<u32>& values) {
    auto in=records(values),expected=in;
    standard_stable(expected,nullptr);
    for(const auto& algorithm:algorithms) {
        auto out=in;Stats stats;
        algorithm.run(out,&stats);
        check_output(in,out,expected,algorithm.stable);
        out=in;algorithm.run(out,nullptr);
        check_output(in,out,expected,algorithm.stable);
    }
    ++verified_arrays;
}
void verify() {
    // Retain independent finite oracle and quotient validation for the inherited kernel.
    u32 oracle=0;
    for(u32 x=0;x<=U;++x) {
        if(u64(oracle+1)*(oracle+1)<=x) ++oracle;
        const auto trace=root_trace(x);
        require(trace.k==oracle,"root exhaustive oracle mismatch");
        require(trace.collapse+trace.residual==x && x<trace.next,"root trace mismatch");
        require(trace.residual<=1998 && trace.k<=1000,"bounded state escaped");
        const u32 packed=(trace.k<<RBITS)|trace.residual;
        require((packed>>RBITS)*(packed>>RBITS)+(packed&RMASK)==x,"codec mismatch");
    }
    u64 quotient_points=0;
    for(u32 d:{2u,6u,16u,1800u,1998u,2000u}) {
        const u64 inv=(1ull<<32)/d;
        for(u32 x=0;x<=U;++x) {
            require(reciprocal_quotient(x,d,inv)==x/d,"reciprocal quotient mismatch");
            ++quotient_points;
        }
    }
    for(u32 d=2;d<=2000;d+=2) {
        const u64 inv=(1ull<<32)/d;
        for(u32 x:{0u,1u,d-1,d,d+1,U,std::numeric_limits<u32>::max()}) {
            require(reciprocal_quotient(x,d,inv)==x/d,"reciprocal boundary mismatch");
            ++quotient_points;
        }
    }
    // Exhaust the actual predictor/correction law on 36,400 points and four anchors.
    u64 correction_points=0;
    for(u32 minimum:{810000u,810007u,810900u,811790u}) {
        const u32 K=exact_root(minimum),d=2*K;
        const u64 inv=(1ull<<32)/d;
        for(u32 x=minimum;x<846400;++x) {
            const u32 truth=exact_root(x);
            const u32 p=K+reciprocal_quotient(x-minimum,d,inv);
            require(p+1>=truth,"new predictor underestimated by more than one");
            const u64 square=u64(p)*p;
            u32 recovered=p;
            if(square<=x) recovered+=u64(x)-square>=2ull*p+1;
            else if(square-(2ull*p-1)<=x) --recovered;
            else recovered=exact_root(x);
            require(recovered==truth,"checked correction mismatch");
            ++correction_points;
        }
    }
    for(unsigned len=0;len<=6;++len) {
        u64 number=1;for(unsigned j=0;j<len;++j) number*=4;
        for(u64 mask=0;mask<number;++mask) {
            u64 code=mask;std::vector<u32> v(len);
            constexpr std::array<u32,4> alphabet={0,1,3,4};
            for(auto& x:v) {x=alphabet[code%4];code/=4;}
            check_case(v);
        }
    }
    const std::vector<std::vector<u32>> edges={
        {},{0},{U},{1,U},{0,U},{3,4},{4,16},{810000,811799,811800,811801},
        {810000,919681},{810000,998001},{810007,811801},
        {102,99,101,121,100},{1000000,81,16,0,81},
        {999998,999999,1000000,999999,0,1},
        std::vector<u32>(100,0),std::vector<u32>(100,123456),original100
    };
    for(const auto& v:edges) check_case(v);
    std::mt19937_64 rng(20261107);
    for(unsigned trial=0;trial<120;++trial) {
        const std::size_t n=trial<100 ? std::size_t(bounded(rng,300)) : 1000;
        std::vector<u32> v(n);
        for(auto& x:v) x=u32(bounded(rng,U+1ull));
        check_case(v);
    }
    for(const auto& condition:all_cases()) {
        // Performance banks are all checked at their real sizes in --bench.
        const auto in=make_data(condition.family,std::min<std::size_t>(condition.n,10000),0);
        std::vector<u32> v;for(const auto& item:in) v.push_back(item.value);
        check_case(v);
    }
    {auto a=records({3,4});Stats s;residual<true>(a,&s);
     require(s.corrected_up==1 && s.roots==1,"upward correction branch not exercised");}
    {auto a=records({810000,919681});Stats s;residual<true>(a,&s);
     require(s.corrected_down==1 && s.roots==1,"downward correction branch not exercised");}
    {auto a=records({810000,998001});Stats s;residual<true>(a,&s);
     require(s.misses==1 && s.roots==2,"large-error exact fallback not exercised");}
    {auto a=records({0,U});Stats s;residual<true>(a,&s);
     require(s.divisions==0 && s.reciprocal_quotients==0,"zero anchor division");}
    u64 paired_points=0;
    for(unsigned bank=0;bank<8;++bank) {
        const auto a=make_data("square_shift0",1000,bank);
        const auto b=make_data("square_shift900",1000,bank);
        const auto c=make_data("square_shift1790",1000,bank);
        for(std::size_t i=0;i<a.size();++i) {
            require(b[i].value-a[i].value==900 && c[i].value-a[i].value==1790,"paired translations mismatch");
            require(exact_root(a[i].value)==exact_root(c[i].value),"translation crossed square basin");
            ++paired_points;
        }
    }
    std::cout<<"{\"root_and_codec_points\":"<<(u64(U)+1)
             <<",\"reciprocal_quotient_points\":"<<quotient_points
             <<",\"correction_law_points\":"<<correction_points
             <<",\"paired_translation_points\":"<<paired_points
             <<",\"verified_arrays\":"<<verified_arrays
             <<",\"algorithms\":"<<algorithms.size()
             <<",\"instrumented_and_uninstrumented_checked\":true,\"result\":\"PASS\"}\n";
}

volatile u64 observed=0;
inline void consume(const std::vector<Record>& a) {
    asm volatile("" : : "g"(a.data()),"g"(a.size()) : "memory");
    if(!a.empty()) {
        const auto& x=a.front();const auto& y=a[a.size()/2];const auto& z=a.back();
        observed=observed ^ (u64(x.value)*0x9e3779b9ull+u64(y.id)*257+z.id);
    }
}
using Clock=std::chrono::steady_clock;
double timed(const Algorithm& algorithm,const std::vector<std::vector<Record>>& banks,
             std::size_t cycles,unsigned rotation) {
    const auto start=Clock::now();
    for(std::size_t cycle=0;cycle<cycles;++cycle) for(std::size_t b=0;b<banks.size();++b) {
        std::vector<Record> work=banks[(b+rotation)%banks.size()];
        algorithm.run(work,nullptr);
        consume(work);
    } // Work, counts, and temporary arrays are all freed inside the timed region.
    return std::chrono::duration<double>(Clock::now()-start).count();
}
double quantile(std::vector<double> v,double q) {
    std::sort(v.begin(),v.end());
    const double p=q*(v.size()-1);const auto i=std::size_t(p);
    return v[i]+(v[std::min(i+1,v.size()-1)]-v[i])*(p-i);
}
void benchmark(const std::string& path,std::size_t maxn,double target_ms,const std::string& filter) {
    constexpr unsigned BANKS=8,ROUNDS=7;
    constexpr std::size_t A=algorithms.size();
    require(target_ms>0,"target_ms must be positive");
    std::ofstream file(path);
    require(bool(file),"cannot open benchmark output");
    file<<"family,n,algorithm,stable,banks,rounds,median_us,p10_us,p90_us,min_us,max_us,calls_per_round,roots,divisions,reciprocal_quotients,direct_hits,prediction_misses,corrected_up,corrected_down,fallback_roots,kspan,rspan,grid_cells,pilot_disabled_fraction,same_basin_fraction,fused_grid_fraction,input_min,input_max,numeric_span,distinct_values,round1_us,round2_us,round3_us,round4_us,round5_us,round6_us,round7_us\n";
    file<<std::setprecision(10);
    u64 validated_banks=0;
    for(const auto& condition:all_cases()) {
        const auto& family=condition.family;const std::size_t n=condition.n;
        if(n>maxn || (!filter.empty() && family.find(filter)==std::string::npos)) continue;
        std::vector<std::vector<Record>> banks;
        for(unsigned b=0;b<BANKS;++b) banks.push_back(make_data(family,n,b));
        std::array<std::vector<Stats>,A> diagnostics;
        double minsum=0,maxsum=0,spansum=0,distinctsum=0;
        for(const auto& in:banks) {
            auto expected=in;standard_stable(expected,nullptr);
            minsum+=expected.front().value;maxsum+=expected.back().value;
            spansum+=u64(expected.back().value)-expected.front().value+1;
            std::size_t distinct=1;
            for(std::size_t i=1;i<expected.size();++i) distinct+=expected[i].value!=expected[i-1].value;
            distinctsum+=distinct;
            for(std::size_t ai=0;ai<A;++ai) {
                auto out=in;Stats s;algorithms[ai].run(out,&s);
                check_output(in,out,expected,algorithms[ai].stable);
                out=in;algorithms[ai].run(out,nullptr);
                check_output(in,out,expected,algorithms[ai].stable);
                diagnostics[ai].push_back(s);
            }
            ++validated_banks;
        }
        std::array<std::size_t,A> cycles;
        std::array<std::vector<double>,A> samples;
        for(std::size_t ai=0;ai<A;++ai) {
            const double one=timed(algorithms[ai],banks,1,0);
            cycles[ai]=std::max<std::size_t>(1,std::size_t((target_ms/1000)/std::max(one,1e-9)+0.999));
            cycles[ai]=std::min<std::size_t>(cycles[ai],100000);
        }
        std::mt19937_64 order_rng(0xB00B1Eull+n+family.size());
        for(unsigned round=0;round<ROUNDS;++round) {
            std::array<std::size_t,A> order;std::iota(order.begin(),order.end(),0);
            std::shuffle(order.begin(),order.end(),order_rng);
            for(auto ai:order) {
                const double seconds=timed(algorithms[ai],banks,cycles[ai],round);
                samples[ai].push_back(seconds*1e6/(cycles[ai]*BANKS));
            }
        }
        for(std::size_t ai=0;ai<A;++ai) {
            double roots=0,divs=0,recip=0,hits=0,misses=0,up=0,down=0,fallback=0;
            double ks=0,rs=0,cells=0,disabled=0,single=0,fused=0;
            for(const auto& s:diagnostics[ai]) {
                roots+=s.roots;divs+=s.divisions;recip+=s.reciprocal_quotients;
                hits+=s.hits;misses+=s.misses;up+=s.corrected_up;down+=s.corrected_down;
                fallback+=s.roots ? s.roots-1 : 0; // all measured BRC variants use one anchor root
                ks+=s.kspan;rs+=s.rspan;cells+=u64(s.kspan)*s.rspan;
                disabled+=s.pilot_disabled;single+=s.same_basin;fused+=s.fused_grid;
            }
            file<<family<<','<<n<<','<<algorithms[ai].name<<','<<algorithms[ai].stable
                <<','<<BANKS<<','<<ROUNDS<<','<<quantile(samples[ai],.5)
                <<','<<quantile(samples[ai],.1)<<','<<quantile(samples[ai],.9)
                <<','<<quantile(samples[ai],0)<<','<<quantile(samples[ai],1)
                <<','<<cycles[ai]*BANKS
                <<','<<roots/BANKS<<','<<divs/BANKS<<','<<recip/BANKS<<','<<hits/BANKS<<','<<misses/BANKS
                <<','<<up/BANKS<<','<<down/BANKS<<','<<fallback/BANKS
                <<','<<ks/BANKS<<','<<rs/BANKS<<','<<cells/BANKS
                <<','<<disabled/BANKS<<','<<single/BANKS<<','<<fused/BANKS
                <<','<<minsum/BANKS<<','<<maxsum/BANKS<<','<<spansum/BANKS<<','<<distinctsum/BANKS;
            for(double sample:samples[ai]) file<<','<<sample;
            file<<'\n';
        }
        file.flush();
        std::cerr<<"completed "<<family<<" n="<<n<<"\n";
    }
    std::cout<<"{\"benchmark_rows\":"<<(validated_banks/BANKS)*algorithms.size()
             <<",\"validated_input_banks\":"<<validated_banks
             <<",\"banks_per_condition\":"<<BANKS<<",\"rounds\":"<<ROUNDS
             <<",\"record_bytes\":"<<sizeof(Record)<<",\"target_ms\":"<<target_ms
             <<",\"instrumented_and_uninstrumented_checked\":true"
             <<",\"observable_sink\":"<<observed<<",\"result\":\"PASS\"}\n";
}
int main(int argc,char** argv) {
    try {
        if(argc==2 && std::string(argv[1])=="--verify") verify();
        else if(argc>=3 && std::string(argv[1])=="--bench")
            benchmark(argv[2],argc>3?std::stoull(argv[3]):1000000,
                      argc>4?std::stod(argv[4]):15,argc>5?argv[5]:"");
        else if(argc==2 && std::string(argv[1])=="--list")
            for(const auto& c:all_cases()) std::cout<<c.family<<','<<c.n<<'\n';
        else {
            std::cerr<<"usage: record_bench --verify | --list | --bench output.csv [max_n=1000000] [target_ms=15] [family_substring]\n";
            return 2;
        }
    } catch(const std::exception& e) {std::cerr<<e.what()<<'\n';return 1;}
}
