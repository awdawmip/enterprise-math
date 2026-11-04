# BRC N=4 / S23: exact K=17 phase classification on 1/3 <= s <= 2/5

Date: 2026-11-05 (Asia/Shanghai). Author-side exact analytic proof with an executed rational certificate, continuing `awdawmip/enterprise-math@0d80449f5c1c46517acfb55585f266e47989ff6b`. Frozen scientific input remains `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Independent review and native task Result admission are pending.

## Typed experiment and question

Let a=11/21, b=10/21. Preserve the original ternary source T with P=(as,1-s,bs), Q=(bs,1-s,as), and the specified Bernoulli projection B with P=(as,1-as), Q=(bs,1-bs). Costs are cT=2-s, cB=1. For t in [0,1], define

    fT(t;s)=-log(1-s+s*(a^t*b^(1-t)+b^t*a^(1-t)))
    fB(t;s)=-log(s*a^t*b^(1-t)+(1-as)^t*(1-bs)^(1-t))
    F(m,n;s)=max_t [m*fT(t;s)+n*fB(t;s)]
    CT(s)=F(1,0;s), CB(s)=F(0,1;s), H(s)=fB(1/2;s).

The shared t in F is necessary: mixed observations are not optimized independently. Maximize F over integers m,n>=0 subject to (2-s)m+n<=17. For every feasible m the objective increases strictly with n, so the maximal n is `n_m=17-2m+floor(ms)`.

## Theorem: two continuous switches and a new boundary activation

There exist unique alpha and beta satisfying

    F(9,2;alpha)=17*CB(alpha),   1/3 < alpha < 167/500;
    F(8,4;beta) =17*CB(beta),  3/8 < beta < 47/125.

The global optimizer is uniquely (9,2) for 1/3<=s<alpha; exactly (9,2) and (0,17) tie at alpha; uniquely (0,17) for alpha<s<3/8; uniquely (8,4) for 3/8<=s<beta; exactly (8,4) and (0,17) tie at beta; uniquely (0,17) for beta<s<2/5; and uniquely (10,1) at s=2/5. Thus 3/8 and 2/5 are integer-feasibility activations producing global optimizer jumps, whereas alpha and beta are continuous Chernoff-information crossings.

## Complete feasible-set reduction

For 1/3<=s<3/8 the maximally filled pairs (m,n_m), indexed m=0,...,10, are

    (0,17),(1,15),(2,13),(3,12),(4,10),(5,8),
    (6,7),(7,5),(8,3),(9,2),(10,0).

For 3/8<=s<2/5 exactly one pair changes: (8,3) becomes (8,4). At s=2/5, the pairs (5,8) and (10,0) become (5,9) and (10,1), respectively. There are no other integer thresholds in the stated parameter interval.

On [1/3,3/8), for m<=9 all the listed points are at or below the line joining (0,17) to (9,2), with equality only at m=0,3,6,9. Convexity of F in (m,n) and strict increase in n reduce the candidates to (0,17),(9,2); the separate point (10,0) is excluded by `17*CB-10*CT>0`.

On [3/8,2/5), every listed point lies at or below the upper concave polygonal chain (0,17)--(8,4)--(10,0), with (9,2) on its last edge. The same convexity reduces to (0,17),(8,4),(10,0). The latter is again excluded by `17*CB-10*CT>0`.

At s=2/5, all maximally filled points lie at or below the straight line (0,17)--(10,1), with only the additional equality (5,9). By convexity, only the endpoints (0,17),(10,1) can maximize, and the exact strict endpoint comparison below selects (10,1).

For clarity about uniqueness: pure T has its unique maximizing t=1/2, while pure B has a unique maximizing t different from 1/2 for 0<s<1. Every mixture with positive T and B weight has an optimal t distinct from both of those pure-design maximizers (its derivative at either pure maximizer is nonzero). Thus a nontrivial convex interpolation of two designs with different optimal t has F strictly smaller than the larger endpoint. This removes the interior points (3,12),(6,7),(9,2) or (5,9) from endpoint ties where relevant. In particular the only ties on the reported open cells occur at alpha and beta.

## Strict continuous-crossing proof by convex secants

For each fixed t, both fT(t;s) and fB(t;s) are convex in s: their underlying Chernoff coefficients are positive concave functions of s, and -log is convex and decreasing. Consequently F(m,n;s), CT and CB are convex in s. For delta=1/10000 and any subinterval [l,r], let

    L_l = [CB(l)-CB(l-delta)]/delta,
    U_(m,n),r = [m*CT(r+delta)+n*CB(r+delta)-m*CT(r)-n*H(r)]/delta.

Because `m*CT+n*H <= F(m,n) <= m*CT+n*CB` at each s, convexity bounds every secant slope of F on [l,r] by U and every secant slope of CB from below by L. Hence `17*L_l-U_(m,n),r>0` implies `F(m,n;y)-17*CB(y)<F(m,n;x)-17*CB(x)` for all l<=x<y<=r.

The attached Fraction-only certificate verifies this strict inequality on 12 equal rational subdivisions of [1/3,3/8] for (9,2), and on 12 equal rational subdivisions of [3/8,2/5] for (8,4). For the extra pure-T competitor it verifies both `D=17*CB-10*CT>0` at the left endpoint and a positive lower secant-slope bound for D on each of [1/3,3/8] and [3/8,2/5]. Thus D>0 throughout.

The exact source inequalities also establish

    9*CT(1/3)+2*H(1/3)>17*CB(1/3),
    9*CT(167/500)+2*CB(167/500)<17*CB(167/500),
    8*CT(3/8)+4*H(3/8)>17*CB(3/8),
    8*CT(47/125)+4*CB(47/125)<17*CB(47/125),
    10*CT(2/5)+H(2/5)>17*CB(2/5).

Continuity and strict decrease yield one and only one root alpha and beta on their respective cells. The last comparison plus the boundary hull establishes the unique optimizer (10,1) at s=2/5. This completes the theorem.

## Verification and research scope

`VERIFY.py` executes an outward interval calculation using only `fractions.Fraction` and `math.isqrt`: it brackets square roots at 10^-48 resolution, computes logarithms with 34-term atanh series and explicit geometric-tail bounds, and evaluates the Bernoulli Chernoff optimum with its closed-form tilted probability `rho=J/(H+J)`, `J=log((1-bs)/(1-as))`, `H=log(a/b)`. All printed `GT N/10^13` statements are strict rational lower bounds, not floating estimates. It executed 24 secant inequalities, 4 D inequalities and 5 pointwise strict inequalities: 33 decisive assertions, followed by `PASS_BRC_S23_K17_CELL_1_3_TO_2_5_TWO_SWITCHES_AND_BOUNDARY_JUMP_20261105` (full stdout in RUN_EVIDENCE.txt).

The source T is retained; B is a declared projection, not a replacement for the ternary experiment. The scope is the fixed-budget finite S23 discrimination experiment. The original ten-label S23 minimax mother target retains its prior open bounds [1/2,2/3] and its own proof obligations.
