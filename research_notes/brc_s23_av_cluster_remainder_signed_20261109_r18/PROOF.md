# Exact mixed-remainder, signed rational-cluster risk formula

2026-11-09 · Enterprise Math / S23 auxiliary AV circle observer · author-side proof, independent review pending.

Frozen science input: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Immediate predecessor: `research_notes/brc_s23_av_direct_affine_rational_clusters_20261109_r17/PROOF.md` at PR #1777 @ `d6ed659529775f1c9180cce46852934d4f5050d6`.

## Statement (exact cluster correction, arbitrary history remainder and either sign)

Let `q>=1`, `gcd(p,q)=1`, `m>=q`, `n>=m`. Let `0<theta<1` and `theta=p/q+epsilon` with `epsilon!=0`; when `epsilon>0` require `0<=p<q`, and when `epsilon<0` allow `1<=p<=q`. Put `eta=|epsilon|`, and assume

```
n*eta < 1/q.
```

Let `C_i={i*theta}` and let `R_theta(m,n-m)` be the minimum whole-future-block Bayes error with uniform initial phase, given the first `m` labelled cut observations. Equivalently,

```
R_theta(m,n-m)=1 - sum_{I in historical m-cut arcs}
                   max_{J subset I, J an n-cut subarc} length(J).
```

For `epsilon>0`, set `k=p`; for `epsilon<0`, set `k=q-p`, and calculate the formula in the reflected phase `theta_+=theta` or `1-theta`, respectively. In either case `theta_+=k/q+eta`, `0<=k<q`, `gcd(k,q)=1`.

For each residue `0<=r<q`, write

```
ell_r(t)=r+q*floor((t-1-r)/q)  (t>=q),
r_plus = (r+k^{-1}) mod q     (q>1);  r_plus=0 (q=1),
G_r(n)=1/q+(r_plus-ell_r(n))*eta,
delta=q*eta,
E_r(n) = 1 if ell_r(n)>ell_r(m), else 0.
```

Then the **exact finite-horizon correction formula**, for all real (rational or irrational) theta meeting the hypotheses, is

```
R_theta(m,n-m) =
 (n-m)*delta
 - sum_{r=0}^{q-1} E_r(n)*max(0, delta-G_r(n)).        (1)
```

In particular the formula requires only `O(q)` exact rational/arithmetic comparisons after `p,q,m,n,eta` are supplied. It handles every value of `m mod q`, both signs of epsilon, and the full cluster-separated interval `n*eta<1/q`, including the boundary regime in which the earlier one-run law is no longer linear.

**Linear-regime corollary.** If `G_r(N)>=delta` for all r, then (1) gives `R_theta(m,n-m)=(n-m)|q*theta-p|` for every `m<=n<=N`. The simpler sufficient condition `(N+q)*eta<1/q` implies these inequalities. Thus predecessor r17's one-run theorem extends from `q|m` to **all m>=q** and includes negative perturbations by phase reflection. At strict equality `G_r=delta`, (1) remains valid and the correction is zero.

## Proof

First take `theta_+=k/q+eta`. Since `n*eta<1/q`, every phase `{i*theta_+}` with `0<=i<n` lies in the unique base-fraction cluster `{rk/q}` of `r=i mod q`, offset by `i*eta`; no cluster wraps or overlaps another. Coprimality orders the q clusters cyclically. Every cluster is nonempty already at time m, because `m>=q`. Consecutive indices inside cluster r differ by q and their phase gap is `delta=q*eta`. Its last index at time t is `ell_r(t)`; the next clockwise cluster has residue `r_plus`.

The clockwise boundary gap from the final point of cluster r to the first point of the next cluster is exactly `G_r(t)=1/q+(r_plus-ell_r(t))*eta>0`. Its sum over all residues is

```
sum_r G_r(t)= 1 - (t-q)*delta,
```

because `sum_r r_plus=sum_r r` and `sum_r ell_r(t)=sum_r r+q(t-q)`.

