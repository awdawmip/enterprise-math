# X6 signed triadic BRC — all-m feasibility and signed degree multiplicity

Date: 2026-11-14. Status: **AUTHOR-PROVED / INDEPENDENT EXACT INTEGER CHECK PASS / UNREVIEWED / NOT_ADMITTED**.

Parent scientific objective: `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. This is bounded author-side portable evidence, **not** a current winning CLAIM, Native semantic PROGRESS, Result, Driver acceptance, or native benchmark completion. Native role identity / activity ownership for this actual invocation was not reauthenticated; do not attribute this new unit to a prior owner's SID, Researcher or RA. Logical research lane requested by owner: `chatgpt-research-onhour-enterprise-math-20260923`, distinct from maintenance lane.

## Exact source and relevance

- Existing actual consumer: `experiments/x6_triadic_decomposition_brc_v2_20260906/check_triadic_decomposition_brc.py`, observed current-main Git blob `5d0f2cb88a0d4e437b5025e9050e3044f7831cd4`, 155 lines. Its `greedy_decompose` and `formula_signed_ordered` implement the exact objects treated here.
- Frozen scientific premises retained from the Task: Source P000 V5 / centered signed X6 baseline `59538f585d037d09ef687b28715c4bc1a3f9fe03`, pre-rebase comparison `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. Global P000 V4 remains distinct from Source V5.
- The existing consumer exhaustively checks degree feasibility only through event count `m<=4`, and signed-degree formula for one and two events. The following universal proofs explicitly discharge those statements for all nonnegative integer degrees and every finite event count. They do not replace native signed-Cell event admissibility, temporal update, geometric closure, or the separate R061/R062 two-generator positive-sector bridge.
- This is a type-preserving combinatorial proof about **three distinct axis labels per triadic event**. It assumes that this labelled-event alphabet is the mathematical object being counted; event feasibility in a more restrictive native transition system requires its own evidence.

## Theorem 1: exact existence of ordered triadic decompositions

Fix six distinguishable axes and let `D=(D_0,...,D_5)` be a vector of **nonnegative integers**. An ordered decomposition into `m` triadic events is a sequence `(S_1,...,S_m)`, where each `S_j` is a three-element subset of `{0,...,5}`, and each axis `i` occurs in precisely `D_i` of those subsets. Repetitions of a triad across distinct events are allowed.

For every integer `m>=0`, such a decomposition exists **if and only if**

`sum_i D_i = 3m` and `max_i D_i <= m`.

**Necessity:** each event has three distinct axes, adding exactly 3 to total degree and at most 1 to each degree. For `m=0`, the only admissible vector is the zero vector.

**Sufficiency and a terminating construction:** assume `r>0`, `sum D_i=3r`, `D_i<=r`. Let `P={i:D_i=r}`. Because the sum is exactly `3r`, `|P|<=3`. At least three coordinates are positive, since two positive coordinates could contribute at most `2r`. Therefore select a three-element set `S` of positive axes containing `P`; the repository's greedy rule selects the remaining highest-degree positive axes, with deterministic axis-index ties. Subtract 1 from each degree indexed by `S`. The new degrees are nonnegative and sum to `3(r-1)`; every unselected coordinate was strictly below `r`, and every selected one was at most `r`, so the new maximum is at most `r-1`. Repeat to `r=0`. This produces a valid decomposition for **all** `m`; there is no finite-event cutoff in the argument.

## Theorem 2: exact signed ordered-event count at any m

For each axis `i`, prescribe nonnegative signed incidence counts `d_(i,+)` and `d_(i,-)`; write `D_i=d_(i,+)+d_(i,-)`. A signed triadic event chooses three **distinct** axes and one sign for each chosen axis. Let `U(D)` denote the number of ordered **unsigned** triadic-event sequences with degree vector `D`. The signed count at the exact 12-slot degree vector `d` is

`N_signed(d) = U(D) * product_{i=0}^5 binom(D_i,d_(i,+))`.

This is zero if the feasibility conditions above fail (or signed counts are inadmissible). To prove it, first fix any one unsigned ordered triadic sequence of degree `D`. Axis `i` appears at `D_i` distinguishable event positions; choose exactly `d_(i,+)` of them to be positive, the rest negative. Choices across axes are independent, and each assignment produces one unique signed ordered sequence. Thus every unsigned sequence has exactly the stated product number of signed refinements. Summing over `U(D)` underlying sequences proves the identity without a bound on `m`.

