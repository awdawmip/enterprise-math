<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-SEMIPRIME-RESIDUAL-PRIORITY-HART-STREAMING-COST-AUDIT",
  "title": "半素数 residual-priority / Hart streaming 全成本审计",
  "kind": "RESEARCH",
  "owner": "research/semiprime-residual-priority-hart-streaming-cost-audit",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Determine whether the only surviving finite-window residual-priority multiplier ordering from RR-2A424E3B8EC11DC1278C yields any factor-blind total-cost improvement over explicitly matched Hart/Fermat baselines once coverage collapse, square tests, gcds, modular sieving and preprocessing are counted.",
  "next_action": "Freeze matched streaming baselines and cost units, implement factor-blind residual-priority and Hart/Fermat orderings with the same modular sieve budget, then compare total work across stratified bit sizes and factor ratios with explicit kill conditions.",
  "dependencies": [
    "research_result_records/RS-SEMIPRIME-SQUARE-SHELL-MIDPOINT-BOUNDARY-FACTORIZATION/RR-2A424E3B8EC11DC1278C.json@e93b8427ced87bc1ce740082df3d2edf52f141fc"
  ],
  "source_refs": [
    "research_returns/SEMIPRIME_SQUARE_SHELL_MIDPOINT_BOUNDARY_FACTORIZATION_RETURN_20260829.md@e93b8427ced87bc1ce740082df3d2edf52f141fc",
    "research_result_records/RS-SEMIPRIME-SQUARE-SHELL-MIDPOINT-BOUNDARY-FACTORIZATION/RR-2A424E3B8EC11DC1278C.json@e93b8427ced87bc1ce740082df3d2edf52f141fc",
    "research_task_records/RS-SEMIPRIME-RESIDUAL-PRIORITY-HART-STREAMING-COST-AUDIT/TP2-8E5A7D21C30F694B2D11.json@e93b8427ced87bc1ce740082df3d2edf52f141fc",
    "research_tasks/SEMIPRIME_RESIDUAL_PRIORITY_HART_STREAMING_COST_AUDIT_20260829.md@e93b8427ced87bc1ce740082df3d2edf52f141fc",
    "research_tasks/SEMIPRIME_SQUARE_SHELL_MIDPOINT_BOUNDARY_FACTORIZATION_EXPLORATION_20260829.md@e93b8427ced87bc1ce740082df3d2edf52f141fc"
  ],
  "evidence_status": "DRIVER_ACCEPTED_NEGATIVE_BOUNDARY / ONLY_SURVIVING_COST_QUESTION",
  "hard_block": null,
  "tags": [
    "semiprime",
    "factorization",
    "Hart",
    "Fermat",
    "residual-priority",
    "streaming",
    "cost-audit",
    "factor-blind"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-SEMIPRIME-RESIDUAL-PRIORITY-HART-STREAMING-COST-AUDIT",
  "parent_objective_id": "OBJ-SEMIPRIME-SQUARE-SHELL-FACTORIZATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "SSMFCOST",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-SEMIPRIME-SQUARE-SHELL-MIDPOINT-BOUNDARY-FACTORIZATION",
  "successor_gate": {
    "new_information_gap": "The accepted parent rules out a stable static shell predictor but leaves one finite-window multiplier ordering whose total streaming cost has not been compared fairly to Hart/Fermat under the same sieve budget.",
    "why_parent_result_does_not_close_it": "RR-2A424 measures conditional rank and coverage but explicitly does not prove a total-cost or asymptotic advantage.",
    "discriminating_outcomes": [
      "prove a reproducible factor-blind total-cost gain in a precisely delimited regime",
      "classify the ordering as cost-equivalent to a known Hart/Fermat schedule",
      "show coverage/preprocessing/square-test cost eliminates the apparent rank gain"
    ],
    "kill_condition": "Terminate negative if matched total work does not improve, if productive coverage collapses with bit size, or if the ordering reduces to standard Hart ordering plus ordinary modular sieving.",
    "alternative_route_or_free_exploration_considered": "Further static shell correlation and larger census were rejected by the accepted negative boundary.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "This is a distinct algorithmic-cost question with a binary/quantitative outcome, not another correlation scan."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:be0a92bae790fc5100f066235a0257c9a75470d152b48cd36909c318d6a61107",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "parent_objective_generation_id": "OG-94F9DC002F795C10ACF9",
  "migration_source": {
    "original_publication_id": "TP2-8E5A7D21C30F694B2D11",
    "original_taskbook_path": "research_tasks/SEMIPRIME_RESIDUAL_PRIORITY_HART_STREAMING_COST_AUDIT_20260829.md",
    "original_taskbook_blob_sha1": "sha1:23ce96521bbec8c970256c91e390519a03ebc111",
    "original_origin_kind": "DRIVER_REVIEW_FOLLOWUP",
    "original_publisher_id": "EM-DVR-P8H4Q2",
    "original_published_at": "2026-08-29T06:20:30+00:00",
    "source_commit": "e93b8427ced87bc1ce740082df3d2edf52f141fc",
    "reason": "Same-task Generation-2 canonical body completion; exact scientific target, lineage, successor gate and original immutable evidence retained."
  }
}
-->

# 半素数 residual-priority / Hart streaming 全成本审计

## Mother question

Hard target: RESIDUAL_PRIORITY_HART_STREAMING_TOTAL_COST_CLASSIFIED.

The remaining question from RR-2A424E3B8EC11DC1278C, section 12, is whether a streaming threshold/bucket order on the upper-square residual can reduce total factor-blind cost when K(N) reaches a Lehman/Hart-relevant range instead of fixed 64. The original mother question is retained in `research_tasks/SEMIPRIME_SQUARE_SHELL_MIDPOINT_BOUNDARY_FACTORIZATION_EXPLORATION_20260829.md`. This Task classifies the residual streaming-cost question; its parent remains OPEN for every uncovered mother-question claim.

## Frozen inputs and scope

The exact prior Result is `research_result_records/RS-SEMIPRIME-SQUARE-SHELL-MIDPOINT-BOUNDARY-FACTORIZATION/RR-2A424E3B8EC11DC1278C.json@e93b8427ced87bc1ce740082df3d2edf52f141fc`, published for TP2-12778A2D48A1D5A57BA9 by researcher EM-SSMF1-5A7C2E. Its complete output manifest, NEGATIVE_BOUNDARY disposition and original contribution disclosures are preserved. The scientific return is `research_returns/SEMIPRIME_SQUARE_SHELL_MIDPOINT_BOUNDARY_FACTORIZATION_RETURN_20260829.md@e93b8427ced87bc1ce740082df3d2edf52f141fc`, SHA-256 `7ec6b0647e8f1e1a41bb0dfcd4fca538b3d152f24e04cfe1f82230cdb65e27f4`, Git blob `sha1:b0c6ca06bec144d69102770a3fd859d28bddd18f`. Original Hart publication `TP2-8E5A7D21C30F694B2D11` and its Taskbook `research_tasks/SEMIPRIME_RESIDUAL_PRIORITY_HART_STREAMING_COST_AUDIT_20260829.md` remain immutable provenance. This new generation supplies the five canonical body sections while preserving the full scientific requirements.

Use only factor-blind inputs at deployment time. Compare residual-priority, matched Hart/Fermat multiplier orderings, and identical modular-sieve budgets. Count multiplier generation, integer square roots/square tests, gcds, modular filtering, preprocessing, memory, and failures before a productive hit. Report coverage separately from conditional rank.

At minimum test 32/40/48/56/64/80/96-bit stratified semiprimes across factor-ratio bands and preserve an unseen holdout. Do not use the hidden factors to choose k or stop early except for offline labeling of the true first productive event.

The original accepted static-feature equivalence and finite-window evidence are frozen inputs. The new scientific unit starts with paid threshold/bucket multiplier generation, residual transport and first-hit accounting, then evaluates the unchanged full stratified target. It preserves prior completed calculations as evidence and spends new work on the unresolved streaming-cost mechanism. Public inputs are N, predeclared K(N), sieve rules and ordering parameters. Hidden factors and productive-hit labels belong to the separate offline evaluator. Integer arithmetic is an explicitly typed external observer within the fixed native X6 basis; exact transformations preserve the joint (N,k,residual,filter,first-hit,cost) relations they use. Algorithmic time and operation counts are explicitly modeled.

## Hard target and required outputs

Return a reproducible classification of RESIDUAL_PRIORITY_HART_STREAMING_TOTAL_COST_CLASSIFIED with matched residual-priority and Hart/Fermat baselines under identical modular-sieve budgets. Freeze the multiplier range, threshold/bucket rule, ties, correctness conditions, bit-cost/operation units, corpus strata, factor-ratio bands, holdout boundary and kill criteria before the decisive comparison. Include pseudocode or exact code, a correctness argument, complete raw and summary artifacts, first-hit/coverage measurements, preprocessing and memory charges, and all failed work before a productive hit. Charge queue/bucket maintenance and square-root or residual-transport work explicitly. Report finite observations separately from general proofs and practical/asymptotic claims.

The first bounded unit derives and checks the exact threshold/bucket streaming generator and its fully paid cost identity; it is a starting unit, not a substitute for the full 32-through-96-bit classification. Preserve all three possible outcomes and the precise valid regime of every theorem or measurement.

## Research value to preserve

The accepted parent closed the tested static shell-predictor route and identified a single residual multiplier-ordering question. Conditional rank gain is useful only if its generation, square-root, sieve, square-test, gcd, memory and failed-candidate costs yield an actual total-work gain. A proof of equivalence or a reproducible paid-cost negative result is also valuable: it closes this specific proposed mechanism and states the remaining question precisely.

## Success, kill, and return criteria

Success may be positive, equivalent, or negative. No asymptotic or practical factorization claim is allowed without total-cost evidence. Freeze checker, raw/summary artifacts, Result and HANDOFF.

Positive: establish a reproducible factor-blind total-cost gain in a precisely delimited regime with the frozen matched baselines and unseen holdout. Equivalent: identify and justify a reduction to a known Hart/Fermat schedule with ordinary modular sieving, including its complete cost accounting. Negative: show that productive coverage, preprocessing, candidate generation, square-root/transport, queue/bucket or square-test cost removes the apparent conditional-rank advantage.

Terminate the affected candidate negatively when matched total work fails to improve, productive coverage collapses with bit size, or its ordering reduces to standard Hart ordering plus ordinary modular sieving. Keep the earlier static-correlation evidence frozen. A finite experiment supports only its stated corpus and parameters. An unresolved output names the exact missing proof or measurement, completed units, durable artifacts and next unproved unit. Completion is Task-scoped, and uncovered mother-question claims remain open.
