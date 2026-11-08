# Sampled local residual counting and exact exception repair

Research started: 2026-11-08, Asia/Hong_Kong.

## Parent question and current experiment

The parent question is whether residual classification can improve complete
integer sorting, and which forms of iteration repay their cost. The preceding
experiment proved a conditional nearest-square local-width invariance, but its
per-value exact coordinate extraction and range learning did not beat the
strongest ordinary comparator in the measured matrix.

This experiment tests a cheaper monotone coarse coordinate. A bounded sample
learns ragged numerical residual intervals. The complete input scan counts exact
members and retains every uncovered value. The intended observer is the full
ascending uint64 multiset, including all repeated occurrences. These are integer
data and an order observer, not a new spatial model or a native cell-address
codec. The underlying project P000 and declared spatial typing are unchanged.

Scientific dependencies are the frozen previous sources:

- `5b8f9f76cd187d9d5aaa62028af6a9e5e2710b28`,
  `experiments/brc_residual_sort_expanded_20261107_b0e94005/pure_bench.cpp`,
  Git blob `868723dc6b627b7230d4c54149d276537138b7aa`.
- `4b66597bce400f6d19336058ac780e877188a769`,
  `experiments/brc_residual_sort_local_20261107_b0e94005/local_kernels.hpp`,
  Git blob `3c5a7302066f333a084101a3ab08b37f974660de`.

The implementations are included unchanged. The small condition recipes retain
their original deterministic generators and prior input identities.

## Exactness independent of sample quality

The coarse coordinate is a monotone integer map

```text
q(x) = (x-origin) >> shift
```

inside its declared range. `origin` is aligned to a power-of-two boundary.
Each sampled coarse bin receives a learned local interval `[lo_q, hi_q]`,
expanded by a bounded pad and clipped to that coarse bin. The learned intervals
are ordered and disjoint. Every actual input value is explicitly tested against
the coarse range and its local interval before counting.

The retained state is the exact count of every covered numerical value plus the
full list of uncovered values. It is sufficient for the declared multiset and
numerical-order observer: each input occurrence contributes exactly once, and
all stored values are reconstructed exactly. A sampled constant does not imply
that the entire array is constant. Values below the sampled origin, absent bins,
outliers and uint64 endpoints are ordinary preserved exceptions.

Before successful counting finishes, the input array remains unchanged. A
rejected layout or excessive exception count can therefore invoke the existing
exact radix sorter on the original values. On an accepted path, count rows emit
the covered values in numerical order, exceptions are sorted, and a backward
merge restores the complete output with multiplicity.

For S sampled values, B coarse bins, L allocated local counters, n inputs and m
exceptions, the fixed-width accepted path costs

```text
O(S + B + L + n + m log(m+1)).
```

This includes sample learning and full reconstruction/merge. The actual code's
named vectors, caps and fallback costs are recorded separately from peak RSS.
Sample quality determines the accepted path and speed, while exact membership
checks and exception retention determine correctness.

### BRC carrier and reuse

The old square-root/residual code remains an executed competitor. The new
representation reuses the exact local-value histogram observation law and the
existing radix recovery, and extends its classification mechanism. It retains
the exact numerical multiset. Any deterministic BRC label f(x) remains
recoverable from each distinct retained value; provenance tied to the original
position is outside this pure-value interface, as in the preceding experiment.

## Iterating only the residual exception problem

The recursive extension applies another learned layout only to the retained
exceptions. Let m_0=n and m_(i+1) be the actual exception count at level i. An
accepted level requires

```text
m_(i+1) <= floor(m_i/2),
L_i <= min(4*1024*1024, max(4096, floor(m_i/2))),
S_i = min(m_i,1024), B_i <= 1025.
```

Then the total classified population, including each level's reconstruction and
merge, is bounded by

```text
sum_i m_i <= n + n/2 + n/4 + ... < 2*n.
```

This is a deterministic certificate based on actual counts, not a probability
claim from the sample. A modeled node has m_i>=257; hence B_i<4*m_i and
L_i<16*m_i. Sample collection, bucket learning, counter initialization,
membership checking, emission and backward merge each cost O(m_i). The geometric
bound applies separately to these phases; it does not claim that the entire
sort performs only 2*n operations.

The first rejected cell layout or failed contraction invokes exact offset radix
on that node's still-unchanged array. Recursion depth 16 also terminates in
radix; nodes of at most 256 values use comparison sorting. The inherited radix
sort performs at most seven ten-bit passes for uint64, with its allocation,
min/max scan, counter clearing and complete output included. Therefore the whole
recursive algorithm has worst-case O(n) time and O(n) auxiliary storage in this
fixed-64-bit word-cost model, assuming successful allocations. The retained
parent vectors and descendant vectors are bounded by the same geometric sum.
This is neither an arbitrary-precision natural-number result nor an improvement
over the established asymptotic bound of fixed-width radix sorting. The original
single-layer sampler already has O(n) worst-case time here because its exception
sort is capped at 4096 entries and its recovery is radix. Recursion changes the
useful accepted region and its measured constants, not that asymptotic class.

