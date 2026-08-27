<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P022-OBS-HIST-FORCED-MIDPOINT",
  "title": "P022 Observation-History Franel Forced-Midpoint Fallback — Split Replay",
  "kind": "RESEARCH",
  "owner": "program/p022-geometry-v2",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Freeze and independently replay-verify the strongest durable P022 primitive-twin forced-midpoint capture theorem: for target primes q congruent to 5 or 23 modulo 24 whose first Franel zero is a nontrivial twin center r, prove that q<6r-1 forces positive defect capture no later than the midpoint segment, while isolating q>=6r-1 as the exact surviving high-range frontier.",
  "next_action": "Start from program/p022-geometry-v2@603ef1c72245612359f8b59cab7a492de21a9166. Audit the exact signed midpoint support, primitive-zero exclusions, the q=23 mod 24 prime-midpoint dangerous index, and the earlier twin-blackout capture implication; run an independent exact recurrence falsification scan and freeze the bounded theorem without claiming the high-range residue is solved.",
  "dependencies": [
    "retained source publication TP2-D78DBA0243911E0363FA from the historical RS-P022-OBSERVATION-HISTORY task-id collision",
    "program/p022-geometry-v2@603ef1c72245612359f8b59cab7a492de21a9166",
    "src/enterprise_math/p022_barlow_forced_midpoint_fallback.py@blob:6c6e8399e622f36015367aa4694e9de62adcb8d7",
    "src/enterprise_math/p022_barlow_twin_transport_closure.py@blob:80bd39a143ed0b4cb8ca5624128b4f823db00d8d"
  ],
  "source_refs": [
    "src/enterprise_math/p022_barlow_forced_midpoint_fallback.py",
    "src/enterprise_math/p022_barlow_franel_midpoint_harmonic_pairing.py",
    "src/enterprise_math/p022_barlow_twin_transport_closure.py",
    "src/enterprise_math/p022_barlow_twin_general_high_transfer.py"
  ],
  "evidence_status": "SPLIT_FROM_P022_PUBLICATION_FORK / ORIGINAL_PUBLICATION_RETAINED / DURABLE_OWNER_THEOREM_REPLAY_OPEN",
  "last_progress_ref": "program/p022-geometry-v2@603ef1c72245612359f8b59cab7a492de21a9166",
  "last_progress_at": "2026-08-12T09:28:26+00:00",
  "hard_block": null,
  "tags": ["P022", "Barlow", "Franel", "primitive-twin", "forced-midpoint", "capture", "split-replay"],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P022-OBS-HIST-FORCED-MIDPOINT",
  "parent_objective_id": "P022_OBSERVATION_HISTORY_AND_COLLISION_GEOMETRY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P022",
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

# P022 Observation-History Franel Forced-Midpoint Fallback — Split Replay

Status: `PUBLISHED_REGISTERED / REPLAY_OR_INTEGRATION / REPLAY`

## Mother question

Let `q>5` be prime with `q ≡ 5` or `23 (mod 24)`, let `m=(q-1)/2`, and suppose the first positive Franel zero modulo `q` occurs at a nontrivial twin center `r`. Determine exactly whether `q<6r-1` is completely captured by the defect family no later than the midpoint segment, including the exceptional signed-support geometry when `q≡23 (mod 24)` and `m` is prime.

## Frozen inputs and scope

Use `program/p022-geometry-v2@603ef1c72245612359f8b59cab7a492de21a9166` and the exact helper sources listed above. The historical source publication `TP2-D78DBA0243911E0363FA` remains immutable provenance. Consume the forced-midpoint identity, adjacent-zero exclusion, primitive first-zero rank, signed-support localization and earlier twin-blackout capture implication only at their exact frozen strength. Later high-range transport modules are context, not premises needed to prove the bounded fallback theorem.

## Hard target and required outputs

Hard target: `P022_FORCED_MIDPOINT_FALLBACK_CAPTURE_EXACT_AND_INDEPENDENTLY_REPLAY_VERIFIED`.

Produce a precise theorem statement; audit the signed support above `B=(q+1)/6`; audit the `q≡23 (mod 24)` prime-midpoint dangerous-index branch; prove that the marker is captured either at the earlier dangerous defect or at `D_m`; run an independent exact-integer recurrence/support falsification scan as regression only; freeze the durable return at `research_returns/P022_OBSERVATION_HISTORY_FORCED_MIDPOINT_FALLBACK_RETURN_20260827.md`; and state explicitly that `q>=6r-1` remains a separate high-range frontier.

## Research value to preserve

This bounded theorem is valuable independently of the later composite-Franel escape program. Giving it a typed task identity preserves the recovered owner theorem and its independent replay requirement without letting a shared historical task ID merge it into a different parent objective.

## Success, kill, and return criteria

Success requires the bounded implication to follow from exact integer identities and frozen owner-local lemmas, with finite scans serving only as regression. Narrow or fail the result if a signed-support term above `B` was omitted, if the dangerous index can cancel the midpoint without an earlier positive defect, or if the range equivalence between `r>B` and `q<6r-1` is incorrect. In that event, return the smallest counterexample or missing premise; do not claim the unresolved high range is solved.
