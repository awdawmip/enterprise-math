<!-- ENTERPRISE_MATH_TASK_V1
{
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "parent_objective_id": "EM-FREE-W59A-JT2-RAMANUJAN-LEGENDRE",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:1f84e78de591605da6106f3f14ffad3cd7fad66aa5bf67e29beb44906b976c8a",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "task_id": "RS-EMW59A-JT2-UR-SUN-PARITY-DEFECT",
  "title": "JT2 UR-Legendre via Sun parity-defect elimination",
  "frontier": "CM0 and simple-root transversality are closed; the divided-value formula has been reduced by the barycentric generalized-Legendre lift. The remaining UR obstruction is the local slope-value congruence 3 P_{p-1}(-1/3,t) P_n'(t) == -p t (mod p^2), with p^2 parity defects at the Frobenius ports still to be eliminated.",
  "next_action": "At the t and -t Frobenius ports, write Sun's a=-1/3 p^3 parameter recurrence together with its x-derivative, retain the p^2 even/odd defect coordinates for the center and adjacent parameters, and eliminate the adjacent values to derive the slope-value congruence.",
  "dependencies": [],
  "source_refs": [
    "research_notes/EMW59A_JT2_COMPLETE_RELEASE_AND_DRIVER_HANDOFF_20260909.md",
    "research_notes/EM_FREE_W59A_JT2_UR_QTF3_STATE_MACHINE_HANDOFF_20260909.md",
    "global-knowledge:awdawmip/chatgpt-global-knowledge@f48cd4d076f61a5b804a7617158359e198b2fd5d:journal/progressive-number-theory/2026-09-09/20260909T105443+0800-ur-legendre-barycentric-lift.md",
    "https://arxiv.org/abs/1101.5386"
  ],
  "evidence_status": "FREE_RESEARCH_JT2_DURABLE_HANDOFF",
  "last_progress_ref": "research_notes/EM_FREE_W59A_JT2_UR_QTF3_STATE_MACHINE_HANDOFF_20260909.md",
  "last_progress_at": "2026-09-09T11:03:17+08:00",
  "hard_block": "SUN_PARITY_DEFECT_SLOPE_VALUE_ELIMINATION",
  "tags": [
    "EM-FREE-W59A",
    "JT2",
    "UR-Legendre",
    "generalized-Legendre",
    "Sun",
    "p-adic",
    "Frobenius-port",
    "BRC"
  ],
  "registry_key": "RS-EMW59A-JT2-UR-SUN-PARITY-DEFECT",
  "identity_lane": "RW59UR",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null
}
-->

# JT2 UR-Legendre via Sun parity-defect elimination

Status: `READY / FREE-RESEARCH INTEGRATION / PUBLISHED_REGISTERED`

## 0. Mother question

Can Sun's generalized-Legendre parameter recurrence at `a=-1/3`, evaluated at the two Frobenius ports `t` and `-t` with its differentiated recurrence, close the remaining UR-Legendre congruence
`3 P_{p-1}(-1/3,t) P_n'(t) == -p t (mod p^2)`?

## 1. Frozen inputs and scope

Read `research_notes/EM_FREE_W59A_JT2_UR_QTF3_STATE_MACHINE_HANDOFF_20260909.md` first.

Work under the exact prime and Frobenius hypotheses of that handoff; at minimum the current branch has `p=3n+1`, `p>3`, `t^2=1/2`, and the exchanged-port relation used by the defect calculation. If an additional congruence class is needed for a parity sign, state and prove the precise restriction rather than silently adding it.

Consume rather than replay: CM0; simple-root transversality; `Q_m'(1/2)=P_n'(t)/(2t)`; and the barycentric lift
`3P_{p-1}(-1/3,x) == P_{2n}(x)+2P_n(x) (mod p^2)`.

Retain `p`-adic valuation, the two port labels, derivative jets, and the `p^2` reflection defects. Do not replace a congruence-level parity statement by an exact even/odd identity. The retired five harmonic-block decomposition is outside the primary route.

## 2. Hard target and required outputs

Hard target: `SUN_PARITY_DEFECT_SLOPE_VALUE_ELIMINATION`.

Deliver:

1. An exact derivation, for every prime in the stated scope, of
   `3 P_{p-1}(-1/3,t) P_n'(t) == -p t (mod p^2)`.
2. An explicit definition of the `p^2` parity-defect coordinates at `t,-t` and a derivation of their balance from Sun's `p^3` parameter recurrence.
3. A correct use of the differentiated recurrence that eliminates the adjacent generalized-Legendre values without discarding the defect terms.
4. The short deduction of
   `(P_{2n}(t)+2P_n(t))P_n'(t) == -p t (mod p^2)`
   from the barycentric lift.
5. The resulting bridge back to the original UR unit-reciprocity obstruction, with every division by `p` justified by the frozen CM0 valuation.
6. If the Sun recurrence is insufficient, an exact obstruction identifying the smallest additional congruence or jet identity required.

## 3. Research value to preserve

This task isolates the first genuinely unresolved unit in the UR line after the CM zero, transversality, and divided-value expression have been compressed away. A proof replaces a supersingular-unit reciprocity statement by one ordinary-Legendre slope-value certificate. A negative result is also valuable if it identifies exactly which `p^2` defect coordinate survives the recurrence, because later work can target that coordinate directly without recreating discarded harmonic data.

## 4. Success, kill, and return criteria

Success is a uniform proof of the displayed slope-value congruence on the exact prime/Frobenius scope, with the valuation and two-port defect bookkeeping visible.

Kill any derivation that proves only a modulo-`p` parity relation, sets a `p^2` defect to zero without proof, divides by `p` before establishing divisibility, or uses numerical agreement as the final argument.

Return either the full proof and the UR deduction, or a minimal exact obstruction with a falsifiable next identity. The task grants no Working Truth or Foundation status merely by being published.
