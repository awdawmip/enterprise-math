# R024 Collapse Atlas Runtime Accelerator — Frozen Return

Researcher-ID: `EM-R024-7C20D0`  
Task: `RS-R024-COLLAPSE-ATLAS-RUNTIME-ACCELERATOR`  
Taskbook source: `0a0af206326a873f28620426371f894ccc92db51`  
Status: `EXECUTABLE_CHECKED / NOT_CANONICAL / NO_R021_R023_SEMANTIC_CHANGE`

Return:

`COLLAPSE_ATLAS_ACCELERATOR_FOUND / HYBRID_PARETO_FROZEN / EXACT_RUNTIME_CHECKED / SHARED_TOOL_CANDIDATE / NOT_CANONICAL`

## Driver decision

Enterprise Math should use a workload-adaptive exact hybrid, not one universal table:

- `p=2`: exact `isqrt`; **do not** materialize all square boundaries.
- `p=3`: adaptive `{full cube atlas | exact verified hot cache | exact nth-root}` according to memory and expected reuse.
- `p>=4`: packed perfect-power boundary atlas for reused 64-bit hot domains, with exact integer-root fallback outside `N_hot`.
- local trajectories: a charged basin cursor `(p,n,k,L,U)` with immediate root fallback for large jumps.
- contiguous Boolean/result-support: exact 16-byte interval/root-support carriers before per-atom execution.
- stable future language with enough reuse: exact structural-versioned hazard cache; otherwise interval+atlas/root directly.
- dense state table: tiny bounded-domain/high-reuse latency mode only, never the default.

No theorem-critical floating-point root is used. R021/R023 semantics are consumed unchanged.

## Frozen substrate

`EnterpriseMath/Arithmetic/IntegerRoot.lean` already proves:

`collapse p n = k^p` iff `k^p <= n < (k+1)^p` for positive exponent.

The runtime therefore locates the exact half-open basin `[k^p,(k+1)^p)`. Fine state, collapse value, root index, basin descriptor, support interval, hazard token, and cache metadata remain distinct types. Metadata is not free.

## Workloads and environment

Frozen local benchmark environment: Python 3.13.5, Linux x86_64/glibc 2.41, AMD EPYC 9V74. Full min/median/max, packed bytes, resident bytes, build times, root-call counts, cache rates, branch width and mutations are in `research/r024_benchmark_results.json`.

Workloads:

1. `RANDOM_LOOKUP`: 40k uniform `(p,n)`, `p=2..8`, `n<=10^18`.
2. `LOCAL_TRAJECTORY`: 100k monotone p=3 deltas `0..128`; separate 20k large-jump probe `0..10^13`.
3. `BRC_BRANCH_HEAVY`: 4k translations of a 512-state contiguous support ending at a cube boundary.
4. `MIXED_HOT_REUSE`: 60k queries, 92% from 72 hot basins, 8% random.
5. `DENSE_MICRO_HOT_DOMAIN`: p=3, `N_hot=250000`.
6. `SEQUENTIAL_ATLAS_BUILD`: finite-difference versus direct power generation.

## Result 1 — p=2 must use exact isqrt

At `N_hot=10^12`, exact `isqrt` measured 229.6 ns median. A complete square-boundary binary-search atlas measured 1.066 us, required 8,000,008 packed bytes and ~228 ms to build.

At `N_hot=10^9`, isqrt was 226.9 ns versus 690.6 ns for a 252,984-byte square atlas.

Analytical packed square-boundary storage:

- `N_hot=10^18`: 8,000,000,008 bytes.
- full unsigned-64 domain: 34,359,738,368 bytes (32 GiB).

So Driver question 1 is answered **yes**: abandon the full p=2 boundary table. Use exact `isqrt`, with cursor locality when available.

## Result 2 — p>=3 splits into p=3 and p>=4

At `N_hot=10^18, P_max=16`, all p>=3 anchors occupy about 8.30 MB packed, but p=3 alone occupies 8,000,008 bytes. The complete p=4..16 layer is only 299,784 bytes. Across the full unsigned-64 domain, p=4..16 still needs only about 604 KB packed.

Dedicated p=3 scaling:

