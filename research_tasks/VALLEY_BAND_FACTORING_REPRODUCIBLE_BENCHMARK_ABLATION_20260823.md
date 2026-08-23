<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-VALLEY-BAND-FACTORING-REPRODUCIBLE-BENCHMARK-ABLATION",
  "title": "Valley-Band Factoring — Reproducible Benchmark, Cost Model, and Ablation",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "VALLEY_BAND_FACTORING_RELATION_YIELD_AND_COST_MODEL_REPRODUCIBLY_CLASSIFIED",
  "next_action": "Independently implement the frozen valley-state and band-sieve candidates, benchmark fixed and seeded semiprime corpora against point-only/CFRAC and a pinned QS context baseline, measure relation rank rather than raw counts, and classify fixed/adaptive band-opening and multiplier policies without cherry-picking.",
  "dependencies": [
    "research_inputs/VALLEY_BAND_PURE_STATE_AND_BENCHMARK_PACKET_20260823.md@f341b1347939e004e6d55c96e119c53337c0c9a0"
  ],
  "source_refs": [
    "research_inputs/VALLEY_BAND_PURE_STATE_AND_BENCHMARK_PACKET_20260823.md@f341b1347939e004e6d55c96e119c53337c0c9a0"
  ],
  "evidence_status": "TASKBOOK_DRIVER_APPROVED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "factoring",
    "valley-band",
    "benchmark",
    "ablation",
    "relation-yield",
    "cost-model"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "VBBMK",
  "origin_kind": "REPLAY_OR_INTEGRATION",
  "task_lineage": "REPLAY",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:9c1f03a5086432f83d1a3821893be5589124293bc5be5b14d4b7e196220271c7",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Valley-Band Factoring — Reproducible Benchmark, Cost Model, and Ablation

Task-ID: `RS-VALLEY-BAND-FACTORING-REPRODUCIBLE-BENCHMARK-ABLATION`

Intended owner branch:

`research/valley-band-factor-benchmark`

Hard target:

`VALLEY_BAND_FACTORING_RELATION_YIELD_AND_COST_MODEL_REPRODUCIBLY_CLASSIFIED`

## Context

A free Python prototype reported successful valley-band factoring through one 128-bit semiprime and a substantial implementation speedup after replacing the stored continued-fraction state with a closed `(A,B,C)` recurrence. It also suggested that selective full-band opening and multiplier pilots improve relation acquisition, while a double-large-prime extension was slower in the tested implementation.

Those are single-implementation checkpoints, not algorithmic conclusions. This task must rebuild the method independently, freeze a non-cherry-picked corpus, measure the complete relation pipeline, and determine which effects survive controlled ablation.

## Parent-Chain Identity

Lineage is `REPLAY` from a targeted benchmark packet. It is parallel to, not dependent on, the pure-state equivalence task.

The parent chain is:

`USER DOWNWARD-COLLAPSE FACTORING DIRECTION -> PRIME BATCH DRIVER -> INDEPENDENT BENCHMARK RESEARCHER`.

No source code, runtime cache, or source worker identity is inherited. Runtime Researcher-ID allocation is external.

## Locked Source Package

Use:

`research_inputs/VALLEY_BAND_PURE_STATE_AND_BENCHMARK_PACKET_20260823.md@f341b1347939e004e6d55c96e119c53337c0c9a0`.

Do not use any unpublished source prototype or code reconstructed from the source conversation. All candidate implementations must be independently authored or, for the context QS baseline, pinned to a disclosed external version with its role limited to benchmarking.

The factors disclosed for frozen instances are verification data only and may not enter multiplier choice, relation collection, dependency selection, or stopping logic.

## Previous Outputs

No prior taskbook has reproduced the reported performance or isolated the source of the gain.

The source times are not targets. A slower, null, unstable, or architecture-dependent result is valid if the experiment is controlled and reproducible.

## Input Artifact Provenance

The packet freezes the candidate recurrence, band polynomial, thresholds to test, metrics, fixed instances, minimum random corpus, and source checkpoint refs. It withholds implementation details and source code.

The benchmark must therefore distinguish mathematical equivalence, implementation simplification, relation-yield change, and wall-clock change.

## Exact Research Question

On a fixed deterministic corpus and one declared execution environment, determine:

1. whether the closed state reproduces the point-only CFRAC relation stream;
2. whether whole-band sieving increases verified full relations or independent matrix rank per unit cost;
3. which fixed band threshold, if any, wins out of `32,64,128,256,512`;
4. whether an adaptive expected-yield/setup-cost policy beats the best fixed threshold on held-out instances;
5. whether the two-stage multiplier policy predicts held-out relation yield and factor time;
6. whether square-multiple equivalence classes behave as predicted;
7. whether single-large-prime handling helps after rank and recombination costs are included;
8. whether double-large-prime handling is beneficial, neutral, or harmful in this implementation;
9. how the method compares with a point-only/CFRAC baseline and a pinned quadratic-sieve context baseline;
10. which claimed gain is algorithmic, which is representation/implementation overhead, and which does not replicate.

Final classification must be one of:

