# Complete-native SO trace bank: bounded execution

Status: **AUTHOR_SHARED_CONTEXT_ACTUAL_BANK_EXECUTION / NOT_ADMITTED**.
The standalone bank passed its declared native checks. No omission policy,
Gram history, ideal-QFT reference, factorization, or full-law experiment was
executed in this unit. Frozen Uniform and Boundary source files were not edited.

## Executed certificate

`SOTraceBank` requires the actual complete 61-carrier native-word program.
Every cold constructor clears the complete-word replay cache for each word,
replays all 61 forward, inverse and inverse-recovery basis inputs, checks the
program's complete columns and binding against that replay, and revalidates
the optional exact carrier codec. The underlying primitive cache may already
be warm; a zero new core-call count does not mean those word loops were skipped.

The new bound uses the actual H4/sign/swap receipt and the frozen native sources.
The H4 is symmetric orthogonal with trace zero and determinant +1; a negation
and a swap each have determinant -1. Distinct-coordinate embedding preserves
these values, so the parity of negative-determinant letters certifies the
complete word's orientation. This is a source-bound structural proof, not a
numerically executed generic determinant. The source pins include the actual
`native_quartet` and `fixed_phase` implementations.

For orientation +1, actual signed positive-path observations compute all
61 diagonal deficits and a deterministic balanced sum
`t_G=61-tr(G)`. The bank returns `s=min(4,t_G)`. Every nonzero eigenvalue of
`(I-G)^T(I-G)` occurs at least twice, so s is a valid squared-norm upper bound.
The generic SO record does not claim that this is the exact norm. If t_G=0,
the zero bound is certified exact. For orientation -1 the bank returns exact
bound 4: a real orthogonal negative-determinant word has eigenvalue -1. The
old failed reflection half-trace 2 is never accepted as a bound.

Each SO word has 122 expression references: 61 deficits, 60 binary additions
and one clipping margin. Identical signed factor sequences share a real
observer receipt, while every diagonal and sum retains its own input address.
All resulting graphs have at most five states and depth two. The bank does
not execute or store the old signed orthogonality-residual, I-G, B or B-squared
matrices. Their orthogonality premise instead follows from the source-bound
orthogonal primitive product and the unchanged complete native-word admission.
Actual trace scalars and clipping comparisons come from the signed observer;
ordinary rational computations are encoding/identity checks only.

Forward/inverse columns and transpose recovery are retained in the evidence.
The same immutable record is returned by forward and inverse lookups because
`2I-G-G^T` is unchanged. This does not equate the forward and inverse maps.
The scalar is computed on the full carrier even when the program uses the
six-coordinate exact codec.

## Results and negative controls

| Native word | Bound s | Method | Unique actual observer calls |
|---|---:|---|---:|
| m2 | 2 | SO half trace | 6 |
| m3 | 38415/65536 | SO half trace | 15 |
| m4 | 640927/4194304 | SO half trace | 15 |
| Empty identity | 0 | SO half trace, exact zero | 3 |
| Single negation | 4 | Negative determinant, exact | 0 |
| Two disjoint quarter turns | 4 | SO half trace, not certified exact | 7 |

The three existing bounds equal the frozen old rank-two witnesses, and their
complete forward columns/denominators match that prior evidence. Full D61 and
encoded D6 constructors give identical scalar bounds. The two-quarter example
has actual squared norm 2 by its two native quarter blocks; the new bound 4 is
valid and illustrates why `bound_valid` must not imply `bound_is_exact`.
The special words are bank fixtures and carry no ideal phase-target accuracy
claim.

Three warm binding checks and 18 bound lookups caused zero new core calls;
their host metadata work remains nonzero. A serialized bank was restored by
fresh complete admission and trace observations. Its logical binding equals
the original, while its setup receipts are the new invocation's receipts.

