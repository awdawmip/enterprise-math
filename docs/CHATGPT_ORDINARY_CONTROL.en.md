# Ordinary ChatGPT research through GitHub

Protocol: `EM_CHAT_CONTROL_V1` · Chinese: [CHATGPT_ORDINARY_CONTROL.zh-CN.md](CHATGPT_ORDINARY_CONTROL.zh-CN.md)

Use the existing GitHub connector. The server runs the admitted Enterprise Math native writers and returns receipts to the original Issue. **No Python, CLI, git clone, full checkout or visible project MCP tools are required in ordinary ChatGPT. Do not require a switch to Work.** The chat still supplies research, evidence judgments and independent review decisions. Check `status.enabled` for actual enabled capabilities.

## Bootstrap and envelope

Establish a valid immutable main snapshot of `awdawmip/chatgpt-global-knowledge`; read its `00_BOOTSTRAP.md`, `OPERATING_MANUAL.md`, `projects/enterprise-math/00_EM_PROJECT_BOOTSTRAP.md` and **`projects/enterprise-math/P000_REALITY_FOUNDATION.json` at that same SHA**. P000 is in this KB repository: do not guess filenames in the Enterprise Math tree. Keep KB, current control Source and frozen research evidence pins distinct. Read the current role/task contracts selectively.

Create an Issue in private `awdawmip/kimi-query-bridge`, with label `em:control` and title `[EM-CONTROL] <request_id>`, supplying title/label/body together. The entire body must be **one `json` fenced block**, not bare JSON or explanatory prose. Replace the example IDs before use:

```json
{"schema":"EM_CHAT_CONTROL_V1","conversation_id":"chat-example-20260922","request_id":"status-20260922-example-01","operation":"status","payload":{}}
```

Required fields are `schema`, `conversation_id`, `request_id`, `operation`, `payload`. `sha256` is optional: **ordinary chats should omit it**. The server always computes the hash; supplied mismatches are rejected. Canonical hashing removes `sha256`, recursively sorts object keys, uses compact UTF-8 JSON with literal non-ASCII characters and no trailing newline. Never guess a digest. Duplicate keys, nonfinite numbers and credential fields are rejected.

`conversation_id` is a stable client-declared logical ID, not platform attestation (1–160 characters; alphanumeric first, then alphanumeric or `:/_.-`). `request_id` uniquely identifies one logical operation (1–128 characters; alphanumeric first, then alphanumeric or `_.-`). The inbox verifies private repository/trusted actor, original immutable body, double-read fingerprint and durable idempotency. Do not edit submitted Issues or create duplicate mutation Issues. Initial requests must be unedited and under 24 hours old. Usually send sequentially; maximum five unfinished requests per conversation. Ordinary payload limit: 16 KiB; canonical envelope: 32 KiB.

## Readbacks and read-only operations

Read the original Issue after about 30 seconds, then about every 15 seconds while pending. Match `EM_CHAT_CONTROL_RECEIPT_V1`, original `issue_number`, `conversation_id`, `request_id` and server `request_sha256`. Inspect inner `bridge_receipt.operation/status/receipt/error/next_actions`. Outer `adapter_status=COMPLETE` can contain FAILED or OUTCOME_UNKNOWN; it is not research completion.

| Operation | Required payload | Optional payload |
|---|---|---|
| `status` | `{}` | None; returns operations/enabled/current session, without granting research authority |
| `dispatch` | None | `kind`: RESEARCH (default), GOVERNANCE, ANY; optional `priority`: P0, P1, P2, P3; omission keeps ordinary routing, explicit null is rejected; inspect native `selection_filter` |
| `pre_final` | `parent_liveness` and exact route fields below | Read-only native final-interaction gate; registration, freeze, review, or close alone does not grant final permission |
| `tasks` | None | `limit=20` (1–100), `cursor`, `dispatch_state` |
| `task`, `continuation` | `task_id` | None |
| `artifact` | `packet_request_id`, `path` | `start_char=0`, `char_count=12000` (max 24000), `source_commit`, `related_start=0`; dependency is successful continuation/artifact/publish_checkpoint |
| `receipt` | `target_request_id` | `start_char=0`, `char_count=12000` (max 24000) |
| `reconcile` | `target_request_id` | None; reconcile an existing uncertain operation rather than replaying it |

