<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PRIME-COORD-FACTOR-VALUATION-WALL-COMPLEXITY-COMPRESSION",
  "title": "Prime Coordinate Valuation-Wall Fast Evaluation and Complexity Compression",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Starting from the accepted exact N-only valuation-wall splitter, determine whether its Theta(p) sequential kernel cost can be compressed by sparse/product-tree/baby-step-giant-step evaluation over Z/NZ, and classify the resulting end-to-end deterministic factoring complexity against current classical baselines.",
  "next_action": "Derive an exact sparse evaluator for A_s=binom(2s,s)^2 binom(3s,s) mod N at the public dyadic wall probes and synchronized fallback seeds without streaming every intermediate index; prove composite-modulus division safety and the full bit complexity, then compare any gain against Pollard-Strassen and the exponent-one-fifth deterministic factoring baseline.",
  "dependencies": [
    "research_result_records/RS-PRIME-COORD-FACTOR-NONLY-VALUATION-WALL-GCD-EXTRACTOR-INDEPENDENT-REPLAY/RR-F24971D684C868A325E2.json@cc0106285c579998747c3e777c11c35a3304a274",
    "driver_reviews/PRIME_COORD_FACTOR_NONLY_VALUATION_WALL_GCD_EXTRACTOR_DRIVER_REVIEW_20260827.md@SAME_PUBLICATION_TRANSACTION"
  ],
  "source_refs": [
    "research_returns/PRIME_COORD_FACTOR_NONLY_VALUATION_WALL_GCD_EXTRACTOR_INDEPENDENT_REPLAY_RETURN_20260827.md@cc0106285c579998747c3e777c11c35a3304a274",
    "research_artifacts/PRIME_COORD_FACTOR_NONLY_VALUATION_WALL_GCD_EXTRACTOR_INDEPENDENT_REPLAY/PHASE_A_FREEZE.md@cc0106285c579998747c3e777c11c35a3304a274",
    "research_tasks/PRIME_COORD_FACTOR_BLIND_BENCHMARK_SUITE_READY_AFTER_PCF1_20260827.md@2edc7e86dad982e3e7a4fb10d21c21ef984e290e"
  ],
  "evidence_status": "PCF4R_EXACT_N_ONLY_SPLITTER_ACCEPTED / THETA_P_STREAMING_BOUNDARY_OPEN / PCF2_BENCHMARK_LANE_ALREADY_EXISTS",
  "last_progress_ref": "RR-F24971D684C868A325E2 accepted by driver_reviews/PRIME_COORD_FACTOR_NONLY_VALUATION_WALL_GCD_EXTRACTOR_DRIVER_REVIEW_20260827.md; exact extraction closed, speed/compression not claimed.",
  "last_progress_at": "2026-08-27T12:10:35+00:00",
  "hard_block": null,
  "tags": [
    "prime-coordinate",
    "factorization",
    "n-only",
    "valuation-wall",
    "fast-evaluation",
    "complexity",
    "product-tree",
    "baby-step-giant-step"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PRIME-COORD-FACTOR-VALUATION-WALL-COMPLEXITY-COMPRESSION",
  "parent_objective_id": "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PCF4C",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-PRIME-COORD-FACTOR-NONLY-VALUATION-WALL-GCD-EXTRACTOR-INDEPENDENT-REPLAY",
  "successor_gate": {
    "new_information_gap": "The exact N-only splitter is now proved, but its current implementation still evaluates the kernel sequentially through an index Theta(p), leaving balanced semiprime cost exponential in bit length.",
    "why_parent_result_does_not_close_it": "PCF4R proves correctness and O(log N) memory, not sparse evaluation, substreaming complexity, or superiority to classical deterministic factoring algorithms.",
    "discriminating_outcomes": "Prove a genuinely sub-Theta(p) end-to-end evaluator; classify the best exact evaluator as classically equivalent/dominated after full baseline comparison; or isolate an exact obstruction to the proposed compression mechanisms.",
    "kill_condition": "Reject any candidate that reads hidden factors, reconstructs all intermediate A_k while claiming sparse evaluation, uses unjustified inverses over Z/NZ, counts only a single probe while hiding preprocessing cost, or claims a factoring speedup without an end-to-end bit-complexity and current prior-art comparison.",
    "alternative_route_or_free_exploration_considered": "PCF2 already owns sealed benchmarking, PCF3 owns separation-spectrum structure, and Lean formalization can follow later; none directly attacks the newly isolated algorithmic bottleneck.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The correctness hard target is terminal with no in-scope residue. Complexity compression is a distinct theorem/algorithm claim with different prior-art, safety and benchmarking obligations."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b78f85af4629ddb714870c44535ad0393418dbc3bebe06da142a90c0c6b9075e",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "program_id": "PRIME_COORD_FACTOR_EXTRACTION_PROGRAM_20260827",
  "requested_risk_tier": "CRITICAL",
  "parent_objective_generation_id": "OG-AA2BAD92F59DC97880C7"
}
-->

# Prime Coordinate Valuation-Wall Fast Evaluation and Complexity Compression

Status: `PUBLISHED_REGISTERED / READY / AFTER_PCF4R_ACCEPTANCE`

## Mother question

The accepted PCF4R theorem gives, for every distinct odd semiprime

\[
N=pq,\qquad 3<p<q,
\]

a deterministic factor-blind splitter built from

\[
A_s=\frac{(2s)!(3s)!}{(s!)^5}
=\binom{2s}{s}^2\binom{3s}{s},
\]

public dyadic wall probes, and the public synchronized fallback near `floor(sqrt(N)/3)`.

Its correctness is closed. Its speed is not: the current streaming constructor advances through `Theta(p)` consecutive recurrence indices. On balanced semiprimes this remains square-root scale in `N` and exponential in the input bit length.

The next question is therefore exact and algorithmic:

> Can the same N-only valuation-wall information be evaluated at the required sparse public seeds in asymptotically fewer than `Theta(p)` sequential kernel steps, without smuggling in hidden factors or invalid field operations over the composite modulus?

## Frozen inputs and scope

Treat `RR-F24971D684C868A325E2` as accepted theorem input at exactly this strength:

- universal exact splitter for distinct odd semiprimes with `3<p<q`;
- constructor receives only `N` and public data;
- local valuation wall, dyadic first-nonunit alternative, synchronization `q<2p`, and two-seed fallback are accepted;
- modular streaming is legal because all inverted indices on the theorem path are below `p`;
- **no factoring-speedup claim is accepted**.

Do not spend this task reproving PCF4R except where a transformed evaluator needs a local lemma or regression guard.

Candidate mechanisms may include product/remainder trees, block factorials, binary splitting, baby-step/giant-step, multipoint evaluation, shared dyadic precomputation, or another exact integer/modular construction. They are targets, not approved methods.

All arithmetic over `Z/NZ` must be valid for composite `N`. Any division or inversion must either be proved to involve a unit or be preceded by an exact gcd guard whose nonunit case already returns a factor. A field-only argument silently transferred to `Z/NZ` is invalid.

## Current deterministic-baseline gate

The task must compare the **full factor-extraction algorithm**, not a single kernel evaluation, against relevant deterministic baselines.

At minimum include:

1. trial-division/Fermat-style square-root baselines where structurally relevant;
2. Pollard-Strassen / product-tree style `N^(1/4+o(1))` deterministic factoring ideas;
3. the rigorous exponent-one-fifth deterministic factoring line of Harvey and Harvey-Hittmeir, including later log-factor improvements;
4. any closer fast-factorial, multipoint, or product-tree result found in a fresh prior-art search at freeze time.

Freeze:

`SUB_THETA_P_EVALUATION != BEST_KNOWN_FACTORING_SPEEDUP`.

In particular, obtaining an `N^(1/4+o(1))` valuation-wall implementation may be mathematically useful but is **not** by itself a general deterministic factoring breakthrough.

## Hard target and required outputs

Hard target:

`N_ONLY_VALUATION_WALL_FAST_EVALUATION_COMPLEXITY_EXACTLY_CLASSIFIED`.

Required outputs:

1. **Sparse-evaluation theorem or obstruction.** Give an exact algorithm that evaluates every PCF4R-required public residue/gcd without streaming all intermediate `A_k`, or prove the sharp failure point of the attempted compression.
2. **Composite-modulus safety proof.** Audit every multiplication, remainder, division and inversion over `Z/NZ`; turn every possible nonunit into an explicit factor-return branch.
3. **Shared-probe analysis.** Determine whether dyadic wall probes can reuse product/remainder-tree or block precomputation, and charge all preprocessing to the final complexity.
4. **End-to-end bit complexity.** State time and memory in terms of `n=ceil(log2 N)` and, where analytically useful, the hidden smaller factor only on the proof side. Constructor control flow must remain N-only.
5. **Baseline comparison.** Prove whether the final bound improves on, matches, or is dominated by the strongest relevant deterministic factoring baseline on the stated semiprime domain.
6. **Exact checker.** Independently regression-test balanced, near-twin, moderately unbalanced and highly unbalanced semiprimes, synchronized fallback cases, and deliberate zero-divisor/inversion hazards. Finite computation is regression only.
7. **Prior-art dedup.** Identify whether the fast evaluator is a new composition, a direct specialization of classical factorial/product-tree factoring, or a known equivalent in different notation. No novelty claim without evidence.
8. **Durable return.** Freeze the complete result at `research_returns/PRIME_COORD_FACTOR_VALUATION_WALL_COMPLEXITY_COMPRESSION_RETURN_20260827.md`, with task-owned checker/certificates fully pinned in the immutable result manifest.

## Success, narrowing, and kill criteria

Freeze exactly one strongest verdict:

- `GENERAL_DETERMINISTIC_COMPLEXITY_IMPROVEMENT_VERIFIED`;
- `SUBSTREAMING_VALUATION_WALL_EVALUATOR_VERIFIED_NO_BEST_BASELINE_ADVANTAGE`;
- `VALUATION_WALL_FAST_EVALUATION_CLASSICALLY_EQUIVALENT_OR_DOMINATED`;
- `FAST_EVALUATION_ROUTE_EXACTLY_OBSTRUCTED`;
- `NO_PROGRESS_WITH_EXACT_BLOCKER`.

A speed claim is invalid unless the proof charges preprocessing, all public probes, gcds, fallback work, and bit-complexity of the modular arithmetic.

Kill or narrow immediately if:

- hidden `p`, `q`, a factor-labelled coordinate, CRT idempotent, or factor-derived seed enters constructor control;
- the method performs `Theta(s)` sequential work under a renamed/block interface while claiming sparse evaluation;
- a nonunit denominator is silently inverted;
- an `N^(1/4)`-scale result is presented as beating the exponent-one-fifth deterministic baseline;
- bounded benchmark wins are used as universal asymptotic evidence.

## Portfolio routing

This successor does **not** replace the already-active PCF2 benchmark lane. PCF2 should remain the sealed empirical/falsification surface; this task owns the proof-level algorithmic compression question.

PCF3 and PCF6 likewise remain independent parallel lanes unless a later Driver review explicitly changes their authority.

No Working Truth, Foundation mutation, global-tool promotion, or canonical factoring-speedup theorem is granted by publication.
