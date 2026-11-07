# BRC local residual counting: floor, nearest-square, and adaptive partitions

Date: 2026-11-07 (Asia/Hong_Kong).

## Outcome

The centered local representation repairs the intended counter-range failure:
the paired 100,000-value jitter input needs only 160 local counters, versus
39,724,660 cells for the rejected global floor-residual rectangle and 8,762,458
for floor-local ranges. Its complete sort took 1,211.964 microseconds, compared
with 1,260.703 for the preceding full-minimum global BRC implementation and
623.656 for the existing affine-range baseline. Frequency sorting took 315.940.
Thus the representation result is strong; an overall performance advantage
over the ordinary competitors was not obtained.

Across all 24 measured conditions, even the retrospectively fastest of the four
new variants did not beat the fastest of the six ordinary candidates in that
condition. This is a comparison of the implementations and matrix measured here,
not an implemented oracle dispatcher or a universal ranking.

## Question

Continue from the preceding 65-condition experiment. Its paired jitter kept
every root prediction correct, but increased the global residue span from 8 to
1,986,233. The global BRC representation switched from a 160-cell joint count
to coordinate radix sorting. This experiment tests whether exact local
residual ranges can remove that inflation, including the cost of constructing
and selecting the representation.

The output is the full numerically ascending `uint64` array with multiplicity.
No original-index stability is requested for this pure-value interface. All
algorithms receive only the array, with no family name, generating parameters,
cluster map, or precomputed state.

## Reused scientific input

The preceding source is pinned at Enterprise Math commit
`5b8f9f76cd187d9d5aaa62028af6a9e5e2710b28`, path
`experiments/brc_residual_sort_expanded_20261107_b0e94005/pure_bench.cpp`,
Git blob `868723dc6b627b7230d4c54149d276537138b7aa`.

`local_bench.cpp` includes that source with its original entrypoint renamed.
Thus existing generators, reference algorithms, exact root/divider routines,
and diagnostics are reused without copying or changing the frozen baseline.
The predecessor's exact-root and reciprocal checks remain applicable. This
experiment adds focused checks for the new partitions, indexing, reconstruction,
adaptive selection, and the actual instrumented/uninstrumented implementations.

## Exact partition laws

The floor-square class is

```text
k = floor_sqrt(x)
x belongs to [k*k, (k+1)*(k+1)-1].
```

The nearest-square class is

```text
c = k + (x-k*k > k).
```

There is no integer tie because the gap between adjacent squares is odd.
For `c>=1`, its exact cell is

```text
c*c-c+1 <= x <= c*c+c.
```

The zero cell contains only zero. At the top of the `uint64` domain, `c` may
equal `2^32`; implementations store a relative class index rather than casting
that center to `uint32`. Cells are clipped to the declared input domain when
necessary. These are ordered, disjoint integer intervals, so visiting classes
in increasing order and values within each class in increasing order yields
the requested numerical order.

The centered residue `x-c*c` can be negative. This is an exact integer
coordinate, not a signed branch weight or a physical interpretation. The hot
counting path does not need to materialize it: for a class minimum `lo`,

```text
(x-c*c) - (lo-c*c) = x-lo.
```

Each occupied class learns actual `lo` and `hi`. Its row has
`hi-lo+1` counters. The total is

```text
L = sum over occupied classes of (hi-lo+1),
```

instead of one rectangular `B*D` grid. A prefix sum assigns row offsets;
counting and full numerical reconstruction preserve every occurrence.

### Constructive invariance under cluster jitter

Let the input labels generate values

```text
x = (K+j)^2 + e + delta_j,
0<=j<B, 0<=e<D, |delta_j|<=A.
```

