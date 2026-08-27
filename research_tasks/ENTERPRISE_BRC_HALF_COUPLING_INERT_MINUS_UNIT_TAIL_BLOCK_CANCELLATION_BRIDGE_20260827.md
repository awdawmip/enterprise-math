<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-MINUS-UNIT-TAIL-BLOCK-CANCELLATION-BRIDGE",
  "title": "Enterprise BRC Half-Coupling Inert Minus Unit-Tail Block Cancellation Bridge",
  "kind": "RESEARCH",
  "owner": "research/enterprise-brc-half-inert-minus-unit-tail-block-cancellation-bridge",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "For inert primes p congruent to 17 or 23 modulo 24, prove or exactly obstruct the cancellation law for the surviving finite-Clausen tail blocks 00,01,02,11 and recover G_p H_p-T_p congruent -p modulo p^3.",
  "next_action": "Start from the exact p=6m+5 block support theorem. Prove the aggregate p-adic divisibilities and first two digits of T00/T01/T02/T11 by a structural cancellation mechanism; do not attempt to discard the unit tail termwise. Use at least two distinct exact routes before returning unclosed.",
  "dependencies": ["research_result_reviews/RR-C7AAFCCFA9417B3F2C0A/DR-9291E2191AE9A09D116E.json@main","research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_FINITE_CLAUSEN_DERIVATIVE_BRIDGE_RETURN_20260827.md@main"],
  "source_refs": ["research_artifacts/ENTERPRISE_BRC_HALF_COUPLING_INERT_FINITE_CLAUSEN_DERIVATIVE_BRIDGE/route_audit_20260827.json@main","Zhi-Wei Sun, Open Conjectures on Congruences, arXiv:0911.5665, Conjecture A14(ii)"],
  "evidence_status": "PARENT_CLASS_SPLIT_ACCEPTED / MINUS_CLASSES_HAVE_GENUINE_UNIT_TAIL / VALUATION_ONLY_ROUTE_REFUTED / CANCELLATION_THEOREM_OPEN",
  "last_progress_ref": "DR-9291E2191AE9A09D116E",
  "last_progress_at": "2026-08-27T09:05:00+00:00",
  "hard_block": null,
  "tags": ["p-adic","inert-primes","17-mod24","23-mod24","Clausen","unit-tail","block-cancellation","supercongruence"],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-MINUS-UNIT-TAIL-BLOCK-CANCELLATION-BRIDGE",
  "parent_objective_id": "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "EBP4M",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-FINITE-CLAUSEN-DERIVATIVE-BRIDGE",
  "successor_gate": {
    "new_information_gap": "The parent proves that for p congruent to 17,23 mod24 the finite Clausen tail contains a genuine valuation-zero I0xI0 triangle and that exactly the 00,01,02,11 block types survive modulo p^3. The missing theorem is cancellation, not valuation.",
    "why_parent_result_does_not_close_it": "Bounded data suggests p-divisibility for 00/01 and p^2-divisibility for 02/11, but no all-prime aggregate cancellation theorem or first-two-digit evaluation has been proved.",
    "discriminating_outcomes": ["Complete proof of the minus-class block cancellation and S_p≡-p mod p^3 for both 17 and 23 mod24.","Proof for one minus residue class with an exact complementary blocker.","Exact counterexample to the candidate aggregate divisibilities or target.","A strictly smaller character-sum, Gamma, involution, or WZ identity controlling the unit tail."],
    "kill_condition": "Any argument that tries to make the I0xI0 unit tail vanish by termwise valuation is already refuted and must be killed. Any bounded divisibility pattern not proved structurally remains regression only.",
    "alternative_route_or_free_exploration_considered": "Preferred routes include an involutive/reflection pairing of the unit triangle, p-adic Gamma expansion of aggregate blocks, finite-field character-sum cancellation, and a parameter-deformed WZ identity. Broad prime-range extension is lower value.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The parent has proved that these classes contain a unit tail absent from the plus classes. This creates a genuinely different proof mechanism and justifies a separate task contract."
  },
  "policy_review": {"policy_set":"research_taskbook_policy.json","policy_digest":"sha256:497a0467870c4d495d4dbf161cf492e9d3d4a51d0a7b34e685086f25daa395f4","review_state":"PASS","temporary_overrides":[]}
}
-->

# Enterprise BRC Half-Coupling Inert Minus Unit-Tail Block Cancellation Bridge

Status: `PUBLISHED_REGISTERED / DRIVER SUCCESSOR / CONTINUATION / EXACT_PROOF`

## Mother question

For every prime `p ≡ 17,23 (mod 24)`, prove or exactly refute

\[
G_pH_p-T_p\equiv -p\pmod{p^3}
\]

by controlling the four surviving finite-Clausen tail block types `00,01,02,11`. The parent has proved that a genuine valuation-zero `I_0×I_0` triangle lies in the tail, so the required theorem is a cancellation theorem rather than a valuation-disposal theorem.

## Frozen inputs and scope

Consume the exact finite identity `S_p=G_pH_p-T_p`, the `p=6m+5` valuation blocks, and the exact support decomposition showing that modulo `p^3` only `00`, symmetric `01`, symmetric `02`, and `11` survive. The `12` and `22` blocks vanish termwise and need not be revisited.

The bounded observations `p|T00`, `p|T01(two-sided)`, `p^2|T02(two-sided)`, `p^2|T11` are candidates only. They may guide the proof but are not frozen theorems.

Any successful route must explain cancellation of the unit tail. Pure termwise valuation is excluded by the parent no-go. Finite regression is falsification support only.

## Hard target and required outputs

Hard target: `INERT_MINUS_UNIT_TAIL_BLOCK_CANCELLATION_BRIDGE_PROVED_REFUTED_OR_EXACTLY_REDUCED`.

Required outputs: exact all-prime aggregate block identities/divisibilities or an exact counterexample; first two relevant p-adic digits needed to combine with `G_pH_p`; separate treatment of classes 17 and 23 mod24; complete dependency/precision bookkeeping; a deterministic checker only for regression; and durable return `research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_MINUS_UNIT_TAIL_BLOCK_CANCELLATION_BRIDGE_RETURN_20260827.md`.

## Research value to preserve

This is the genuinely difficult half exposed by the parent class split: the correction includes p-adic units, so the mechanism must be structural cancellation. A proof would close the negative-sign inert half of Sun's target; a refutation or smaller exact identity would prevent repeated false closures based on valuation heuristics.

## Success, kill, and return criteria

Freeze one of `INERT_MINUS_BRIDGE_PROVED`, `INERT_MINUS_TARGET_REFUTED`, `ONE_MINUS_CLASS_PROVED`, `UNIT_TAIL_ROUTE_EXACT_NO_GO`, or `PROOF_NOT_CLOSED_WITH_SMALLER_CANCELLATION_IDENTITY`.

Any exact violation of the target or candidate block divisibility must be independently recomputed and frozen. No bounded pattern is theorem evidence. Do not reopen the plus classes or reissue the undifferentiated inert task. Stop at the strongest exact statement and return for Driver review.
