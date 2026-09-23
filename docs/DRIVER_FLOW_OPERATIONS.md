# Driver evidence synthesis and follow-up through ordinary ChatGPT

Use the existing private `EM_CHAT_CONTROL_V1` GitHub inbox. These operations run
the current native Source functions; they do not create a third Driver review or
choose mathematical dispositions. Use the own active Driver session and declare
all prior contributions. Read the actual Result and both reviews before judging.

All four operations take the own successful Result `artifact` request as
`result_request_id`. Optional `reviewer_contribution_ids` supplements the actual
Source session history; omission never clears known contributions. Session/Driver
IDs, Result hash, exact review set and Source commits are derived by the service.

The `status` response and authenticated MCP `em_status` publish
`operation_contracts` for all four operations. The checked-in machine-readable
copy is [DRIVER_FLOW_CONTRACT.json](DRIVER_FLOW_CONTRACT.json). Each includes the
exact payload schema, required fields, enums, defaults, role obligations and the
native Source validation boundary. Ordinary Driver receipts repeat their own
`operation_contract`, including when evidence needs paging. Rejected requests
include `recovery.operation_contract` and `recovery.next_action`.

| Operation | Additional payload |
|---|---|
| `review_flow_state` | None. Read the exact current review IDs, reference passes, synthesis, follow-up and their evidence pins. |
| `review_reference` | `pass_number` 1 or 2, explicit `finding`, explicit `independence_status`. Native pass 1 is semantic; pass 2 is adversarial. |
| `review_synthesize` | Explicit `disposition`, `rationale`, `destination_class`; optional `destination_ref_or_none`. Both exact-set reference passes are required. |
| `followup_materialize` | The own successful `driver_publish` request as `publication_request_id`, plus `followup_spec_filename`. The spec must contain the explicit native gates and Task/closure decision. |

`independence_status` accepts exactly `CLEAN_INDEPENDENT_CONTEXT`,
`SHARED_CONTROL_CONTEXT_DISCLOSED`, `NOT_INDEPENDENT`, or `NOT_APPLICABLE`.
It has **no default**. Select the truthful actual context classification, and
put its explanation in `finding`. Use `CLEAN_INDEPENDENT_CONTEXT` only after
checking actual clean independence; disclose shared control context with
`SHARED_CONTROL_CONTEXT_DISCLOSED`; explain nonindependence or inapplicability
with the other two values. None exempts the caller from Source author/contribution
overlap checks. A new session, Driver ID, or correctly spelled value does not
establish independence. Never rewrite a prose declaration into a favorable enum
without making this judgment.

`finding` is nonblank analysis (at most 12000 characters), not a fixed keyword.
Pass 1 checks semantic evidence across the complete exact review set. Pass 2
checks adversarial/control consistency. Complete them in order. An identical
existing pass is consumed without another Source write; differing content is
rejected with an instruction to read the immutable current pass.

`disposition` accepts `ACCEPTED`, `REJECTED`, `PARKED`, `CLOSED`, `SUPERSEDED`,
`RETURN_TO_OWNER`, `REQUEST_REPLICATION`, or `REQUEST_REVISION`.
`destination_class` accepts `NONE`, `FOUNDATION`, `TOOL`, `L4`, `REPLICATION`,
`FOLLOWUP_TASK`, or `ARCHIVE`. Both require an explicit judgment and have no
default. `rationale` is nonblank, at most 12000 characters.
`destination_ref_or_none` defaults to the empty string and accepts up to 2000
characters. Optional `reviewer_contribution_ids` defaults to an empty supplement;
the service always retains known contribution history. Payloads reject unknown
fields and preserve the active Driver role and current DA requirements.

The following are complete payload examples for an **isolated control fixture**.
Replace request references with your own successful requests, read the evidence,
and author the actual finding/disposition before a real mutation. The shared
context and ACCEPTED selections illustrate syntax; they are not defaults or
recommendations for a scientific review.

`review_flow_state`:
```json
{"result_request_id":"result"}
```

`review_reference` (use pass 2 only after the semantic pass exists, with an actual
adversarial finding):
```json
{"result_request_id":"result","pass_number":1,"finding":"CONTROL FIXTURE: exact-set semantic check in explicitly shared control context; no scientific claim is evaluated.","independence_status":"SHARED_CONTROL_CONTEXT_DISCLOSED"}
```

`review_synthesize`:
```json
{"result_request_id":"result","disposition":"ACCEPTED","rationale":"CONTROL FIXTURE: both exact-set checks consumed; isolated writer validation only.","destination_class":"NONE"}
```

`followup_materialize`:
```json
{"result_request_id":"result","publication_request_id":"publish","followup_spec_filename":"portable.json"}
```

The `portable.json` file is uploaded with `artifact_upload` then published by
`driver_publish` in this same Driver session. Its required top-level fields are
`decision` and `gate_decisions`; `tasks` defaults to `[]`. The full native spec
contract, six exact gate names, gate/decision/task-role enums, task fields and
conditional closure obligations are published in
`operation_contracts.followup_materialize.followup_spec_contract` and
[DRIVER_FLOW_CONTRACT.json](DRIVER_FLOW_CONTRACT.json). Source
`research_driver_followup_contract.json` and its native writers remain
authoritative for task admission and successor/closure semantics. In particular,
an empty task list is not a shortcut around a required research follow-up.
For `TASK_SCOPE_CLOSURE_PORTFOLIO_CONTINUATION`, explicitly include
`"terminal_scope":"TASK"` and the exact seven-field `portfolio_continuation`
object. Its `remaining_parent_scope` and `evidence_refs` are nonempty arrays of
unique nonblank strings; `next_action` is a concrete nonblank string. The native
accepted PASS/SUCCESS and satisfaction prerequisites still apply.

For a definite adapter `REJECTED` response, no native submission occurred.
Read `recovery`, correct the exact rejected fields after truthful judgment,
read `review_flow_state` again, and send one corrected request with a new
`request_id` (and a new inbox issue). Do not edit/replay an already-bound issue.
Wrong role or missing DA requires the caller's own real authorized Driver;
contribution overlap requires a genuinely independent authorized reviewer.
For `OUTCOME_UNKNOWN`, reconcile the original request ID and never retry under a
new ID. Source result/review drift requires re-reading and re-evaluation.

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
