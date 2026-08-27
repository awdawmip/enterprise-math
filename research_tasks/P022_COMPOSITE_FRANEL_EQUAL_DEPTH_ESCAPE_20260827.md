<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P022-COMPOSITE-FRANEL-EQUAL-DEPTH-ESCAPE",
  "title": "P022 Composite Franel Equal-Depth Escape",
  "kind": "RESEARCH",
  "owner": "program/p022-geometry-v2",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Close, refute, or sharply isolate the surviving composite Franel equal-depth p-adic escape after the first-reentry kernel, transfer-depth reductions, forced-midpoint scale identity, and harmonic pairing U_p=2T_p.",
  "next_action": "Combine the forced-midpoint scale identity with the exact harmonic pairing to derive the first p-adic correction governing v_p(F_(2k-1))=v_p(F_m)>0. Prove equal first jets impossible in the admissible residue classes or freeze the smallest exact exceptional condition.",
  "dependencies": [
    "research_task_records/RS-P022-OBSERVATION-HISTORY/TP2-2346F5D3E731ED56DB0A.json",
    "program/p022-geometry-v2@603ef1c72245612359f8b59cab7a492de21a9166",
    "research_tasks/P022_OBSERVATION_HISTORY_COMPOSITE_FRANEL_ESCAPE_REPLAY_20260827.md@blob:55ab98b3377820daca63825513bbda0b415f4912"
  ],
  "source_refs": [
    "src/enterprise_math/p022_barlow_forced_midpoint_scale_hasse.py@program/p022-geometry-v2",
    "src/enterprise_math/p022_barlow_franel_midpoint_harmonic_pairing.py@program/p022-geometry-v2",
    "src/enterprise_math/p022_barlow_franel_reflection_first_jet.py@program/p022-geometry-v2",
    "src/enterprise_math/p022_barlow_franel_terminal_depth_lift.py@program/p022-geometry-v2"
  ],
  "evidence_status": "RETAINED_P022_SUBFRONTIER / LEGACY_SHARED_TASK_CLAIM_NOT_OPERATIONAL / TYPED_REBINDING",
  "last_progress_ref": "research_task_records/RS-P022-OBSERVATION-HISTORY/TP2-2346F5D3E731ED56DB0A.json",
  "last_progress_at": "2026-08-27T11:45:00+00:00",
  "hard_block": null,
  "tags": [
    "P022",
    "Franel",
    "p-adic",
    "equal-depth",
    "first-jet",
    "identifiability"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P022-COMPOSITE-FRANEL-EQUAL-DEPTH-ESCAPE",
  "parent_objective_id": "P022_OBSERVATION_HISTORY_IDENTIFIABILITY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P022ESC",
  "origin_kind": "REPLAY_OR_INTEGRATION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-P022-OBSERVATION-HISTORY",
  "successor_gate": {
    "new_information_gap": "The retained P022 composite-escape publication isolates an equal-positive-depth signature after the forced-midpoint and transfer reductions, but no valid execution/result chain exists for that subfrontier under its shared legacy task id.",
    "why_parent_result_does_not_close_it": "The accepted q=3r-1 fixed-kernel reduction and the bounded midpoint theorem address different residue and range mechanisms. Neither proves or refutes equality of the surviving positive Franel depths.",
    "discriminating_outcomes": [
      "An exact p-adic first-jet obstruction rules out the equal-depth signature and forces row visibility.",
      "A verified admissible equality witness refutes universal escape closure.",
      "A smaller explicit congruence or exceptional residue class becomes the sole remaining blocker."
    ],
    "kill_condition": "Kill any route that only increases a prime cutoff, replaces depth equality by residue nonvanishing, or imports an unproved generic p-adic independence statement.",
    "alternative_route_or_free_exploration_considered": "The fixed-kernel boundary is separated into its own typed task; the bounded midpoint route is closed. Parking was considered but rejected because the equal-depth signature is an independent, already-developed owner-lineage residue.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The original publication shares a legacy task id whose operational binding belongs to the first-reentry kernel route, so its attempted claim could not be authoritative. Typed rebinding preserves the mathematics without allowing another collision."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:497a0467870c4d495d4dbf161cf492e9d3d4a51d0a7b34e685086f25daa395f4",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# P022 Composite Franel Equal-Depth Escape

Status: `PUBLISHED_REGISTERED / CONTINUATION / TYPED_P022_ARITHMETIC_FRONTIER`

## Mother question

P022 row visibility can still fail only if a surviving composite-defect transport creates an exact equality of positive Franel depths while the adjacent depth vanishes. The durable owner branch reduces this mechanism to a p-adic first-jet problem tied to the forced midpoint and the harmonic pairing

\[
U_p\equiv 2T_p\pmod p.
\]

Determine whether that equal-depth signature is impossible under the admissible P022 hypotheses, or freeze its smallest exact exception.

## Frozen inputs and scope

Use `program/p022-geometry-v2@603ef1c72245612359f8b59cab7a492de21a9166` as the durable source. The first-reentry kernel classification, prime-boundary deletion, zero-transfer and reflection laws, terminal-transfer reductions, forced-midpoint scale identity, and harmonic pairing may be consumed after exact statement audit.

This task does not reopen the bounded `q<6r-1` midpoint theorem and does not replace the separate fixed-kernel nonvanishing problem. It is restricted to the composite equal-depth escape mechanism.

Finite computation may search for a counterexample or test a derived p-adic identity, but it cannot establish an all-prime theorem by cutoff.

## Hard target and required outputs

Hard target:

`P022_COMPOSITE_FRANEL_EQUAL_DEPTH_ESCAPE_CLOSED_OR_MINIMAL_EXCEPTION_FROZEN`

Required outputs:

1. derive the next exact p-adic relation implied by the scale identity and harmonic pairing;
2. prove or refute the surviving equal-depth signature in the admissible residue constellation;
3. reconnect the conclusion to composite-defect row visibility;
4. if universal closure is not justified, state the smallest exact exceptional congruence or verified witness;
5. freeze proof, counterexample, or exact reduction separately from finite regression.

## Research value to preserve

This route replaces a vague composite-index gap by a sharply stated p-adic cancellation mechanism. A proof would close an independent P022 escape channel; a counterexample or minimal exception would prevent false all-index identifiability claims and preserve the useful transfer machinery at its correct strength.

## Success, kill, and return criteria

Success is a proof-level obstruction to equal positive depths, or an exact admissible witness showing that the equality can occur.

Kill a proposed shortcut if it only raises the numerical cutoff, assumes generic p-adic independence, drops a frozen P022 hypothesis, or confuses first-residue nonvanishing with equality of valuations.

If the next p-adic correction reduces to a genuinely independent named congruence, freeze that congruence as the exact blocker rather than continuing by brute force.
