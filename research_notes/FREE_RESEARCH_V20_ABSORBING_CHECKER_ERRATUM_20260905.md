# V20 Absorbing-State Checker Erratum

Status: `CORRECTION / FIRST CHECKER AND FIRST TARGETED WORKFLOW SUPERSEDED`
Date: `2026-09-05`
Researcher-ID: `EM-FREE-PI-PRIME-20260905`

The mathematical signless-lift theorem is stated on the absorbing-zero subspace

\[
f(0)=0.
\]

On that subspace the deterministic quotient and adaptive history operator satisfy

\[
Q_cL f=LQ_c f.
\]

They are not equal as full matrices on an unrestricted state space: their difference is supported in the absorbing column, which disappears only after evaluation on `f(0)=0`.

Accordingly, the first draft checker

`scripts/check_free_research_defect_signless_lift_v20.py`

must not be cited for the full-matrix assertion `Q_c L = L Q_c`, and the first targeted workflow

`.github/workflows/pi-prime-v20-exact-checks.yml`

is superseded.

The corrected checker is

`scripts/check_free_research_defect_signless_lift_v20_absorbing_corrected.py`.

It:

1. constructs exact rational fields with `f(0)=0`;
2. verifies `(Q_cL-LQ_c)f=0` on those fields;
3. verifies the direct logarithmic-rectangle formula for `[Q_c,D]f` pointwise;
4. verifies `delta_c Df=D delta_c f+[Q_c,D]f` on the correct carrier;
5. verifies the parity-fold realization of `D` and its positive stopped-square bound.

The corrected targeted workflow is

`.github/workflows/pi-prime-v20-exact-checks-corrected.yml`.

This correction narrows the checker semantics; it does not change the V20 theorem, which already assumes the absorbing-zero condition.
