# Scheduled research: autonomous execution and checkpoint recovery

[Chinese](AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md)

Status: ACTIVE. This document governs execution orchestration; it adds no task admission, mathematical conclusion, or role authority. Research evidence is the primary deliverable. Status descriptions, support requests, and polling are not research progress by themselves.

## Responsibilities

Keep the existing schedules for the three Researcher jobs, one Driver job, and one control-maintenance job. Role counts do not replace executable paths:

| Responsibility | Required action in each run |
| --- | --- |
| Researcher | First recover this conversation's unfinished operations and authorized frontier, actually advance the smallest research unit, and persist verifiable evidence and the next step. Claim a new task only when there is no existing work. |
| Driver | Consume frozen Results and the exact review set. Under current authority, complete review, reference passes, synthesis, follow-up materialization, or scope closure, then continue to the next lawful unit. |
| Control maintenance | Own recovery orchestration, interface defects, and task runtime state. Route each blocker to an actual responsible path, repair it or deliver an executable continuation packet, and verify that the affected path reaches its next real state. |

Two types of reference pass do not require finding two additional reviewers. When sufficient canonical reviews already exist, do not add a third review merely to repair transport. Authors/contributors must not use a new identity to independently review their own results; disclose shared context truthfully.

## Entry to each run

1. Reuse a still-valid account knowledge-base read lease and unchanged files. Read the necessary entries according to current control authority, P000, and the actual role. Expand only material needed for the next action.
2. Preserve the stable ID of this logical conversation; compaction within the same conversation does not require a new identity. First inspect service `status` and public operation contracts; read `recovery_status` first when available. That entry lists only local request/session pointers for this subject. It proves neither current Source ownership nor conversation liveness, and does not submit requests itself.
3. Reconcile unknown side effects and unfinished transactions first, recover existing work second, and use canonical dispatch last. After context loss, do not issue a new CLAIM, repeat an upload/publication, or register another identity from memory.
4. A new conversation uses its own real execution identity and continues through the current Task's Source continuation packet. A logical conversation's ability to recover its own service session does not let an arbitrary new conversation borrow another conversation's private capability.

## Real conversations and logical identities

One stable `conversation_id` corresponds to one real execution conversation. Compaction within that conversation preserves the ID. A real conversation created by a new chat, copy, fork, or another scheduled job cannot inherit its identity from historical prose. When a platform thread/chat ID is available, it may form the stable logical identifier. Otherwise this conversation generates and preserves its own unique identifier, without copying a template example or another conversation's identifier. Scheduled prompts must not preset the same execution conversation ID for several real conversations.

If two real conversations have already claimed the same logical ID, treat the old ID/session/request only as historical provenance awaiting verification. Do not determine ownership from creation order, task title, or the last respondent; both conversations first stop role-bound writes that depend on the shared identifier. Each preserves its real platform ID, prior contributions, and unpublished results, then resolves or allocates a separate logical identifier and local role ID belonging to its real conversation under the identity protocol. This step does not require first obtaining a CLAIM, ownership of the old session, or Source takeover approval. Formal continuation still requires verification under the current Source continuation contract. Do not rebind, close, revoke, or impersonate an old session whose ownership is unresolved. Correcting identity does not clear an existing platform denial or justify retrying a denied action with another ID. A new identifier grants no CLAIM, takeover right, or independent-review qualification.

Registration proceeds through `RESOLVE_OR_ALLOCATE_ROLE_IDENTITY` first, then registration of one's own identity and research activity through an actually available and permitted write path. If that path is unavailable, explicitly preserve one's local role ID, real conversation provenance, all prior contributions, and `REGISTER_PENDING` / `SYNC_DEBT`. This local ID is not a service-issued researcher/session ID. Do not borrow the old E267A2 whose ownership is unresolved, or invent a service ID, session key, or successful registration receipt. Reconcile an unresolved original request under its original request_id first. Handle an explicit denial within its specific action boundary; a semantic checkpoint is not permission to bypass it by retrying.

When the native control path is actually available and the call is permitted, request `session_start` under the public contract using one's own conversation_id and truthful contribution history; the service issues the real identity. `task_id` is optional, and identity registration does not require a prior CLAIM. Formal continuation obtains a currently valid `continuation_prepare`, a new CLAIM, and open, in that order; every step remains subject to current Source, ownership, and freeze boundaries. Successful registration or prepare is not execution authorization. For portable research permitted without native write access, see the next section; do not describe pending registration as an already registered Research-Activity or formal task execution.

## Recovery decisions

