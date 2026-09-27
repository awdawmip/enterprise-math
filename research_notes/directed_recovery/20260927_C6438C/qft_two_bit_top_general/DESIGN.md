# Highest selected bit, arbitrary modulus: bounded native execution design

Status: **CODE_ONLY / NOT_EXECUTED**. This document and the checker are prepared
without importing a scientific module or running arithmetic. The coordinator
must review the exact sources and supply an actual startup guard before the
single declared execution. No new result or operation-cost saving is assumed.

The independent observer source is `top_bit_general.py`, SHA-256
33a46d5f3dacf61e83cedd75cb3424f2375485b3b58984429d5c9fc76b8c96d0.
Its proof is `TOP_BIT_GENERAL_MODULUS.md`, SHA-256
880fb9d90f9258e0b96f6f47281bd711b11bd2ec515bddb6a6212cf45266ee89,
with `guard_review/TOP_BIT_GENERAL_MODULUS_REVIEW.md`, SHA-256
e5f31e9619a3233c65af23b642d262e98996d6ca9ee538910e38c21ba412aaab.
The science source and those two notes remain unchanged by checker preparation.

## API and actual arithmetic

`TopBitGeneralObserver.two_negative(g, ell, k, R, r, stride=1)` requires strict
integers, g>=2, 0<=ell<k<g, **k=g-1**, R>=1, 0<=r<R and stride one. It has no
2^ell-divides-R admission test. R and r are supplied counting inputs, not an
order or address discovered by this algorithm. The certificate schema is
`BRC_TOP_BIT_GENERAL_MODULUS_V1`, distinct from the aligned and shortcut schemas.

Both difference orientations are retained. At r=0 their heads are 0 and R;
at a half-modulus residue the equal heads have multiplicity two. For each
orientation, actual typed canonical counts split d<L at d<L/2 versus d>=L/2.
Zero-count segments are skipped with their actual zero receipts. Nonempty
segments use two degree-three moment tables with offsets b and b+V, V=2^ell.
Polynomial coefficients, signed moment differences, displacement-weighted
moments and the numerator are actual typed operations. One certified exact
division by three yields each segment sum. Original raw normalization is 4^-g.

At most eight top-level tables are requested per residue. This is not eight
native operations: recursive nodes, cache queries, digit replays, bit wiring,
coefficient construction, exact division and replay must all be counted. The
constructor uses the frozen direct runner and floor routine; it does not use
an ordinary numerical reference, a host scientific pow/mod/gcd/trigonometric
evaluation, a matrix propagation substitute or a lattice-counting backend.

## Exactly declared new comparison grid

Each tuple visits every r in [0,R), with one independent typed ordered-pair
histogram pass per tuple, accumulating all residue buckets together.

| g | ell | k | R | New residue values | New ordered pairs |
|---:|---:|---:|---:|---:|---:|
| 2 | 0 | 1 | 3 | 3 | 16 |
| 3 | 1 | 2 | 3 | 3 | 64 |
| 3 | 1 | 2 | 5 | 5 | 64 |
| 4 | 2 | 3 | 6 | 6 | 256 |
| 4 | 2 | 3 | 9 | 9 | 256 |
| 3 | 1 | 2 | 11 | 11 | 64 |
| Total | | | | 37 | 720 |

These are six new tuples. The count 720 coincides with the earlier aligned
experiment's count, but none of these tuple comparisons reexecutes an old
fixture. The checker copies `typed_pair_histogram` verbatim as Python source
from the frozen aligned checker, SHA-256
6777057a9468b673c7d58a657467c65ae1c37bd353fd55b9eb86a743efdaa969.
Before the run it checks that file's bytes and compares both extracted AST
source segments. It records a function-text hash and helper hashes. It reads
but does not import or execute the old checker. The copied algorithm obtains
sign bits, signed differences, quotient/remainder and bucket updates through
the actual typed runner; it retains every digit and pair observation.

The grid covers ell=0, ell>0, previously nonaligned R, both polynomial pieces,
the exact L/2 junction, nonzero low remainders, empty segments/orientations,
negative answers, r=0, half-modulus multiplicity and R>L. Assertions consume
actual retained source-bound records. No additional input or answer is chosen
after seeing performance. All six complete certificates receive fresh positive
replay, including every request and all integer evidence; only the declared
primitive-cache native-call delta is excluded from semantic equality.

