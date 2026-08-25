<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "GS-TRIAXIAL-DIRECTIONAL-DEFECT-T1-NARROWED-INTEGRATION",
  "title": "Triaxial Directional Defect Calculus — T1 Narrowed Subtool Integration",
  "kind": "GOVERNANCE",
  "owner": "integration/triaxial-directional-defect-t1-subtool",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "T1_TRIAXIAL_DIRECTIONAL_DEFECT_SUBTOOL_NARROWED_INTERFACE_INTEGRATED_OR_EXPLICITLY_BLOCKED",
  "next_action": "Integrate the Driver-accepted narrowed triaxial directional-defect interface into the current T1 toolbox surface without adding mathematics: transplant/adapt the independently verified implementation, split adjoint versus compressed-Gram semantics, preserve tomography/Hive/finite-characteristic regressions, register the GLOBAL_SUBTOOL under T1, update the method inventory, and return an exact integration disposition.",
  "dependencies": [
    "driver_reviews/TRIAXIAL_DIRECTIONAL_DEFECT_INDEPENDENT_TOOL_VERIFICATION_DRIVER_REVIEW_20260825.md@f364c75d55e8018bcea80bdf00fc025f2ad7dd02",
    "research/triaxial-directional-defect-independent-tool-verification@b1f79d2314de2d1ae1511a693cdf37e7c7812cf8",
    "enterprise_toolbox_registry.json@main",
    "research_method_inventory.json@main"
  ],
  "source_refs": [
    "driver_reviews/TRIAXIAL_DIRECTIONAL_DEFECT_INDEPENDENT_TOOL_VERIFICATION_DRIVER_REVIEW_20260825.md@f364c75d55e8018bcea80bdf00fc025f2ad7dd02",
    "research/triaxial-directional-defect-independent-tool-verification:src/enterprise_math/triaxial_directional_defect.py@b1f79d2314de2d1ae1511a693cdf37e7c7812cf8",
    "research/triaxial-directional-defect-independent-tool-verification:tests/test_triaxial_directional_defect.py@b1f79d2314de2d1ae1511a693cdf37e7c7812cf8",
    "research/triaxial-directional-defect-independent-tool-verification:tests/test_triaxial_directional_defect_hive.py@b1f79d2314de2d1ae1511a693cdf37e7c7812cf8",
    "research/triaxial-directional-defect-independent-tool-verification:tests/test_triaxial_directional_defect_phaseb.py@b1f79d2314de2d1ae1511a693cdf37e7c7812cf8"
  ],
  "evidence_status": "DRIVER_ACCEPTED_NARROWED_T1_GLOBAL_SUBTOOL_READY_FOR_INTEGRATION",
  "last_progress_ref": "driver_reviews/TRIAXIAL_DIRECTIONAL_DEFECT_INDEPENDENT_TOOL_VERIFICATION_DRIVER_REVIEW_20260825.md@f364c75d55e8018bcea80bdf00fc025f2ad7dd02",
  "last_progress_at": "2026-08-25T20:28:00+08:00",
  "hard_block": null,
  "tags": [
    "triaxial",
    "T1",
    "tool-integration",
    "global-subtool",
    "no-new-mathematics",
    "tomography",
    "hive",
    "finite-difference"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "GS-TRIAXIAL-DIRECTIONAL-DEFECT-T1-NARROWED-INTEGRATION",
  "parent_objective_id": "OBJ-TRIAXIAL-DIRECTIONAL-DEFECT-T1-NARROWED-SUBTOOL-INTEGRATION",
  "publication_migration_source": "research_tasks/TRIAXIAL_DIRECTIONAL_DEFECT_T1_NARROWED_INTEGRATION_20260825.md@9c9358159111e7f29c9fe6e5860a330589654c0e",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "TDINT",
  "origin_kind": "REPLAY_OR_INTEGRATION",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:31624b616557f081e4adf2ae91ea591233062c12e0c29d1c53c9ef4fac3f2271",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Triaxial Directional Defect Calculus — T1 Narrowed Subtool Integration

Status: `READY / DRIVER_APPROVED / INTEGRATION / NO NEW MATHEMATICS`

Task-ID:

`GS-TRIAXIAL-DIRECTIONAL-DEFECT-T1-NARROWED-INTEGRATION`

Owner branch:

`integration/triaxial-directional-defect-t1-subtool`

Hard target:

`T1_TRIAXIAL_DIRECTIONAL_DEFECT_SUBTOOL_NARROWED_INTERFACE_INTEGRATED_OR_EXPLICITLY_BLOCKED`

## 0. Purpose

This task integrates an already independently verified and Driver-accepted reusable method. It is not a theorem-discovery task and may not enlarge theorem scope.

Accepted method classification:

`GLOBAL_SUBTOOL` under `T1_SCALE_ENUMERATION_VALUATION`.

The verification task is closed. Use its frozen implementation/tests as integration evidence, subject to the mandatory interface narrowing in the Driver review.

## 1. Frozen accepted mathematics

Do not strengthen or generalize these statements during integration. Preserve only the scope accepted by the Driver review:

- declared commuting three-direction/120-degree frame;
- `Delta_i=tau_i-I`;
- `H_ij=Delta_i Delta_j`;
- `G=Delta_1 Delta_2 Delta_3`;
- cyclic covariance and reversal sign law at the verified typing strength;
- `Delta_1 H_23 = Delta_2 H_31 = Delta_3 H_12 = G` up to one fixed sign/translation convention;
- endpoint six-point collapse with `ENDPOINT_COALESCENCE != TRACE_IDENTITY_COALESCENCE`;
- native-hex/support-compatible tomography kernel/width/uniqueness certificates at the verified domain scope;
- primitive frame census at the verified primitive/canonical frame scope;
- exposed-vertex minimal ambiguity-killing certificate;
- characteristic-sensitive adjoint/Gram path and its small-characteristic negative controls;
- Hive/rhombus reuse of the same second/third defect operators;
- no finite-support translation-invariant convolutional left inverse at the verified Laurent-carrier scope.

Explicitly out of scope:

- Foundation edits;
- Y–Delta/general rational boundary-response mutation;
- binary/nonlinear tomography feasibility;
- arbitrary-domain extension of the native-hex width law;
- field-universal chirality/Gram claims;
- a new top-level tool family.

## 2. Mandatory narrowed interface

The integrated module must expose typed equivalents of:

- `DECLARE_FRAME`;
- `DIFF1`;
- `RHOMBUS2`;
- `TRIPLE_DEFECT`;
- `XRAY_KERNEL_CERT`;
- `FRAME_WIDTH`;
- `MULTIFRAME_UNIQUENESS`;
- `EXPOSED_AUGMENT`;
- `CHIRALITY_ADJOINT` or `FULL_ADJOINT`;
- `COMPRESSED_GRAM` / `GRAM_FACTOR`.

Do not conflate `G*` on the full field with the compressed interior `G*G` operator. Their domains, codomains and coefficient restrictions must be explicit.

`DECLARE_FRAME` must validate the primitive/canonical assumptions needed by frame-width/census results and must make unoriented-ray/frame-orbit deduplication explicit.

## 3. Implementation integration

Adapt the independently verified implementation into the current shared source surface. Preserve or improve typing and diagnostics; do not silently weaken a rejected input into a coercion that changes semantics.

The shared implementation must support both verified application families through the same operator core:

1. triaxial discrete tomography;
2. Hive/rhombus discrete convexity.

A second application may wrap the common operators but may not duplicate an unrelated `RHOMBUS2`/`TRIPLE_DEFECT` implementation merely to satisfy the reuse gate.

## 4. Required regressions

Retain executable regression coverage for at least:

1. cyclic covariance / reversal sign behavior;
2. second-to-third defect bridge;
3. six-point endpoint stencil versus eight-state trace-cube typing;
4. native-hex single- and multi-frame kernel/uniqueness certificates;
5. Euler-phi primitive frame census at bounded exact widths;
6. exposed-vertex augmentation and unimodular certificate cases;
7. chirality/Gram success on admitted coefficient domains;
8. explicit small-characteristic failure guards;
9. Hive/rhombus reuse through the same shared operators;
10. Y–Delta rejection/out-of-scope guard if the public API could otherwise be misused for it.

The integration return must report the exact executable commands and results used to establish these regressions.

## 5. Toolbox and method inventory

Register the accepted capability as a T1 `GLOBAL_SUBTOOL`, not as a new top-level family.

Update the current toolbox/method inventory surfaces using their current schemas. The registration must preserve:

- parent family `T1_SCALE_ENUMERATION_VALUATION`;
- capability triggers around triaxial directional differences, rhombus defects/Hessian transport, triple defect/ghost kernels, frame-width uniqueness and augmentation certificates;
- hard boundaries from this taskbook and the Driver review;
- source/test references for the integrated implementation.

Do not transfer theorem ownership into the toolbox record. The toolbox owns the reusable interface; theorem/proof provenance remains in the verification and Driver-review artifacts.

## 6. Required outputs

Produce or update, as applicable:

1. `src/enterprise_math/triaxial_directional_defect.py` with the narrowed public interface;
2. shared regression tests covering tomography, Hive/rhombus and coefficient-boundary behavior;
3. current T1 toolbox registry entry/subtool registration;
4. current research-method inventory/addendum entry classifying the method as `GLOBAL_SUBTOOL`;
5. any mirrored human toolbox documentation required by the current registry schema;
6. `research_output/evidence/TRIAXIAL_DIRECTIONAL_DEFECT_T1_NARROWED_INTEGRATION_MANIFEST_20260825.json` with artifact digests and test evidence;
7. `research_returns/TRIAXIAL_DIRECTIONAL_DEFECT_T1_NARROWED_INTEGRATION_RETURN_20260825.md`.

## 7. Integration guards

If current source structure requires an adapter, keep the adapter semantics explicit.

If a current-main conflict shows that the independently verified interface cannot be integrated without changing theorem statements, stop integration and return the conflict rather than changing the mathematics.

If a public API name differs from this taskbook, the return must map old-to-new names and show that the accepted semantic split remains intact.

No new mathematical theorem is needed to complete this task. Any newly discovered mathematical gap is returned as a separate research residue rather than solved inside the integration task.

## 8. Final disposition

Return exactly one primary disposition:

- `T1_TRIAXIAL_DIRECTIONAL_DEFECT_SUBTOOL_INTEGRATED`;
- `INTEGRATION_REPAIR_REQUIRED`;
- `INTEGRATION_BLOCKED_BY_CURRENT_MAIN_CONFLICT`.

For `T1_TRIAXIAL_DIRECTIONAL_DEFECT_SUBTOOL_INTEGRATED`, the return must show that the narrowed interface, method registration and required regressions all agree at one frozen integration head.

## 9. Stop condition

Stop when one disposition is fully evidenced and the required integration artifacts are frozen. Do not use the integration task to open a stronger tool family, broaden native semantics, or add theorem rows.
