# Structural two-bit successor: bounded execution design

Status: CODE_ONLY / NOT_EXECUTED. The coordinator will run the declared checker
once after source review and the actual startup guard, under the existing
research authorization. This subtask writes and compiles code only.

The exact design source is `STRUCTURAL_SHORTCUTS.md`, SHA-256
`845df9a8a9e67862f197412d2bd8a20fdc10aedf14db73efc59f70ca97cfda7f`, with shared-context
symbolic review `guard_review/STRUCTURAL_SHORTCUTS_REVIEW.md`, SHA-256
`133d81d27860bc108075a8b995ec42644d37834c3824caaacfc6c22b30f946ab`.
Neither source is changed. The executed aligned predecessor remains frozen.

## API, admission and routing

`ShortcutTwoBitObserver.two_negative(g, ell, k, R, r, stride=1)` accepts strict
integers, g>=2, 0<=ell<k<g, R>=1, 0<=r<R and stride one, with V=2^ell dividing R.
The signed count retains the original raw denominator exponent 2g. This is a
supplied-modulus scalar observer, not an order oracle or full Gram computation.

The new version composes the frozen `DirectSignedGapObserver` and its typed
runner. It never invokes the old public whole-query method or imports/runs the
old checker. Public bit/exponent indices are wiring; numerical divisibility,
scales, signs, lengths, sums and exact quotients are recorded typed work.

1. Construct V and perform typed R/V. A nonzero remainder rejects before any
   cancellation test. An incomplete request makes the observer terminal: later
   requests and complete export reject, preserving already paid work.
2. Construct **original** U=2^k, then perform typed U/R. If its remainder is zero,
   return a typed zero with the residue-histogram cancellation reason. The record
   explicitly says no orientations, affine progressions or moments were evaluated.
3. Otherwise retain both difference orientations, including head R at r=0 and
   both equal heads at half modulus. Typed R/V parity determines whether each
   orientation is split into two progression branches. The chronological
   record preserves the actual order: both outer heads are made before either
   orientation executes. Original compressed parity supplies the scalar sign.
4. If k=g-1, each required single progression uses the affine formula in the
   proof. Otherwise it invokes only the frozen direct private progression.
   Selection depends on the declared bit index, never the saved answer or cost.
5. For each branch, the observed low remainder t=0 omits the entire shifted
   progression. Its receipt has `OMITTED_ZERO_COEFFICIENT`, `progression_called`
   false, and no fabricated computed value, length or operation interval.
   For t>0 both sums are computed with their own canonical lengths. Any dropped
   shifted endpoint must be proven exactly M by typed equality; it denotes the
   empty A_one(M)=0, not a nonempty table at the boundary.

The affine progression records typed canonical n; U_c minus head; the reached
division and candidate q; candidate minus n for the minimum selection; and the
selected q. Both T(n) and T(q) retain s-1, s(s-1), exact division by two, head and
step products and their sum. The s=0 case remains signed typed arithmetic (the
intermediate s-1 is -1). Each shifted progression recomputes its own n and q.
No host `min`, modulo, power, division or ordinary numerical reference computes
these results. Host routing consumes signs/remainders from saved typed outputs.

Each nonzero query has at most eight requested private progressions and sixteen
top-level moment tables; omitted progressions are counted separately. Empty
requested affine progressions remain actual calls with receipts. Recursive
moment calls and primitive/digit costs are distinct from these structural counts.

## Fixed fixture and exact historical reuse

The only planned production grid is the predecessor's six tuples, all residues:

| g | ell | k | R |
|---:|---:|---:|---:|
| 2 | 0 | 1 | 1 |
| 3 | 0 | 1 | 3 |
| 3 | 1 | 2 | 2 |
| 3 | 1 | 2 | 4 |
| 4 | 1 | 3 | 6 |
| 4 | 2 | 3 | 20 |

This is 36 new residue results. The checker reads the complete historical
61,934,942-byte payload and validates SHA-256
`61aee1882148519bd9738bacf6f107a39532aa98de6c128854edb98df334aba9`, its 2,183,581-byte
gzip SHA-256 `f6bf350f188d4252c60c897778561e3c4957d65774a25a12334b35261f0b7bd3`,
all three old stage source pins, old startup guard, imported arithmetic/proof
pins and complete old positive replay equality. It compares against the 36
saved values. The old 720-pair comparison and old production/replay are **read,
not executed again**. Output stores the immutable raw pins and per-case pointers,
old values and old cost metadata; historical cost is never added to current work.

The same grid covers residue cancellation, affine progression and moment
fallback; zero coefficients, nonzero shifted coefficients, empty progressions,
the M boundary, q=0/q=n/the affine junction and retained half-modulus multiplicity.
The even compressed-step fixture is cancelled before propagation in this new
dispatcher. The surviving even-step propagation branch remains inherited in
form from the reviewed predecessor, but this six-tuple successor run does not
claim to re-exercise that branch after a failed cancellation test.

Six new complete positive replays are planned. Sixteen certificate tamper
controls include eleven full paid replays (zero reason/output, orientation,
omitted coefficient, affine length/minimum/exact-half, shifted tail, sign,
fallback table offset and output), one paid incomplete nonalignment replay,
and four early source/schema/bool/non-string-key rejections. All actual replay
receipts are retained, including rejection. A non-string-key attempt is saved
using a typed-key encoding. Ordinary input controls retain ten pre-rejections,
two paid nonaligned rejections and two valid-input reuse attempts on those
incomplete observers; reuse must add no operations or mutate the old receipt.

## Evidence and cost accounting

The checker has the actual startup-guard hook and refuses any existing
`SHORTCUT_RESULTS.json.gz`, `SHORTCUT_SUMMARY.json` or
`SHORTCUT_FAILED_EXECUTION.json.gz` before main-run work. Success and failure
writes are exclusive. Frozen executed source hashes and the guard are checked
again at the end.

Report current production, positive replay, paid input rejection and negative
replay separately: actual native CALLS intervals, digit replays, typed and signed
operations, host arithmetic wiring/bit-length counts, moment/cache statistics
and structural route counts. Zero-work pre-rejection and reuse intervals remain
visible. Historical production/comparator counts form a separate comparison
column. This is a correctness and operation-cost comparison, not a matched
timing benchmark; current costs and any speed advantage are unknown before run.

Top-level main-run failure handling preserves completed output, current runner
and inflight work, fresh replay captures, all CALLS, current/finished negative
and input attempts, source pins and guard. Unreturned local branch dictionaries
are not promised; their paid raw operations remain in the runner. Import errors
and failure-save I/O errors are outside this recovery promise. A failed request
is not advertised as a resumable certificate.

Mathematical review and further reasoning can continue in any dialogue using
the proof and saved evidence. Actual computation retains the typed BRC contract;
no new primitive, precision escalation, ordinary matrix propagator or independent
admission is claimed.

Global-Knowledge-Sync: main@9f0e65b / GLOBAL_KNOWLEDGE_V1
