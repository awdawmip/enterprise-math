<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R024-COLLAPSE-ATLAS-RUNTIME-ACCELERATOR",
  "title": "R024 Collapse Atlas Runtime Accelerator and Collapse-Domain Navigation",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH_TOOLING_LEVERAGE",
  "frontier": "Compile the already-proved collapse-basin structure and accepted BRC support semantics into an exact workload-adaptive runtime: decide when dense lookup, perfect-power boundary atlases, local basin cursors, symbolic interval/support carriers, hazard signatures, memoization, and exact integer-root fallback are Pareto-optimal.",
  "next_action": "Implement and benchmark a Collapse Atlas oracle/runtime prototype, prove/check boundary correctness and hazard sufficiency in the declared workloads, and return a measured representation/work/latency Pareto with a narrow shared-tool recommendation.",
  "dependencies": [
    {"target": "R021 accepted branching-collapse tool calculus", "action": "CONSUME_NO_RESURRECTION_AND_RESOURCE_ACCOUNTING", "satisfied": true},
    {"target": "R023/R023I BRC semantic Lean core", "action": "CONSUME_BOOLEAN_SUPPORT_AND_RECOALESCENCE_BOUNDARY", "satisfied": true},
    {"target": "R020 accepted P021 dynamic-completeness audit", "action": "CONSUME_TYPED_SUPPORT_COUNT_PROVENANCE_BOUNDARIES", "satisfied": true},
    {"target": "EnterpriseMath/Arithmetic/IntegerRoot.lean", "action": "CONSUME_EXACT_BASIN_CHARACTERIZATION", "satisfied": true}
  ],
  "source_refs": [
    "EnterpriseMath/Arithmetic/IntegerRoot.lean",
    "R021 Draft PR #496 / accepted branching-collapse report",
    "R023 Draft PR #498 and R023I Draft PR #499",
    "R020 Draft PR #501",
    "research_tasks/R021_COLLAPSE_ATLAS_ACCELERATOR_ADDENDUM_20260811.md",
    "R014 representation-resource methodology"
  ],
  "evidence_status": "RUNTIME_ACCELERATOR_DISCOVERY_GATE",
  "last_progress_ref": "R020 accepted / R023I exact replay accepted / Collapse Atlas post-R021 proposal",
  "last_progress_at": "2026-08-11T20:58:00+08:00",
  "hard_block": null,
  "tags": ["R024", "collapse-atlas", "integer-root", "basin", "cache", "runtime", "branching-collapse", "hazard-signature", "benchmark", "pareto"],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R024",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:a03b06c1c6d29ca2776592fd12aa77406f45a21afb8fc1a8431b25cd41963c77",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R024 — Collapse Atlas Runtime Accelerator and Collapse-Domain Navigation

Status: `READY / P0 / HIGH_TOOLING_LEVERAGE / RUNTIME ACCELERATOR DISCOVERY / NOT CANONICAL`

## 1. Task purpose

R021 established that BRC has a real sparse/symbolic/table-precompute Pareto regime while `NO_RESURRECTION` forbids hiding lost pointwise information in free branch metadata. R023/R023I froze the exact Boolean/result-support semantic core. R020 separated Boolean support, nonnegative path-count, and witness/provenance carriers.

This task therefore does **not** reopen BRC semantics. It asks a narrower execution question:

> Given the exact p-th-power collapse basins already proved by Enterprise Math, what runtime representation and navigation algorithm minimizes lookup/precompute/storage/branch-decision cost under declared workloads while preserving exact semantics?

The object is a reusable **Collapse Atlas** runtime candidate, not a new Foundation primitive.

## 2. Frozen mathematical substrate

Consume, do not re-prove, the exact positive-exponent basin law from `EnterpriseMath/Arithmetic/IntegerRoot.lean`:

`collapse p n = k^p` iff `k^p <= n < (k+1)^p`.

Thus a collapse basin is the half-open interval

`[k^p, (k+1)^p)`.

Keep these APIs semantically distinct even if they share the same boundary data:

- exact fine integer `n`;
- lower-collapse value `k^p`;
- root index `k`;
- bracket/cell label;
- full basin/fibre descriptor;
- exact support interval/subset;
- BRC branch/hazard token;
- future-support signature.

No floating-point root may be theorem-critical. Any approximate seed must be followed by exact integer boundary verification.

## 3. R024-T01 — workload model before optimization

Define at least three benchmark workloads:

1. **RANDOM_LOOKUP** — independent random `(p,n)` queries over declared `P_max,N_hot` distributions;
2. **LOCAL_TRAJECTORY** — sequential/local updates `n -> n+c_t` or monotone scans with high basin locality;
3. **BRC_BRANCH_HEAVY** — branch/support execution concentrated near collapse boundaries where hazard classification matters.

