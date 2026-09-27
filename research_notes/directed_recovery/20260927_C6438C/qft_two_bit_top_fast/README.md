# Highest-bit scalar correlation: singleton path and setup reuse

The single declared native run and complete author/shared-context peer
saved-record reviews pass. On the fixed six-input grid, production digit
replays fall from 96,452 to 26,596. Four cases now cost less than the historical
typed pair comparator; two still cost more. This is a measured arithmetic
counter improvement for a scalar component, not a whole-Shor speedup.

The source `top_bit_fast.py` implements the unchanged domain `g >= 2`,
`0 <= ell < k = g-1`, positive supplied `R`, canonical `r`, stride one, with
schema `BRC_TOP_BIT_POINT_AND_SETUP_REUSE_V1` and raw normalization `4^-g`.
It retains both displacement orientations and signed answers. It neither
discovers an order nor assumes a new phase/common-root identity.

The implementation builds typed scales once per `(g, ell)` observer key,
creates piece coefficients only when needed, evaluates singleton segments by
an actual typed point formula, and retains the earlier exact floor-moment
route for longer segments. A cache hit references completed prior evidence;
it does not fabricate a second receipt or hide first-use work.

## Actual bounded result

| `(g, ell, k, R)` | New production digits | Previous production | Historical typed pair comparator |
|---|---:|---:|---:|
| `(2,0,1,3)` | 715 | 5,640 | 456 |
| `(3,1,2,3)` | 4,790 | 9,827 | 2,241 |
| `(3,1,2,5)` | 1,901 | 12,549 | 2,547 |
| `(4,2,3,6)` | 11,254 | 22,915 | 12,472 |
| `(4,2,3,9)` | 5,210 | 28,293 | 13,995 |
| `(3,1,2,11)` | 2,726 | 17,228 | 2,833 |
| Total | **26,596** | **96,452** | **34,544** |

All 37 main values exactly match the complete source-bound predecessor raw.
The historical 720 ordered-pair records were fully read, not executed again.
Four extra mixed-cache control queries and their fresh replay are separate
from this grid. They test switching to another setup, returning to the first,
and reuse across moduli; same-g/different-ell keys remain unexecuted coverage.

The main production has 30 empty, 94 singleton and ten moment segments,
20 top-level moment tables instead of 208, six setup constructions, 31 setup
hits and four lazy coefficient constructions. Both singleton pieces/parities,
nonzero remainders, negative outputs and half-modulus multiplicity are present.

All 28 current paid streams total **122,802 digit replays**: production 26,596,
positive replays 26,596, mixed-cache control and replay 4,464 each, paid
negative replay 60,682. One actual 12-state native core invocation supplies the
shared full-adder columns; subsequent digit work remains charged. Twelve
invalid inputs and four early tamper cases add no arithmetic. Thirteen full
paid tamper replays and one paid-valid-prefix input rejection are retained.

The production reduction is about 72.43% versus the predecessor and 23.01%
versus the aggregate historical comparator. Those are fixed-grid counter
comparisons. The 20.5260481-second record includes historical loading and all
controls/replays, stops before serialization, and is not a matched timing
benchmark. Host metadata/serialization costs are not fully instrumented.

## Evidence, restoration and limits

The actual original gzip is 1,258,273 bytes, SHA-256
`7cea2d841376650734622fe7d29b529a8f46cd195a4dc87b63993d9e995fc507`.
Decoded raw is 33,060,129 bytes, SHA-256
`db60ed6dd188c5936585c0d1a4dbffa83652baca0dd2551182148d2c8457038a`.
It retains complete current signed/typed streams, moment/cache records,
positive and failed replay work, and native CALLS. Lossless source chunks
restore the exact gzip; the delivery ZIP contains that original. Full
dependencies and historical raw locators are in DEPENDENCIES.md.

Source, proof and checker headers retain their pre-execution wording; the
actual guard/run/raw and EXECUTION_NOTE.md establish the subsequent execution
without changing those source bytes. Author and peer saved-record review do
not constitute formal independent admission.

This does not close unknown-order/address discovery, general non-top mixed
moments, matrix correlations with noncommuting words, general-history sampling,
or complete Shor dequantization. The copied `next_design` degree-five proof,
runner and two reviews are frozen source-only work, not executed by this unit.
They close a single-floor moment family symbolically, not products of two
independent floors. The separately reviewed mixed-threshold proof/review pair
is also copied: it reduces the particular mixed sum to a precise remaining
interface but does not prove a terminating general evaluator. No successor
checker or draft experimental result is included.

The additional reviewed adjacent-shift proof pair gives a narrower positive
continuation: adjacent selected bits, including non-top positions, reduce to
a shifted single-bit sum plus a finite-boundary correction for arbitrary
supplied R. It needs at most eight existing degree-three top-level tables per
query and no degree-five backend. Only its proof and review are copied; this
package contains no execution, cost or API claim for that extension.

Global-Knowledge-Sync: main@106dd75 / GLOBAL_KNOWLEDGE_V1 (coordinator's actual
canonical read and helper lease; startup observation remains unchanged).
