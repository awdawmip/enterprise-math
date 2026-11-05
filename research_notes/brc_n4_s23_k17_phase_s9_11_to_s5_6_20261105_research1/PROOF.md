# Exact S23 BRC K=17 phase theorem: 9/11 ≤ s ≤ 5/6

**Date:** 2026-11-05. **Status:** AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED. **Frozen scientific pin:** `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

## Model and exact theorem

Write `a=11/21`, `b=10/21`. Full-source observation T distinguishes the three-outcome laws `(as,1-s,bs)` and `(bs,1-s,as)`; the separately typed projection B distinguishes Bernoulli laws `(as,1-as)` and `(bs,1-bs)`. For `0≤t≤1` put

```
fT(t,s)=-ln(1-s+s*(a^t*b^(1-t)+b^t*a^(1-t)))
fB(t,s)=-ln((as)^t*(bs)^(1-t)+(1-as)^t*(1-bs)^(1-t))
F(m,n;s)=max_{0≤t≤1} (m*fT(t,s)+n*fB(t,s))
CT(s)=F(1,0;s), CB(s)=F(0,1;s), H(s)=fB(1/2,s).
```

Each integer design `(m,n)∈Z_{≥0}²` has exact budget `(2-s)m+n≤17`. The Chernoff tilt `t` is **shared** across all observations in a mixed design.

**Theorem.** There exists exactly one `α∈(81839/100000,81841/100000)`, i.e. `0.81839<α<0.81841`, with `F(11,4;α)=17 CB(α)`. For every real `s∈[9/11,α)`, the unique globally optimal integer count pair is `(11,4)`; for `α<s<5/6`, it is `(0,17)`. At `s=α` those two and only those two designs tie. At `s=5/6`, `(12,3)` becomes feasible and is the unique global optimizer. The floor threshold `s=14/17` does not change the feasible set because the affected `m=17` row remains infeasible.

## Exact feasibility reduction

For fixed m, increasing n strictly raises F because the B hypotheses differ. The largest feasible n is `n_m=17-2m+floor(ms)`, retained only if `n_m≥0`. It suffices to test m=0,…,17; m=17 is infeasible throughout. The complete set of rational floor thresholds for m≤17 inside the closed interval is precisely `9/11,14/17,5/6`. The middle threshold only affects m=17; its n remains negative. Therefore for **all real** `9/11≤s<5/6` the upper convex hull of the feasible maximal-n integer points has vertices `(0,17),(11,4),(14,0)`; at `s=5/6` the vertices are `(0,17),(12,3),(14,0)`. VERIFY.py enumerates every maximal-n pair, calculates the hull with exact integer cross products and checks one representative for each constant-floor cell and each relevant boundary.

As `F(m,n;s)` is the supremum of affine functions of `(m,n)`, F is convex in the count vector. Hence the maximum of F over these integer feasible points is attained at a hull vertex; the strict-tilt argument below eliminates nonvertex ties.

## Positivity and uniqueness certificates

For `0<s<1`, `CT(s)=-ln(1-s+2s√(ab))`. `H(s)=-ln(s√(ab)+√((1-as)(1-bs)))` and `H≤CB`. Every mixed count pair obeys

```
m CT(s)+n H(s) ≤ F(m,n;s) ≤ m CT(s)+n CB(s).
```

Both `CT,CB` and every fixed-count `F(m,n;·)` are continuous convex functions of s. For CT this follows from negative log of a positive affine coefficient; for fixed t in B, the Chernoff coefficient is a sum of weighted geometric means of affine positive functions, hence concave, and negative log preserves convexity.

**Exclusion of (14,0).** Put `D(s)=17CB(s)-14CT(s)`. Split `[9/11,5/6]` into four equal exact rational intervals `[x,y]` and put `δ=1/10000`. The verifier checks `D(x)>0` and

```
17[CB(x)-CB(x-δ)]/δ > 14[CT(y+δ)-CT(y)]/δ.
```

Secant monotonicity of convex functions makes this a strict lower bound for `D'` on each open subinterval. Thus `D(s)>0` throughout, and `(14,0)` loses to `(0,17)`.

**The unique crossing.** Let `G(s)=F(11,4;s)-17CB(s)`. Divide `[9/11,5/6]` into twelve equal rational intervals `[x,y]`, `δ=1/10000`, and define

```
L=[CB(x)-CB(x-δ)]/δ
U=[11CT(y+δ)+4CB(y+δ)-11CT(y)-4H(y)]/δ.
```

On every interval the one-sided derivative of `G` is at most `U-17L` by convex secant inequalities and the preceding F bounds. All twelve exact `17L-U>0` assertions pass, establishing strict decreasing G for **every real** s in the interval. At `s=81839/100000`, `11CT+4H-17CB>0`; at `s=81841/100000`, `11CT-13CB<0`. Hence continuity and strict decreasing prove precisely one α in the stated strict rational bracket.

**Right jump.** At `s=5/6` the exact lower bounds

```
12CT+3H-17CB>0,  and  3H-2CT>0
```

show `F(12,3)>F(0,17)` and `F(12,3)>F(14,0)`.

**Strict nonvertex exclusion.** For `p=as>q=bs` and `p+q=s<1`, the B Chernoff coefficient has strictly negative t-derivative at `t=1/2`. Indeed `p/q>(1-q)/(1-p)>1` and `z/sinh(z)` decreases for `z>0`; the derivative equals `(p-q)[u/sinh(u)-v/sinh(v)]<0` for `u=(1/2)ln(p/q)`, `v=(1/2)ln((1-q)/(1-p))`. Thus its unique minimizing tilt `tB>1/2`, while the symmetric T coefficient has its unique optimum at `1/2`. At any positive mixed ratio m:n the unique tilt is strictly between them. Two different T/B ratios cannot share a maximizer, since their first-order equations would force both component derivatives to vanish. For any segment between distinct nonproportional hull vertices, the support-function convexity inequality is therefore strict at interior points. Every nonvertex feasible point is dominated by a vertex, including at the α tie and right boundary.

## Exact computation and coverage

The accompanying CPython standard-library `VERIFY.py` ran locally on 2026-11-05. It uses `Fraction`, `isqrt`, square-root enclosing intervals with denominator `10^34`, and 28 terms of the `atanh` log expansion; the remainder satisfies `|error|≤2|v|^57/[57(1-v²)]` for `v=(z-1)/(z+1)`, `|v|<1/3`. For CB it bounds the exact tilted Bernoulli mass `ρ=J/(ln(a/b)+J)` where `J=ln((1-bs)/(1-as))`, then uses the exact KL representation `CB=D((ρ,1-ρ)||(as,1-as))` with outward intervals. Four hull checks, twelve monotonicity certificates, three crossing signs, eight D certificates, and two right-boundary certificates pass; **25 strict interval inequalities** are asserted. No numeric sample is used in place of a real-interval inequality.

**Result scope:** exact joint-Chernoff integer-design theorem for the declared two-observer auxiliary N=4 S23 model and real s∈[9/11,5/6]. Original ten-label S23 minimax remains its separately tracked [1/2,2/3] question. The B projection retains its observer distinction and joint provenance, consistent with P000 and the active project constraints. Independent mathematical review and formal task admission remain pending.