| N_hot | packed cube atlas | atlas median | exact-root median | speedup | build crossover |
|---:|---:|---:|---:|---:|---:|
| 1e9 | 8,008 B | 512 ns | 835 ns | 1.63x | ~1.3k q |
| 1e12 | 80,008 B | 540 ns | 1.042 us | 1.93x | ~5.0k q |
| 1e15 | 800,008 B | 627 ns | 1.229 us | 1.96x | ~45k q |
| 1e18 | 8,000,008 B | 824 ns | 1.150 us | 1.40x | ~805k q |

A separate interleaved p=3 run narrowed to about 1.07x, and another random p3 subbench measured ~902 ns atlas versus ~1.211 us root. This cache sensitivity is a real reason not to mandate a resident cube atlas for every process.

For p=4..16 at `10^18`, packed storage ranges from ~253 KB down to 112 B. The frozen run measured roughly 2.10x–5.97x lookup speedups over exact root, with build crossover from about 16k queries at p=4 down to tens/hundreds for larger p. Therefore complete p>=4 boundary atlases are genuine hot-domain wins.

The tested stride-64 sparse cube atlas was slower than exact root under uniform random lookup, so it is rejected for this Python runtime. A secondary bucket index also did not survive the frozen p3 random subbench after index memory/build was charged.

Driver question 2 therefore has a qualified positive answer: **full higher-power atlases are strongly justified for p>=4; p=3 is reuse/cache dependent; the tested simple sparse p3 atlas is not justified.**

## Dense table

For p=3, `N_hot=250000`:

- dense collapse u64: ~257 ns, 2,000,008 packed bytes;
- dense root u32: ~287 ns, 1,000,004 packed bytes;
- dense root+next-boundary: ~349 ns, 3,000,012 packed bytes;
- boundary atlas: ~384 ns, 504 packed bytes;
- exact root: ~692 ns.

Dense therefore survives only as an explicit tiny-domain latency-for-memory option. Against the atlas, its build/latency crossover is on the order of 0.3 million queries. It is not a scalable default.

## Cursor

For p=3 local deltas `0..128`, the 40-byte cursor measured ~119 ns/update versus ~716 ns exact-root recomputation. Across 100k updates it made one initial exact root call and only 94 adjacent boundary updates.

For large jumps `0..10^13`, naive repeat-then-fallback cost ~1.945 us and performed ~73.8k boundary updates. The smart cursor precheck cost ~1.412 us, near the ~1.423 us exact-root baseline, by falling back before grinding through many boundaries. `advance_cursor` must therefore have a declared crossing threshold.

## Finite-difference boundary generation

For fixed p, consecutive `k^p` anchors are generated from exact initial forward differences using additions only. Broad equality tests match direct integer powering and an off-by-one difference mutation is detected.

CPython finite-difference generation was slower than built-in powering in the frozen benchmark. R024 therefore returns it as an exact native/streaming builder candidate and work-proxy tool, **not** as a Python speed claim or random-lookup optimization.

## Hot cache

A naive linear interval LRU achieved ~90.9% hits in the skewed workload but cost ~3.76 us/query, slower than exact root (~1.25 us). High cache hit rate does not imply a win when index/search work is charged.

The exact coarse-bucket cache realized 3,505 entries, ~140,296 packed bytes (~1.0 MB Python resident), ~77.8% warm hits, ~22.2% exact-root fallback calls, and ~707 ns/query. Every candidate hit checks exact `(p,L,U)` membership; wrong-exponent/corruption mutations become misses and are repaired by exact fallback. This is the recommended memory-constrained p=3 hot-set option.

## Exact symbolic support

Two exact support cases are implemented:

- full floor-quotient fibre translated by `+c`;
- full p-th-power basin/gap interval translated by positive `+c`.

A floor-fibre example compressed 10,000 u64 states (80,000 bytes) to a 16-byte exact interval. A cube-basin example compressed 3,003,001 states (~24 MB packed) to 16 bytes. This represents the exact support set, not an unknown exact point.

Because collapse is monotone on a contiguous integer interval, Boolean/result-support after collapse is exactly represented by the root-index interval determined from the two endpoints.

## Exact future hazard

