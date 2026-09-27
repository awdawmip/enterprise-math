# Shared-context review of the segmented-view matched benchmark

**PASS within the declared six-pair scope. No substantive discrepancy found.**
This review read the design, adapter, benchmark/checker and cost-extraction
sources, the execution note, and the complete 16,546,526-byte decompressed raw
record. It used only standard-library I/O, serialization, equality and recorded
cost/timing accounting. It did not import scientific modules, replay any native
arithmetic, rerun a prefix, or add a fixture. It is a separate shared-context
review, not formal independent mathematical admission.

## Exact inputs and reproducibility

- Benchmark: `66b61035dc3cb5650071b4aac5fd8ac21c3dd7d9a9c036e081b3292b2f15bea6`.
- Predeclared design: `3d0506db485480b1f743027d80e51304d88130b24e05842029c3a96a7558b25a`.
- Adapter: `90c773c74a81ed239e32fcc12fa8d238032d6fbcfef3f4d6eb2056856666ed99`.
- Raw payload: `461f1c84cafdee8b8d38ae9577f4d9a6472737d9f292aef9c7fdf606921fc80d`.
- Gzip: `2d19cac21d4f18f885b161d06bbf16e686b733a71c4cea95b140641eccd83ba3`, 733,837 bytes.
- Execution note reviewed: `78454082e2d4253780a3a0f8a4ab92b9d87c2f9f36d5014c51a4222e89fada96`.
- Existing cost-accounting JSON: `7c3e9a712a5242f90757425d811393a5ecc3783fa2883388f1e087c95a08ae1c`.

The companion `read_segmented_benchmark.py` has SHA-256
`e800c80d826e9bf03cea210c98efd72ef406423127138660b71539044add284f`.
Its `SEGMENTED_BENCHMARK_RECORD_REVIEW.json` has SHA-256
`8ae7002d5612c10f0144ddcc5b3570949953bc31d1cf0a69ba7ee0541d492c73`.
Run this reader directly to reproduce the checks; its imports are exclusively
Python standard library. It also checks all eight original source pins, the
actual startup-guard bytes, and the frozen exact-codec source used to reconstruct
the token representation. Duplicate JSON keys and nonfinite JSON constants are
rejected. Equality checks use canonical JSON bytes, preserving bool/int and
string/number distinctions. No historical scientific raw was modified.

## All samples and complete numeric equality

The raw contains exactly the declared fixtures `(21,2)`, `(21,4)`, `(65,3)` at
width four, with history `1000` and epsilon `1/3`. Each fixture has two pairs,
first old/new then new/old: six pairs and twelve timed engines in total. The
source constructs a fresh Gram engine/cache for every sample. The actual
SOTraceBank is shared; there is no old rank-two bank in the comparison.

For every pair the reader checks every entry of all saved 6-by-6 covariance
matrices, their keys and denominators, the entire observer operation streams,
conditional plans, numeric ledgers, terminal positive mass labels, phase/codec
and two-H4 bindings. The six-dimensional representation is the source-certified
lossless restriction of complete native 61-dimensional words, not discarded
residuals. Native call counts, Gram and policy counters and both pre-evidence
and final guard topology agree. These checks exceed trace-only equality.

The distinct saved matrices per engine are 22, 13 and 35 for the three fixtures;
the observed native calls per engine are respectively 73, 116 and 54. Every
observer's saved kernel, graph dimension and depth is matched to the corresponding
entry of the actual native call stream. No matrix arithmetic was recalculated
by this reader. Exact cross-version cursor equality is correctly not claimed:
the versioned policy/token metadata intentionally differs.

## Calls, shared tables, and token storage

The source-recorded half-open call intervals form a disjoint complete partition
of the 1,495 retained actual `recurrent_mass_power` calls:

| Component | Calls |
|---|---:|
| Native program/bank admission | 244 |
| One shared cold SO bank | 36 |
| Three paid cache warmups | 243 |
| Twelve timed engines | 972 |
| Standalone token derivation | 0 |

The cold-bank call slice also equals its complete embedded setup call list.
Counts are not recomputed by summing overlapping cumulative reports. All timed
factory **and inverse** instances have unchanged computed columns, column digit
replays, and arithmetic bit-wiring/bit-length counters. The 18 final concrete
instances (nine factories and nine created inverses) are counted once each:
9,032 setup digit replays, 11,077 column digit replays, 88 columns, 502 requests,
414 cache hits, plus 5,494 separately recorded permutation-verification digit
replays. These are distinct from the 1,495 native calls.

Using only saved admitted columns, words, counts and metadata, the reader
reconstructs all three token byte segments: 235,766 + 235,524 + 235,745 =
**707,035 bytes**. It reproduces the 707,088-byte original wrapper and exact token
SHA-256 `14860d161647b13bc70db5743ba6da11e5f71b575dfdea8ce7223492aa653340`.
This is an encoding check on existing evidence, not a new propagator. These
numbers measure payloads, not peak RSS, Python object overhead or allocator use.

Each calculation interval has six logical binding checks. The old route calls
the frozen whole-view method six times; the new route calls it once in its
constructor and has five complete-byte fast accepts. Evidence capture adds a
sixth fast accept and a seventh logical binding check. No measured sample uses
the slow compatibility fallback. Source inspection confirms that constructors
derive their own token; the standalone derivation is neither injected nor
subtracted. The result does not weaken the admitted-bank identity, canonical
wrapper, ordinary trusted-object, synchronous-entry or strict-restore contracts.

## Timing meaning and limits

All six saved new calculation intervals are shorter than their old pair. The
two-pair mean calculation reductions reported in the note, 10.80%, 13.20% and
18.05%, accurately describe these fixtures. Full recorded sample values remain
in the companion JSON and original raw; no sample is discarded or replaced.

Calculation includes the constructor (including checks and new token derivation),
four advances and final mass. The evidence timer covers `engine.evidence()`.
The through-evidence timer also includes the intervening counter/inventory/UTC
gap. The reader verifies each timing identity and ordered UTC bracket. Per-run
deep-copy detachment and final JSON/gzip serialization are outside these timers.
The whole-checker 13.109781299950555-second timestamp is taken before the final
`capture_tables` comprehension as well as before serialization. It is therefore
a pre-final-capture elapsed record, not an end-to-end archive-generation time;
no performance ratio in the note uses it.

The preserved wall window is 2026-09-27 05:56:54.549064 to 05:57:07.658753 UTC.
The note reports team coordination with no scientific/large-I/O overlap; this
reader cannot independently prove quiet OS load or absence of any unrecorded
run. Within the saved execution all declared samples and warmups are retained,
and no unexpected failure artifact is present.

There are only three fixed fixtures, two deterministic alternating orders per
fixture, one process, one history, and warmed shared modular tables. The twelve
engines are not twelve independent random trials. This supports the bounded
host binding optimization and does not establish significance, full-law speed,
asymptotic improvement, a reduction in native Gram arithmetic, or a general
Shor simulation improvement. No further execution is needed for this review.

Authority/context: shared active RA-CAAAC604CB513AEA8BBC1DFC and preserved actual
startup PASS. The review reused the current canonical policy under the existing
valid lease; it neither changes native activity nor claims independent admission.
