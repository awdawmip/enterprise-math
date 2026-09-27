# Final uniform-policy cost audit

The reusable certificate removes the repeated prefix-specific defect calculation, and the four complete bounded output laws match the previous state-specific policy exactly. **This execution does not demonstrate an overall speedup:** the new complete checker recorded 301.223288 seconds, versus 129.345168 seconds for the previous checker. The workloads and concurrent activity differ, so this is an observed whole-run regression, not a controlled timing benchmark or a causal attribution to one operation.

This is shared-context, author-level read-only accounting. No scientific source was imported or experiment repeated by the extractor. Source snapshots and scope are recorded in `SOURCE_REVIEW.md`. The final input is `uniform_execution/UNIFORM_FEEDBACK_RESULTS.json.gz`: raw SHA-256 `4a4e57d960ff689f5244307070d94ff180b594fb0db3824119d741cad78a1460`, 120,817,955 bytes; gzip SHA-256 `14456595a5ff8e7c3e67d78fe091b1aefec68be835a9674cefbd4dfba3b0b015`, 4,649,416 bytes. All four current source hashes match the final summary.

The historical comparator is the frozen adaptive raw `3e356df6befcbf201801657016f64072e2bccebbc0a877a51570f77748d7b78b`, with cost JSON `f82a4362365c95112b3780685ac4e02ca0a24e88b37f421219ab06883d6999f3`. Its scientific experiment was not rerun. The new read-only extractor also verifies equality of every recorded selected-word ledger, for both routes and all four fixtures, against that frozen run.

## Once-per-bank cost and reuse

The first shared bank certificate covers the same three complete 61-dimensional words, with exact witnesses:

| Phase index | s | Unique signed observer expressions |
|---|---:|---:|
| 2 | 2 | 13 |
| 3 | 38415/65536 | 102 |
| 4 | 640927/4194304 | 90 |

Each word binds 14,885 expression references: four complete 61×61 matrices and one scalar witness. Identical expressions reuse actual observer receipts. Across the bank there are 44,652 stored full-matrix scalar entries, 22,326 complete forward/inverse column entries, and 1,382,158 serialized logical bytes. The setup cost is **205 native observer calls and 9.1329235 seconds** in this main run, excluding original program/bank admission. Do not add the 205 unique observers again to its 205 core calls.

Cold cursor restoration constructs the same bank again: another **205 core calls and 8.8056591 seconds** for bank setup, plus the separately counted prefix replay. Forward, inverse and inverse-recovery loops cover all 61 basis columns in each construction. Their extra native-kernel-call intervals are zero because lower-level primitive data are already cached; clearing the complete-word replay cache still forces the full loops. Zero additional kernel calls are not zero integer or host work.

`certificate_bank_final` repeats the same immutable setup evidence; it is not a third construction. Warm use performs a complete structural binding check and returns a frozen witness without rerunning its scientific observers.

The independent word-certificate checker is a separate execution, raw SHA-256 `c4a88c9bd19b9ac6c3b96ac9f42f339f436a48c32fdcb6a5230d37cb3a666e44`. Its 2,100 core calls, twelve rejection controls, reflection failure and identity-zero boundary were read and hash-checked, but are **not added** to the main execution's 15,183 calls. Its twelve cross-program warm checks made no additional native calls; they still did structural comparison/serialization work.

## Comparable warm-route counters

Every route below replays all 16 proposed length-four histories from separate Gram objects, stopping impossible histories early. The table is not a set of independent stochastic trials. The actual six-coordinate adapter has complete-61-column provenance and retains the admitted residual subspace.

| N, a | Previous adaptive low: vector actions | Uniform low: vector actions | Uniform reference: vector actions | Uniform low/reference observers | Uniform low/reference Gram requests | Matrices per route, summed across objects |
|---|---:|---:|---:|---:|---:|---:|
| 21, 2 | 2,556 | 1,440 | 1,536 | 778 / 744 | 1,152 / 1,152 | 352 |
| 21, 4 | 3,708 | 2,592 | 2,880 | 1,250 / 1,216 | 864 / 864 | 208 |
| 65, 3 | 1,788 | 672 | 768 | 562 / 528 | 1,488 / 1,488 | 560 |
| 15, 2 | 60 | 24 | 24 | 126 / 124 | 312 / 312 | 80 |

The first three new low routes save 96, 288 and 96 word-boundary vector-adapter calls relative to their reference routes. Those savings are real counts in this bounded checker, not native-kernel calls or a speed measurement. Each new low route also pays its scalar certificate tests: 34, 34, 34 and 2 lookups, respectively. All saved receipts show **zero prefix-specific defect calls, zero defect-matrix entries observed, and zero prefix-mass observations for policy selection**. Forbidden old defect/policy-mass observer labels are absent. The sampler still computes its own branch masses and correlations.

