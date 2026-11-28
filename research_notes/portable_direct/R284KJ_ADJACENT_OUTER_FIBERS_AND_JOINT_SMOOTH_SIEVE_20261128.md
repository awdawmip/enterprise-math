# R284KJ — Adjacent outer fibers and joint smooth-composite sieve
2026-11-28. Author proof and local exact computations, NOT_REVIEWED; auxiliary arithmetic of R284, not a native spatial transfer. Own recovery r1-20261128-1400-own-recovery confirms original open RESEARCHER registration r1-20261124-0256-r284gd-session-v1, no formal own runs; EM-DIRECT-0C386E / TASK_RESEARCH / RA-B82240E8488EF5A1DA5186C4 (existing Activity). Current owner inventory r1-20261128-1400-owner-read queued then RUNNING (source ba259d8004d4a8a3616cd739e2b8a6961f0ccd61); subsequent receipt read failed BACKEND_IDENTITY_CHECK_UNAVAILABLE, operation_sent=false. Current terminal inventory not established at this observation. No shared Task/CLAIM mutation; independent continuation of own existing research line. Global main 98d183ac8e00894237e44bf1b84faae71f9bed19 entry blobs verified. P000 V4/V5, ACTIVE worldview, joint/residual contracts, portable and current method consulted.

Frozen inputs: KI 206cb02a626169e6dc075566a80666bb2bfe763e:research_notes/portable_direct/R284KI_FACTORIAL_FIXED_DIVISOR_AND_NORMALIZED_PERIOD_20261128.md; KG 0c5c18b5e6725fcdebad3c12b9ebec33659ba12f:research_notes/portable_direct/R284KG_SEXTIC_POLE_FIBER_AND_PRIMITIVE_COMPOSITE_SIEVE_20261128.md; JR 88211c0912397b00536b6c4d6427cab29d4499f2:research_notes/portable_direct/R284JR_GLOBAL_BUDGET_POLYNOMIAL_AND_INTEGER_ROOT_EXCLUSION_20261127.md; KD 544d7a97fa075fe62848ae1cf27acdb9bdc7df19:research_notes/portable_direct/R284KD_FINITE_BRIDGE_AND_MODULAR_FALLBACK_20261128.md (bracket as carried by KG). JH decfd2e7f01e53d1036716b13efda9bf1bb36e87:research_notes/portable_direct/R284JH_SECOND_BRANCH_REMOVABLE_POLE_AND_HALF_WINDOW_20261127.md states r=1 already treated in JA, so this note makes no novelty claim for that pole direction. JO 81cc0f06a4cf0209733a50284362f9bb1e8aded9 covers 3<=r<=d. JP/JQ treat q itself. KI's low yield of small-prime global fixed-divisor normalization motivates changing to adjacent whole-composite coordinates instead of repeating its unfinished p=7 calculation.

## 1. Exact adjacent outer fibers of the cleared carrier (all d>=3)

Let u=q+d, n=2q+d, l=d-k; S_v(k)=prod_{i<k}(v-i) prod_{k<=i<d}(v+i+3). Retain JR's polynomial weights a_k=(k+1)(l+1)S_u(k)S_n(l), b_k=(k+1)l S_u(k)S_n(l-1) (zero when l=0). Write v=sum a_k, b=sum b_k, a=sum (u-k)(u+k+2)(a_k+b_k). J=2u(2u+1), L=4n+2; Wn=L a+u S_u(d)D_n q(2d+3)(n+2), Qn=JL b, Zn=L(q a+J(b+v)), D_n=S_n(0). P=3q(4q+3d+1)^2 Wn Qn-32(3q+d+1)Zn^2, D=JL D_u D_n, P=D^2 C. For legal positive q, D>0. These are the full cleared observations, not substitution into the rational observer at a pole.

Fiber A: q_A=-d-1, u=-1,n=-d-2. Then S_n(l)=0 for all l<d, because the tail contains the factor at i=d-1. S_u(0)=(d+1)!, S_n(d)=(-1)^d(2d+1)!/(d+1)!. Put B=(-1)^d(2d+1)!. Exactly v=(d+1)B, b=0, a=-v, J=2, L=-4d-6, endpoint zero. Thus Qn=0, Zn=L(d+3)(d+1)B. Consequently
    P(-d-1)=64(d+1)^3(d+3)^2(4d+6)^2 ((2d+1)!)^2 >0.