- `REPRODUCIBLE_RELATION_YIELD_AND_RUNTIME_GAIN`;
- `RELATION_YIELD_GAIN_WITH_NO_RUNTIME_GAIN`;
- `INSTANCE_OR_IMPLEMENTATION_DEPENDENT_GAIN`;
- `NO_REPRODUCIBLE_GAIN`;
- `SOURCE_CHECKPOINT_NOT_REPRODUCED`;
- `INCONCLUSIVE_AFTER_VALIDATED_PARTIAL_MATRIX`.

The hard target requires a cost model and rank-aware evidence, not merely another successful factorization.

## Scope Guard

### In scope

- independent implementations of standard CFRAC/continued-fraction relation collection, closed-state point collection, and closed-state band collection;
- pinned context benchmarking against an established QS implementation or a separately authored minimal QS with disclosed limitations;
- fixed and adaptive band-opening policies;
- multiplier scoring and pilot selection;
- full, single-large-prime, and optional double-large-prime relation handling;
- GF(2) rank, dependency quality, and final gcd extraction;
- deterministic corpora, repeated runs, environment manifests, and profiling;
- exact verification of every relation before matrix insertion.

### Out of scope

- source-code reuse from the free prototype;
- changing corpus, multiplier candidates, thresholds, or factor-base bounds after seeing test outcomes without labeling a new exploratory run;
- reporting raw relation count without matrix rank and recombination cost;
- comparing Python timing directly with optimized QS/NFS as an algorithmic claim;
- claiming asymptotic improvement from finite bit-length timing;
- using the known factors of frozen instances inside the algorithm;
- dropping failed seeds or timeouts from aggregate statistics.

Kill condition:

If relation verification fails, if factors leak into algorithm decisions, if the corpus is selected after results are viewed, or if two variants do not perform equivalent mathematical work, invalidate that comparison and preserve it as a failed attempt rather than repairing the table silently.

## Required Outputs

Produce:

1. Full report:
   `research_output/VALLEY_BAND_FACTORING_REPRODUCIBLE_BENCHMARK_ABLATION_20260823.md`
2. Reducer result:
   `research_output/reducer_results/VALLEY_BAND_FACTORING_REPRODUCIBLE_BENCHMARK_ABLATION_REDUCER_20260823.md`
3. Independently authored implementation directory:
   `experiments/valley_band_benchmark/`
4. Frozen corpus and factors-for-validation file:
   `research_output/VALLEY_BAND_BENCHMARK_CORPUS_20260823.csv`
5. Long-form run table:
   `research_output/VALLEY_BAND_BENCHMARK_RUNS_20260823.csv`
6. Aggregate comparison table:
   `research_output/VALLEY_BAND_BENCHMARK_AGGREGATES_20260823.csv`
7. Cost-model specification:
   `research_output/VALLEY_BAND_OPENING_COST_MODEL_20260823.md`
8. Environment and dependency manifest:
   `research_output/VALLEY_BAND_BENCHMARK_ENVIRONMENT_20260823.json`
9. Evidence event stream:
   `research_output/evidence/VALLEY_BAND_FACTORING_REPRODUCIBLE_BENCHMARK_20260823.jsonl`

The implementation directory must include one command that regenerates the corpus and one command that runs the frozen matrix without interactive tuning.

## Validation Standard

Required validation includes:

- exact completion of the packet's minimum corpus;
- precommitted deterministic seeds and parameter grids;
- at least three timing repetitions for completed sub-128-bit configurations, reporting median and dispersion;
- relation verification before matrix insertion;
- rank trajectories, not only final relation totals;
- identical factor-base and large-prime semantics when variants are compared;
- separate profiling of root setup, sieving, trial division, recombination, linear algebra, and gcd extraction;
- held-out evaluation of the adaptive opening policy and multiplier pilot;
- a pinned QS context baseline run on the same machine and instances, with implementation-language caveats explicit;
- all packet-specified negative controls;
- exact replay of the 104-, 112-, and 128-bit fixed checkpoints or a fully diagnosed failure record.

A successful factor found by one lucky dependency is not enough. Report success rates, dependency counts, rank, and total work.

## Evidence Policy

Keep correctness, relation-yield, rank, runtime, memory, and historical/complexity claims separately typed.

Exploratory tuning results may motivate a policy but cannot evaluate it. Evaluation must use held-out instances frozen before the policy is selected.

A null result, including a slower double-large-prime lane, is a first-class deliverable.

## Reporting Requirements

Use the repository-standard six report sections and add:

- `Corpus Freeze and Leakage Audit`;
- `Implementation Equivalence Ledger`;
- `Per-Stage Cost Breakdown`;
- `Rank-Aware Relation Analysis`;
- `Fixed Threshold Ablation`;
- `Adaptive Policy Holdout`;
- `Multiplier Holdout`;
- `Large-Prime Ablation`;
- `CFRAC and QS Context Baselines`;
- `Final Classification`.

Do not open or compare source implementation details after completion; none are required for this task. Stop after the benchmark evidence package is frozen.

## Repository Closure Protocol

Use the inherited repository closure protocol with no task-specific deviation. Promote code, corpus, raw runs, aggregates, model, environment manifest, report, reducer, and evidence stream together before archival.
