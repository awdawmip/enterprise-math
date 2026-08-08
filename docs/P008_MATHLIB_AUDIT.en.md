# P008 mathlib audit framework

Status: RESEARCH

## Purpose

This document records the separation between existing mathlib mathematics, Enterprise Math specializations, and possible upstream candidates. The audit is intentionally conservative: finding that a P008 result is already in mathlib narrows our novelty boundary and is treated as progress.

The current formal audit is pinned to mathlib commit `87adeaebd370a3b6a41ac4f044fddd4bf81803ad` and its matching Lean toolchain `v4.33.0-rc2`. A later audit may update the pin, but claims below refer to this inspected snapshot unless stated otherwise.

## Classification

Each result is assigned one status:

- `MATHLIB_EXISTING`: already represented by mathlib APIs or theorems.
- `MATHLIB_DERIVED`: follows directly from existing mathlib structures but is not currently being treated as a distinct upstream theorem.
- `ENTERPRISE_SPECIALIZATION`: an application of general mathematics to Enterprise Math definitions or semantics.
- `UPSTREAM_CANDIDATE`: general reusable mathematics for which the current audit has not found an equivalent mathlib theorem. This is provisional until compilation and broader source review succeed.

## Detailed audit

| Topic | Status | Mathlib evidence / Enterprise Math action |
| --- | --- | --- |
| Natural-number integer nth root | `MATHLIB_EXISTING` | Reuse `Nat.nthRoot`; do not define a parallel Lean root primitive. |
| Root adjunction | `MATHLIB_EXISTING` | `Nat.le_nthRoot_iff` gives `a ≤ Nat.nthRoot p b ↔ a^p ≤ b` for `p ≠ 0`. |
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
| `Nat.nthRoot (p*q) n = Nat.nthRoot p (Nat.nthRoot q n)` for positive exponents | `UPSTREAM_CANDIDATE` | Exact-name/source search found no equivalent theorem in the pinned snapshot. A Lean proof derived from existing adjoint APIs is being compiled before any upstream claim. |
| Commutation of iterated positive integer roots | `UPSTREAM_CANDIDATE` | Expected corollary of the preceding composition law and multiplication commutativity; remains provisional for the same reason. |
| Enterprise Math scale compatibility | `ENTERPRISE_SPECIALIZATION` | Expected to be formalized as a specialization of existing `u_comm_of_l_comm` plus the power/multiplication commuting square. |

## Consequence for the original P008 mother-theorem plan

The original plan proposed four general mother theorems. The audit now shows that the general order-theoretic content is already present in mathlib:

1. reductive/idempotent collapse from an adjunction — existing;
2. fixed points equal the lower-adjoint image — existing;
3. right adjoints compose in reverse order — existing;
4. commuting left-adjoint squares induce commuting right-adjoint squares — existing.

Therefore P008 should **not** upstream renamed versions of these results. The Lean layer may contain thin project-facing wrappers where useful, but their documentation must state that the mathematical content is inherited from mathlib.

## Lean architecture rule

The formal layer is organized as:

```text
mathlib
  ↓
EnterpriseMath.Order.Adjoint      -- thin project-facing wrappers
  ↓
EnterpriseMath.Arithmetic.IntegerRoot
  ↓
scale / collapse-composition specializations
  ↓
Enterprise Math interpretation and physical hypotheses (documentation, not mathlib claims)
```

The project pins a mathlib commit and matching Lean toolchain so that formal evidence is reproducible. `Nat.nthRoot` is the executable/formal root primitive; the notation `R_p` remains the project mathematical notation.

## Upstream gate

A result may remain an `UPSTREAM_CANDIDATE` only if all of the following survive review:

1. it compiles against the pinned mathlib revision without `sorry`;
2. no equivalent theorem is found by exact-name, semantic/API, or source search;
3. the statement is ordinary reusable mathematics independent of Enterprise Math ontology;
4. its assumptions and orientation fit mathlib conventions;
5. it provides enough reuse value to justify an upstream API addition.

No candidate is a novelty or priority claim merely because an initial search found no exact theorem.