The sum reduction uses joint support of both branches and the endpoint, not independent marginals.

Fiber B: q_B=-d-1/2, u=-1/2,n=-d-1. Set B=S_u(0)S_n(d)=prod_{i=0}^{d-1}[(2i+5)/2]*(-d-1-i). Now S_n(l)=0 for l<=d-2, due to i=d-2 in the tail; S_n(d-1)/S_n(d)=-1/(2d); S_u(1)/S_u(0)=-1/5. The only nonzero a_k are k=0,1 and the only nonzero b_k is k=0. Hence v/B=d+1+1/5, b/B=-1/2. The weight (u-k)(u+k+2) equals -3/4 and -15/4 at k=0,1; a/B=-3(2d+3)/8. J=0, L=-4d-2, endpoint zero. Qn=0, Zn=L q_B a=(2d+1)^2 a. Therefore
    P(-d-1/2)= (9/4)(4d+1)(2d+1)^4(2d+3)^2 B^2 >0.
The formulas are exact in Q; no division by a vanishing rational denominator is performed.

## 2. Whole-composite and joint smoothness necessary constraints (unbounded d)

Suppose an integer legal q satisfies C(q,d)=0. Since P is integral and P(q)=0, P(X)=(X-q)T(X) with T integral. Substituting q_A gives the full integer divisibility
    u+1 | P(-d-1).
At q_B, if N=deg P=4d+9, then 2^N P(q_B)=-(2u+1)2^(N-1) T(q_B) and the latter factor is integer. Thus
    2u+1 | 2^N P(-d-1/2).
These retain every prime power of the composite coordinates, and no fixed-divisor normalization is assumed. The explicit fiber constants imply:
 * Every prime factor of u+1 is <=2d+3.
 * Every prime factor p of 2u+1 exceeding 2d+3 must divide 4d+1. Such p must equal 4d+1 (if prime). (The factors of B have odd-prime support <=2d+3.)
 * KG: every p>2d+2 dividing u must divide f(d)=64d^6-61d^5+13d^4+61d^3-29d^2+16, with v_p(u)<=v_p(f(d)).
The coordinates u,u+1,2u+1 are pairwise coprime by elementary subtraction, and all are retained in a single joint predicate. There is no independence assumption. In KD's bracket for d>=81, each coordinate is smaller than the square of its threshold for large primes, so the largest-prime-factor tests below are exactly equivalent to the displayed large-prime necessary conditions (not to root existence).

Also, for p>2d+3 dividing u+1, the cleared P is a p-unit by Fiber A and all denominator factors at q_A are p-units except one D_n factor 2(u+1). Hence v_p(C)=-2v_p(u+1). For p>2d+3 dividing 2u+1 with p not dividing 4d+1, P is a p-unit by Fiber B. The denominator has exactly the J factor 2u+1 and the D_n factor 2u+1 at i=d-2, with all other factors units. Thus v_p(C)=-4v_p(2u+1). These are sufficient exact nonzero witnesses; no claim of novelty for r=1 compared to JA. Both observations preserve P and the original denominator for future higher jets.

## 3. Executed exact computation
Local Python Fraction/integer code verified both displayed fiber identities for every d=3..200 (396 identities). Then local C++ exact sieve over all integer q in [ceil(4d^2/5),floor(4d^2/3)], d=3001..3100, computed the joint predicate. Largest prime factors are generated for all integers up to maximum 2u+1 by ascending prime multiples, overwriting with the largest. The sextic is evaluated by signed integer Horner modulo p (negative remainders are harmless for the zero test); all intermediate products fit signed 64-bit. No floating point and no independence assumption.

Output columns: d, initial, KG survivors, KG+u+1 survivors, all three survivors, u+1 alone survivors, 2u+1 alone survivors. Actual rows:
    3001 4803201 1691189 569325 143684 1691045 1299356
    3002 4806402 1691980 569755 143870 1692781 1300838
    3003 4809605 1694335 570486 144014 1693722 1301529
    3099 5122028 1802877 606914 153198 1802876 1386799
    3100 5125334 1803885 607480 153461 1804711 1388719
    total 496340491 174770270 58853464 14859030 174782052 134396352