The accepted omission occurrences are 8, 8, 8 and 0 across repeated leaves, corresponding to 4, 4, 4 and 0 unique prefix decisions. The complete laws and recorded word ledgers equal the frozen previous policy; this coincidence is established for these fixtures only. Joint TV relative to the unchanged reference is zero in three fixtures and exactly `8317233883492754523506912687407/324518553658426726783156020576256` for `(21,4)`.

**No matrix-count compression occurred.** Retained matrix totals are the same as in the prior adaptive run. Maximum single-object cache sizes remain 792, 468, 1,260 and 576 scalar slots; those exclude temporary matrices, evidence objects and the explicit-state checker. Audit unions of identical history-specific queries remain 82, 61, 104 and 22, and were not implemented as shared caches.

Full-state checker vector actions were not separately instrumented. Its observer operations are reported independently in the JSON; they are not attributed to the uniform policy. The explicit checker no longer performs the old policy's full state-dependent defect comparison, so raw whole-checker call totals do not measure only the optimization of the production path.

## Binding, modular tables and controls

The saved Uniform objects performed **12,139 successful certificate-binding checks**, including checks triggered during their evidence capture. Four explicit fixture-level checks and two constructor checks on discarded early-rejected objects occur outside those saved objects. The per-route binding counts are 1,712 / 1,712, 1,328 / 1,328, 2,160 / 2,160 and 516 / 516. Each check reconstructs and compares word/column views and serializes binding data. Its full host-bit or timing cost was not profiled. This is a concrete overhead candidate, not a proven allocation of the whole elapsed-time difference.

Shared modular tables are counted once per actual program/factory/inverse instance, preserving distinct caches with the same multiplier. Final monotone snapshots and column receipts pass the same read-only checks as in the previous cost audit. Across the four programs there are 24 actual table instances, 117 newly computed columns and **28,430 adder-digit replays**: 10,295 setup, 13,119 columns and 5,016 constructor verification. The per-program totals are 5,482, 3,204, 17,172 and 2,572. These counters span both routes and controls; summing cumulative per-leaf table reports would double-count them. There are 4,552 total column requests, most served from these existing caches.

The original and warm-restored cursor objects each record 108 vector actions, 63 requests, 41 hits, 22 matrices and 74 observer calls. The cold-restored object's prefix replay, distinct from its 205-call bank setup, records 108 actions, 30 requests, 20 hits, 10 matrices and 34 observers. The cold fixture stops at the serialized pending prefix rather than duplicating the two warm objects' terminal continuation, so these counts should not be treated as three equal workloads.

Nine malformed cursors each perform a real failed prefix replay before rejection: 108 vector actions, 30 requests, 20 hits, 10 matrices and 34 observers. Their **972 vector actions and 306 observers** are included. Three other controls reject before Gram/observer work. Both successful replay and failed replay bind the unchanged ordered-word ledger and bank identity.

The budget-interrupted-and-retried object records 10 requests, 5 hits, 4 matrices and 2 observers; its fresh comparison records 7 requests, 3 hits, 4 matrices and 2 observers. Both have zero phase-vector actions. Retry counters include the failed attempt and the successful same-bit retry; there is no fabricated separate interruption cost snapshot and no persisted cache/RNG claim.

## Complete-run evidence and next boundary

The main list of **15,183 native-core calls** decomposes without overlap into:

- 410 for the two cold bank constructions;
- 5,820 Gram/policy observers across complete laws and controls;
- 8,046 independent explicit-state checker observers;
- 663 observers for the two joint-law comparisons;
- 244 other calls for bank/vendor/program admission or shared arithmetic setup, left without a finer unrecorded attribution.

The total recorded Gram vector-adapter actions, including controls, are 11,232. Core-call elapsed time sums to 109.618119 seconds; the checker interval is 301.223288 seconds, excluding final serialization. The prior checker recorded 20,725 calls, a core-time sum of 109.6708839 seconds and a checker interval of 129.345168 seconds. The new suite adds cold restoration and more controls/comparisons, removes state-dependent explicit defect checks, and initially overlapped a separate word-certificate run. **These timings do not establish an end-to-end improvement or isolate a causal bottleneck.** Fewer phase actions and observers are the supported narrow improvement; whole-run elapsed time increased.

A next implementation can investigate one-time admission of an immutable program/word view with a cheaper bound token for recursive queries, while preserving source, ledger and mutation boundaries. That change has not been made or tested here. The present certificate also does not make exact Gram queries efficient, remove paid modular arithmetic, or establish general polynomial-time Shor dequantization.

Reproduce the accounting with `python extract_uniform_cost.py`. It reads the fixed final raw files, imports only standard-library accounting helpers pinned by hash, and rewrites only this directory's `COST_ACCOUNTING.json`. The helper dependency is the already published adaptive `extract_cost_accounting.py`, SHA-256 `925cc3ee46effb69490ccb11ccf92d51120df489d4ec0b8c3a29ded3695ef730`.