Add at least one mixed/reuse workload with a skewed hot-set distribution.

Every performance claim must name:

- integer domain / bit width;
- `P_max`;
- `N_hot` or query distribution;
- query count;
- warm/cold cache state;
- representation serialization format;
- exact semantic output being requested.

Do not declare one universal fastest strategy independent of workload.

## 4. R024-T02 — dense table baseline

Implement a dense baseline storing per-state collapse data for bounded hot domains.

At minimum compare variants storing:

- lower-collapse value only;
- root index only;
- root index plus boundary/hazard metadata.

Charge actual packed bytes, not only abstract entry count. Python-object overhead may be reported separately but must not be mistaken for the representation lower bound.

Kill pressure: dense `n -> collapse_p(n)` duplicates the same label across every point in one basin. It should survive only if bounded-domain latency/reuse justifies that storage.

## 5. R024-T03 — perfect-power boundary atlas

For each selected exponent `p`, store ordered anchors

`0^p,1^p,2^p,... <= N_hot`.

Use exact search to locate `k` with

`k^p <= n < (k+1)^p`.

Measure:

- anchor count;
- packed storage;
- binary-search latency;
- bucket/interpolation-index variants if exact verification is retained;
- build/update cost.

Benchmark at least `N_hot = 10^9, 10^12, 10^15, 10^18` analytically or materially as feasible, with at least two `P_max` choices.

Record that anchor count is approximately

`sum_{p=2..P_max}(floor(N_hot^(1/p))+1)`

and is usually dominated by square anchors. Test the hypothesis that `p=2` should use an exact integer square-root rather than a complete boundary table, while higher powers may profit from atlas storage.

## 6. R024-T04 — basin cursor / local navigator

Implement a local state such as

`(p,k,L=k^p,U=(k+1)^p,offset=n-L,distance=U-n)`.

For local updates, avoid recomputing integer roots while the new state remains in `[L,U)`.

When a boundary is crossed, update `k,L,U` exactly. Compare:

- one-step adjacent boundary update;
- repeated crossing for large jumps;
- fallback root/search when a jump exceeds a declared threshold.

Measure amortized root calls, boundary updates and latency on monotone scans and bounded translations.

## 7. R024-T05 — finite-difference boundary generation

For fixed `p`, exploit that `k^p` is a degree-p polynomial sequence and its p-th finite difference is constant.

After exact initialization, generate consecutive anchors/gap widths using additions only.

Verify exact equality against direct integer powering over broad bounded ranges. Include mutation tests for off-by-one difference initialization.

Compare build throughput and energy/work proxy counts against repeated exponentiation.

Do not claim addition-only generation improves random lookup unless the workload actually consumes sequential anchors.

## 8. R024-T06 — exact root fallback and hybrid indexing

Implement an exact fallback using integer nth-root or equivalent verified search.

Compare hybrids such as:

- `p=2` exact isqrt + higher-p boundary atlas;
- sparse anchors + exact root correction;
- coarse bucket index + local exact boundary search;
- memoized recently-hit basins + exact fallback.

A hybrid must remain correct for arbitrary inputs outside `N_hot` and for cache misses.

## 9. R024-T07 — symbolic support interval carrier

R021 showed that some legitimate support semantics stay compact even when pointwise futures would force fine refinement.

Implement exact symbolic support for interval-like arithmetic cases, at minimum:

- a full floor-quotient fibre translated by `+c`;
- a full p-th-power open-gap interval under positive translation.

Track exact interval endpoints rather than enumerating all fine states when mathematically valid.

Compare:

- fine-state enumeration;
- coarse branch list;
- exact interval token;
- interval + boundary atlas.

This is a support-semantic optimization only. It must never be advertised as recovering an unknown exact point.

## 10. R024-T08 — future-hazard signatures

For a declared future generator family `G`, define/cache the minimum exact information needed to decide whether a current basin/support can execute the next generator without splitting.

For translations, investigate signatures based on distance-to-boundary / threshold classes rather than eagerly restoring the full residue or fine point.

Distinguish:

- `ONE_STEP_HAZARD_EXACT`;
- `FINITE_SUFFIX_HAZARD_EXACT`;
- merely heuristic hazard classes.

A hazard cache that is exact for one step but reused for a longer suffix without proof is a failure.

For any cached class, return the factorization/sufficiency condition or exhaustive finite evidence supporting the declared scope.

## 11. R024-T09 — BRC integration benchmark

Integrate the candidate atlas with a small exact BRC executor/oracle without modifying shared BRC semantics.

Compare at least:

A. exact fine execution;
B. exact BRC with raw set/branch atoms;
C. BRC + boundary atlas;
D. BRC + basin cursor;
E. BRC + symbolic interval support;
F. BRC + hazard cache;
G. chosen hybrid.

Measure separately:

