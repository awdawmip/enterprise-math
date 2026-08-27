<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P022-OBS-HIST-ARITHMETIC-CORE",
  "title": "P022 Observation-History Primitive Franel Arithmetic Core — Split Replay",
  "kind": "RESEARCH",
  "owner": "program/p022-geometry-v2",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Resume the frozen P022 first-reentry kernel at its isolated arithmetic boundary: for a twin center r with q=3r-1 prime and the required prime-boundary constellation, prove or refute q | F_r in the surviving q≡17,35 (mod 72) classes, or reduce the route to the smallest exact finite-field/p-adic identity that remains genuinely open.",
  "next_action": "Start from program/p022-geometry-v2@c07ca4c719117829fe2c6919bbe635a1e97a8c4b. Reconstruct the exact Franel-number convention and first-reentry hypotheses, derive the q=3r-1 boundary congruence symbolically before extending computation, and freeze either an all-r obstruction/proof, an exact counterexample, or the smallest explicit residual identity.",
  "dependencies": [
    "retained source publication TP2-DE338F269CA11E9BC01B from the historical RS-P022-OBSERVATION-HISTORY task-id collision",
    "program/p022-geometry-v2@c07ca4c719117829fe2c6919bbe635a1e97a8c4b first-reentry kernel and midpoint residue obstruction",
    "frozen exact primitive Franel-divisor and Lucas-rank helpers on the same owner lineage"
  ],
  "source_refs": [
    "src/enterprise_math/p022_barlow_twin_escape_midpoint.py@c07ca4c719117829fe2c6919bbe635a1e97a8c4b",
    "src/enterprise_math/p022_barlow_franel_lucas_rank.py@c07ca4c719117829fe2c6919bbe635a1e97a8c4b",
    "src/enterprise_math/p022_barlow_twin_defect_difference.py@c07ca4c719117829fe2c6919bbe635a1e97a8c4b"
  ],
  "evidence_status": "SPLIT_FROM_P022_PUBLICATION_FORK / ORIGINAL_PUBLICATION_RETAINED / BOUNDARY_FRANEL_CORE_OPEN",
  "last_progress_ref": "program/p022-geometry-v2@c07ca4c719117829fe2c6919bbe635a1e97a8c4b",
  "last_progress_at": "2026-08-10T13:47:00+08:00",
  "hard_block": null,
  "tags": ["P022", "Barlow", "Franel", "primitive-divisor", "first-reentry", "split-replay"],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P022-OBS-HIST-ARITHMETIC-CORE",
  "parent_objective_id": "P022_OBSERVATION_HISTORY_COMPLETION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P022OH",
  "origin_kind": "REPLAY_OR_INTEGRATION",
  "task_lineage": "REPLAY",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:497a0467870c4d495d4dbf161cf492e9d3d4a51d0a7b34e685086f25daa395f4",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# P022 Observation-History Primitive Franel Arithmetic Core — Split Replay

Status: `PUBLISHED_REGISTERED / REPLAY_OR_INTEGRATION / REPLAY`

## Mother question

At the exact first-reentry boundary isolated by the frozen P022 observation-history kernel, can a primitive Franel row born at a twin center `r` remain invisible when `q=3r-1` is the reflecting prime? Under the frozen prime-boundary constellation and the surviving classes `q ≡ 17,35 (mod 72)`, prove or refute the remaining divisibility `q | F_r`.

## Frozen inputs and scope

Use `program/p022-geometry-v2@c07ca4c719117829fe2c6919bbe635a1e97a8c4b` and the exact helper sources listed above. The historical source publication `TP2-DE338F269CA11E9BC01B` is retained unchanged as provenance. Treat the first-reentry kernel, twin-blackout identities, primitive-divisor convention, absence of adjacent Franel zeros below the prime, and midpoint obstruction as frozen unless an exact contradiction is found. Finite enumeration may falsify or discover identities but is not proof of an infinite statement.

## Hard target and required outputs

Hard target: `P022_BOUNDARY_FRANEL_ESCAPE_CORE_PROVED_OR_REFUTED_OR_EXACTLY_REDUCED`.

Reconstruct the exact Franel convention and boundary hypotheses; derive the `q=3r-1` divisibility reduction symbolically; pressure-test both surviving residue classes; and return either a general proof/no-go theorem, an exact counterexample, or the smallest explicit finite-field or p-adic identity that remains genuinely open after elementary reductions. Freeze the durable return at `research_returns/P022_OBSERVATION_HISTORY_ARITHMETIC_CORE_RETURN_20260827.md` with any deterministic checker or certificate used.

## Research value to preserve

The earlier P022 work reduced a high-dimensional identifiability defect to one sharp arithmetic gate. Keeping this arithmetic core under its own typed task identity prevents it from being conflated with the forced-midpoint fallback theorem or the later composite-Franel escape frontier while preserving the original immutable evidence.

## Success, kill, and return criteria

Success is an exact theorem, no-go theorem, or exact counterexample at the stated boundary. If the all-r statement cannot be closed, a task-terminal return is valid only after the residual uncertainty is reduced to one explicit identity with elementary and valuation-only routes exhausted. A single counterexample kills a claimed universal obstruction immediately. Do not infer an infinite theorem from a bounded scan.
