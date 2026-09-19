<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-EMW59A-JT2-UR-SUN-PARITY-DEFECT",
  "title": "JT2 UR-Legendre: norm-jet scalar evaluation",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "Exact finite Sun parity/derivative elimination and Frobenius-aware Wronskian normalization are reviewed. The original UR target is equivalent to epsilon_p=0, with a degree<=2n+1<p norm-jet certificate; its all-prime value remains unknown.",
  "next_action": "Use the exact specified P_n and its primitive I_n to seek a uniform arithmetic evaluation of epsilon_p on p=13,19 mod24, preserving the inherited CM0/SIMPLE scope. Consume the prior elimination and test any proposed new arithmetic relation against full polynomial realizability.",
  "dependencies": [],
  "source_refs": [
    "https://github.com/awdawmip/enterprise-math/blob/969846f1d451b3e086f34a19b217e333c8a90c8d/research_result_records/RS-EMW59A-JT2-UR-SUN-PARITY-DEFECT/RR-60983E048B55C2AC7F66.json",
    "https://github.com/awdawmip/enterprise-math/blob/969846f1d451b3e086f34a19b217e333c8a90c8d/research_returns/EMW59A_JT2_UR_SUN_PARITY_DEFECT_RETURN_EF9380_20260910.md",
    "https://github.com/awdawmip/enterprise-math/blob/969846f1d451b3e086f34a19b217e333c8a90c8d/research_task_records/RS-EMW59A-JT2-UR-SUN-PARITY-DEFECT/TP2-22F5729C777040ECA121.json",
    "driver_reviews/JT2_UR_NORM_JET_STAGE_REVIEW_57CCCE_20260920.md",
    "research_artifacts/JT2_PERSISTENT_LINE_DRIVER_20260909/reviews/ur_norm_jet_57ccce_20260920/prior_art_review.md"
  ],
  "evidence_status": "DRIVER_REVIEW_FOLLOWUP_V1",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": "UNIFORM_UR_NORM_JET_VANISHING",
  "tags": [
    "MATHEMATICAL_CONTINUATION",
    "DRIVER_AUTO_FOLLOWUP",
    "JT2",
    "NORM_JET",
    "SAME_TASK_NEW_GENERATION",
    "UR_OPEN",
    "RESULT_ONLY"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-EMW59A-JT2-UR-SUN-PARITY-DEFECT",
  "parent_objective_id": "EM-FREE-W59A-JT2-RAMANUJAN-LEGENDRE",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "RW59UR",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-EMW59A-JT2-UR-SUN-PARITY-DEFECT",
  "successor_gate": {
    "new_information_gap": "Evaluate the specified arithmetic scalar epsilon_p=9(P_n(t)/p)(P_n'(t)/t)-2I_n(t)/t-3 modulo p on every admissible prime. The reviewed return gives its exact equivalence to UR and a degree<=2n+1 certificate, but not its value.",
    "why_parent_result_does_not_close_it": "The exact Sun/derivative elimination and degree-p normalization only produce EQUIV. No all-prime vanishing, admissible counterexample, or full-system logical-independence certificate is provided.",
    "discriminating_outcomes": [
      "A uniform exact proof of epsilon_p=0 and the original UR congruence",
      "An exact admissible prime counterexample with all frozen hypotheses verified",
      "A rigorously identified unresolved arithmetic step, explicitly PARTIAL and not another SUCCESS-by-reformulation claim"
    ],
    "kill_condition": "Reject a route that drops x^p, sets a p² defect to zero without proof, uses freely perturbed jets incompatible with fixed Legendre coefficients, divides by p before CM0, or treats finite examples/equivalent rewriting as uniform UR proof.",
    "alternative_route_or_free_exploration_considered": "Considered continuing the unchanged gen2 instructions, a duplicate new Task-ID, the existing certificate audit/final integration, and independent unrelated exploration. Gen2's elimination is completed; audit/integration require a UR certificate as input. A new Task-ID is unnecessary. A revised publication of this same UR task preserves the exact mother question and consumes the verified reduction.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "This is a new generation of the same Task, not a new Task-ID or direction. It retains the uniform UR target, removes completed elimination from the to-do list, and makes the genuinely unevaluated norm-jet scalar the first action. Closure is unjustified while that scalar remains open."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:98ee2981553fb4eeaf5bd8599513719ee2ac987fae875e9c5daf8a3e2156f3cf",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# JT2 UR-Legendre: norm-jet scalar evaluation

Status: `READY / DRIVER REVIEW FOLLOW-UP / PENDING IMMUTABLE PUBLICATION`

## 0. Mother question

For every prime p>3 with p=13 or19 modulo24, n=(p-1)/3 and 2t²=1 on the exchanged Frobenius branch, does 3P_{p-1}(-1/3,t)P_n'(t)=-pt modulo p² hold?

## 1. Frozen inputs and scope

Use the unchanged RR-60983E048B55C2AC7F66 and its repaired attachment source de3e3c02df785b2ac7c62623d9d5efaece0b15fa, the accompanying Driver stage review, and the original gen2 source handoff. Preserve p>3, p mod24 in {13,19}, n=(p-1)/3, R=Z_(p), A=R[t]/(2t²-1), CM0 and SIMPLE. Consume BL, A/C-ELIM, DEF-ELIM, FROB-NORM, EQUIV, the legal original G_div normalization and accepted QTF3. No old77-prime scan, retired harmonic-block reconstruction, QTF3 re-review, or free-jet perturbation is a default task. I_n is the exact polynomial primitive with I_n(0)=0. The same-task prior generation is TP2-22F5729C777040ECA121; this publication does not reopen an old claim or authorize execution.

## 2. Hard target and required outputs

Hard target remains the original uniform UR slope-value congruence. Deliver (1) a uniform proof or exact admissible counterexample to 9P_n(t)P_n'(t)=p(2I_n(t)+3t) modulo p²; (2) the corresponding conclusion for 3B(t)P_n'(t)=-pt and the original UR product through the accepted EQUIV/BL/coordinate bridge; (3) explicit preservation of p-integrality, exact prime scope, the x^p normalization and full polynomial realizability in every new argument; (4) if unresolved, the precise remaining arithmetic step and a truthful PARTIAL return, not a claim that an equivalent new scalar proves UR.

## 3. Research value to preserve

A uniform proof closes the original UR obligation; an exact counterexample with all hypotheses checked is decisive negative evidence. A failed route should isolate genuine missing arithmetic information without discarding coefficients, valuations, ports or jets.

## 4. Success, kill, and return criteria

Success requires a uniform proof of the original target on the entire stated scope, or an exact admissible counterexample establishing its failure. Further reformulation, finite agreement or a generic rank/kernel observation is not success. Preserve all exact computations as finite evidence. If neither decisive outcome is reached, return PARTIAL with the smallest actual unfinished arithmetic step. Do not claim logical independence without an admissible full-system witness. No Working Truth/Foundation/L4 status or researcher execution authority is granted by this task publication.
