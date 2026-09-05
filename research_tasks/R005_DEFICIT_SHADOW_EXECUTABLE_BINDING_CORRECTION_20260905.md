<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R005-DEFICIT-SHADOW-EXECUTABLE-BINDING-CORRECTION",
  "title": "R005 deficit-shadow executable binding correction",
  "kind": "RESEARCH",
  "owner": "research/r005-deficit-shadow-executable-binding-correction",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "The R005 deficit-shadow mathematics at source head f9e2a611b45631c43effce36b7300c6f9a56b77b is structurally reviewable, but the published scanner bytes contain a metadata-name defect and a malformed coverage error string; the frozen validation transcript therefore does not bind to the executable bytes, and no positive attested-catalog validation path is frozen.",
  "next_action": "Repair only the executable/evidence binding at the frozen R005 source, add a genuinely complete synthetic attested-catalog positive-path regression, rerun exact-byte validation on the final files, and regenerate the transcript and manifest digests without changing the mathematical frontier.",
  "dependencies": [],
  "source_refs": [
    "research/r005a-prime-algorithm-lab-20260903@f9e2a611b45631c43effce36b7300c6f9a56b77b",
    "docs/R005A_P2_DEFICIT_SHADOW_INVERSION_20260902.md",
    "experiments/r005a_p2_gap_shadow_inversion.py",
    "experiments/r005a_p2_gap_shadow_inversion_regression.py",
    "research_artifacts/RS-R005-PRIME-ALGORITHM-LAB_20260902/R005A_ARTIFACT_MANIFEST_20260902.json",
    "research_artifacts/RS-R005-PRIME-ALGORITHM-LAB_20260902/evidence/R005A_VALIDATION_TRANSCRIPT_20260902.txt"
  ],
  "evidence_status": "DRIVER_REVIEW_FOUND_EXECUTABLE_BINDING_DEFECT / MATHEMATICAL_DSI_RESULT_NOT_REOPENED",
  "last_progress_ref": "research/r005a-prime-algorithm-lab-20260903@f9e2a611b45631c43effce36b7300c6f9a56b77b",
  "last_progress_at": "2026-09-05T00:35:00+00:00",
  "hard_block": null,
  "tags": [
    "R005",
    "maintenance",
    "deficit-shadow",
    "executable-integrity",
    "manifest-binding",
    "regression"
  ],
  "claim_lease_minutes": 360,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-R005-DEFICIT-SHADOW-EXECUTABLE-BINDING-CORRECTION",
  "parent_objective_id": "OBJ-R005-PRIME-ALGORITHM-LAB-RESULT-INTEGRITY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "R005-FIX",
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

# R005 deficit-shadow executable binding correction

Status: `READY / P1 / HIGH / NARROW INTEGRITY CORRECTION`

## Mother question

Can the already-derived R005 deficit-shadow reduction be made reviewable as an exact executable artifact by repairing the published scanner bytes and rebinding the validation evidence, without reopening the DSI mathematics or extending the certified prime frontier?

## Frozen inputs and scope

Freeze the mathematical content of `docs/R005A_P2_DEFICIT_SHADOW_INVERSION_20260902.md` at source head `f9e2a611b45631c43effce36b7300c6f9a56b77b`. The accepted review target is only executable/evidence integrity. In `experiments/r005a_p2_gap_shadow_inversion.py`, correct the exact published defects around `max_gap_bound_end` metadata access and the malformed coverage error string. Preserve the fail-closed catalogue contract, the q=78553 constants, the DSI1/DSI2/DSI3 formulas, and the existing one-unit guard semantics. Do not attempt to obtain the real complete gap-916 catalogue and do not extend the certified endpoint.

## Hard target and required outputs

Hard target: `R005_DEFICIT_SHADOW_EXECUTABLE_BYTES_AND_EVIDENCE_REBOUND`.

Required outputs are: (1) a syntactically valid corrected scanner; (2) a regression that enters `completeness_attestation=true` using a genuinely complete synthetic small-domain consecutive-prime-gap catalogue and reaches the positive certification path; (3) at least one negative-path check showing insufficient coverage or max-gap-bound extent still fails closed; (4) exact-byte compile/regression results produced from the final corrected files; and (5) regenerated validation transcript plus artifact manifest hashes that match those final bytes. If any other executable byte changes, explain it explicitly and include it in the regenerated manifest.

## Research value to preserve

The DSI result collapses a multi-billion-event seam search to a finite near-maximal-gap shadow search. That structural reduction should not be discarded because its first durable executable bundle was damaged in publication. A narrow integrity repair preserves the mathematical work while giving later Driver review a byte-exact executable surface.

## Success, kill, and return criteria

Success requires all required outputs above, with the positive synthetic attested-catalog path actually executed and the final transcript/manifest bound to the exact corrected bytes. Kill the task if repairing the scanner reveals a mathematical inconsistency in DSI1/DSI2/DSI3 or changes the q=78553 reduction; in that case freeze the smallest exact counterexample and return without broadening the task. Stop once executable/evidence integrity is restored. The real exact-916 catalogue search, q=78553 seam closure, Lean formalization, and any stronger theorem claim are outside this task.
