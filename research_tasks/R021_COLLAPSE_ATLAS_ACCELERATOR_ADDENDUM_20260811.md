# Post-R021 Proposal — Collapse Atlas / Collapse-Domain Accelerator

Status: `POST_R021_PROPOSAL / DRIVER_REVIEW_REQUIRED / NOT_DISPATCHABLE / NOT_CANONICAL`
Source foundation: `RS-R021-BRANCHING-COLLAPSE-TOOL-CALCULUS` accepted/frozen result

This file records a follow-up optimization proposal discovered after the R021 mother task was already accepted and frozen. It is **not** an active R021 addendum and must not reopen or alter the frozen R021 theorem package. A current Driver may route it as a bounded owner continuation or a new optimization task if priority justifies dispatch.

## A. Question

Determine whether repeated collapse/future execution should use a precomputed collapse table, an optimized collapse-domain navigator, or a hybrid.

Do **not** default to a dense table `n -> collapse_p(n)`. The proven integer-root structure partitions the natural states into basins

`[k^p, (k+1)^p)`

on which the lower perfect-power collapse is constant. The tool should exploit interval/boundary structure directly.

The design space must be parameterized by both:

- exponent cap `P_max`;
- hot numeric domain `N_hot`.

There is no meaningful fixed answer of the form "precompute up to exponent p" without also fixing the numeric domain and workload.

## B. Strategies to compare

### B1. Dense state table

Store `collapse_p(n)` (and/or bracket/fibre metadata) for every `0 <= n <= N_hot`.

Treat this mainly as a baseline/kill candidate because it duplicates the same basin label across many states.

### B2. Perfect-power boundary table

For each hot exponent `2 <= p <= P_max`, store only ordered anchors

`0^p, 1^p, 2^p, ... <= N_hot`

and locate the basin by search.

Measure compact-array storage rather than Python-object overhead when comparing representations.

The anchor count is approximately

`A(N_hot, P_max) = sum_{p=2..P_max} (floor(N_hot^(1/p)) + 1)`,

and is dominated asymptotically by the square anchors.

Benchmark at least `N_hot = 10^9, 10^12, 10^15, 10^18` (the latter two need not be fully materialized if memory is excessive) and at least two `P_max` choices.

### B3. Basin cursor / local navigator

For local or sequential execution maintain a state such as

`(p, k, L=k^p, U=(k+1)^p, offset=n-L, distance=U-n)`.

A future operation that moves `n` locally should update this cursor without recomputing an integer root until a boundary is crossed.

Measure amortized cost for scans and bounded translations.

### B4. Addition-only boundary generation

Exploit finite differences of the polynomial sequence `k^p`.

For fixed `p`, after initializing the finite-difference vector, generate consecutive p-th-power anchors and gap widths using additions only. Compare this with repeated exponentiation/root calls.

At minimum recover familiar special cases such as

`(k+1)^2 = k^2 + 2k + 1`

and generalize via finite-difference recurrence.

### B5. Sparse anchor + exact integer-root fallback

Test a hybrid in which only sparse/hot anchors or bucket indices are retained and arbitrary queries fall back to an exact integer root with final integer boundary verification.

No theorem-critical floating-point root is allowed.

### B6. Future-hazard cache

For the declared future generator set `G`, attach to a basin/cell only the information needed to know whether the next generator is safe inside the current branch or requires a split.

For translations this should expose boundary-crossing classes using offset/distance-to-boundary instead of eagerly restoring the complete fine state whenever possible.

For branching collapse, compare:

- raw cell lookup;
- cell + hazard class;
- on-demand branch partition;
- full residue/offset refinement;
- exact fine state.

The hazard cache is valid only if its classes are proved/checked sufficient for the declared future language; it must not silently introduce a one-step-only approximation into multi-step execution.

## C. Collapse Atlas candidate architecture

Evaluate a tiered `Collapse Atlas` design:

1. `HOT_BOUNDARIES`: packed perfect-power boundary arrays for selected `(p, N_hot)`;
2. `BASIN_CURSOR`: local state for nearby transitions;
3. `HAZARD_SIGNATURE`: language/generator-relative split information for on-demand branching;
4. `MEMOIZED_HOT_CELLS`: optional cache for repeatedly hit cells/signatures;
5. `EXACT_FALLBACK`: integer nth-root / verified boundary search outside the hot domain.

The atlas must return semantic objects with explicit typing: lower-collapse value, bracket/cell label, full fibre descriptor, branch/hazard token, or exact state. Do not merge these APIs merely because they share boundary data.

## D. Resource and correctness gates

Measure separately:

- preprocessing time;
- serialized/packed storage;
- resident memory;
- random-query latency;
- local/sequential-query latency;
- branch decision latency;
- cache hit rate under declared workloads;
- update cost when `P_max`, `N_hot`, or future language changes.

Correctness must be checked at every exact boundary and for random interior states. Include mutation tests for off-by-one upper/lower anchors and stale hazard classes.

The raw dense table should be rejected unless it wins under a clearly declared bounded workload after storage is charged honestly.

## E. Follow-up decision classes

A future bounded accelerator task/continuation should return one of:

- `DENSE_TABLE_JUSTIFIED_IN_BOUNDED_HOT_DOMAIN`;
- `BOUNDARY_ATLAS_DOMINATES_DENSE_TABLE`;
- `CURSOR_PLUS_FALLBACK_DOMINATES_PRECOMPUTATION`;
- `HYBRID_COLLAPSE_ATLAS_PARETO_FRONTIER`;
- `PRECOMPUTATION_NOT_MATERIAL`.

It must state recommended `(P_max, N_hot)` selection policy as workload-dependent, not as a universal constant.

This proposal does not alter R021 acceptance, R023 semantics, or shared-tool status by itself.