Full 101-line local stdout SHA256 e323f2175d6517565521b3b9575c2ef12528bed0d5c8755b45c85769555d0bba (reproducible by code). KG count exactly matches its previously saved result. Additional exclusions relative to KG alone: 159911240, of which 115916806 from u+1 and 43994434 further from 2u+1. Total excluded by union 481481461; remaining 14859030. These are exact counts within the whole bracket, not new all-budget d closures. No independent mathematical review, no overlap count with KI small-prime sieve, and no claim of eliminating all smooth triples. The scan uses O(M log log M) sieve work and O(M) storage for M=max(2u+1), followed by O(number of budgets) integer checks.

Reproduction 1: Python code (executed local SHA256 8e60dfaa8ed1c8716f0ed5bb4993f50f6e1cbce993fc7278972b6d2f57518cb7).
```python
from fractions import Fraction as F
from math import factorial

def carrier(d,q):
 u=q+d;n=2*q+d
 def S(v):
  tail=[1]*(d+1)
  for k in range(d-1,-1,-1):tail[k]=tail[k+1]*(v+k+3)
  pre=1
  for k in range(d+1):tail[k]*=pre;pre*=v-k
  return tail
 U,N=S(u),S(n);v=b=a=0
 for k in range(d+1):
  l=d-k;A=(k+1)*(l+1)*U[k]*N[l];B=(k+1)*l*U[k]*N[l-1] if l else 0
  v+=A;b+=B;a+=(u-k)*(u+k+2)*(A+B)
 J=2*u*(2*u+1);L=4*n+2;W=L*a+u*U[d]*N[0]*q*(2*d+3)*(n+2);Q=J*L*b;Z=L*(q*a+J*(b+v));return 3*q*(4*q+3*d+1)**2*W*Q-32*(3*q+d+1)*Z**2
for d in range(3,201):
 q=-d-1; B=(-1)**d*factorial(2*d+1);L=-4*d-6; Z=L*(d+3)*(d+1)*B
 assert carrier(d,q)==64*(d+1)*Z*Z
 q=F(-2*d-1,2);B=F(1)
 for i in range(d):B*=F(2*i+5,2)*(-d-1-i)
 L=-4*d-2;a=-F(3*(2*d+3),8)*B;Z=L*q*a
 assert carrier(d,q)==16*(4*d+1)*Z*Z
print('396 exact fiber identities passed')
```
Reproduction 2: C++ (executed local SHA256 fb2012511d7404050e43bfccd7a4d3d5e30e2435224c2794092c9c5ea0644b1b). g++ -O3 -std=c++17 r284kj_scan.cpp -o r284kj_scan; ./r284kj_scan > r284kj_scan.txt
```cpp
#include <vector>
#include <iostream>
#include <cstdint>
#include <cassert>
using namespace std;
int main(){const int lo=3001,hi=3100,M=2*(4*hi*hi/3+hi)+1;vector<int> lp(M+1);for(int p=2;p<=M;p++)if(!lp[p])for(int i=p;i<=M;i+=p)lp[i]=p;
int64_t total=0,s0=0,s1=0,s2=0,t1=0,t2=0;
for(int d=lo;d<=hi;d++){int a=(4*d*d+4)/5,b=4*d*d/3;int64_t c0=0,c1=0,c2=0,z1=0,z2=0;
for(int q=a;q<=b;q++){int u=q+d,p=lp[u];bool ok0=p<=2*d+2;if(!ok0){int64_t f=64;for(int c:{-61,13,61,-29,0,16}) f=(f*d+c)%p;ok0=f==0;}
bool ok1=lp[u+1]<=2*d+3;int p2=lp[2*u+1];bool ok2=p2<=2*d+3||(4*d+1)%p2==0;
z1+=ok1;z2+=ok2;if(ok0){c0++;if(ok1){c1++;if(ok2)c2++;}}}
cout<<d<<' '<<b-a+1<<' '<<c0<<' '<<c1<<' '<<c2<<' '<<z1<<' '<<z2<<'\n';total+=b-a+1;s0+=c0;s1+=c1;s2+=c2;t1+=z1;t2+=z2;}
cout<<"total "<<total<<' '<<s0<<' '<<s1<<' '<<s2<<' '<<t1<<' '<<t2<<'\n';assert(total==496340491&&s0==174770270);}
```

## Next
Use the exact whole-composite divisibility constants after removing KG's known variable factors, or the local normalized observer KI, on the joint smooth survivors rather than on the entire budget grid. Seek additional low-height adjacent fiber constants and use KD's unique real root to localize actual integer candidates. Full non-equality d=3..3000 retained; unbounded integer equality remains open. This note does not claim a new formal Task, Result or Review.
