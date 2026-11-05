# Exact phase theorem: S23 N=4, K=17, 4/5 <= s <= 9/11

**Date:** 2026-11-05. **Status:** AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / INDEPENDENT_REVIEW_PENDING / NOT_ADMITTED. **Frozen science pin:** `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Previous verified author frontier: PR #1765 `053477b8808763d9fcc35059096de66c7c2b1559`, phase [3/4,4/5].

## Original mathematical model

Put a=11/21 and b=10/21. For real 0<s<1, full-source T samples have three-label distributions (as,1-s,bs) and (bs,1-s,as), while projected B samples have Bernoulli distributions (as,1-as) and (bs,1-bs). For 0<=t<=1 define

```text
fT(t,s) = -log(1-s+s*(a^t*b^(1-t)+b^t*a^(1-t)))
fB(t,s) = -log((as)^t*(bs)^(1-t)+(1-as)^t*(1-bs)^(1-t))
F(m,n;s) = max_{0<=t<=1} [m*fT(t,s)+n*fB(t,s)].
CT(s)=F(1,0;s), CB(s)=F(0,1;s), H(s)=fB(1/2,s).
```

The design consists of nonnegative **integer** counts (m,n), budget (2-s)m+n<=17. A *single shared tilt* t is optimized for the joint design. B is a typed projection; it has not been identified with the full-source T observation. All logarithms are natural; information values are dimensionless.

## Theorem (real continuum, exact boundary)

There is exactly one real `alpha` in the **strict rational interval (4001/5000,8003/10000)=(0.8002,0.8003)** such that F(10,5;alpha)=17 CB(alpha). Throughout **[4/5,9/11)**, (10,5) is the unique global optimal feasible count pair for s<alpha, (0,17) is the unique global optimal feasible pair for alpha<s<9/11, and at s=alpha precisely these two pairs tie for global optimum. At **s=9/11**, the unique global optimal pair becomes **(11,4)**. The internal rational feasibility threshold s=13/16 changes the feasible integer set, but does not change the upper convex hull, nor the optimum.

### 1. Complete rational integer hulls

At fixed integer m, F is strictly increasing with n since fB(t,s)>0 for s in this domain. Thus the top feasible count is n_m(s)=17-2m+floor(ms), for each m=0,...,16 with nonnegative n_m. The only rational thresholds k/m in [4/5,9/11] with m<=16 are **4/5,13/16,9/11**. Exhaustive Fraction enumeration proves that on both [4/5,13/16) and [13/16,9/11) the upper convex hull vertices of these integer points are **(0,17),(10,5),(14,0)**, including the left endpoints. At s=9/11 the vertices are **(0,17),(11,4),(14,0)**. These statements are exact finite combinatorial identities checked by VERIFY.py, not floating point samples.

For each s, F is the supremum of affine functions of (m,n), hence convex in these counts; the maximum over the feasible integer points lies at a vertex of this upper convex hull. Strict positivity of fB eliminates designs with fewer B samples at fixed m.

### 2. Ruling out 14T on the open cell

Define D(s)=17 CB(s)-14 CT(s). The strict certificate proves D(s)>0 for every real s in [4/5,9/11], so vertex (14,0) is worse than (0,17). Divide the interval into four equal rational pieces [x,y]. Both CT and CB are convex in s. For delta=1/10000, exact outward-rational interval arithmetic verifies at each x both

```text
D(x)>0,
17*(CB(x)-CB(x-delta))/delta
  -14*(CT(y+delta)-CT(y))/delta >0.
```

Convexity bounds the derivative of D below by the second displayed expression on every piece, and therefore D remains positive over the whole real interval. Eight strict rational certificates cover this argument.

### 3. Unique continuous information crossing

Define G(s)=F(10,5;s)-17 CB(s). For fixed t, fT and fB are convex in s; the Bernoulli Chernoff coefficient is concave in s by weighted-geometric-mean concavity, and -log preserves the asserted convexity. Their pointwise max F is convex. For each of twelve equal rational pieces [x,y] of [4/5,9/11], set delta=1/10000 and

```text
L = (CB(x)-CB(x-delta))/delta
U = (10*CT(y+delta)+5*CB(y+delta)
     -10*CT(y)-5*H(y))/delta.
```

The inequalities 10 CT+5 H<=F(10,5)<=10 CT+5 CB, together with the secant bounds for convex functions, imply G'(s)<=U-17L<0 in the interior of each piece (and hence G is strictly decreasing on the entire interval). All twelve **17L-U>0** assertions pass using exact rational intervals.

At s=8002/10000 the strict lower bound 10 CT+5 H-17 CB>0 passes; at s=8003/10000 the strict upper bound 10 CT+5 CB-17 CB<0 passes. By continuity and strict monotonicity, the crossing alpha exists once and is unique in this interval.

Uniqueness of optimal count pairs, including at alpha and at the new right boundary, uses the previous author theorem's strict-tilt argument: fT has unique tilt t=1/2 while fB has tilt unequal to 1/2 when 0<s<1. Thus F is strictly convex along any segment joining distinct count vectors with different T/B ratios, excluding nonvertex ties on upper-hull edges. This does not claim strict convexity of F on the entire positive quadrant.

### 4. New discrete jump at s=9/11

At the endpoint s=9/11 the new vertex (11,4) becomes feasible. Exact lower bounds show

```text
11*CT+4*H-17*CB > 0,
4*H-3*CT > 0.
```

Therefore F(11,4)>F(0,17) and F(11,4)>F(14,0). The strict-tilt fact excludes any other integer count pair tying at this boundary. This is a discontinuous change in the optimizer due to integer feasibility, not a discontinuity of each fixed-count F.

## Verification method and scope

The executable standard-library Python VERIFY.py implements exact fractions, integer-square-root enclosures with denominator 10^33, and a 27-term artanh logarithm series with rigorous tail 2|v|^(55)/[55(1-v^2)] when v=(z-1)/(z+1), |v|<1/3. Bernoulli CB is calculated from exact rational bounds on its optimal Chernoff tilted mass rho=J/(H0+J), H0=log(a/b), J=log((1-bs)/(1-as)), and the KL expression D((rho,1-rho)||(as,1-as)); H is evaluated at t=1/2. It executes 12 monotonicity, 3 endpoint, 8 competitor, and 2 boundary certificates = **25 strict assertions**, plus full finite hull and feasibility-break assertions. The recorded program was actually executed, giving RUN_EVIDENCE.txt. Mathematical result is for the defined two-observer auxiliary N=4 model. Separate unrestricted ten-label S23 minimax remains bracketed by [1/2,2/3] in the source frontier.

### Remaining objectives

Independent review of this proof and its computational certificates; next exact feasibility cell [9/11,5/6), especially whether (11,4) relinquishes optimality to (0,17) and the next threshold. A separate bridge must be established before this auxiliary count optimization is used as a theorem for the mother minimax problem. P000's six spatial axes plus time and the residual-provenance constraints remain unchanged.
