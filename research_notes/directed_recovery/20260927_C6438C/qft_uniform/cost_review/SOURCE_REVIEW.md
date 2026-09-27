# Shared-context source and cost-boundary review

This is a bounded read-only cross-check by another author agent with shared context, not formal independent admission. No scientific calculation was repeated and no builder, policy, checker or prior frozen source was edited.

Reviewed source snapshots:

| File | SHA-256 |
|---|---|
| `uniform_execution/uniform_feedback.py` | `755d398a19881508112c9e360c94bf10133681af8d3cbdbb103accdecc306e28` |
| `uniform_execution/check_uniform_feedback.py` | `e2a34cfa0d2a2ace6cb309ce25148778b0b880ef899e9f5452f22a6c36e44efa` |
| `word_certificates/word_certificates.py` | `c3e8156b5c7573778cd1e781f23e82394c83842a9f4655b59c9659035dc62ce3` |
| `word_certificates/check_word_certificates.py` | `8b0288c83b8e130b4fa20aad6c02eea84995975a26fc348ff842ba394590fe98` |

The frozen adaptive source and checker are explicit dependencies. The new checker reuses their actual full-state `child`, `mass` and covariance observations, and compares reference laws against the saved old raw payload. It does not substitute an ideal phase/QFT reference.

## Mathematical and implementation alignment

The builder reconstructs each full 61-column word after clearing the complete-word replay cache. Both inverse columns and inverse recovery are exercised. A warm primitive cache may give zero additional native-kernel calls for those loops; the loops and integer work still occur. Their elapsed time and native-cache state are retained, so zero kernel calls must not be read as zero setup cost.

`B=(I-G)^T(I-G)` and `B^2-sB` are formed from complete actual columns via signed positive-path observations. Every full-carrier entry has an explicit receipt-index address. Identical ordered factor expressions, including a single actually observed zero expression, reuse a receipt; this neither erases residual entries nor assumes a small ideal target angle. The nonnegative witness test, the half-trace choice of `s`, and the full residual check agree with the stated sufficient norm theorem. The reflection counterexample correctly fails: its sole nonzero `B` eigenvalue is 4, while the proposed half-trace is 2, giving residual 8. The identity boundary has `s=0` and passes.

The immutable bank binds the full word, direction, full columns, codec and sources, while excluding `N`, `a`, work schedule and history. Reuse across four programs with identical word/codec views is therefore appropriate. Its `check` is a structural comparison and serialization operation, not another observer replay. Its `restore` rebuilds and compares fresh logical evidence, including the strict boolean/type distinctions of JSON encoding. The supplied mutable setup fields are provenance, and the returned object carries the new actual setup receipts.

The new `prepare_next` uses the oldest active word certificate and the rational test `8s-s^2<=16e^2`. It does not call `gamma`, take a policy prefix-mass trace, or construct a candidate defect matrix. The inherited `defect` entry point is explicitly rejected. The common remaining orthogonal left factor is retained in the original order; no commutation assumption is introduced. Exact Gram calls remain in the underlying branch probabilities and committed-state checks. The universal bound extends to a zero vector, while `probabilities` still refuses conditioning on zero mass.

The strict `WordCertificateBank` type check was added before execution, removing reliance on a caller-supplied duck-typed `check/get` object. Ordinary Python monkeypatching or `object.__setattr__` bypasses are outside the stated trusted implementation contract, as they were for the frozen dependencies.

## Restore and accounting

Public-prefix restoration binds the policy, program, own/parent source, immutable bank hash, ordered selected words, charges and pending certificate. It pays for replay of that prefix. Cold restoration also constructs the complete bank again. These are different cost categories, and neither restores a cache or random tape.

Malformed cursors that fail after deterministic replay retain actual failed-replay evidence. Strict bit validation can reject before constructing a new object; unchanged-program/history validation can reject before Gram work. The two paths must not be assigned identical cost. The bounded retry retains the selected input bit/pending decision, rolls back the uncommitted step, and uses the inherited fixed ledger. There is no new random driver in this experiment.

`certificate_binding_checks` counts each successful binding call made by a retained `UniformFeedbackGram` object, including checks triggered while capturing its evidence. Four explicit per-fixture bank checks occur outside those objects; two deliberately discarded invalid-state objects also have constructor checks. The immutable `certificate_bank_final` contains setup provenance, not a dynamic final warm-check counter, so its position in record construction causes no counter omission. Repeated copies of that bank evidence are not additional cold constructions.

No substantive discrepancy was found in the reviewed source snapshots. The final read-only cost extractor must still verify actual raw hashes, zero policy-defect counters and observer labels, shared table-instance totals, and the separation of full-law validation costs from warm policy work. This source review alone does not assert execution results or a speedup.