| Verified state | Next action |
| --- | --- |
| QUEUED/RUNNING/POSTING | Read back the original request; do not resubmit. |
| OUTCOME_UNKNOWN/RECONCILE | Reconcile the original request_id and verify actual Source effects; do not resend the original write under another ID. |
| ADMITTED_NOT_SUBMITTED | Recover the existing admission using the original request's receipt; do not create the same logical operation again. |
| One's own CLAIM succeeded, but open has not occurred | Request open using the original claim_request_id; first check current native authorization. |
| One already has open/resume | Use recovery pointers and current authorization checks; resume with a new generation when required, without claiming the task again. |
| Files uploaded but unpublished | Use the request_id of the completed final chunk; verify files and destination, then publish the existing evidence. |
| Checkpoint published | Consume exact Source bytes, completed/no-repeat units, and the next action; reconcile an unknown receipt first. |
| Lawfully released or lease expired | A newly authorized session prepares through canonical continuation, wins a new CLAIM, then opens; preserve the original task and highest valid frontier. |
| FROZEN/awaiting review | Route to the currently lawful Driver; do not reclaim the frozen mathematical unit. |
| Closed or fenced | An old local receipt is not write authority; use a new identity and current canonical continuation, without reusing the old run. |
| Validation explicitly rejected before admission, with no native effect | Read the returned operation_contract, correct the fields, then submit one new request; preserve the original failure record. |

The capabilities exposed to ordinary Chat and standard MCP are determined by current `status`. Do not invent parameters when an ordinary interface lacks a capability. RESUME after canonical release/lease expiry is an automatic continuation path that does not require contacting the former researcher. Early takeover of a live claim still requires genuine inactivity evidence accepted by Source and predecessor CAS. Merely having no service requests for 600 seconds, or seeing a UI spinner, does not prove that the previous conversation stopped.

Before a platform deadline or real handoff, the current owner first persists results and a recovery packet. Use canonical `publish_checkpoint(release=true)` when a handoff is appropriate. When preparing to freeze, retain `release=false` and complete the actual Result path. Normal execution does not renew leases merely to poll; mark all unpersisted material UNKNOWN.

## Separating reads and writes when tools fail

First distinguish reading current state, preserving evidence, and obtaining/using execution authority. Do not turn an invisible tool into a permanent task limitation. When native `em_status` is actually provided, use that read-only entry directly. Without it, first use the existing GitHub connection to read current Source, existing original requests, and receipts. Reading these existing materials does not require creating another Issue and grants no current session/claim authorization. Ordinary `status/recovery_status` transported through an Issue request still entails an Issue-creation write; use it only when that transport is currently permitted and no relevant explicit denial exists.

| Actual failure boundary | Actions that may continue |
| --- | --- |
| Tool absent, or unsupported tool name/parameters | Select an actually available and authorized entry under the current public contract. Read-only diagnosis may read Source/original receipts directly; do not invent tools, parameters, or credentials. |
| Service explicitly rejects schema/fields before admission, with no side effects confirmed | Correct the fields identified by the returned contract, then submit once more; do not interpret schema validation rejection as a platform safety denial. |
| Timeout, disconnection, or incomplete response; whether a write occurred is unknown | Preserve the original request_id and first read its receipt and actual Source. Reconcile only when a native unresolved request exists; do not resend the same logical write under another ID. |
| Platform/host explicitly denies an action or requires approval not yet obtained | Preserve the denied action, reason, and source; do not replay it through another tool, channel, identity, or wording. Without direct error output, record only that the original conversation reported a denial, not that it was independently verified. |
| A required computation/verification capability has been established but is currently unavailable | Freeze inputs, portable code/evidence, and expected checks; record checks not yet executed. Continue other research units within existing authorization that do not depend on that capability, without marking unrun checks PASS. |

An explicit denial blocks only the actions it covers; it does not automatically establish that all research or persistence is unavailable. Within the same scientific question explicitly authorized by the user, use this conversation's own local role identity to continue portable proofs, literature verification, counterexamples, or certificate construction, without making native session/CLAIM/run acquisition a prerequisite for reasoning. When the write path is unavailable, truthfully preserve `REGISTER_PENDING` / `SYNC_DEBT` and do not claim research activity is registered. These new original materials are research awaiting registration, at `UNREVIEWED / NOT_ADMITTED` strength. They are not role-bound formal task execution, a canonical checkpoint, a Result, an accepted review, or an admitted frontier. Formal writes, continuation, and admission still require their respective current authority and real receipts; do not fabricate CLAIMs, restore expired authorization, or substitute for independent review. If an explicit denial covers the research action itself, respect that specific boundary. Mere tool absence, unresolved ownership of an old identity, or denial of one particular write cannot be expanded into stopping all mathematics.