The m-cut history has precisely `m-q` intra-cluster arcs of length delta, and q boundary arcs. Refinement never splits an old intra-cluster arc. If cluster r acquires no new point between m and n, its original boundary arc is a single interval of length `G_r(n)=G_r(m)`. Otherwise the old boundary arc splits into at least one interval of length delta and a terminal interval of length `G_r(n)`; its longest n-subarc is `max(delta,G_r(n))`. Consequently the sum of the m historical-arc maxima is

```
(m-q)*delta + sum_r G_r(n)
                + sum_r E_r(n)*max(0,delta-G_r(n)).
```

Substitute the displayed sum of boundary gaps into `R=1-sum maxima` to obtain (1).

For negative epsilon, the cut sequence for `theta` is the reflection of the sequence for `1-theta=(q-p)/q+eta`: `{i*(1-theta)}={-i*theta}`. Reflection preserves every historical/refined arc length and the inclusion relation, so the two Bayes risks agree. This completes the proof.

For the corollary, `ell_r(t)` is nondecreasing in t, so `G_r(t)` is nonincreasing, and `G_r(t)>=G_r(N)>=delta` for all t<=N. Under `(N+q)*eta<1/q`, `G_r(N)>=1/q-(N-1)*eta>q*eta=delta`. QED.

## Frozen S23 application and new short-range exact certificate

The predecessor's strict parameter enclosure is

```
262204504569236716045286/10^24 < theta
 < 262204504569236716045287/10^24.
```

Take `p/q=16/61`, `eta=16/61-theta`, `m=128`; use reflection, so `k=45` and `k^{-1}=19 mod 61`. The strict cluster-separation inequality holds through `n=180`, but fails at `n=181`. Across the entire certified theta enclosure, all 61 correction-comparison signs are stable at each n in [128,180]. Formula (1), with exact rational endpoint checks, yields

```
R_theta(128,n-128) =
  (n-128)*(16-61*theta)                                  (128<=n<=164),
  36*(16-61*theta)+(n-164)*(164*theta-43)              (165<=n<=180).
```

At the first deviation n=165, cluster residue r=42 has `r_plus=0`, `ell_42(165)=164`; its new correction is `delta-G=59-225*theta>0`, yielding `R_theta(128,37)=533-2032*theta`. The new endpoint is

```
R_theta(128,52)=R_theta(128,180-128)=-112+428*theta.
```

This derives the first two earlier observed S23 risk-increment slopes from an explicit rational-cluster carrier rather than a general Farey scan. The finite certification covers n=128,...,180 exactly; the general theorem covers all qualified real theta,m,n.

## Independent executable evidence

`VERIFY_CLUSTER_MIXED.py` performs exact `fractions.Fraction` direct n-cut subdivision against the new O(q) formula for 11,040 selected finite cases, including 8,048 with `q ∤ m`, 5,520 with negative epsilon and 914 positive-correction cases. It separately checks both strict S23 theta endpoints over every n=128,...,180, checks all branch signs coincide at both endpoints and reconstructs the integer-affine coefficients `(A,B)` of `A+B*theta`. Its actual stdout is `RUN_EVIDENCE.txt`. The checker uses rational parameters in its finite comparison tests; the theorem itself is a direct proof for all real parameters under the displayed inequalities.

Scope: S23 auxiliary scalar finite-future Bayes observer; no native X6 transfer, shared-task CLAIM, Result/Review or Foundation admission claimed. The phase- and residue-labelled carrier `(k,q,eta,ell_r,r_plus)` must be kept for provenance-sensitive future operations.

## Next question

Can the correction sum `sum_r E_r max(0,delta-G_r)` be rank-selected without scanning q residues, first for the S23 convergent q=61 and then for large q, while preserving signed/reflected residue labels and explicit arithmetic/precision costs? In the range beyond cluster separation, test an adjacent Farey rational-epoch decomposition against this exact boundary-correction formula.