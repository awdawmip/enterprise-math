# Bounded review of adaptive feedback execution

Status: SHARED_CONTEXT_AUTHOR_REVIEW / NOT_INDEPENDENT_ADMISSION.
No new scientific run was performed for this review. The five earlier frozen theory/source-readback files are unchanged.

The final implementation matches the local Gram-action theorem within its declared native word-omission scope. Two issues found during review were repaired before the final execution: a post-commit resource exception could previously leave a bit committed, and an unobserved candidate defect was previously serialized as zero. The old source and completed first run remain in `adaptive_execution/prior_validation/`.

## Read scope and binding

I read both implementation and checker source, the final summary, and the complete decompressed raw JSON. From the raw record I inspected the saved decisions, full-matrix comparison flags, terminal-law records, codec bindings, serialized replay, interruption event and rejected-cursor replay evidence. Administrative checks matched the payload byte count/hash, summary/source bindings, current source hashes and the length of the native-call receipt list. I did not rerun native gates, independently regenerate the probability laws, or treat stored checker flags as an independent scientific execution.

- `adaptive_feedback.py`: `86263eb4a70fe53f8960aae2c1f0b8695dbca40a597b2711af90f20667ed3c45`.
- `check_adaptive_feedback.py`: `cd77bc2ff17a6b2938665a622a74c332e7e24cbe362ba359225fc071716510d3`.
- `ADAPTIVE_FEEDBACK_RESULTS.json.gz`: 4,807,682 bytes; SHA256 `36a6460fbda4d081d1416bbfa48fa0fd641f96d0df235d2d168a7ac06aa5a9c0`.
- Decompressed payload: 118,117,750 bytes; SHA256 `3e356df6befcbf201801657016f64072e2bccebbc0a877a51570f77748d7b78b`.
- The corresponding theorem is `ADAPTIVE_NATIVE_PRECISION_INTERFACE.md`, SHA256 `a0b95c02554e85c3693022bd309a4486f008be80491e1a1f0679d8f40b75d1d6`.

## Mathematical and implementation checks

The reference word sequence is determined by the measured prefix. `_gates` obtains every past selected sequence from immutable committed steps and the current sequence from the pending decision. Consequently the inherited Gamma recurrence sees the actual selected past words, rather than recomputing the past with a newly chosen bank. The matrix cache belongs to one monotonically extended measured history. No private latent work label enters the precision policy.

`defect` computes all four signed terms of `(T-S) C (T-S)^T`. It correctly cancels the inherited `_combine` routine's structural factor 1/4 before tracing the result. The computation retains the entire encoded covariance, not only a scalar bit correlation. The recorded exact six-mode codec is bound to complete 61-mode forward/inverse columns; its omitted complement is exactly zero. Identity and these specific admitted direct words preserve the same subspace. This does not establish a codec for RP1 roots.

For a positive-mass candidate, the implementation first checks `0<=A<=4M` and then observes `8AM-A^2-16e^2M^2<=0` using the signed native observer. This is precisely the theorem's squared local-isometry test. A successful omission charges the **entire remaining budget**, so at most one positively charged omission occurs along a path. This is conservative and can consume budget even if a candidate happens to have zero defect; it is correct, but not an optimized allocation rule. Failure selects the complete reference feedback and adds no local defect.

When no candidate was tested, `candidate_A` is now null and `candidate_defect_observed` is false. All such fields in the inspected final raw record satisfy that convention. Zero physical mass is never treated as a normalized error certificate. The gate decision has a reference/identity extension there, while inherited conditional probabilities reject conditioning on zero mass and `advance` rejects a zero-probability child. This is consistent with an exact low-policy path; it is not the totalized approximate-row walker used in the earlier pruning experiment.

## Continuation repair and evidence

`advance` now installs a temporary next-step ledger solely for validating the new-depth mass. If any exception occurs, it restores the parent history, steps and pending decision, removes cache entries depending on the uncommitted bit, and preserves actual observations, counters and an interruption event. It appends the certificate only after successful validation. The actual query-budget-2 fixture raises after the pending decision, records `history_committed:false`, increases the budget and retries the same bit. The resulting cursor and mass match a fresh run, with exactly one committed bit.

Serialized cursors are fully reexecuted and compared using strict JSON bytes. The final evidence includes pending and terminal equality and ten rejected controls. Seven controls that performed a failed prefix replay retain the actual replay evidence through `CursorReplayError`; the three early consistency/type controls did not claim such a replay. This closes the failed-replay accounting omission identified while reviewing the earlier checker.

This cursor restores a deterministic committed-prefix/pending-decision ledger by **paying for reexecution**. It does not restore the Gram cache or an RNG/random tape. A future stochastic driver must separately persist its already selected bit and RNG state across interruption. The current code is a trusted in-process scientific object and a strict serialized-cursor verifier, not a sandbox against arbitrary direct mutation of its Python attributes.

## Actual bounded results and their limits

All four fixtures use t=4 and epsilon=1/3. The final checker records 448 prefix comparisons of the implicit covariance and child masses with a separate explicit signed native construction. Whenever a candidate defect is observed, every matrix entry is compared. Both complete joint history/work laws are normalized.

| Fixture | Recorded joint history/work TV | Accepted omission occurrences across replayed leaf runs |
|---|---:|---:|
| N21/a2 | 0 | 8 |
| N21/a4 | 8317233883492754523506912687407 / 324518553658426726783156020576256 | 8 |
| N65/a3 | 0 | 8 |
| N15/a2 | 0 | 0 |

The nonzero N21/a4 value is below 1/3. It is a declared additional sensitivity fixture, not a resampling-until-success selection. Repeated leaf runs revisit prefixes; neither the 448 checks nor the omission counts represent independent random inputs or single-sample costs.

The zero-TV even-order cases have a relevant structural explanation when the omission occurs only at the last step. Before that step the support lies in H=<a^2>; for even ord(a), H and aH are disjoint. Each arm therefore lands on different work labels and a complete orthogonal change of feedback cannot change the immediate measured joint bit/work law. For odd order this disjointness argument is unavailable, making N21/a4 a useful sensitivity check. This explanation does not make arbitrary intermediate omission exact.

The full run retains 20,725 actual native-call receipts. Its reported 129.34516849997453 seconds is the checker's combined bounded workload through the recorded timer, not a matched one-sample speedup. Bank construction/admission, explicit law validation, repeated prefix work, candidate-defect construction, fresh cursor replays, failed replays, table setup/replay and certificate serialization are distinct costs. Core-call count is not a substitute for all typed digit/phase/observer/bit-complexity counts. A final resource audit must respect actual object/call ownership rather than recursively charging repeated embedded source certificates.

This is an executed interface witness using existing direct words and certified omission. It is **not** RP1 b8/b64 execution, a proof of fixed low-precision success, a useful-factor guarantee at canonical width, a general polynomial Gram oracle, or an end-to-end speedup result. No remaining substantive mismatch with the stated theorem was found in this bounded source/evidence review.

Global-Knowledge-Sync: main@06788df / GLOBAL_KNOWLEDGE_V1.
