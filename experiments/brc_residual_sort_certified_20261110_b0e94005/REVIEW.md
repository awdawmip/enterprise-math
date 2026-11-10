# Author-side review of fixed-grid feasibility repair

## Scope and review status

The kernel, harness and mathematical note were developed by collaborating
agents in the same project context and workspace, with the parent integrating
the experiment. The mathematical reviewer authored THEORY.md and then read the
completed kernel, generator, checking code and execution receipts. This is
author-side multi-agent review. It is not external independent peer review,
proof-assistant verification, a novelty determination or a project theorem
promotion.

The first part of this record covers the source/proof audit and executed
optimized and sanitizer verification. It was written while the frozen timing
run was in progress. The final sections record the subsequently completed
raw-result and report audit. This reviewer performed only source/receipt
reading, proof review, document writing and messages during the timing window;
numerical reconciliation began after completion was signaled.

## Executed verification evidence

`execution_optimized_verify_v1.json` and `execution_sanitized_verify.json` both
record successful verification of the final source, with the same coverage:

- 740 input cases: 341 exhaustive short arrays, 340 lifted arrays, 32 random
  boundary arrays and 27 focused cases.
- 1,734 checked algorithm outputs. Of these, 1,472 are the new candidate's
  diagnostic and nullptr outputs on 736 inputs, 208 are the 26 frozen controls
  on four control-only cases through both paths, and 54 are extra phase-three
  combined-selector reference outputs. The total 740 includes those four
  control-only cases; it should not be described as 740 new-candidate inputs.
- 47 applicable cases comparing decisions and output work with the phase-three
  combined selector when no singleton or DP repair was accepted.
- 337 fixed-grid repair fixtures with explicit subset enumeration, comparison
  to a separate full-row DP and selected-mask reconstruction checks. These
  fixtures satisfy the helper's entry condition: an over-budget grid whose
  inherited greedy proposal failed the original-sample half-mass gate.
- All four repair outcomes exercised: singleton acceptance, fractional
  rejection, DP acceptance and DP rejection; 16 complete sorter paths.
- All-node actual-membership checks, exact-half/half-plus-one cases, a DP
  repair below the root, forced-depth fallback, failed-layout nonmutation and
  truthful preservation of the preceding greedy proposal diagnostics.
- No fresh phase-four heldout bank generated or evaluated by verification.

The optimized verification uses GCC 14.2.0, C++20, `-O3 -DNDEBUG -march=native`
with warnings enabled. The other build uses `-O1 -g`, AddressSanitizer and
UndefinedBehaviorSanitizer. `ASAN_OPTIONS=detect_leaks=0` excludes leak checking
from its executed scope. Both recorded compiler runs have only the inherited
warning from the unused renamed historical main.

Both receipts record 15 successful frozen-dependency checks. Their recorded
kernel hash is
`47629f6640aeb0e99e53e22c81c0865a741e951d60875711e5c89ebc1343c959`,
and harness hash is
`d5466c4d5c418d23323d3b2f6c92b210a9221ca9f4c9297e71adbb2e08218303`.
The optimized binary hash is
`37ca2132ca6360ba3f16f088bdb0dcb89e7eab1b452e2175a09c43475f6efb00`.
This reviewer consumed the existing receipts and did not rerun either build or
verification.

## Fixed-grid theorem versus implementation

The reviewed `certified_kernels.hpp` implements the cascade in THEORY.md. No
substantive disagreement was found between the stated fixed-grid theorem and
the final source.

The unchanged compact, whole-grid and successful density-greedy paths return
before repair. A failed greedy proposal leaves the original layout intact.
Repair ignores bins of zero width or zero sample mass and bins whose width
exceeds the counter budget; no feasible whole-bin solution can require such an
over-budget bin. Production positive-width bins have positive learning mass.
The mass threshold is computed from `layout.sample.size()`, which retains the
complete original sample even after a gap window shrinks.

The best singleton is chosen by maximum mass, then minimum width, then minimum
original bin index. A passing singleton is a feasible witness. It is not
claimed to be a maximum-mass subset. The same distinction applies to an early
successful density proposal.

For the remaining individually feasible bins, exact integer cross products
give the density order. The fractional prefix stops at the first nonfitting
bin and adds at most its fitting fraction. Excluding individually infeasible
bins before this relaxation is valid, because their retain variables are zero
in every integral solution. The floor is an upper bound on every integral
sample mass for this particular grid. A floor below the original-sample
threshold is therefore a negative feasibility certificate, not a prediction
about the actual input population.

The mass-index DP maintains the minimum width of each exact sample mass. Its
descending update reads the preceding item's smaller-mass state, so a bin
cannot be selected twice. The source skips unreachable predecessor states and
only stores a candidate smaller than the current entry. Since every entry is
at most the sentinel C+1, candidates above C are never stored as reachable;
this implements the proof's saturated recurrence without an explicit minimum
expression.

