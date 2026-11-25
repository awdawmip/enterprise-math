# R284IC — Mode-anchored integer interval transport and finite K certificates

2026-11-26. Author proof and executed finite computation; NOT_REVIEWED. Auxiliary binary-tag safe-word total-count observer, not native physical attribution. Frozen definition and comparison frontier: R284IB @ 83bf56fa44b7dc12cb176c83222dac8a272546ac : research_notes/portable_direct/R284IB_ASYMMETRIC_PAYMENT_7300_ONSET_20261126.md (full text read). IB gives onset 7300 with its pinned dependencies; this work's finite certificate does not assume their sign claims. P000 V5, ACTIVE worldview, joint-observer, residual-fidelity, portable/method rules read. Global entries matched main@3d3cffa94df1e1e96b982f33b6df097aa6b51873. Own registration r1-20261124-0256-r284gd-session-v1 recovered, EM-DIRECT-0C386E / RA-B82240E8488EF5A1DA5186C4. Owner inventory r1-20261126-0302-owner-read SUCCEEDED, as_of 2026-11-25T19:03:42.975722Z, no LEASED rows; source drift explicitly recorded by receipt. No shared CLAIM or Result mutation.

## Finite theorem and observer reduction

Let 1<=u, 0<=q<u, h=u-q, m=u+q. Use IB's M_n(k)=(k+1)/(n+1)*binom(2n+2,n-k), zero outside 0<=k<=n. Set C_(n,m)(g)=sum_k M_n(k)M_m(g-k), Q=C_(u,m)(h-1), V=C_(u,m)(h), A=C_(u-1,m)(h)+C_(u-1,m)(h-1), E=M_(m-1)(0)[M_(u-1)(h)+M_(u-1)(h+1)]. K=(3u+q+1)^2*(A+E)*Q/[(u+2q+1)*(Q+V+qA)^2].

**Executed finite theorem.** For each valid base point in {u<=1200} union {u<=7299,h<=256}, K(q,u+1)>K(q,u), and when q+1<u, K(q,u)>K(q+1,u). Two complete runs certified 2,281,944 distinct read and 2,274,645 distinct omit comparisons (4,556,589 total; overlap removed by counting). No unresolved comparison in either completed run. The finite theorem is independent of IB's proof of the unbounded onset. In combination with IB, all h<=256 are covered for all u, and the remaining possible finite gap lies in 1201<=u<=7299, h>=257, before subtracting earlier proven regions.

New exact carrier: P_k=M_u(k)M_m(h-k), k=0..h. Let l=h-k. The successive ratio is
P_(k+1)/P_k = [(k+2)(u-k)l(m+l+2)]/[(k+1)(u+k+3)(l+1)(m-l+1)].
Each M_n has decreasing adjacent ratio (k+2)/(k+1)*(n-k)/(n+k+3). Hence the joint ratio decreases; choose a maximum branch index k0 by binary search for the first ratio <=1 (or h). For W_k=P_k/P_k0, W_k0=1; propagate outwards with positive rational factors <=1. This avoids exponential underflow of separately normalized ports. Every branch remains in the calculation. Let
t(l)=l(m+l+2)/[(l+1)(m-l+1)],
v(k)=(u-k)(u+k+2)/[2u(2u+1)].
These equal M_m(l-1)/M_m(l) and M_(u-1)(k)/M_u(k), including t(0)=0, v(u)=0. Consequently the four true counts divided by P_k0 are exactly
V'=sum W_k; Q'=sum W_k*t(l); A'=sum W_k*v(k)*(1+t(l));
E'=W_h*v(h)*(1+r)*gamma_m if h<u, and 0 otherwise,
where r=(h+2)(u-1-h)/[(h+1)(u+h+2)] and gamma_m=(m+2)/(4m+2).
The common factor cancels in K. No independent marginal substitution or removal of structural boundary E occurs. This quotient is sufficient specifically for the K observer and the two independently evaluated adjacent comparisons, not a global joint-state quotient.

## Integer interval certificate

Set S=2^48. For an interval [a,b] in units 1/S, multiplication by positive rational n/d gives [floor(a*n/d),ceil(b*n/d)]. Addition is endpoint addition. Initialize mode at [S,S]. Since every outward step has n<=d, each step increases interval width by at most two integer units; all W endpoints remain between 0 and S. In particular no relative-precision assumption is made for a tiny branch. Its omitted sub-unit portion is enclosed by the upper endpoint, and participates in all sums.

