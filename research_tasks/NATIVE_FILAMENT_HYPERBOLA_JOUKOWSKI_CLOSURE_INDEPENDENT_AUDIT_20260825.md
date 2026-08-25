# Research Taskbook — Native Filament Hyperbola/Joukowski Closure Independent Audit

Task-ID: `RS-NATIVE-FILAMENT-HYPERBOLA-JOUKOWSKI-CLOSURE-INDEPENDENT-AUDIT`

Date: `2026-08-25`

Hard target:
`HYPERBOLA_JOUKOWSKI_CROSS_ROUTE_STATEMENT_STRENGTH_INDEPENDENTLY_VERIFIED_OR_NARROWED_OR_REFUTED`

## 1. Input

Read only:

`research_inputs/NATIVE_FILAMENT_HYPERBOLA_JOUKOWSKI_CLOSURE_BLIND_AUDIT_PACKET_20260825.md`

before freezing the return.

## 2. Independence wall

Before return freeze, do not read:

- PR #627;
- branch `research/native-filament-generalization-theorem-package-20260824`;
- any proof notes or checker scripts created for the hyperbola/Joukowski/closure package;
- unpublished reasoning from the originating researcher.

The parent native-prime branch may be used only for already frozen base definitions if strictly required by a statement, but reconstructing the formulas directly from the packet is preferred.

## 3. Required method

Independently prove or refute every H1--H7 row.

Must include:

1. symbolic/algebraic derivation of H1/H2/H3;
2. independent finite-field pressure checks, not copied from source checkers;
3. explicit proof of H4 second-moment uniqueness or a counterexample;
4. direct reconstruction of q=3,5,7 C3 root/orbit patterns in H5;
5. independent verification of the H6 gate table at least through s=13 and proof of the general bounds;
6. independent proof or refutation of H7 unique boundary closure;
7. active search for scope mistakes involving q|s, q<=s, characteristic2, repeated tangent slopes, and unrestricted-prime versus breaker-coprime semantics.

## 4. Required verdicts

For H1--H7 assign exactly one:

- `VERIFIED_EXACT`;
- `VERIFIED_WITH_NARROWING`;
- `DEPENDENCY_GAP`;
- `REFUTED_COUNTEREXAMPLE`.

If narrowed, state the exact repaired theorem.

## 5. Required controls

At minimum pressure:

- odd primes q<=101;
- odd sector counts s<=99;
- both q=2s-1 and q=2s+1 when prime;
- native q=5,7,13 controls;
- K4 orbit decompositions at q=5,7,53;
- C3 lane roots at q=3,5,7 and at least one nonsaturating q>7;
- gate examples s=3,5,7,9,11,13.

Finite checks support but do not replace proofs.

## 6. Prior-art boundary

This task does not decide novelty. Classical use of Joukowski/Dickson maps, conic duality, finite-group orbits, Legendre symbols, and finite-field power sums is allowed.

## 7. Required return

Write:

`research_returns/NATIVE_FILAMENT_HYPERBOLA_JOUKOWSKI_CLOSURE_INDEPENDENT_AUDIT_RETURN_20260825.md`

containing:

- input hashes / audit head;
- independence attestation;
- H1--H7 verdict matrix;
- independent proofs/counterexamples;
- finite pressure-test log;
- exact narrowed statements if any;
- dependency graph;
- final hard-target line.

## 8. Freeze

Freeze the return before reading #627 or its proof/checker branch.

Keep any audit PR Draft; do not merge as canonical mathematics solely from this task.