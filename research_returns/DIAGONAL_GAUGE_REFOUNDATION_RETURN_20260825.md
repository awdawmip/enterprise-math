# Diagonal Gauge Refoundation — research return

Status: `FROZEN FOR INDEPENDENT / DRIVER REVIEW`
Date: `2026-08-25`
Researcher-ID: `EM-DGR-8C2D41`
Mode: `TASK_RESEARCH`
Owner branch: `research/diagonal-gauge-refoundation`
Frozen base main: `9d1aceb5d98c4e029a68734ef89f7b80e6c1bf8c`

Hard disposition:

`DIAGONAL_GAUGE_REFOUNDATION_TYPED_CORRECTION_CANDIDATE_ESTABLISHED__CURRENT_R061_R062_CORE_PRESERVED__CANONICAL_SOURCE_EDIT_WITHHELD_PENDING_REVIEW`

## Executive result

The blanket freeze `NO_NATIVE_DIAGONAL_SHIFT_QUOTIENT` is too strong once the current R061 Stage-2 arbitrary-point decoder is included.

Without importing the superseded Euclidean carrier metric, the current decoder independently reconstructs an exact **derived lifted-displacement gauge quotient**:

`G_D = Z^3 / Z(1,1,1) ~= Z^2`.

The current min-zero address atlas is the unique canonical section

`can(a,b,c)=(a,b,c)-min(a,b,c)(1,1,1)`.

This quotient is typed as a **derived endpoint/displacement object**, not a primitive native-point ontology and not a native Euclidean vector space.

## Exact recoveries

1. Current Stage-2 decoder:
   `D_E(r,s)=can(r,s,0)`.
2. Current displacement composition:
   `x (+)_D y = can(x+y)`.
3. Current reversal:
   `(-)_D(A,B,C)=(M-A,M-B,M-C)`.
4. Current directed gauge:
   `ell_E(g)^2=sum can(g)_i^2`.
5. Current Stage-3 spectrum:
   `SPEC={ell_E(g),ell_E(-g)}`.
6. Current trace composition descends to endpoint displacement, but endpoint displacement is not a line classifier.

## Metric fork

The quotient does **not** restore the historical native metric.

The unique globally quadratic, S3-symmetric, diagonal-gauge-invariant, unit-axis-calibrated quadratic is

`Delta=a^2+b^2+c^2-ab-bc-ca`.

But `Delta(1,1,0)=1` whereas the current sector Pythagorean gauge requires `q_E(1,1,0)=2`.

Therefore the 2026-08-20 correction is consistently interpreted as a switch from a global symmetric quadratic metric to a three-sector positive-section asymmetric gauge; deleting the displacement quotient was not mathematically necessary.

## Balanced triad / path result

At displacement level:

`g_1+g_2+g_3=0`.

At path level, current sources establish two nontrivial length-3 closed native PATH witnesses per commuting-diamond context by closing `X_iX_j` / `X_jX_i` with the reversed third-family shortcut edge.

Thus:

`ZERO_DISPLACEMENT != IDENTITY_PATH`.

The identity path has path count `0`; the closed excursions have path count `3`.

These loops are **not** members of the frozen two-component native line trace or current R062 component-typed line BRC skeleton. Therefore current finite line/path fibers are not inflated by loop dressing.

## Endpoint forgetful object

The correct global derived object is start-typed:

`(P,g): P -> P·g`.

It forms a displacement action groupoid. Path and trace concatenation descend to it. Trace groupoid inverse and independently decoded canonical reverse trace remain distinct upstream but coequalize to the same downstream arrow `(Q,-g)`.

The diagonal endpoint quotient is distinct from both native trace quotient and Boolean BRC support quotient.

## Source-impact audit

If accepted, the smallest coherent integration is expected to:

- retype the overstrong no-quotient wording in `ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md`;
- add a dedicated derived diagonal displacement gauge definition;
- add an interpretation note to the Stage-2 arbitrary-point gauge with formulas unchanged;
- route the new derived object from `00_CURRENT_NATIVE_FOUNDATION.md`;
- optionally clarify `GEOMETRIC_TOOL_REFOUNDATION_POLICY.md`.

Do not modify current R061 native line formulas, Stage-3 bidirectional spectrum, R062 BRC multipath definition, or path-valued square-root definition merely for this correction.

## Verification

Checker:

`scripts/check_diagonal_gauge_refoundation.py`

Report:

`research_results/DIAGONAL_GAUGE_REFOUNDATION/DIAGONAL_GAUGE_REFOUNDATION_CHECK_REPORT.json`

Result: `PASS`.

Report SHA-256:

`5a5d2d1f46bf876434b9c95365e85d69af9ce47c10dd069a704d8b21e7e5569a`.

Finite regression includes canonical-section, kernel, Stage-2 decoder, group law, associativity, exact triangle certificate, S3 covariance, historical-Delta gauge invariance, current reversal examples, and displacement-level balanced triad checks.

## Artifacts

- `research_notes/DIAGONAL_GAUGE_REFOUNDATION_EXECUTION_STAMP_20260825.md`
- `research_results/DIAGONAL_GAUGE_REFOUNDATION/DIAGONAL_GAUGE_REFOUNDATION_PHASE_A_THEOREM_PACKAGE_20260825.md`
- `research_results/DIAGONAL_GAUGE_REFOUNDATION/DIAGONAL_GAUGE_REFOUNDATION_PHASE_B_GLOBAL_PATH_TYPING_20260825.md`
- `research_results/DIAGONAL_GAUGE_REFOUNDATION/DIAGONAL_GAUGE_REFOUNDATION_PHASE_C_ENDPOINT_FORGETFUL_GROUPOID_20260825.md`
- `research_results/DIAGONAL_GAUGE_REFOUNDATION/DIAGONAL_GAUGE_REFOUNDATION_PHASE_D_SOURCE_DEPENDENCY_AUDIT_20260825.md`
- `research_results/DIAGONAL_GAUGE_REFOUNDATION/DIAGONAL_GAUGE_REFOUNDATION_CHECK_REPORT.json`
- `scripts/check_diagonal_gauge_refoundation.py`

## Review gate

Recommended independent/Driver hard target:

`DIAGONAL_GAUGE_REFOUNDATION_TYPED_CORRECTION_ACCEPTED_OR_NARROWED_OR_REFUTED`.

Independent review should attack, rather than assume:

- exact kernel `Z(1,1,1)` from the current decoder;
- quotient-section interpretation of Stage-2 composition/reversal;
- metric-fork theorem;
- non-collapse of trace/BRC semantics;
- zero-displacement versus identity-path distinction;
- G1-derived versus N0-primitive typing.

## Stop condition

`STOP_FOR_INDEPENDENT_OR_DRIVER_REVIEW`.

No canonical foundation file has been edited by this owner branch.