When preserving material in already authorized Source/knowledge-base/file artifacts, state authorship and contribution provenance, the immutable frontier, unresolved requests, unexecuted checks, and truthful statuses such as `UNREVIEWED / NOT_ADMITTED`. Neutral preservation grants no session, claim, Research-Activity, review, or mathematical admission, and does not perform another conversation's denied registration. If remote writes are also disallowed, deliver complete reusable artifacts and explicit pending destinations; do not report prepared prose as already written back.

When the same denial signature has no state change, do not replay equivalent writes or send identical blocker notifications every run. Recheck the applicable boundary after new user authorization, platform approval/availability changes, or a substantively different, safer permitted action becomes available. New authorization still does not override a platform prohibition. Preserve the existing scheduled jobs and a minimal recovery packet so the next run resumes from the highest verified frontier, without requiring the user to say "continue" or creating a duplicate scheduler.

## Discoverable continuation packets

In an existing authorized Source checkpoint, Result/review, or control-maintenance handoff, record the parent objective, Task/publication, input/authority pins, highest immutable frontier, completed and no-repeat units, smallest unfinished unit, exact next action, logical conversation_id, real session/claim/run, unresolved request_id and original receipt Issue, support problem, and responsible path. Do not store private keys or establish a second task registry.

Each new run must consume these existing records first. After completing a semantic unit, continue within the same run whenever the parent objective remains open and a lawful next action exists. Do not require another user "continue" or suspend scheduled jobs unilaterally. If the platform forcibly ends execution, recover in the next run; prompts do not promise an immortal model process.

## Acceptance of control-maintenance work

Create only one traceable disposition per failure signature, recording the actual failure boundary, original request, responsible path, concrete next action, and validation condition. A repaired interface must be verified by the affected business flow reaching its next real state. Editing prompts or closing a support issue does not complete recovery. If a task is temporarily unexecutable, continue other executable research under current authority while preserving that task's frontier and recovery conditions. Missing environment capabilities cannot be rewritten as mathematical conclusions or permanent task-admission gates.

Do not repeat notifications when ordinary state is unchanged; report research results, substantive repairs, failures, or actions genuinely required from the user. Preserve existing scheduling frequency and user notification settings.

Related entries: [Ordinary Chat control](CHATGPT_ORDINARY_CONTROL.en.md), [Driver operations contract](DRIVER_FLOW_OPERATIONS.md), [Cross-conversation continuation](CONTINUE_RESEARCH.en.md), [Portable research delivery](PORTABLE_RESEARCH_PROTOCOL.md).

## When old staging blocks a successor identity (after discovering 0.6.6 capabilities)

Use actual `status` and `operation_contracts`; this section does not prove service deployment. Do not loop between "new identity rejected" and "close rejected by unpublished uploads," or rebind/delete old evidence. The same real logical conversation still bound to the old service session first reconciles its original unresolved requests. When no current active CLAIM/run or similar blocker exists, request `session_preserve_staging` under the public contract. Control maintenance orchestrates this recovery only; it does not operate a research identity by borrowing an old conversation_id/capability.

A neutral archive preserves complete/incomplete staging and original request provenance without loss. It is not a task checkpoint, Result, review, current task input, or mathematical progress; original staging rows are not rebound. After reading back the original successful request receipt and the immutable manifest identified by `manifest_read`, independently perform one's own `session_close`, then `session_start` a new service identity within the same real logical conversation, preserving contribution history. Preservation does not automatically close/revoke authority. For UNKNOWN, reconcile only the original request. A genuinely new conversation uses its own conversation_id, without copying an old identifier.

After recovery, first consume verified Source checkpoints. For native frontiers such as D24, `continuation_prepare` uses only the new successful packet's `packet_request_id` and `reason`, without rewriting the frontier. For initial-publication input seeds such as P11, read the exact seed pin and retain `completed_units=[]`; place prior parent results in provenance/no-repeat units. Without a seed, do not substitute repeated parent Result reads for repair. Neither path claims/opens early or recomputes completed research.

Acceptance must record separately: completed neutral preservation, one's own close/new identity and inherited contributions, successful continuation_prepare for the real task, and subsequent lawful execution recovery. Archive completion, document publication, or support-ticket closure alone must not be described as recovered research or accepted results.
