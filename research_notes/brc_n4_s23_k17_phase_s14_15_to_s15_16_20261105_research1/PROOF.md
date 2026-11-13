# BRC N=4, S23 auxiliary T/B phase: full integer Chernoff optimizer on [14/15,15/16]

**Date:** 2026-11-05. **Scientific input:** immutable inherited pin `43ec6098b1330ae86d0a7863be336c5d97f6ef34`; source model restated below. **Status:** AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED. This is an auxiliary binary hypothesis testing experiment, not a claim of the ten-label S23 minimax solution.

## Model (unchanged)

Put `a=11/21`, `b=10/21`. For each real `s in [14/15,15/16]`, the *complete* three-category observer T and its deterministic *coarsening* B have distributions

```
P_T = (a*s, 1-s, b*s),        Q_T = (b*s, 1-s, a*s)
P_B = (a*s, 1-a*s),           Q_B = (b*s, 1-b*s).
```

B maps T's first category to 1 and its other two categories to 0. This source/projection map is part of the observation semantics; the separate sample costs are `c_T=2-s` and `c_B=1`.

Write

```
f_T(t,s) = -ln[1-s+s*(a^t*b^(1-t)+b^t*a^(1-t))]
f_B(t,s) = -ln[(a*s)^t*(b*s)^(1-t)+(1-a*s)^t*(1-b*s)^(1-t)]
F(m,n;s) = max_(0<=t<=1) {m*f_T(t,s)+n*f_B(t,s)}
C_T=F(1,0;s), C_B=F(0,1;s), H=f_B(1/2,s).
```

The Chernoff tilt `t` is common to all T and B samples, **not optimized separately** in a mixed design. Optimize `F(m,n;s)` over nonnegative integer `m,n` with `(2-s)m+n<=17`. Since both observers carry positive information for `0<s<=1`, each fixed `m` is best with `n=17-2m+floor(m*s)` whenever nonnegative.

## Exact phase theorem

There is a unique `alpha` in the **strict rational interval**

```
93343/100000 < alpha < 93344/100000,
```

such that the *entire* real-parameter integer argmax is:

| Parameter | All optimal integer `(m,n)` |
| --- | --- |
| `14/15 <= s < alpha` | `(15,1)` only |
| `s = alpha` | exactly `(15,1)` and `(0,17)` |
| `alpha < s < 15/16` | `(0,17)` only |
| `s = 15/16` | `(16,0)` only |

For numerical orientation only, `alpha ≈ 0.93343368` (the rational enclosure above is the proved statement).

## Complete integer feasible hull (not a grid argument)

Every possible cost breakpoint with `m in {1,...,17}` is of the form `k/m`. Exact `Fraction` enumeration of all such rationals in this closed interval returns *only* `[14/15,15/16]`. Thus the upper-boundary integer points `(m,n_m)` remain fixed throughout the half-open chamber `[14/15,15/16)`. Exact monotone-chain arithmetic gives its upper convex hull as

```
(0,17) ---- (15,1).
```

At the new feasible-cost boundary `s=15/16`, `(16,0)` becomes feasible and the upper hull becomes

```
(0,17) ---- (16,0).
```

Both edges are primitive: `gcd(15,16)=gcd(16,17)=1`. `F` is convex in `(m,n)` because it is a supremum of affine functions of the sample counts. Since interior or lower integer points are dominated by the upper hull, and the hull edges have no interior lattice points, **every global integer maximizer must be one of the indicated hull vertices**, with no third optimizer at a tie. Strict monotonicity in counts justifies dropping all feasible points below the maximal admissible `n_m`.

## Certified Chernoff bounds and continuum uniqueness

Let `u=s*sqrt(a*b)`, `L=ln(a/b)>0`, `J=ln((1-b*s)/(1-a*s))>0`, and `rho=J/(L+J)`. Direct symmetric minimization for T and Bernoulli Chernoff's equal-KL criterion give

```
C_T = -ln(1-s+2*u),
H   = -ln(u+sqrt((1-a*s)*(1-b*s))),
C_B = rho*ln(rho/(a*s)) + (1-rho)*ln((1-rho)/(1-a*s)).
```

For all `s`, the **common-tilt** mixed exponent obeys

```
15*C_T + H <= F(15,1;s) <= 15*C_T + C_B.              (1)
```

For fixed `t`, T's overlap is positive and affine in `s`, and B's overlap is positive and concave in `s` (one linear term plus the weighted geometric mean of two positive affine terms). The composition with decreasing convex `-ln` is convex. Consequently `f_T(t,s)`, `f_B(t,s)`, their nonnegative linear combinations, `F(m,n;s)`, `C_T(s)` and `C_B(s)` are convex in `s`.

