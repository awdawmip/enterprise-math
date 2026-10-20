#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <set>
#include <vector>
using i64 = std::int64_t;

static i64 product(const std::vector<int>& P){ i64 q=1; for(int p:P) q*=p; return q; }
static bool wheel_strike(i64 n,const std::vector<int>& P){ for(int p:P) if(n%p==0) return true; return false; }
static bool actual_union_strike(i64 n,const std::vector<int>& P){ for(int p:P) if(n>=1LL*p*p && n%p==0) return true; return false; }
static std::vector<int> support(i64 d,const std::vector<int>& P){ std::vector<int> J; for(int p:P) if(d%p!=0) J.push_back(p); return J; }

static std::pair<i64,i64> generic_separator_gap_count(const std::vector<int>& P,i64 d){
    const i64 Q=product(P); i64 first=-1,prev=-1,best=0,count=0;
    for(i64 x=0;x<Q;++x){
        bool a=wheel_strike(x,P), b=wheel_strike((x+d)%Q,P);
        if(a==b) continue;
        ++count; if(first<0) first=x; if(prev>=0) best=std::max(best,x-prev); prev=x;
    }
    assert(first>=0); best=std::max(best,Q+first-prev); return {best,count};
}

static bool in_defect(i64 x,const std::vector<int>& P){
    if(x==0) return true;
    return std::find(P.begin(),P.end(),(int)x)!=P.end();
}

static void check_finite_defect_lift(){
    const std::vector<int> P={2,3,5,7}; const i64 Q=product(P); const i64 mu=8;
    // Prime-prefix Boolean actual stream equals the wheel with exactly D={0} union P toggled.
    for(i64 n=0;n<2*Q;++n){
        bool lhs=actual_union_strike(n,P);
        bool rhs=wheel_strike(n%Q,P) ^ in_defect(n,P);
        assert(lhs==rhs);
    }
    // Exact pair separator lift:
    // A(a+t) xor A(b+t) = M_{b-a}(a+t) xor 1_D(a+t) xor 1_D(b+t).
    for(i64 a=0;a<mu+Q;++a){
        for(i64 b=a+1;b<mu+Q;++b){
            i64 d=b-a;
            for(i64 t=0;t<2*Q;++t){
                bool direct=actual_union_strike(a+t,P)^actual_union_strike(b+t,P);
                bool lifted=(wheel_strike((a+t)%Q,P)^wheel_strike((a+t+d)%Q,P))
                            ^in_defect(a+t,P)^in_defect(b+t,P);
                assert(direct==lifted);
            }
        }
    }
}

static void check_support_orbit_boundary(){
    const std::vector<int> P={2,3,5}; const i64 Q=30;
    const i64 d1=6,d2=12;
    assert((support(d1,P)==std::vector<int>{5}));
    assert(support(d1,P)==support(d2,P));
    // d2 = 7*d1 mod 30 with 7 a unit: same multiplicative-unit orbit.
    assert(std::gcd<i64>(7,Q)==1 && (7*d1)%Q==d2);
    auto [g1,c1]=generic_separator_gap_count(P,d1);
    auto [g2,c2]=generic_separator_gap_count(P,d2);
    assert(c1==4 && c2==4);       // same Hamming separator mass
    assert(g1==14 && g2==10);     // different additive gap geometry
    assert(g1-1==13 && g2-1==9);  // different local future horizons
}

static void check_generic_eventual_domination_failure(){
    // Period-2 steady word W=0101... has steady separation radius 0.
    // Finite defects can nevertheless make transient shift residuals agree arbitrarily long.
    const int m=50;
    auto W=[](int n){return bool(n&1);};
    auto D=[&](int n){return n>=0 && n<=2*m && n%2==0;};
    auto A=[&](int n){return W(n)^D(n);};
    int lcp=0; while(A(lcp)==A(lcp+1)) ++lcp;
    assert(lcp==2*m+1);
}

static int transient_vs_steady_max(const std::vector<int>& P,int expected_s,i64 expected_d){
    const i64 Q=product(P); const int mu=P.back()+1;
    std::vector<unsigned char> W((size_t)Q);
    for(i64 x=0;x<Q;++x) W[(size_t)x]=wheel_strike(x,P);

    int best=-1,best_s=-1; i64 best_b=-1;
    for(int s=0;s<mu;++s){
        for(i64 b=0;b<Q;++b){
            int h=0;
            while(h<=best && actual_union_strike(s+h,P)==bool(W[(size_t)((b+h)%Q)])) ++h;
            if(h<=best) continue;
            while(h<2000 && actual_union_strike(s+h,P)==bool(W[(size_t)((b+h)%Q)])) ++h;
            if(h>best){best=h;best_s=s;best_b=b;}
        }
    }
    // Also include transient/transient pairs.
    for(int s=0;s<mu;++s) for(int t=s+1;t<mu;++t){
        int h=0; while(h<2000 && actual_union_strike(s+h,P)==actual_union_strike(t+h,P)) ++h;
        if(h>best){best=h;best_s=s;best_b=t;}
    }
    assert(best_s==expected_s);
    assert((best_b-best_s+Q)%Q==expected_d);
    return best;
}

static void check_large_prime_prefix_transients(){
    const std::vector<int> P17={2,3,5,7,11,13,17};
    const std::vector<int> P19={2,3,5,7,11,13,17,19};
    int t17=transient_vs_steady_max(P17,12,217140);
    int t19=transient_vs_steady_max(P19,18,9699690/19);
    assert(t17==91);
    assert(t19==173);
    // Independent steady certificates give rho(17#)=237 locally and
    // companion r005a_boolean_rho19_certificate.cpp proves rho(19#)=365.
    assert(t17<237 && t19<365);
}

int main(){
    check_finite_defect_lift();
    check_support_orbit_boundary();
    check_generic_eventual_domination_failure();
    check_large_prime_prefix_transients();
    std::cout << "R005-A Boolean future defect/orbit regressions passed\n";
}
