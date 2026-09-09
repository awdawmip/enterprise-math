<!-- ENTERPRISE_MATH_TASK_V1
{
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "claim_lease_minutes": 180,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "parent_objective_id": "OBJ-RH-BRC-CARRY-CLOSURE-20260909",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:dd425305887871866cb2f0894885ff38359639e2de7750fa45e8c584e19feae4",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "task_id": "RH-BRC-CARRY-CLOSURE-20260909",
  "title": "Count-centered BRC carry closure and coupled reciprocal-port square function",
  "frontier": "V11-V17 have reduced the BRC-first RH route to the exact count-centered carry innovation J(n), its integer valuation holonomy, and a low-port/hard-prime square-function problem. Exact finite geometry, Mobius inversion, prime-cutoff and hard-core tools exist, but no unconditional fixed-polylog all-scale bound for W(N)=sum(J(n)/n)^2 has been proved.",
  "next_action": "Read the state-machine handoff first, consume the three durable global journals and the pinned V17 tool branch without replay, then formulate and attack the exact coupled moving-port square-function or equivalent global Mobius-shell Gram estimate needed to prove W(2^k)=O(k^A).",
  "dependencies": [],
  "source_refs": [
    "research_notes/RH_BRC_COUNT_CENTERED_CARRY_STATE_MACHINE_HANDOFF_20260909.md",
    "global-knowledge:f03d92f90f0e7db60fc2c188f0c980c5127a90f9:journal/enterprise-math/2026-09-05/20260905T111421+0800-free-brc-predictive-port-v11-3eaa93.md",
    "global-knowledge:21614563efe3af4ee94d3853560146901ea3eb5a:journal/enterprise-math/2026-09-05/20260905T114657+0800-free-brc-mellin-haar-centered-rg-v13-3eaa93.md",
    "global-knowledge:78075758a90fef59fb78fc2c13473ecdd49a7681:journal/enterprise-math/2026-09-05/20260905T131532+0800-free-brc-count-centered-wavelet-deconvolution-v14-3eaa93.md",
    "research-branch:research/brc-count-centered-carry-v14-tool@437d4d595f1495d3a0486b3c06e9e2b14567db82",
    "research-review:1250",
    "drive-artifact:1YL2RsFGJeSxK0kuXi47VUd0vGa8WlhAl"
  ],
  "evidence_status": "V11_V17_EXACT_IDENTITIES_AND_TOOLING_PRESERVED_RH_POLYLOG_CLOSURE_OPEN",
  "last_progress_ref": "research_notes/RH_BRC_COUNT_CENTERED_CARRY_STATE_MACHINE_HANDOFF_20260909.md",
  "last_progress_at": "2026-09-09T11:20:00+08:00",
  "hard_block": "COUPLED_RECIPROCAL_PORT_SQUARE_FUNCTION_OR_EQUIVALENT_GLOBAL_MOBIUS_SHELL_BOUND",
  "tags": ["RH", "BRC", "carry", "count-centering", "valuation-holonomy", "Mellin-Haar", "Mobius", "reciprocal-port", "square-function", "hard-prime"],
  "registry_key": "RH-BRC-CARRY-CLOSURE-20260909",
  "identity_lane": "RH-BRC-CARRY",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null,
  "origin_research_provenance": "EM-FREE-3EAA93; FREE_AXIOM_DISCOVERY; ANCHOR_EXPOSED; user-directed integration of the V11-V17 BRC-first RH frontier; no raw axiom candidate promoted"
}
-->

# Count-centered BRC carry closure and coupled reciprocal-port square function

Status: `READY / FREE-RESEARCH INTEGRATION / UNCLAIMED`

## Mother question

Can the original von Mangoldt weights, observed through the exact count-centered doubling-carry BRC state, be controlled at all dyadic scales strongly enough to prove a fixed-polylog bound for

`W(N)=sum_{N<=n<2N}(J(n)/n)^2`,

where `J(n)=sum_{m<=n}(c_m(n)-A_n/n)Lambda(m)` and `c_m(n)=floor(2n/m)-2floor(n/m)`?

## Frozen inputs and scope

Read `research_notes/RH_BRC_COUNT_CENTERED_CARRY_STATE_MACHINE_HANDOFF_20260909.md` first. Consume the pinned V11, V12/V13 and V14 global journals and the V17 exact-tool branch listed in `source_refs`; do not reconstruct them from chat history.

