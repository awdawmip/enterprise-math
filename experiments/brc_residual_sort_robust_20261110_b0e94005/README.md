# Robust sampled residual sorting: dense, trimmed and compact intervals

Experiment date: 2026-11-10. This is the first frozen experiment of the current
continuation; a subsequent adaptive repair experiment is motivated by the
failures retained here. All measurements below belong to this experiment's
single final run, not to its earlier calibration runs.

## Result

The two preceding bottlenecks can be repaired on specific distributions.
Trimming a rejected sample layout recovers narrow clusters contaminated by a
few far values. Counting one contiguous sampled interval, while retaining every
outside value as an exact exception, eliminates unnecessary recursive holes in
compact ranges. These changes improve both known target cases and several
fresh input-bank conditions.

The strongest fixed variant here, `robust_compact_1024`, beats the fastest of all
16 declared controls on 6 of the 14 fresh conditions, with a ratio of at least
1.10 on 5. It is at least 10% slower on 5. Its geometric mean speedup against
that retrospective per-condition reference is 0.859, and its median ratio is
0.967. Consequently, these data support a useful specialized improvement, not
a universal replacement or a general complexity breakthrough.

Compared with the previous recursive candidate itself, the compact variant
wins 10 of the 14 fresh condition medians, with 6 ratios of at least 1.10 and a
geometric mean ratio of 1.963. This comparison answers a different question from
the stronger 16-control reference. Both are preserved in the analysis.

## Question, domain and observer

The parent question is whether residual classification and iteration can
accelerate complete ascending integer sorting. The experiment handles full
unsigned 64-bit values, repeated occurrences, endpoints, compact ranges,
multiple clusters, skew and contamination. The original 100 random integers
below one million are still included. The implemented cutoff sends all arrays
of at most 256 elements to comparison sorting; timing differences among those
wrappers do not establish a new sorting method.

The observer is the full ascending numerical multiset. Exact histogram rows
plus retained exceptions preserve every value and multiplicity. Deterministic
BRC labels of values remain recoverable from those retained values. Original
positions and attached records are outside this pure-value interface. This
experiment does not change the project's spatial carrier or address semantics.

## Implementations and causal comparison

The frozen 15 preceding candidates are reused, and upstream `pdqsort` is added
as a mature comparison-sort control. Four new variants bring the total to 20.

| Candidate | Added routing rule | Cost or boundary |
|---|---|---|
| `robust_dense_1024` | If sample span is small, check true full-input extrema and directly count an eligible range | A rejected probe adds a full scan |
| `robust_trim_1024` | Only after oversized original layout, rebuild from inclusive sample ranks S/64 and S-S/64-1 | One global-tail trim can retain interior contaminants or too many tail observations |
| `robust_combined_1024` | Dense gate followed by the single trim repair | Combines both overheads and boundaries |
| `robust_compact_1024` | Count a bounded contiguous sample interval with exact outside exceptions; retain the single trim repair | Avoids the full extrema scan, but actual exception and counter budgets still decide acceptance |

The compact policy was specified before reading the precompact calibration
timings. All four policies were frozen after eight known calibration conditions
and before generating or timing the 14 fresh input-bank conditions. No policy
or parameter was changed after that freeze.

Each modeled node uses a sample cap of 1,024, actual exception acceptance
`spills <= floor(n/2)`, and counter budget

```text
min(4*1024*1024, max(4096, floor(n/2))).
```

Depth 16 terminates in offset radix; arrays of at most 256 values use
`std::sort`. Compact padding and the exact single-bucket representation are
specified in [THEORY.md](THEORY.md) and implemented in
[robust_kernels.hpp](robust_kernels.hpp).

An accepted interval is only a proposed representation. Every actual input
value still undergoes an exact membership check. Values outside it are kept
verbatim. If actual exceptions exceed half the input, the original array is
still intact and the code falls back to exact radix sorting. Otherwise only
the retained exceptions recurse, counted values are emitted in order, and a
backward merge produces the complete output.

## Measured results

