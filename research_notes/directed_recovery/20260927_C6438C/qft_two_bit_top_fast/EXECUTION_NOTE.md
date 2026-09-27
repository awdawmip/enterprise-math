# Actual point-path and setup-reuse execution

The one declared bounded native run passed. Its 37 main values equal the
previous top-general values; four additional mixed-cache queries also passed.
This note is grounded in the complete saved raw, not just the summary. The
author reader and the separate shared-context peer reader have both checked
all 28 current charged streams. Neither reader imports the scientific
executor or recomputes its arithmetic answers. This is author evidence and
shared-context cross-checking, not formal independent admission.

## Fixed source and evidence

| Item | SHA-256 |
|---|---|
| `top_bit_fast.py` | `8c73aa1ad2f195b9d8f440112dac7b08cacbc1e544e65850a754dc38f2fa48e8` |
| `check_top_bit_fast.py` | `76dc68753c07e9eedd64183c4a2875fde709ef6f1f0f59dd32b6ce39eee8dc21` |
| `DESIGN.md` | `87e0d3416e24030a6e76f9b418d9cdb1aa9ffba9175e63fbff4ce622521ed275` |
| `POINT_AND_SETUP_REUSE.md` | `e4c0f33e1fd6c8d62d3604eb37db41b937ba999e536b61cfeac6e1300c9690e6` |
| Actual `STARTUP_GUARD.json` | `f8ff9c3877cfc3dd22ad91bbc05a3927105769a60ac541b74ffe31bcc77647ae` |
| Original gzip, 1,258,273 bytes | `7cea2d841376650734622fe7d29b529a8f46cd195a4dc87b63993d9e995fc507` |
| Decoded raw, 33,060,129 bytes | `db60ed6dd188c5936585c0d1a4dbffa83652baca0dd2551182148d2c8457038a` |
| `read_top_fast_cost.py` | `3513008ffc95b1d135b8dcc5b70bca341c10f4f5171ae2e6e80a48373a8ce9d2` |
| `TOP_FAST_COST_READBACK.json` | `b8b83cb5a7f6a862931bbb3cfc376371f0adfbb56b13cc522503d84feb6a437b` |

The saved pre-execution design/proof remains unchanged; its code-only status
describes preparation time. This note records the subsequent actual run.
The reader pins and loads only the predecessor's stdlib I/O helper
`read_top_general_cost.py`, SHA
`a96696eb187d6c6251934f9b1651f5abc1b8d2db5a5357ea051960b8e4489f5a`.
The record contains all actual source, proof, native-catalog and helper hashes.

## What changed and what was checked

The contract remains a two-selected-bit signed scalar autocorrelation with
`g >= 2`, `0 <= ell < k = g-1`, a supplied positive modulus `R`, canonical
residue and unit stride. The new schema is
`BRC_TOP_BIT_POINT_AND_SETUP_REUSE_V1`. It does not infer a Shor order.

Each observer constructs the typed scale data once per `(g, ell)` key.
Subsequent residues or moduli reuse that completed entry. Piece polynomial
coefficients are created lazily only when a segment has at least two points.
An empty segment has an actual typed zero. A singleton uses typed quotient,
remainder and parity followed by its signed overlap expression, without
constructing moment tables. Longer segments retain the predecessor's exact
floor-moment route and division-by-three check. No ordinary numeric reference
was substituted for any of these executed scalar calculations.

The six main fixtures contain 134 segments: 30 empty, 94 singletons and ten
moment segments. They issue 20 top-level moment tables, versus 208 before.
There are six setup constructions, 31 setup hits and four lazy coefficient
constructions. Both singleton pieces and parities, nonzero remainders,
negative values and half-modulus orientation multiplicity are present.

The separate four-query mixed control returns `[6,6,-3,6]`, with setup
indices `[0,1,0,0]` and hit flags `[false,false,true,true]`. It tests return to
an earlier key and reuse across `R` for a fixed key. Its complete fresh replay
is paid separately. Same-`g`/different-`ell` cache keys were not exercised in
this bounded run and are not presented as tested coverage.

The full-record reader follows each request's setup index and every lazy
coefficient reference chronologically. Hits must refer to previously complete
entries. It checks all signed-to-typed output links and every retained adder
cell against the actual eight-column native catalog. The moment I/O cursor
checks node, child, cache and range references. No saved setup, coefficient or
typed operation is silently detached from the executed request stream.

## Complete cost accounting