### A constructive family with small residual width

For 20 clusters I_j=[a+j*2^g,a+j*2^g+7], j=0..19, with a aligned to 2^g,
g>=8 and all values inside uint64, a sample touching every cluster gives
shift=g-5, origin=a and cluster coordinate q_j=32*j. Each complete eight-value
cluster is inside its learned padded interval. Thus the scan has no exceptions
and L<=800, independent of the overall numerical span. This is a conditional
deterministic statement. For independent uniform cluster labels at S fixed,
distinct sample positions, the probability of missing a cluster is at most
20*(19/20)^S. The actual constructed benchmark forces two endpoint observations;
the IID expression is a separate model, not a literal claim about every generated
position. The harness directly checks the sample-coverage premise and predicted
zero exceptions instead of relying on that probability.

An additional mathematical family illustrates why residual iteration can help:
K<=256 distinct point values a+j*2^g with a aligned to 2^g and all values inside
uint64, each repeated T>=34 times, uniformly randomly permuted. With k_i
remaining value classes, the distinct coarse bins give L_i<=17*k_i and
m_i=T*k_i, hence L_i<=m_i/2; also 17*K is below the absolute counter cap.
The current cell budget therefore accepts. Deleting complete covered value
classes leaves a uniformly permuted residual multiset. With k remaining classes
and S=min(m,1024), sampling without replacement gives
E[m_next/m] <= (1-1/k)^S <= exp(-S/k). When m>=1024 this is at most exp(-4),
about 1.83%; Markov's inequality bounds the probability of more than half
remaining by 2*exp(-4), about 3.67%. When m<=1024 the sample sees every value.
These probability statements require this explicit random-permutation model.
At a rejection there is no child, so conditional expected child size is no
larger than this expected spill size. Iterating the bound gives expected total
node input at most n/(1-exp(-4)), approximately 1.0187*n, in this model. This
counts subproblem input sizes, not all operations or elapsed time. The executed
contraction guard and exactness proof do not require the probabilistic model.

## Existing algorithmic context

Sampling, sorting uncovered spill values and merging are established components
of sampled/learned sorting. LearnedSort 2.0 describes this pattern and discusses
the cost of handling sampled repeated keys by a hash table:
https://arxiv.org/pdf/2107.03290, Sections 2--3.
The present experiment measures an exact integer shift-bin/local-value-counter
implementation and its cost tradeoffs; it does not rely on a learned model's
prediction being exact.

Recursive radix/comparison hybrids are also established; Boost's official
Spreadsort documentation describes selecting recursive radix or comparison
processing according to the subproblem:
https://live.boost.org/doc/libs/1_85_0/libs/sort/doc/html/sort/single_thread/spreadsort/sort_hpp/rationale/hybrid_radix.html.
Neither that implementation nor LearnedSort is timed in this matrix. Performance
claims below refer to the explicitly executed candidates, not to all published
or industrial integer sorters.

## Method

The harness includes the existing comparison, radix, dense-count, hash-frequency,
affine-local and BRC implementations. A dynamically growing flat open-address
frequency counter is added as a strong ordinary comparator. A full-data
shift-local method separates the effects of a cheap coordinate from sampling.
S=1024 and S=4096 sample variants expose learning-cost tradeoffs.

Every timed candidate receives only the value array. Generating cluster count,
width, square anchor and jitter are not supplied to any sorter. The flat hash
table is an empirical competitor; fixed hashing and linear probing do not give
it a worst-case linear-time guarantee.

Known calibration conditions are selected before viewing new results. Other
legacy conditions form regression coverage, and new independent cluster-offset
seeds, skew, sparse tails, endpoint outliers, deterministic sample traps and
unstructured uint64 data form the held-out evaluation. Eight banks and seven
randomized timing rounds retain the preceding inclusive measurement convention:
copy, setup, allocations, complete sorting/output and destruction are timed.
Generation, diagnostic collection and reference checking are outside timing.

The first calibration had 9 conditions and 14 candidates. Its exact pre-recursion
sources and 126 rows are preserved under `calibration_v1/`. The final frozen
implementation adds the recursive candidate, retains all 34 original conditions,
and adds 5 explicitly constructed mechanism witnesses. The final matrix has
39 conditions and 15 candidates: 9 calibration, 15 regression, 10 new held-out,
and 5 mechanism conditions. `evaluation` means the 25 regression-plus-held-out
conditions; it excludes calibration and constructed witnesses. Mechanism cases
are not random-generalization evidence.

