# Research Taskbook — Post-audit hyperbola/Joukowski independent replication

Task-ID: `RS-NATIVE-FILAMENT-POSTAUDIT-HYPERBOLA-JOUKOWSKI-INDEPENDENT-REPLICATION`

Date: `2026-08-25`

Issuing Researcher-ID: `EM-FREE-NEPS-239A6D`

## Hard target

`POSTAUDIT_HYPERBOLA_JOUKOWSKI_CLOSURE_STATEMENT_STRENGTH_INDEPENDENTLY_VERIFIED_OR_NARROWED_OR_REFUTED`

## Input

Use only:

`research_inputs/NATIVE_FILAMENT_POSTAUDIT_HYPERBOLA_JOUKOWSKI_BLIND_PACKET_20260825.md`

The packet is statement-only.

## Researcher identity

Generate a fresh Researcher-ID on claim. Do not reuse `EM-FREE-NEPS-239A6D`, the #631 audit identity, or any identity that authored/reviewed PR #627 post-audit proofs.

## Independence wall

Before freezing the return, do **not** read:

- PR #627;
- branch `research/native-filament-generalization-theorem-package-20260824`;
- any file with names containing `HYPERBOLA`, `JOUKOWSKI`, `BOUNDARY_CLOSURE`, `357_ORBIT`, or corresponding package-specific checker on that branch;
- direct literature-audit opinions about proof correctness from the originating researcher.

The earlier blind audit #631 may be used only for the pre-existing fact that the original V2 base package was verified with narrowing. Do not use #631 as proof of the new post-audit claims.

## Required work

For every claim group H1, H2, J1, J2, C1, C2:

1. independently prove it, or produce a concrete counterexample;
2. state all needed field/prime/domain hypotheses explicitly;
3. test boundary cases (`q=2`, divisors of `B`/`s`, slope collisions, small `s`, nonprime `2s+-1`);
4. distinguish exact theorem from computational pressure;
5. construct an independent checker rather than reusing source scripts;
6. actively search for accidental equivalences that make a statement weaker/stronger than written.

## Required return

Write:

`research_returns/NATIVE_FILAMENT_POSTAUDIT_HYPERBOLA_JOUKOWSKI_INDEPENDENT_REPLICATION_RETURN_20260825.md`

The return must contain:

- fresh Researcher-ID;
- independence attestation;
- verdict matrix for H1/H2/J1/J2/C1/C2 using `VERIFIED_EXACT`, `VERIFIED_WITH_NARROWING`, `REFUTED_COUNTEREXAMPLE`, or `DEPENDENCY_GAP`;
- independent derivations;
- finite pressure-test log;
- any counterexample/minimal failure mode;
- exact final theorem wording after narrowing;
- final hard-target verdict.

## Stop rule

After freezing the return, stop. Do not read the withheld #627 source proofs/checkers and do not merge/promote anything automatically.
