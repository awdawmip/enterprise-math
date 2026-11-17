# EC49FRS — Exact two-parameter named-observer cost phase diagram

Date: 2026-11-17. Scientific input **unchanged**: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Parent original-BRC research: [EC49FRR PR #2645](https://github.com/awdawmip/enterprise-math/pull/2645), immutable commit `bf6939bbaffa98a6be07ea83f65f90a3207a7ce1`. Status: **AUTHOR_PROVED / EXACT_FINITE_BELLMAN_GRID_CHECKED / NOT_REVIEWED**.

## Model

Take the frozen BRC class 16943, 141 *complete named* response states (from 310 configurations) and all 228 original physical observations (terminal indices 0–143; root indices 144–227). Preserve the original native response map, decision-tree legality, labels, source provenance, and weights. Let `x=r/t=1`, `lambda=0` (uniform prior over 141 named states), and `t>0`. All observations cost `t` except named terminal q32 and q34, which cost `(1+a)t` and `(1+b)t`, respectively, with arbitrary **real** `a,b>=0`.

For a complete identifying tree Q, write `U(Q)` for its total number of path observation uses across 141 states, and `n_j(Q)` for uses of the *named* qj. Then

`C_Q(a,b)/t = [U(Q)+a n_32(Q)+b n_34(Q)]/141.`

This is original named-observer incidence, not a cost on a lossy partition quotient.

## Theorem 1 — Exact unrestricted Bellman value, all real nonnegative (a,b)

\[
\boxed{V(a,b)/t=\min\{296/141+a,\quad296/141+b,\quad298/141\}}
\]

or equivalently `141 V(a,b)/t = 296+min(141a,141b,2)`. Thus the global value depends on the two independent named surcharges only through their minimum. The phase threshold is `c=2/141`.

**Proof.** The inherited *unrestricted 228-action* diagonal theorem EC49FRR-B states for every real `z>=0`:

`V(z,z)/t=min(296/141+z,298/141).`

Its finite original-native Bellman proof uses exact anchors `z=0` and `z=2/141`. Four fully replayed named decision-tree witnesses have incidence vectors

| Original tree | First physical q | U | n32 | n34 |
|:--|--:|--:|--:|--:|
| A | 32 | 296 | 141 | 0 |
| A′ | 34 | 296 | 0 | 141 |
| B | 140 | 298 | 0 | 0 |
| B′ | 142 | 298 | 0 | 0 |

Let `m=min(a,b)`. Because each query-use incidence is nonnegative, every admissible original tree satisfies `C_Q(a,b)>=C_Q(m,m)>=V(m,m)`. Taking the infimum proves the lower bound `V(a,b)/t>=min(296/141+m,298/141)`. For `a<=b`, witness A attains `296/141+a`; for `b<=a`, witness A′ attains `296/141+b`. B attains `298/141` for every pair. Their minimum equals the lower bound. Therefore the formula is globally exact, without restricting the competitor trees. QED.

## Theorem 2 — ALL optimal first original physical observations

Set `c=2/141` and `m=min(a,b)`.

| Parameters | Exact complete set of first physical query IDs |
|:--|:--|
| `a=b<c` | {32,34} |
| `a<b,\ a<c` | {32} |
| `b<a,\ b<c` | {34} |
| `a=b=c` | {32,34,140,142} |
| `a<b,\ a=c` | {32,140,142} |
| `b<a,\ b=c` | {34,140,142} |
| `m>c` | {140,142} |

**Proof.** For all Q,
\[
C_Q(a,b)=C_Q(m,m)+\frac t{141}\big[(a-m)n_{32}(Q)+(b-m)n_{34}(Q)\big].
\]
Both summands of the increment are nonnegative. Theorem 1 says the global optima at (a,b) and (m,m) are equal. Therefore an optimal Q must (i) be optimal at (m,m), and (ii) have zero incidence for every *strictly more expensive* selected query. From EC49FRR-B, the exhaustive original diagonal first-query sets are {32,34} below c, {32,34,140,142} at c, and {140,142} above c. A first use of a named query occurs on all 141 state paths, so if `a<b`, q34 is excluded; if `b<a`, q32 is excluded. The listed remaining indices are attained by A, A′, B and B′ at their respective prices. At equality `a=b`, retain the inherited diagonal sets. QED.

## Theorem 3 — Three, and exactly three, universal price-incidence types suffice

A fixed menu of original native decision trees `{A,A′,B}` attains the full Bellman optimum for every `(a,b) in [0,infinity)^2`. No menu of **two** fixed complete deterministic trees can attain the value over the whole quadrant. Each fixed tree has cost affine in (a,b), while the global Bellman value has three open chambers with pairwise distinct gradients `(1,0)`, `(0,1)`, and `(0,0)`. To equal the value on each open chamber, an affine tree cost must agree with that chamber’s affine function throughout a nonempty open set. One affine function cannot equal two pieces with different gradients. Thus any universal fixed-tree menu requires >=3 members; the exhibited menu attains this minimum. B′ is a distinct tied named tree with the same price-incidence vector as B. QED.

## General min-coordinate lifting lemma

In any finite query-identification decision problem with k selected nonnegative cost surcharges `s_i`, suppose (1) the unrestricted diagonal optimum is `V(z,...,z)=min(L+Nz,H)` for every real z>=0; (2) for each i a feasible witness of base cost L makes exactly N normalized uses of selected query i and none of the other selected queries; (3) a feasible witness of cost H avoids every selected query. Then

`V(s_1,...,s_k)=min(L+N min_i s_i,H)`.

Proof is the same coordinatewise monotonic lower bound at `min_i s_i`, attained by the corresponding single-query witness or the avoiding witness. This lemma is *conditional* when transferred to other BRC families.

## Independent finite verification and reproducibility

All physical response vectors are reconstructed from the exact frozen 94-family raw original BRC master and root-profile CSV. Exact original data SHA256:
- master: `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`
- profile: `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`.

The attached verifier checks identity of all 228 original physical response vectors across two independently implemented data builders (with exact typed native root-key reindexing). Its unrestricted integer Bellman recursion ranges over all 228 physical observations for each subproblem and visits 13,063 substate masks at every one of seven rational price points, including both asymmetric chambers, the diagonal, threshold and constant chamber. The exact minimum and all tied *original* first physical query IDs are recorded in the attached machine certificate. These finite checks independently corroborate the phase diagram; the all-real conclusion is the proved analytic consequence of the inherited full diagonal Bellman theorem.

The original response and query mapping, P000 six-dimensional spatial basis, joint-relation/provenance semantics and source firewall are unchanged. This is named-observer *price sensitivity* of the finite original BRC decision problem, not a newly asserted physical dynamical law. No formal task CLAIM, Source Result, Review, or theorem admission is asserted.

**Next scientific question:** extend to three or more independently priced original named observations and determine whether the single-coordinate witness criterion still holds. If it fails, compute the genuine higher-dimensional incidence-Pareto hull from full original Bellman. Separately study negative but physically positive price surcharges `a,b>-1`, where the monotonic lower-bound proof is not available.
