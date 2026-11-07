# BRC N=4, S23 auxiliary T/B: complete K=17 upper-parameter phase on [15/16,1]

Date: 2026-11-05. Scientific source: immutable `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Status: **AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED**.

## Model

Set (a=11/21, b=10/21, a+b=1). For every real (s\in[15/16,1]), the two hypotheses (P,Q) give a full three-category observation T and its deterministic Bernoulli projection B:

```
P_T=(a*s,1-s,b*s),      Q_T=(b*s,1-s,a*s)
P_B=(a*s,1-a*s),        Q_B=(b*s,1-b*s)
B=indicator(first T category).
```

One independent T sample costs (2-s), one B costs 1. Choose integers (m,n\ge0) under ((2-s)m+n\le17). The common-tilt Chernoff exponent, with **one shared t** (not separately optimized for mixed samples), is

```
f_T(t,s)=-ln[1-s+s*(a^t*b^(1-t)+b^t*a^(1-t))]
f_B(t,s)=-ln[(a*s)^t*(b*s)^(1-t)+(1-a*s)^t*(1-b*s)^(1-t)]
F(m,n;s)=max_{0<=t<=1}{m*f_T(t,s)+n*f_B(t,s)}
C_T(s)=F(1,0;s),  C_B(s)=F(0,1;s).
```

## Theorem: all optimizers, every real s

There is precisely one (α) with **937594859/10^9 < α < 937594860/10^9** such that

| s | All integer maximizers of F |
| --- | --- |
| 15/16 ≤ s < α | (16,0) alone |
| s = α | (16,0) and (0,17), exactly |
| α < s < 1 | (0,17) alone |
| s = 1 | all 18 designs (m,17-m), m=0,...,17 |

At **s=16/17**, the floor expression for m=17 changes from -2 to -1 but stays infeasible. It produces no feasible or optimizer phase change. In particular this theorem completes the previously open [15/16,16/17] stage **and every remaining s up to 1**.

## Integer feasible domain: exhaustive symbolic argument

For each m, the largest feasible n is (n_m=17-2m+\lfloor ms\rfloor) provided (n_m\ge0). For **all** s∈[15/16,1), (⌊ms⌋=m-1) for m=1,...,16. The boundary points are therefore

```
(0,17), (1,15), (2,14), ..., (15,1), (16,0).
```

For m=17, n_17=-2 on [15/16,16/17) and -1 on [16/17,1), always infeasible. These claims and the entire formal rational breakpoint list `[15/16,16/17,1]` are checked with exact Fraction arithmetic.

The upper convex hull of the feasible points is the **single primitive edge** from (0,17) to (16,0), with gcd(16,17)=1. Every interior boundary point ((m,16-m)), 1≤m≤15, lies strictly beneath its chord by (1-m/16>0). The objective F is convex in (m,n) as a supremum of affine functions; it strictly increases with n at fixed m for distinct P_B and Q_B and any interior Chernoff tilt. Therefore every interior feasible integer design is strictly inferior to at least one hull endpoint. **Exactly two candidates** remain: (16C_T) and (17C_B).

At s=1 the full T law has a zero-probability middle category, so its nonzero binary law equals B under each hypothesis: P=(a,b), Q=(b,a). Both costs are 1. Every m+n=17 design gives the identical exponent 17C_T(1)>0; every smaller count is strictly worse. This proves exactly 18 endpoint ties.

## Continuous unique crossover: closed rational certificates

Define (u=s\sqrt{ab}), (L=\ln(a/b)>0), (J=\ln[(1-bs)/(1-as)]>0), (ρ=J/(L+J)). Exchange symmetry of T implies its minimizing Chernoff tilt t=1/2. Bernoulli tilted equal-KL condition gives the optimum mass ρ, hence

```
C_T(s)=-ln(1-s+2*u)
C_B(s)=rho*ln[rho/(a*s)]+(1-rho)*ln[(1-rho)/(1-a*s)].
```

For each t, T's overlap is positive affine in s. B's overlap is positive concave: its first term is affine, its second term is the weighted geometric mean of positive affine terms. Because -ln is decreasing convex, (f_T(t,s)) and (f_B(t,s)) are convex in s, as is (C_B(s)=\sup_t f_B(t,s)).

Put (d=1-2\sqrt{ab}>0). Then (C_T(s)=-\ln(1-ds)) and (C_T'(s)=d/(1-ds)), increasing in s. On each of 16 closed rational cells [x,y] covering the full [15/16,1], with δ=1/10000, convexity gives every interior z the bounds

```
C_B'(z) >= [C_B(x)-C_B(x-delta)]/delta,
C_T'(z) <= d/(1-d*y).
```

The attached VERIFY.py computes **rigorous outward rational intervals** and proves the strict inequality

```
17*[C_B(x)-C_B(x-delta)]/delta > 16*d/(1-d*y)
```

in **all 16 cells**. Therefore (G(s)=16C_T(s)-17C_B(s)) is strictly decreasing throughout the **whole real interval**. Four additional strict rational endpoint signs establish

```
G(15/16)>0,
G(937594859/10^9)>0,
G(937594860/10^9)<0,
G(1)<0.
```

Existence and uniqueness of α follow by continuity and strict decrease, proving the full optimizer classification (including the exact tie at α).

## Computation, reproducibility, and mathematical scope

`VERIFY.py` uses Python 3 standard library `Fraction`, `isqrt`, and `gcd`. Each square root is enclosed by neighboring rational points on a 10^-36 mesh with integer-square proof. Logs use the exact atanh expansion with N=34 terms and tail `2*|v|^(2N+1)/[(2N+1)*(1-v^2)]`, `v=(x-1)/(x+1)`, `|v|<1/3`. All interval operations enclose exact real values. Every certificate asserts a **strict positive rational lower bound**, not a sampled float value. The checker executed successfully for 16 continuum derivative certificates and four endpoint certificates, 20 in total, together with complete exact floor/hull and s=1 checks; actual stdout is saved in `RUN_EVIDENCE.txt`. Marker: `PASS_K17_S23_PHASE_15_16_TO_1_EXACT_20261105`.

The method reuses typed BRC observer preservation (full T category provenance and deterministic T→B projection), integer budget enumeration, common-tilt Chernoff information and convex rational slope certification. The finite-sample Blackwell-risk lemma for this precise T/B model was proved in the predecessor `@60a312ae34476f0b6b637189e7e452bf127f962a/PROOF.md`.

**Mother S23 ten-label lawful minimax:** its earlier recorded risk bracket is [1/2,2/3]. Transferring this auxiliary classification to that target remains a separate mathematical task: extract the mother encoder/decoder laws and permitted policies, and certify a hypothesis-wise stochastic kernel with its direction and policy composition. Independent reviewer and native Result admission are open.