When `receipt_truncated=true`, use new read-only `receipt` requests, follow `next_start_char`, and retain returned hash/source_status. Full underlying artifact hash verification does not mean the chat has read every page. QUEUED/RUNNING/POSTING/RECONCILE means keep reading the original request; OUTCOME_UNKNOWN means reconcile, never issue the mutation under another ID. Only an actual canonical NO_DISPATCH establishes no route for its stated kind/snapshot. Permission, source, environment, receipt or ownership errors are not NO_DISPATCH.

## Session and researcher chain

Check status and reuse an existing session in this conversation. For a genuinely new researcher execution:

```json
{"schema":"EM_CHAT_CONTROL_V1","conversation_id":"chat-example-20260922","request_id":"session-20260922-example-02","operation":"session_start","payload":{"role":"RESEARCHER","research_mode":"TASK_RESEARCH","prior_contribution_ids":[]}}
```

Optional `task_id` binds a known task. Declare actual prior contribution IDs; an empty example is not permission to omit existing contributions. Driver uses role/mode RESEARCH_DRIVER. Only one unclosed service session per conversation. Real session IDs/keys, role IDs, claims, ERs, publication/taskbook pins and generation are server-derived. Keys remain private on the server. Chats pass their successful prerequisite request IDs, never session_key, manual pins or fabricated identities.

Normal chain: dispatch → session_start → prepare → claim → open → artifact_upload → publish_checkpoint → freeze. Wait for each prerequisite SUCCEEDED and inspect its exact scope; session/prepare is not a winning claim.

| Operation | Required payload | Notes |
|---|---|---|
| `prepare` | `dispatch_request_id` | Successful dispatch; optional execution_branch must be main and allowed_outputs must be empty |
| `prepare_exact` | `task_request_id` | Successful task/continuation; native eligibility still enforced |
| `claim` | `prepare_request_id` | Successful prepare/prepare_exact/continuation_prepare |
| `open` | `claim_request_id` | Its successful request ID becomes `run_request_id` |
| `resume` | `run_request_id` | Successful same-session resume yields a new request ID/generation; stop using the old one |
| `artifact_upload` | `upload_id`, `filename`, `part_index`, `content` | `final=false` default; final part must use true |
| `publish_checkpoint` | `run_request_id`, `upload_request_ids`, `completed_units`, `current_unfinished_unit`, `next_action`, `do_not_repeat` | `release=false` default; true publishes CONTINUATION and releases. Keep false before freeze |
| `freeze` | `run_request_id`, `publication_request_id`, `return_filename`, `metadata` | Publication must be the same run's successful publish_checkpoint |
| `session_close` | `reason` | Pending requests, active claims or unpublished uploads must be resolved first |

Upload IDs and filenames are simple 1–96 character names (alphanumeric first, then alphanumeric or `_.-`, no slash). Parts start at zero and are contiguous up to index 128. Maximum 16000 UTF-8 bytes and 24000 JSON-escaped bytes per part, 1 MiB per file, 16 files/4 MiB per publication. Use a new request ID for each part; retain upload_id/filename. `upload_request_ids` lists the successful **final complete part request** for each file, not upload IDs or all part IDs. Uploading never executes code.

Checkpoint `completed_units` and `do_not_repeat` are string arrays; `current_unfinished_unit` and `next_action` are nonempty strings. Describe the actual remaining envelope/review work when research is ready; do not invent completion. Use service-generated immutable blob URLs, not custom branch@commit-plus-path strings.

