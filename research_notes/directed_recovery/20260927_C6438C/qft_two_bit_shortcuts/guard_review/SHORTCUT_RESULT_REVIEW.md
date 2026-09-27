# Shared-context complete saved-record review

Verdict: PASS; no substantive discrepancy found in the completed shortcut
experiment. This is a peer review within shared context, not independent
admission. The reviewer performed only complete file reads, hashes, strict
record comparisons, operation-link checks and cost accounting. No scientific
module was imported, no moment or scalar answer was recalculated, and no
scientific experiment or historical pair enumeration was rerun.

## Exact reviewed evidence

- `SHORTCUT_RESULTS.json.gz`: 2,027,431 bytes, SHA-256
  `07ff488f357a2d80a682508f28b7f242a4cdd92c2cc15cfd54b95e884104e53a`.
- Complete decompressed JSON: 57,941,257 bytes, SHA-256
  `55f0652225cffe7a658f5528e30ebf8c90342b9422def6799285d32a7dc66be7`.
- Source/checker/design: respectively `874d5d79f67ef5a00176b48faa2959811b925820031a90f71f80b6ba6fd5a34b`,
  `e7dca9fe712c367ed5434ed88ac2027178bbf05fff1fb94373d77c8c01d39e22`,
  and `b41ebf07ab34b9fa6981f529a5d230952b050786dd97f64eb1886827b1b3d667`.
- Actual startup guard: `d002bf88886316a60af33391ebaf0ef54325c0dc5f9787fb88a96c08022fb297`.
  Its complete saved object matches the local pinned guard and allows activity
  and persistence with no sync debt.
- Full historical aligned gzip and 61,934,942-byte payload were read and hash
  checked, including payload `61aee1882148519bd9738bacf6f107a39532aa98de6c128854edb98df334aba9`,
  all three source pins, native ancestry and guard. Its 36 values and per-case
  evidence/cost pointers match this run; its 720 ordered-pair records are
  historical evidence, not newly performed work.

The reproducible pure-I/O reader is `read_shortcut_result.py`, SHA-256
`31a3e584c96accfe1d27e0e74d1dd96af547b2507a6cf785af934d7efb32c47f`.
Its full result is `SHORTCUT_RECORD_REVIEW.json`, SHA-256
`940163869f3ebbb8cdeffde522bf82e9fb9239967b71043579910eb38000aad6`.
It uses the pinned previous aligned and direct I/O readers, whose hashes are
recorded in that JSON; neither imports a scientific executor.

## Complete operation links and controls

All 26 actually charged streams were inspected: six production, six positive
fresh replay, two paid input failures and twelve paid negative replays. Every
saved signed operation consumes its exact typed-operation index span; saved
sign/magnitude outputs match the corresponding typed output fields. All
retained native adder cells match the saved source-bound eight columns, and
digit/wiring/bit-length counters were independently recounted from these
records. The single global native call has 12 states; it is not the total work.

The chronological cursor checks admission before cancellation, original U/R,
all surviving scale/coefficient construction, the two heads before either
orientation, parity splitting, and each final signed sum. Affine progressions
check their own canonical n, typed minimum selection, both T constructions,
exact half division, all products and final combination. Nonzero shifted terms
retain independent lengths and the exact M empty-tail witness. Zero-coefficient
omissions have no fabricated value, length or execution interval. Every direct
table input/output, recorded node/child/cache link and its operation range is
checked; node recurrences are not scientifically evaluated again.

All 36 answers equal the frozen historical values. The recorded routes are
seven cancellations, 26 affine queries and three direct-moment queries.
There are 158 requested private progressions: 146 affine and twelve direct;
38 shifted progressions were actually omitted, with 24 top-level moment tables.
Checks include negative answers, r=0, doubled half-modulus orientations,
empty progressions, the affine junction, q=0/q=n and shifted M tails.

All sixteen tamper controls are present: four zero-work early failures, eleven
full paid fresh replays and one paid partial unaligned replay. Each full replay
strictly matches its honest source case and differs from the supplied forgery;
the partial replay ends after failed alignment and before the zero test. Typed
key decoding retains the non-string-key negative rather than normalizing it.
The twelve input rejections comprise ten early and two paid failures. Both
subsequent valid-input reuse attempts on terminal failed observers record zero
additional work. Their unchanged-snapshot claim is the executed checker's
assertion plus the retained original snapshot; no second after-snapshot is
invented by this review. There is no unexpected failure artifact.

## Costs and valid comparison

| Charged category | Streams | Adder digits | Typed operations | Signed operations |
|---|---:|---:|---:|---:|
| Production | 6 | 37,503 | 8,313 | 8,068 |
| Positive fresh replay | 6 | 37,503 | 8,313 | 8,068 |
| Paid input rejection | 2 | 43 | 5 | 5 |
| Rejected certificate replay | 12 | 111,661 | 24,829 | 24,094 |
| Total | 26 | 186,710 | 41,460 | 40,235 |

The total also contains 2,009,303 arithmetic wiring operations, 111,794
arithmetic bit-length calls, 115 retained moment nodes, 195 requests and 80
cache hits. These counters exclude serialization, dictionary/index work and
other uninstrumented host overhead. CALLS intervals partition the one actual
native invocation exactly. Repeated saved copies are not separately charged.
The author's `SHORTCUT_COST_READBACK.json` cost categories, native source and
complete CALLS object agree exactly with this independent record extraction.

| g, ell, k, R | New production digits | Historical observer | Historical pair comparator |
|---|---:|---:|---:|
| 2, 0, 1, 1 | 16 | 4,664 | 387 |
| 3, 0, 1, 3 | 11,894 | 16,088 | 2,268 |
| 3, 1, 2, 2 | 78 | 6,800 | 2,186 |
| 3, 1, 2, 4 | 204 | 7,273 | 2,530 |
| 4, 1, 3, 6 | 8,065 | 18,074 | 12,547 |
| 4, 2, 3, 20 | 17,246 | 24,864 | 15,613 |

Production drops by exactly 40,260/77,763, about 51.77%, relative to the
historical observer on this grid. Four of six cases use fewer digits than their
historical pair comparator, but total production 37,503 remains above 35,531.
This is an operation-count comparison, not a universal advantage. The recorded
28.76671770005487 seconds includes reading the previous full payload and the
larger negative-control suite, and ends before final serialization. It cannot
be compared directly with the older whole-checker elapsed time as a speedup.

## Remaining boundary

The grid does not exercise surviving even-compressed-step propagation after a
failed cancellation test; the relevant old fixture cancels first here. Source
review covers that branch, but this execution does not. The interface still
requires supplied R and 2^ell dividing R. It has not integrated general Gram
queries, order discovery or full sampling. The separate arbitrary-modulus
top-bit proof is symbolic and does not expand this run's admission or coverage.

Global-Knowledge-Sync: main@9f0e65b / GLOBAL_KNOWLEDGE_V1
