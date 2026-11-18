# Four-bin exact rational-cluster Bayes risk: constant-size residue summation

Date: 2026-11-09. Mode: author-side TASK_RESEARCH. Frozen science: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Predecessor: `research_notes/brc_s23_av_cluster_remainder_signed_20261109_r18/{PROOF.md,ADDENDUM_POSITIVE_GAP.md}` at immutable revision `652630a5feb1afb5f629d94e0b3f6196c74aa70a` (Draft PR #1777).

## Statement

Let `q>=1`, `gcd(p,q)=1`, `m>=q`, `n>=m`, `0<theta<1`, and `theta=p/q+epsilon` with `epsilon!=0`. Take `0<=p<q` for positive epsilon, `1<=p<=q` for negative epsilon. Set `eta=abs(epsilon)>0`, `delta=q*eta`; on reflection use `k=p` for epsilon>0 and `k=q-p` otherwise. Set `s=inv(k) mod q` for q>1, `s=0` for q=1. Write `n=a*q+b`, `0<=b<q`, `t=q-s`.

Assume the positive-gap cluster-order condition of r18: for every residue `0<=r<q`,

```
G_r(n)=1/q + (((r+s) mod q) - (r+q*floor((n-1-r)/q)))*eta > 0.
```

Define half-open integer residue intervals
`X_1=[0,b)`, `X_0=[b,q)`, `Y_1=[t,q)`, `Y_0=[0,t)`.
Let `E` be the set of residues of integers in `[m,n)`, and `w_xy = | E intersect X_x intersect Y_y |`. If n-m>=q, E=[0,q); otherwise E is a cyclic residue interval of length n-m and has at most two ordinary-interval pieces.

**Theorem.** For the uniform initial-phase circle-cut observer, the minimum whole-future-block error is

```
R_theta(m,n-m) = (n-m)*q*eta
 - sum_{x,y in {0,1}} w_xy*max(0,(a*q-s+q*(x+y))*eta-1/q).      (A)
```

The all-residue hypothesis `G_r(n)>0` is **itself** equivalent to at most four exact checks: for each `(x,y)` with nonempty `X_x intersect Y_y` check

```
G_xy = 1/q - ((a-1)*q-s+q*(x+y))*eta > 0.                      (B)
```

Thus the O(q) correction sum *and its validity guard* from r18 both collapse to O(1) arithmetic and order comparisons **given** the inverse s, for arbitrary history remainder and either epsilon sign. Extended Euclid obtains s in O(log q) arithmetic divisions. This is an arithmetic-operation claim; exact representation, bit length, parameter construction and comparison precision must be included for bit complexity. The q=1 case uses s=0.

## Proof

For `n=a*q+b` the final source index in residue r satisfies

```
ell_r(n)=r+q*floor((n-1-r)/q)
        =r+q*(a-1)+q*[r<b].                                   (C)
r_plus=(r+s) mod q =r+s-q*[r>=q-s].                             (D)
```

Put `x=[r<b]` and `y=[r>=q-s]`. Subtracting gives
`ell_r(n)-r_plus=q*(a-1)-s+q*(x+y)`.
Consequently `G_r(n)=G_xy` and
`delta-G_r(n)=(a*q-s+q*(x+y))*eta-1/q`.
By the proved r18 positive-gap refinement formula,

```
R_theta(m,n-m)=(n-m)*delta
 - sum_{r=0}^{q-1} E_r(n)*max(0,delta-G_r(n)),
```

where `E_r(n)=1` exactly when some new source index `i in [m,n)` has residue r. Partitioning these residues by the two predicates x and y makes the summand constant on each of four bins and replaces its count by w_xy, proving (A). The same partition groups all G_r into the four exact candidate values (B), proving the guard equivalence. Each w_xy is at most two intersections of three half-open integer intervals, each computed by `max(0,min(rights)-max(lefts))`. Reflection theta -> 1-theta preserves every phase-arc length and risk. QED.

## Exact first invalid cluster horizon

For fixed p,q,theta,m with positive gaps at m, each `ell_r(n)` is nondecreasing, so `min_r G_r(n)` is nonincreasing in n. Applying the four-bin guard to exponential bracketing and binary search obtains the last positive-gap n and first invalid n using O(log n_bad) exact guard queries without looping over q residues. This locates the *boundary event*; after the event, use the r18 first-swap theorem or a future correctly labeled local-swap calculation rather than extending (A) beyond its hypotheses.

For the frozen S23 interval
`262204504569236716045286/10^24 < theta < 262204504569236716045287/10^24`,
with p/q=16/61, negative epsilon and m=128, strict exact rational endpoint checks give last valid n=225, first invalid n=226. The r19 formula reproduces every n=128,...,225 value, including
`R_theta(128,97)=-2047+7808*theta`. For n=226 use r18's separately certified first crossing `R_theta(128,98)=-2090+7972*theta`.

## Executed finite checks and scope

The locally executed `VERIFY_INTERVAL_COLLAPSE.py` and its `RUN_EVIDENCE.txt` used exact Python `fractions.Fraction` arithmetic. They compared 101,686 positive-gap cases against an independently coded O(q) residue sum, and 37,747 cases against sorted-circle historical-arc maxima. The data include 5,526 genuine nonzero-correction cases and 3,212 cases with n*eta>=1/q but all boundary gaps positive. Both strict S23 enclosure endpoints were tested for each n=128,...,225 and for the first invalid n=226. Large-q checks used q=10007,1000003,1000000007; q=10007 was also compared to the full residue loop. A transparent small correction example: theta=5/8, p/q=1/2, m=2, n=4 has exact R=3/8 versus uncorrected linear term 1/2.

The complete source carrier includes p,q,epsilon sign, eta,s,m,n and recoverable residue labels (r,r_plus,ell_r,E_r). The four-bin quotient is sufficient for this *scalar Bayes-risk observer*; provenance-sensitive future operations can recover source labels by interval membership. This is not a transfer to native X6 dynamics. Independent mathematical review, shared CLAIM, Result/Review, and Foundation admission are pending.

## Next

Construct an output-sensitive and provenance-preserving updater for post-positive-gap local cluster swaps. Identify and check the **second** boundary exchange after S23 n=226 against both certified parameter endpoints and explicit circle subdivision; compare bit cost and event count to the Farey/three-gap oracle.