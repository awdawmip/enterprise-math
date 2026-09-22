# NFHJPA last-progress artifact / Driver PRE_FINAL recovery

Status: `ACTIVE_RECOVERY_RECORD / CONTROL_PLANE_ONLY / NO_NEW_MATHEMATICS`
Scope: `Enterprise Math`
Observed-main: `0dceb5418c811981835e79c007accd6c949f0c6c`

This record does not create or release a CLAIM, grant Researcher/Driver authority, write a Result/review/follow-up, or change mathematical status. It records two independently verified control-path stalls and the smallest safe recovery actions.

## A. NFHJPA typed continuation cannot authenticate the current last-progress artifact

Task: `RS-NATIVE-FILAMENT-POSTAUDIT-HYPERBOLA-JOUKOWSKI-EXTERNAL-PRIOR-ART-AUDIT`
Publication: `TP2-39ACFC69F85D8661CFBF`

Verified ordinary-control chain from logical conversation `chat-em-r11-20260922-3db9ba0d`:

- exact continuation request `cont-r11-20260922-3db9ba0d-09` (bridge Issue #394) completed `SUCCEEDED`;
- the continuation projected `HANDOFF_READY / NEEDS_DISPATCH`, no live claim, predecessor claim `CLM-NFHJPA-20260922-0658-1A7C9E`, predecessor researcher `EM-NFHJPA-5B519F`;
- `persisted_checkpoint.state=NOT_FOUND`, `durable_frontier=null`;
- `last_progress_ref=driver_reviews/NATIVE_FILAMENT_POSTAUDIT_HYPERBOLA_JOUKOWSKI_INDEPENDENT_REPLICATION_DRIVER_REVIEW_20260829.md` is a bare repository-relative path;
- the packet's authenticated `source_artifacts` / frontier template contain the taskbook and publication record, but the bare `last_progress_ref` is not exposed as an immutable artifact candidate;
- artifact request `artifact-r11-20260922-3db9ba0d-12` (Issue #400) for that last-progress path was rejected `ARTIFACT_NOT_IN_CONTINUATION_PACKET`;
- typed continuation request `contprep-r11-20260922-3db9ba0d-15` (Issue #403), even with the allowed taskbook artifact, was rejected `CHAT_AUTHENTICATED_LAST_PROGRESS_ARTIFACT_REQUIRED`.

Current Source behavior was rechecked on `0dceb5418c811981835e79c007accd6c949f0c6c`: `continuation_packet(...)` copies `runtime.last_progress_ref` into `immutable_external_artifact_candidates` only when `_fixed_source_candidate(...)` can parse it as an immutable GitHub blob URL or `file@<40hex commit>` form. A bare relative path is therefore retained in `last_progress_ref` but is not independently readable through the ordinary-control `artifact` allowlist.

Classification:

- exact continuation projection and task/publication pins: `VERIFIED_COMPLETE`;
- predecessor mathematical reconstruction: preserve provenance / `DO_NOT_REPLAY` for this external-prior-art task;
- external prior-art classification required by this task: `UNFINISHED`;
- ordinary-control typed continuation preparation: `UNFINISHED`;
- bare authenticated `last_progress_ref` versus artifact-authentication requirements: `CORRUPT_OR_CONFLICTED` at the control/adapter compatibility layer only; no mathematical bytes are declared corrupt.

Recovery rule:

1. Do not retry generic fresh `prepare`, and do not call this `NO_DISPATCH`, capability mismatch, or research failure.
2. Do not repeatedly request the same disallowed last-progress artifact or resubmit the same failing `continuation_prepare` while the packet shape is unchanged.
3. Refresh the exact continuation once in a new authorized Researcher session. If the packet now exposes the last-progress evidence as an authenticated immutable artifact, read it and continue through `continuation_prepare -> claim -> open`.
4. If the packet remains unchanged, leave the task unclaimed and preserve this exact adapter/source compatibility blocker. A source/adapter fix must make the authenticated last-progress evidence consumable without inventing a commit, weakening artifact gates, or replaying predecessor mathematics.
5. A newly registered Researcher session by itself is not a claim and must not be preempted. At the time of this record, a new TASK_RESEARCH session `MCP-88935ccecac24f0e96497c284122d6dd` / `EM-DIRECT-3186A7` had been registered on current main but had not yet established task ownership in the evidence reviewed here.

## B. Driver PRE_FINAL returned FINAL_FORBIDDEN but the client stopped before the required routing recompute

Verified Driver conversation: `chatgpt-driver-auto-20260922-t5-7f8c2a1e`.

- session registration completed for Driver session `MCP-ee7f8ca792dd4642802329de6433d958`;
- `driver_activate` completed and produced Driver `EM-DVR-064EA4` with source-backed authority record `DA-9A29BE2010141AA4936C`;
- `pre_final` request `prefinal-session-20260922T1140Z-7f8c2a1e` completed with `final_allowed=false` and `required_action=RECOMPUTE_PARENT_ROUTING_ONCE`;
- no later operation in that logical Driver conversation was found that performed the required recompute before the conversation stopped.

Classification:

- Driver session/activation: `VERIFIED_COMPLETE` for that historical execution conversation;
- requested PRE_FINAL evaluation: `VERIFIED_COMPLETE`;
- parent routing recompute required by PRE_FINAL: `UNFINISHED`;
- this is a client control-flow stall, not a review-authority failure and not evidence that the review queue is empty.

Recovery rule:

1. A future Driver run uses its own new real session/authority; it does not borrow this historical session.
2. Consume the durable PRE_FINAL receipt as provenance that the prior run ended nonterminally.
3. Recompute current Driver routing once from current source: current review/follow-up inventory and the exact selected continuation/governance action.
4. If current state already contains a lawful review/follow-up produced by another Driver, consume it and do not duplicate it.
5. PRE_FINAL with `final_allowed=false` is never a completion boundary. The client must execute the returned `required_action` before any new PRE_FINAL/final attempt, unless a genuine external blocker is then established.

## Do not repeat

- do not redo accepted predecessor mathematics merely to repair NFHJPA control routing;
- do not create a Researcher CLAIM until the typed continuation evidence gate is satisfiable;
- do not fabricate an immutable source binding for the bare last-progress path;
- do not reuse an old Driver or Researcher session after its execution conversation is stale;
- do not treat wrapper receipt success as target-operation success;
- do not treat PRE_FINAL transport success as permission to finalize when native `final_allowed=false`.
