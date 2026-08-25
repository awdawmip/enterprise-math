# CBRC F5B — Positive-Separation Regularity Admission Driver Review

Status: `ACCEPTED_WITH_RESTRICTED_WORKING_EXTENSION_ADMISSION`
Date: `2026-08-25`
Driver-ID: `EM-DVR-CBRC-F0-7C3A21`
Task-ID: `RS-CBRC-F5B-POSITIVE-SEPARATION-REGULARITY-AXIOM-ADMISSION`
Taskbook source: `11c5c651df54cf0117f936d5dbf421e37b9b7a34`
Accepted owner branch: `research/cbrc-f5b-positive-separation-regularity-axiom-admission`
Accepted owner head: `e7208733eab81119941552e38987b75dd3fb9a44`
Researcher-ID: `EM-CBRCF5B-B8E421`

## 0. Driver verdict

`F5B_ACCEPTED_WITH_SCOPE_NARROWING`.

Accepted primary research verdict:

`F5B_ADMIT_RESTRICTED_FREE_FIBER_POSITIVITY_ONLY`.

Hard target:

`POSITIVE_SEPARATION_REGULARITY_AXIOM_ADMISSION_STATUS_CLASSIFIED = ACCEPTED`.

Admit only to the Coherent-BRC working extension:

`FREE_PROJECTION_ZERO_SEPARATION : pi(z) != 0 => q(z) > 0`.

Do not promote this rule to `CANONICAL_FOUNDATION`.

## 1. Publication-liveness / evidence

The pre-math gate passed. The frozen stamp records:

- `phase = STARTED_BEFORE_MATH`;
- `admission_verdict = null`;
- `math_source_read_before_stamp = false`;
- exact taskbook source and whitelisted mathematical refs.

The final owner branch is 10 commits ahead of the taskbook source and contains all six required artifacts. Final owner head is `e7208733eab81119941552e38987b75dd3fb9a44`.

## 2. Source firewall

`TARGET_LEAK_AUDIT_PASS` is accepted.

Before raw freeze the execution used only:

1. `research_inputs/CBRC_F5B_POSITIVE_SEPARATION_REGULARITY_ADMISSION_PACKET_20260825.md@1cdfb6b1f8fb0806507c9a4ce72278461246034b`;
2. the accepted F4 positive-separation rank-one boundary by exact blob identity `54fefbc20ad485ce3a7cab95ca6146f6c711b7c1`;
3. `driver_reviews/CBRC_F5AR_INDEPENDENT_BRANCH_ONTOLOGY_AXIOM_ADMISSION_DRIVER_REVIEW_20260825.md@0c983a5c98456a4d9c4b6be29b9a988631984842`.

No downstream coherent-wave, R063/R064/R065/FQ, external quantum/wave, rank-two target, complex/quadratic carrier, phase group, norm, inner product, quadratic/power law, Hadamard/Fourier/splitter target was used as a mathematical premise or selector.

## 3. Accepted regularity lattice

At the issued finitely generated torsion-free-rank-one scope, write `C` with canonical retraction `pi:C->Z e` and finite kernel `T`, and define

`f(n)=min{q(z): pi(z)=n e}`.

Accepted relations:

`P0 => P1 <=> P2 => P3`.

Here:

- `P0`: all nonzero coefficient states have positive scalar;
- `P1`: every state with nonzero old/free projection has positive scalar;
- `P2`: every nonzero finite fiber has positive minimum envelope;
- `P3`: only embedded copies `n e` are required positive.

The equivalence `P1 <=> P2` is accepted only at finite-fiber scope. P1 remains intrinsically meaningful without finiteness; P1 need not imply a positive infimum over an infinite fiber.

`P4` active-branch positivity and `P5` elementary-output positivity are typing-restricted and do not replace P1/P2 globally.

Accepted strictness witnesses include:

- P1 without P0 via zero-valued pure-kernel states;
- P3 without P1 via a zero-valued torsion-labelled state in a nonzero free fiber.

## 4. Minimal serious local regularity

