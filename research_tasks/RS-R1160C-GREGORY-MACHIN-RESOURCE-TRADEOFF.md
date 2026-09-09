<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R1160C-GREGORY-MACHIN-RESOURCE-TRADEOFF",
  "title": "Gregory-Machin rational-atom resource tradeoff theory",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Determine sharp endpoint-constrained tradeoff laws between generalized completion cost and exact atom-description resources after the unrestricted rational-alphabet Lehmer objective was proved degenerate.",
  "next_action": "Read the #1160 handoff, no-go theorem, bit-Pareto lower bound and Pell calibration, then test sharpness of the universal mu-times-height inequality under exact diagonal endpoint constraints before adding any new resource coordinate.",
  "dependencies": [],
  "source_refs": [
    "research_handoffs/GREGORY_MACHIN_1160_DURABLE_HANDOFF_20260909.md",
    "research_notes/GREGORY_MACHIN_UNRESTRICTED_RATIONAL_ALPHABET_NO_GO_20260904.md",
    "research_notes/GREGORY_MACHIN_GENERALIZED_BIT_PARETO_BOUND_20260904.md",
    "research_notes/GREGORY_MACHIN_RATIONAL_COMPLEMENT_PELL_CHAIN_20260904.md",
    "research_notes/GREGORY_MACHIN_RATIONAL_SUPPORT2_H1000_PARETO_20260904.md"
  ],
  "evidence_status": "SOURCE_BACKED_OPEN_FRONTIER",
  "last_progress_ref": "research_handoffs/GREGORY_MACHIN_1160_DURABLE_HANDOFF_20260909.md",
  "last_progress_at": "2026-09-09T10:30:46+08:00",
  "hard_block": null,
  "tags": ["R1160", "gregory-machin", "rational-turn", "resource-bound", "pareto", "asymptotic"],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-R1160C-GREGORY-MACHIN-RESOURCE-TRADEOFF",
  "parent_objective_id": "EM-OBJ-1160-GREGORY-MACHIN-DISCRETE-WINDING",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "R1160C",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:8ac3d9c2fa05d6e96b01415562970e7b856d38e44479aa76fbf99ca875959fb6",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Gregory-Machin rational-atom resource tradeoff theory

Status: `READY / SOURCE_BACKED / CLAIMABLE_AFTER_IMMUTABLE_RECORD`

## Mother question

What parameter-free or operationally justified inequalities describe the attainable tradeoff between generalized analytic completion cost and exact rational-atom description resources for diagonal-turn formulas, once the unrestricted rational alphabet is known to make Lehmer measure alone degenerate?

## Frozen inputs and scope

Use the #1160 durable handoff as the source router. In particular, treat the following as established at their stated scopes:

- unrestricted primitive rational atoms with Lehmer-only cost have infimum zero;
- the first-crossing family realizes decreasing completion cost while atom-coordinate complexity grows at least on the order of `q log q`;
- every `s`-distinct-atom strict-slope formula satisfies `mu * B_log >= s^2 log_2(10)`;
- the complementary Pell chain is an exact minimum-determinant calibration for the unavailable rational half-diagonal turn;
- the H=1000 support-two census supplies a concrete seven-point feasible Pareto frontier.

Keep analytic completion cost, atom-coordinate encoding, coefficient size, support and winding as typed resources. Do not introduce a weighted sum unless a concrete arithmetic model derives its weights and domain.

The native endpoint condition remains the exact `C8 + free Gaussian valuation` relation. Any asymptotic construction must still provide exact endpoint certificates; proximity of real angles alone is insufficient.

## Hard target and required outputs

1. Determine whether the universal inequality

\[
\mu B_{\log}\ge s^2\log_2 10
\]

is asymptotically sharp under exact diagonal endpoint constraints for any fixed support `s>=2`.
2. If it is not sharp, prove a stronger endpoint-constrained lower bound or identify an additional exact obstruction responsible for the gap.
3. Analyze at least two explicit infinite exact families as upper-bound calibrations. The first-crossing family and complementary Pell family are available baselines; a new family is welcome only if it is independently exact and materially discriminating.
4. Separate support effects from atom-height effects: determine which conclusions persist at fixed support and which require support growth.
5. Test whether coefficient bit length or finite winding complexity is asymptotically forced by the same endpoint mechanism or can vary independently at fixed `(mu,B_log)` scale.
6. Produce a theorem, counterexample or sharp conjectural interval with exact computational evidence for any still-open constant. Do not report a numerically fitted scalar tradeoff as a theorem.
7. State implications for bounded Pareto searches: provide at least one rigorous pruning inequality or impossibility region that a future support-three or higher-support census can safely consume.

## Research value to preserve

Without a resource theorem, generalized rational atoms can manufacture arbitrarily small Lehmer values by hiding complexity in atom coordinates. The existing lower bound repairs the typing but may be far from the true endpoint-feasible envelope. A sharper theory would turn the generalized #1160 program from a sequence of bounded censuses into a principled geometry of attainable resource tradeoffs, and it can supply mathematically safe pruning to every later search.

## Success, kill, and return criteria

**Success:** prove sharpness or a stronger exact endpoint-constrained resource law, with explicit exact families or obstructions and at least one reusable finite-search consequence.

**Kill:** if no improvement over the elementary lower bound can be proved and the tested families do not discriminate candidate asymptotics, return the strongest certified bounds, counterexamples to attempted strengthenings and a precise remaining constant/problem rather than inventing a composite score.

**Return:** include exact assumptions, endpoint certificates for constructive families, asymptotic derivations, any finite checker used, relation to the H=1000 frontier, and a clear statement of which resource coordinates remain independent.