- resident representation bytes;
- precompute/build time;
- random lookup latency;
- local update latency;
- branch-decision latency;
- live branch width;
- exact root calls;
- cache hit rate;
- transition work;
- serialized cache/table size;
- amortized cost over repeated queries.

All branch tokens, interval endpoints, dictionaries, hazard metadata and cache indices are charged.

## 12. R024-T10 — exactness and mutation suite

Build focused tests including:

- every stored perfect-power boundary;
- random interior basin points;
- lower/upper off-by-one mutations;
- stale cursor after boundary crossing;
- stale hazard signature after future-language change;
- approximate-root seed one below/above the exact root;
- cache corruption / wrong exponent entry;
- interval carrier accidentally widened to a full fibre;
- one-step hazard class incorrectly reused at horizon 2+.

Where practical, cross-check independent implementations: direct exact nth-root, boundary search, cursor, and atlas.

## 13. R024-T11 — Pareto and selection policy

Return a workload-parameterized Pareto table over at least:

- preprocessing time;
- packed storage;
- resident memory;
- per-query latency;
- local trajectory latency;
- branch-decision latency;
- exact root-call count;
- online work;
- cache rebuild/update cost;
- reuse/amortization threshold.

The final policy must select strategy as a function of workload, e.g.

`Strategy = F(bit_width, P_max, N_hot, locality, query_reuse, future_language, support_shape)`.

Do not hard-code a universal `P_max` or `N_hot` without an explicit workload assumption.

## 14. R024-T12 — shared-tool recommendation

If a robust exact regime survives, propose a narrow API boundary, suggested conceptual surface:

- `locate_basin(p,n)`;
- `basin_descriptor(p,k)`;
- `advance_cursor(cursor,delta)`;
- `support_interval_step(interval,op)`;
- `hazard_signature(state_or_support, future_descriptor)`;
- `exact_fallback(p,n)`.

Do not publish to shared common surface in this task. Return the exact proposed API, typing, evidence status and ownership route to Driver.

## 15. Kill criteria

A negative result is acceptable. Kill or sharply scope the atlas hypothesis if:

- exact nth-root is already faster/smaller for the relevant workload after cache effects;
- square-boundary storage dominates all benefits;
- cursor locality is too weak in realistic workloads;
- hazard signatures reconstruct essentially the full fine coordinate at comparable cost;
- cache invalidation by future-language changes destroys reuse;
- symbolic support ceases to remain compact under intended generators;
- packed table gains disappear once serialized/index/cache metadata is charged;
- the winning strategy is simply a standard library integer-root plus tiny memoization.

## 16. Required artifacts

Return:

1. `R024_COLLAPSE_ATLAS_REPORT.md`;
2. executable prototype/oracle, suggested `experiments/r024_collapse_atlas.py`;
3. focused correctness/mutation tests;
4. machine-readable benchmark/result JSON;
5. strategy/Pareto table;
6. workload definitions;
7. memory/anchor-count estimates through at least `10^18` where materialization is safe or analytically estimated;
8. exact semantic typing table;
9. proposed shared runtime API or explicit `NO_SHARED_TOOL_RECOMMENDED`;
10. one explicit answer to: **what should Enterprise Math actually use at runtime for collapse-domain lookup and BRC boundary decisions?**

## 17. Return classes

Preferred hybrid positive return:

`COLLAPSE_ATLAS_ACCELERATOR_FOUND / HYBRID_PARETO_FROZEN / EXACT_RUNTIME_CHECKED / SHARED_TOOL_CANDIDATE / NOT_CANONICAL`

If boundary atlas dominates in the target workload:

`BOUNDARY_ATLAS_DOMINATES_DENSE_TABLE / EXACT_LOOKUP_CHECKED / NOT_CANONICAL`

If cursor/fallback dominates:

`CURSOR_PLUS_EXACT_FALLBACK_DOMINATES / PRECOMPUTATION_NARROWED / NOT_CANONICAL`

If dense bounded table is actually justified:

`DENSE_TABLE_JUSTIFIED_IN_DECLARED_HOT_DOMAIN / WORKLOAD_SCOPED / NOT_CANONICAL`

If optimization is immaterial:

`PRECOMPUTATION_NOT_MATERIAL / EXACT_ROOT_BASELINE_DOMINATES / NO_SHARED_TOOL_RECOMMENDED / NOT_CANONICAL`

## 18. Scope boundary

No R021/R023 theorem change. No BRC semantic strengthening. No P021 count/provenance collapse. No canonical/common-surface rewrite. No new Lean proof required unless a tiny correctness lemma is independently useful; if so, return it as a proposed later payload rather than widening this task.

CI is not required for research. Benchmark/probe locally or in the researcher environment and return exact commands/environment metadata. GitHub should remain sparse until a semantic/performance checkpoint.