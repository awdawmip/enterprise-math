<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-CBRC-F5-RETURN-MATERIALIZATION-RECOVERY",
  "title": "Coherent-BRC F5 — Return Materialization Recovery",
  "kind": "RECOVERY",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "F5_COMPLETED_RETURN_MATERIALIZED_WITHOUT_NEW_MATHEMATICS",
  "next_action": "Recover and publish the already-completed F5 return/evidence packet without changing mathematical conclusions, source boundary, or theorem scope; if no completed artifacts can be located, freeze exact recovery diagnostics and stop.",
  "dependencies": [
    "research_tasks/COHERENT_BRC_F5_FORGETFUL_BRANCH_NONDEGENERACY_SEMANTIC_CLASSIFICATION_20260823.md@3a84d32e3516a0771ba1f07502898d21293900e8",
    "driver_reviews/CBRC_F5_RETURN_MATERIALIZATION_STATUS_20260824.md@c1d64034c8655a5e71c6fec93d036f9961bf5eeb"
  ],
  "source_refs": [
    "research_inputs/CBRC_F5_BLIND_FORGETFUL_BRANCH_SEMANTICS_PACKET_20260823.md@a107c133e11597623bbe79ef37397fc8ba5c13f7",
    "definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md@6ec0d73a19e28ec586c59a97d24f5798c9119771",
    "definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md@b631242db84c5bd3640e6dc554b19a1d04d464f3"
  ],
  "evidence_status": "TASKBOOK_DRIVER_APPROVED_RECOVERY",
  "tags": ["CBRC","F5","recovery","return-materialization","no-new-mathematics","evidence-recovery"],
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "CBRCF5REC"
}
-->

# Coherent-BRC F5 — Return Materialization Recovery

Task-ID:

`RS-CBRC-F5-RETURN-MATERIALIZATION-RECOVERY`

Driver:

`EM-DVR-CBRC-F0-7C3A21 / CONTROL_PLANE`

Original F5 task:

`RS-CBRC-F5-FORGETFUL-BRANCH-NONDEGENERACY-SEMANTIC-CLASSIFICATION`

Original taskbook source:

`3a84d32e3516a0771ba1f07502898d21293900e8`

Original intended owner branch:

`research/cbrc-f5-forgetful-branch-nondegeneracy-semantic-classification`

## 0. Recovery-only authority

The user has reported the original F5 execution complete, but Driver intake cannot see a materialized remote return/evidence packet.

This task is **not a mathematical rerun**.

Hard prohibition:

`NO_NEW_MATHEMATICS`.

Do not improve, narrow, strengthen, repair, reinterpret, or reverse the completed mathematical result. Do not consult downstream coherent-BRC/wave work to reconstruct a preferred conclusion.

## 1. Hard target

`F5_COMPLETED_RETURN_MATERIALIZED_WITHOUT_NEW_MATHEMATICS`.

Valid final outcomes are exactly:

1. `F5_RETURN_RECOVERED_AND_MATERIALIZED`;
2. `F5_RETURN_ALREADY_EXISTS_AT_DIFFERENT_REF_AND_IS_REPORTED`;
3. `F5_COMPLETED_LOCAL_ARTIFACTS_NOT_FOUND_RECOVERY_DIAGNOSTICS_FROZEN`.

Do not substitute a new proof for missing artifacts.

## 2. Recovery search order

Search only execution/evidence locations that may contain the original completed work:

- local/remote branch refs related to the original F5 task;
- existing worktrees;
- local commits not yet pushed;
- stashes or detached HEADs created by the original execution;
- existing bundles/checkpoints produced by that execution;
- already-written required artifact paths;
- researcher handoff metadata from the original run.

Repository/governance reads are allowed for recovery procedure.

Do not use mathematical sources outside the original F5 whitelist to recreate content.

## 3. Original mathematical firewall to preserve

The recovered packet must preserve the original Phase-A mathematical source boundary exactly:

1. `research_inputs/CBRC_F5_BLIND_FORGETFUL_BRANCH_SEMANTICS_PACKET_20260823.md@a107c133e11597623bbe79ef37397fc8ba5c13f7`;
2. `definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md@6ec0d73a19e28ec586c59a97d24f5798c9119771`;
3. `definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md@b631242db84c5bd3640e6dc554b19a1d04d464f3`.

If the recovered original work used a forbidden source before its raw freeze, report that fact faithfully; do not sanitize it after the fact.

## 4. Required recovered artifacts

Materialize exactly the original F5 required artifacts if they exist:

1. `research_reports/CBRC_F5_FORGETFUL_BRANCH_NONDEGENERACY_RETURN_20260823.md`
2. `research_reports/CBRC_F5_SOURCE_AND_TARGET_LEAK_AUDIT_20260823.md`
3. `research_reports/CBRC_F5_SEMANTIC_COUNTERMODEL_AND_ABLATION_PACKET_20260823.md`
4. `scripts/cbrc_f5_validate_forgetful_branch_semantics.py`
5. `evidence/cbrc_f5_forgetful_branch_semantics_manifest.json`

If the completed artifacts have equivalent content under different filenames, preserve originals and add a recovery mapping rather than silently rewriting them.

## 5. Checker recovery

If the original checker exists, run exactly:

`python3 scripts/cbrc_f5_validate_forgetful_branch_semantics.py`

Record:

- exit status;
- deterministic digest if the original checker emits one;
- any mismatch count;
- checker source SHA-256.

Do not edit checker logic to make it pass. If it fails, freeze the failure as recovered evidence.

## 6. Git materialization

Preferred owner branch remains:

`research/cbrc-f5-forgetful-branch-nondegeneracy-semantic-classification`.

If the original completed work already has another owner ref, report and preserve that ref rather than rewriting history unnecessarily.

The final materialized surface must report:

- owner branch/ref;
- final owner head SHA;
- artifact SHA-256 digests;
- checker result/digest;
- clean working-tree status or exact reason a local tree is unavailable.

## 7. Recovery diagnostics if artifacts are absent

If no completed F5 artifact can be located after the search order in Section 2, create only:

`research_reports/CBRC_F5_RETURN_MATERIALIZATION_RECOVERY_DIAGNOSTICS_20260824.md`

containing exact checked refs/locations and the conclusion:

`F5_COMPLETED_LOCAL_ARTIFACTS_NOT_FOUND_RECOVERY_DIAGNOSTICS_FROZEN`.

Then stop.

Do not recreate the mathematical F5 result.

## 8. Driver handoff

On successful recovery, report only the recovered materialization metadata and original primary F5 verdict. Driver will independently read the packet and perform the mathematical acceptance review.

No F6/rank-two/downstream comparison is authorized by this recovery task.

---

Driver issue note:

`USER REPORTS F5 COMPLETE; REMOTE RETURN IS ABSENT. RECOVER THE ORIGINAL EVIDENCE SURFACE WITHOUT NEW MATHEMATICS.`
