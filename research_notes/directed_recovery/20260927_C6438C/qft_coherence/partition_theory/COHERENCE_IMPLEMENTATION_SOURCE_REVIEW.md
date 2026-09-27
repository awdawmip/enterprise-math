# Read-only source review of the coherence-skip prototype

Status: SHARED_CONTEXT_AUTHOR_CHECK / NOT_INDEPENDENT_ADMISSION.
This review did not modify or execute the sampler. The parent was running its bounded checker separately. No execution result is certified by this source review.

Reviewed sources:

- `coherence_sampler/coherence_skip.py`, SHA256 `5c9a2388d063bc8d2c9ef02382856e67fa399e322c1347fefcdf41ef0d3d8fed`.
- `coherence_sampler/check_coherence_skip.py`, SHA256 `03b840dc8c63057ab6ae9814ca41cb6354f9c2b95857a8eb7385d4eb33060456`.
- The inherited frozen `single_walker.py` row-query, append, exact-rational random draw and run/pause behavior; the existing typed binomial observer and lazy-program constructor were also read.

No substantive algorithm defect was found in this source version.

The fair step preserves the actual latent proposal and avoids row queries. At restored exact-score steps, the implementation does not reject a zero parent row: a nonzero queried pair uses its exact full-vector score, while a zero pair has an explicit fair extension. Thus intermediate fair replacements do not rely on the approximate latent state obeying the exact norm law. The future point-row oracle uses the full recorded measured history and the original ordered complete native feedback.

The statistical verifier reconstructs the training selection, every typed validation path, union-event record, exact binomial tail, squared error bound, status, observer receipts and contract metadata, rather than trusting a rehashed summary. The fail route keeps `skip_depth=None`, so it uses the original exact scores with a harmless totalization outside reference support. Independence of training, validation and sampling remains a random-source contract; seeded software tests do not prove physical randomness or a history of no prior selective retries.

On a point-query budget pause the parent history and sampled auxiliary proposal remain intact; partial recursive row caches are retained. On a random-source pause, any completed plan also remains intact. Once the selected bit is drawn, the inherited `PointRowOracle.append` only appends a tuple and does not perform a budgeted query. There is therefore no current post-draw budget-failure window requiring the extra `pending_selected_bit` used by the earlier projected-row updater. Extending append to do fallible work would require revisiting this conclusion. Durable cross-process recovery and arbitrary runtime monkeypatch protection are not supplied by this review.

The checker enumerates all finite histories for verification only, propagates the approximate joint latent law separately from the actual raw reference state, and compares all final joint atoms. It explicitly includes impossible-reference zero-pair behavior and measures zero-parent restoration plans. The checker currently exercises random-source pause/resume; a claim that query-budget resume was also executed would require a corresponding actual record. Source reasoning supports its inherited budget-pause mechanism without claiming that additional test ran.

Cost presentation needs the same distinction as the prior package: inherited `program_metrics` branch counters are not counters for the row/proposal route. Count all table instances, including separate inverse caches with equal `(N,b)`, and separately charge the constructor's permutation-certificate verification digits. Global native call counts and per-run oracle records capture different units and phases. Later exact row queries can rebuild ancestors across a skipped layer; avoiding two local queries alone does not prove a whole-run reduction.

The final TV statement applies to the completed outer distribution. Any history-dependent budget pause must be resumed or have its unresolved probability charged; selecting only completed runs is not certified. Current source flags express this boundary correctly.

Global-Knowledge-Sync: main@f44ed595 / GLOBAL_KNOWLEDGE_V1