The freeze is recorded in `frozen_implementation.json`. No implementation or
parameter tuning follows observation of the final held-out timings. Each CSV
numeric diagnostic is averaged over 8 banks, including the column named
`recursive_max_depth`; exact maxima and actual node paths must instead be read
from the accompanying `.recursive_nodes.csv`. That sidecar records integer
per-node input, sample, hit, spill, counter, emission, merge and terminal data.
Named auxiliary-vector byte counts are not peak RSS: they exclude counter
arrays (reported separately), diagnostic trace storage, stack and allocator
overhead. Recursive descendants must also be included when assessing storage.

Reproduction from this experiment's directory in the project repository:

```bash
python run_experiment.py --subset all
python run_experiment.py --sanitize --verify-only --subset final
python analyze_results.py results_all.csv
```

For separately supplied dependencies, pass `--base-source` and `--local-kernels`.
The runner writes actual command, environment, stdout/stderr and exit receipts.
Address/undefined sanitizers run with leak checking disabled; no leak-check
result is claimed.

The final optimized correctness receipt records 8,324 input-array invocations,
85,244 reference-output checks across diagnostic and actual nullptr timing paths,
and 12 focused recursive cases. The same checks pass with address/undefined
sanitizers. All seven recursive routes are exercised, including exact-half and
half-plus-one contraction, child sizes 256/257, multi-level alternating uint64
extrema, independent child cell-budget failure, and the explicitly forced
depth-16 terminal. The forced-depth test is not described as a naturally reached
depth in these input sizes. The unchanged square-root/divider tests from the
frozen sources are reused. The only compile warning is the frozen old `main`
renamed into an unused ordinary function with its inherited implicit return.

## Actual results and current frontier

The frozen final run succeeded: **39 conditions, 585 timing rows, 312 input
banks, and 404 exact recursive-node trace rows**. It ran in one process pinned
to CPU 0, using g++ 13.3.0, C++20, `-O3 -DNDEBUG`, on the reported Intel Xeon
Platinum 8573C environment. The command elapsed 228.703 seconds. Full actual
environment/command/exit/stdout/stderr are in `execution_all_frozen.json`.

The comparison below uses the minimum median of eight ordinary candidates in
each condition: std sort, offset radix, global range count/radix, standard hash
frequency, flat hash frequency, affine-range local, affine-square local, and
full-data shift-local. This is a conservative retrospective comparator, not an
implemented selector that knows in advance which algorithm is fastest.

| Condition | n | Best ordinary | Ordinary µs | Recursive S1024 µs | Ratio ordinary/recursive |
|---|---:|---|---:|---:|---:|
| Original uniform values below 1e6 | 100 | std_sort | 0.491 | 0.583 | 0.843 |
| New quarter-jitter cluster seeds | 100,000 | frequency_sort | 456.642 | 236.328 | 1.932 |
| New three-quarter-jitter cluster seeds | 100,000 | frequency_sort | 470.821 | 260.526 | 1.807 |
| 90% of draws in cluster 0 | 100,000 | flat_frequency | 393.264 | 229.808 | 1.711 |
| Two full-width outliers | 100,000 | frequency_sort | 499.678 | 384.190 | 1.301 |
| Rare distant cluster | 100,000 | frequency_sort | 464.068 | 1113.852 | 0.417 |
| Uniform uint64 | 100,000 | offset_radix | 2505.581 | 2615.660 | 0.958 |
| Uniform support of 4096 values | 100,000 | range_count_or_radix | 460.565 | 1255.203 | 0.367 |
| 20 jittered narrow clusters | 1,000,000 | frequency_sort | 5350.325 | 3088.158 | 1.733 |
| Uniform values below 1e6 | 1,000,000 | offset_radix | 13289.953 | 17868.963 | 0.744 |

All values above are medians from the same frozen run. The original n=100 case
does not benefit. Large narrow-cluster inputs do show a repeatable mechanism
advantage within this measured matrix, while dense small domains, broad uniform
data, and rare distant clusters expose important failure regions. A distant
sample can enlarge a coarse bin's learned numerical width enough to reject the
entire layout. Increasing sample count can therefore make that case worse.

### What the iteration itself changed

For the calibrated 256-cluster/eight-value-width condition, n=100,000:

| Policy | Median µs | Actual route over 8 banks |
|---|---:|---|
| Single layer, S=1024 | 1069.099 | 5 radix recoveries; 3 direct spill merges |
| Recursive residual, S=1024 | 418.900 | 8 genuine one-edge residual recursions |
| Single layer, S=4096 | 317.714 | 8 zero-spill counting paths |
| Best ordinary reference: full-data shift-local | 637.296 | 8 full-data counting paths |

