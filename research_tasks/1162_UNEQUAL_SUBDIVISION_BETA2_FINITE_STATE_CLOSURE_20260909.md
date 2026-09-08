<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-1162-UNEQUAL-SUBDIVISION-BETA2-FINITE-STATE-CLOSURE",
  "title": "1162: Unequal-Subdivision Beta2 Finite-State Closure",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "Equal subdivision has an all-order finite Schur-mode closure, and arbitrary positive series-path modules have exact fixed-order finite port packets with serial composition. The unresolved layer is the global arbitrary-unequal-subdivision update for the scalar beta2 future language and the minimal observer-safe state needed across repeated subdivision steps.",
  "next_action": "Start from the exact order-2 edge packet and all-order serial composition law, compose arbitrary positive path replacements on every edge of one weighted cycle, and derive the smallest exact global state update that determines beta2 under a second unequal subdivision without reopening hidden vertices.",
  "dependencies": [],
  "source_refs": [
    "research_notes/1162_research_handoff_index_20260909.md",
    "research_notes/1162_all_order_equal_subdivision_schur_modes_20260908_b62d.md",
    "research_notes/1162_unequal_subdivision_order2_finite_port_jet_20260908_b62d.md",
    "research_notes/1162_series_path_all_order_port_composition_20260908_b62d.md",
    "research_notes/1162_matrix_stieltjes_port_moments_20260908_b62d.md",
    "research_notes/1162_refinement_projector_stability_20260908_b62d.md",
    "research_notes/1162_resolution_admissibility_correction_20260907_b62d.md"
  ],
  "evidence_status": "RESEARCH_HANDOFF_INTEGRATION_V1",
  "last_progress_ref": "research_notes/1162_research_handoff_index_20260909.md",
  "last_progress_at": "2026-09-09T00:36:00+08:00",
  "hard_block": "UNEQUAL_SUBDIVISION_BETA2_GLOBAL_STATE_AND_MINIMALITY",
  "tags": [
    "1162",
    "discrete-rotation-spectrum",
    "weighted-cycle",
    "unequal-subdivision",
    "beta2",
    "finite-port",
    "Schur",
    "rooted-forest",
    "BRC"
  ],
  "claim_lease_minutes": 180,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-1162-UNEQUAL-SUBDIVISION-BETA2-FINITE-STATE-CLOSURE",
  "parent_objective_id": "EM-1162-DISCRETE-ROTATION-SPECTRUM",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "R1162U2",
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

# 1162: Unequal-Subdivision Beta2 Finite-State Closure

Status: `READY / DIRECT USER RESEARCH INTEGRATION / PUBLISHED_REGISTERED`

## 0. Mother question

For a positive weighted cycle whose coarse edges may each be replaced by arbitrary positive series paths, what finite observer state is necessary and sufficient to determine the second scale-free inverse-spectral moment `beta2` through repeated unequal subdivision steps, without reopening hidden vertices or introducing unstable microscopic differentiation?

## 1. Frozen inputs and scope

Read `research_notes/1162_research_handoff_index_20260909.md` first. Consume, do not replay, the exact equal-subdivision all-order Schur closure, the order-2 arbitrary-path finite port theorem, the all-order serial path composition law, and the matrix-valued Stieltjes moment positivity theorem listed there.

The admissible carrier is finite: positive edge resistances; finite weighted Laplacians; formal characteristic/resolvent coefficients; endpoint-labelled Schur packets; integer subdivision operations; rooted-forest coefficients; and finite exact algebra on those objects. A formal probe parameter may be used to name polynomial or resolvent coefficients, but no conclusion may depend on taking a below-resolution derivative or on choosing a smooth interpolation of the integer refinement index.

The classical identification of uniform-cycle fixed coefficients with `zeta(2m)/pi^(2m)` remains a separate compatibility layer. This task is about the finite rough-state law and must not assume the uniform fixed coefficient after rough information has been discarded.

## 2. Hard target and required outputs

Hard target: `UNEQUAL_SUBDIVISION_BETA2_FINITE_STATE_CLOSED_OR_MINIMAL_NO_GO`.

Deliver all of the following, or an exact negative boundary replacing an impossible item:

1. An exact finite update law for replacing every coarse cycle edge by an arbitrary positive series path, using only the already admissible fixed-order edge packets or a proved quotient of them.
2. A finite global state whose value before a subdivision step and finite labelled input for that step determine the next `beta2` readout and remain composable for a further unequal subdivision step.
3. A proof of observer sufficiency: two hidden realizations identified by the proposed state must remain indistinguishable for every allowed future `beta2` operation in scope.
4. A minimality result, dimension lower bound, or explicit fiber-loss witness showing which coordinates cannot be dropped. Do not infer scalar-state minimality from generic independence of the full serial-safe edge packet.
5. A derivative-free admissibility layer using the available matrix-Stieltjes/block-Hankel constraints where relevant, including how exact or interval port data can falsify an impossible packet without converting matrix-valued signed information into positive scalar mass.
6. At least one nontrivial exact rational example that exercises two successive unequal subdivision steps and independently checks the proposed state law or exposes its failure.
7. A return map separating: exact theorem; exact counterexample/no-go; finite computational check; classical compatibility statement; and still-unresolved residue.

A successful negative result may prove that no low-dimensional analogue of the Basel `(H,V;Gamma,U)` state can factor the `beta2` future language, provided the obstruction is exact and the smallest surviving finite carrier is identified or bounded.

## 3. Research value to preserve

The #1162 route now has a stable discrete foundation: integer refinement has bounded finite-projector sensitivity; uniform and rough equal-subdivision cycles have exact finite Schur modes; arbitrary positive path modules have finite serially composable response packets. The remaining scientific question is whether the scalar second inverse-spectral observer admits a substantially smaller rough state than the full per-edge packet when unequal subdivision is repeated.

Preserve the user's central correction: information erased by a rough relation may reappear under a later permitted operation, so compression is valid only relative to a declared future language. A compact state is valuable only if its fiber is proved safe under the next allowed subdivision and `beta2` readout.

## 4. Success, kill, and return criteria

Success is an exact finite closure law for repeated unequal subdivision at the `beta2` observer level, together with a sufficiency proof and a meaningful minimality or lower-bound statement. An exact no-go proving that a proposed small state cannot close is equally successful if it identifies the missing port information and leaves a strictly smaller unresolved question.

Kill any route that relies on microscopic derivative signs, an unproved continuum interpolation of resolution, positive-total collapse of endpoint-labelled Schur data, one-step packet sufficiency when future serial composition is still allowed, or numerical fitting of a state-update law without exact algebraic verification.

Do not rerun the completed equal-subdivision Schur theorem, the single-edge order-2 packet sufficiency proof, or the all-order serial path composition theorem. Return the first exact closure, exact minimality obstruction, or sharply reduced finite-state frontier; do not broaden into higher `m` until the order-2 state question is resolved or killed.
