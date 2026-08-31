<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PRIME-COORD-FACTOR-CRITICAL-COFACTOR-SUPPORT-COMPRESSION",
  "title": "PCF5 restricted support compression Result integrity re-freeze V2",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Recover the already-frozen PCF5 restricted support-compression theorem into a current reviewable Result whose return, checker, artifact, execution provenance and result manifest all bind the exact frozen bytes with Git blob SHA-1 and SHA-256, without changing any mathematical claim.",
  "next_action": "Reproduce the frozen PCF5 theorem checkpoint and exact regression bytes from the pinned execution history, freeze an integrity-only revision return with no mathematical delta, and emit a new execution record plus new immutable Result-ID under the current digest contract.",
  "dependencies": [
    "research_tasks/PRIME_COORD_FACTOR_CRITICAL_COFACTOR_SUPPORT_COMPRESSION_20260827.md@blob:029494c0a2bc2322ca20914b1ea6dadfc655c7f3",
    "research/prime-coord-factor-critical-cofactor-support-compression-em-pcf5-3432b6@67d2146aae18e2f503477b824e9b5d92681bc41e"
  ],
  "source_refs": [
    "research_returns/PRIME_COORD_FACTOR_CRITICAL_COFACTOR_SUPPORT_COMPRESSION_RETURN_20260827.md@blob:604bd1719a1573064521e6f67f27176c56d89326",
    "research_result_records/RS-PRIME-COORD-FACTOR-CRITICAL-COFACTOR-SUPPORT-COMPRESSION/RR-2A4E099EAD6A017F1272.json@historical-envelope"
  ],
  "evidence_status": "RESTRICTED_SUPPORT_COMPRESSION_PROVED / MATHEMATICS_FROZEN / RESULT_RETURN_BLOB_BINDING_INVALID / ZERO_MATH_DELTA_RECOVERY",
  "last_progress_ref": "RR-2A4E099EAD6A017F1272 / frozen theorem checkpoint 67d2146aae18e2f503477b824e9b5d92681bc41e",
  "last_progress_at": "2026-08-29T00:58:13+00:00",
  "hard_block": null,
  "tags": [
    "PCF5",
    "prime-coordinate-factor-extraction",
    "result-integrity",
    "support-compression",
    "zero-math-delta"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PRIME-COORD-FACTOR-CRITICAL-COFACTOR-SUPPORT-COMPRESSION",
  "parent_objective_id": "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION",
  "parent_objective_generation_id": "OG-AA2BAD92F59DC97880C7",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PCF5R2",
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

# PCF5 restricted support compression Result integrity re-freeze V2

Status: `READY / P1 / INTEGRITY-ONLY`

## Mother question

The PCF5 execution already froze a restricted N-blind support-compression theorem, but its immutable historical Result binds a return Git blob that does not equal the actual frozen return bytes. How can that completed mathematics be restored as a current reviewable Result without silently rewriting history or changing theorem strength?

## Frozen inputs and scope

Freeze the mathematical checkpoint at `67d2146aae18e2f503477b824e9b5d92681bc41e`. The load-bearing return is the exact file whose Git blob is `604bd1719a1573064521e6f67f27176c56d89326`. Preserve the theorem that the full layer with `m=max(2,ceil((kappa*N)^(1/6)))` has `m^2=O_kappa(N^(1/3))` cells, exactly partitions the declared interval, and makes a prime visible exactly when `p<=m^3+m+1`. Preserve the restricted all-divisor coverage condition `P^+(N)^2<=kappa*N`, the batch-evaluation interface, the explicit `N=2018, kappa=4` all-prime-visibility boundary, and the original regression semantics.

This task is evidence-chain recovery only. It must not strengthen the restricted theorem into universal factor extraction, must not weaken its counterexample boundary, and must not alter the original mathematical return/checker/artifact bytes except for a separately named revision return that states the integrity repair.

## Hard target and required outputs

Hard target: `PCF5_RESTRICTED_SUPPORT_COMPRESSION_RESULT_REFROZEN_WITH_EXACT_DIGEST_CHAIN_AND_ZERO_MATH_DRIFT`.

Required outputs:

1. An integrity revision return explicitly stating `NO_MATH_DELTA`.
2. Exact replay of the frozen theorem/checker/certificate bytes or an explicit failure if any byte cannot be reproduced.
3. A new execution record under the current contract.
4. A new immutable Result-ID under the current contract.
5. A complete output manifest binding every frozen output by path, Git blob SHA-1 and SHA-256.
6. An explicit declaration that historical `RR-2A4E099EAD6A017F1272` remains immutable history and is not edited.
7. A clear separation between this maintenance result and any future investigation of whether the visibility theorem implies a stronger universal proper-factor extractor.

## Research value to preserve

The PCF5 theorem is a potentially high-leverage bridge between Perfect-Prime-Table cell geometry and N-blind factor support. Losing it because of an incorrect Result envelope would erase a completed mathematical checkpoint; silently repairing the old Result would destroy immutable evidence semantics. A zero-delta re-freeze preserves both the mathematics and the control history.

## Success, kill, and return criteria

Success requires exact mathematical-byte recovery and a new current-schema Result with a complete digest chain. Stop with an integrity failure rather than guessing if the frozen bytes cannot be reproduced.

Kill conditions include any change to theorem scope, asymptotic bounds, the declared counterexample, regression semantics, or source mathematical bytes; any claim of a universal `N^(1/3)` factorization theorem inside this maintenance task; or any novelty/speedup claim not present in the frozen mathematics.

Return one durable integrity report and the new execution/Result records. The task ends at evidence-chain restoration; mathematical strengthening belongs to a separately authorized research task after Driver review.