## Input, forgery, paid-prefix and reuse controls

Twelve ordinary input controls reject before numerical work: bool g, too-small
g, negative ell, ell=k, k>=g, nonpositive R, negative r, r>=R, stride!=1,
bool ell, well-ordered but non-top k, and bool R. They record empty operations,
empty request lists, inflight=None and zero additional native calls.

Fourteen certificate controls are predeclared:

- Nine retain complete honest fresh replay before detecting changed evidence:
  segment split, high-segment head, polynomial coefficient, shifted offset,
  exact-third denominator, missing half-modulus orientation, moment-table
  output, raw denominator exponent and final signed output.
- One preserves a paid valid first request before a second request whose g is
  changed from 3 to 4, making k=2 non-top. It captures exactly one completed
  request and its full typed work, with **inflight=None**. This is an incomplete
  verification of a forged request sequence, not a failure of a valid numerical
  input and not a terminal failed observer. No later request is executed.
- Four reject before arithmetic: wrong source, schema, bool first input and
  non-string key. A typed-key representation preserves the last forgery instead
  of losing the key type through JSON normalization.

Reasonable reuse is tested without adding successful queries: in the first
production fixture, after its legitimate r=0 request, the checker attempts
non-top input (4,0,1,3,0). It saves complete before/after snapshots and requires
them, operations and CALLS to be unchanged. The original grid's r=1 and r=2
then execute normally on that observer. This zero-work subinterval is contained
in the production interval and is not counted again. Its two saved snapshots
overlap the production evidence and are not additional cost streams.

No eligible input is deliberately made to fail an arithmetic assertion, and
no external monkeypatch creates an artificial scientific failure. True
unexpected failures are retained by the outer handler, not reported as PASS.

## Cost, startup and failure retention

The checker requires an actual STARTUP_GUARD allowing this activity, mode
TASK_RESEARCH, startup boundary and no sync debt. It records the complete guard
and its hash. It pins the observer, checker, DESIGN, proof/review, direct helper
and comparator template before work, and checks the same identities at the end.
It refuses an existing success gzip, summary or failure gzip. Writes are
exclusive; failures are not erased and performance is not retried for a better
sample. Running the checker is a separate coordinator action after review.

Cost categories are current production, new typed comparator, positive fresh
replay and negative fresh replay (including the single paid-prefix rejection).
The zero-work input controls and embedded reuse check remain visible without
fake paid-input streams. CALLS intervals are disjoint and cover actual global
native invocations exactly once. Digit, typed/signed operation, bit wiring,
bit-length, moment-node/request/cache and maximum counters remain distinct.
Repeated evidence copies are not extra executions. Elapsed time is the declared
whole-checker interval before serialization, not a matched speed benchmark;
record bookkeeping, hashing and serialization are outside arithmetic counters.

A LIVE registry retains completed cases, current observer, current typed pair
runner and digit/pair/bucket observations, current and completed attempts,
replay captures and CALLS. The failure handler snapshots available raw fields
without computing a new answer; each field's snapshot error is isolated and
reported while preserving the independent CALLS list. Unreturned constructor
objects, import failures before main and failure-save I/O are outside the
recovery guarantee. A partial verification record is not a resumable program.

The output filenames are TOP_BIT_GENERAL_RESULTS.json.gz,
TOP_BIT_GENERAL_SUMMARY.json and TOP_BIT_GENERAL_FAILED_EXECUTION.json.gz.
Full raw receipts and source bindings are retained for later metadata-only
author/peer readers. This preparation performs no scientific execution and
does not claim formal independent admission.

## Scope after a successful run

Success would establish these 37 new exact scalar outputs and their controlled
certificate behavior. The symbolic algorithm uses a fixed number of existing
degree-three floor tables with polynomial-bit bounds in explicit scale length
O(g+log(R+1)). Actual costs can still exceed the finite comparator. It would not
establish a faster entire Shor algorithm, unknown-order discovery, general
non-top two-bit compression, growing-mask compression, arbitrary noncommuting
matrix correlation or a complete approximate/strong simulation.

Global-Knowledge-Sync: main@604893e / GLOBAL_KNOWLEDGE_V1
