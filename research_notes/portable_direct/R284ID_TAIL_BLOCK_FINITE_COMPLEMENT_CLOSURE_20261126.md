# R284ID — Geometric tail-block payment and finite complement closure

2026-11-26. Author calculation and proof, NOT_REVIEWED. Scope: same auxiliary binary-tag safe-word total-count observer K, no native physical attribution. Own activity RA-B82240E8488EF5A1DA5186C4 / EM-DIRECT-0C386E; own recovery r1-20261126-0404-own-recovery confirmed original registration SUCCEEDED, session open, metadata only. Inventory r1-20261126-0404-owner-read SUCCEEDED, as_of 2026-11-25T20:05:12.144827Z, Source 1dcce57cb49b5e210a407c3e257379809c4837fe, LEASED query empty; no shared CLAIM or formal Result write.

Frozen inputs (all under research_notes/portable_direct/):
- IC @ 6a347839e01058e1953013562b1af46cb0603279 R284IC_MODE_ANCHORED_INTERVAL_CERTIFICATES_20261126.md
- IB @ 83bf56fa44b7dc12cb176c83222dac8a272546ac R284IB_ASYMMETRIC_PAYMENT_7300_ONSET_20261126.md
- HW @ 8c3bad026fc69c3a685218fc4677433a48310256 R284HW_UNIFORM_WEDGE_RESIDUAL_PAYMENT_20261125.md
- HY @ 0164790b93645d9e15c65baa4d77260fcaa8e1c9 R284HY_CAPACITY_COUPLING_AND_SQRT_DOMAIN_20261125.md
Read exact input definitions and relevant theorem statements. Current global entry blobs 7b0754aa0fdf6f34db53b0349b6b0ebe74ecda42 and 01de3bea2155db8c4ce29f832906b2df114f88bf, common immutable main pin not established at initial read. Current P000 V5, worldview, joint preservation, portable, method and residual rules loaded. No changes to premises.

## Result and coverage
For u=1201..7299 and 257<=h=u-q<=H(u), where H(u)=min(floor((u+9)/2), floor(sqrt(441u-1))), both strict adjacent comparisons K(q,u+1)>K(q,u) and K(q,u)>K(q+1,u) are certified by outward integer intervals. Here q>=0 and h>=257 so both comparisons exist. Exactly 6,549,662 base points, 13,099,324 comparisons, zero overlaps. Independently counted with integer square root, not inferred from the program's own count.

Consequently the finite complement is empty **relative to the pinned author theorems IB, HW, HY and IC**: u>=7300 by IB, u<=1200 or h<=256 by IC, otherwise h^2>=441u by HY or 2h>=u+10 by HW (u>=640), else ID. For omit only compare when h>=2; read at every 1<=h<=u. The combined all-integer monotonicity theorem therefore has an assembled proof at author level, with independent review of the analytic dependencies and executable certificate still pending. No new shared Result/Working Truth acceptance is asserted. Do not rerun completed rows just to expand coverage. The next useful unit is audit of the analytic dependencies, exact interval arithmetic and mother-question implications.

## 1. Exact observer and tail theorem
Use IC's M_n(k)=(k+1)/(n+1) binom(2n+2,n-k) for 0<=k<=n, zero outside; C_ab(g)=sum M_a(k)M_b(g-k). Set m=2u-h, q=u-h, Q=C_um(h-1), V=C_um(h), A=C_(u-1,m)(h)+C_(u-1,m)(h-1), E=M_(m-1)(0)[M_(u-1)(h)+M_(u-1)(h+1)]. K=(3u+q+1)^2(A+E)Q/[(u+2q+1)(Q+V+qA)^2].
P_k=M_u(k)M_m(h-k); W_k=P_k/P_mode. The exact step ratio is
 P_(k+1)/P_k=(k+2)(u-k) l(m+l+2)/[(k+1)(u+k+3)(l+1)(m-l+1)], l=h-k.
Log-concavity (each factor port has decreasing successive ratios, including reversed port) gives nonincreasing outward ratios on each side of the mode. Reuse IC's exact normalized joint contributions:
 V'=sum W, Q'=sum W*t(l), A'=sum W*v(k)*(1+t(l)),
 t(l)=l(m+l+2)/[(l+1)(m-l+1)], v(k)=(u-k)(u+k+2)/[2u(2u+1)].
 E'=0 at h=u; otherwise E'=W_h*v(h)*(1+r)*(m+2)/(4m+2), r=(h+2)(u-1-h)/[(h+1)(u+h+2)].
The shared normalization cancels in K; it is not a claim about other observers.

