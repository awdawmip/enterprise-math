# Adjacent selected-bit scalar observer: actual bounded execution

Status: ACTUAL BOUNDED PASS / AUTHOR SHARED-CONTEXT EVIDENCE / NOT FORMAL
ADMISSION. This note describes the single completed checker run and a separate
standard-library readback of its saved records. It does not replace the frozen
pre-execution status in the design or the symbolic proof with an earlier-run
claim. No scientific experiment was repeated during this readback.

The executable domain now includes two adjacent selected bits strictly below
the top bit, with arbitrary supplied positive modulus R. The tested observer
uses the frozen one-bit progression plus its shifted-window correction. It
does not use the later point/setup shortcuts or the degree-five extension.
The measured small cases establish correctness, not a cost advantage:
production used 126,950 full-adder digit replays against 52,700 for the actual
typed pair comparator on the same six inputs. Every case was more expensive.

## Frozen records and inspection

- `adjacent_shift.py`: `bee8a702062dfb16a75139a63b6c52b9451a02834a5b3033f5d52fcaebff9c6e`.
- `check_adjacent_shift.py`: `6a7969e779800652a6143354bcbe732b670cb90128781e2f1243db91d1e6a9fe`.
- `DESIGN.md`: `f5b85d9c7e2836259910ee9f25d16766a9a820521326c65693ff002480030cb2`.
- Original gzip: 3,547,684 bytes,
  `385295e9a5581ce762761f24d0d5c25e32f9bc06d645f32fbaecbdffd75b8294`.
- Decoded complete raw: 114,912,852 bytes,
  `a084a16fa26a9a2143729620ba3f2fdc1331579ae16087a5f3ddcce199a96d82`.
- Author reader `read_adjacent_cost.py`:
  `bef0ae5a25d3da29677a146e6209039f0aab927abd68a270fe14420d92a3e9bc`.
- Author record `ADJACENT_COST_READBACK.json`:
  `f8b4e67fdaa4d300680a38b0a02d6babc76b1a686f65c75d01d1c8fa0f34bd2c`.

The reader imports only the pinned standard-library saved-record helper
`../sep27-qft-two-bit-top-general/read_top_general_cost.py`, SHA256
`a96696eb187d6c6251934f9b1651f5abc1b8d2db5a5357ea051960b8e4489f5a`.
It never imports a scientific runner or recomputes a correlation using ordinary
arithmetic. Its cursor consumes saved operation outputs, verifies ordered
inputs and links, and reconciles all recorded signed operations with typed
output fields and native full-adder columns. It traverses every retained
digit cell, recounts charged work, binds floor-table records to their retained
nodes, and checks outer base/correction expressions in chronology. This is
full-record evidence inspection, not another native execution or a formal
proof of the implementation.

The original startup receipt, current source hashes, complete final summary,
and final JSON in `run.log` agree. The comparator's `typed_pair_histogram`
function is text-identical to the frozen aligned checker
`6777057a9468b673c7d58a657467c65ae1c37bd353fd55b9eb86a743efdaa969`;
its copied function text has SHA256
`c665b55053b03bb96a0411bd5fab39ae0f7d920ec08b1cf1ee0d62ac0b4f58e7`.
The old checker was neither imported nor executed. These are six new tuple
executions, not reuse or rerun of the old 720-pair highest-bit grid.

## Actual positive coverage

Each tuple `(g, ell, k, R)` tests every residue `0 <= r < R`. Each production
observer has one fresh complete serialized-certificate replay and one fresh
actual typed ordered-pair histogram.

| Tuple | Values | New ordered pairs | Production digits | Pair-comparator digits |
|---|---:|---:|---:|---:|
| (3, 0, 1, 5) | 5 | 64 | 12,622 | 2,533 |
| (4, 0, 1, 5) | 5 | 256 | 24,490 | 12,263 |
| (4, 1, 2, 6) | 6 | 256 | 26,651 | 12,552 |
| (4, 1, 2, 9) | 9 | 256 | 25,862 | 14,056 |
| (3, 0, 1, 11) | 11 | 64 | 13,898 | 2,844 |
| (4, 0, 1, 1) | 1 | 256 | 23,427 | 8,452 |
| Total | 37 | 1,152 | 126,950 | 52,700 |

All 37 signed outputs agree exactly with the new typed histograms. All six
cases have `k < g-1`; the tested domain includes ell zero and one, odd/even R,
R=1, R greater than the interval length, negative outputs, empty orientations,
and the two retained opposite orientations at a half-modulus residue.