If `A<=K-1` and `A+D-1<=K`, then every value remains in the nearest-square
cell `c=K+j`: the signed displacement is between `-(K+j)+1` and `K+j`.
For fixed labels, a common displacement of each cluster shifts both its local
minimum and maximum by the same amount. Hence its local width, occupied class
set, multiplicities, and **sum L remain exactly unchanged**. In particular,
`L<=B*D`, even when some labels are absent. The old quarter-K jitter and the
held-out half-K/three-quarter-K families with D=8 satisfy these conditions.

Floor-square grouping alone can merge the upper residues of one displaced
cluster with the small residues of another cluster. Conversely, larger positive
shifts can preserve floor classes while crossing nearest-square boundaries.
The adaptive implementation measures both actual local-range totals and chooses
the cheaper viable counter layout. This minimizes that measured counter
requirement among its candidates; its extra learning work is also timed.

## Implementations

`local_kernels.hpp` provides:

- `local_floor_cached`: exact floor-square classes, local ranges, cached relative
  class indices.
- `local_center_cached`: nearest-square classes, local ranges, cached indices.
- `local_center_recompute`: the same centered partition, recomputing classes on
  the counting pass instead of storing an n-element index vector.
- `local_adaptive_cached`: learns floor and centered local ranges in one
  classification pass, chooses an actual viable layout, and reuses cached
  floor-relative indices.

Both endpoint roots are computed inside each call. Per-element classification
uses the existing complete-minimum predictor and exact one-step repair/fallback.
The monotonic predictor's maximum candidate is checked once: when every square
fits `uint64`, the kernel uses that width; otherwise candidate arithmetic uses
`u128`. Zero anchors, wide candidates, and the upper integer boundary retain
exact recovery. Known endpoint roots can be reused directly.

All local-range and prefix sums use wide arithmetic before allocation. Actual
counter and bucket caps remain explicit. Inapplicable/oversized layouts fall
back to offset radix on the original values, including all setup already
performed. Diagnostics distinguish local counts, selected partition, and radix
fallback; 1,024 cells on a radix path describe the actual radix table, not the
demanded local range. A zero residue span after an early exit means it was not
computed.

On an accepted layout with bounded per-element state extraction, counting plus
full output costs `O(n+B+L)`, with additional index storage `O(n)` for cached
variants and no n-element index array for the recomputing variant. Endpoint
roots, state extraction, allocation, selection, and fallback work are included
in the measured total. Reported vector bytes/counter cells are named data
structures, not measured peak RSS.

### Output-observer comparison

A nondecreasing bucket map `q(x)` and exact within-bucket numerical order also
suffice to sort all values. The preceding affine baselines already use this
fact: their bucket index need not equal an exact square-root coordinate.
They preserve the numbers through actual local values and counts. Therefore
exact BRC-coordinate recovery is useful retained structure whose cost must be
compared with these simpler order-preserving carriers. The existing affine
baseline is kept as a competing algorithm, not relabeled as a new BRC gain.

## Method and reproducibility

The focused matrix keeps the preceding deterministic label sequences and adds
three held-out signed jitter amplitudes, K/8, K/2, and 3K/4. Each amplitude has
one distinct fixed offset seed; its eight banks vary label/sample draws, not
the cluster-offset seed. A separate positive [0,5K/4] control crosses the
nearest-square partition boundary while retaining floor classes.
It includes small/large uniform inputs, distinct values, larger residual widths,
values near `10^12`, `9*10^18`, and the `uint64` endpoint.

Each actual bank is checked against exact reference output for every measured
algorithm, both with and without diagnostic collection. Performance uses eight
rotating banks, seven rounds with randomized algorithm order, and a nominal
12 ms per algorithm/round. Input copies, setup, all allocations, classification,
selection, counting/sorting, complete output, and destruction are timed;
generation, correctness checks, and diagnostic collection are outside timing.
The recorded quantiles summarize batch averages, not confidence intervals.

Default reproduction from this experiment directory in the pinned repository:

```bash
python run_experiment.py --max-n 1000000
python run_experiment.py --sanitize --verify-only
python analyze_results.py
```

