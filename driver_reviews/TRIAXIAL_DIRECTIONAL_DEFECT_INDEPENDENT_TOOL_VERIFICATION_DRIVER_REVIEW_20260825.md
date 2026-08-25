# Driver Review — Triaxial Directional Defect Independent Tool Verification

Status: `ACCEPTED_WITH_NARROWING / INTEGRATION_AUTHORIZED`
Date: `2026-08-25`
Driver: `EM-FREE-C19420 / CONTROL_PLANE`

## 1. Intake

Task:

`RS-TRIAXIAL-DIRECTIONAL-DEFECT-INDEPENDENT-TOOL-VERIFICATION`

Owner branch:

`research/triaxial-directional-defect-independent-tool-verification`

Frozen final head:

`b1f79d2314de2d1ae1511a693cdf37e7c7812cf8`

Researcher:

`EM-TDDEF-79114C`

Independent execution evidence:

- execution stamp commit: `0f6e3d558411c282af1ffd1cdeae7f045c5722c7`;
- Phase-A frozen return commit: `9ff6b64bee6431be0a44bf876254875c47a6e588`;
- final return: `research_returns/TRIAXIAL_DIRECTIONAL_DEFECT_INDEPENDENT_TOOL_VERIFICATION_RETURN_20260825.md`;
- final report: `research_outputs/TRIAXIAL_DIRECTIONAL_DEFECT_INDEPENDENT_TOOL_VERIFICATION_20260825.md`;
- independent implementation: `src/enterprise_math/triaxial_directional_defect.py`;
- independent checker: `research_output/evidence/triaxial_directional_defect_independent_checker.py`;
- tomography/Hive/Phase-B regressions under `tests/test_triaxial_directional_defect*.py`.

The execution stamp predates mathematical work, and the Phase-A return was frozen before current-tool visibility. The independent run therefore satisfies the task's replication boundary at the claimed statement-exposed implementation-verification strength.

## 2. Research verdict

The research return's primary verdict is accepted:

`NEEDS_NARROWER_TOOL_INTERFACE`.

Driver integration verdict:

`ACCEPT_NARROWED_T1_TRIAXIAL_DIRECTIONAL_DEFECT_GLOBAL_SUBTOOL_FOR_INTEGRATION`.

Method-harvest classification:

`GLOBAL_SUBTOOL`.

Tool ownership:

`T1_SCALE_ENUMERATION_VALUATION`.

This is not accepted as a new top-level tool family. Generic mixed finite differences already belong to T1; the accepted new reusable value is the typed three-direction/120-degree specialization and its cross-domain certificates.

## 3. Independently sustained payload

The following payload survived independent reconstruction at the required scope:

1. For a declared commuting three-direction frame, the operator ladder
   `Delta_i=tau_i-I`, `H_ij=Delta_i Delta_j`, `G=Delta_1 Delta_2 Delta_3`.
2. Cyclic frame covariance of `G` and sign reversal under simultaneous frame reversal, with explicit orientation typing.
3. The common second-to-third defect bridge
   `Delta_1 H_23 = Delta_2 H_31 = Delta_3 H_12 = G`
   up to a fixed sign/translation convention.
4. The endpoint six-point switching stencil as the endpoint-collapse image of an abstract eight-state signed cube, while preserving
   `ENDPOINT_COALESCENCE != TRACE_IDENTITY_COALESCENCE`.
5. Exact native-hex tomography kernel/uniqueness certificates, including the multi-frame support-width law and the injectivity threshold at the independently reconstructed scope.
6. Primitive frame-width census consistent with the Euler-phi orbit law under the explicit primitive/canonical frame conventions.
7. A robust exposed-vertex augmentation giving a triangular/unimodular ambiguity-killing certificate with one scalar sample per kernel degree of freedom.
8. The adjoint/Gram factorization into directional Laplacians where its coefficient-domain hypotheses hold, together with explicit small-characteristic failure cases.
9. No finite-support translation-invariant convolutional left inverse for the nonunit triple-defect Laurent operator.
10. Genuine reuse of the same `RHOMBUS2`/`TRIPLE_DEFECT` implementation in a second independent problem family: Hive/rhombus discrete convexity.
11. Y–Delta/three-port rational response remains outside this linear directional-defect interface.

## 4. Mandatory interface narrowing

Integration must not preserve the provisional broad API unchanged. Freeze the following corrections.

### 4.1 Adjoint versus compressed Gram

Do not expose one ambiguous `GRAM_FACTOR` operation that conflates:

- the full-field adjoint/chirality readout `G*`;
- the interior ghost-amplitude Gram operator `G*G` after domain restriction/compression.

The integrated interface must distinguish them explicitly, for example:

- `CHIRALITY_ADJOINT` or `FULL_ADJOINT`;
- `COMPRESSED_GRAM` / `GRAM_FACTOR`.

Their input and output domains must be typed separately.

### 4.2 Frame assumptions

`DECLARE_FRAME` must explicitly validate the primitive/canonical frame assumptions used by the width/census theorems. Unoriented ray/frame-orbit deduplication must be explicit rather than inferred from coordinate coincidence.

### 4.3 Coefficient-domain assumptions

The chirality/Gram reconstruction path is characteristic-sensitive and must not be advertised as field-universal. Small-characteristic failures are retained as regression guards.

The exposed-vertex augmentation is the robust minimal linear ambiguity-killing route at the independently verified scope and should be the default field/ring-robust certificate.

### 4.4 Domain and semantic limits

The simple support-width formula is frozen only for the native hex/support-function-compatible domains actually verified.

Endpoint cancellation may not be retyped as native trace cancellation.

Binary/nonlinear tomography feasibility is unresolved.

Y–Delta and general rational boundary-response mutation are outside scope.

No Foundation definition changes follow from this tool acceptance.

## 5. Accepted integration surface

The narrowed reusable interface may expose equivalents of:

- `DECLARE_FRAME`;
- `DIFF1`;
- `RHOMBUS2`;
- `TRIPLE_DEFECT`;
- `XRAY_KERNEL_CERT`;
- `FRAME_WIDTH`;
- `MULTIFRAME_UNIQUENESS`;
- `EXPOSED_AUGMENT`;
- `CHIRALITY_ADJOINT` / `FULL_ADJOINT`;
- `COMPRESSED_GRAM` / `GRAM_FACTOR`.

Integration may reuse the independently verified implementation as evidence/source material after this review. It must preserve theorem ownership in the research artifacts and register only the reusable method interface under T1.

## 6. Verification-task closure

`RS-TRIAXIAL-DIRECTIONAL-DEFECT-INDEPENDENT-TOOL-VERIFICATION = VERIFIED_COMPLETE`.

The verification route is closed. No additional replication is required before a bounded narrowed integration attempt.

The next action is a separate `NO_NEW_MATHEMATICS` integration task whose only purpose is interface narrowing, current-main transplantation, regression preservation, T1 registration and method-inventory update. Any theorem-strengthening request must leave that integration task and return to research.

## 7. Driver disposition

`INTEGRATION_AUTHORIZED_AS_T1_GLOBAL_SUBTOOL_WITH_MANDATORY_NARROWING`.

`NEW_TOP_LEVEL_TOOL_FAMILY = REJECTED`.

`TRIAXIAL_BOX_BOUNDARY_EXCHANGE = NOT_ACCEPTED_BY_THIS_REVIEW`.
