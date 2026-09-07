# BRC Opportunistic Shortcut Portfolio — Local Wins Preservation

Status: `TOOLIZED OPPORTUNISTIC PORTFOLIO / EXACT-FALLBACK SAFETY / REGIME TELEMETRY`
Date: `2026-09-07`
Family: `T0_BRC`
Role: preserve locally useful shortcuts that are not universal production rules

## 1. Why this portfolio exists

Earlier Enterprise Math / BRC work repeatedly found methods with the following shape:

- the shortcut is excellent on one finite population or one geometric band;
- it is neutral or negative on a shifted population;
- the setup cost dominates only in some execution regimes;
- or it becomes valuable only when an upstream state has already been computed.

The former promotion discipline correctly refused to call those methods universal
improvements.  But "not universally promotable" is not the same as "worth
forgetting".

This portfolio changes the retention rule:

> A partial shortcut may be preserved if it is cheap to probe, cannot change the
> final mathematical answer after fallback, and has evidence of positive value
> on at least one nontrivial regime.

Heuristic shortcuts therefore act only as **prefixes, orderings, or optional
backend routes**.  A miss falls back to the exact scan-complete path.

The portfolio also records per-regime empirical net value so future work can
discover hidden applicability regions instead of averaging them away.

## 2. Safety contract

The shortcut catalogue uses three safety classes.

### `EXACT`

The shortcut itself preserves all true candidates.  Example: a square-residue
necessary-condition table.

### `CONDITIONAL_EXACT`

The method is exact when its explicit condition holds.  Example: quotient-jet
or energy-jet transport after their proved tail/crossover conditions.

### `HEURISTIC_FALLBACK`

The method may change hit order or cover only a subset, but it can never be the
last word.  Its candidates are tried first and the exact structural candidate
set is appended afterward.

For multiplier ordering, every complete specialist helper verifies

`set(specialist_order) == set(prioritized_odd_multiplier_order(M))`.

For early prefixes such as the 13-kernel set, the portfolio exposes both a
prefix-only probe and a complete order that appends the exact structural
fallback.

## 3. Preserved shortcut inventory

### 3.1 Same-parity structural priority — keep as the baseline expert

For odd semiprimes, the earlier structural score counts admissible same-parity
factor-pair decompositions of a multiplier.

Historical bounded validation:

- old population: feasible ascending mean/median first hit `16.91 / 12`;
- structural order: `8.82 / 5`;
- independent shifted population: ascending `26.36 / 25`;
- structural order: `10.97 / 5`.

The original finite runtime prototype also improved across 128--2048 bit
samples.  This remains the first general expert, while still being a heuristic
ordering rather than an optimality theorem.

Source:
`research_notes/BRC_MULTIPLIER_PRIORITY_JUMP_20260906.md`.

### 3.2 Learned fixed 20-multiplier prefix — preserve despite slight runtime loss

A greedy training-coverage order began

`1,48,96,8,15,80,21,16,56,45,35,3,72,7,99,88,40,55,9,24`.

Historical results:

- old population structural mean/median `8.82 / 5`;
- learned prefix/order `6.01 / 5`;
- independent population structural `10.97 / 5`;
- learned order `8.89 / 5`;
- held-out p90 improved from about `31` to `23`.

The original CPython prototype was a few percent slower because the improved
rank did not offset execution overhead.  That is exactly the kind of result the
portfolio should preserve: if later candidate evaluation is more expensive, or
transport becomes cheaper, the same ordering may become positive.

The portfolio therefore stores only the historical 20-element prefix and
appends the current structural fallback.

Evidence source: conversation experiment, `2026-09-06`.

### 3.3 Log-ratio coverage prefix — retain as a moderate-imbalance specialist

The log-ratio greedy cover began

`1,96,75,45,56,99,72,33,63,55,87,39,21,29,64,48,51,69,15,81`.

It was worse overall, so it was correctly not promoted.  However, on the
diagnostic factor-ratio band `q/p in [2,4]` it improved the median first-hit rank
from roughly `24` to `13` and slightly improved the mean.

The portfolio therefore keeps it behind an explicit
`likely_moderate_factor_imbalance` signal or an exploration slot.  A miss falls
back to the structural order.

Evidence source: conversation experiment, `2026-09-06`.

### 3.4 Exact-gap sorting — retain only when states are already materialized

Gap sorting substantially improved first-hit rank in two finite populations:

- older sample: about `22.55 / 16 -> 10.60 / 6`;
- independent sample: about `35.12 / 33 -> 24.14 / 13`.

It lost wall time because all candidate states had to be generated merely to
sort them.  That negative result does **not** apply when those states already
exist for another observer.

`gap_sorted_order_from_materialized_states()` therefore refuses incomplete
state maps and is only recommended under `states_materialized=True`.

This converts the old failure mode into a context-sensitive shortcut rather
than deleting the idea.

### 3.5 Thirteen squarefree kernels — preserve as an early prefix, never a replacement

The long-horizon `m<=1000` experiment greedily selected the 13 kernels

