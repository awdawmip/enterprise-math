<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P022-OBSERVATION-HISTORY",
  "title": "P022 Observation-History Primitive Franel Escape Core — Current-Policy Replay",
  "kind": "RESEARCH",
  "owner": "program/p022-geometry-v2",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Resume the frozen P022 first-reentry kernel at its isolated arithmetic boundary: for a twin center r with q=3r-1 prime and the required prime-boundary constellation, prove or refute q | F_r in the surviving q≡17,35 (mod 72) classes, or reduce the route to the smallest exact finite-field/p-adic identity that remains genuinely open.",
  "next_action": "Start from program/p022-geometry-v2@c07ca4c719117829fe2c6919bbe635a1e97a8c4b. Reconstruct the exact Franel-number convention and first-reentry hypotheses, derive the q=3r-1 boundary congruence symbolically before extending computation, and freeze either an all-r obstruction/proof, an exact counterexample, or the smallest explicit residual identity.",
  "dependencies": [
    "program/p022-geometry-v2@c07ca4c719117829fe2c6919bbe635a1e97a8c4b first-reentry kernel and midpoint residue obstruction",
    "frozen exact primitive Franel-divisor and Lucas-rank helpers on the same owner lineage"
  ],
  "source_refs": [
    "src/enterprise_math/p022_barlow_twin_escape_midpoint.py@c07ca4c719117829fe2c6919bbe635a1e97a8c4b",
    "src/enterprise_math/p022_barlow_franel_lucas_rank.py@c07ca4c719117829fe2c6919bbe635a1e97a8c4b",
    "src/enterprise_math/p022_barlow_twin_defect_difference.py@c07ca4c719117829fe2c6919bbe635a1e97a8c4b"
  ],
  "evidence_status": "LEGACY_HANDOFF_REPLAY / EXACT_FIRST_REENTRY_KERNEL_FROZEN / BOUNDARY_FRANEL_CORE_OPEN",
  "last_progress_ref": "program/p022-geometry-v2@c07ca4c719117829fe2c6919bbe635a1e97a8c4b",
  "last_progress_at": "2026-08-10T13:47:00+08:00",
  "hard_block": null,
  "tags": [
    "P022",
    "Barlow",
    "Franel",
    "primitive-divisor",
    "first-reentry",
    "legacy-migration"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P022-OBSERVATION-HISTORY",
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

# P022 Observation-History Primitive Franel Escape Core — Current-Policy Replay

Status: `PUBLISHED_REGISTERED / REPLAY_OR_INTEGRATION / REPLAY`

## Mother question

At the exact first-reentry boundary isolated by the frozen P022 observation-history kernel, can a primitive Franel row born at a twin center `r` remain completely invisible when `q=3r-1` is the reflecting prime? Equivalently, under the frozen prime-boundary constellation and the surviving residue classes `q ≡ 17,35 (mod 72)`, prove or refute the remaining divisibility `q | F_r`, where `F_r` is the Franel number used by the owner lineage.

## Frozen inputs and scope

Use `program/p022-geometry-v2@c07ca4c719117829fe2c6919bbe635a1e97a8c4b` as the replay source. Treat the existing first-reentry kernel classification, twin-blackout identities, primitive-divisor convention, absence of adjacent Franel zeros below the prime, and the midpoint obstruction reducing boundary escape to `q ≡ 17,35 (mod 72)` as frozen inputs unless an exact contradiction is found.

The task is arithmetic and exact. Finite enumeration may falsify or discover identities but is not proof of an infinite statement. Do not broaden into a Barlow-animal census, generic collision geometry, continuum asymptotics, or unrelated prime-pattern searches. New general-purpose machinery is allowed only if the existing owner helpers cannot express the exact residual congruence.

## Hard target and required outputs

Hard target: `P022_BOUNDARY_FRANEL_ESCAPE_CORE_PROVED_OR_REFUTED_OR_EXACTLY_REDUCED`.

Required outputs are: a self-contained reconstruction of the exact Franel convention and boundary hypotheses; a symbolic reduction of `q | F_r` at `q=3r-1`; exact pressure tests in both surviving residue classes; and one of (i) a general proof that the divisibility is impossible under the frozen constellation, (ii) a general proof/classification of when it occurs, (iii) an exact counterexample that closes the proposed escape obstruction, or (iv) the smallest explicit finite-field or p-adic identity whose proof is genuinely still missing after all elementary reductions. Freeze the result in `research_returns/P022_OBSERVATION_HISTORY_ARITHMETIC_CORE_RETURN_20260827.md`, with any deterministic checker and machine-readable certificate used.

## Research value to preserve

The previous P022 work has already reduced a high-dimensional identifiability defect to one sharp arithmetic gate. Closing or sharply reducing this gate determines whether the first-reentry observation-history mechanism can fail at its most dangerous reflection boundary, and prevents future work from expanding finite cutoffs or adding local congruences before the actual obstruction is understood.

## Success, kill, and return criteria

Success is an exact theorem, no-go theorem, or exact counterexample at the stated boundary. If the all-r statement cannot be closed, a task-terminal return is still valid only after the residual uncertainty has been reduced to one explicit identity with all elementary and valuation-only routes exhausted and with exact finite evidence clearly labeled as such. A single counterexample to a claimed universal obstruction kills that obstruction immediately. Do not claim an infinite theorem from a bounded scan.
