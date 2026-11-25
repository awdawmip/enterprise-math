# R284HM — Sub-square-root band via exact Pólya port transport

2026-11-25. Author proof, NOT_REVIEWED. Auxiliary binary-tag safe-word total-count observer only, not native physical attribution. Own registration recovery r1-20261125-1100-own-recovery returned original registration r1-20261124-0256-r284gd-session-v1 SUCCEEDED, session MCP-8cd6c4fa26b9459d923ff73ba0082220 open, role RESEARCHER; EM-DIRECT-0C386E / RA-B82240E8488EF5A1DA5186C4. No shared CLAIM or run. Current LEASED inventory request r1-20261125-1100-owner-read was RUNNING at prepublication read; no claim inference. Account entry blobs read at main@29a72ffa196c6d1ebe150e859dd2054ed6577656; project source main@693bcd92357fc0601b55eb3370deeb493b26d26a; P000 V5, ACTIVE worldview, joint observer and residual fidelity contracts read. Frozen scientific dependency: b2e9363fef39a8f536548ad8eaca5a204b0e03e7:research_notes/portable_direct/R284HL_CRITICAL_SQRT_BAND_CORRELATED_PORT_TRANSPORT_20261125.md, exact moment identities and compact-band theorem, conditional on original auxiliary safe-word counting model. The original joint distribution remains available.

## New theorem

Put d=u-q and write K_u(d)=K(q,u). Define
    f(d)=2d(2d²+6d+7)/[(d+1)(d+2)(2d+3)].
Uniformly as u tends to infinity, for 4<=d<=sqrt(u),
    log[K_u(d)/K_u(d-1)] = log[f(d)/f(d-1)] + O(1/u),
    log[K_(u+1)(d+1)/K_u(d)] = log[f(d+1)/f(d)] + O(1/u).
The constants are absolute; no explicit effective threshold claimed. In particular on every integer sequence d->infinity, d²/u->0, both log gaps multiplied by d² tend to 3/2. Both strict directions hold eventually. For each fixed positive d, u K_u(d) tends to (16/3) f(d), and the same strict signs follow (q-direction requires d>=2). Consequently, combining with frozen HL's compact positive square-root band theorem, for every fixed B>0 there is U_B such that for every u>=U_B and integer 1<=d<=B sqrt(u), the u-direction is strictly positive and the q-direction is strictly negative whenever d>=2. This closes the sub-square-root asymptotic gap including arbitrary intermediate growth. The remaining unbounded gap lies at d/sqrt(u)->infinity below HK's moving threshold; finite effective closure remains open.

## Proof

Frozen counts (HL):
M_n(k)=(k+1)/(n+1) binom(2n+2,n-k);
C_(n,m)(g)=sum_k M_n(k)M_m(g-k) (zero for g<0).
n=u, m=2u-d, Q=C_(n,m)(d-1);
S=C_(n,m)(d)+Q+q[C_(n-1,m)(d)+C_(n-1,m)(d-1)];
P=sum_(j=0)^3 binom(3,j) C_(n-1,m-1)(d+1-j);
K=(P Q/S²) W, W=(3u+q+1)²/(u+2q+1).

### 1. Exact joint transport and a second-difference bound

Write M_n(k)/M_n(0)=(k+1) w_n(k), with w_n(0)=1 and w_n(k+1)/w_n(k)=rho_n(k)=(n-k)/(n+k+3). For g<=2sqrt(u)+4, n,m>=u/2 and sufficiently large u, every relevant weight is positive. Set c_g=binom(g+3,3) and A_g(n,m)=C_(n,m)(g)/(M_n(0) M_m(0)c_g). The convolution of (k+1)(g-k+1) gives c_g exactly. Introduce a probability on k=0,...,g with weight (k+1)(g-k+1)/c_g. It is exactly the number of first-color draws in a Pólya urn with initial counts (2,2): probability of an ordered word with k first-color draws is (2)_k(2)_(g-k)/(4)_g, where (a)_k denotes the rising factorial. Multiplying by binom(g,k) gives the stated mass. The step k -> k+delta has delta=1 probability p_g(k)=(k+2)/(g+4).

Thus A_g=E[w_n(k)w_m(g-k)]. Retain the joint allocation under tilt by this product, denoting its probability by mu_g. Define b_n(k)=1-rho_n(k)=(2k+3)/(n+k+3) and
    a_g(k)=p_g(k)b_n(k)+(1-p_g(k))b_m(g-k).