`freeze.metadata` has exactly seven explicit fields: `terminal_verdict`, `hard_target_disposition`, `unresolved_residue`, `method_harvest`, `independence_status`, `source_exposure_status`, `next_control_plane_recommendation`. They report the actual task-bounded verdict, hard-target disposition, remaining gaps, method outputs, independence, exposure and next control action. Native contracts validate values/types; there is **no default PASS**. Server derives the current ER/pin/write authorization. Only native admission, Source publication and complete readback permit frozen HANDOFF. Frozen Result still awaits independent Driver review.

## Existing-frontier continuation

Read exact continuation/artifacts, classify completed/unfinished/conflicted/unknown units and preserve verified work. `continuation_prepare` currently supports a canonically released predecessor with **no live claim and NEEDS_DISPATCH**, not client-declared stale takeover. Required: `packet_request_id`, `reason`. If persisted checkpoint state is SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED, pass only those fields and preserve the native frontier. Otherwise provide `artifact_request_ids` and `frontier_notes` containing exactly the four checkpoint fields above; actual fully hashed artifacts must include authenticated last-progress evidence. Server inherits contributors. Then claim/open. Frozen, active, restricted-source or specialized-lane states require their canonical route, never forced reopening.

## Independent Driver

Use a genuine independent Driver session/conversation and declare all contributions. Chain: session_start(RESEARCH_DRIVER) → driver_activate → continuation → artifact(exact Result/evidence) → artifact_upload(report and required followup spec) → driver_publish → review. Reuse an already-authorized session rather than reactivating repeatedly.

| Operation | Required payload | Optional/conditions |
|---|---|---|
| `driver_activate` | `reason` | previous_authority defaults null; non-null replacement is not supported through this Chat operation |
| `driver_publish` | `upload_request_ids` | Own complete report/spec uploads |
| `review` | `publication_request_id`, `result_request_id`, `review_filename`, `metadata` | `followup_spec_filename`; first native review needs its previously published native followup spec |

`result_request_id` is the Driver's own successful **artifact request**, not a worker freeze request. It must read actual `research_result_records/<Task-ID>/<Result-ID>.json` with complete underlying byte hash verified. Read all necessary pages/evidence before judging. Server derives `result_id` and `expected_result_sha256`; do not supply or calculate them manually. Review metadata requires `disposition`, `destination_class`, `reviewer_contribution_ids`, optionally `destination_ref_or_none`. No automatic ACCEPTED or successor is chosen. Native gates retain current ACTIVE DA/session, contributor independence, current Result bytes and HEAD CAS. Report publication is not formal review; consume verified review/followup before claiming progress.

## Failure actions and acceptance limits

| Error | Next action |
|---|---|
| ONE_JSON_BLOCK_REQUIRED / EXACT_CHAT_OPERATION_FIELDS_REQUIRED | Correct fence/fields after verified rejection, with a new request ID; do not edit history |
| ENVELOPE_HASH_MISMATCH / CHAT_REQUEST_SHA256_MISMATCH | After verified rejection, omit optional sha256 in a new request; do not guess |
| PREREQUISITE_NOT_SUCCEEDED | Read original dependency to completion/failure; do not skip it |
| CHAT_SESSION_START_REQUIRED / CHAT_ACTIVE_SESSION_EXISTS_USE_EXISTING_OR_CLOSE | Complete session start, or inspect/reuse existing session; close only after durable handoff |
| CHAT_DEPENDENCY_SESSION_MISMATCH / CHAT_RUN_SESSION_MISMATCH | Repair own-conversation dependency chain; do not borrow request IDs or old generations |
| STALE_EXECUTOR_GENERATION / CANONICAL_CLAIM_FENCED | Read current continuation; continue only with lawful ownership |
| CHAT_CONTINUATION_REQUIRES_NATIVE_RELEASE_NO_LIVE_TAKEOVER | Preserve current owner/frozen state; follow control recovery |
| COMPLETE_OWN_UPLOAD_REQUIRED | Check final=true, complete receipt and final-part request ID |
| EXACT_NATIVE_FREEZE_FIELDS_REQUIRED | Supply all seven truthful fields; never fabricate PASS |
| VERIFIED_RESULT_ARTIFACT_REQUIRED | Read the actual authorized Result via Driver continuation/artifact |
| *_DISABLED / authorization or admission failure | Preserve exact error, task and unfinished unit; do not invent authority or NO_DISPATCH |
| OUTCOME_UNKNOWN / SUBMIT_UNKNOWN | Retain original operation and reconcile; never replay under a new ID |

