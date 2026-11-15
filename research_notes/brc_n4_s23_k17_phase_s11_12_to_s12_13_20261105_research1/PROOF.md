# Exact BRC S23 auxiliary Chernoff phase: K=17, 11/12 ≤ s ≤ 12/13

Date 2026-11-05 · AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific source pin: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Previous author proof frontier: `fc7d8d315492b6e4e9d5c418f24c8ca5b5d47e31` (10/11 ≤ s ≤ 11/12).

## Exact model

Write a=11/21, b=10/21 and K=17. Full three-label experiment: P_T=(as,1-s,bs), Q_T=(bs,1-s,as). Projected Bernoulli experiment: P_B=(as,1-as), Q_B=(bs,1-bs). A common Chernoff tilt t∈[0,1] is shared by both observation types:

```
f_T(t,s)=-log(1-s+s*(a^t*b^(1-t)+b^t*a^(1-t)))
f_B(t,s)=-log((as)^t*(bs)^(1-t)+(1-as)^t*(1-bs)^(1-t))
F(m,n;s)=max_{0≤t≤1} (m*f_T(t,s)+n*f_B(t,s))
C_T(s)=F(1,0;s), C_B(s)=F(0,1;s).
```

Feasible nonnegative integer counts m,n satisfy (2-s)m+n≤17. The common tilt means F(m,n;s) must be optimized jointly.

## Full interval theorem

There is exactly one α with **91678/100000 < α < 91679/100000**. The *complete* global optimal integer count sets are:

* 11/12≤s<α: uniquely **(m,n)=(12,4)**;
* s=α: exactly **(12,4)** and **(0,17)**;
* α<s<12/13: uniquely **(0,17)**;
* s=12/13: uniquely **(13,3)**.

## Exhaustive lattice geometry

For each fixed m, the optimal B count is n_m(s)=17-2m+floor(ms), when this is nonnegative, because B has strictly positive Chernoff information. Exhausting rational k/m (1≤m≤17, 0≤k≤m) in [11/12,12/13] gives **only its two endpoints** as cost breakpoints. The upper lattice hull is therefore (0,17),(12,4),(15,0) everywhere on [11/12,12/13), and (0,17),(13,3),(15,0) at 12/13. The verifier checks the finite arithmetic at all breakpoints and representative interiors.

F is a supremum of affine functions in (m,n), so it is convex and coordinatewise nondecreasing. Every feasible point is bounded in value by the hull vertices. Upper edge step vectors (12,-13), (3,-4), (13,-14), (2,-3) are primitive (coordinate gcd=1), so no extra integer point lies in a hull edge. Strict vertex comparisons and the stated two-vertex crossing therefore classify every integer optimizer, including ties.

## Analytical bounds valid on the real continuum

Let H(s)=f_B(1/2,s). T symmetry and the Bernoulli Chernoff tilt yield

```
C_T(s)=-log(1-s+2*s*sqrt(ab))
H(s)=-log(s*sqrt(ab)+sqrt((1-as)(1-bs)))
L=log(a/b), J=log((1-bs)/(1-as)), rho=J/(L+J)
C_B(s)=D_Bernoulli(rho || as).
```

For all m,n≥0: m*C_T+n*H ≤ F(m,n;s) ≤ m*C_T+n*C_B. For fixed t the T overlap is positive affine in s, and the B overlap is concave in s (affine term plus positive weighted geometric mean of affine factors). Thus -log of each overlap is convex, hence F,C_T,C_B are convex in s.

Set G(s)=F(12,4;s)-17*C_B(s), D(s)=17*C_B(s)-15*C_T(s). Partition [11/12,12/13] into 16 rational cells [x,y], δ=1/10000. Standard secant inequalities for convex functions show, almost everywhere z∈[x,y]:

```
F'(12,4;z) ≤ [12*C_T(y+δ)+4*C_B(y+δ)-12*C_T(y)-4*H(y)]/δ
C_B'(z) ≥ [C_B(x)-C_B(x-δ)]/δ
C_T'(z) ≤ [C_T(y+δ)-C_T(y)]/δ.
```

The executed exact-rational verifier checks both strict inequalities on **each** of the 16 cells:

```
17*(C_B(x)-C_B(x-δ)) > 12*(C_T(y+δ)-C_T(y))+4*(C_B(y+δ)-H(y))
17*(C_B(x)-C_B(x-δ)) > 15*(C_T(y+δ)-C_T(y)).
```

Therefore G is strictly decreasing and D strictly increasing across the entire real interval. Six additional rigorous signs are established:
(1) 12*C_T(11/12)+4*H(11/12)>17*C_B(11/12);
(2) 17*C_B(11/12)>15*C_T(11/12);
(3) 12*C_T(91678/100000)+4*H(91678/100000)>17*C_B(91678/100000);
(4) 17*C_B(91679/100000)>12*C_T(91679/100000)+4*C_B(91679/100000);
(5) 13*C_T(12/13)+3*H(12/13)>17*C_B(12/13);
(6) 13*C_T(12/13)+3*H(12/13)>15*C_T(12/13).

Signs 1,3,4 and strict decrease give one and only one zero α of G. Sign 2 and strictly increasing D eliminate 15T for all s<12/13. Signs 5,6 select the new 13T+3B endpoint configuration. Primitive hull edges exclude all hidden integer ties.

## Execution, provenance, open question

Run `python3 VERIFY.py`. It uses only `Fraction`, `isqrt`, exact outward sqrt brackets at scale 10^36 and 34 atanh-log terms with a strict tail bound 2|v|^69/[69(1-v²)] valid for |v|<1/3. There are 32 exact continuum secant certificates and 6 exact signs: 38 rigorous rational assertions. See `RUN_EVIDENCE.txt`. The remote verifier is the preceding phase's certified interval algorithm with the new parameter range, hull, endpoints and counts; the independently executed local author version has the same equations and assertions but may differ textually.

B forgets source-label distinctions: strict weighted Hölder for 0<s,t<1 yields f_B(t,s)<f_T(t,s). The S23 auxiliary finite-label information model is a typed readout, not a native P000 X6 spatial update or the original ten-label S23 minimax risk. The original mother objective's reported [1/2,2/3] bracket remains an open independent frontier. Continue the next auxiliary phase at 12/13≤s≤13/14, and separately derive a provenance-preserving risk bridge on an explicit lawful policy family.