Then r_g=A_(g+1)/A_g=1-E_mu_g a_g exactly. Uniformly 0<=a_g<=O((g+1)/u), so r_g=1+O((g+1)/u), bounded away from zero for large u.

Consider the joint distribution nu of a prefix under mu_g followed by one ordinary urn step. The tilted law mu_(g+1) is its marginal after reweighting by rho/r_g, where rho is rho_n(k) if delta=1, otherwise rho_m(g-k). This is a positive reweighting, not signed mass cancellation. Uniformly |rho/r_g-1|=O((g+1)/u). The function a_(g+1) is bounded by O((g+2)/u), so its expectation under the new tilt and under nu differ by O((g+2)^2/u²). On each allowed step,
    |p_(g+1)(k+delta)-p_g(k)|<=1/(g+5),
    |b_n(k+1)-b_n(k)|=(2n+3)/[(n+k+3)(n+k+4)]=O(1/u)
(and likewise for m).
Consequently |a_(g+1)(k+delta)-a_g(k)|=O(1/u): the change in p is multiplied by a difference of b's of size O((g+2)/u). Taking expectations proves
    |r_(g+1)-r_g|=O(1/u+(g+2)^2/u²)=O(1/u)
on the stated range. Since r_g is bounded away from zero, the same holds for log r. This pays the variation of the relative port residual directly instead of paying its full size O(g/u) twice.

For a unit shift of n or m in this range, the logarithm of each w changes uniformly by O((g+1)^2/u²). Indeed each factor has logarithmic derivative in its real size parameter z equal to (2i+3)/[(z-i)(z+i+3)] = O((i+1)/u²), and sum for 0<=i<k gives the bound. Positive weighted averaging transfers the same log-ratio bound to A_g. These unit-size shifts cost O(1/u) in the square-root range.

### 2. Extract the exact combinatorial factor and correlate neighboring errors

For d>=3 and g=d+j, j in {-2,-1,0,1}, write T_j=A_(d+j)/A_d. By the preceding r estimate T_j=1+O((d+1)/u). When d is incremented or decremented by one with n,m unchanged, the log T_j changes by O(1/u), because T_j is a product of at most two consecutive r's or their reciprocals. For a simultaneous unit shift of n,m the preceding log-weight bound independently pays O(1/u). Therefore T_j itself changes by O(1/u) on both actual neighboring parameter moves (q+1: d-1, n unchanged, m+1; u+1 at fixed q: d+1,n+1,m+1).

In the exact P,S formulas replace normalized size-shifted A_g by unshifted ones with multiplicative 1+O(1/u) from section 1. The unnormalized zero-moment shift M_(n-1)(0)/M_n(0)=(n+2)/(4n+2)=1/4+O(1/u), similarly for m. The two q-independent S terms cost only O(1/u) relative to its q-dependent terms, since q=u-d is comparable to u and the terms have comparable positive normalized sizes. Direct cancellation now gives
    K_u(d)= (W/q²) f(d) H(d;n,m) [1+O(1/u)],
where
    H=T_-1 * (sum_(j=0)^3 binom(3,j)c_(d+1-j)T_(1-j) / sum_(j=0)^3 binom(3,j)c_(d+1-j))
        / ((c_d + c_(d-1)T_-1)/(c_d+c_(d-1)))²,
and
    f(d)=c_(d-1) sum_(j=0)^3 binom(3,j)c_(d+1-j)/(c_d+c_(d-1))².
Expanding the elementary cubic c_g yields the formula above. This cancellation is confined to K's total-count observer.

Each normalized coefficient in the weighted means defining H varies by O(1/d) on adjacent d>=3: the positive c_(d+j) have relative increments O(1/d), and dividing by their finite positive weighted sum preserves that bound. As the normalized coefficients sum to 1, their change contributes only O(1/d)*O((d+1)/u)=O(1/u) when multiplied by T_j-1. The change of T_j contributes O(1/u) as established above. Every mean is bounded away from zero, hence adjacent log H differences are O(1/u). The two leftover multiplicative errors can be paid independently at O(1/u); the elementary log(W/q²) changes by O(1/u) along both moves, since q comparable to u and all linear factors in W comparable to u. This proves both uniform adjacent expansions.

### 3. Exact positive leading gaps and scale closure

For d>=1,
    f(d+1)-f(d)=6(2d³+8d²+15d+15)/[(d+1)(d+2)(d+3)(2d+3)(2d+5)]>0.