Each item has its own initially zero take-bit row. A bit is set only for a
strict width improvement, while width ties keep the previous-row skip choice.
Reverse item traversal therefore follows historical DP identities and reaches
mass zero. This avoids the invalidity that can arise from reusing a mutable
single-row predecessor chain. The chosen largest reachable mass is the exact
maximum feasible mass, and its stored width is minimal among subsets with that
mass. This stronger optimum statement applies only when DP actually runs.

With budget at most 2^22 and positive sample mass at most 1024, the 32-bit width
entries and sentinel are safe. A candidate formed from a reachable predecessor
and one eligible width is at most 2C. The fractional numerator and density
cross products use 128-bit intermediates. Zero-mass bins are excluded before
the unsigned descending loop, and D[0]=0 guarantees the final reachable-mass
search terminates. The packed row allocation covers masses zero through the
feasible-mass sum, including the 1024 boundary.

Rejected fractional or DP proposals do not change bin widths, lower endpoints,
sample counts or total layout cells. Accepted proposals only omit complete
bins and preserve the retained intervals. The theorem is thus a complete
decision procedure for existence of a budget-feasible half-sample subset of
each fixed learned grid. It does not optimize all possible grids, interval
splittings, gap sequences, actual population mass or running time.

## Exact population and output checks

The first feasible representation still receives one actual membership scan.
A scan stops on the floor(n/2)+1-th residual and sorts the intact original
input by the inherited fallback; it does not retry another learned model or
recurse on an oversized residual. Accepted recursive calls therefore retain
the actual half-size contraction, separately from sample feasibility.

The harness reconstructs each chosen model and the actual input at every
recursive node. Its membership check uses explicit lower and upper interval
comparisons, rebuilds the processed prefix and residual sequence, and checks
the exact child input. Thus a rejected prefix is not mistaken for a complete
population scan. The full output of each checked path is compared element by
element with `std::sort`, preserving both numeric order and multiplicity.

Retaining complete bins preserves the previously proved disjoint ordered
interval invariant. The inherited fused emitter remains valid: residuals lie
outside all retained intervals, and accepted nodes write exactly n final value
elements. The source and harness keep those direct output writes separate
from semantic histogram-emitted occurrences, child work and fallback work.
No associated-record stability or original-position observer is part of this
numeric interface.

The harness's separate full-row DP uses immutable preceding rows, 64-bit width
costs and row comparison for reconstruction. It avoids the kernel's in-place
updates and packed take bits. The small-fixture subset enumeration adds a
different exact oracle for feasibility, fractional bounds, maximum mass and
minimum width. These are distinct computational checking implementations
within the author team, not external independent review.

## Constructive witness and generator audit

The final mechanism generator agrees with the proof's endpoint prescription.
For odd sample masses, the extra observation goes to the high endpoint:
307 observations split as 153 low and 154 high. Its complete initial population
uses consecutive modular cycling with a bank-dependent additive offset, so
the proof's at-most-two-occurrences-per-value bound does not rely on a hidden
coprimality assumption. The bank translation is a multiple of 2^36, preserving
the required coarse-cell alignment.

For the DP witness, the source fixes sample masses 410/307/307, raw spans
29711/24680/24680 and coarse-cell positions 0/256/512 at shift 16. These yield
padded widths 30000/25000/25000, total demand 80000 and budget 50000. Greedy and
the best singleton retain 410; the fractional upper floor is 655; DP selects
the latter two bins with mass 614 and width 50000. The executed mechanism
assertions check these quantities on banks zero and one.

The complete pre-overwrite population is 40%/30%/30%, and at most 1024 sample
positions are then prescribed. Thus retaining the latter two raw intervals
leaves at most 41024 actual residuals. The executed check requires a positive
recursive child within that bound. The read-only proof audit also confirms
the preceding gap selector's distinguishing route: it first retains A+B,
then A's high endpoint and B, and learns only 43 endpoint slots whose actual
coverage is at most 1078 in this constructed population. That route must fail
the actual half gate.

The hidden-majority mechanism preserves the same prescribed sample but fills
all nonsampled positions with a value in A. It therefore selects the same
DP-certified sample model yet reaches 50001 actual residuals, takes fallback
and creates no child. The executed assertions explicitly check this separation.

The singleton mechanism checks acceptance of mass 1000 at width 50000 with no
fractional or DP work. The fractional mechanism checks upper floor 342 and
fixed-grid rejection before DP. These are deliberately prescribed-sample
mechanisms, not natural-sampling workload estimates.

## Freeze and measurement boundary

