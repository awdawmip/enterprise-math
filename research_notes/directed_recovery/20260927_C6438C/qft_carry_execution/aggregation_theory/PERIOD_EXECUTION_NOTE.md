# Bounded actual execution of whole-period aggregation

Status: AUTHOR_ACTUAL_NATIVE_BOUNDED / SHARED_CONTEXT / NOT_ADMITTED.
This extends the symbolic period aggregation note with a concrete executor.
It is a correlation-representation test, not an ideal-QFT experiment or a
new factoring implementation. No previous frozen scientific source changed.

## Result and exact scope

The declared first run completed all eight comparisons for N=21,a=2 and
N=65,a=3, t=4, fixed history (1,0,1,0), retained depths 3 and 4, and two
period addresses r=0,1. Every entry and the dyadic common denominator of
the returned matrix equal the sum of all independently discovered native
displacement coefficients. Every compared matrix has a nonzero entry in
a residual row or column (carrier index at least two).

The executable state dimension was six, admitted through the existing
actual full61 word replay and exact reachable-carrier codec. This is not a
new full61-versus-six numerical experiment, and no residual was deleted.
The source bank is the frozen direct-word integration bank, fully verified
by its existing importer. These t=4 fixtures are not the default-width,
strong-error-budget Shor factoring tests.

| Input | Depth | Actual first-return R | s | q | Aliases for each target |
| --- | ---: | ---: | ---: | ---: | ---: |
| 21, 2 | 3 | 3 | 0 | 3 | 5 |
| 21, 2 | 4 | 6 | 1 | 3 | 5 |
| 65, 3 | 3 | 6 | 1 | 3 | 3 |
| 65, 3 | 4 | 12 | 2 | 3 | 3 |

Thus the original eight-case run covers the no-low-block case and nonempty
low blocks, including negative/wrapped aliases. A separate subsequent
boundary unit, documented below and in `PERIOD_BOUNDARY_NOTE.md`, covers
q=1, s=i and s>i without changing this original evidence or executor source.
Neither unit is a general parameter sweep or a test of arbitrary zero-mass
histories.

## Actual interface and admission

`PeriodAggregator(program, history)` derives from the frozen CarryExecutor.
Its method is

    gamma_known_period(depth, r, R, *, target, period_certificate)

The returned object is the inherited immutable Correlation(rows, den).
R and r are explicit claims, not trusted order/discrete-log inputs.
`certify_period(program, depth, limit)` creates a fresh actual typed modular
table and walks from label one until the first return, or returns PARTIAL
after the declared limit. It retains every consecutive column and both the
inherited-table and fresh-table permutation replays. This implementation
pays O(R) discovery on success. It does not implement the symbolic
small-odd-part discovery or projected-address algorithm in the theorem.

Every positive aggregation query fully reruns that certificate through
`verify_period_certificate`, compares complete scientific evidence with only
process-dependent native cache-call deltas excluded, and checks the actual
cycle label at exponent r against target. It checks integer types (booleans
excluded), 0<=r<R, the depth, source and program binding, and exact R.
There is no free target-address or exact-order assumption.

The q-state transition routes are themselves obtained through the inherited
typed Arithmetic add/divide/modsubtract observers. Actual amplitudes use
only inherited `_left`, `_right_transpose`, `_combine`, `_seed` and `_zero`.
Each `_combine` performs the exact signed positive-path sum and already
includes the raw 1/4 factor for that layer. There is no extra final scaling,
ordinary-matrix propagator, ideal target propagation or word reordering.
Fresh immutable boundary entries avoid mutation through equal seed values.

The independent complete alias lists come from the sibling's typed bounded
alias discovery, with width three. The comparison then calls the parent's
actual `sum_coefficients` on those complete lists. It does not use host
modular exponentiation or provide a classical ideal quantum reference.

Eight negative controls rejected: boolean R, incorrect period multiple,
boolean r, r outside [0,R), target/r mismatch, wrong certificate depth,
tampered final-return evidence, and an incomplete period certificate.
The tampered-record rejection includes its actual full replay. The incomplete
discovery itself is also retained. There is no rejection-by-status-only
acceptance path for a successful query.

The certificate comparator is a scientific-content replay mechanism, not
a separately certified strict parser for arbitrary external JSON schemas.
The public scientific depth/R/r/target arguments have strict integer checks,
and the actual target is finally checked against the freshly replayed cycle.
The supplied program and its admitted Python methods are trusted and fixed;
this module does not claim protection against arbitrary runtime monkeypatching.

## Cost and what is actually reduced

The complete run retained 2,568 native kernel call receipts. The decompressed
scientific evidence is 5,780,769 bytes; its gzip is 301,357 bytes. Wall time
was about 4.82 seconds on this host, including admission and all checks.
These times are fixture observations, not an asymptotic statement.