All 23 negative controls passed. They cover strict phase/direction types,
immutable records, codec mismatch, warm metadata bool-to-int change, a cached
column int-to-bool change, illegal gate coordinates, unrehashed scalar changes,
and ten independently rehashed scientific/provenance changes. A rehashed
reflection claiming bound 2, the old bank schema and duplicate JSON keys are
also rejected. Eleven controls include a complete freshly constructed bank
in their rejection evidence. One of these is the reflection replay, which
does real full-column work but needs zero trace/core observations. Thus the
13 zero-core-call rejections must not all be described as zero-work failures.

The new immutable bank and strict serialized view have separate schemas and
types. They intentionally cannot be injected through the frozen Uniform or
Boundary classes' exact `WordCertificateBank` type gates. Policy integration
requires a separately reviewed version; it was not performed here.

## Cost and evidence scope

The whole checker took 32.9694428 seconds and 722 actual core calls. Saved bank
construction/replay invocations account for 478 of those calls, exactly the
478 retained signed observer operations; the remaining 244 are initial native
admission. There are 17 saved bank invocations and 43 replayed-word records,
including the intentional serialized failures. They are not independent
sampling trials.

The encoded three-word cold bank used 36 observer calls in 1.5287003 seconds.
Its old historical comparator used 205 calls in 8.1595358 seconds. The new
observer-reference count is 366 versus the old 44,655; actual unique observer
graph states total 170 versus 1,696. These counts concern different certificate
algorithms on the same actual words. The elapsed times came from separate
runs, so this is not a controlled paired timing result or a whole-program
speedup claim.

The new bank stores 363 trace nodes instead of the old four full witness
matrices containing 44,652 entries. Both retain 22,326 complete forward/inverse
column entries. The encoded logical bytes only changed from 1,382,158 to
1,356,564, because full source words, bindings and columns still dominate.
This measured size prevents equating fewer auxiliary matrices with a similarly
large reduction in the whole certificate's serialized size.

Each word's recorded 61+61+61 basis actions describes its compulsory first
fresh replay. Final codec validation can cause additional replay-cache misses;
these extra native word loops are covered by constructor elapsed time but not
claimed to be counted completely by that basis-action field. No total host
bit-cost or total primitive-loop count was measured. Factory table snapshots
are kept per program instance and not summed across repeated evidence views;
initial permutation-verification receipts remain in the raw payload.

`extract_so_trace_cost.py` is a stdlib-only reader. It verifies payload/source
hashes, checks nonoverlapping saved call intervals, and emits
`SO_TRACE_COST_ACCOUNTING.json`. Running it does not execute native science.

## Failure boundary and immutable binding

The checker has an outer `BaseException` handler that writes a distinct
`FAILED_EXECUTION_<id>.json.gz` with source hashes, known stage, traceback and
all actual core calls, using exclusive creation. No unexpected failure occurred
in this run. That handler's failure path was added before the execution; it
is not itself claimed to have been exercised.

A raw `SOTraceBank` constructor admission failure does not promise an attached
`TraceReplayError.evidence`. The executed serialized-tamper controls are the
different case where fresh construction succeeds and logical comparison then
rejects; those complete fresh-replay receipts are attached and preserved.
The outer checker catcher is the safety net for an unexpected constructor
failure during this checker, not a generalized partial-constructor API.

- Implementation SHA-256: `e2f7f839a8b6826ee3edff7b06070dd91f3e90e7f29278d56e1682d608c6b18d`.
- Checker SHA-256: `219094fe4e27ea35b53aa618d26d272e89355820df88aec47b48144180e02418`.
- Raw payload: 18,396,582 bytes, SHA-256 `6ec1b936ddb16370aa4ba596e7ba095f3bd90fc823d5a7b0d054cb3503019975`.
- Gzip payload: 919,004 bytes, SHA-256 `926d8b6aa7ed4b11dc8a8bdab0add0149585ecf877445262edc66caa865487ac`.

The next small unit is the explicitly versioned uniform-policy integration
from `SO_TRACE_CERTIFICATE_PLAN.md`, using these bound records while preserving
public-history decisions, exact typed charging, strict restore, and transaction
semantics. This bank result does not remove the remaining large-work-support
or general Shor complexity problem.
