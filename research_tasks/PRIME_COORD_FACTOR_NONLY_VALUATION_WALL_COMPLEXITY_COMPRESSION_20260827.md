<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PRIME-COORD-FACTOR-NONLY-VALUATION-WALL-COMPLEXITY-COMPRESSION",
  "title": "Prime Coordinate N-only Valuation-Wall Complexity Compression",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Determine whether the accepted exact N-only valuation-wall factor extractor can be compressed below its Theta(p) sequential wall-search cost on balanced semiprimes, or freeze a precise construction-family barrier/equivalence to classical factorial or product-tree factorization.",
  "next_action": "Treat the accepted public recurrence as fixed input, replace sequential s-by-s advancement by rigorously factor-blind batching or divide-and-conquer candidates, and prove their bit complexity and gcd-separation behavior before comparing them with factorial/product-tree and sealed classical baselines.",
  "dependencies": [
    "RS-PRIME-COORD-FACTOR-NONLY-VALUATION-WALL-GCD-EXTRACTOR-INDEPENDENT-REPLAY"
  ],
  "source_refs": [
    "research_result_records/RS-PRIME-COORD-FACTOR-NONLY-VALUATION-WALL-GCD-EXTRACTOR-INDEPENDENT-REPLAY/RR-F24971D684C868A325E2.json@6aa4e2c87835b44989bf01166cd3d88262f7377d",
    "research_returns/PRIME_COORD_FACTOR_NONLY_VALUATION_WALL_GCD_EXTRACTOR_INDEPENDENT_REPLAY_RETURN_20260827.md@6aa4e2c87835b44989bf01166cd3d88262f7377d",
    "research_tasks/PRIME_COORD_FACTOR_BLIND_BENCHMARK_SUITE_READY_AFTER_PCF1_20260827.md@6aa4e2c87835b44989bf01166cd3d88262f7377d"
  ],
  "evidence_status": "DRIVER_ACCEPTED_EXACT_N_ONLY_EXTRACTOR / NO_SPEEDUP_CLAIM / COMPLEXITY_COMPRESSION_OPEN",
  "last_progress_ref": "RR-F24971D684C868A325E2 accepted by DR-8D0F336B048B93D0D43F; exact correctness closed, Theta(p) sequential cost remains the smallest open unit.",
  "last_progress_at": "2026-08-27T12:18:00+00:00",
  "hard_block": null,
  "tags": [
    "prime-coordinate",
    "factorization",
    "n-only",
    "valuation-wall",
    "complexity-compression",
    "product-tree",
    "pcf4c"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PRIME-COORD-FACTOR-NONLY-VALUATION-WALL-COMPLEXITY-COMPRESSION",
  "parent_objective_id": "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PCF4C",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-PRIME-COORD-FACTOR-NONLY-VALUATION-WALL-GCD-EXTRACTOR-INDEPENDENT-REPLAY",
  "successor_gate": {
    "new_information_gap": "Universal factor-blind correctness is now closed, but the accepted constructor advances the valuation wall sequentially for Theta(p) indices and therefore remains square-root-scale on balanced semiprimes.",
    "why_parent_result_does_not_close_it": "The parent task explicitly froze NO_SPEEDUP_CLAIM and treated complexity compression as outside its hard target; it proves correctness, not an asymptotically competitive implementation or a lower bound against one.",
    "discriminating_outcomes": "Prove a strict sub-square-root or subexponential-in-bitlength N-only compression, prove an exact batching/product-tree equivalence or lower barrier for the frozen construction family, or isolate the smallest arithmetic operation that prevents either conclusion.",
    "kill_condition": "Any proposed speedup that reads hidden factors, uses factor-derived thresholds, hides least-factor search, or still performs Theta(p) equivalent work after bit-cost expansion does not satisfy the compression target.",
    "alternative_route_or_free_exploration_considered": "The live PCF2 benchmark measures candidates and PCF7 classifies portfolio complexity, but neither is tasked with inventing or refuting a construction-specific acceleration of this exact valuation-wall algorithm; broad free exploration is lower leverage until this bottleneck is isolated.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "Correctness is terminal and should remain frozen. A separate continuation can attack only the computational bottleneck without reopening the independent replay, weakening its theorem, or conflating benchmark measurement with algorithm design."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b78f85af4629ddb714870c44535ad0393418dbc3bebe06da142a90c0c6b9075e",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "program_id": "PRIME_COORD_FACTOR_EXTRACTION_PROGRAM_20260827",
  "requested_risk_tier": "CRITICAL"
}
-->

# Prime Coordinate N-only Valuation-Wall Complexity Compression

Status: `PUBLISHED_REGISTERED / READY / POST-PCF4R`

## Mother question

Given the accepted N-only extractor for distinct odd semiprimes `N=pq`, `3<p<q`, can the valuation-wall search be computed in asymptotically fewer than `Theta(p)` sequential index advances on balanced inputs while preserving an executable interface that depends only on `N` and public parameters?

Equivalently, can the divisibility information carried by

`A_s=(2s)!(3s)!/(s!)^5`

be aggregated by blocks, product trees, factorial-mod-`N` methods, binary splitting or another exact public transformation so that a nontrivial gcd is found without effectively scanning the wall up to the smaller factor?

## Frozen inputs and scope

The parent correctness theorem is frozen input, not a target to re-prove. The executable side may use `N`, public constants, deterministic or independently seeded public schedules, integer square root, modular arithmetic and gcd. Hidden factors may appear only in proofs and sealed regression oracles.

Start from the accepted recurrence and stopping/fallback theorem, but permit algebraically equivalent batch representations. For every proposed acceleration, count modular multiplications, gcds, product-tree work, intermediate integer growth, preprocessing and memory as functions of `n=ceil(log2 N)`.

The primary comparison is with the parent sequential constructor and with standard factorial/product-tree style gcd factorization baselines. The already-published PCF2 benchmark remains a separate common evaluation surface; this task may produce a candidate package for it but must not rewrite that benchmark.

A faster-looking coordinate or block count is not sufficient if bit-cost expansion or hidden scans restore square-root-scale work.

## Hard target and required outputs

Hard target: `N_ONLY_VALUATION_WALL_COMPLEXITY_COMPRESSION_CLASSIFIED`.

Required outputs:

1. an exact formal description of the parent sequential cost model and its balanced-semiprime asymptotic regime;
2. at least one serious factor-blind batching/divide-and-conquer acceleration attempt, with exact arithmetic semantics;
3. a proof that each attempted constructor still returns a nontrivial gcd on its claimed domain, or an exact failure mechanism;
4. a bit-complexity and memory derivation in `n=ceil(log2 N)`, including preprocessing and intermediate growth;
5. a direct comparison with factorial-mod-`N`, product-tree or batch-gcd baselines under the same arithmetic model;
6. if a genuine compression survives, an exact public algorithm and independent regression checker suitable for later PCF2 ingestion;
7. if no compression survives, the strongest construction-family barrier or equivalence theorem that can be proved without claiming an unrestricted lower bound for integer factorization;
8. a clear statement of whether any improvement is polynomial, subexponential, strict sub-square-root, square-root-scale, or only constant-factor;
9. a durable return at `research_returns/PRIME_COORD_FACTOR_NONLY_VALUATION_WALL_COMPLEXITY_COMPRESSION_RETURN_20260827.md`.

## Research value to preserve

PCF4R is the first accepted exact deterministic N-only splitter in this program, so correctness is no longer the bottleneck. Its present weakness is concentrated in one place: reaching enough valuation-wall support appears to require work proportional to the smaller factor.

That makes this a high-value compression target. A positive result would turn a structural extraction theorem into a materially stronger algorithmic object. A negative barrier would be equally useful because it would identify the valuation-wall construction as a classical square-root-scale factorization mechanism rather than a hidden speedup, preventing repeated rediscovery of the same cost under geometric or p-adic language.

## Success, kill, and return criteria

Freeze exactly one strongest primary verdict:

- `STRICT_SUB_SQRT_COMPRESSION_PROVED`;
- `SUBEXPONENTIAL_IN_BITLENGTH_COMPRESSION_PROVED`;
- `VALUATION_WALL_BATCHING_BARRIER_PROVED`;
- `CLASSICAL_FACTORIAL_OR_PRODUCT_TREE_EQUIVALENCE_FROZEN`;
- `SQUARE_ROOT_SCALE_RECONFIRMED_WITH_SHARP_COST`;
- `NO_PROGRESS_WITH_EXACT_COMPLEXITY_BLOCKER`.

A positive speedup verdict requires an exact N-only algorithm, correctness proof and full bit-cost derivation. A barrier verdict must state the construction family it covers and must not be inflated into a lower bound for unrestricted factorization. Finite benchmarks are regression evidence only.

The task terminates once the strongest asymptotic classification and its proof or exact blocker are frozen; benchmark ranking, portfolio-wide PCF7 classification and Lean formalization remain separate downstream decisions.

## Queue interface

- Program: `PRIME_COORD_FACTOR_EXTRACTION_PROGRAM_20260827`.
- Requested priority/leverage: `P1 / HIGH`.
- Requested risk tier: `CRITICAL`.
- Dependency gate: `RS-PRIME-COORD-FACTOR-NONLY-VALUATION-WALL-GCD-EXTRACTOR-INDEPENDENT-REPLAY` terminally accepted.
- First executable action: derive a batch/product-tree representation of the recurrence or prove why it cannot skip the first useful valuation wall, then expand the exact bit cost before running broad regression.
- Task-terminal return resumes Driver evaluation; it does not mutate the accepted PCF4R theorem.

## Result return contract

Return one durable report at `research_returns/PRIME_COORD_FACTOR_NONLY_VALUATION_WALL_COMPLEXITY_COMPRESSION_RETURN_20260827.md` containing the primary verdict, exact theorem or blocker, source pins, algorithm/checker artifacts if any, bit-complexity derivation, comparison baseline, remaining assumptions and the smallest unresolved unit.
