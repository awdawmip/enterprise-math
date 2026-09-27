# Complete-native SO trace bank review

Status: **SHARED_CONTEXT_REVIEW / NOT_FORMAL_ADMISSION**. No material mathematical, implementation, or accounting defect was found within the stated bank-only scope. This review read the final implementation and checker, the complete decompressed result, the cost extractor and its output, and `SO_TRACE_EXECUTION_NOTE.md`. It performed only saved-byte, structural equality, hash and cost-metadata checks; no native calculation or scientific experiment was rerun.

## Bindings and inspected evidence

| Object | SHA-256 |
|---|---|
| `so_trace_certificates.py` | `e2f7f839a8b6826ee3edff7b06070dd91f3e90e7f29278d56e1682d608c6b18d` |
| Final `check_so_trace_bank.py` | `219094fe4e27ea35b53aa618d26d272e89355820df88aec47b48144180e02418` |
| Cost extractor | `a7b690a16acb242712afe88de6ea8f2834bdb68e56aebf0297f8dc0f40b24b89` |
| Cost accounting | `54c14d72a2b2076d413b6fe0a0ad545aca1a3e3ed8f92ca90bb14fb7c5e93d7d` |
| Execution note | `499133c620df3944bb30d1e5d7184d597cece12748c2a9fe0de9a6e49545d27f` |
| Raw result, 18,396,582 bytes | `6ec1b936ddb16370aa4ba596e7ba095f3bd90fc823d5a7b0d054cb3503019975` |
| Gzip result, 919,004 bytes | `926d8b6aa7ed4b11dc8a8bdab0add0149585ecf877445262edc66caa865487ac` |

`read_so_trace_evidence.py` and `SO_TRACE_METADATA_REVIEW.json` document this review's independent administrative extraction. The current source hashes equal the result and summary bindings. The raw call-list length is 722. Every saved bank setup's entire call slice equals the corresponding global call-list slice, and the nonempty setup intervals do not overlap. All bank logical hashes were recomputed from strict canonical JSON bytes, without importing scientific code.

## Mathematical and native-admission checks

The orientation premise is a structural theorem about the actually returned, source-pinned primitive alphabet. The stored H4 is symmetric orthogonal with trace zero, hence has two positive and two negative eigenvalues and determinant +1. Negation and a coordinate swap each have determinant -1; legal distinct-coordinate embeddings preserve these determinants. Counting their occurrences in the normalized replayed word is therefore sufficient. This is not an executed generic determinant or an ideal-angle assumption. The raw primitive receipt and source hashes for `fixed_phase.py` and `shor_benchmark.py` are present.

For an SO word, nonzero squared singular values of I-G from nonreal eigenvalues occur in conjugate pairs; the -1 eigenspace has even dimension as well. Therefore the largest is at most half their trace, `61-tr(G)`, and at most 4. The implemented clipped bound is valid. For determinant -1, at least one -1 eigenvalue exists, and the squared norm is exactly 4. The implementation correctly distinguishes `bound_valid` from `bound_is_exact`: the two-quarter fixture obtains a valid bound 4 without claiming exactness; the reflection obtains exact 4, not its invalid half-trace value 2.

Each constructor first forces a complete-word replay for every phase and compares the supplied program against actual full forward/inverse columns, sparse application caches, phase source bindings, and exact codec structure. The complete 61-dimensional columns are stored even for D6. The codec checks both directions, zero cross blocks, and identity on the complement. All stored full-column transpose comparisons and the D61/D6 column/scalar comparisons passed this saved-evidence review. No residual coordinate is removed from the norm certificate.

The 61 diagonal deficits, 60 balanced sums and one clipping margin are evaluated through signed positive-path observers. Every trace node points to an actual observer result, including shared identical expressions. The saved graphs have at most five states and depth two. Removing the old extra signed Gram and B-squared observations relies on the bound orthogonal primitive product plus unchanged actual complete-word admission; it does not turn an ordinary host dot product into the sole scientific source.

