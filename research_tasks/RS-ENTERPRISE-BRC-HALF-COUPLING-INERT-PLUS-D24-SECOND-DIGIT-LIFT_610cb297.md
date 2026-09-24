<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT",
  "title": "Enterprise BRC inert-plus D=-24 second-digit LIFT",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Consume the accepted D=-24 UR/JT0 first-digit Result and solve only the surviving second-digit certificate LIFT: Delta_p=(G_p h-1)/p congruent R_p mod p for every p congruent 13 or 19 modulo 24. Preserve G_p mod p^2, h mod p^2, cutoff-sensitive Phi_xx, derivative/Frobenius ports and provenance; do not reopen CM0, SIMPLE, UR or the first-digit Chisholm/Clausen proof.",
  "next_action": "Derive an exact expression for Delta_p-R_p modulo p from the accepted scalar interface and classify the smallest remaining p-adic/finite-field observer; then either prove it uniformly in both residue classes, produce an exact counterexample, or strictly reduce it to a smaller certificate. Reuse current high-precision BRC notes only after proving they preserve the LIFT observer.",
  "dependencies": [
    "RR-82F6383FB6634F72B457",
    "DR-2EA60F5817976E662FA6",
    "RR-AC9B3BA5BD277CE043F5"
  ],
  "source_refs": [
    "research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_RETURN_20260828.md",
    "research_artifacts/mcp/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SUPERSINGULAR-UNIT-RECIPROCITY/MCP-e6cc623799404ca09be0012f8654712c/0f0be0d17d5eb48c835b/d24_ur_jt0_result_20260924.md"
  ],
  "evidence_status": "DRIVER_REVIEW_FOLLOWUP_V1",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "MATHEMATICAL_CONTINUATION",
    "DRIVER_AUTO_FOLLOWUP"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT",
  "parent_objective_id": "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "MATHEMATICAL_CONTINUATION",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SUPERSINGULAR-UNIT-RECIPROCITY",
  "successor_gate": {
    "new_information_gap": "The accepted first-digit Result evaluates the nonzero reciprocal unit and proves UR/JT0, but it does not determine the divided second p-adic digit Delta_p or compare it with the frozen target R_p.",
    "why_parent_result_does_not_close_it": "UR is only the reduction of G_p h modulo p after dividing g by p. LIFT depends on G_p and h modulo p^2 and on the cutoff-sensitive Phi_xx/derivative corrections that are invisible to the first-digit theorem.",
    "discriminating_outcomes": [
      "Prove LIFT uniformly for p congruent 13 or 19 modulo 24 and hence prove JT2 at the frozen interface.",
      "Produce one exact independently recomputed counterexample to LIFT/JT2.",
      "Prove an exact lower-complexity equivalent certificate for Delta_p-R_p."
    ],
    "kill_condition": "A verified all-prime proof or exact counterexample terminates LIFT. Finite regression or unrelated higher-precision BRC expansions do not.",
    "alternative_route_or_free_exploration_considered": "Reopening CM0/SIMPLE/UR and continuing unbounded auxiliary cancellation-carrier census were rejected because those do not address the unique second-digit residual.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The UR task is terminal at first-digit scope. A new narrow LIFT continuation preserves the accepted theorem boundary and isolates the only remaining scalar p-adic digit needed for JT2."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:44b2174111ec85b5dd252d07f474772649a4d36936b2c99acbfa2cfba8af7a73",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Enterprise BRC inert-plus D=-24 second-digit LIFT

Status: `READY / DRIVER REVIEW FOLLOW-UP / PENDING IMMUTABLE PUBLICATION`

## 0. Mother question

For every prime p congruent 13 or 19 modulo 24, does the accepted D=-24 inert-plus scalar interface satisfy Delta_p=R_p modulo p, where Delta_p=(G_p h-1)/p modulo p, thereby proving JT2 now that UR/JT0 is closed?

## 1. Frozen inputs and scope

Freeze accepted parent RR-82F6383FB6634F72B457 and its review DR-2EA60F5817976E662FA6, plus accepted first-digit Result RR-AC9B3BA5BD277CE043F5 and its exact-set Driver review/synthesis. Treat CM0, SIMPLE, JT0<=>UR, W_p congruent p mod p^2, and UR as closed inputs. LIFT/JT2 alone is live. Keep G_p=g/p modulo p^2 and h modulo p^2; do not quotient away Phi_xx, derivative order, residue-class identity, or p-adic valuation/provenance before the divided second-digit observer.

## 2. Hard target and required outputs

Hard target: D24_SECOND_DIGIT_LIFT_PROVED_REFUTED_OR_STRICTLY_REDUCED. Required: an all-target proof of Delta_p=R_p mod p for both residue classes, or one exact independently recomputed counterexample, or a genuinely smaller exact equivalent certificate; explicit derivation from the frozen scalar interface; deterministic exact checker used only for falsification/regression; and a precise information-loss audit for every quotient used.

## 3. Research value to preserve

Preserve the separation between first and second p-adic digits achieved by the parent. The only live information is the divided p-adic residual after the accepted UR unit has been removed. Positive-mass or mod-p-only summaries are not adequate if they erase the second digit or source/Frobenius ports.

## 4. Success, kill, and return criteria

Success is a uniform proof of LIFT, which together with frozen UR proves JT2 at the accepted interface. A single exact counterexample refutes JT2. A strict reduction is acceptable only if it lowers live p-adic/derivative complexity and proves equivalence. Finite scans, re-proving UR, or extending auxiliary precision without connecting it to Delta_p-R_p are non-closing. Return the narrowest verified certificate and exact scope.
