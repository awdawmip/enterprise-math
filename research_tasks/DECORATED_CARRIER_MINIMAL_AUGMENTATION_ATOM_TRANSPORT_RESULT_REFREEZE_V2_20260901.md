<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-DECORATED-CARRIER-MINIMAL-AUGMENTATION-ATOM-TRANSPORT",
  "title": "Decorated carrier minimal augmentation Result envelope refreeze V2",
  "kind": "RESEARCH",
  "owner": "research/decorated-carrier-minimal-augmentation-atom-transport",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Generation 1 mathematically classifies the C2->S3 and S3->S4 augmentation hierarchy, but immutable Result RR-AA2C14AA62C19342EB97 binds only the short Return in output_manifest while the claim relies on the full proof artifact, machine-readable atlas, deterministic checker, and execution provenance. Re-freeze the same mathematics with a complete dual-digest evidence envelope and zero mathematical drift.",
  "next_action": "Replay the exact frozen checker, verify byte identity of the Generation-1 short Return, full proof artifact, augmentation atlas and checker, freeze a new integrity manifest and execution record, then create a fresh Result whose output_manifest binds every load-bearing output with Git blob SHA-1 and SHA-256.",
  "dependencies": [
    "RR-AA2C14AA62C19342EB97",
    "DR-8D02777A882DB5E95E45"
  ],
  "source_refs": [
    "research_returns/DECORATED_CARRIER_MINIMAL_AUGMENTATION_ATOM_TRANSPORT_RETURN_20260901.md",
    "research_artifacts/DECORATED_CARRIER_MINIMAL_AUGMENTATION_ATOM_TRANSPORT/full_research_return_20260901.md",
    "research_artifacts/DECORATED_CARRIER_MINIMAL_AUGMENTATION_ATOM_TRANSPORT/augmentation_atlas_20260901.json",
    "research_checks/DECORATED_CARRIER_MINIMAL_AUGMENTATION_ATOM_TRANSPORT_CHECK_20260901.py",
    "driver_reviews/DECORATED_CARRIER_MINIMAL_AUGMENTATION_ATOM_TRANSPORT_DRIVER_REVIEW_20260901.md"
  ],
  "evidence_status": "GEN1_MATHEMATICS_RETAINED / RESULT_ENVELOPE_INCOMPLETE / ZERO_MATH_DRIFT_REFREEZE_REQUIRED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "decorated-carrier",
    "transport",
    "minimal-augmentation",
    "result-envelope",
    "integrity-refreeze",
    "zero-math-drift",
    "C3",
    "V4",
    "twisted-cohomology"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-DECORATED-CARRIER-MINIMAL-AUGMENTATION-ATOM-TRANSPORT",
  "parent_objective_id": "OBJ-DECORATED-CARRIER-TRANSPORT-AUGMENTATION-MINIMALITY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "DCTRMINR2",
  "origin_kind": "MAINTENANCE",
  "task_lineage": "MAINTENANCE",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->
# Decorated carrier minimal augmentation Result envelope refreeze V2

## Mother question

Can the mathematically retained Generation-1 augmentation atlas be re-frozen under the current Result contract with a complete immutable dual-digest evidence chain, without changing any theorem, formula, gauge classification, countermodel, or scope boundary?

This is an integrity repair only. It is not permission to strengthen the augmentation theorem or reopen the closed Seed-6 arithmetic objective.

## Frozen inputs and scope

The following Generation-1 mathematical bytes are frozen and must remain byte-identical:

- short Return blob `sha1:12a88ef6d9624082c0512a107f775d481d7e6ae8`;
- full proof artifact blob `sha1:37dcf2f063a45e869e616ca47aa83e16f25c3c7f`;
- augmentation atlas blob `sha1:309514bbab835dc3930f9aafa174e24f62b4d3eb`;
- deterministic checker blob `sha1:173b84f3855b98a52c87bcbb9898b7fa1396723f`;
- Generation-1 execution record blob `sha1:f35d69559cbc72784b6665e8a94816fdb78fed4b` as provenance history.

The immutable Generation-1 Result `RR-AA2C14AA62C19342EB97` is preserved unchanged as historical evidence. Its one-row `output_manifest` is the exact defect being repaired and must not be edited in place.