Calculate interval sums Q',V',A',E' via the preceding formulas; all terms are nonnegative, so direct monotone endpoint substitution in numerator and inverse substitution in denominator bounds K. Let B=Q'+V'+qA'. The exact floor/ceil of S*(3u+q+1)^2*(A'+E')*Q'/[(u+2q+1)*B^2] at the appropriate endpoints gives the final integer enclosure for S*K. The shared counts are kept in both numerator and denominator; interval substitution may overestimate uncertainty but cannot reverse a true sign. The certificate is the disjointness of the two enclosures, not floating-point agreement.

Arithmetic safety for implemented u<=7301: m<=14601, h<=7301; each individual linear factor in step and t is <2^15, hence numerator/denominator products of at most four factors <2^60. In v*(1+t), numerator and denominator products (including the sum td+tn) <2^62. Since W endpoints <=2^48, individual recurrence/weighted multiplication intermediates <2^111, including ceiling addition. t<=2^15, v<=1/2, r<=2 and gamma_m<=1; interval sums <2^78 including q multiplier (<2^13), more conservatively <2^92. The sequential E multiplications have ample headroom as well. Thus unsigned 128-bit interval intermediates are exact, no wraparound. Final cross products and quotients use arbitrary precision cpp_int; denominator lower endpoint is asserted positive. The returned K interval fits in 128 bits: S*K_upper <= S*(3u+q+1)^2*(1+2)*(S+rounding scale factor)/[u+2q+1] using Q,V<=B, A<=B, E<=2S in scaled units and B>=S, so a looser bound <2^100 suffices. The printed extrema fit in uint64_t on the executed grids.

Complexity: O(h) fixed-width recurrence/accumulation per parameter, O(log h) mode search, a constant number of bounded-size big-int operations for final endpoints; O(D) row memory. Cost of the whole triangle is still cubic in U, and no whole-domain speedup measurement is claimed. Reuse of two consecutive rows ensures each point is evaluated once per run and certifies all requested reading/omission neighbors; for a read at base (u,h), compare next-row (u+1,h+1), for omit compare same-row (u,h-1). Extra row U+1 and extra deficit D+1 are used only for comparison boundaries. An interval overlap would be reported as unresolved, not a failed strict inequality; a future exact fallback can consume that point.

## Reproduction (C++17, GCC with Boost.Multiprecision)

Save as check.cpp; compile `g++ -O3 -std=c++17 check.cpp -o check`. Actual source SHA256 b5a5233e324fea921cab1ae6a969602bff6a0ffd123b8e814d1ee0703e190a15 (local compiled file; embedded text includes the trailing newline).

```cpp
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>
using I=__uint128_t;
using Z=boost::multiprecision::cpp_int;
constexpr I S=I(1)<<48;
struct B{I lo=0,hi=0;};
B add(B a,B b){return {a.lo+b.lo,a.hi+b.hi};}
B mul(B a,I n,I d){assert(d);return {a.lo*n/d,(a.hi*n+d-1)/d};}
struct Rat{I n,d;};
Rat step(int u,int m,int h,int k){int l=h-k;return {I(k+2)*(u-k)*l*(m+l+2),I(k+1)*(u+k+3)*(l+1)*(m-l+1)};}
B value(int u,int h){
 assert(1<=h&&h<=u&&u<=7301);int q=u-h,m=u+q;
 // First non-increasing ratio. Every outward multiplier is <=1.
 int left=0,right=h;while(left<right){int k=(left+right)/2;auto r=step(u,m,h,k);if(r.n>r.d)left=k+1;else right=k;}
 int mode=left;B V,Q,A,E;
 auto accumulate=[&](int k,B w){int l=h-k;I tn=I(l)*(m+l+2),td=I(l+1)*(m-l+1);I vn=I(u-k)*(u+k+2),vd=I(2)*u*(2*u+1);
 V=add(V,w);Q=add(Q,mul(w,tn,td));A=add(A,mul(w,vn*(td+tn),vd*td));
 if(k==h && h<u){I rn=I(h+2)*(u-1-h),rd=I(h+1)*(u+h+2);E=mul(mul(mul(w,vn,vd),rd+rn,rd),m+2,4*m+2);}
 };
 B w{S,S};accumulate(mode,w);for(int k=mode;k<h;++k){auto r=step(u,m,h,k);assert(r.n<=r.d);w=mul(w,r.n,r.d);accumulate(k+1,w);}w={S,S};for(int k=mode;k>0;--k){auto r=step(u,m,h,k-1);assert(r.n>=r.d);w=mul(w,r.d,r.n);accumulate(k-1,w);}
 I dl=Q.lo+V.lo+q*A.lo,dh=Q.hi+V.hi+q*A.hi;assert(dl>0);
 Z Lnum=Z(3*u+q+1)*(3*u+q+1),Lden=u+2*q+1;
 Z nl=Z(S)*Lnum*Z(A.lo+E.lo)*Z(Q.lo),nh=Z(S)*Lnum*Z(A.hi+E.hi)*Z(Q.hi);
 Z dlow=Lden*Z(dl)*Z(dl),dhigh=Lden*Z(dh)*Z(dh);
 return {(nl/dhigh).convert_to<I>(),((nh+dlow-1)/dlow).convert_to<I>()};
}
int main(int argc,char**argv){int U=std::stoi(argv[1]),D=std::stoi(argv[2]);assert(U<=7300&&D>=1);uint64_t r=0,o=0,fail=0,points=0;I minGap=~I(0),maxWidth=0;std::vector<B> prev;
 for(int u=1;u<=U+1;++u){int H=std::min(u,D+1);std::vector<B> cur(H+1);for(int h=1;h<=H;++h){cur[h]=value(u,h);++points;maxWidth=std::max(maxWidth,cur[h].hi-cur[h].lo);}
 auto check=[&](B larger,B smaller,int h,char type){if(larger.lo<=smaller.hi){++fail;std::cerr<<"unresolved "<<u<<" "<<h<<" "<<type<<"\n";}else minGap=std::min(minGap,larger.lo-smaller.hi);};
 if(u<=U)for(int h=2;h<=std::min(u,D);++h){check(cur[h],cur[h-1],h,'O');++o;}
 if(u>=2)for(int h=1;h<=std::min(u-1,D);++h){check(cur[h+1],prev[h],h,'R');++r;}
 prev.swap(cur);
 }
 std::cout<<"U="<<U<<" D="<<D<<" bits=48 points="<<points<<" read="<<r<<" omit="<<o<<" unresolved="<<fail<<" min_gap_units="<<(uint64_t)minGap<<" max_width_units="<<(uint64_t)maxWidth<<"\n";return fail!=0;
}
```