There are 74 oriented progressions, 7 empty ones and 67 correction evaluations.
The 67 nonempty progressions each use two base and two correction tables,
yielding 268 top-level tables, at most eight per query. These are table calls,
not primitive operations: production retains 162 distinct moment nodes,
384 total moment requests and 222 cache hits. The maximum observed production
recursion depth is three and integer width is 14 bits. Those small bounds are
fixture observations, not asymptotic bounds for all inputs.

The algebraic implementation covers the adjacent top-bit subfamily as well,
but this grid deliberately tests the new non-top domain. It does not run a
separate top-bit fixture or establish a speed comparison there. No point-route
or cross-query setup-cache optimization is implemented in this version.

## Rejections, partial evidence and reuse

All twelve strict input controls reject before typed work. Following the
first valid production query, one invalid nonadjacent request rejects with
unchanged detached snapshots, no added typed or native work, `inflight=None`
and `failed=False`; the original remaining grid then completes on that same
observer. These before/after snapshots are overlapping production evidence
and are not billed as new executions.

Fourteen certificate tamper controls also reject:

- Nine retain a complete honest fresh replay before the semantic mismatch.
  They cover the base and correction coefficients, correction offset/table
  output/term, reused displacement sum, dropped half-modulus orientation,
  raw normalization and final signed output.
- One retains the valid first request before a later nonadjacent input
  rejects. Its 5,925 digit replays remain charged and saved. This is a
  verification attempt with a rejected next input, not an interrupted
  arithmetic request or a terminal failed observer.
- Four schema/source/type/key controls reject early without a replay stream.

The nine complete negative replays total 127,627 digits; adding the retained
prefix gives 133,552. The semantic comparison excludes only the declared
native-cache call delta. It retains all scientific values, signs, source
bindings, request order and cost-bearing records.

The checker did not inject a mid-arithmetic interruption. Source handling of
an exception after a valid request has started is therefore not reported as
an executed recovery test. No unexpected failed-execution artifact was
produced. Failure collection has the documented available-object boundary:
objects that did not finish construction cannot be reconstructed afterwards.

## Complete cost accounting

| Disjoint category | Streams | Digit replays | Typed operations | Signed operations |
|---|---:|---:|---:|---:|
| Production | 6 | 126,950 | 26,658 | 26,181 |
| New pair comparator | 6 | 52,700 | 5,380 | 3,968 |
| Positive fresh replay | 6 | 126,950 | 26,658 | 26,181 |
| Paid negative replay | 10 | 133,552 | 38,581 | 37,917 |
| Total | 28 | 440,152 | 97,277 | 94,247 |

The complete current run also records 4,749,667 host bit-wiring operations
and 275,334 bit-length calls inside typed arithmetic. These instrumented
counts do not cover every interpreter operation, allocation, hash, JSON step,
memory peak or host bit cost. Positive and negative replays are separate
costs, not independent statistical trials. The twelve input refusals and
four early certificate refusals add no scientific digit stream.

The disjoint native-call intervals reconcile to one actual core call:
`recurrent_mass_power`, 12 states, depth one, used to obtain the shared eight
full-adder columns. Later operations reuse the actual catalog. One core call
does not mean one arithmetic operation or free computation: the 440,152
recorded digit replays account for the composed arithmetic work.

Production hotspot partition, with no overlapping charges:

| Component | Digit replays |
|---|---:|
| Scales | 543 |
| Base coefficients | 5,698 |
| Correction coefficients | 489 |
| Base moment tables | 33,375 |
| Base outer expressions | 29,503 |
| Correction moment tables | 43,616 |
| Correction outer expressions | 12,184 |
| Empty base progressions | 224 |
| Routing and final additions | 1,318 |
| Total | 126,950 |

The recorded whole checker elapsed time before result serialization is
45.467766999965534 seconds. It includes production, comparisons, replays and
controls; it is not a matched single-query benchmark. There is no timing
speedup claim. The negative cost result is retained: all six production
totals exceed their same-input typed comparator totals.

## What this closes and what remains

This run validates the exact shifted single-bit construction for a bounded
new adjacent-bit grid, including the full correction and both orientations.
The accompanying symbolic fixed-degree recurrence gives a polynomial-bit
scalar route in the relevant bit length, but this small execution does not
demonstrate its large-input scaling. Supplied R and any group address remain
paid external information; no order or discrete logarithm is discovered.

The output is a signed scalar correlation normalized externally by `4^-g`.
It is not a full work-state simulation, a matrix-word contraction, a general
separated-bit observer, or a completed Shor dequantization. Arbitrary bit
gaps, growing masks, signed noncommuting chronology, address discovery and
total sampling cost remain open. A concrete next step is a separately
versioned point/setup reuse route on the same adjacent formula, with a
declared fresh test and complete charging; this note records no such result.
