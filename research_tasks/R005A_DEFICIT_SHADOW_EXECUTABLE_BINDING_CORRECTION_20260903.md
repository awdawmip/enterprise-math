<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R005-DEFICIT-SHADOW-EXECUTABLE-BINDING-CORRECTION",
  "title": "R005-A deficit-shadow executable binding correction",
  "kind": "RESEARCH",
  "owner": "research/r005a-deficit-shadow-executable-binding-correction",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "The R005-A deficit-shadow structural result at f9e2a611b45631c43effce36b7300c6f9a56b77b is mathematically reviewable, but its published scanner has a NameError typo and a malformed f-string, while the frozen validation transcript and manifest do not bind the exact published bytes. The original researcher execution has been abandoned, so a separate integrity-repair task is required.",
  "next_action": "Start from exact source commit f9e2a611b45631c43effce36b7300c6f9a56b77b; repair only the executable/binding defects, add a true-attestation positive-path regression and a max-bound-coverage rejection, rerun compile/regressions on final bytes, regenerate transcript and manifest, and freeze a no-math-delta return.",
  "dependencies": [],
  "source_refs": [
    "research/r005a-prime-algorithm-lab-20260903@f9e2a611b45631c43effce36b7300c6f9a56b77b",
    "docs/R005A_P2_DEFICIT_SHADOW_INVERSION_20260902.md@f9e2a611b45631c43effce36b7300c6f9a56b77b",
    "experiments/r005a_p2_gap_shadow_inversion.py@f9e2a611b45631c43effce36b7300c6f9a56b77b",
    "research_returns/RS-R005-PRIME-ALGORITHM-LAB_20260902.md@f9e2a611b45631c43effce36b7300c6f9a56b77b",
    "PR#1140 Driver blocking review 5097275954"
  ],
  "evidence_status": "DRIVER_BLOCKING_REVIEW_5097275954 / MATH_STRUCTURE_REVIEWABLE / EXECUTABLE_BINDING_BROKEN",
  "last_progress_ref": "PR#1140/review/5097275954",
  "last_progress_at": "2026-09-03T02:55:00+00:00",
  "hard_block": null,
  "tags": [
    "R005",
    "R005-A",
    "maintenance",
    "executable-integrity",
    "byte-binding",
    "deficit-shadow",
    "q78553"
  ],
  "claim_lease_minutes": 360,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-R005-DEFICIT-SHADOW-EXECUTABLE-BINDING-CORRECTION",
  "parent_objective_id": "OBJ-R005-PRIME-ALGORITHM-LAB",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "R005A-FIX",
  "origin_kind": "MAINTENANCE",
  "task_lineage": "MAINTENANCE",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:fbe51ab884e1267b7bb6de0de598ad5504fd0d67d1570475115a9a16a6ec4ca0",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R005-A deficit-shadow executable binding correction

Status: `READY / P1 / HIGH / INTEGRITY-CORRECTION / NO-MATH-DELTA`

## Mother question

Can the already-derived R005-A bounded-deficit gap-shadow result be made executable and byte-auditable at its exact current mathematical strength after the original researcher execution was abandoned, without reopening the DSI mathematics or claiming any new q=78553 frontier extension?

## Frozen inputs and scope

Freeze the mathematical content at source commit `f9e2a611b45631c43effce36b7300c6f9a56b77b`: DSI1 `I prime-free iff g>D+t`, DSI2 `t+(G-g)<=d-1` for `D=G-d`, DSI3 exact floor-square inversion, the q=78553 constants, and the statement that the certified frontier remains `k<=2822453183433`.

The correction surface is intentionally narrow. The published `experiments/r005a_p2_gap_shadow_inversion.py` contains two binding defects: `metada` instead of `metadata`, and a malformed coverage error f-string. The frozen validation transcript reports compile success even though those exact published bytes cannot support that claim. Preserve the structural note, the old finite endpoint, and the catalogue-blocked status. Do not attempt to obtain the missing complete exact-916-gap catalogue in this task.

Allowed edits are limited to the scanner, its focused regression, regenerated validation evidence, regenerated artifact manifest/digests, and the correction return/handoff needed to bind those exact final bytes. Existing one-unit mathematics and the q=78553 reduction may be cited but not strengthened.

## Hard target and required outputs

Hard target: `R005_DEFICIT_SHADOW_EXECUTABLE_BINDING_CORRECTED_AND_BYTE_REVALIDATED`.

Required outputs:

1. Correct the exact scanner so it parses and the full `validate_catalog_for_seam` path can execute, including the `max_gap_bound_end` check and the coverage diagnostic.
2. Add a focused synthetic regression with `completeness_attestation=true` that reaches the positive catalogue-validation path, plus a negative case that must fail because the declared max-gap-bound coverage ends too early.
3. Run `python3 -m py_compile` on the final scanner and regression bytes, then run the focused regression suite. Record commands, exit status and exact checked paths in a fresh validation transcript.
4. Recompute the artifact manifest from the final repository bytes, including updated byte counts and SHA-256 values for every changed scanner/regression/evidence file.
5. Freeze a correction return stating `NO_MATH_DELTA`, the exact source lineage, the final evidence hashes, and that q=78553 remains blocked on a complete independently auditable exact-916-gap catalogue for starts `[1291005053866735,1294364244470160]`.

## Research value to preserve

The DSI reduction is a useful search-dimension collapse and appears mathematically sound, but Driver acceptance requires the executable certificate and its evidence chain to refer to the bytes that actually exist. This task preserves that result without wasting another researcher cycle on already-audited mathematics and without converting a packaging defect into a false frontier claim.

## Success, kill, and return criteria

Success is exactly `R005_DEFICIT_SHADOW_EXECUTABLE_BINDING_CORRECTED_AND_BYTE_REVALIDATED`: final scanner bytes compile, the focused positive and negative catalogue-path regressions pass, the fresh transcript agrees with those bytes, and the manifest hashes/byte counts match the returned files.

Kill and return immediately if repairing the scanner changes any DSI theorem, q=78553 arithmetic constant, certified endpoint, catalogue obligation, or search semantics; such a finding is a mathematical delta and must be returned as `MATH_DELTA_FOUND_REQUIRES_DRIVER_REVIEW` rather than silently repaired here.

A valid terminal return must preserve one of only two dispositions: `NO_MATH_DELTA_EXECUTABLE_BINDING_REPAIRED` or `MATH_DELTA_FOUND_REQUIRES_DRIVER_REVIEW`. No q=78553 seam-closure or larger endpoint claim belongs to this task.