Actual completed outputs (wall time measured by /usr/bin/time; machine-specific):
```
U=300 D=300 bits=48 points=45451 read=45150 omit=44850 unresolved=0 min_gap_units=79203450691 max_width_units=115120
0.22 s
U=1200 D=1200 bits=48 points=721801 read=720600 omit=719400 unresolved=0 min_gap_units=4249132450 max_width_units=1103827
10.20 s
U=7299 D=256 bits=48 points=1843204 read=1835904 omit=1828605 unresolved=0 min_gap_units=101304176 max_width_units=90334
9.06 s
```
The separate run 2000 2000 timed out without a final summary; excluded entirely. The 300 run is nested in 1200. Overlap of 1200 and 7299/256 runs: sum_{u=1}^{1200}min(u,256)=274560 read comparisons, minus 1200 gives 273360 omit comparisons. Thus distinct counts stated above.

Independent direct binomial/Fraction crosscheck executed at all 630 points 1<=u<=35, 1<=h<=u, against final interval endpoints, all passed. Reproduce with:
```cpp
#define main grid_main
#include "check.cpp"
#undef main
int main(){for(int u=1;u<=35;++u)for(int h=1;h<=u;++h){auto b=value(u,h);std::cout<<u<<' '<<h<<' '<<(uint64_t)b.lo<<' '<<(uint64_t)b.hi<<'\n';}}
```
Compile this as sample.cpp and run ./sample > sample.txt.
```python
from math import comb
from fractions import Fraction
from functools import lru_cache
@lru_cache(None)
def M(n,k):
 if not 0<=k<=n:return 0
 x,r=divmod((k+1)*comb(2*n+2,n-k),n+1);assert not r;return x
def C(n,m,g):return sum(M(n,k)*M(m,g-k) for k in range(g+1))
N=0
for line in open('sample.txt'):
 u,h,lo,hi=map(int,line.split());q=u-h;m=u+q
 Q=C(u,m,h-1);V=C(u,m,h);A=C(u-1,m,h)+C(u-1,m,h-1);E=M(m-1,0)*(M(u-1,h)+M(u-1,h+1))
 K=Fraction((3*u+q+1)**2*(A+E)*Q,(u+2*q+1)*(Q+V+q*A)**2)
 assert lo<=K*(1<<48)<=hi,(u,h,K,lo,hi)
 N+=1
print('exact binomial independent crosschecks:',N)
```
Actual stdout: exact binomial independent crosschecks: 630.

Next: use proved analytic regions to omit already settled comparisons; extend finite coverage in checkpointable row ranges. Mode-outward monotone tails admit certified bulk upper mass bounds; avoid counting an unfinished run as exhaustive coverage. Seek a quantitative tail grouping certificate and exact fallback for any overlapped interval. Independent review and strict Activity observation audit pending.