| Four queries per input | Aggregation | Same-query alias sum |
| --- | ---: | ---: |
| N=21 native phase-vector applications | 672 | 1,266 |
| N=65 native phase-vector applications | 480 | 696 |
| Both inputs, signed observer operations | 544 | 1,780 |
| N=21 chronological high / low bit layers | 12 / 2 | 70 coefficient digits |
| N=65 chronological high / low bit layers | 8 / 6 | 42 coefficient digits |
| N=21 weighted high qH plus low s work units | 36 + 2 | 70 coefficient digits |
| N=65 weighted high qH plus low s work units | 24 + 6 | 42 coefficient digits |

There are 144+8 high/low transition terms for N=21 and 96+24 for N=65.
`high_layers` counts chronological bits, not qH matrix work units; the
latter is `high_transition_terms/4`. The corresponding low work units are
`low_transition_terms/4`.
The separate slot counters peak at 108 scalar slots for the q-residue
boundary and 72 for a carry boundary. These are logical boundary sizes,
not total peak memory. The implementation additionally retains current and
fresh accumulators, contribution matrices, column-action temporaries,
certificates, query records and observer transcripts. It does not promise
constant total memory or overwrite prior evidence.

The metadata accounting file separately counts 58,313 typed adder-digit
replays: program modular setup/columns/verification; four initial complete
cycle discoveries; eight positive query cycle replays; one failed-certificate
replay; one partial discovery; independent alias discovery; and all typed
aggregation index routing. Cycle evidence retains 14 distinct fresh table
instances and 85 requested cycle columns. Equal modulus/multiplier instances
are not merged out of this cost ledger. Native phase applications and
signed-observer work are counted separately rather than equated with these
integer digit operations.

Cached native primitives mean many typed digit replays add no new kernel
CALLS. Therefore the 544-versus-1,780 kernel-call deltas are not complete
running-cost counts. Each aggregation query still replays its cycle, and
the current implementation reconstructs high-state matrices for each target;
cross-target or cross-history reuse is not implemented or claimed.

This verifies an actual reduction relative to the separately evaluated
alias sums on these eight equal-target cases. It does not establish a
speed advantage over the old Gram sampler, explicit small-q rows, the
existing fair-suffix sampler, or an ordinary classical factor algorithm.
Those have different computations and must receive the same discovered
order information in any comparison.

## Separate boundary execution

The separately recorded nine-case run used the same unchanged executor.
It actually discovered R=2 for N=17,a=4,depth=3; R=8 for N=17,a=3,depth=3;
and R=24 for N=97,a=5,depth=2. These reach q=1 with a nonempty high block,
s=i, and s>i respectively. The final input additionally exercised the
negative sole displacement and the empty-alias zero matrix. All nine
complete matrices equal the independently discovered coefficient sums.
The run retained 377 kernel CALLS and its own full observer/typed evidence.
Its detailed scope and separate 85,419 typed-digit accounting are in
`PERIOD_BOUNDARY_NOTE.md` and `PERIOD_BOUNDARY_ACCOUNTING.json`.

## Frozen sources and evidence

- `period_aggregator.py`:
  `6f2c855bec09f7cf7fc4853b55ea41f94a195ba3d3b783d18921e9a3b6465f0c`.
- `check_period_aggregator.py`:
  `19308af165e5c979e679ae024494d5ba6ad52a3554882a409f718cb78e1eba16`.
- Parent `carry_executor.py`:
  `f017b1fb1516e8faa97afd39d663e4eda6d21cad95f65bb2ccf5a79d7ff3b810`.
- Inherited `lazy_modular.py`:
  `08df3595a2a56dc2501bb481828093481bf76e4ac53c8b966990d233fefac1e4`.
- `PERIOD_AGGREGATION_RESULTS.json.gz` decompressed payload:
  `2a7dae92955c8ad4c4ab5b91ee49936d30dd6587bbc4ba18b79e2d453533fef5`.

The checker compared these execution-source bindings before and after the
run. Alias records retain their own typed source bindings; the bank importer
retains its full-column source and error admission. The gzip contains the
complete native CALLS, signed observer records, arithmetic route traces,
period and alias discovery receipts, matrices and rejection evidence.
`summarize_period_resources.py` only reads that frozen gzip and counts stored
metadata; it does not run another scientific calculation.

This standalone module does not add a persistent aggregation cursor,
automatic factoring driver or production sampling policy. Incomplete period
discovery remains PARTIAL. A comparison against the old Gram baseline or a
different history family is not represented as done by these artifacts.

Global-Knowledge-Sync: main@06788df0 / GLOBAL_KNOWLEDGE_V1
