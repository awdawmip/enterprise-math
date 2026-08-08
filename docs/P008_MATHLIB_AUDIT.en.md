# P008 mathlib audit framework

Status: RESEARCH

## Purpose

This document records the separation between existing mathlib mathematics, Enterprise Math specializations, and possible upstream candidates.

## Classification

Each result is assigned one status:

- `MATHLIB_EXISTING`: already represented by mathlib APIs or theorems.
- `MATHLIB_DERIVED`: follows directly from existing mathlib structures.
- `ENTERPRISE_SPECIALIZATION`: an application of general mathematics to Enterprise Math definitions.
- `UPSTREAM_CANDIDATE`: general reusable mathematics absent from mathlib.

## Initial audit

| Topic | Status | Notes |
| --- | --- | --- |
| Natural number nth root characterization | MATHLIB_EXISTING | Reuse Nat.nthRoot and related order lemmas. |
| Square root specialization | MATHLIB_EXISTING | Reuse Nat.sqrt API. |
| Galois connections | MATHLIB_EXISTING | Use existing order theory. |
| Integer root as exact state semantics | ENTERPRISE_SPECIALIZATION | Interpretation belongs to Enterprise Math. |
| Perfect-power collapse operator | ENTERPRISE_SPECIALIZATION | Derived from existing structures with project semantics. |
| General missing order lemmas | UPSTREAM_CANDIDATE | Requires independent verification. |

## Rule

Enterprise Math should not duplicate mature mathlib definitions. Upstream contributions must be ordinary reusable mathematics and must not depend on the physical interpretation layer.