`FutureDescriptor` is compared by structural equality. `FutureRegistry` allocates a non-reused runtime version token. The 64-bit digest is diagnostic only and never establishes semantic identity.

For the declared finite p=3 future family, 6,181 bounded support samples produced 18 exact outcome classes under `(one_step_bits,suffix_bits)`. All declared hazard queries factor through that exact decision vector. One-step and finite-suffix safety are stored separately; mutation testing includes a state that is one-step safe but not safe at horizon 3.

Changing the future descriptor changes the version and stale reuse raises `STALE_HAZARD_SIGNATURE`.

## BRC integration

Exact Boolean/result-support outputs were cross-checked across:

- A fine exact execution: ~661 us/query, 2,048,000 root calls;
- B raw BRC atoms + exact root: ~625 us/query, 2,048,000 root calls;
- C per-atom atlas: ~278 us/query, zero root calls;
- D per-atom cursor: ~458 us/query, 512 initialization/fallback root calls;
- E symbolic interval + exact root: ~3.43 us/query;
- E2 symbolic interval + atlas: ~1.95 us/query;
- F exact versioned hazard dictionary: ~758 ns warm;
- F2 exact hazard + bisect: ~871 ns warm.

Mean live branch width was 1.248. The hazard signature/registry/dictionary were all charged; total hazard build was ~3.43 ms and its measured crossover versus interval+atlas was ~2.9k decisions. Thus hazard caching is enabled only for stable future languages with enough reuse; otherwise E2 is the simpler exact branch-decision path.

## Exactness and mutation gates

The full local research harness recorded 330,714 correctness checks with all declared mutations detected. The focused publication suite additionally verifies every stored boundary and lower neighbor for the chosen `p=3..16, N_hot=10^18` higher-power atlases.

Covered failures include lower/upper off-by-one, finite-difference initialization, stale cursor, approximate seed ±1 correction, wrong exponent/cache corruption, interval widening, stale future language, and improper one-step hazard reuse at longer horizon.

Publication extraction test command:

`PYTHONPATH=experiments python3 -m unittest -v tests/test_r024_collapse_atlas.py`

Result: `9 tests / OK`. The larger local harness: `12 tests / OK`.

## Runtime selection policy

`Strategy = F(bit_width, P_max, N_hot, locality, query_reuse, future_language_stability, support_shape, memory_budget, latency_target)`.

Recommended order:

1. p=2 -> exact isqrt.
2. Live local path -> basin cursor; large jump -> exact fallback.
3. Exact contiguous Boolean support -> symbolic interval/root-support interval.
4. p>=4 reused hot domain -> packed boundary atlas + exact fallback.
5. p=3 -> choose full cube atlas, exact verified hot cache, or exact root from reuse/memory regime.
6. Stable/reused future language -> exact versioned hazard cache; otherwise interval+atlas/root.
7. Dense table only if a tiny fixed hot domain wins after actual packed bytes/build amortization are charged.
8. All misses/out-of-hot-domain -> exact integer nth-root.

## Shared-tool candidate

No common surface is changed by R024. Proposed later API:

- `locate_basin(p,n) -> BasinDescriptor`
- `basin_descriptor(p,k) -> BasinDescriptor`
- `advance_cursor(cursor,delta) -> BasinCursor`
- `support_interval_step(interval,op) -> ExactSupportInterval`
- `hazard_signature(support,future_descriptor) -> HazardSignature`
- `exact_fallback(p,n) -> BasinDescriptor`

Evidence status: `EXECUTABLE_CHECKED / BENCHMARKED / MUTATION_CHECKED / NOT_CANONICAL`.

## Final architecture

`p=2 exact isqrt`

`+ p=3 adaptive {exact root | full cube atlas | exact hot-bucket cache}`

`+ p>=4 packed perfect-power atlas for reused hot domains`

`+ exact integer-root fallback`

`+ basin cursor for local trajectories with large-jump fallback`

`+ exact symbolic interval/root-support for contiguous Boolean support`

`+ structural-versioned hazard cache only when reuse amortizes rebuild`

`+ dense table only as an explicit tiny-domain/high-reuse mode`

This is the R024 Driver recommendation. It does not modify R021/R023 semantics.
