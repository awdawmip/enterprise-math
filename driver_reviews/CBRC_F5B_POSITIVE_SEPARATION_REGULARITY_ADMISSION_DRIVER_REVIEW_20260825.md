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

The pre-math gate passed. The frozen stamp records `phase = STARTED_BEFORE_MATH`, `admission_verdict = null`, `math_source_read_before_stamp = false`, and the exact taskbook/source refs. All six required artifacts exist at final owner head `e7208733eab81119941552e38987b75dd3fb9a44`.

## 2. Source firewall

`TARGET_LEAK_AUDIT_PASS` is accepted. Before raw freeze the execution used only the frozen F5B input plus the accepted F4 and F5AR boundaries. No downstream coherent-wave, R063/R064/R065/FQ, external quantum/wave, rank-two target, complex/quadratic carrier, phase group, norm, inner product, quadratic/power law, Hadamard/Fourier/splitter target was used as a mathematical premise or selector.

## 3. Accepted regularity lattice

At issued finite-torsion rank-one scope, with canonical retraction `pi:C->Z e` and envelope `f(n)=min{q(z):pi(z)=ne}`:

`P0 => P1 <=> P2 => P3`.

P1 is free-projection/fiber positivity; P2 is envelope zero separation. Their equivalence is accepted only for finite fibers. P4/P5 are typing-local and do not replace P1/P2 globally.

## 4. Minimal serious local regularity

The F4 contradiction needs an envelope rule strong enough to forbid the periodic zero forced by every non-signed-permutation free block. For finite torsion, P2 is sufficient and P1 is equivalent to it. P0 is unnecessarily strong because pure-kernel positivity is unused.

Weaker proof-side P6/P7 can also defeat periodicity but are global arithmetic envelope-shape conditions, not preferred local scalar-separation semantics. Therefore admit P1 as the intrinsic/local representative:

`FREE_PROJECTION_ZERO_SEPARATION : pi(z) != 0 => q(z)>0`.

## 5. Insufficiency below P1/P2

The exact period-6 witness is accepted:

`h=[0,1,1/4,3/4,1/4,1]`,
`A=[[-4,-3],[-3,-2]]`.

It has `det(A)=-1`, exact marked scalar conservation on all 36 residue pairs, nonzero elementary old projections and positive elementary outputs, but `q(6e)=0`. Driver independently replayed all 36 residue pairs with zero mismatches.

Thus `A0+P5` and elementary active-output positivity do not close rank one.

## 6. Working-extension rank-one closure

Combine admitted A0 with admitted P1:

1. finite-fiber P1 gives P2;
2. F4 forces every rank-one free quotient block to be signed-permutation;
3. such a first column has exactly one nonzero old-coordinate output;
4. A0 requires both elementary old-refining outputs nonzero;
5. contradiction.

Therefore accept:

`A0 + FREE_PROJECTION_ZERO_SEPARATION + BALANCED_REVERSIBLE_CONSERVATION => torsion_free_rank(C) >= 2`.

Status: `WORKING_EXTENSION_THEOREM`.

This is not native BRC/Foundation truth.

## 7. Conservativity

P1 leaves pure-kernel scalar-zero states legal, preserves exact signed cancellation, leaves canonical Path/N/Boolean BRC unchanged, and is intrinsic in the canonical retraction rather than a chosen splitting.

## 8. Checker

Accepted pushed-checker evidence:

- blob `719a7f1820e4b6c9d495e2cdb83e77af4c6c64f1`;
- SHA-256 `8a472298db0b9270213f2deaf4180cadbe4fb8bb4c1d5fcecb6f2deaa7157895`;
- result `PASS`;
- check count `101`;
- mismatch count `0`;
- digest `668c57c8da749b33eac111420644ee27739cacd267b83b9903edfb7e0ab53f7e`.

## 9. Successor authorization

Freeze:

`A0_WORKING_EXTENSION_AXIOM_ADMITTED = true`.

`FREE_PROJECTION_ZERO_SEPARATION_WORKING_EXTENSION_AXIOM_ADMITTED = true`.

`TORSION_FREE_RANK_AT_LEAST_TWO_WORKING_EXTENSION_THEOREM = true`.

A blind-forward rank-two carrier search is now authorized, but it must first classify the minimal conservative additive carrier and inherited unary transport structure. Do not preselect complex/quadratic systems, rings, phase groups, norms, inner products, square laws, splitter matrices, or downstream wave structures.