`(1,13,14,3,15,2,5,6,30,22,105,33,7)`,

covering 98 exact mod-8 representative multipliers.

Measured coverage of full-hittable cases:

- training `101..997`: `10153 / 10153 = 100%`;
- validation `1009..4999`: `16513 / 19481 = 84.7646%`;
- validation `5003..19997`: `14591 / 26399 = 55.2710%`.

Thus it is a bad universal compression theorem but a plausible **cheap early
probe**.  Trying 98 candidates before the full 625-representative `m<=1000`
scan can still have positive expected value on populations resembling either
validation regime, provided a miss continues into the full scan.

Canonical finite evidence:
`research_artifacts/brc_squarefree_kernel_compression_probe_20260907.csv`.

### 3.6 LOW12 compact square-gap table — preserve when filtering is hot

The unsynced Round-14 prototype used the exact necessary-condition cascade

`4096 -> 3465 -> 221 -> 12673`.

The first reduction is division-free:

`value mod 4096 = value & 4095`.

Raw table payload is only `2559` bytes.  All squares pass every stage, so this
shortcut has zero false negatives.

The filter-level microbenchmark improved strongly as gap bit length increased,
while complete pipeline gains depended on whether gap filtering remained the
actual bottleneck.  The portfolio therefore includes an executable
`passes_low12_compact_square_filter()` but does not make it the universal
default.

### 3.7 Table-free tail — storage specialist

The certified Taylor/Pell tail removed O(M) predictor-table dependence but was
not a CPU win in CPython at the tested orders.  It remains valuable in:

- memory-constrained execution;
- environments where static tables are inconvenient;
- very large multiplier horizons where storage scaling matters more than one
  Python benchmark.

It is retained as a conditional backend route, not as a universal speed route.

### 3.8 Quotient/remainder jet — large-bit crossover specialist

The exact stride-8 quotient jet uses only fifteen seed divisions, then bounded
repairs.  The committed finite benchmark crossed over from loss to gain around
the 4096-bit scale in the tested CPython environment.

The portfolio encodes that as a regime trigger, not a theorem about a universal
bit threshold.

### 3.9 Energy difference jet — very-large-bit specialist

The exact energy/square-increment jet removed later general products.  It was
near parity around 4096 bits and favorable at 8192/16384 bits in the committed
benchmark, including roughly 26--29% gain over the fresh-product quotient-jet
path in those large cohorts.

Again: preserve the backend and route by regime rather than forcing one path on
all sizes.

### 3.10 Completion-gap residue jet — ultra-large stream specialist

The unsynced Round-14 experiment transported square-gap residues exactly and
removed recurring full-width modulo operations.  It did not pay at ordinary
RSA-like bit sizes in CPython; the observed crossover was only in the tens of
thousands of bits and long scans.

The portfolio keeps the route descriptor disabled by default and activates it
only for ultra-large, long, filter-dominated contexts.

### 3.11 Pisano/rank metadata probe — cross-family opportunistic specialist

The earlier Fibonacci-side work found strong local divisor reduction when a
Pisano period/rank was **already available**.  Computing that metadata from
scratch can erase the gain.

The portfolio therefore keeps a metadata-triggered route only:

`pisano_period_available -> try the Pisano/rank probe first`.

No claim is made that one should compute the period just to activate the
shortcut.

### 3.12 Cheap BRC shadow observables — preserve as telemetry, not a router

Earlier adaptive attempts using small residues of `N`, `J`, `R`, and a BRC
phase quartile did not show stable held-out ordering gain.  The old conclusion
"do not promote this classifier" remains correct.

The portfolio changes only what happens to the **observables**.  Function
`brc_shadow_signature()` preserves a cheap exact tag

`(N mod M, J mod M, R mod M, phase quartile)`.

It does not alter candidate order by itself.  When outcome logging is already
enabled, the tag can be appended to the regime key.  This lets future evidence
show whether a shortcut is positive in a small hidden cell without re-running
the failed classifier design.

### 3.13 Fibonacci/delete-code compression — preserve as a storage specialist

The earlier additive/Fibonacci experiment achieved more than 90% table-space
compression in some bounded encodings (about 91.2% for one `k=6`
configuration), while semiprimes did not become meaningfully more
distinguishable than ordinary integers.

That is a negative factor-leakage result but a positive **storage** result.
The portfolio therefore keeps a disabled-by-default storage descriptor.  It is
not tried as a direct factor oracle; it becomes relevant only when the problem
is compact representation or table transmission.

## 4. Round-robin multiplier probing

The new helper `multiplier_probe_batches()` implements the user's desired
policy directly.

It cycles through cheap expert streams with a configurable small `quantum`:

1. structural priority;
2. learned 20-element prefix;
3. optional ratio specialist;
4. optional 13-kernel specialist.

Already-tried multipliers are deduplicated.  After specialist prefixes are
exhausted, one final `structural_fallback` batch contains every remaining exact
mod-8 representative.

Therefore:

