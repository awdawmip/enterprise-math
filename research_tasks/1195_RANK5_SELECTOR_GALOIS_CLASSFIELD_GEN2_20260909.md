<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-1195-RANK5-SELECTOR-GALOIS-CLASSFIELD",
  "title": "1195: Arithmetic Descent of the Rank-5 Pi-Free q-Selector",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "Later #1195 work supersedes the earlier CP15 frontier. CP17 gives a conditional selector-descent theorem under row-wise period factorization; CP18 identifies the selector intrinsically as the odd-period maximal-minor/Gauss map; CP19 eliminates the explicit 1/pi^2 scale from Almkvist-Guillera's q-parametrization and gives two exact pi-free projective q-ratios. The smallest unresolved arithmetic question is now to prove algebraicity and Galois transport of those two ratios at a genuinely modular/CM rank-5 specialization, or to identify the exact obstruction.",
  "next_action": "Choose one rank-5 family for which modular/CM special-value algebraicity is proved independently, write the two CP19 pi-free projective q-ratios in that family's modular coordinates, and prove that their values lie in the expected arithmetic field and conjugate equivariantly. If this fails, isolate the first q-function or period-normalization factor whose value is not controlled by the available CM theorem.",
  "dependencies": [],
  "source_refs": [
    "research_notes/1195_research_handoff_index_20260909.md",
    "research_notes/1195_research_handoff_postcp16_20260909.md",
    "issue:1195#issuecomment-5576393018",
    "issue:1195#issuecomment-5576406515",
    "issue:1195#issuecomment-5576426514"
  ],
  "evidence_status": "RESEARCH_HANDOFF_RECONCILED_V2",
  "last_progress_ref": "research_notes/1195_research_handoff_postcp16_20260909.md",
  "last_progress_at": "2026-09-09T01:05:00+08:00",
  "hard_block": "CM_DESCENT_OF_TWO_PI_FREE_RANK5_Q_SELECTOR_RATIOS",
  "tags": ["1195","rank5","selector","Gauss-map","q-parametrization","CM","class-field","Galois"],
  "claim_lease_minutes": 180,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-1195-RANK5-SELECTOR-GALOIS-CLASSFIELD",
  "parent_objective_id": "EM-PI-POWER-SPECTRAL-SELECTOR",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "R1195G",
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

# 1195: Arithmetic Descent of the Rank-5 Pi-Free q-Selector

Status: `READY / RECONCILED SUCCESSOR GENERATION / PUBLISHED_REGISTERED`

## 0. Mother question

At a proved modular or CM specialization of a rank-5 Ramanujan-Sato/Calabi-Yau family, do the two explicit pi-free projective q-ratios obtained in #1195 CP19 lie in the expected arithmetic/class field and satisfy Galois transport, and what minimal special-value theorem makes that descent exact?

## 1. Frozen inputs and scope

Read both #1195 handoff notes before execution. Consume CP17 `5576393018`, CP18 `5576406515`, and CP19 `5576426514`; do not restart from the older CP15 generic cross-product frontier.

Frozen facts:

- row-wise period factorization is sufficient for projective selector descent, but full period algebraicity is not required;
- the selector is the maximal-minor/Gauss map of the normalized odd-period jet matrix;
- Almkvist–Guillera's rank-5 q-parametrization can be projectivized so the explicit `1/pi^2` scale cancels identically;
- outside proved modular subfamilies, the special-value algebraicity package is conjectural, so an unconditional theorem for arbitrary fifth-order Calabi-Yau equations is out of scope.

The scalar `c=1` Borwein/Masser theorem is completed background. The target `1/pi^2` evaluation may be used only as later compatibility, not as an input to algebraize the projective selector.

## 2. Hard target and required outputs

Hard target: `CM_GALOIS_DESCENT_OF_RANK5_Q_SELECTOR_OR_EXACT_OBSTRUCTION`.

Deliver all of the following, or an exact negative boundary replacing an impossible item:

1. Select one rank-5 family with independently proved modular/CM parametrization or special-value algebraicity. State the exact theorem used and its arithmetic field.
2. Write the CP19 two projective q-ratios explicitly in the chosen modular coordinates, with every period, mirror, Yukawa, logarithmic, or extension factor typed.
3. Prove that the two ratios are algebraic in a specified field and transform equivariantly under at least one nontrivial Galois/class-field conjugation, or isolate the first uncontrolled factor that prevents the proof.
4. Reformulate the proof in the CP18 maximal-minor language and identify whether arithmetic descent occurs by row-wise scalar factorization or by a weaker direct descent of minor ratios.
5. Check one exact conjugate orbit, minimal polynomial, or class-field relation without relying on decimal recognition as proof.
6. State precisely which ingredients are classical modular/CM prior art and which part is the pi-free selector synthesis.
7. After the single-family theorem/no-go, state the strongest justified hypothesis for a general rank-5 descent theorem and the first reason it may fail outside modular families.

Do not require algebraicity of the full rank-5 period vector if projective minor ratios already descend.

## 3. Research value to preserve

The route has already proved that the rank-5 selector exists generically and is a target-free projective observable. It has also reduced the arithmetic problem to two explicit q-ratios. The remaining question is now genuinely arithmetic and sharply finite: whether those ratios are class-field/Galois observables at modular/CM points.

A positive result would upgrade the scalar `c=1` class-field phenomenon to a higher-rank projective selector. A negative result would identify the exact additional period or extension datum that prevents elliptic-style descent and therefore delimit the general `1/pi^c` program.

## 4. Success, kill, and return criteria

Success is a proved modular/CM rank-5 example with algebraic two-ratio selector and exact Galois transport, together with the minimal sufficient special-value hypothesis; or an exact obstruction showing why such descent cannot be deduced even in the selected family.

Kill any route that redoes the generic Gauss-map derivation, algebraizes the entire period vector unnecessarily, uses the even `1/pi^2` completion equation to choose the projective ray, treats conjectural Almkvist–Guillera algebraicity as proved in a non-modular family, or identifies the field only by floating-point matching.

Return the first exact descent theorem, exact failed factor, or strictly smaller arithmetic frontier.