An exact positive-integer recurrence for `U` is `U(0,...,0)=1` and, for nonzero `D`, `U(D)=sum_{S subset {0..5}, |S|=3, D_i>=1 for i in S} U(D-1_S)`; this is the original consumer's recurrence. A signed **degree vector** is not a signed **net displacement**: identifying opposing signs at the endpoint requires a separately specified pushforward and must not be silently performed during this count.

## Executed exact integer certificate

Companion standalone checker:

`research_checks/X6_TRIADIC_BRC_ALL_M_FEASIBILITY_SIGN_MULTIPLICITY_20261114.py`

It was actually executed in this invocation using Python exact integers and returned exit code 0:

```text
PASS_X6_TRIADIC_BRC_ALL_M_PROOF_CORROBORATION
admissible_degree_vectors_m0_to_6 [1, 20, 141, 580, 1751, 4332, 9331]
signed_degree_census_m1_to_3 [(1, 160, 160), (2, 5284, 25600), (3, 73580, 4096000)]
uniform_degree_two_m4 (85, 1860)
uniform_degree_three_m6 (550, 297200)
fixed_signed_degree_m6 216658800
arithmetic=exact_integers; coverage=finite; universal_proof=separate
```

Coverage details:

1. Enumerated **all** nonnegative six-component degree vectors summing to `3m` and satisfying each `D_i<=m`, for `m=0..6`; reconstructed a greedy ordered decomposition and compared all six degrees without failure. This extends original finite checks to `m=5,6`.
2. Independently enumerated all `160^m` signed ordered event words for `m=1,2,3` by an exact 12-slot-degree dynamic census. For each of `160`, `5284`, and `73580` distinct degree vectors respectively, compared its count to the exact formula and obtained zero mismatches.
3. Computed `U((3,3,3,3,3,3))=297200` by the ordered recurrence at `m=6`; independently enumerated the `C(25,6)` multisets of six triad types, found `550` admissible multisets, weighted each by `6!/prod multiplicity!`, and obtained the same `297200`.
4. For signed counts `d_(i,+)=2`, `d_(i,-)=1` for all six axes, the sign factor is `3^6=729` and `N_signed=297200*729=216658800`. Independent four-event multiset recalculation also reproduces the original `85` unordered, `1860` ordered counts for `D=(2,...,2)`.

The universal conclusions rely on the explicit induction and bijective refinement proof; finite enumeration corroborates and guards the implementations. This checker is independent of the repository's original 155-line checker, which **was not rerun** in this unit. Original per-Cell native benchmark, existing accepted R062 and R063 results, frozen foundation and Source review status are unchanged.

## Consumer disposition and continuation

The actual inspected `check_triadic_decomposition_brc.py` is **KEEP**: its existing mathematical recurrence/greedy/sign refinement rules are supported by the all-`m` proofs. These proofs upgrade the demonstrated scope of that consumer from finite inspection to an arbitrary finite number of labelled triadic events; they do not authorize interpreting signed-degree counts as endpoint multiplicities or substituting them for original Native temporal event experiments.

Next exact scientific work: trace a real consumer that passes `N_signed(d)` or R061/R062 two-generator positive-sector BRC to a **signed six-axis endpoint** or full native Cell, preserving the 12-slot degree, the 6-slot net displacement, event order and selected axes/signs. If found, inspect its exact line-level coercion and test a minimal typed witness; otherwise retain `LP011/LP019 UNRESOLVED_PROVENANCE` and continue bounded source coverage. The 28-LP dependency closure and independent Driver `REQUEST_REVISION` remain open.

Source continuity: original Research lineage cited only as historical evidence (`EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`); it is not an authenticated capability for this invocation. Earlier exact read request `onhour-20261114-0211-own-continuation-read-v1` is `SUCCEEDED` with `execution_authorized=false`. New Source continuation read `onhour-20261114-03-x6-read-continuation-v1` was `QUEUED` at last observation. Sites recovery with only a bridge `conversation_id` was rejected as missing session/start selector. No CLAIM, RUN open, semantic PROGRESS, RA update, upload or request replay was performed. Activity attribution for this invocation remains `REGISTER_PENDING / SYNC_DEBT` until this actual lane's authentication and registration are independently established.

Preserve: original task/publication pins and original already-saved X6 scientific frontier, historical owner work, signed/relative type distinction, original test coverage, pending requests, and active scheduler settings.