Preserve exactly the mathematical payload:

- `L1 -> L2`: `1 -> C3=A3 -> S3 -> C2 -> 1`, with the marked carrier state giving the typed stabilizer split and relative lift classes `H^1(X;C3_h)`;
- `d2=0` for `beta=0`, `d2=beta` for `h=0`, and `d2=beta-1` for `h!=0`;
- `L2 -> L3`: `1 -> V4 -> S4 -> S3 -> 1`, with relative atom-lift classes `H^1(X;V4_rho)`;
- for `beta>=1`, `d3=2*beta-2+dim(V4^im(rho))`, and `d3=0` for `beta=0`;
- all four homomorphic `S3 -> S4` sections are `V4`-gauge-equivalent presentation choices;
- the frozen lower reduct forces no preferred nonzero `C3` or `V4` kernel-cohomology class.

`MATHEMATICAL_DELTA = NONE` is mandatory.

## Hard target and required outputs

Hard target:

`DCTRMIN_RESULT_ENVELOPE_REFROZEN_WITH_COMPLETE_LOAD_BEARING_DIGEST_CHAIN_AND_ZERO_MATH_DRIFT`

Required new outputs:

1. `research_returns/DECORATED_CARRIER_MINIMAL_AUGMENTATION_ATOM_TRANSPORT_RESULT_REFREEZE_V2_RETURN_20260901.md`;
2. `research_artifacts/DECORATED_CARRIER_MINIMAL_AUGMENTATION_ATOM_TRANSPORT_RESULT_REFREEZE_V2/integrity_manifest_20260901.json`;
3. a fresh execution record under the stable Task-ID;
4. a fresh immutable Result bound to publication `TP2-1C9E7635984115B9DEF1`.

The new Result `output_manifest` must bind, at minimum, all of the following with both `git_blob_sha1` and `sha256`:

- the new revision Return;
- the preserved Generation-1 short Return;
- the preserved full proof artifact;
- the preserved augmentation atlas;
- the preserved deterministic checker;
- the new integrity manifest;
- the fresh Generation-2 execution record.

The integrity manifest must additionally pin the historical Generation-1 execution record and immutable Result record so the repaired chain is auditable without mutating history.

Replay the exact checker and require the same terminal line:

`PASS checks=8384; L1_to_L2=C3_twisted_H1; S3_sign_kernel=3; marked_split=canonical; L2_to_L3=V4_twisted_H1; S4_kernel=4; sections=4_all_V4_gauge; L3_one_loop_dims=id:2,transposition:1,3cycle:0; clean_single_multi_equality=PASS`

## Research value to preserve

The value of this maintenance generation is evidentiary, not mathematical: it turns a mathematically persuasive but incompletely bound Result into a complete immutable reviewable chain. It must preserve the sharp distinction between canonical zero split gauge classes and exogenous nonzero kernel-cohomology choices, while avoiding any claim that standard extension/cohomology theory is historically novel.

A clean Generation-2 Result will permit the Driver to terminally accept the augmentation atlas and then decide whether the parent Objective closes. Until that clean Result exists, the Objective remains OPEN.

## Success, kill, and return criteria

SUCCESS requires all of the following:

- every frozen Generation-1 mathematical file above is byte-identical to its pinned Git blob;
- the deterministic checker replays exactly with no theorem or regression drift;
- the integrity manifest records Git blob SHA-1 and SHA-256 for every preserved/load-bearing source;
- every new Result output-manifest row has `path + git_blob_sha1 + sha256`;
- the new Result is bound to this Generation-2 publication and a fresh execution record;
- `MATHEMATICAL_DELTA=NONE` is stated explicitly.

Return or fail closed if any preserved mathematical byte changes, if the checker no longer reproduces the frozen verdict, or if any load-bearing evidence is omitted from the new Result envelope. A mathematical conflict must become a substantive revision rather than being hidden inside an integrity patch.

Forbidden changes include choosing a preferred nonzero `C3`/`V4` class, adding a new section/frame axiom, changing the `d2`/`d3` formulas, reopening factorization/additive-distance semantics, or closing the parent Objective from the researcher lane.