Times are microseconds per complete sort. The strongest control is the minimum
median among all 15 preceding implementations plus `pdqsort`, chosen separately
for each condition. This is a conservative retrospective reference, not an
implemented algorithm selector. A speedup greater than one favors the compact
variant.

| Stage | Input condition | n | Previous recursive | Compact variant | Strongest control | Control time | Compact speedup |
|---|---|---:|---:|---:|---|---:|---:|
| Calibration | Rare far cluster | 100,000 | 1,196.696 | 248.428 | frequency_sort | 446.093 | 1.796× |
| Calibration | Uniform values in 4096 positions | 100,000 | 1,088.545 | 307.932 | range_count_or_radix | 419.793 | 1.363× |
| Fresh | 0.01% high tails | 100,000 | 651.674 | 233.546 | frequency_sort | 587.259 | 2.515× |
| Fresh | 1% high tails | 100,000 | 3,657.879 | 319.815 | flat_frequency | 558.025 | 1.745× |
| Fresh | Dense4096 with two extremes | 100,000 | 1,108.746 | 436.354 | frequency_sort | 987.685 | 2.263× |
| Fresh | Dense8192 with 0.3% extremes | 131,072 | 3,640.191 | 859.924 | frequency_sort | 1,991.239 | 2.316× |
| Fresh | 2% high tails | 100,000 | 4,246.394 | 4,235.181 | flat_frequency | 659.181 | 0.156× |
| Fresh | Interior contamination | 100,000 | 1,981.431 | 2,055.009 | flat_frequency | 345.837 | 0.168× |
| Regression | Uniform integers below one million | 1,000,000 | 17,674.730 | 17,777.366 | offset_radix | 12,864.132 | 0.724× |

The complete 58-condition table, all four new variants, all controls and every
loss appear in [analysis_table.md](analysis_table.md). Raw round times and
diagnostics are in [results_all.csv](results_all.csv), with per-bank node traces
in [results_all.csv.robust_nodes.csv](results_all.csv.robust_nodes.csv).

### What actually changed in the target mechanisms

On the known rare-far case, the old recursive method rejects the initial layout
in 4 of 8 banks. The compact variant's global trim repairs those four banks;
the other four retain their already-useful original layout. Mean root counter
demand after repair is 477.875, with 100.5 actual exceptions per bank. The total
recursive input population averages 100,100.5. The sample repair, rather than
deep recursion, accounts for this rescue.

On the uniform4096 case, the previous method has mean total recursive input
138,095.875 and mean merge writes 134,290.125, while its total allocated counter
cells across levels are exactly 4,096. The compact method instead uses a single
count leaf in all eight banks: no spills or merge writes, total input 100,000,
and mean padded counter length 4,107.875. Its median is 307.932 microseconds,
compared with 443.107 for the dense-gate combination and 419.793 for direct
global range counting in the same run. A few extra counters avoid repeated
classification and merging.

On dense4096 with two extremes, compact selection occurs at the root in seven
banks; the remaining bank's original sparse layout is already useful. Actual
root exceptions average 1.875 instead of the previous 31,715.875. Mean total
recursive input falls from 133,872.75 to 100,001.875. Merge writes still average
87,500.125: a small number of low exceptions can shift a long covered suffix.
The cost of merging is included, not inferred to be small from exception count.

On dense8192 with 0.3% extremes, five banks use a trimmed compact interval,
one uses an original compact interval, and two retain an ordinary sparse layout.
Mean total recursive input is 133,296.25 for n=131,072. This shows both the useful
repair and the fact that the policy does not replace every eligible sparse
layout after a successful original budget check.

### Retained failures and stronger reference

All eight 2%-high-tail banks and all eight 5%-two-sided-tail banks reject the
single-trim layout. The compact candidate therefore pays learning/selection
costs and then radix-sorts the full node. In the 2% condition it is about 6.42
times slower than the fastest control. Interior contamination yields six root
budget rejections and two accepted sparse paths, with an overall compact
median about 5.94 times the fastest control.