The accepted F4 contradiction mechanism needs exactly an envelope rule strong enough to forbid the periodic zero forced by a non-signed-permutation free block.

For finite torsion, P2 is sufficient, and P1 is equivalent to it. Full P0 is unnecessary because positivity on pure-kernel states is not used.

The report also identifies weaker proof-side global conditions P6/P7 that defeat periodicity, but they are not admitted because they are arithmetic shape constraints on the already-formed envelope rather than local zero-separation semantics.

Therefore the preferred local/intrinsic working-extension rule is P1:

`FREE_PROJECTION_ZERO_SEPARATION : pi(z) != 0 => q(z) > 0`.

## 5. Insufficiency below P1/P2

The exact period-6 rank-one witness is accepted:

`q(n e)=h(n mod 6)` with

`h=[0,1,1/4,3/4,1/4,1]`,

and

`A=[[-4,-3],[-3,-2]]`.

Then `det(A)=-1`, `A` is not signed-permutation, and exact residue checking gives marked scalar conservation. Elementary outputs from `(e,0)` have nonzero old projections and positive scalars `1/4,3/4`, yet `q(6e)=0`.

Driver independently replayed the 36 residue pairs and confirmed zero mismatches.

Thus `A0 + P5` and elementary active-output positivity do not close rank one.

The uniform family `q_m(n e)=0 iff m|n` with `A_m=[[1,m],[m,1+m^2]]` further confirms that leaving a nonzero free-coordinate subgroup unprotected permits exact non-signed rank-one survivors.

## 6. Working-extension rank-one closure

Combine only the already admitted working-extension axiom A0 from F5AR with P1:

1. finite-fiber P1 gives P2;
2. accepted F4 then forces every rank-one free quotient block to be signed-permutation;
3. a signed-permutation first column has exactly one nonzero old-coordinate output;
4. A0 requires both elementary old-refining outputs to have nonzero old projection;
5. contradiction.

Therefore the following is accepted as a theorem of the explicit working extension:

`A0 + FREE_PROJECTION_ZERO_SEPARATION + BALANCED_REVERSIBLE_CONSERVATION => torsion_free_rank(C) >= 2`.

Status:

`WORKING_EXTENSION_THEOREM`.

This is not a theorem of native BRC alone and is not a Foundation promotion.

## 7. Conservativity / scope

P1 is accepted over P0 because:

- pure-kernel states may remain scalar-zero;
- exact signed cancellation to coefficient zero remains legal;
- canonical Path/N/Boolean BRC objects are unchanged;
- the rule is intrinsic in terms of the canonical retraction `pi`, not a chosen splitting;
- future enrichments incur only the obligation that states with nonzero old projection cannot have scalar zero.

## 8. Checker

Accepted pushed-checker evidence:

- checker blob `719a7f1820e4b6c9d495e2cdb83e77af4c6c64f1`;
- SHA-256 `8a472298db0b9270213f2deaf4180cadbe4fb8bb4c1d5fcecb6f2deaa7157895`;
- byte identity `PASS`;
- result `PASS`;
- check count `101`;
- mismatch count `0`;
- deterministic digest `668c57c8da749b33eac111420644ee27739cacd267b83b9903edfb7e0ab53f7e`.

General rank-one claims are accepted from theorem proofs, not bounded enumeration.

## 9. Successor authorization

The last known rank-lift gate is now closed at working-extension scope.

Freeze:

`A0_WORKING_EXTENSION_AXIOM_ADMITTED = true`.

`FREE_PROJECTION_ZERO_SEPARATION_WORKING_EXTENSION_AXIOM_ADMITTED = true`.

`TORSION_FREE_RANK_AT_LEAST_TWO_WORKING_EXTENSION_THEOREM = true`.

A rank-two carrier search may now be opened, but it must remain blind-forward and must not preselect complex numbers, quadratic integers, finite phase groups, rings, norms, inner products, square laws, Hadamard/Fourier/splitter matrices, or downstream wave structures.

The first rank-two successor should classify the minimal conservative additive carrier and inherited unary transport structure before any two-slot mixing/readout search.
