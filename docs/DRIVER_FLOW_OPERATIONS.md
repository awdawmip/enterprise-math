# Driver evidence synthesis and follow-up through ordinary ChatGPT

Use the existing private `EM_CHAT_CONTROL_V1` GitHub inbox. These operations run
the current native Source functions; they do not create a third Driver review or
choose mathematical dispositions. Use the own active Driver session and declare
all prior contributions. Read the actual Result and both reviews before judging.

All four operations take the own successful Result `artifact` request as
`result_request_id`. Optional `reviewer_contribution_ids` supplements the actual
Source session history; omission never clears known contributions. Session/Driver
IDs, Result hash, exact review set and Source commits are derived by the service.

| Operation | Additional payload |
|---|---|
| `review_flow_state` | None. Read the exact current review IDs, reference passes, synthesis, follow-up and their evidence pins. |
| `review_reference` | `pass_number` 1 or 2, explicit `finding`, explicit `independence_status`. Native pass 1 is semantic; pass 2 is adversarial. |
| `review_synthesize` | Explicit `disposition`, `rationale`, `destination_class`; optional `destination_ref_or_none`. Both exact-set reference passes are required. |
| `followup_materialize` | The own successful `driver_publish` request as `publication_request_id`, plus `followup_spec_filename`. The spec must contain the explicit native gates and Task/closure decision. |

`review_reference.independence_status` is a closed native enum, not free text. The
only accepted literals are `CLEAN_INDEPENDENT_CONTEXT`,
`SHARED_CONTROL_CONTEXT_DISCLOSED`, `NOT_INDEPENDENT`, and `NOT_APPLICABLE`, exactly
as defined by `research_review_evidence_store.py::INDEPENDENCE`. The current Driver
must choose the literal that is factually supported by its real contribution and
context history. A fresh conversation, session, or Driver ID never by itself
justifies `CLEAN_INDEPENDENT_CONTEXT`; known overlap must remain disclosed. An
`INVALID_REFERENCE_INDEPENDENCE` response means the payload literal is outside
this native set (or otherwise failed the adapter contract), not that the Result or
existing immutable reviews should be replayed.

For multiple existing reviews, read state, complete only the next missing pass,
then synthesize and materialize. Existing immutable records survive a new Driver
session/conversation. Read and consume prior steps instead of overwriting them.
A new Driver retains the original reviewer/synthesis author in provenance and is
recorded separately as the current materialization publisher. Never borrow the
old Driver ID or infer independence from a new session.

The service freezes both Result bytes and the complete current review set including
raw review hashes. A drift before Source CAS requires re-evaluation, not timestamp
selection. Unknown remote outcomes use `reconcile` with the original request ID.
Successful materialization returns real Task/publication IDs. Continue their
smallest unfinished question; do not stop at a control summary or publish an empty
follow-up merely to satisfy a lifecycle gate. A justified native parent closure
is distinct from Task-scope continuation.

For routing, a dispatch or receipt response with `action_summary_complete=true`
and `paging_required_for_selected_action=false` contains all selected-action
metadata. Proceed to its exact Task/continuation or eligible preparation without
paging unrelated activity history. `receipt_truncated` alone does not require
reading those diagnostics. The original raw receipt remains available in bounded
pages. This exception concerns routing metadata only: actual task, Result, review
and artifact evidence still must be read as needed, across pages.

No Working Truth, Foundation, P000 change, automatic ACCEPTED disposition or
unperformed experiment is implied by this transport. A result is a mathematical
or evidence contribution; registering, polling or inspecting the queue alone is
not that result.