For the 26 older regression conditions excluding the old deterministic
mechanism cases, compact has two median wins over the strongest control but
none by the descriptive 10% margin. Combining those 26 with the 14 fresh
conditions gives 40 evaluation conditions: 8 median wins, 5 at least-10%
speedups, 13 at least-10% slowdowns, geometric mean speedup 0.888. This broad
aggregate does not support calling the new policy universally faster.

The small 3.9% median advantage on the fresh highly skewed condition is counted
as a median win but not as a 10% result. Seven round quantiles are descriptive;
no significance or confidence-interval claim is made.

## Mathematical findings

[THEORY.md](THEORY.md) gives the exact count/spill invariant, a constructive
20-cluster family with at most 800 padded counters after a successful trim, and
two precise boundaries: the 16/17 upper-tail rank threshold and four central
poisoned bins whose counter demand is at least 65,512 against a 50,000 budget.
The positive family explicitly excludes interior-gap contamination. Neither
failure contradicts the algorithm's exactness; it determines routing cost.

For the chosen fixed-width model, every actual recursive edge has child size
at most half its parent. The sum of node populations is less than 2n; learning,
clearing, emission and merge each have separate charges. The fixed sample and
bucket bounds, actual counter budget and at-most-seven-pass uint64 radix
terminal give O(n) time and auxiliary storage under constant-cost word
operations and successful allocation. This does not improve the known
asymptotic class of fixed-width radix sorting or establish a bit-complexity
result for unbounded natural numbers.

The supplemental exact finite-population calculation in
[sampling_probabilities.json](sampling_probabilities.json) makes the rank
threshold quantitative. Under an ideal uniform shuffle of 100,000 values,
with 1,024 fixed sample positions and 16 ranks trimmed per side, the probability
that the high selected endpoint remains in the high tail is about 3.119% for
1,000 high tails and 81.241% for 2,000 high tails. With only ten actual high
tails it is exactly zero, not a small positive binomial approximation. These
are hypergeometric endpoint events, not probabilities of total sorting success
or measured speed. They were calculated after policy freeze and did not tune
the implementation.

## Experimental method and verification

The matrix has 58 conditions: 8 known calibration, 31 regression, 14 fresh
input-bank conditions and 5 new deterministic mechanism witnesses. The five
old mechanism conditions inside regression retain `original_stage=mechanism`
and are separately summarized. Fresh banks include both random and deliberately
adversarial constructions; fresh does not mean every distribution family was
conceptually unseen.

Every condition has eight input banks and seven randomized algorithm-order
rounds. The nominal target is 12 milliseconds per algorithm/round, with whole
bank cycles; expensive calls can exceed that target. The inherited timer
includes input copying, sample/model construction, allocation, complete output
and vector destruction. Diagnostics run outside the timed region. The timed
specializations do not allocate diagnostic trace vectors. One volatile output
consumer is retained from the frozen timer.

All algorithms use the same compiler and run environment:

- Intel Xeon Platinum 8573C, Linux 6.18.57 x86_64, glibc 2.39.
- GCC 13.3.0, C++20, `-O3 -DNDEBUG -march=native -Wall -Wextra`.
- Performance process pinned to CPU0; no parallel benchmark or compilation by
  this research team during the timed run.
- One process, eight reused banks per condition and seven rounds. Host noise,
  cache effects and frequency behavior remain limits of these local measurements.
  Reported p10/p90 values are empirical quantiles, not confidence intervals.

The optimized and AddressSanitizer/UndefinedBehaviorSanitizer verification
suites each passed 2,824 arrays and 28,238 diagnostic/nullptr output checks for
the four new candidates and pdqsort. These include 1,365 exhaustive short
arrays, 1,364 lifted above the small cutoff, 70 random boundary cases and 25
focused cases. Sixteen meaningful paths were exercised. Leak checking was
disabled; no leak-check result is claimed.

The final benchmark additionally checked all 20 candidates on all 464 banks,
both instrumented and nullptr calls, for 18,560 output checks against std::sort.
It produced 1,160 summary rows and 3,225 recursive node records and exited zero.
The measured binary and all frozen source hashes still matched after the run.

