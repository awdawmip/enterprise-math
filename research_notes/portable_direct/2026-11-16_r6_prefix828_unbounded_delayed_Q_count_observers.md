# PREFIX-828 — Arbitrarily delayed exact observation of named BRC sources

**Status:** AUTHOR_PROVED / EXACT_BIGINT_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.  
**Input:** frozen `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`; inherits PREFIX-827's fully defined unnormalized positive-count Q-only BRC source model. No native X6 timing, source-phase or shared CLAIM admission is asserted.

## 1. Unbounded delay theorem

**Theorem 828.1.** For every integer `n≥1`, there exist two distinct positive-integer-weight named-source initial configurations with absent distinguished mark, source count `p=2^{n-1}`, and capacity `q=p\), whose complete occupancy histograms under the same unnormalized operator `Q=R+A` agree at every `t=0,\ldots,n-1` and first differ at `t=n`. At that time their difference in occupancy bin `p-n` equals exactly
\[
\boxed{-n!(n-1)!\,2^{n(n-1)/2}.}
\]
The two configurations use the same shared nonnegative distinguished insertion/removal weights `a,b`; the statement works in particular for positive `a,b`.

Construct two sets of positive removal weights by dividing the integers `1,\ldots,2^n` according to the parity of the binary digit sum of `j=\beta-1`. Let `A_n` contain even-parity `j+1` and `B_n` odd-parity `j+1`. Each contains exactly `2^{n-1}` positive integers; assign independent named sources to their entries. These are different weight multisets, not merely different labels.

## 2. Exact finite-polynomial proof

Consider the finite integer polynomial
\[
P_n(z)=\prod_{r=0}^{n-1}(1-z^{2^r})
=\sum_{j=0}^{2^n-1}(-1)^{s_2(j)}z^j,
\]
where `s_2(j)` is the number of set binary digits. Substitute `z=1+u` using the exact finite binomial identity. Each factor has a zero of degree one at `u=0`, with linear coefficient `-2^r`. Consequently
\[
P_n(1+u)=(-1)^n 2^{n(n-1)/2}u^n+u^{n+1}T(u)
\]
for an integer polynomial `T`. Multiplication by `1+u` corresponds to the chosen positive shift `j\mapsto j+1` and does not change the first nonzero coefficient.

Equating coefficients of `u^k` shows that the two groups have identical binomial moments `\sum\binom{\beta}{k}` for all `k<n` and difference `(-1)^n 2^{n(n-1)/2}` at `k=n`. Because the polynomial families `k!\binom{x}{k}` and `x^k` differ by a degree-triangular rational change of basis, their power sums agree in degrees `0,\ldots,n-1`; the degree-`n` power sum difference is `(-1)^nn!2^{n(n-1)/2}`.

Newton's exact integer-polynomial identities relating power sums and elementary symmetric polynomials `e_k` then imply
\[
e_k(A_n)=e_k(B_n)\quad(0\le k<n),
\qquad e_n(A_n)-e_n(B_n)=-(n-1)!\,2^{n(n-1)/2}.
\]
PREFIX-827 Theorem 827.1 shows that the entire occupancy histogram after `t` Q steps depends only on `e_0,\ldots,e_t`, so all histograms agree for `t<n`. At `t=n`, reaching occupancy `p-n` requires exactly `n` unmarked removals and no distinguished-source operation; those paths have weight `n!e_n` by permutation of the removed named sources. The displayed difference follows, proving first separation at exactly step `n`. □

The argument uses finite integer polynomials, exact binomial coefficients and legal named BRC branch counts. It makes no π/trigonometric, analytic Taylor, physical-time or approximate numerical claim.

## 3. Explicit example and significance

At `n=3`, `p=q=4`:
\[
A_3=\{1,4,6,7\},\qquad B_3=\{2,3,5,8\}.
\]
They have identical `e_0,e_1,e_2`, so **all five occupancy bins** match at `t=0,1,2`. At `t=3` their occupancy-one bin differs by `-3!\,2!\,2^3=-96`.

This is **arbitrary finite-horizon invisibility with increasing source count**. It does not say that a fixed finite model can hide a future discrepancy forever. It demonstrates why an observer quotient valid through horizon `H` is not automatically safe for the unbounded Q-only future. It does not claim that identical count traces imply identical named provenance, or that a Q-only quotient is valid under separate R/A or individually addressed source operations.

The sequence index `t` counts BRC operator applications; it is neither elapsed physical time nor a native X6 heartbeat interval. Positive count masses are not signed/complex amplitudes.

## 4. Reproducibility and limits

`PREFIX828_R6_DELAYED_OBSERVER_CHECK.js` validates the partition, all elementary-symmetric moment agreements and power sum differences for `n=1..10` using BigInt. For `n=1..5`, it independently enumerates every reachable named subset and each weighted legal Q branch through the first distinguishing step, taking `a=2,b=3` and `q=p`; it checks **the entire histogram**, not only the target output bin. The largest fully enumerated example uses `p=q=16`. Results are in `PREFIX828_R6_DELAYED_OBSERVER_RESULTS.json`. These finite tests do not substitute for the all-`n` combinatorial proof.

**Frontier:** determine minimal positive source count and bounded-weight tradeoffs for prescribed delay; compare individually addressable operations. Also retain independent unresolved `q≥5,b>0` minimum nonnegative linear Q carrier problem of PREFIX-825. Current native task owner read identifies no active CLAIM; this auxiliary result changes no shared Task/Result/Review state and has no newly authenticated Activity checkpoint.