For a separately supplied preceding source, pass `--base-source /path/to/pure_bench.cpp`.
The helper records the expected source pin separately from its supplied path;
the actual published experiment's source identities and execution are recorded
in its receipts. AddressSanitizer and UndefinedBehaviorSanitizer are used with
`ASAN_OPTIONS=detect_leaks=0`, reusing the predecessor's observed executor
limitation on LeakSanitizer `/proc` task enumeration.

## Governance and evidence status

The valid global read lease is reused: `c36e525df5094cce80698b9603021922c92588a2`,
verified 2026-11-07T09:51:31Z. Previously read applicable entry, code, mathematics,
output, P000, and research-method rules remain in this control phase. Scientific
inputs retain their separate immutable pins. The current native `em_status`
attempt again returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH`,
`operation_sent=false`. Canonical researcher/activity metadata remains
unconfirmed. The derivation and shared-context code review are author-side
evidence; source persistence does not assert independent mathematical admission.

## Actual results

### Execution and verification

- Compiler: g++ 13.3.0, C++20, `-O3 -DNDEBUG -Wall -Wextra`.
- Runtime: Linux x86_64, AMD EPYC 9V74; performance pinned to CPU 0.
- Actual benchmark: 2026-11-07T11:38:57Z to 11:41:11Z; 134.576 seconds wall time,
  including the benchmark program's independent input/output checks.
- 24 conditions, 12 algorithms, 288 rows, 192 actual input banks, seven timing
  rounds. All banks passed checks for both instrumented and timed paths.
- Focused optimized verification: 5,715 input arrays, 49,048 checked algorithm
  outputs, 72 midpoint boundary values, 40 paired-control banks, unique 100,000
  values, cap boundaries, actual uint128 nonendpoint correction, and independent
  local-layout/selection oracles: PASS.
- The same focused suite with AddressSanitizer and UndefinedBehaviorSanitizer:
  PASS, empty runtime stderr. LeakSanitizer was disabled for the documented
  executor limitation; no leak-check result is claimed.
- One retained compiler warning belongs to the included, renamed old `main`,
  whose implicit `return 0` rule no longer applies after renaming. That unused
  historical entrypoint is never called; the active entrypoint and new kernels
  compile without warnings.

The benchmark receipt records actual source hashes, binary hash, base Git blob,
compiler, CPU, command, timing, exit code and result hash. No benchmark was run
concurrently by the collaborating agents. Their source/mathematical review
shared this task context and is not independent formal admission.

### The representation result and its limits

All rows below use n=100,000, K=1,000,000, B=20, D=8, the same sampled labels,
and matched actual numeric endpoints. These are **demanded** cells computed
independently from the input, before caps; rejected layouts are not allocated.

| Input displacement | Global floor rectangle | Floor-local L | Center-local L | Adaptive choice |
|---|---:|---:|---:|---|
| None | 160 | 160 | 160 | Floor, tie |
| Prior signed quarter-K jitter | 39,724,660 | 8,762,458 | 160 | Center |
| Held-out signed K/8 | 39,627,160 | 11,221,113 | 160 | Center |
| Held-out signed K/2 | 39,867,860 | 7,984,808 | 160 | Center |
| Held-out signed 3K/4 | 38,255,300 | 5,640,758 | 160 | Center |
| Positive [0,5K/4] | 21,879,260 | 160 | 6,398,703 | Floor |

This verifies the predicted partition-dependent behavior. Merely making rows
local does not prevent a large hole when the floor partition merges displaced
clusters. Centering fixes that family, but the positive-shift control shows
why it is not an unconditional replacement for floor grouping.

The center cached variant on the paired quarter-K input uses 160 counters
(1,280 bytes here), 400,000 bytes of relative indices and 480 bytes of bucket
metadata. The entire algorithm's extra storage is therefore not just 160 cells.
The original BRC implementation rejects the 39.7-million-cell layout and uses
coordinate radix; it never allocates that hypothetical rectangle.

### Complete sorting cost

For the paired quarter-K jitter, center-local versus the preceding full-minimum
global BRC algorithm was:

| n | Global BRC division, microseconds | Center-local, microseconds | Ratio global/center | Center wins among 7 rounds |
|---:|---:|---:|---:|---:|
| 10,000 | 112.811 | 121.092 | 0.932 | 1 |
| 100,000 | 1,260.703 | 1,211.964 | 1.040 | 5 |
| 1,000,000 | 14,920.000 | 13,033.262 | 1.145 | 6 |

At n=100,000 the center p10-to-p90 range was 1,172.777--1,319.261 microseconds;
the global baseline range was 1,230.699--1,301.820. The 3.9% median reduction is
small against this run's batch variation. The older square-anchor BRC variant
was 1,192.832 microseconds on the same data, also slightly below center-local.
These quantiles and round counts do not constitute confidence intervals.

At n=1,000,000 the center variant reduced median elapsed time by 12.6% against
global BRC division. The affine-range baseline still took 6,919.681 microseconds
and frequency sorting 3,445.304. All algorithms produce the full million-value
output, including repeated occurrences. There are 160 distinct values in this
family; the frequency baseline makes that structure explicit.

The unjittered n=100,000 input already fits the old 160-cell rectangle. Center
local counting took 1,372.999 microseconds versus 727.643 globally, so the added
local-range work provides no compensating counter reduction there.

The unique n=100,000 input avoids the repeated-value benefit: center-local took
1,634.800 microseconds, old full-minimum BRC 890.521, and offset radix 714.249.
Thus the failure to outperform the strongest ordinary competitor is not solely
an artifact of including a frequency-sort baseline.

### Cache, selection, and early exits

On the paired n=100,000 jitter input:

- Cached center: 1,211.964 microseconds; 400,480 bytes in index/bucket vectors.
- Recomputed center: 2,272.284 microseconds; 480 bytes in bucket vectors. Its
  prediction count doubles from an average 98,733.25 to 197,466.5 because it
  actually classifies again. Both variants additionally allocate 1,280 counter
  bytes, and both include the common input work vector in timing.
- Adaptive: 1,557.712 microseconds. It correctly chooses the 160-cell center
  layout, but learning both layouts costs more than the fixed centered version.
- Positive [0,5K/4] input: adaptive chooses the 160-cell floor layout and takes
  1,408.300 microseconds versus center-local's 1,721.296 fallback and fixed
  floor-local's 1,201.116. Counter minimization and elapsed-time minimization
  are different objectives.

The largest apparent speedup occurs for 100,000 uniform values below 10^12:
center-local takes 1,043.544 microseconds versus global BRC's 8,953.159. Its
bucket-span check rejects the layout after two endpoint roots and invokes
offset radix. That improvement is an early-rejection result, not a fast
centered counting result; direct offset radix takes 872.013 microseconds.

For the original 100-value uniform input below 10^6, `std::sort` takes 0.574
microseconds, center-local 5.629, and adaptive 7.491. The new structure has not
improved that original small-input task.

### Research frontier after this run

The useful retained increment is the exact nearest-square partition and its
proved local-width invariance under stated perturbations, together with explicit
counter/bucket caps and full-domain fallback. The measured sorting interface
does not yet benefit enough from exact-coordinate recovery to beat the simpler
ordinary competitors. This benchmark is not a phase-level CPU profile, so it
does not identify one arithmetic instruction as the unique bottleneck.

The next focused question is whether a cheap monotone bucket map, learned from
a bounded sample or certified from endpoints, can retain small actual local
ranges without exact root recovery for every input. Existing affine baselines
already establish a strong benchmark for that route. Its acceptance criterion
should be total sorting cost, including sampling, learning, validation and
fallback. Another exact-root iteration or always learning two complete layouts
is not supported as the default next step by these results.

For the accepted fixed-width count path, the derived cost remains O(n+B+L).
In the stated cluster family L<=BD, yielding O(n+B+BD) when classification cost
is bounded. On a variable-width integer model, division/root and output-bit
costs must remain explicit; for general input B and L need not be small. The
actual implementation applies caps and includes its radix recovery path.

### Full matrix

The following ordinary-candidate column is the retrospectively fastest of
`std_sort`, offset radix, range count/radix, frequency sort, affine-range local,
and affine-square local. It is not a measured adaptive dispatcher. The raw CSV
retains every algorithm, selected path, independent demanded widths, diagnostic
counts, seven raw timings and summary quantiles.

| Family | n | Previous BRC division, µs | Center local, µs | Adaptive, µs | Fastest ordinary candidate, µs |
|---|---:|---:|---:|---:|---|
| uniform_1e6 | 100 | 4.088 | 5.629 | 7.491 | std_sort: 0.574 |
| uniform_1e6 | 100,000 | 5739.637 | 5015.804 | 5246.959 | offset_radix: 596.884 |
| uniform_1e6 | 1,000,000 | 56673.623 | 56281.004 | 57291.827 | offset_radix: 5862.183 |
| uniform_1e12 | 100,000 | 8953.159 | 1043.544 | 1037.151 | offset_radix: 872.013 |
| square1e6_s0 | 10,000 | 71.022 | 128.156 | 154.346 | frequency_sort: 41.085 |
| square1e6_s0 | 100,000 | 727.643 | 1372.999 | 1732.260 | frequency_sort: 296.900 |
| square1e6_s0 | 1,000,000 | 7881.646 | 14042.611 | 15604.596 | frequency_sort: 2818.865 |
| jitter1e6_B20_D8 | 10,000 | 112.811 | 121.092 | 141.198 | frequency_sort: 39.377 |
| jitter1e6_B20_D8 | 100,000 | 1260.703 | 1211.964 | 1557.712 | frequency_sort: 315.940 |
| jitter1e6_B20_D8 | 1,000,000 | 14920.000 | 13033.262 | 16012.678 | frequency_sort: 3445.304 |
| square900_s0 | 100,000 | 666.785 | 1280.571 | 1542.002 | range_count_or_radix: 338.681 |
| jitter900_B20_D8 | 100,000 | 981.043 | 1373.373 | 1617.433 | frequency_sort: 270.096 |
| square900_s1790 | 100,000 | 657.725 | 1224.925 | 1501.446 | range_count_or_radix: 315.191 |
| square1e6_s1999990 | 100,000 | 667.652 | 1261.793 | 1445.755 | frequency_sort: 266.936 |
| square1e6_B256_D8 | 100,000 | 684.773 | 1281.790 | 1502.096 | affine_square_local: 664.832 |
| square1e6_B256_D512 | 100,000 | 1508.631 | 2324.312 | 2618.148 | offset_radix: 772.012 |
| unique1e6_B256_D512 | 100,000 | 890.521 | 1634.800 | 1975.281 | offset_radix: 714.249 |
| square3e9_B20_D8 | 100,000 | 739.705 | 1261.397 | 1591.550 | frequency_sort: 318.096 |
| square900_anchor7 | 100,000 | 829.123 | 1366.078 | 1564.731 | frequency_sort: 318.304 |
| uint64_top_window | 100,000 | 903.589 | 752.672 | 735.544 | offset_radix: 557.703 |
| heldout_jitter_K8 | 100,000 | 1226.295 | 1224.803 | 1466.368 | frequency_sort: 301.268 |
| heldout_jitter_K2 | 100,000 | 1243.432 | 1185.707 | 1531.472 | frequency_sort: 322.556 |
| heldout_jitter_3K4 | 100,000 | 1217.491 | 1186.353 | 1469.292 | frequency_sort: 345.462 |
| positive_jitter_5K4 | 100,000 | 1212.924 | 1721.296 | 1408.300 | frequency_sort: 305.383 |