Also f(d)=2-3/d+O(d^-2) and the displayed exact difference is 3/d²+O(d^-3). Thus d² log[f(d+1)/f(d)] and d² log[f(d)/f(d-1)] both tend to 3/2. Multiplying our paid errors by d² shows they vanish when d²/u->0.

For fixed d>=1 the finite normalized weights tend to 1 and q/u->1, W/u->16/3. The same exact cancellation gives u K_u(d)->(16/3) f(d), including d=1 by c_-1=0. Thus fixed d comparisons are strict eventually, with q-direction d>=2. To establish the combined uniform theorem for a fixed B, suppose arbitrarily large u admit a wrong sign in the band. Take a subsequence with d/sqrt(u) converging in [0,B]. Positive limit is covered by frozen HL; zero limit with unbounded d is covered by our paid-gap theorem; bounded d has a constant subsequence covered by the fixed-d result. All possibilities contradict a wrong sign. This is a uniform existence theorem without numerical onset.

## Executed evidence

Python 3 exact arbitrary integers and fractions; all 66 sign comparisons exact. Displayed scaled quantities converted to float only after rational arithmetic. Sampling includes fixed, quarter-power, cube-root and square-root fractions, not exhaustive. Actual run (33 base pairs, 99 K computations):
```python
from math import comb,isqrt
from fractions import Fraction as F
from functools import lru_cache
@lru_cache(None)
def m0(n): return comb(2*n+2,n)//(n+1)
def moments(n,g):
 a=[m0(n)]
 for k in range(g):
  v,r=divmod(a[-1]*(k+2)*(n-k),(k+1)*(n+k+3)) if k<n else (0,0)
  assert r==0
  a.append(v)
 return a
def K(u,d):
 q=u-d; m=u+q; g=d+1
 A,a,B,b=(moments(n,g) for n in (u,u-1,m,m-1))
 def C(a,b,g):return sum(a[k]*b[g-k] for k in range(g+1)) if g>=0 else 0
 Q=C(A,B,d-1); S=Q+C(A,B,d)+q*(C(a,B,d)+C(a,B,d-1)); P=sum(comb(3,j)*C(a,b,d+1-j) for j in range(4))
 return F(P*Q*(3*u+q+1)**2,S*S*(u+2*q+1))
def f(d):return F(2*d*(2*d*d+6*d+7),(d+1)*(d+2)*(2*d+3))
rows=[]
for u in [256,1024,4096,16384,32768]:
 for d in sorted(set([2,3,5,isqrt(isqrt(u)),int(u**(1/3)),isqrt(u)//4,isqrt(u)//2])):
  k,kq,ku=K(u,d),K(u,d-1),K(u+1,d+1)
  assert k>kq and ku>k
  rq=k/kq;ru=ku/k; fq=f(d)/f(d-1);fu=f(d+1)/f(d)
  rows.append((u,d,float(d*d*(rq-1)),float(d*d*(ru-1)),float(u*(rq/fq-1)),float(u*(ru/fu-1))))
print('pairs',len(rows),'exact_K',3*len(rows),'comparisons',2*len(rows),'max_abs_relative_error_scaled',max(abs(x) for row in rows for x in row[-2:]))
for row in rows:print('%d %d %.9f %.9f %.9f %.9f'%row)
```
Actual summary: pairs 33 exact_K 99 comparisons 66 max_abs_relative_error_scaled 2.6762291168815233. Selected actual rows (u,d,d²*qgap,d²*ugap,u*relative-q-error,u*relative-u-error):
```
256 6 1.502165752 1.077275002 2.654848147 1.620916190
1024 10 1.482267549 1.184476053 2.634885643 1.615807916
4096 15 1.440483863 1.236992961 2.623194955 1.615118038
16384 25 1.467332611 1.329979132 2.618831453 1.615141409
32768 31 1.467273466 1.355199982 2.617735408 1.615390452
32768 90 2.105408617 1.824892785 2.611549711 1.604310983
```
No counterexample in this finite scope. The numerical maximum is not an analytic error constant. The exact cubic identity and difference were also checked symbolically by SymPy; the proof is by direct algebra and the transport bounds above.

## Next

Retain the tilted joint allocation law; seek a sharper curvature/transport bound when d/sqrt(u)->infinity but d<16sqrt(u log u), where the simple O(d²/u²) reweighting bound no longer pays the full adjacent separation. Consider concentration of the tilted allocation and correlated covariance instead of uniform range. Derive effective constants and close finite complement only after the remaining asymptotic bridge. Independent review and strict Activity observation audit pending.
