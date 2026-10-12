<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-T6-P17-VERTICAL-ORDER1-EXACT-AFFINE-BUDGET",
  "title": "T6 maximal-p17 order1: sixteen-row classification with twelve admissible affine classes",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "The independently verified p17 valuation guard and saturated q0 certificate exclude vertical order0. At order1, sixteen q1 residues split into four exact maximal-prime domain exclusions and twelve admissible affine classes. The farther-choice bound leaves at most299 potential signed-budget paths for the actual domain; no affine class has been searched.",
  "next_action": "Record the four exact maximal-prime exclusions, construct the twelve remaining q1 affine classes from the saturated p17 q0 certificate, enumerate all admissible farther-choice index sets with exact rational Gram-Schmidt and original separate side budgets, and return a complete sixteen-row ledger with every local feasible vector and completion obligation.",
  "dependencies": [
    "research_result_records/RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND/RR-C428294CF760BD8D99AA.json@2f257c02d95b9cd630c23284bea2516a1be3f853",
    "research_artifacts/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260920_01A079FC/p17_q0_certificate.json@2f257c02d95b9cd630c23284bea2516a1be3f853",
    "research_artifacts/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260920_01A079FC/PROOF.md@2f257c02d95b9cd630c23284bea2516a1be3f853",
    "driver_reviews/mcp/MCP-cd5eefdde49843898b2a70c1af94d8dd/7592bca554f5d835bc7c/T6_P17_ORDER1_SMALL_BRANCH_THEOREM.md@bcf86761cfd4ccf391df6e277e30d7e0f2a9bab4",
    "driver_reviews/mcp/MCP-cd5eefdde49843898b2a70c1af94d8dd/7592bca554f5d835bc7c/T6_P17_ORDER1_BRANCH_BOUND_RESULTS.json@bcf86761cfd4ccf391df6e277e30d7e0f2a9bab4"
  ],
  "source_refs": [
    "research_artifacts/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260920_01A079FC/NEXT_FRONTIER.json@2f257c02d95b9cd630c23284bea2516a1be3f853",
    "driver_reviews/mcp/MCP-cd5eefdde49843898b2a70c1af94d8dd/7592bca554f5d835bc7c/T6_INDEPENDENT_PAPER_REVIEW.md@bcf86761cfd4ccf391df6e277e30d7e0f2a9bab4",
    "driver_reviews/mcp/MCP-cd5eefdde49843898b2a70c1af94d8dd/7592bca554f5d835bc7c/T6_INDEPENDENT_STATIC_CERTIFICATE_RESULTS.json@bcf86761cfd4ccf391df6e277e30d7e0f2a9bab4",
    "driver_reviews/mcp/MCP-cd5eefdde49843898b2a70c1af94d8dd/7592bca554f5d835bc7c/T6_SMALL_BRANCH_BOUND_SECOND_PASS.md@bcf86761cfd4ccf391df6e277e30d7e0f2a9bab4",
    "driver_reviews/mcp/MCP-cd5eefdde49843898b2a70c1af94d8dd/7592bca554f5d835bc7c/T6_PAPER_SCOPE_SECOND_PASS.md@bcf86761cfd4ccf391df6e277e30d7e0f2a9bab4",
    "driver_reviews/mcp/MCP-cd5eefdde49843898b2a70c1af94d8dd/7592bca554f5d835bc7c/T6_CURRENT_OWNER_PARTIAL_PROGRESS_AND_P17_REVIEW_20261012.md@bcf86761cfd4ccf391df6e277e30d7e0f2a9bab4"
  ],
  "evidence_status": "DRIVER_REVIEW_FOLLOWUP_V1",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "MATHEMATICAL_CONTINUATION",
    "DRIVER_AUTO_FOLLOWUP",
    "T6",
    "shape-moment",
    "p17",
    "order1",
    "exact-affine-lattice",
    "signed-budgets",
    "bounded-299-paths"
  ],
  "claim_lease_minutes": 180,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-T6-P17-VERTICAL-ORDER1-EXACT-AFFINE-BUDGET",
  "parent_objective_id": "EM-T6-SHAPE-MOMENT-EXACT-THRESHOLD",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "T6P17Q1",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND",
  "successor_gate": {
    "new_information_gap": "The exact signed-budget feasible points of the twelve admissible order1 affine classes are unknown. The four outside-domain residues can already be removed by explicit maximal-prime certificates; the remaining finite search has a proved299-path upper bound.",
    "why_parent_result_does_not_close_it": "The parent Result proves a q0 homogeneous exclusion and reports p19 clearance. It explicitly does not test p17 orders1..16. Failure of the old single-candidate sufficient gate neither proves a kernel nor excludes one.",
    "discriminating_outcomes": [
      "All twelve admissible classes are EMPTY under exact signed budgets, closing actual maximal-p17 order1; four other rows are OUTSIDE_MAXIMAL_P17_DOMAIN, not relaxation-empty.",
      "A complete exact local feasible-vector list survives in one or more admissible classes; retain exact lower-prime/H0 completion conditions and any named completion-cut failure."
    ],
    "kill_condition": "Reject any omitted allowed nonpreferred index set, unfixed half-integer tie, floating arithmetic, ignored signed budget, outside-domain row relabeled as relaxation-empty, unvisited class labeled EMPTY, or modular kernel relabeled as a full collision. No p19 replay or automatic order2 expansion.",
    "alternative_route_or_free_exploration_considered": "Continuing the global task unchanged and attacking every p17 order were considered. This local unit has only sixteen affine classes and an independently justified finite search bound. Unrelated free exploration remains available to other portfolio lanes.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "Root preserves the end-to-end global Task OPEN via a nonterminal RETURN_TO_OWNER review. This child has a genuinely finite changed hard target with sixteen domain/status rows and at most299 potential paths; completing it supplies a local reusable result without terminalizing the global problem."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:be0a92bae790fc5100f066235a0257c9a75470d152b48cd36909c318d6a61107",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# T6 maximal-p17 order1: sixteen-row classification with twelve admissible affine classes

Status: `READY / DRIVER REVIEW FOLLOW-UP / PENDING IMMUTABLE PUBLICATION`

## 0. Mother question

For the original T6 separate signed budgets at most2331, what are all feasible q0 vectors in actual maximal-prime17 vertical order1? Return a complete sixteen-row classification: four exact domain exclusions and twelve affine signed-budget classes. The original global T6 threshold, all remaining orders and lower-prime/H0 completion remain open.

## 1. Frozen inputs and scope

Reuse immutable RR-C428294CF760BD8D99AA, the full composite-denominator p17 q0 saturated basis/Gram-Schmidt certificate, and the newly published independent paper/static certificates at the exact Source pins below. The old p19 70,285,694-rejection census is author evidence and must not be rerun or relabeled independently replicated. No q1 affine center or census has previously been executed in this preparation.

Use q1 atom a_r=17(17+r), cost v_r=288+17r, with sign fixed positive by the global sign symmetry. Keep all q0 coordinates u_s for s=1..16, including composite denominators17s. Require sum_s u_s s^(-k)=-(17+r)^(-k) mod17^k, k=1..6. Set w_s=17s-1, P(u)=sum_s w_s max(u_s,0), and N(u)=sum_s w_s max(-u_s,0). Separate bounds are P(u)<=2043-17r and N(u)<=2331, using these original weighted positive and negative masses; the enclosing Euclidean sphere is necessary only.

The four rows r=2,6,12,14 have cofactors19,23,29,31 above17 and are OUTSIDE_MAXIMAL_P17_DOMAIN, never relaxation-empty. Search exactly r=1,3,4,5,7,8,9,10,11,13,15,16. Preserve every local survivor; a modular kernel alone is not a full collision. No automatic order2 expansion.

## 2. Hard target and required outputs

Hard target: P17_ORDER1_SIXTEEN_ROW_DOMAIN_AND_TWELVE_AFFINE_SIGNED_BUDGET_CLASSIFICATION_COMPLETE.

Construct one exact affine center per admissible residue from the six mixed congruences. Validate every center against all six congruences. Reuse the saturated full16-coordinate lattice and exact Gram-Schmidt data. The published bound implies each feasible descending path has at most two nonpreferred choices; ties at half-integers choose the smaller integer. Enumerate every allowed empty/singleton/pair index set with sum of D_i <=4R_r^2 and recompute actual centers from previously chosen higher coordinates. Their complete actual-domain total is at most299 paths (at most2946 shared-prefix nodes). Floor/ceil, radius pruning, and comparisons use exact integers/Fractions, never floating point.

Return: (1) complete sixteen-row ledger, with four OUTSIDE rows and twelve EMPTY or FEASIBLE_LOCAL_VECTOR_LIST rows; (2) exact affine representatives plus center, input, basis and certificate pins; (3) complete enumeration coverage and each actual leaf, sphere and two signed-budget checks; (4) independently checkable script and a verification receipt; (5) all survivors with exact H0 and lower-prime completion obligations; (6) explicit unresolved global scope.

For a survivor retain M_0=1+sum u_s and M_k=a_r^(-k)+sum_s u_s/(17s)^k. Actual collision requires17-free lower-prime<=13 denominators t_a satisfying all seven rational moment balances and both residual side budgets. Cheap necessary cuts -B_+<=M_0<=B_- and -B_+/2^k<=M_k<=B_-/2^k may reject a local vector; passing them is no completion proof.

## 3. Research value to preserve

The reviewed parent is genuinely partial: p19 and p17 order0 were excluded, while p17 orders1..16 and the global threshold remain unresolved. This independent299-path bound makes the first unexplored order a decisive finite local unit. Preserve the exact affine/signed-budget operator for any lower-prime/H0 continuation; ordinary lattice methods and this task-specific optimization are not claimed novel or promoted as a global toolbox family.

## 4. Success, kill, and return criteria

Success is the complete sixteen-row classification and verified complete list for each of the twelve actual classes; an all-EMPTY admissible list closes only actual maximal-p17 order1. A surviving local vector is a valid bounded outcome if every survivor and its completion obligations are retained; it is not a full collision.

Kill incomplete branching, unproved affine representatives, floating arithmetic, omitted composite q0 denominators, unfixed ties, ignored separate side budgets, OUTSIDE mislabeled EMPTY, unvisited rows declared EMPTY, repetition of p19, and automatic escalation to order2. The parent remains OPEN; do not convert its original NEGATIVE_BOUNDARY or PARTIAL_PROGRESS verdict to SATISFIED. Return any implementation failure with preserved exact inputs and remaining classes.