- occasional specialist success saves work;
- specialist failure costs only its bounded prefix;
- no candidate is tested twice;
- the union remains scan complete.

## 4.1 Current mod-8 portfolio rank recheck

A fresh finite recheck was run after the current exact mod-8 representative
reduction, so every compared order contained the same 62 candidates for
`m<=100`.

### Population A — all distinct semiprimes from primes 101..997

| order | mean rank | median | p90 | top-10 rate |
|---|---:|---:|---:|---:|
| structural | 8.67 | 5 | 21 | 67.25% |
| learned prefix + fallback | **6.08** | 5 | **13** | **83.15%** |
| ratio prefix + fallback | 8.97 | 6 | 19 | 72.72% |
| round-robin structural+learned, q=4 | 6.80 | 5 | 16 | 79.09% |
| round-robin + ratio, q=4 | 7.03 | 5 | 18 | 79.50% |

### Population B — 20,000 deterministic pairs from primes 1009..4999

| order | mean rank | median | p90 | top-10 rate |
|---|---:|---:|---:|---:|
| structural | 13.79 | 11 | **31** | 47.93% |
| learned prefix + fallback | **11.49** | **7** | 33 | 59.68% |
| ratio prefix + fallback | 15.27 | 13 | 33 | 49.25% |
| round-robin structural+learned, q=4 | 12.01 | **7** | 33 | **62.02%** |
| round-robin + ratio, q=4 | 12.50 | **7** | 36 | 58.36% |

This illustrates the purpose of the portfolio:

- the learned prefix is excellent on mean/median rank but slightly worsens the
  held-out p90 relative to structural;
- structural is more conservative in the tail;
- a four-candidate round-robin preserves much of the learned median advantage
  while retaining more structural diversity;
- the ratio expert remains a specialist and should not be globally enabled.

The benchmark is rank-only.  It does not assert wall-clock gain, because the
value of earlier rank depends on the downstream candidate cost.

Artifact:
`research_artifacts/brc_opportunistic_shortcut_rank_probe_20260907.csv`.

## 5. Regime telemetry: preserve hidden patterns instead of averaging them away

`RegimeShortcutLedger` records, per cheap observable regime:

- attempts;
- hits;
- probe cost;
- saved cost;
- empirical expected net saving.

The default coarse regime key includes:

- N bit-length bucket;
- expected transition-count bucket;
- whether candidate states are already materialized;
- memory-pressure flag;
- moderate-imbalance signal;
- whether gap filtering is a measured bottleneck;
- whether Pisano metadata is already available.

This is intentionally modest.  The goal is not to fit a complex learned model
online.  It is to keep enough empirical separation to notice facts such as:

> shortcut X is negative globally but positive for 8192--32767-bit long streams.

The cost unit is caller-defined but must be consistent inside one ledger
(microseconds, expensive root calls, transported states, etc.).

### Adaptive reordering after enough local evidence

`adaptive_trial_plan()` keeps the static cheap-first order until a shortcut has
at least a configurable minimum number of observations in the current regime
(default `5`).

After that:

- positive empirical net-saving shortcuts move earlier;
- negative empirical net-saving shortcuts move later;
- undersampled shortcuts retain their original exploration order.

This is intentionally conservative.  One lucky hit cannot immediately rewrite
the route, but repeated local benefit can.

## 6. Trial-plan policy

`opportunistic_trial_plan(context)` is cheap-first:

- structural priority and learned prefix are generally tried;
- kernel13 is added for longer multiplier horizons;
- gap sorting appears only if states already exist;
- ratio cover appears only under its specialist signal;
- table-free appears under memory pressure;
- quotient and energy jets appear after their finite observed crossover regimes;
- LOW12 appears only when filtering is hot;
- residue jet appears only for ultra-large long streams;
- Pisano metadata probe jumps to the front only when its setup cost is already
  sunk.

This is an **execution policy**, not a theorem of optimal expected ordering.
The ledger is designed so future data can reorder these probes.

## 7. What remains deliberately excluded

Some past ideas are not even useful as cheap specialists:

- simple BRC support/Pell-phase selector for factor success;
- low-cost N/J/R shadow classifier whose held-out gain vanished;
- reciprocal-table/Newton replacement of the native linear division in CPython;
- fixed comparison trees and allocation micro-optimizations that did not show
  stable cross-size gain.

They remain in research history but are not in the active opportunity portfolio
unless a new execution environment materially changes their cost model.

## 8. Decision

Register:

`t0.brc_opportunistic_shortcut_portfolio`

as a `T0_BRC` global subtool with status:

`RESEARCH_TOOLIZED_HEURISTIC_PORTFOLIO_WITH_EXACT_FALLBACK`.

It does not promote any heuristic to Working Truth or Foundation.  Its purpose
is exactly the opposite: preserve useful non-universal experiments without
mislabeling them as global laws.

The long-term criterion for keeping an opportunistic shortcut is expected value,
not universal win rate:

`cheap probe + exact fallback + positive local empirical net value -> retain`.