Recursion improves the small-sample variant by **2.552x** here, but the larger
single-layer sample is faster still. Mean recursive input processed is
101,238.75, only 1.0123875 times the root size. This is not a claim of only 1.24%
total overhead: the same path emits 100,000 histogram values and performs
71,246.875 backward-merge assignments on average, in addition to learning and
counter work.

The two new jitter rows in the first table have no exceptions and only one
node. Their speedups validate cheap sampled local counting, not a benefit from
iteration. Conversely, uniform support of 4096 values really uses two recursive
edges and mean total node input 138,095.875, yet is **2.725x slower** than direct
range counting. Geometric contraction alone does not imply competitive speed.

The four-edge constructed witness follows exactly
131072 -> 65536 -> 32768 -> 16384 -> 8192 in every bank. Summed node input is
253,952, histogram emission is 131,072, and backward-merge assignments are
163,840. Its recursive time is 975.017 µs; flat frequency takes 356.539 µs.
This establishes executed multi-level behavior and the work accounting, not
superiority over the ordinary baseline. All five constructed mechanism cases
lose to the best ordinary median.

### Evaluation counts and limits

| Fixed candidate | Evaluation median wins / 25 | Evaluation ratios >=1.10 / 25 | New held-out median wins / 10 | New held-out ratios >=1.10 / 10 |
|---|---:|---:|---:|---:|
| Single layer S1024 | 20 | 19 | 6 | 5 |
| Single layer S4096 | 20 | 18 | 6 | 4 |
| Recursive S1024 | 20 | 19 | 6 | 5 |

The 25 evaluation conditions contain 15 legacy regression cases, many deliberately
covering narrow clusters, and 10 new held-outs. These counts are not a probability
of winning on arbitrary user data. Seven randomized rounds are within one
process on one environment. p10/p90 values are empirical quantiles, not confidence
intervals; the 1.10 threshold is descriptive, not a statistical significance test.
Small apparent improvements on radix-recovery paths (for example uniform1e12,
wide B256/D512, and the positional trap) are not attributed to recursion or a
new algorithmic advantage. Their timing ranges overlap the ordinary comparators.

The supported research conclusion is **conditional practical value**: short local
residual intervals permit exact counting without scanning the enormous global
value span, and certified spill recursion repairs some insufficient samples.
The complete uint64 output is exact. No new general integer-sorting complexity
bound, universal performance lead, or exact native-BRC-coordinate output speedup
is established. The ordinary value observer retains information sufficient to
recover deterministic BRC labels per distinct value; that downstream coordinate
materialization is not included in these timing numbers.

The concrete remaining frontier is a cheaper decision between direct dense
counting, compact learned intervals, residual iteration and radix, especially
when rare outliers expand the learned scale. This run establishes the positive
region and counterexamples before any such selector is designed. No selector
was tuned against these new held-outs.

### Files

- `sampled_kernels.hpp`: exact single-layer, full-data and recursive kernels.
- `flat_frequency.hpp`: ordinary flat-table frequency baseline.
- `sampled_bench.cpp`: frozen inputs, verification, timing and node tracing.
- `results_all.csv`, `results_all.csv.recursive_nodes.csv`: complete measurements
  and exact per-bank recursion observations.
- `results_table.md`, `analysis_summary.json`, `evaluation_speedup.svg`: derived
  comparisons. `analyze_results.py` recreates them and the PNG preview.
- `sampled_*_v2.json`, `execution_sanitized_final.json`,
  `execution_all_frozen.json`, `frozen_implementation.json`: actual validation,
  execution and implementation-freeze receipts.
- `calibration_v1/`: preserved pre-recursion source and calibration evidence.

## Control and source scope

Current global entry snapshot:
`036e24c743bd26542f84022195def378b1828f5a`, verified 2026-11-08T15:02:54Z.
Current source control read snapshot:
`d7e56a1821bfcef28e22a6701980474955247b0c`.
These current normative inputs are separate from the frozen scientific sources.
The native session registration succeeded and was canonically published at
`c6093d644d9c98acc1ec04e9798625755ce36b2e`:

- Researcher-ID: `EM-DIRECT-1F3468` / `TASK_RESEARCH`.
- Activity: `RA-F9EFA12FBDF0EE5FF9158589`.
- Activity path: `research_activity_records/RA-F9EFA12FBDF0EE5FF9158589.json`.
- Own service-issued session: `MCP-0d700f879f2c408195398e03c2999279`.
- Source activity startup guard: `activity_allowed=true`,
  `persistence_allowed=true`, `required_action=CONTINUE_ACTIVITY`, using the
  original native immutable readback. No formal shared Task CLAIM is attached
  to this direct-question experiment.

Shared-context agent checks are author-side review and preserve the real
contribution history. The source activity record tracks publication receipts
separately from mathematical acceptance. These experiments and derivations do
not claim independent formal review, a shared Task completion, or project-wide
mathematical acceptance.