Let S=2^48. If the first omitted outward branch has S W<=B (integer upper endpoint) and the ratio of that branch to its preceding included branch is r0=a/b<=1, log-concavity bounds all subsequent ratios by r0. For N remaining branches, their scaled total T lies in [0,J], J=min(NB,ceil(B*b/(b-a))) when a<b, J=NB otherwise. This follows by geometric summation or N times the first upper bound. No positive mass is erased. Since t(l) increases with l (both nonnegative factors l/(l+1), (m+l+2)/(m-l+1) increase), use T times t(lmax) as the Q upper payment; for A use T*(1+t(lmax))/2 because 0<=v<=1/2. Each payment is rounded outward. For the right tail, E upper payment is B: v<=1/2, 1+r<5/2 for h>=1, (m+2)/(4m+2)<=1/2, so its coefficient is <1. Left tail contains no k=h boundary. Bounds apply separately to declared V,Q,A,E observations, not a global claim that branch identities are redundant. Peak search and non-tail recurrence are IC. Full final cross products use cpp_int.

## 2. Arithmetic safety and coverage
Executed u<=7300; sample u<=7299. All n,m,h and linear factors in step() <2^15, so step products <2^60. Every outward W endpoint <=S (integer ceil of a nonincreasing ratio). Individual multipliers in accumulation have numerator/denominator <2^60; products with W <2^108, and ceil addition <2^109. Tail mass <=N*cutoff<2^33 for the two executed cutoffs, geometric numerator <2^80. t<=2^15; v<=1/2; sums and q*A <2^92. For endpoint conversion, Vlo>=S and Vhi-Vlo<=2(h+1)^2+2(h+1)*cutoff<2^35: ordinary outward interval width increases by <=2 at each step and at most two tail blocks each paid by N*cutoff. Thus Vhi<2Vlo. Each of Qhi,Ahi<=2^16 Vlo plus at most h+1 rounding units; Ehi<=2Vlo. Dlo>=Vlo; the upper scaled K bound is consequently <2^115 using Lnum<2^30 and Lden>=1. All 128-bit operations and conversion are in range; final products use exact big integers. Printed min gap/max width fit uint64 in these executed grids (actual values below; the bound for general endpoint is larger).
H(u) is nondecreasing. For each base row u the program evaluates from h=256 through H(u)+1 (clipped at u), so same-row omit neighbor and next-row read neighbor both included; next-row h+1 is <=H(u+1)+1. Extra row and neighbors are evaluated but not counted as new base comparisons. Integer crosscheck of coverage uses H=min((u+9)//2,isqrt(441*u-1)); each row contributes H-256 for each direction. Five disjoint consecutive row intervals cover all missing rows.
Complexity remains O(h) worst case per point, O(log h) mode search, O(H) row memory, bounded-width recurrence and constant big integer endpoint evaluation. Tail payments reduce visited branch count, not an asserted asymptotic improvement. No matched full no-tail runtime benchmark in this round.

## 3. Actual runs
First parallel launch timed out; only its completed first block has a valid final summary. Other blocks rerun serially; no incomplete run counted. Exact source compiled with g++ -O3 -std=c++17 check.cpp -o check. Five completed stdout lines:
```
L=1201 U=2400 D0=257 D1=0 cutoff=64 points=724959 read=721785 omit=721785 unresolved=0 min_gap=1069330200 max_width=15 visits=248228262 blocks=1192517 omitted=165657010
L=2401 U=3600 D0=257 D1=0 cutoff=1048576 points=1073660 read=1070254 omit=1070254 unresolved=0 min_gap=436694924 max_width=20692 visits=389267798 blocks=1865109 omitted=368706509
L=3601 U=4800 D0=257 D1=0 cutoff=1048576 points=1327638 read=1324037 omit=1324037 unresolved=0 min_gap=237707823 max_width=9438 visits=562673954 blocks=2211242 omitted=513580967
L=4801 U=6000 D0=257 D1=0 cutoff=1048576 points=1546914 read=1543142 omit=1543142 unresolved=0 min_gap=149927376 max_width=5844 visits=736151387 blocks=2507588 omitted=658337841
L=6001 U=7299 D0=257 D1=0 cutoff=1048576 points=1894582 read=1890444 omit=1890444 unresolved=0 min_gap=100154085 max_width=4116 visits=992398508 blocks=3012391 omitted=875635533
```
Totals: points evaluated including boundary reuse 6,567,753; explicit branches 2,928,719,909; tail blocks 10,788,847 enclosing 2,581,917,860 branches (46.85334% of total branch visits without grouping). Minimum strict separation 100154085 units of 2^-48; largest width 20692 units. Timings 20.53 s (first concurrent), 11.31, 17.32, 20.42, 28.22 s (serial). IC's 4,556,589 distinct comparisons lie outside ID base domain; combined 17,655,913 finite comparisons, excluding analytic-covered rows where not needed.

Independent exact integer crosschecks: 37 sample lines per cutoff (some small-u duplicate points), both cutoffs passed. For cutoff 64 the sample used 28 tail blocks enclosing 15749 branches; cutoff 1048576 used 30 blocks enclosing 16548. Exact full integer counts rather than approximate weights were evaluated by direct binomial for n<=500, exact integer recurrence otherwise, through u=7299. Sample source and independent Python verifier below.

## 4. Reproduction
Local executed check.cpp SHA256: 31b56c0e6e788c5e3e2f6cb2eb0410f133798db152494e9c85ae7353bfc5e697. The following is the executed source.
```cpp
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>
using I=__uint128_t; using Z=boost::multiprecision::cpp_int;
constexpr I S=I(1)<<48;
struct B{I lo=0,hi=0;}; B add(B a,B b){return {a.lo+b.lo,a.hi+b.hi};} B mul(B a,I n,I d){assert(d);return {a.lo*n/d,(a.hi*n+d-1)/d};}
struct Rat{I n,d;}; Rat step(int u,int m,int h,int k){int l=h-k;return {I(k+2)*(u-k)*l*(m+l+2),I(k+1)*(u+k+3)*(l+1)*(m-l+1)};}
uint64_t visited=0,skipped=0,blocks=0; I cutoff=64;
B value(int u,int h){assert(1<=h&&h<=u&&u<=7301);int q=u-h,m=u+q;
 int left=0,right=h;while(left<right){int k=(left+right)/2;auto r=step(u,m,h,k);if(r.n>r.d)left=k+1;else right=k;}int mode=left;B V,Q,A,E;
 auto t=[&](int l)->Rat{return {I(l)*(m+l+2),I(l+1)*(m-l+1)};};
 auto accum=[&](int k,B w){int l=h-k;auto r=t(l);I vn=I(u-k)*(u+k+2),vd=I(2)*u*(2*u+1);V=add(V,w);Q=add(Q,mul(w,r.n,r.d));A=add(A,mul(w,vn*(r.d+r.n),vd*r.d));if(k==h&&h<u){I rn=I(h+2)*(u-1-h),rd=I(h+1)*(u+h+2);E=mul(mul(mul(w,vn,vd),rd+rn,rd),m+2,4*m+2);}++visited;};
 // w bounds first omitted weight; r bounds the ratios between subsequent omitted weights.
 auto tail=[&](B w,int N,Rat r,int lmax,bool includes_right){assert(N>0&&r.n<=r.d);I mass=w.hi*N;if(r.n<r.d)mass=std::min(mass,(w.hi*r.d+(r.d-r.n)-1)/(r.d-r.n));B b{0,mass};auto s=t(lmax);V=add(V,b);Q=add(Q,mul(b,s.n,s.d)); // v<=1/2
 A=add(A,mul(b,s.n+s.d,2*s.d));if(includes_right&&h<u)E=add(E,{0,w.hi});++blocks;skipped+=N;};
 B w{S,S};accum(mode,w);for(int k=mode;k<h;++k){auto r=step(u,m,h,k);assert(r.n<=r.d);w=mul(w,r.n,r.d);if(w.hi<=cutoff){tail(w,h-k,r,h-k-1,true);break;}accum(k+1,w);}w={S,S};for(int k=mode;k>0;--k){auto r=step(u,m,h,k-1);assert(r.n>=r.d);w=mul(w,r.d,r.n);if(w.hi<=cutoff){tail(w,k,{r.d,r.n},h,false);break;}accum(k-1,w);}
 I dl=Q.lo+V.lo+q*A.lo,dh=Q.hi+V.hi+q*A.hi;assert(dl>0);Z Lnum=Z(3*u+q+1)*(3*u+q+1),Lden=u+2*q+1;Z nl=Z(S)*Lnum*Z(A.lo+E.lo)*Z(Q.lo),nh=Z(S)*Lnum*Z(A.hi+E.hi)*Z(Q.hi);Z dlow=Lden*Z(dl)*Z(dl),dhigh=Lden*Z(dh)*Z(dh);return {(nl/dhigh).convert_to<I>(),((nh+dlow-1)/dlow).convert_to<I>()};}
// D1=0: complement of HW/HY and IC for u>=1201.
int cap(int u){int a=0,b=u+1;while(a+1<b){int c=(a+b)/2;if(1LL*c*c<441LL*u)a=c;else b=c;}return std::min(a,(u+9)/2);}
int main(int argc,char**argv){int L=std::stoi(argv[1]),U=std::stoi(argv[2]),D0=std::stoi(argv[3]),D1=std::stoi(argv[4]);cutoff=std::stoull(argv[5]);assert(L>=1&&L<=U&&U<=7299&&D0>=1&&(D0<=D1 || (D1==0&&L>=1201&&D0==257)));uint64_t r=0,o=0,fail=0,points=0;I minGap=~I(0),maxWidth=0;std::vector<B> prev;
 for(int u=L;u<=U+1;++u){int H=std::min(u,(D1?D1:cap(u))+1);std::vector<B>cur(H+1);for(int h=std::max(1,D0-1);h<=H;++h){cur[h]=value(u,h);++points;maxWidth=std::max(maxWidth,cur[h].hi-cur[h].lo);}auto ck=[&](B a,B b,int h,char t){if(a.lo<=b.hi){++fail;std::cerr<<"unresolved "<<u<<" "<<h<<" "<<t<<"\n";}else minGap=std::min(minGap,a.lo-b.hi);};if(u<=U)for(int h=std::max(2,D0);h<=std::min(u,D1?D1:cap(u));++h){ck(cur[h],cur[h-1],h,'O');++o;}if(u>L)for(int h=D0;h<=std::min(u-1,D1?D1:cap(u-1));++h){ck(cur[h+1],prev[h],h,'R');++r;}prev.swap(cur);}
 std::cout<<"L="<<L<<" U="<<U<<" D0="<<D0<<" D1="<<D1<<" cutoff="<<(uint64_t)cutoff<<" points="<<points<<" read="<<r<<" omit="<<o<<" unresolved="<<fail<<" min_gap="<<(uint64_t)minGap<<" max_width="<<(uint64_t)maxWidth<<" visits="<<visited<<" blocks="<<blocks<<" omitted="<<skipped<<"\n";return fail!=0;}
```
Replay:
```sh
g++ -O3 -std=c++17 check.cpp -o check
./check 1201 2400 257 0 64
./check 2401 3600 257 0 1048576
./check 3601 4800 257 0 1048576
./check 4801 6000 257 0 1048576
./check 6001 7299 257 0 1048576
```
Crosscheck:
```cpp
#define main grid_main
#include "check.cpp"
#undef main
int main(){for(int u: {1,2,10,35,80,200,500,1201,2400,7299})for(int h: {1,u/4,u/2,u})if(h>=1){auto b=value(u,h);std::cout<<u<<' '<<h<<' '<<Z(b.lo)<<' '<<Z(b.hi)<<'\n';}std::cerr<<"blocks="<<blocks<<" skipped="<<skipped<<'\n';}
```
Compile as sample.cpp, run ./sample > sample.txt. For the second cutoff insert cutoff=1048576; at start of main and redirect to sample20.txt. Verify with Python (repeat for both files):
```python
from math import comb,isqrt
from fractions import Fraction
from functools import lru_cache
@lru_cache(None)
def M(n,k):
 if not 0<=k<=n:return 0
 x,r=divmod((k+1)*comb(2*n+2,n-k),n+1);assert not r;return x
@lru_cache(None)
def arr(n):
 a=[comb(2*n+2,n)//(n+1)]
 for k in range(n):
  x,r=divmod(a[-1]*(k+2)*(n-k),(k+1)*(n+k+3));assert not r;a.append(x)
 return a
def m(n,k):return (M(n,k) if n<=500 else arr(n)[k]) if 0<=k<=n else 0
def C(n,p,g):return sum(m(n,k)*m(p,g-k) for k in range(g+1))
N=0
for line in open('sample.txt'):
 u,h,lo,hi=map(int,line.split());q=u-h;p=u+q
 Q=C(u,p,h-1);V=C(u,p,h);A=C(u-1,p,h)+C(u-1,p,h-1);E=m(p-1,0)*(m(u-1,h)+m(u-1,h+1))
 K=Fraction((3*u+q+1)**2*(A+E)*Q,(u+2*q+1)*(Q+V+q*A)**2)
 assert lo<=K*(1<<48)<=hi,(u,h,lo,hi)
 N+=1
print('exact integer crosschecks:',N)
d=lambda u:min((u+9)//2,isqrt(441*u-1))
for L,U in [(1201,2400),(2401,3600),(3601,4800),(4801,6000),(6001,7299)]:
 print(L,U,sum(d(u)-256 for u in range(L,U+1)))
```
Actual outputs: 37 crosschecks each; row counts 721785, 1070254, 1324037, 1543142, 1890444 respectively.

Remaining: independent review of complete assembled proof, especially analytic onset IB and HW/HY assumptions and finite IC/ID coverage/arithmetic. No remaining base parameter positions under these pinned prior author theorems. Review may reveal a dependency defect; retain evidence and repair the precise affected region. Continue mother objective implications rather than more finite enumeration.