`frozen_manifest.json` records `2026-11-10T09:41:06.516851+00:00` before fresh
input generation and performance started. It freezes the source, generator,
analysis, design, theory, verification receipts and optimized binary. The
experiment adds one fixed candidate to all 26 preceding candidates; it does
not choose among newly tuned variants after seeing the results.

The planned single serial run contains ten exactly reused phase-three
conditions labeled calibration, six fresh targeted families and four separate
mechanism conditions. The reused density witness is among the known calibration
conditions. Fresh families allocate exact group populations, generate random
values within intervals and shuffle before taking the ordinary deterministic
position sample; their sample locations are not overwritten.

The recorded design uses the same current AMD EPYC 9V74 / GCC 14.2.0 environment
for all 27 candidates, CPU 0, eight banks and seven randomized-order rounds per
condition. Copying, learning, selection, allocations, complete output and
destruction are included. Diagnostic checks run outside the timed path. The
fastest preceding candidate per condition is a retrospective reference, not
an implemented automatic selector. The six fresh distributions are motivated
by the selection failure, so their condition-weighted aggregate is not an
estimate for arbitrary deployment data.

The exact repair has real work: another eligible-bin collection and density
ordering, the fractional scan, and sometimes O(B*S) DP and reconstruction.
Logical vector capacities and repair peak auxiliary bytes are not process RSS.
An exact sample-feasibility decision can improve coverage, fail the real
population gate, or cost more than proceeding directly to another sort.
Measured outcomes must remain separate from the selection capability theorem.

## Completed raw-result and report audit

`execution_all_frozen.json` records a successful run beginning at
`2026-11-10T09:41:07.074345+00:00` and lasting 293.87005971200006 seconds. The
optimized binary hash agrees with the verification receipts and freeze
manifest. The completed run contains 20 conditions, 540 algorithm rows, 160
input banks and 8,640 complete algorithm-output checks. The source/receipt
review found the freeze and verification boundary preserved.

After execution, a separate read-only calculation reconciled the raw data
with `analysis_summary.json`, `analysis_table.md` and README.md:

- Every condition contains the same 27 candidates, including the 26 preceding
  controls. The condition partition is exactly ten known calibration, six
  fresh targeted and four mechanism conditions. Each row has eight banks,
  seven rounds and eight-byte values.
- All 2,700 timing summary fields were recomputed from the seven individual
  rounds. For sorted rounds z0 through z6, median=z3,
  p10=0.4*z0+0.6*z1 and p90=0.6*z5+0.4*z6. The maximum discrepancy was
  1.4551915228366852e-11 microseconds, below the 1e-6 microsecond audit
  tolerance. Minimum and maximum fields also agree.
- All 20 condition records, fastest-old-control choices, ratios, stage counts,
  median ratios, geometric means and extrema agree with the raw medians.
  Geometric means were recomputed by a product raised to 1/k, separately from
  the analyzer's mean-log expression.
- All 2,761 node records, 315 certified repair records and 3,888 preceding
  selection-proposal records agree with the run receipt. The new candidate's
  292 nodes include exactly 160 roots. Its root/node path counts and repair
  method counts agree with the analyzer.
- 440 additional diagnostic comparisons recomputed the new candidate's
  per-condition node and repair aggregates from the detailed traces. They
  cover recursive input, sampling, processed values, residuals, allocated
  cells, output writes, actual-half failures, certificate outcomes, DP state
  visits and per-bank peak repair capacities.
- All 20 rows in the generated full Markdown condition table agree with the
  raw data. README.md's 20 timing rows, ten workload rows and three stage
  aggregate rows also match, including their displayed rounding.

The actual maximum recorded repair work-vector capacity is 12,364 bytes.
There are 81 DP attempts in the separate diagnostic calls: 41 accept the sample
gate and 40 reject it exactly. The other repair records comprise 226 fractional
rejections and eight singleton acceptances. These counts refer to diagnostic
executions, not all repeated timed calls. The completed run records 111
applicable no-accepted-repair parity cases, separately from the 47 pre-freeze
verification cases.

No compilation, benchmark or optional sorter retest was performed for this
audit. The trace reconciliation checks reporting consistency; the actual
membership and complete-output checks are the executed harness evidence.

## Bounded performance interpretation

The exact capability repair did not establish a faster sorter on the six fresh
targeted families. Relative to the fastest of 26 preceding controls, the new
candidate wins zero of six medians; all six are at least 10% slower. The
geometric mean of control time divided by new time is 0.551458819. Relative to
the preceding phase-three combined selector, it wins three of six medians,
has no improvement of at least 1.10 times, and has geometric mean ratio
0.980999719. The million-element condition is at least 10% slower than that
preceding selector.

