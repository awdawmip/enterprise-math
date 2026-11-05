# Exact S23 BRC K=17 phase theorem: 5/6 ≤ s ≤ 6/7

Date: 2026-11-05. Status: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific source: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Continuity: prior immutable author-side proof `c24d3cc348b49a33b3333529ac8787a8481d9c88`, cell `9/11≤s≤5/6`.

## Exact model and theorem

Let `a=11/21, b=10/21`, `0≤t≤1`. The three-output source experiment T compares `(as,1-s,bs)` with `(bs,1-s,as)`; its separately typed Bernoulli projection experiment B compares `(as,1-as)` with `(bs,1-bs)`. Keep the two observation/provenance types distinct, using a **single shared** Chernoff tilt t across all observations:

```
fT(t,s)=-ln(1-s+s*(a^t*b^(1-t)+b^t*a^(1-t)))
fB(t,s)=-ln((as)^t*(bs)^(1-t)+(1-as)^t*(1-bs)^(1-t))
F(m,n;s)=max_{0≤t≤1}(m*fT(t,s)+n*fB(t,s))
CT(s)=F(1,0;s); CB(s)=F(0,1;s); H(s)=fB(1/2,s).
```

A design `(m,n)∈Z≥0²` is feasible iff `(2-s)m+n≤17`.

**Theorem.** There exist exactly two continuous strategy crossing points

```
83353/100000 < α < 83355/100000
84634/100000 < β < 84636/100000
```

such that the complete set of globally optimal integer count pairs is

| real parameter s | all global optimizers |
|---|---|
| 5/6 ≤ s < α | (12,3) uniquely |
| s = α | (12,3) and (0,17) only |
| α < s < 11/13 | (0,17) uniquely |
| 11/13 ≤ s < β | (13,2) uniquely |
| s = β | (13,2) and (0,17) only |
| β < s < 6/7 | (0,17) uniquely |
| s = 6/7 | (14,1) uniquely |

The jumps at `11/13` and `6/7` are genuine integer-budget feasibility events; both newly feasible designs immediately beat 17B.

## Exact integer reduction

For fixed m, fB(t,s)>0 at any interior tilt because the Bernoulli laws differ. Thus increasing n strictly improves F. The maximal feasible B count is `n_m=17-2m+floor(ms)`; rows with `n_m<0` are discarded. For all m=1,…,17 and real `s∈[5/6,6/7]`, the complete floor breakpoints are `5/6,11/13,6/7`. Exact integer cross-product hull enumeration (code) gives:

```
5/6 ≤ s < 11/13: upper hull (0,17),(12,3),(14,0)
11/13 ≤ s < 6/7: upper hull (0,17),(13,2),(14,0)
s=6/7:             upper hull (0,17),(14,1)
```

The hull and breakpoints are exact for every real s in each stated cell: floors are constant on each open cell, and endpoints are checked independently. Since F is the supremum of linear forms in (m,n), it is convex in the count vector; a maximum is attained at an upper-hull vertex (and lower n are strictly worse).

## Strict comparison certificates for all real s

At `0<s<1`, write
`CT=-ln(1-s+2s sqrt(ab))`, `H=-ln(s sqrt(ab)+sqrt((1-as)(1-bs)))`, and `H≤CB`.
For all m,n≥0, exact pointwise tilt bounds give
`mCT+nH ≤ F(m,n;s) ≤ mCT+nCB`.
The three scalar functions `CT,CB,F(m,n;·)` are continuous convex in s: for each fixed t, the T coefficient is affine and the B coefficient is a sum of concave weighted geometric means of positive affine forms in s; applying -ln and taking a supremum preserves convexity.

For `G_A=F(12,3;s)-17CB(s)` on `[5/6,11/13]` and `G_B=F(13,2;s)-17CB(s)` on `[11/13,6/7]`, partition each domain into 12 equal rational intervals `[x,y]`, set `δ=1/10000`, and evaluate outward rational intervals for

```
L = [CB(x)-CB(x-δ)]/δ
U = [mCT(y+δ)+nCB(y+δ)-mCT(y)-nH(y)]/δ.
```

Convex secant inequalities establish for all `s∈(x,y)` the strict upper bound `G'_(s)≤U-17L<0` in the one-sided/subgradient sense. The 24 exact assertions `17L-U>0` all pass, proving each G strictly decreasing over its whole real interval.

The positive endpoint lower signs `mCT+nH-17CB>0` at `s=5/6,83353/100000,11/13,84634/100000`, and negative endpoint upper signs `(17-n)CB-mCT>0` at `83355/100000,84636/100000`, all have strict rational certificates. Continuity therefore supplies exactly one zero of each G in its strict bracket.

To remove vertex (14,0) throughout `[5/6,6/7]`, put `D=17CB-14CT`. Partition into four rational intervals. Eight positive certificates assert `D(x)>0` and `17[CB(x)-CB(x-δ)]/δ>14[CT(y+δ)-CT(y)]/δ`; convex secants imply D is strictly increasing from a positive lower bound. Thus (14,0) loses to (0,17) for the entire interval.

At `s=6/7`, strict certified inequalities `14CT+H>17CB` and `H>0` show (14,1) beats both other hull vertices. At the internal jump `11/13`, the left sign for G_B proves (13,2) beats (0,17); the D certificate removes (14,0).

**No additional ties.** For `p=as>q=bs` and `p+q=s<1`, T has uniquely optimal tilt `t_T=1/2`. For B, its Chernoff coefficient's derivative at 1/2 equals `(p-q)(u/sinh(u)-v/sinh(v))<0`, where `u=(ln(p/q))/2>v=(ln((1-q)/(1-p)))/2>0` and `z/sinh(z)` decreases on positive z. Hence the unique B tilt `t_B>1/2`. A mixed design with m,n>0 has a strictly intermediate unique tilt; distinct positive T:B ratios have different maximizing tilts by their stationarity equations. The max of linear forms in counts is **strictly convex along any hull segment joining different T:B ratios**. Every interior/nonvertex point therefore lies strictly below the larger endpoint value, including at α and β. Lower-than-maximal-n designs are strictly inferior.

## Reproducible exact evidence

Run `python VERIFY.py` (CPython standard library). The verifier enumerates integer breakpoints and hulls, uses `Fraction`, `isqrt`, outward square-root intervals at scale 10^34, and a 28-term log atanh series with remainder `2|v|^57/[57(1-v²)]`, `|v|<1/3`. It bounds CB using the exact Bernoulli tilted mass `rho=J/(ln(a/b)+J)`, `J=ln((1-bs)/(1-as))`, and `CB=D(Bernoulli(rho)||Bernoulli(as))`, enclosing all quantities with rational intervals. 24 monotonicity + 6 endpoint + 8 D + 2 right-boundary strict certificates = **40 exact rational interval assertions**; all passed locally. Hull/breakpoint checks also passed.

**Scope:** exact global integer-design phase classification for this two-observer, shared-tilt N=4 S23 auxiliary model on all real `s∈[5/6,6/7]`. The distinct original ten-label minimax stays at the separately tracked `[1/2,2/3]` bound; connecting its admissible encoders and risks to this observation-design objective is the next mother-problem bridge. Mathematically independent review and native Result admission remain pending.
