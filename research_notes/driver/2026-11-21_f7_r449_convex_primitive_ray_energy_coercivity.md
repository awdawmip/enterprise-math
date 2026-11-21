# CBRC F7 Driver r449 — Convex primitive-ray energy coercivity

Date: 2026-11-21 (+08:00). Mathematical consequence of the original F7 old-axis identity and r448's disjoint primitive-pair construction. The original frozen F7 Result and scalar assumptions belong to researcher `EM-CBRCF7-83A1D4` (`RR-AA38973D56330E59D315`). This quantitative corollary is derived by the continuing Driver line `EM-DVR-DEBB5E`. It is NOT a Native Review, independent acceptance of that Result, or Task completion.

## Exact hypotheses and notation

Let `q: Z^2 -> [0,infinity)` satisfy the original F7 admissibility assumptions: `q(0,0)=0`, `q(-x,y)=q(x,y)`, `q(s,0)=1` for nonzero `s`, `q(x,y)>=1/2` for nonzero `(x,y)`, and `q(2,1)=q(-1,-1)=1/2`. Let `A=I+uv^T` with `u=(1,1,-1,-1)`, `v=(1,-2,-1,2)`, and set
```
D_q(a,b,c,d)=q((Az)_1,(Az)_2)+q((Az)_3,(Az)_4)-q(a,b)-q(c,d),
E(q)=sup_{z in Z^4}|D_q(z)|.
```
Fix `0 <= epsilon < 1` and suppose `E(q)<=epsilon`. Write `delta(x,y)=q(x,y)-1/2>=0` on nonzero points. For integer `L>=2`, let
```
Omega_L={(x,y) in Z^2 : x>0, y!=0, gcd(x,abs(y))=1,
          x<=3L-2, abs(y)<=L-1}
N(L)=sum_{c=2}^L phi(c).
```

## Theorem: convex energy lower bound, with a pinned-mark improvement

For EVERY convex nondecreasing function `Psi:[0,infinity)->[0,infinity)` with `Psi(0)=0`,
```
sum_{(x,y) in Omega_L} Psi(delta(x,y))
 >= Psi(1-epsilon) + 2*(N(L)-1)*Psi((1-epsilon)/2).       (R449.1)
```
In particular, for every real `p>=1`,
```
sum_{(x,y) in Omega_L} (q(x,y)-1/2)^p
 >= (1-epsilon)^p * [1 + (N(L)-1)*2^(1-p)].           (R449.2)
```
For `p=2`, the right-hand side is `(N(L)+1)*(1-epsilon)^2/2`. At a hypothetical `E(q)=1/2`, it is `(N(L)+1)/8`. The leading asymptotic is
```
sum_{Omega_L} delta(x,y)^p
 >= [2^(1-p)*3/pi^2*(1-epsilon)^p] L^2 + O(L log L),
```
where this asymptotic describes the explicit LOWER-BOUND expression; it is not an asserted asymptotic equality for the actual sum.

Consequently, for `E(q)<1` and every `p>=1`, the primitive positive-first-coordinate deviations `delta(x,y)` do not belong to `ell^p`; any admissible model requiring a uniformly bounded total such p-energy over all primitive nonaxis inputs has `E(q)>=1`. More generally the same conclusion applies to an Orlicz-type total energy `sum Psi(delta)` whenever `Psi((1-epsilon)/2)>0`.

## Proof

For every `2<=c<=L` and `1<=t<c` with `gcd(c,t)=1`, r448 supplies two distinct, pairwise-disjoint primitive arguments
```
P(c,t)=(c+2t,t),    R(c,t)=(c-t,-t).
```
Both lie in `Omega_L`. On the old-axis input `z=(c+t,0,c,0)`, both old scalar values equal 1, while the transformed values are `q(P)` and `q(R)`. Thus
```
q(P)+q(R)>=2-epsilon,
delta(P)+delta(R)>=1-epsilon.                         (R449.3)
```
For each pair, monotonicity and Jensen's inequality give
```
Psi(delta(P))+Psi(delta(R))
 >=2*Psi((delta(P)+delta(R))/2)
 >=2*Psi((1-epsilon)/2).
```
The pair `(c,t)=(2,1)` is stronger. It equals `P=(4,1)`, `R=(1,-1)`. The original marked equality at `(-1,-1)`, combined with `q(-x,y)=q(x,y)`, yields `q(R)=1/2`, hence `delta(R)=0` and `delta(P)>=1-epsilon`. Its two-point energy is therefore at least `Psi(1-epsilon)`. All other `N(L)-1` pairs remain distinct by r448. Summing their bounds and using nonnegative energy on any remaining `Omega_L` points gives (R449.1). Substitute `Psi(t)=t^p` for (R449.2). The standard totient summatory estimate `N(L)=(3/pi^2)L^2+O(L log L)` gives the stated explicit lower-bound growth. QED.

## Evidence scope and utility

The exact combinatorial pair-disjointness used here was proved symbolically in r448; an independent integer enumeration of the pair geometry for L=2,3,10,50 has `N=1,3,31,773` and union cardinalities `2,6,62,1546`. Equation R449.1 is symbolic for all L and requires no numerical solver or unverified finite-to-infinite leap.

This strengthens finite-exception support obstruction into a quantitative exclusion of finite convex regularization energy. It is useful when assessing infinite-ray minimax candidates: a search or interpolation method that penalizes total primitive deviation with a finite summable p-energy cannot realize global defect strictly below 1. It does not tighten the unrestricted F7 optimum `1/2<=E_infinity<=4/7`, and it does not establish independence or native admission.

Scientific source: [r448 at its pinned commit](https://github.com/awdawmip/enterprise-math/blob/b4b3141368975f7598a8c98acbf49b435161c4cf/research_notes/driver/2026-11-21_f7_r448_primitive_ray_quadratic_boundary_pressure.md). Original F7 author/Result claims remain unmodified. Native first-review audit budget issue and original frozen SHA256 discrepancies are separate: https://github.com/awdawmip/enterprise-math/issues/2874.