| Fresh condition | Previous combined / certified | Fastest preceding control / certified |
|---|---:|---:|
| Three bins, 40/30/30 | 1.046144 | 0.492396 |
| Same proportions, shifted intervals | 0.979264 | 0.487578 |
| Three bins, 20/40/40 | 1.012305 | 0.678515 |
| Three bins, 44/28/28 | 1.013467 | 0.499389 |
| Eight-bin family | 0.939844 | 0.655542 |
| Three bins, one million values | 0.902289 | 0.527377 |

The known ten-condition geometric mean ratio is 0.976605276 against the
preceding combined selector and 0.898360692 against the fastest preceding
control. The four mechanism conditions have corresponding ratios 0.966858794
and 0.579849774. Neither set should be merged into the fresh six-condition
aggregate or presented as additional fresh workload evidence.

### Root repair succeeds while residual children still fail

The detailed node traces materially qualify the aggregate
`actual_spill_failures` field, which sums failures throughout a sort. A value
of one does not imply the root rejected its DP-selected model.

In the balanced fresh family, seven of eight roots use DP and the remaining
root uses the inherited successful density path. All eight root scans pass,
leaving mean residual size 40,000.875. Each of the eight child nodes then takes
an actual-half fallback. Those child whole grids fit the counter budget and
retain all 1,024 sampled observations, with mean 12,683.375 counter cells, so
the repair is never entered there. Their actual populations nevertheless
produce more than half residuals. This is downstream sample-to-population
coverage failure, not incompleteness of the fixed-grid half-sample decision.

The 44/28/28 family has DP acceptance and successful actual scans at all eight
roots, leaving exactly 44,000 residuals each. All eight child models again
retain all 1,024 samples and fit the budget, with mean 12,584.25 counter cells;
all eight child scans then fail the actual-half test.

The million-value family likewise accepts DP at every root, with mean root
residual 400,205. All eight child nodes reject their actual populations: seven
use an original fitting grid and one uses a later gap grid. The mean child
processed prefix is 357,085.625 values. Mean total recursive input is
1,400,205, selected-model processed values are 1,357,085.625, allocated counter
cells across nodes are 627,658.5, and successful counting-node output writes
are 1,000,000. Root DP visits only 1,146.5 state-loop entries on average in this
three-bin case. These operation counts show substantial scanning, counter and
output work remaining after a small exact selection problem is solved. They
do not provide an elapsed-time breakdown or prove which component consumes a
particular fraction of runtime; radix fallback's internal passes are separate
from the selected-model processed-value count.

### Rejection work and unchanged paths

The shifted three-bin family has only two root DP acceptances. Its traces
contain 13 root DP rejections, plus six child fractional rejections. Some
rebuilt grids really have no feasible half-sample subset; a fractional upper
bound above the gate does not promise that DP will find one.

The eight-bin family has 27 DP rejections and no DP or singleton acceptance
across its eight banks. Its original selection decisions and output work
match the preceding policy, while the exact certificate machinery adds mean
8,754.125 DP state-loop visits per sort. Its 1,086.307 microsecond median
exceeds the preceding selector's 1,020.959. Certification work without a changed
representation is a concrete cost risk, although this experiment does not
isolate the timing of each added operation.

The 20/40/40 family invokes no exact repair at any node. Both policies select
the same density root and retain the same 20,000 residuals, and both have
actual-half failure at the child. Its small median difference must not be
credited to a DP improvement that did not run. More generally, differences on
unchanged decision paths can reflect code-generation/layout and measurement
effects; seven within-process rounds are not a causal timing decomposition.

### Constructive success is not a performance promise

The prescribed DP witness behaves as proved: every root selects mass 614 and
50,000 cells, and its actual residual is 40,000. The preceding selector rejects
at 50,001 residuals. Yet the new sort takes 784.365 microseconds versus the
preceding selector's 704.591 and offset radix's 603.660. Its successful root
opens a residual computation whose mean recursive input total is 168,076.375
and selected-model processed total is 166,807.125, with a later actual-half
failure. The new representation capability is real, but does not justify
claiming that pursuing it is faster than an earlier fallback.

The hidden-majority mechanism gives the complementary boundary: it also
selects the DP-optimal sample model at every root, then rejects at 50,001
actual residuals without a child. Sample optimality, population acceptance and
time benefit remain three different propositions.

The report's numerical tables and bounded headline are supported. Its wording
about the two new-candidate output paths was corrected to identify the
diagnostic path and the nullptr timing path. The reviewer confirmed the
updated wording. No consequential mathematical, implementation or numerical
defect was found in this completed audit.

The resulting research conclusion is a correct finite selection repair with a
negative broad speed result on these fresh targeted families, plus a concrete
remaining failure pattern in child population coverage. It does not overturn
the earlier phase-three improvements, does not establish deployment-wide
performance, and does not change the sorting family's general fixed-word
complexity class.