The inverse lookup correctly shares only the bound/word-pair record: `2I-G-G^T` is the same for G and its actual inverse. It does not claim the two matrices are identical. The three actual phase bounds are 2, 38415/65536, and 640927/4194304; the source-bound prior full-column evidence and the current D61/D6 records agree as reported.

## Restore, negative controls, and detachment

All 23 saved controls are genuine rejections with recorded exception type, reason, and call interval. Twelve reject before a fresh bank replay. Ten independently rehashed logical/provenance changes each pay 36 observer calls and fail strict comparison after complete fresh construction. The rehashed reflection bound 2 also fails after fresh construction, with zero new core calls but real complete-word work. Thus 11 controls carry complete fresh bank evidence, whereas 13 controls have zero new core calls; these categories must not be conflated.

For every attached failed replay, the retained logical object equals the honest fresh result, its logical digest is valid, and its setup receipt matches that rejection's actual global call slice. Boolean/integer changes are rejected by strict serialized comparison. Raw duplicate JSON keys are rejected. A legitimate serialized restore returns the fresh setup evidence and exactly the original logical bank identity. The old schema is rejected deliberately.

The bank stores serialized immutable evidence bytes and returns decoded copies. The negative-control helper additionally deep-copies attached exception evidence. Temporary program mutations are restored in `finally`; the cached-column test uses replacement of the frozen word record. No intermediate live-list alias was found in these stored objects. These checks operate within the declared trusted in-process/no-monkeypatch contract; they are not a security boundary against arbitrary Python object manipulation.

The earlier partial-constructor issue is now accurately bounded in the final note. A raw admission exception need not carry `TraceReplayError.evidence`. Current attached records cover successful fresh construction followed by serialized logical mismatch. The checker has an outer unexpected-failure catcher preserving context and actual core calls, but that path was not triggered or experimentally validated here. This review does not upgrade it to a general resumable partial-constructor API.

## Costs and cache boundary

The exact total is **244 initial admission calls + 478 saved bank observer calls = 722**. The initial admission intervals are [0,243) and [243,244). The bank subtotal comprises three ordinary three-word banks at 36 calls each, special words at 3+0+7 calls, ten failed ordinary restores at 36 calls each, and the failed reflection restore at zero calls.

There are 17 saved bank invocations and 43 replayed-word records. Their first forced replays alone represent at least **7,869 basis actions**: 43 times 61 forward, 61 inverse, and 61 inverse-recovery inputs. This is a lower bound, not total native word-loop work. The final codec revalidation may cause further complete-replay cache misses, which remain included in elapsed construction time but are not exhaustively counted by those fields.

The encoded bank's 36 unique observer calls split 6/15/15 across the three words, with 366 expression references and 363 stored trace nodes. Its primitive-call interval is empty because initial native admission already populated the lower-level cache. Clearing the complete-word cache still executes full word loops; zero new kernel calls in those intervals does not make that execution free. Warm reuse records three checks and 18 lookups with zero new core calls, not zero host work.

The encoded cold time was 1.5287003 seconds; the old historical bank time was 8.1595358 seconds with 205 calls. These are separate runs, not a paired timing study. The new graph-state sum is 170 versus 1,696 historically. Full forward/inverse storage remains 22,326 scalar entries in both; total logical serialization changed only from 1,382,158 to 1,356,564 bytes. The note correctly avoids translating fewer auxiliary matrices into a comparable whole-certificate storage reduction.

Factory snapshots preserve the five distinct program instances, with 3, 3, 2, 2, and 2 tables respectively. Repeated equal modulus/multiplier values do not collapse distinct instances. The extractor explicitly leaves permutation replay receipts in raw and does not claim a full typed-digit, host-bit, primitive-loop, or memory ledger. Its stated limits are appropriate.

## Conclusion for the next bounded unit

The actual bank is ready to be consumed by a separately versioned, reviewed SO policy. No policy, omission, conditional probability, full output law, or factorization run occurred here. The immutable bank and schema intentionally do not pass the frozen Uniform/Boundary exact-type gates. Further integration must retain this separation and continue to charge actual cold admission separately from warm lookup and policy/Gram work. This result does not establish general Shor simulation efficiency.