Set `G(s)=F(15,1;s)-17*C_B(s)`. Partition `[14/15,15/16]` into 16 *closed rational cells* `[x_i,y_i]`; take `delta=1/10000`. For any interior derivative point `z` in a cell, convexity and (1) imply

```
F'(15,1;z) <= [15*C_T(y+delta)+C_B(y+delta)-15*C_T(y)-H(y)]/delta,
C_B'(z)    >= [C_B(x)-C_B(x-delta)]/delta.
```

The attached checker establishes the following **strict inequality for each of all 16 cells** using *outward rational intervals*:

```
17*[C_B(x)-C_B(x-delta)] >
  15*[C_T(y+delta)-C_T(y)] + C_B(y+delta)-H(y).          (2)
```

Thus `G` is strictly decreasing at every real parameter, not only at sampled rationals. Convex functions are differentiable almost everywhere, so the strict one-sided derivative bound applies on the full interval and implies strict decrease by continuity/absolute continuity on compact interior subintervals.

The checker separately establishes the following fully rational strict bounds:

```
15*C_T(14/15) + H(14/15) > 17*C_B(14/15),
15*C_T(93343/100000) + H(93343/100000) > 17*C_B(93343/100000),
17*C_B(93344/100000) > 15*C_T(93344/100000)+C_B(93344/100000),
16*C_T(15/16) > 17*C_B(15/16),
C_T(15/16) > C_B(15/16).                                (3)
```

Equations (1)-(3), continuity, strict decrease and the primitive integer hull prove the phase theorem. At `15/16`, `C_T>C_B` also shows `(16,0)` beats the old `(15,1)` design directly: `F(15,1) <= 15*C_T+C_B < 16*C_T`.

## Source-compatible finite-sample risk lemma

For *the specific two-hypothesis experiments just defined*, let `R(E)` denote optimal 0-1 decision risk at any fixed binary prior under the product experiment `E`. Since T deterministically coarsens to B and independent samples preserve this garbling order,

```
R(T^(m+n)) <= R(T^m B^n) <= R(T^m),       m,n >= 0.       (4)
```

Proof: from `m+n` complete T observations, apply the deterministic T-to-B map to the last `n` samples, reproducing the mixed experiment exactly. From the mixed experiment, discard all B samples to obtain `T^m`. Every randomized decision rule for a coarser observation can be composed with either Markov kernel to give the same risk on its finer predecessor; taking infima proves (4). This lemma supplies a concrete encoder/decoder bridge **within the auxiliary observer model**. A future link to the ten-label S23 mother problem must specify its own hypothesis distributions, Markov kernels and legal policies before transporting (4).

## Repair to the previous phase's checker (research continuity)

The previous `[13/14,14/15]` `VERIFY.py` at immutable commit `3143148c54840d4db5c6eb025ac9521e5ff8eb77` has a label `RIGHT_15T1B_GT_17B` whose tested expression is `14*C_T+2*H-17*C_B`, rather than its literal `15*C_T+H-17*C_B` claim. This turn **independently checks the correctly typed latter expression with a strictly positive rational lower bound** at `s=14/15` (`PREVIOUS_RIGHT_CORRECTED_15T1B_GT_17B` in VERIFY). This repairs the proof-to-code correspondence of that boundary comparison; prior published bytes/history stay unchanged. No independent reviewer acceptance is claimed.

## Exact computation, certificate meaning, and scope

Execute `python VERIFY.py` (Python standard library: `Fraction`, `math.isqrt`, `math.gcd`, `functools.lru_cache`). The included `RUN_EVIDENCE.txt` is the actual stdout from this exact local program, not a copied expectation. It yields 16 continuum strict-derivative certificates, 5 sign/data-processing certificates, and 1 previous-boundary correction certificate, **22 strict rational assertions total**, alongside exact rational breakpoint and integer hull checks.

All square roots are enclosed by `1e-36`-mesh rational lower/upper endpoints checked by integer squares. Natural logarithms are bounded by 34 terms of the exact atanh series, with tail `<= 2*|v|^69/[69*(1-v^2)]` for `|v|<1/3`; rational intervals propagate all dependencies with outward endpoint arithmetic. Inferences in this note concern **every real `s` on the declared interval**; the retained source/observer distinction separates this result from original S23 minimax admission, and the BRC-native Heartbeat operation restrictions are not invoked by this auxiliary ordinary probability calculation.

**Next:** classify `[15/16,16/17]` from newly available pure 16T, but prioritize a documented, provenance-preserving probability map from the lawful ten-label S23 encoder/decoder mother problem to a specific two-hypothesis auxiliary experiment to determine whether (4) is usable there.
