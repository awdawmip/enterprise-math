# P008 mathlib audit framework

Status: `VERIFIED-RESEARCH`

## Purpose

This document records the separation between existing mathlib mathematics, Enterprise Math specializations, and possible upstream candidates. The audit is intentionally conservative: finding that a P008 result is already in mathlib narrows our novelty boundary and is treated as progress.

The current formal audit is pinned to mathlib commit `87adeaebd370a3b6a41ac4f044fddd4bf81803ad` and its matching Lean toolchain `v4.33.0-rc2`. A later audit may update the pin, but claims below refer to this inspected snapshot unless stated otherwise.

## Classification

Each result is assigned one status:

- `MATHLIB_EXISTING`: already represented by mathlib APIs or theorems.
- `MATHLIB_DERIVED`: follows directly from existing mathlib structures but is not currently being treated as a distinct upstream theorem.
- `ENTERPRISE_SPECIALIZATION`: an application of general mathematics to Enterprise Math definitions or semantics.
- `UPSTREAM_CANDIDATE`: general reusable mathematics for which the current audit has not found an equivalent mathlib theorem. This is provisional until broader upstream review succeeds.

## Detailed audit

| Topic | Status | Mathlib evidence / Enterprise Math action |
| --- | --- | --- |
| Natural-number integer nth root | `MATHLIB_EXISTING` | Reuse `Nat.nthRoot`; do not define a parallel Lean root primitive. |
| Root adjunction | `MATHLIB_EXISTING` | `Nat.le_nthRoot_iff` gives `a ≤ Nat.nthRoot p b ↔ a^p ≤ b` for `p ≠ 0`. |
| Exact root interval characterization ingredients | `MATHLIB_EXISTING` | `Nat.pow_nthRoot_le`, `Nat.lt_pow_nthRoot_add_one`, and `Nat.nthRoot_eq_of_le_of_lt`; Enterprise Math exposes T001 as a thin project theorem. |
| Exact recovery of perfect powers | `MATHLIB_EXISTING` | Reuse `Nat.nthRoot_pow`. |
| Perfect-power recognition | `MATHLIB_EXISTING` | Reuse `Nat.exists_pow_eq_iff'` and related lemmas. |
| Galois connection | `MATHLIB_EXISTING` | Reuse `GaloisConnection`; no Enterprise-specific substitute. |
| Reductivity of `l ∘ u` | `MATHLIB_EXISTING` | `GaloisConnection.l_u_le`. |
| Monotonicity of `l ∘ u` | `MATHLIB_EXISTING` | `GaloisConnection.monotone_l_comp_u`. |
| Idempotence of the induced projection | `MATHLIB_EXISTING` | `GaloisConnection.l_u_l_eq_l` supplies the core equality directly. |
| Fixed points versus image of the lower adjoint | `MATHLIB_EXISTING` | `GaloisConnection.exists_eq_l` already characterizes the image/fixed-point condition. |
| Composition of adjoints | `MATHLIB_EXISTING` | `GaloisConnection.compose` gives reverse composition of right adjoints. |
| Transfer of a commuting square across adjoints | `MATHLIB_EXISTING` | `GaloisConnection.u_comm_of_l_comm` and `l_comm_iff_u_comm`. This absorbs the general mother theorem behind the P008 scale argument. |
| Natural-number multiplication / floor division adjunction | `MATHLIB_EXISTING` | `Nat.galoisConnection_mul_div` for a positive multiplier. |
| Integer root as an internally exact Enterprise Math state operation | `ENTERPRISE_SPECIALIZATION` | Foundational interpretation belongs to Enterprise Math, not mathlib. |
| `C_p(n) = Nat.nthRoot p n ^ p` called perfect-power collapse | `ENTERPRISE_SPECIALIZATION` | The operator is a project specialization of established adjoint projection laws. |
| Enterprise Math scale compatibility | `ENTERPRISE_SPECIALIZATION` | Lean-checked as `EnterpriseMath.Scale.scaledRoot_succ_div`, derived from `u_comm_of_l_comm` via `root_div_scale`. |
| Merged-history monotonicity | `ENTERPRISE_SPECIALIZATION` | Lean-checked as set inclusion plus finite `Set.ncard` monotonicity; the ingredients are standard. |
| `Nat.nthRoot (p*q) n = Nat.nthRoot p (Nat.nthRoot q n)` for positive exponents | `UPSTREAM_CANDIDATE` | Exact-name, API, and pinned-source searches found no equivalent theorem. The no-`sorry` Lean proof `root_mul` compiles with warnings fatal. Historical or upstream novelty is still unverified. |
| Commutation of iterated positive integer roots | `UPSTREAM_CANDIDATE` | Lean-checked corollary `root_mul_comm`; remains provisional for the same upstream-review reason. |

## Consequence for the original P008 mother-theorem plan

The original plan proposed four general mother theorems. The audit shows that the general order-theoretic content is already present in mathlib:

1. reductive/idempotent collapse from an adjunction — existing;
2. fixed points equal the lower-adjoint image — existing;
3. right adjoints compose in reverse order — existing;
4. commuting left-adjoint squares induce commuting right-adjoint squares — existing.

Therefore P008 does **not** upstream renamed versions of these results. The Lean layer contains thin project-facing wrappers only where they make Enterprise Math statements easier to read, and their documentation states that the mathematical content is inherited from mathlib.

## Verified Lean architecture

The formal layer is now:

```text
mathlib
  ↓
EnterpriseMath.Order.Adjoint
  ↓
EnterpriseMath.Arithmetic.IntegerRoot
  ├─ EnterpriseMath.Scale.Compatibility
  └─ EnterpriseMath.Dynamics.History
  ↓
Enterprise Math interpretation and physical hypotheses (documentation, not mathlib claims)
```

The project pins a mathlib commit, transitive Lake manifest, and matching Lean toolchain. `Nat.nthRoot` is the executable/formal root primitive; the notation `R_p` remains the project mathematical notation.

The strict CI command is:

```bash
lake build --wfail -KCI EnterpriseMath
```

The current layer kernel-checks T001, T002, T004, T005, T006, T010, T012, T013, T014, and T015. Warnings are fatal, so `sorry` warnings cannot silently pass this gate.

## Upstream gate

A result may remain an `UPSTREAM_CANDIDATE` only if all of the following survive review:

1. it compiles against the pinned mathlib revision without `sorry` or warnings;
2. no equivalent theorem is found by exact-name, semantic/API, or source search;
3. the statement is ordinary reusable mathematics independent of Enterprise Math ontology;
4. its assumptions and orientation fit mathlib conventions;
5. it provides enough reuse value to justify an upstream API addition;
6. a mathlib-facing review confirms that the theorem is not merely discoverable under another formulation.

No candidate is a novelty or priority claim merely because the current audit found no equivalent theorem.

## P008 outcome

P008 has therefore succeeded in **reducing** the required foundation: the root/collapse core sits on standard order adjunctions, while project-specific mathematics begins at selected specializations, compositions, scale identities, and the finite-state interpretation. The remaining open part of P008 is the literal minimality question for future extensions, not a need for a heavier structure today.
