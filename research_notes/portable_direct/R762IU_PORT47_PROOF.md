# R762IU — Six-axis k=0 Port–Euler compression to at most 47 events

Date: 2026-11-22 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FINITE_CONSTRUCTION_CHECKED_IN_5_DISJOINT_RANGES / NOT_REVIEWED.
Scientific input pin: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\` (unchanged). Predecessor: R762IT, Draft PR #2947 @ \`9687b5b5bf25c68cbc101dc6645e808bfcd1cab2\`; dependent on R762IR/R762IS triangle-redundancy reductions and the k=0 ≤48 result. The model is a **composite** six-axis Port–Euler observer; no native signed P000 Cell/force/time/rotation lift is asserted.

## Result

Let A={0,…,5}. Ports are the 15 unordered 2-subsets of A, and supports are the 20 unordered 3-subsets. Each event of support S chooses one edge between two Ports contained in S. A legal closed history is a connected even-degree multigraph on the set V of its positive-degree Ports, with any specified initial p∈V. Write N_p(n)>0 for existence with support-count vector n.

**Theorem (k=0 uniform 47, computer-assisted).** For every vector n∈{0,1,2,3}^{20} having a legal closed realization with active-Port set V and designated starting Port p, there is h≤n satisfying N_p(h)>0, the **same** active set V, the **same positive support types**, and h_S≡n_S (mod 2) for every S, with

\[
\sum_S h_S\le47.
\]

Deleted same-support event pairs can be reinserted along a surviving edge of that support. The statement strengthens the author-proved R762IT bound of 48 by one event; optimality is open.

## Proof and complete finite reduction

Use R762IT to obtain a witness of length at most 48. Only the exactly-48 case needs further reduction. Let t,d,s,z be the numbers of triple-, double-, single- and zero-multiplicity supports. Then

\[
t+d+s+z=20,\quad 3t+2d+s=48,\quad t-s-2z=8.
\]

If t≥11, the R762IR triangle-redundancy lemma (or immediate two-active-Port reduction) removes a same-support event pair and finishes at 46. If t≤10 the **complete** list of possible terminal histograms is

| t | d | s | z | meaning |
|---|---|---|---|---|
| 8 | 12 | 0 | 0 | eight triple supports |
| 9 | 10 | 1 | 0 | nine triple, one single |
| 10 | 8 | 2 | 0 | ten triple, two singles |
| 10 | 9 | 0 | 1 | ten triple, one *absent* support |

The fourth case is easy to overlook and is explicitly included here. In any case where a triple support has only two active Ports, its three events all use the unique edge, and replacing three by one preserves degrees mod 2, connectivity, support presence and the active set. If one of the t full-Port triangles is not connectivity-essential among the triple-support triangles, use the established R762IR GF(2) redundancy reduction. Therefore it remains to treat **all-essential** full-Port triangle families.

All 20 supports are present in the first three rows. Two inactive Ports sharing an axis would both lie in one of the present support triangles, preventing that support from having any legal edge. Hence the inactive Port set is a matching of K6; there are exactly **76** matchings (including empty). The exhaustive support-triangle component checker identifies:
- t=8: exactly 4,920 all-essential families, partitioned into **16** S6-permutation orbits.
- t=9: exactly 240 all-essential families, represented by support bitmasks 967489 and 971528 (orbit sizes 180 and 60; the same representatives as R762IT).
- t=10: exactly 6 all-essential families, each a complete axis star. A fully active ten-triangle axis star covers every one of the 15 Ports.

For each t=8 or t=9 orbit representative and every matching inactive set, for each choice of the single support in t=9, a finite exact witness checker reduces **a fixed triple support** from multiplicity 3 to 1, leaving all other multiplicities unchanged. For t=10 with two singles it checks all unordered choices of two nonstar single supports and all 76 matchings. For t=10 with one absent support, all star triangles being fully active forces V to be *all 15 Ports*, so it suffices to check the ten possible missing nonstar supports with no inactive Ports. The same chosen triple is reduced in each representative family.

The complete explicit finite parameter domain is therefore

| terminal type | checked 46-event witness cases |
|---|---:|
| t=8, s=0, z=0 | 16×76 = 1,216 |
| t=9, s=1, z=0 | 2×11×76 = 1,672 |
| t=10, s=2, z=0 | C(10,2)×76 = 3,420 |
| t=10, s=0, z=1 | 10 |
| **Total** | **6,318** |

In every case a nonnegative integer allocation x_{S,e}∈{0,1,2,3} across the three allowed edges of support S is produced, and an **integer-only independent witness verifier** checks the exact per-support counts, no edges incident to forbidden Ports, positive even degree for every required Port, zero degree for other Ports, and connectivity of the active graph. The candidate constructor uses SciPy/HiGHS integer linear optimization with iterative violated connectivity cuts, but correctness depends only on the verified integral witness, not the optimizer's claimed feasibility. A connected even-degree graph admits an Euler circuit from each p∈V.

All 6,318 cases passed in five disjoint local batches on 2026-11-22, using the same finite construction/checker logic as the accompanying Python script. No arbitrary code-execution sandbox or remote CI is part of the mathematical argument. The exact ranges and hashes of their verified witness streams are in the evidence record. No formal Lean verification or independent mathematical review has occurred.

## Scope and next work

This establishes the author-side k=0 47-event upper bound **under the frozen composite observer and the cited antecedent reduction lemmas**. All k>0 cases retain the separately reported broader 54-event upper bound; neither number is a native signed P000 dynamical theorem. Next: study 47-event terminal histograms and a possible 46-event uniform bound, then analyze four-event critical supports k>0 and the signed native TRIADIC_CLOSURE_E transport.

Role: independent portable mathematics, not a new shared TASK CLAIM. Native task state last read 2026-11-22 06:21:48 UTC: task RS-X6-TRIADIC-CLOSURE-DYNAMICS, no live actor/claim, dispatch=NEEDS_DISPATCH, execution_authorized=false. No protected PROGRESS/Result/Review is asserted.
