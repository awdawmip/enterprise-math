# BRC N=4 S23 K=17: exact auxiliary observation-design phase on [7/8, 8/9]

Date: 2026-11-05. Mathematical source frozen at `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Independent author-side proof and exact rational verification. Previous certified author-side frontier: `0e3b9163039840fc407ee16f7d60eb3e86f413f5`. Independent mathematical review and native Result admission pending.

## Defined model (unchanged)

Set `a=11/21`, `b=10/21`; `7/8 <= s <= 8/9`. Preserve the original three-label observation `T` with laws `(as,1-s,bs)` vs `(bs,1-s,as)`, and its separate Bernoulli projection `B` with laws `(as,1-as)` vs `(bs,1-bs)`. These are two distinct typed experiments, not a claim of sufficiency of B for T or of the original ten-label minimax.

For one common Chernoff tilt `0<=t<=1`, put

`fT(t,s)=-ln[1-s+s(a^t b^(1-t)+b^t a^(1-t))]`

`fB(t,s)=-ln[(as)^t(bs)^(1-t)+(1-as)^t(1-bs)^(1-t)]`

`F(m,n;s)=max_t(m fT(t,s)+n fB(t,s))`, `CT=F(1,0;s)`, `CB=F(0,1;s)`, `H=fB(1/2,s)`.

Integers `m,n>=0` satisfy `(2-s)m+n<=17`.

## Theorem: full optimizer set for all real s in [7/8, 8/9]

There exists exactly one `alpha` in `(87516/100000, 87517/100000)`, and the optimizer set is:

- `7/8 <= s < alpha`: exactly `(m,n)=(8,8)`.
- `s=alpha`: exactly `(8,8)` and `(0,17)`.
- `alpha < s < 8/9`: exactly `(0,17)`.
- `s=8/9`: exactly `(9,7)`.

The floor-expression breakpoint `s=15/17` changes no *feasible* integer pair and does not change the upper hull or optimizer. At the right endpoint `8/9`, the newly feasible `(9,7)` is strictly optimal.

## Complete real-parameter proof

**Feasibility and convex-hull reduction.** Since `fB(t,s)>0` for the nonidentical Bernoulli laws, increasing the allowed B count strictly improves the optimized Chernoff information. For each feasible integer m its best n is
`n_m(s)=17-2m+floor(ms)`. Exhaustive rational breakpoints `k/m` for `1<=m<=17` within `[7/8,8/9]` are precisely `7/8,15/17,8/9`. Integer cross-product hull enumeration at these endpoints and one representative of each open cell yields upper hull vertices `(0,17),(8,8),(15,0)` throughout `[7/8,8/9)`, and `(0,17),(9,7),(15,0)` at `8/9`. The feasible lists immediately to either side of `15/17` are identical; `m=17` remains infeasible. As a supremum of linear functions in `(m,n)`, `F` is convex in the count vector; its maximum on this finite set lies at an upper-hull vertex. All submaximal n are strictly inferior for their fixed m.

**Convexity in s and rigorous derivative intervals.** For each fixed tilt `t`, `fT(t,s)` is minus log of a positive affine expression. In `fB`, the first Chernoff summand is affine in s, and the second is a weighted geometric mean of two positive affine expressions and hence concave; minus log of their positive sum is convex. Thus `F(m,n;s)` and `CB(s)` are convex as suprema of convex functions of s. Uniform bounds:
`L=m CT+n H <= F(m,n;s) <= U=m CT+n CB`.
For rational subinterval `[x,y]` and `delta=1/10000`, convexity gives for almost every `z in [x,y]`:
`F'(z) <= [U(y+delta)-L(y)]/delta`,
`CB'(z) >= [CB(x)-CB(x-delta)]/delta`.
A partition into 16 equal rational intervals yields 16 certified strictly positive values of
`17[CB(x)-CB(x-delta)]-[U(y+delta)-L(y)]`,
proving `G(s)=F(8,8;s)-17CB(s)` strictly decreasing on `[7/8,8/9]`. This derivative argument is valid across all real s, not merely rational sample points.

**Excluding 15T for the entire interval.** Let `D(s)=17CB(s)-15CT(s)`. Convex secant bounds and 16 additional exact inequalities
`17[CB(x)-CB(x-delta)] > 15[CT(y+delta)-CT(y)]`
show D strictly increasing; the exact sign `D(7/8)>0` therefore excludes `(15,0)` throughout the interval.

**One and only one interior crossing.** The exact signs
`8CT+8H>17CB` at `s=87516/100000` and
`8CT+8CB<17CB` at `s=87517/100000` trap the zero of G. Continuity and strict decrease make it unique. The left endpoint has `8CT+8H>17CB`.

**Endpoint jump.** At `s=8/9`, exact rational intervals establish both `9CT+7H>17CB` and `7H>6CT`. Thus newly feasible `(9,7)` strictly beats both other hull vertices.

**No hidden ties.** For distinct Bernoulli laws `p=as,q=bs`, the Bernoulli Chernoff-optimal tilt equals `1/2` exactly when `p+q=1`: rewrite the first-order equation with `u=p/q>1, v=(1-q)/(1-p)>1`, observe `ln(u)/(sqrt(u)-1/sqrt(u))` is strictly decreasing for u>1, so equality forces u=v, equivalent to p+q=1. Our `p+q=s<1`, whereas T uniquely maximizes at tilt `1/2`. The maximizing tilts for `F(8,8)` and `17CB` therefore differ, so on their connecting count segment strict convexity excludes interior tied count points at alpha. Every other feasible count is strictly inferior by hull convexity or by smaller B count.

## Executable proof certificate and coverage

`VERIFY.py` is a standalone stdlib `Fraction`/`isqrt` program. Rational outward sqrt bounds use scale `10^35`. A 32-term log atanh series uses the strict remainder `2|v|^65/[65(1-v^2)]` for `|v|<1/3`. `CB` is enclosed using the exact Bernoulli Chernoff optimum `rho=J/(L+J)`, `L=ln(a/b)`, `J=ln[(1-bs)/(1-as)]`, and `D(rho||as)`. All intermediate interval products and quotients are outward enclosures; exact rational assertions certify every printed strictly positive lower bound.

The executed verifier proves 16 G derivative certificates, 16 D derivative certificates, 6 endpoint/crossing signs (38 strict assertions), plus complete integer floor/hull checks. The executed stdout is in `RUN_EVIDENCE.txt`.

This is an exact theorem for the two-observer auxiliary K=17 experiment. A stochastic-kernel/decision-risk bridge to the original ten-label S23 minimax remains an independently specified research problem. Project P000, the ACTIVE X6 world, and frozen scientific source are unchanged.
