# R5 — complete optimizer-family cut support and three-observation tomography (K ≥ 214)

Date: 2026-11-14. **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.** Frozen scientific input: `435e77af0d180eac32bd1f9c4c464bc4010b7551`.

This result concerns the **derived 954-event, integer one-dimensional, radius-two, event-index center observer**. No native X6/three-dimensional-slice state, signed paths, BRC provenance, or original certificate is erased or retyped by the conclusion.

## Definitions and background theorem

The ordered 954 events have 28 original disjoint (separation at least 5 by starting event index) length-three gaps, indexed `I={0,...,27}`. Under a closure mask `B⊆I`, each selected gap is shortened from 3 to 2, preserving event indices. A set of exactly K indexed centers is feasible if every event is within distance two of a center, and has cost equal to the sum of its distances to its nearest center.

Write `Opt_B(K)` for the **entire set-family** of feasible K-center subsets minimizing the integer cost `J_B(K)`; write `N_B(K)=|Opt_B(K)|`.

Previously proved, at every K≥214, the minimum cost is independent of B. For each all-closed feasible center set S, the nonadjacent-gap principal-filter theorem supplies a unique least enabling mask `M(S)` with

`S∈Opt_B(K) ⇔ S∈Opt_I(K) and M(S)⊆B.`

This uses cost constancy across feasible closures, and is stronger than comparing only the optimum values. At the 954-event endpoint K=954 the statement remains valid by direct observation.

## Theorem 1: exact global support from only 29 endpoint spectra

Fix K≥214 and put `D_i(K)=N_I(K)-N_{I\{i}}(K)`. Since `Opt_{I\{i}}(K)⊆Opt_I(K)`, each D_i is a nonnegative integer and

`D_i(K)>0 ⇔ there exists S∈Opt_I(K) with i∈M(S).`

Consequently `E(K)={i:D_i(K)>0}` is the **unique minimal coordinate support** for the complete optimizer-family observer at K: for every closure B,

`Opt_B(K)={S∈Opt_I(K): M(S)⊆B∩E(K)}.`

Every coordinate in E(K) is genuinely necessary because changing it in the background `I\{i}` strictly enlarges the family. Every other coordinate is globally inert for this declared observer at that fixed budget.

Exact min-cost/tie-count path DP at the all-closed endpoint and at all 28 one-cut-deleted endpoints, for K=214..315, together with previously published K≥315 full optimizer-family invariance, gives:

| Budget K | Exact effective cut set E(K) | Distinct complete optimizer families |
|---|---|---:|
| 214–221 | {3,8,9,10,27} | 32 |
| 222 | {27} | 2 |
| 223–291 | {25,27} | 4 |
| 292 | ∅ | 1 |
| 293–314 | {15,17} | 4 |
| 315–954 | ∅ | 1 |

This improves earlier 17-variable family bounds to at most **five bits per budget** across K≥214, and to **eight bits for the joint entire-budget observer**, with the exact scope above.

## Theorem 2: exact Möbius cohorts and count-level decoding

For a fixed K with effective bits E=E(K), let `a_M(K)` be the number of fully closed optimal K-center sets whose least enabling mask is exactly `M⊆E`. Then

`N_B(K)=Σ_{M⊆B∩E} a_M(K)`

and Möbius inversion on E gives

`a_M(K)=Σ_{D⊆M}(-1)^{|M|-|D|}N_D(K).`

The executable verifier evaluates all 32 closure masks of E={3,8,9,10,27} through K=221; both masks of {27} at 222; four masks of {25,27} through K=291; and four masks of {15,17} through K=314. It checks every coefficient is nonnegative, exact reconstruction of all computed N_B, and that the positive coefficient support matches the independently inferred E(K). The number of positive least-enabling-mask cohorts is 20 at K=214..219, 18 at K=220, 10 at K=221, 2 at K=222, 4 at K=223..290, 3 at K=291, 1 at K=292, and in the later interval as shown by the existing two-bit theorem.

The exact scalar counts `N_B(214)` are **all different** over the 32 choices of five effective bits. Likewise `N_B(223)` differs over all four choices of {25,27}, and `N_B(294)` differs over the four choices of {15,17}. These are integer comparisons in the verifier, not floating-point estimates.

Thus the three scalar observations

`(N_B(214), N_B(223), N_B(294))`

**uniquely recover all eight bits** in

`U={3,8,9,10,15,17,25,27}`.

Two original 28-bit closure configurations have the same triplet **if and only if** they have the same complete optimizer families for every 214≤K≤954. Under the uniform closure prior, the observable has exactly `2^8=256` distinct signatures, with exactly `2^20=1,048,576` original configurations per signature; its Shannon entropy is **8 bits**. The information quotient is precise for this declared complete family of derived observers and budgets.

## Exact computation and finite certificate

Program: `VERIFY_R5_GLOBAL_OPTIMIZER_TOMOGRAPHY.py`, Python standard library, unbounded integer arithmetic. Reconstruction starts from the pinned 15-term subset-sum coefficients and verifies 538/298/229 number pools, 954 events, coordinate extent 1065, 28 length-three gaps and gap-index separation 5. The shortest-path DAG counts optimal center index sets with min-plus costs and exact integer tie sums; every feasible indexed center set is represented once by its increasing selected indices.

The local execution printed `PASS_EXACT_R5_GLOBAL_OPTIMIZER_TOMOGRAPHY`, with 102 budget rows (214..315), all 29 endpoint spectra, 32 five-bit spectra, and the exact Möbius/count-injectivity assertions. The generated full JSON is 28,337 bytes, SHA-256 `261b3945e9efdcf1a3f4be215a42b19bccac3fee9e06e2ef3bd3eba4dc279f41`. The script prints this self-contained full JSON deterministically for independent reproduction.

Reference exact counts: `N_all(214)=4573020854769248525038387200000`; `N_all(292)=247939829006869892620615680`. Previously established two-cut counts for K=293..315 are used as a cross-reference. The exhaustive 28-bit space is certified algebraically from the principal-filter theorem and finite exact spectra, not by enumerating 268,435,456 configurations individually.

Scientific input is the immutable commit above. Relevant preserved source: `research_notes/portable_direct/r5_requirement_zeta_20261114/RESEARCH.md` and `VERIFY_R5_REQUIREMENT_ZETA.py` on PR #2412 (commit `a242de1dbb59cd6df8cfced61f1405e8c09d3f7c`). Earlier minimum-cost classification and high-budget invariance: Draft PR #2379. The result remains author-side, **NOT_REVIEWED**. No formal Task, CLAIM, Result, or independent Review is represented by this independent research branch.

## Next questions

1. Compute the exact max-new/min-old center replacement distance at K=214..291 for the five-, one-, and two-bit bands, preserving the min/max quantifier order and the full indexed center-set observer.
2. Determine the least number of *scalar budget observations* needed to reconstruct the eight-bit quotient; three suffice here.
3. Compare these observer-specific information residuals with native X6/BRC path and source-provenance observers via explicit preservation mappings, without assuming the 1D quotient is native lossless.