Theoretical source review and diagnostic-accounting review were performed by
a parallel agent with shared author context. [REVIEW.md](REVIEW.md) records
scope and corrections. This is not an independent formal mathematical acceptance.

## Reproduction and artifacts

In a checkout containing the three frozen sibling experiment directories:

```bash
python run_experiment.py --verify-only --cpu 0
python run_experiment.py --sanitize --verify-only --cpu 1
python run_experiment.py --skip-build --skip-verify --cpu 0 --subset all
python analyze_results.py results_all.csv
python sample_tail_probability.py
```

CPU choices must be within the current affinity mask. Running the complete
measurement is optional when only correctness is needed. The runner checks
the exact dependency bytes and records actual commands, compiler, flags,
environment, source hashes, exit codes and output. It does not download code.

- [frozen_implementation.json](frozen_implementation.json): pre-heldout policy
  freeze, hashes, condition design and calibration provenance.
- [execution_optimized_verify_v1.json](execution_optimized_verify_v1.json),
  [execution_sanitized_verify.json](execution_sanitized_verify.json),
  [execution_all_frozen.json](execution_all_frozen.json): actual execution receipts.
- [analysis_summary.json](analysis_summary.json), [analysis_table.md](analysis_table.md)
  and [analysis_heldout_speedup.svg](analysis_heldout_speedup.svg): complete analysis.
- [results_calibration_precompact.csv](results_calibration_precompact.csv) and
  [results_calibration_final.csv](results_calibration_final.csv): developmental
  calibration, kept separate from the final run.

`prepare_frozen_include.py` generates a disposable copy of the preceding
harness with exactly its final main signature renamed. All algorithm,
generator and timer bytes remain unchanged. The generated build file and
executables are not maintained as new source implementations. The precompact
developmental header's inverse-patch recovery is explicitly documented in
[calibration_precompact/PROVENANCE.md](calibration_precompact/PROVENANCE.md).

### Immutable dependencies

| Source | Commit | Relevant file |
|---|---|---|
| Expanded pure sorting | `5b8f9f76cd187d9d5aaa62028af6a9e5e2710b28` | experiments/brc_residual_sort_expanded_20261107_b0e94005/pure_bench.cpp |
| Previous local kernels | `4b66597bce400f6d19336058ac780e877188a769` | experiments/brc_residual_sort_local_20261107_b0e94005/local_kernels.hpp |
| Previous sampled experiment | `8bf6a677359b62d406eaa7258f5541431466315b` | experiments/brc_residual_sort_sampled_20261108_b0e94005/ |
| Upstream pdqsort | `b1ef26a55cdb60d236a5cb199c4234c704f46726` | pdqsort.h, license.txt |

Upstream pdqsort is used unmodified under its Zlib license. Its default
arithmetic comparator selects the upstream branchless route. Source and license
provenance are in [vendor/SOURCE.json](vendor/SOURCE.json). Its published
performance figures are not used as this experiment's measurements.

Primary background: [orlp/pdqsort](https://github.com/orlp/pdqsort) and Pat Morin's
[Counting Sort and Radix Sort](https://opendatastructures.org/ods-cpp/11_2_Counting_Sort_Radix_So.html).

## Continuation frontier

The preserved negative regions motivate a separate adaptive experiment: bounded
successive sample trims and omission of a few excessively wide local bins.
That later experiment must treat these results as known calibration/regression
evidence and use new frozen input banks for fresh evaluation. The present
58-condition results and their frozen policy remain unchanged.

Researcher-ID: EM-DIRECT-10677F / TASK_RESEARCH

Research-Activity-ID: RA-851F29EFE6B4190069FE0D3B

Source activity path: research_activity_records/RA-851F29EFE6B4190069FE0D3B.json

Current control read pin: `5cbc536fa64f10ab4b87acc3d8faf17a6b7fbc58`.
The previous scientific contribution `EM-DIRECT-1F3468` is retained as provenance.
This is an ordinary experiment artifact, not a formal shared-task completion,
theorem promotion or review acceptance.
