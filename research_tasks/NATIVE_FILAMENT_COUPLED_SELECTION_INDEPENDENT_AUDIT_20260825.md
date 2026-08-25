# Taskbook — Native filament coupled-selection theorem independent audit

Research task: `RS-NATIVE-FILAMENT-COUPLED-SELECTION-INDEPENDENT-AUDIT`

Date: `2026-08-25`

Owner branch: `audit/native-filament-coupled-selection-20260825`

Input packet:

`research_inputs/NATIVE_FILAMENT_COUPLED_SELECTION_BLIND_AUDIT_PACKET_20260825.md`

Hard target:

`NATIVE_FILAMENT_COUPLED_SELECTION_STATEMENT_STRENGTH_INDEPENDENTLY_VERIFIED_OR_NARROWED_OR_REFUTED`

## 1. Independence wall

Until the audit return is frozen, DO NOT read:

- branch `research/native-filament-generalization-theorem-package-20260824`;
- PR #627;
- any file whose path begins with `NATIVE_FILAMENT_ODD_CURVATURE_`, `NATIVE_ODD_CURVATURE_`, `NATIVE_ODD_SECTOR_`, or `NATIVE_FILAMENT_LEGENDRE_DUAL_` outside the supplied packet;
- any checker written specifically for the generalization package;
- source proof comments in PR #627.

The audit must derive proofs/counterexamples independently from the statement packet and standard mathematics.

Native parent facts explicitly listed in Section H of the packet may be used as frozen inputs; do not reopen their source proofs.

## 2. Required audit rows

Audit every row A1--I in the supplied packet.

For each row return exactly one of:

- `VERIFIED_EXACT`;
- `VERIFIED_WITH_NARROWING`;
- `REFUTED_COUNTEREXAMPLE`;
- `DEPENDENCY_GAP`.

A row cannot be marked verified merely because finite tests pass.

## 3. Proof obligations

Priority order:

1. E: complete breaker classification;
2. A/H: sector-count/curvature provenance and native selection corollary;
3. D/F: dual-parabola tangent/value-set coupling;
4. C: finite quotient cardinality/injectivity;
5. G: CRT basin and asymptotic/profinite phase;
6. B: recurrence/curvature formulas;
7. I: independent primality replay.

For E/F, derive the finite-field formulas independently; using standard order-2 cyclotomic numbers is allowed if the exact normalization is checked.

For D, explicitly check all signs, parity conventions, determinant factors, and the distinction between fixed-chirality and union-over-chirality discriminants.

For G3, identify exactly which analytic theorems are invoked and verify that the quadratic characters are nonprincipal in the no-break residue classes.

For G4, define the metric precisely and prove the Hausdorff lower bound rather than inferring it from box dimension alone.

## 4. Counterexample pressure tests

Mandatory pressure tests:

- B values divisible by q;
- M=2 and even composite moduli in C;
- q<=k-1 slope-collision boundary in D;
- B=1,3,5,7,15,27,39,51;
- k=3,4 versus k>=5;
- negative/zero H values where relevant;
- ordinary-integer versus profinite realization in G4;
- tiny prime exceptions involving 2 or3 in prime statements.

Do not silently extend any theorem beyond its quantified domain.

## 5. Independent computation

You may write new scripts from scratch.

For finite rows, exhaust small grids where feasible:

- odd B<=99;
- primes q<=101;
- k<=10;
- moduli M<=60.

Computational agreement is supporting evidence only; exact rows still require proof.

For witness I, independently verify all 12 values using a deterministic method valid on the displayed numerical range.

## 6. Prior-art handling

This audit is primarily mathematical correctness, not novelty.

If a supplied statement is immediately subsumed by a standard named theorem, record that in a `PRIOR_ART_NOTE` field but still verify the specialization.

Do not claim external novelty.

## 7. Return file

Freeze the audit at:

`research_returns/NATIVE_FILAMENT_COUPLED_SELECTION_INDEPENDENT_AUDIT_RETURN_20260825.md`

Required sections:

1. Audit metadata / input hash;
2. Verdict matrix A1--I;
3. Independent proofs or counterexamples;
4. Pressure-test log;
5. Witness-I primality certificate/replay description;
6. Dependency graph;
7. Exact list of narrowed statements, if any;
8. Final verdict:
   - `PACKAGE_VERIFIED`;
   - `PACKAGE_VERIFIED_WITH_NARROWING`;
   - `PACKAGE_REFUTED`;
   - `PACKAGE_INCOMPLETE`.

## 8. Stop condition

After freezing the return, stop. Do not read PR #627 proofs for comparison unless a later Driver/user instruction explicitly opens post-audit comparison.