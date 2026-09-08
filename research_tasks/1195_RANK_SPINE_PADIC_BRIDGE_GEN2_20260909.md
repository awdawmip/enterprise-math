<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-1195-RANK-SPINE-PADIC-BRIDGE",
  "title": "1195: Projected Middle-Selector Relative p-adic Error Depth",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "Later #1195 work substantially resolves the broad rank-spine question. Roberts-Rodriguez Villegas already supply the relevant Hodge-gap prior-art framework. CP28 proves the exact term-valuation staircase; CP29 explains the leading p^c valuation from the middle filtration under standard strongly-divisible input; CP30 kills simple pairwise involutions; CP31 constructs the p-adic selector Gauss map; CP32 proves the mixed archimedean/p-adic identification budget. The smallest unresolved p-adic unit is the extra c+1 relative-error digits needed to lift the projected middle-selector contribution from p^c to the observed p^(2c+1) depth.",
  "next_action": "Fix a proved c=2 supercongruence with the middle Artin-Tate line already identified, express its weighted finite sum as the CP31 projected selector/Dwork block, and prove or falsify a relative congruence modulo p^(c+1)=p^3 after factoring the leading p^c. Use the explicit terminating/WZ, Dwork quotient, or p-adic Gamma structure of that example; then test whether the mechanism survives one c=3 case.",
  "dependencies": [],
  "source_refs": [
    "research_notes/1195_research_handoff_index_20260909.md",
    "research_notes/1195_research_handoff_postcp16_20260909.md",
    "issue:1195#issuecomment-5576623215",
    "issue:1195#issuecomment-5576660404",
    "issue:1195#issuecomment-5576674540",
    "issue:1195#issuecomment-5576697400",
    "issue:1195#issuecomment-5576753904",
    "issue:1195#issuecomment-5576765125"
  ],
  "evidence_status": "RESEARCH_HANDOFF_RECONCILED_V2",
  "last_progress_ref": "research_notes/1195_research_handoff_postcp16_20260909.md",
  "last_progress_at": "2026-09-09T01:05:00+08:00",
  "hard_block": "EXTRA_C_PLUS_1_RELATIVE_PADIC_DIGITS_FOR_PROJECTED_MIDDLE_SELECTOR",
  "tags": ["1195","p-adic","supercongruence","middle-filtration","selector","Dwork","relative-error","Hodge-gap"],
  "claim_lease_minutes": 180,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-1195-RANK-SPINE-PADIC-BRIDGE",
  "parent_objective_id": "EM-PI-POWER-SPECTRAL-SELECTOR",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "R1195P",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:dd425305887871866cb2f0894885ff38359639e2de7750fa45e8c584e19feae4",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 1195: Projected Middle-Selector Relative p-adic Error Depth

Status: `READY / RECONCILED SUCCESSOR GENERATION / PUBLISHED_REGISTERED`

## 0. Mother question

After the degree-`c` selector and middle filtration account for the leading `p^c` valuation of a Ramanujan `1/pi^c` finite sum, what exact global p-adic mechanism supplies the additional `c+1` relative digits needed for the projected middle eigenvalue to match the observed `p^(2c+1)` supercongruence depth?

## 1. Frozen inputs and scope

Read both #1195 handoff notes before execution. Consume CP27 through CP32; do not restart from the broad observation that the number `2c+1` appears on both archimedean and p-adic sides.

Frozen facts and boundaries:

- Roberts–Rodriguez Villegas already connect Hodge gaps and accelerated hypergeometric supercongruences; do not claim that general principle as new;
- the exact Pochhammer valuation staircase is proved;
- under standard strongly-divisible/crystalline hypotheses the middle filtration supplies the leading `p^c` scale;
- simple reflection/pairwise cancellation inside the low-slope block has an exact no-go;
- the p-adic coefficient constraints form a projective selector/Gauss map, and archimedean plus p-adic coefficient-identification precision already has an exact mixed-place uniqueness theorem;
- the complex selector cannot by itself recover the finite Artin character.

The remaining target is relative depth, not the existence of the middle Tate/Artin line and not a generic Hodge-gap restatement.

## 2. Hard target and required outputs

Hard target: `PROJECTED_MIDDLE_SELECTOR_RELATIVE_DEPTH_C_PLUS_1_PROVED_OR_KILLED`.

Deliver all of the following, or an exact negative boundary replacing an impossible item:

1. Choose one proved `c=2` Ramanujan/Guillera supercongruence with an explicit finite-sum proof technology and state the exact good-prime range and target congruence.
2. Factor the leading `p^c` middle-filtration contribution in a way compatible with the CP31 p-adic selector/Gauss-map formulation.
3. Prove a relative congruence of depth at least `c+1` for the projected middle component, or exhibit an exact prime/family obstruction showing that the missing digits arise from another summand or normalization.
4. Identify the global cancellation mechanism: terminating identity, WZ/telescoping certificate, Dwork quotient, p-adic Gamma expansion, Frobenius projector, or another exact block-level operator. Pairwise term cancellation is already ruled out.
5. Separate the classical Hodge-gap/Dwork input from the new selector-projection statement. State which part is inherited prior art and which part is needed to connect the project precision architecture to that theorem.
6. Test one `c=3` example after the `c=2` mechanism is understood. A counterexample at `c=3` is acceptable and should delimit the scope.
7. Explain whether the first negative bilateral jet or inhomogeneous Frobenius extension from CP33–CP34 participates in the proof; if not, keep that regulator direction separate rather than forcing a unification.

A successful negative result may show that the `c+1` relative digits are not determined by the selector/middle projector alone. It must identify the exact missing Frobenius, unit-root, or extension datum.

## 3. Research value to preserve

The broad numerical coincidence has already been converted into a typed arithmetic picture: middle Hodge depth explains the leading `p^c`, the selector organizes finite coefficient constraints, and the Artin–Tate line supplies the special rank-one arithmetic channel. Only the extra `c+1` relative digits remain between that structure and the full `p^(2c+1)` congruence.

Closing this gap would give the first exact bridge from the pi-free projective selector to accelerated p-adic precision. Killing it would prevent the selector from being overcredited for arithmetic information that actually lives in a finer Frobenius/unit-root extension.

## 4. Success, kill, and return criteria

Success is an exact `c=2` relative-depth theorem in the projected middle-selector language, with a second-rank test and an explicit mechanism for the additional digits; or an exact counterexample locating the missing p-adic datum.

Kill any route that only restates the known Hodge-gap principle, argues from `2c+1` numerology, uses prime-by-prime experiments as proof, reopens the pairwise involution route already killed in CP30, or conflates the leading `p^c` filtration result with the unresolved relative `p^(c+1)` improvement.

Return the first exact relative-depth proof, exact separating counterexample, or strictly smaller Frobenius/extension frontier.