| Current-run category | Streams | Adder digit replays | Typed operations | Signed operations |
|---|---:|---:|---:|---:|
| Main production | 6 | 26,596 | 4,855 | 4,615 |
| Main positive fresh replay | 6 | 26,596 | 4,855 | 4,615 |
| Mixed cache control | 1 | 4,464 | 1,115 | 1,085 |
| Mixed cache fresh replay | 1 | 4,464 | 1,115 | 1,085 |
| Paid negative replay | 14 | 60,682 | 13,128 | 12,699 |
| Total | 28 | 122,802 | 25,068 | 24,099 |

The same complete streams contain 118 moment nodes, 198 moment requests,
80 moment-cache hits, 1,319,820 counted host bit-wiring operations and 69,970
arithmetic bit-length calls. There is one actual native core invocation:
`recurrent_mass_power`, depth one, 12 positive states, for the shared full-adder
catalog. The first production stream owns this call; all later streams reuse
the catalog. One core call does not make the 122,802 digit replays free.

Production hotspots are disjoint partitions of the saved typed records:

| Work | Digit replays |
|---|---:|
| Scale setup | 246 |
| Lazy low/high coefficients | 993 |
| Empty segments | 60 |
| Singleton segments | 6,093 |
| Moment-segment outer expressions | 5,275 |
| Actual moment-table internals | 5,624 |
| Routing and final expressions | 8,305 |
| Total | 26,596 |

This split charges coefficient construction separately from the first segment
that triggers it. A cache hit incurs its recorded lookup/routing work but no
second arithmetic construction. It is a record-level cost decomposition,
not a measurement of per-component wall time or all Python bit complexity.

## Same-input historical comparison

| `(g, ell, k, R)` | New production | Old top-general production | Historical typed pair comparator |
|---|---:|---:|---:|
| `(2,0,1,3)` | 715 | 5,640 | 456 |
| `(3,1,2,3)` | 4,790 | 9,827 | 2,241 |
| `(3,1,2,5)` | 1,901 | 12,549 | 2,547 |
| `(4,2,3,6)` | 11,254 | 22,915 | 12,472 |
| `(4,2,3,9)` | 5,210 | 28,293 | 13,995 |
| `(3,1,2,11)` | 2,726 | 17,228 | 2,833 |
| Total | 26,596 | 96,452 | 34,544 |

For this grid, production digit work is about 72.43% below the predecessor,
and every case improves. Its aggregate is about 23.01% below the historical
typed comparator; four cases beat that comparator and the first two do not.
This is not a uniform input-family advantage.

The predecessor's complete 75,217,873-byte raw was read and hash-checked. Its
720 retained typed ordered-pair records were inspected, not executed again.
Their 34,544 digits and the old production/replay costs are historical
comparators, excluded from the current 122,802 total. The four mixed-cache
queries are additional controls, not part of the 37-value grid.

The current elapsed record is 20.52604810008779 seconds before final
serialization. It includes loading historical evidence, controls and fresh
replays. This is not a matched timing benchmark. JSON, hashing, dictionary
maintenance, serialization and uninstrumented host work are not all covered
by the arithmetic counters, so the measured counter decrease is not relabeled
as a whole-program wall-clock speedup.

## Rejection, partial evidence and remaining boundaries

All 12 ordinary invalid inputs reject with zero work. All 18 tamper controls
reject: 13 perform and retain a complete honest fresh replay before mismatch
rejection, four reject before arithmetic, and one retains a valid paid first
request before rejecting a non-top second input. The latter records 1,784
digits and `inflight=None`; it is a rejected input after a valid prefix, not
an interrupted numeric transaction. Every paid negative stream is included
in the totals above.

During the first main production observer, the inserted invalid non-top input
has equal detached before/after snapshots and no added work. The observer then
completes its original request grid. Those snapshots overlap production and
are not billed a second time. A deliberately interrupted valid numerical
request was not run; the incomplete-cache guard is source-reviewed rather
than claimed as an exercised recovery scenario.

Fresh replay compares the complete schema and source-bound evidence after
excluding only the declared native primitive cache-call delta. No unexpected
failure artifact exists. The exclusive-output and available-object failure
capture are retained in the checker; this successful run does not prove all
possible constructor or mid-arithmetic failures have been exercised.

The result preserves signed values and raw normalization `4^-g`. It is a
supplied-modulus scalar unit; non-top mixed moments, paid unknown-order
discovery, full noncommuting carrier correlations, general-history sampling
and complete Shor dequantization remain outside this execution. A direct next
step is to use the measured routing/moment hotspots to choose one separately
proved optimization, with new source binding and same-input complete costs.
