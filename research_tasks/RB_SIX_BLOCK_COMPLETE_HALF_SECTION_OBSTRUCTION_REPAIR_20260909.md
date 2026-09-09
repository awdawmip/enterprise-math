<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-RB-SIX-BLOCK-COMPLETE-HALF-SECTION-OBSTRUCTION-REPAIR",
  "title": "RB six-block obstruction repair with complete half-section spaces",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "The local special-Q degrees2/4 are recovered, and a non-author check confirms that the cited six-block exclusion omitted allowed half-section poles at nonzero two-torsion. Its global exclusion conclusion is not established by that argument; the conditional two-pattern results and concrete accepted map remain intact.",
  "next_action": "Form the complete four-type even-divisor pencil for the six-point branch block, preserve constant square classes and the full fixed-k ODE, and prove the exclusion or produce an exact fully verified fixed-k counterexample; do not rerun old blind reductions or the180/360 enumeration.",
  "dependencies": [],
  "source_refs": [
    "https://github.com/awdawmip/enterprise-math/blob/610123ed59fab638abcaf6ee013df2bfcdcac419/research_result_records/RS-RB-ENTERPRISE-DEGREE6-CM24-BLIND-REPLICATION/RR-5BA6B8E6F611D72FA4F6.json",
    "https://github.com/awdawmip/enterprise-math/blob/610123ed59fab638abcaf6ee013df2bfcdcac419/research_artifacts/RB_BLIND_DELIVERY_INTAKE_20260909_5816EB/parallel_source_manifest.json",
    "https://github.com/awdawmip/enterprise-math/blob/610123ed59fab638abcaf6ee013df2bfcdcac419/research_artifacts/RB_BLIND_DELIVERY_INTAKE_20260909_5816EB/DEPENDENCY_IMPACT_REVIEW.md",
    "https://github.com/awdawmip/enterprise-math/blob/61dedaa3528fc32757e1a7c8636b5167da2e959b/research_artifacts/RB_EVEN_DIVISOR_NONAUTHOR_CHECK_20260909_82DF76/REPORT.md",
    "https://github.com/awdawmip/enterprise-math/blob/c73816d3552b4247861e12e476101e94a4a2ce5a/research_artifacts/RB_ENTERPRISE_DEGREE6_CM24_BLIND_REPLICATION/raw_freeze_reduction.json",
    "https://github.com/awdawmip/enterprise-math/blob/108ac80d4af9a1ebe19cc613aaccb7402564100e/research_artifacts/RB_BLIND_BRANCH_PATTERN_COMPLETION_20260908/squareclass_rr_reduction.md",
    "https://github.com/awdawmip/enterprise-math/blob/108ac80d4af9a1ebe19cc613aaccb7402564100e/research_artifacts/RB_BLIND_BRANCH_PATTERN_COMPLETION_20260908/empty_fiber_obstruction.md",
    "https://github.com/awdawmip/enterprise-math/blob/610123ed59fab638abcaf6ee013df2bfcdcac419/research_artifacts/RB_BLIND_DELIVERY_INTAKE_20260909_5816EB/TOOL_REUSE_RESOLUTION.md"
  ],
  "evidence_status": "DRIVER_REVIEW_FOLLOWUP_V1",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "MATHEMATICAL_CONTINUATION",
    "DRIVER_AUTO_FOLLOWUP",
    "SOURCE_EXPOSED",
    "PROOF_REPAIR",
    "RESULT_ONLY",
    "NO_BLIND_REPLAY"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-RB-SIX-BLOCK-COMPLETE-HALF-SECTION-OBSTRUCTION-REPAIR",
  "parent_objective_id": "RB_ENTERPRISE_THEOREM_PACKAGE_V2_INDEPENDENT_VALIDATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "RB6FIX",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-RB-ENTERPRISE-DEGREE6-CM24-BLIND-REPLICATION",
  "successor_gate": {
    "new_information_gap": "The cited six-block proof's exhaustive even-divisor classification is refuted by an independently checked omitted half-section pole. The complete pencil plus fixed-k ODE has not been ruled out or solved.",
    "why_parent_result_does_not_close_it": "The parent is a historical INCOMPLETE blind reduction with no map/period result; the later source-exposed certificate supplies one4+2 map but does not settle all six-block possibilities. Existing two-pattern enumeration assumes the six-block exclusion.",
    "discriminating_outcomes": [
      "The corrected complete fixed-k system proves no six-block correspondence exists.",
      "An exact fully verified fixed-k six-block correspondence refutes that exclusion at its proper scope.",
      "A bounded partial run freezes the precise unsolved full-space equations, without promoting a local or cover-only candidate."
    ],
    "kill_condition": "Reject a purported solution on a field/source-pin mismatch, omitted T_r half-section pole, unsupported cancellation, wrong degree/fiber, or nonzero fixed-k ODE/unsquared-differential residual. Retain all exact failure evidence.",
    "alternative_route_or_free_exploration_considered": "Replaying the completed blind reductions, rerunning180/360 assignments, or recomputing the accepted concrete map adds no discriminating information. Period/homology work is a separate parent gap. This bounded repair targets an actual newly verified dependency defect.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "A source-exposed proof repair must not be represented as another clean blind reconstruction of the old whole target. The new scope is precisely the missing half-section/exclusion dependency and retains the old incomplete evidence and parent openness."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b3d44e7cb736426e48b7994d280192f2f48ddde306af1d7ad80db2012c00864b",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# RB six-block obstruction repair with complete half-section spaces

Status: `READY / DRIVER REVIEW FOLLOW-UP / PENDING IMMUTABLE PUBLICATION`

## 0. Mother question

After retaining all allowed L(2O+T_r) half-sections, is the six-point branch-block pattern actually impossible for the frozen CM(-24) k and lambda, or does an exact degree-six correspondence with that block satisfy every frozen cover and differential condition?

## 1. Frozen inputs and scope

This task is SOURCE_EXPOSED proof repair. It is not blind discovery and may not claim restored blindness. Work with C:t^2=R^3-3R, O at infinity, B={O,(0,0),(sqrt(3),0),(-sqrt(3),0),(-2,i sqrt(2)),(-2,-i sqrt(2))}, F=(R+2)t, and D:w^2=F. The frozen coefficient field is K=Q(i,3^(1/4),sqrt(2)); k=-i*3^(1/4)*(sqrt(6)-2), lambda=35+24sqrt(2)-20sqrt(3)-14sqrt(6), and phi=(t+k)dR/(wt). Geometric work over an algebraic closure must be distinguished from descent to K or an explicitly declared finite extension. These are named algebraic-model coordinates, not new native axes or a change to P000.

Inputs: https://github.com/awdawmip/enterprise-math/blob/c73816d3552b4247861e12e476101e94a4a2ce5a/research_artifacts/RB_ENTERPRISE_DEGREE6_CM24_BLIND_REPLICATION/raw_freeze_reduction.json; https://github.com/awdawmip/enterprise-math/blob/610123ed59fab638abcaf6ee013df2bfcdcac419/research_artifacts/RB_BLIND_DELIVERY_INTAKE_20260909_5816EB/DEPENDENCY_IMPACT_REVIEW.md; https://github.com/awdawmip/enterprise-math/blob/61dedaa3528fc32757e1a7c8636b5167da2e959b/research_artifacts/RB_EVEN_DIVISOR_NONAUTHOR_CHECK_20260909_82DF76/REPORT.md; https://github.com/awdawmip/enterprise-math/blob/108ac80d4af9a1ebe19cc613aaccb7402564100e/research_artifacts/RB_BLIND_BRANCH_PATTERN_COMPLETION_20260908/squareclass_rr_reduction.md; https://github.com/awdawmip/enterprise-math/blob/108ac80d4af9a1ebe19cc613aaccb7402564100e/research_artifacts/RB_BLIND_BRANCH_PATTERN_COMPLETION_20260908/empty_fiber_obstruction.md; https://github.com/awdawmip/enterprise-math/blob/610123ed59fab638abcaf6ee013df2bfcdcac419/research_artifacts/RB_BLIND_DELIVERY_INTAKE_20260909_5816EB/TOOL_REUSE_RESOLUTION.md. The raw six-block exclusion is the claim under repair, not a proof premise. The exact contradiction is to its auxiliary even-divisor classification. The old returns, source exposure history and incomplete conclusions remain immutable.

The correct geometric even-divisor sectors of L(6O) are L(3O)^2 and (R-r)L(2O+T_r)^2 for r=0,+/-sqrt(3), with L(2O+T_r)=<1,R,t/(R-r)>. Retain nonzero constant factors when the field does not absorb them. Preserve poles at T_r before multiplication by the zero of R-r. Preserve q_i target-special labels: e_X=2 at ordinary values,4 at special values. A fixed target V4 translation may send the occupied six-point block to infinity; no S4 or source-sign quotient preserving fixed parameters is assumed.

Reuse the existing task-local integer polynomial ring and exact BRC DIV where its natural-integer input domain applies. Clear denominators with valuation checks. For symbolic calculations use the integer derivation 2delta, (2delta)R=2t and (2delta)t=3(R^2-1), retaining the factor4 in squared identities. Positive branch counts do not prove field identities, cancellation or descent. No new tool family or decorative BRC invocation is warranted. Any actual research execution first requires its own valid publication/claim/runtime binding and declared resource/trace limits.

## 2. Hard target and required outputs

Hard target: RB_SIX_BLOCK_FIXED_K_EXCLUSION_PROVED_OR_EXACT_FIXED_K_CORRESPONDENCE.

1. Give a complete even-divisor/half-section parameterization including all four geometric two-torsion sectors and arithmetic constant factors. Keep the compensated T_r poles, exact pole6 at O, nonvanishing at the five finite B points, and degree6 after cancellation.
2. With the six-point block normalized to infinity, write X=G/F and explicitly form G,G-F,G-lambda*F in those complete sectors. Retain all compatible unramified square classes. State which equations are only necessary, which enforce the frozen double cover, and which enforce the prescribed differential.
3. Impose the full fixed-k identity F*(delta X)^2=K_ODE*(t+k)^2*X*(X-1)*(X-lambda), K_ODE nonzero and independent of R,t. A solution of an even-divisor member or triple alone is not a full correspondence. Do not silently omit this gate.
4. A positive exclusion must cover the complete allowed system, not an undersized ansatz or finitely sampled parameters. An exact counterexample must give coefficients, field/embedding, X/Y, target twist/j, all six-point-block fibers with valuations/basepoints, both relevant degrees, and the unsquared pulled-back differential. A cover-level candidate that fails the ODE stays partial.
5. Freeze the exact proof/obstruction or the smallest unresolved equation set, actual checker inputs/outputs and meaningful tamper checks under research_artifacts/RB_SIX_BLOCK_COMPLETE_HALF_SECTION_REPAIR_20260909/. Return at research_returns/RB_SIX_BLOCK_COMPLETE_HALF_SECTION_OBSTRUCTION_REPAIR_RETURN_20260909.md. Historical programs and the180/360 search need not be replayed.

The existing1980 parameter components within4+2 and2+2+2, the180 conditional exclusions and the accepted concrete source-exposed map are separate preserved scope. Period integer, homology index and independent absolute normalization are not discharged by this repair.

## 3. Research value to preserve

Preserve the independently checked auxiliary counterexample, every earlier return and source hash, the distinction between geometric square classes and arithmetic descent, and the conditional value of all existing two-pattern results. A failed six-block proof does not refute a correct concrete map; a local type is not a global map.

## 4. Success, kill, and return criteria

PASS only for a complete fixed-k exclusion proof using the full spaces or an exact fixed-k correspondence meeting every stated gate. A complete auxiliary pencil without the ODE, a finite local enumeration, a parameter sample, or the U witness alone is not PASS. On missing field/descent, unresolved saturation, unsupported denominator cancellation, or resource exhaustion, preserve the first exact unresolved unit and return INCOMPLETE without changing the hard target. Do not claim parent closure, Working Truth, Foundation, kernel verification, a new tool family or a clean blind reconstruction.