Read-only canaries use status and exact continuation/artifact with sha256 omitted. Do not invent tasks, seize active claims or activate fake Drivers for a demo. Formal acceptance requires actual authorized current task routing and separate researcher/Driver sessions. Report transport, formal freeze, formal review and mathematical/experimental validation separately. Native spectralDNS/MPI/FFTW, Lean or other task-required checks still need real capable hosts; this adapter is not an arbitrary shell or code executor. Preserve P000, FREE firewalls, scope, provenance, independent review and Foundation/Working Truth gates. Tests or documentation publication alone do not prove original ChatGPT end-to-end success.

## Final-interaction gate

Before the final-channel response, submit read-only `pre_final` through this same GitHub transport. The server calls the admitted Source `tools/research_runtime_guard.py` gate. A successful freeze/review or a closed session is not PRE_FINAL permission. `status=SUCCEEDED` means evaluation completed; inspect `receipt.result.final_allowed` and `required_action`. When false, continue the required action. This gate grants no mathematical or execution authority.

- Formal completed/handed-off work: supply `run_request_id` (own successful open/resume), `completion_request_id` (own successful freeze or publish_checkpoint with release=true), and `parent_liveness`. Historical frozen/closed runs remain readable; do not reauthorize ended research. The server verifies native receipt/session/intent bindings and derives parent closure from current Source. Client COMPLETE cannot override it. Other formal states remain unsupported rather than being labeled complete.
- Driver control work without a formal run: supply its own `session_request_id` and `parent_liveness`. Optional `research_mode` must be `RESEARCH_DRIVER`. A Driver session already bound to a formal run must use the formal path.
- Maintenance without any issued research session in this logical conversation: supply `research_mode=CONTROL_PLANE_MAINTENANCE` and `parent_liveness`. Dropping an existing research binding cannot select this path.

`parent_liveness` preserves the actual original parent objective and requires these eight booleans: `parent_objective_complete`, `user_requested_stop_pause_review_or_wait`, `parent_hard_blocker`, `platform_or_tool_hard_limit`, `independent_safe_work_exhausted`, `same_action_repeated_without_state_change`, `supported_alternative_available`, `parent_state_recomputed_without_change`; also supply nonnegative integer `executable_next_actions`, with optional boolean `continuation_lease_active`. Do not invent a stop request or hard limit merely to obtain a final. Formal parent completion is independently Source-derived. An unknown closure returns `final_allowed=false` with its repair/check action. Record the Source pin and evaluated-state hash from the receipt.


## Portable research delivery (2026-09-23)

Follow [PORTABLE_RESEARCH_PROTOCOL.md](PORTABLE_RESEARCH_PROTOCOL.md) for scheduled research and task authoring. A missing execution environment does not prevent mathematical reasoning or automatically disable a schedule. Preserve actual pending native checks and publish a precise portable next question.

## Continuation repair additions (2026-09-23)

Public receipts expose `delivery_requirements`, without exposing private capability keys. If `continuation_seed.state=CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS`, read its `input_artifacts` through this conversation's successful artifact requests. Supply those request IDs and truthful `frontier_notes` to `continuation_prepare`, with `completed_units=[]`. Current task inputs are not evidence of a predecessor's completed work. Exact task/publication/predecessor CLAIM/comment binding, source firewalls and new claim/open admission remain required; an active owner cannot be displaced through this seed route.

A genuinely closed Researcher session that never claimed or opened work may use its own `session_request_id` plus truthful `parent_liveness` for `pre_final`. This preserves its Researcher/RA type and verifies fresh Source state. When another research action exists, the result is `final_allowed=false` with `next_research_route`: continue that action. The path does not declare research complete or relabel the session as maintenance.