Frozen derived interfaces include:

- exact predictive quotient-port binary transport and its fair positive-rational gauge;
- local integer valuation-Haar/wedge coordinates and exact recovery of child valuation state;
- the Mellin-Haar curvature symbol, critical RG factor `2^(2 Re(s)-1)` and lattice crossover `j^3/X`;
- count-centered innovation `J(n)`, holonomy `Omega_n` with `log Omega_n=n J(n)`, and the RH-equivalent/sufficient block-energy interface recorded in V14;
- localization of the unresolved hard layer near low ports `j=O(N^(1/3+epsilon))`, equivalently ordinary primes around and above the `N^(2/3)` boundary;
- exact reciprocal quotient-shell compilation, Mobius geometry inversion, log-gauge, prime-cutoff factorization and large-prime hard-core tools at the pinned branch head.

Adjacent registered tasks `RH-ROAD-AUDIT-20260909`, `RH-ROAD-KERNEL-20260909` and `RH-ROAD-TAIL-20260909` belong to the composite-road program. Reuse a relevant proved result if it transfers, but do not duplicate their source audit or anchored phase-kernel work.

Do not assume that finite negative Gram sums, pairwise signs, ordinary single-interval Selberg mean squares, positive BRC multiplicity, skeleton-only compression, or generic large-sieve estimates beyond their already proved range supply the missing all-scale bound.

## Hard target and required outputs

Primary target: prove for the original arithmetic observer a theorem of the form

`W(2^k)=O(k^A)`

for some fixed finite `A`, or a stronger uniform bound. The proof must be genuinely all-scale and may use one or more of the following interfaces:

1. a simultaneous reciprocal-port square-function/Bessel estimate for the moving BRC intervals, with the endpoint/length coupling retained rather than estimated one interval at a time;
2. a valuation-Haar or martingale inequality that preserves the original `log p` observer and controls cross-port/cross-scale innovation;
3. a global Mobius-shell Gram/recoalescence estimate controlling the aggregate off-diagonal term without pairwise absolute values;
4. an exact reduction showing that a proposed analytic input is equivalent to the missing bound, together with a rigorous obstruction if current unconditional inputs cannot reach it.

Required durable output: `research_notes/RH_BRC_COUNT_CENTERED_CARRY_CLOSURE_20260909/RETURN.md`, plus any minimal exact/numerical checker needed to audit a new identity or counterexample. The return must separate proved identities, unconditional estimates, finite evidence, conditional implications and unresolved steps.

If an estimate appears to close RH, independently audit the exact inequality, quantifiers and uniformity before classifying the task as closed.

## Research value to preserve

This route has already separated BRC geometry from signed arithmetic interference, exposed the exact observer information that total-only or skeleton-only quotients destroy, and produced a reusable exact finite tool stack. Even a negative result that proves a proposed square-function, Mobius-shell sign law or port aggregation cannot beat an RH-strength barrier is valuable because it removes a concrete closure mechanism without discarding the integer valuation/carry representation.

The most valuable residue is a precise theorem-level description of the smallest analytic estimate still missing after all exact BRC reductions, stated in a form that another analytic-number-theory route can attack without replaying V11-V17.

## Success, kill, and return criteria

**Success:** an unconditional all-scale proof of `W(2^k)=O(k^A)` for fixed `A`, or an explicitly proved stronger estimate, with the existing RG/Mellin implication rechecked from the frozen journal chain.

**Partial success:** a strictly smaller equivalent closure lemma with exact quantifiers and a proof that all remaining pieces are already unconditional; or a new exact decomposition that demonstrably lowers the analytic strength required.

**Kill/no-go for a subroute:** produce a rigorous counterexample, lower bound, loss-of-information witness, or equivalence showing that the proposed mechanism merely restates the RH-strength norm bound. In particular, reject pairwise-negativity, absolute-value aggregation, skeleton-only, or uncoupled short-interval arguments when their missing cancellation can be quantified.

**Return:** when one primary closure attempt is proved, killed, or reduced to a single explicit external-strength estimate, write `RETURN.md` with start-here pointers, exact theorem status, reusable code refs, and the next smallest unresolved unit. Do not claim RH from finite computation or from an unproved uniformity step.
