# OAI7 r309 — Universal hypergeometric lower bound on shared-list tail certificates

Date: 2026-11-18. Status: Driver-authored exact finite-group combinatorial proof, intended as a necessary feasibility test for r307 (not Native Result admission). Contributor EM-DVR-DEBB5E. This is an external finite-abelian certificate, preserving full native X6/joint observer provenance for any later application.

## Question and dependencies

The integrated-tail coverage-transfer theorem r307 replaces conditional iid/Chernoff with a direct worst-set small-list tail quantity `q_c`. How short can an arbitrary (even dependent or deterministic) sample vector be before such a certificate is mathematically impossible?

Input: `research_notes/driver/2026-11-18_oai7_integrated_list_tail_transfer_r307.md`, revised exact GitHub commit `baaaabaacaf8543f62a45a00cdfcf03e95389075`, and the original external `openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a:.../coverage-transfer.tex`.

## Exact finite theorem

Let `G` be any finite abelian group of order `p>=2`, `1<=u<=p`, `n>=1`, and let `W=(w_1,...,w_n)` be an arbitrary random vector of elements of `G` (all temporal/coordinate dependence allowed). For each *fixed* subset `K subseteq G` with `|K|=u`, set
```text
L_K(W) = {x in G : sum_{l=1}^n 1_{x+w_l in K} <= n b u/p},
q = max_{|K|=u} Pr( |L_K(W)| > L_* )
```
for any `b>=0` and any real `0<=L_*<=p`. Define `m_*=min(n,p)` and the integer hypergeometric quantity
```text
R(p,n,u) = C(p-m_*,u) / C(p,u),
C(a,u)=0 when a<u.
```
Then, universally,
```text
      q >= [ R(p,n,u) - L_*/p ]_+.                 (HYP)
```
The bound does **not** assume marginal uniformity, stationarity, iid or a fixed number of distinct sampled offsets. It uses only the number `n` of exposed offsets and the definition of the list.

## Proof

Fix a realization `W=w`. Its number `m` of distinct values lies in `[1,min(n,p)]`. For each fixed `x`, the set `{x+w_l : 1<=l<=n}` contains exactly `m` group elements. Choose `K` uniformly from the `C(p,u)` subsets of cardinality `u`. The probability that *none* of those `m` points belongs to `K` is exactly `C(p-m,u)/C(p,u)`, which is at least `R(p,n,u)`.

Let `L_K^0(w)= {x : sum_l 1_{x+w_l in K}=0}`. Since `b>=0`, `L_K^0(w) subseteq L_K(w)`. Averaging over `K` and `W` yields
```text
E_{W,K}|L_K^0(W)| >= p R(p,n,u).
```
Let `E={|L_K(W)|>L_*}`. On the complement `|L_K^0(W)|<=L_*`; on `E`, `|L_K^0(W)|<=p`. Thus
```text
p R(p,n,u) <= E|L_K^0(W)| <= L_*+p Pr_{W,K}(E).
```
Now `Pr_{W,K}(E)` is the average over fixed `K` of their failure probabilities, bounded above by the maximum `q`. Rearranging and taking the positive part proves (HYP).

## Consequence for r307

For signed coordinate `c`, take `p=p_c`, `u=ceil(p_c^(1-beta))`, `b=tau+delta`, and `L_*=p_c^(1-beta'/2)`. Then r307's worst-set tail satisfies the **law-independent** lower bound
```text
q_c >= qmin_c :=
  [ C(p_c-min(n,p_c),u_c)/C(p_c,u_c) - p_c^(-beta'/2) ]_+.
```
Hence the integrated excess-tail criterion `R_xi <= eta(a_0-xi-delta/2)` can hold only if
```text
(1/(2k)) sum_c (qmin_c-xi)_+
                 <= eta (a_0-xi-delta/2).          (NEC)
```
This is an exact, cheap necessary precheck before investing in a proposed correlated-sampling schedule. Failure of (NEC) rules out the **r307 tail-certificate route at that n**; it does not assert that terminal residue coverage itself is impossible.

In particular, if every fixed K must have a small list with probability one (`q=0`), then necessarily
```text
C(p-min(n,p),u)/C(p,u) <= p^(-beta'/2).
```

## Sampling-scale corollary

Hold `0<beta'<=beta<1` fixed, take `u=ceil(p^(1-beta))`, and let `n=c p^beta log p` for fixed `c>0` (rounded to an integer). Then `n=o(p)` and
```text
R(p,n,u) = product_{j=0}^{n-1}(1-u/(p-j))
         = exp(-n u/p + o(log p))
         = p^(-c+o(1)).
```
Therefore universal almost-sure small lists `q=0` require `n >= (beta'/2-o(1)) p^beta log p`. More precisely, any fixed `c<beta'/2` contradicts that requirement for all sufficiently large `p`. This lower bound is specific to almost-sure/worst-set certificates. With an allowed positive tail budget `xi`, the exact bound (HYP) and (NEC) are the appropriate tests; one must not extrapolate the log-factor obstruction to every positive-tail scheme.

## Exact small example

For `p=101`, `beta=beta'=1/2`, `u=11`, `n=5`, the bound is
```text
q >= C(96,11)/C(101,11) - 101^(-1/4)
  > 0.2394.
```
This bound applies to *every* possible five-sample joint law, including fully correlated sampling. It is only a feasibility check on list tails; `p=101` is not asserted to meet the separate logarithmic hypotheses of the original transfer theorem.

## Interpretation and next useful step

r307 proves how a small averaged list tail transfers coverage under one entropy bill. r309 proves how to reject a too-short proposed shared-sample schedule without assuming independence or knowing its distribution. A constructive low-entropy schedule with `R_xi` below the sufficient r307 threshold for a nonuniform starting law remains a separate problem. No native X6/Link/Port or Gaussian-prime schedule realization is inferred here.

No sorry, admit or custom target axiom was used.
