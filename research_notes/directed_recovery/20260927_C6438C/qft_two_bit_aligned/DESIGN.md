# Aligned two-bit adapter: bounded execution design

Status: CODE_ONLY / NOT_EXECUTED. This draft is code-only; the coordinator will
run the declared checker once after source review and the actual startup guard,
under the existing research authorization.
The mathematical source is `../sep27-qft-two-bit/TWO_BIT_PERIOD_NESTING.md`,
SHA-256 `9189f01243aa308f516534337b40e6e2c03a7fcf3f79a7dde179a5689bca1d26`.
Its shared-context symbolic review is frozen separately; no source is changed.

The new `aligned_two_bit.py` exposes
`AlignedTwoBitObserver.two_negative(g, ell, k, R, r, stride=1)` for strict integer
inputs g>=2, 0<=ell<k<g, R>=1, 0<=r<R, stride=1 and **V=2^ell dividing R**.
It returns a signed integer count with the original raw denominator exponent
2g. It neither discovers an order nor computes phases/full Gram matrices.

The adapter composes the frozen `DirectSignedGapObserver` and uses its same
`TypedFloorMoments` runner. It calls only `_coefficients` and `_progression`,
never the old public whole-query `one_negative`. Each orientation is retained
separately. Compressed M=L/V, high bit k-ell and R/V are derived by actual typed
integer operations (public exponent/index differences are wiring). Divisibility,
h parity, branch-head parity, original/branch lengths, signs and all weighted
arithmetic are recorded. If h is odd, both parity branches remain, even if one
is empty. Equal half-modulus heads are not deduplicated.

For each surviving branch, the original progression and shifted-by-one
progression each compute their own canonical length in [0,M). The shifted
sum uses the sign of the original z, followed by the explicit subtraction;
it does not reuse (-1)^(z+1) with a second sign flip. If its count is smaller,
the difference must be one and a typed equality certifies that the discarded
original endpoint is M-1, hence the shifted term is the explicitly empty
A_one(M)=0. No nonempty table can receive displacement M. The maximum is eight
single-bit progressions and sixteen top-level moment tables per modular query;
recursive nodes, cache requests and digit work are additional costs.

## Frozen run grid

The planned checker uses these six tuples, every residue once:

| g | ell | k | R | Purpose |
|---:|---:|---:|---:|---|
| 2 | 0 | 1 | 1 | Smallest domain, ell0, R1 |
| 3 | 0 | 1 | 3 | ell0, compressed high-period count H=2 |
| 3 | 1 | 2 | 2 | Adjacent bits, odd compressed step, half modulus |
| 3 | 1 | 2 | 4 | Even compressed step, nonzero low remainder |
| 4 | 1 | 3 | 6 | Separated positive bit positions, odd compressed step |
| 4 | 2 | 3 | 20 | R>L, empty/singleton orientations and shifted zero tail |

This is exactly **36 residue outputs and 720 ordered pairs**. The comparator
enumerates all (x,y) once per tuple and accumulates every residue bucket in that
one pass; it does not re-enumerate for each r. Both sign bits are extracted by
typed division; differences, Euclidean residues, bit sums, parity and bucket
updates use the typed runner. No ordinary host modulo, powers, arithmetic
reference values or old scientific rerun supplies the expected answers.

Every tuple has one fresh positive certificate replay. Negative controls will
alter orientation multiplicity, compressed length, shifted zero-tail record,
branch sign, h parity, raw exponent, final output, an input modulus changed to
nonalignment, source, schema and bool input, plus a non-string key: twelve
certificate negatives in total. Invalid ordinary inputs are pre-rejected without work.
Two nonaligned inputs have actual typed divisibility work and retain incomplete
receipts; they are not advertised as free pre-rejections. Math/record tampering
requires a paid fresh replay, whose complete receipt is retained even when the
final equality rejects; source/schema/bool/key rejection can occur earlier.
An observer with an incomplete request refuses further requests. Each of the
two paid input failures is followed by a valid-input reuse attempt that must
reject without changing the retained request, evidence or counters. This does
not implement an unfinished-request resume protocol.

## Evidence and cost boundaries

The planned artifacts are `TWO_BIT_ALIGNED_RESULTS.json.gz`,
`TWO_BIT_ALIGNED_SUMMARY.json` and, only on unexpected failure,
`TWO_BIT_ALIGNED_FAILED_EXECUTION.json.gz`. The checker refuses any existing
success, summary or failure before scientific work and uses exclusive writes.
Top-level failure handling preserves all native CALLS, complete finished cases,
the live production request/runner, live brute labels/pairs/buckets, captured
replay work and the current tamper attempt. Mixed-key attempted inputs use an
explicit typed-key encoding so JSON serialization cannot silently change them.
Unreturned local branch/orientation dictionaries are not promised: their
already-recorded signed and typed operations remain in the runner snapshot.
The handler covers errors inside the main run, including its serialization;
module import or failure-save I/O errors remain outside that recovery promise.

Report production, one-pass comparator, positive replay, paid input rejection
and negative replay separately: actual native call intervals, adder-digit
replays, typed operations, host arithmetic wiring/bit-length counters, signed
operations, moment requests/nodes/cache hits and top-level progression/table
counts. Do not sum maxima or shared native calls as independent work. Host
serialization/index bookkeeping is outside the arithmetic counters. This is a
correctness/cost fixture, not a matched timing benchmark or a general speed claim.

Only source writing and `py_compile` occur in this code-only subtask. The
coordinator will run the declared checker once after source review and the
actual startup guard, under the existing research authorization. Future actual work
must preserve full signed receipts, frozen native sources and the shared-context
not-admitted scope. Mathematics and further symbolic review can proceed from
this note in any conversation without requiring the local executor.

Global-Knowledge-Sync: main@a3609ca / GLOBAL_KNOWLEDGE_V1
