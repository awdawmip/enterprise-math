# Enterprise Math agent operating rules

These are execution rules, not a research roadmap.

Before substantive mathematical or engineering research:

1. read `docs/RESEARCH_COMMON_SURFACE.en.md` (or the Chinese semantic pair);
2. read `research_common_surface.json`, especially its root-Lean import index, registered executable families, active interface alerts, repository-tool index, and Foundation backflow pointers;
3. read `docs/RESEARCH_SCHEDULING_PROTOCOL.en.md`;
4. read `docs/RESEARCH_SCHEDULER_NONBLOCKING_STARTUP.md`; this later narrow addendum controls new-conversation startup, scheduler writes, and handoff liveness where the older scheduling protocol conflicts;
5. read `research_scheduler.json`; read the live Research Dispatch Board Issue #240 when it is available through a non-blocking read path;
6. read `docs/RESEARCH_OWNER_ISOLATION.en.md`;
7. read `docs/PROBLEM_STATUS.en.md` and the relevant canonical theorem/result documents;
8. read the latest relevant entries in Research Relay Issue #82 when available;
9. inspect overlapping executable specs/tests/Lean modules before inventing a parallel tool or theorem family;
10. when the work touches foundational language, notation, formulas, theorem/tool interfaces, a flagged contradiction, or a mature cross-route result that may change the common bottom layer, read `docs/FOUNDATION_STEWARD_PROTOCOL.en.md`, `docs/FOUNDATION_BACKFLOW_LOOP.en.md`, `foundation_backflow.json`, and relevant entries in Foundation Problem Set Issue #164.

Scheduler availability is never a startup gate. Failure to read Issue #240, failure to write scheduler events, an interactive connector/workflow approval requirement, rate limits, network errors, or tool unavailability are coordination degradations only. They must not stop a new conversation, stop an explicit user task, or be represented as a mathematical `HARD_BLOCK`.

Dispatch and handoff rules:

- an explicit current user task always overrides automatic dispatch;
- when a new research conversation has no user-selected task, reduce the live Issue #240 scheduler events if they are readable without blocking; otherwise select from the static canonical frontier in `research_scheduler.json` using the same ranking policy;
- **no scheduler write is required to start research**. A `CLAIM` is a best-effort coordination signal, not a startup transaction or permission gate;
- post `CLAIM` only when the Issue #240 write path is immediately available without interactive workflow/approval. If posting is unavailable, blocked, requires user interaction, or fails, continue the selected owner-scoped research unleased and do not retry merely to satisfy scheduler bookkeeping;
- when a `CLAIM` is successfully posted, immediately re-read Issue #240 through the new comment and reduce the state again; begin under that lease only if the `claim_id` is the winning live lease. If another claim won the race, select the next eligible task. This race rule applies only to successfully published claims;
- before publishing persistent results from an unleased session, refresh Issue #240 when practical. If an overlapping live lease now exists, preserve the work but route it as a non-conflicting owner-local result, `TEST`/Relay evidence, or another valid scope instead of discarding mathematics or blocking the conversation;
- a claim is a renewable lease, not permanent ownership; the default lease duration is defined by `research_scheduler.json`;
- `PROGRESS` and `HEARTBEAT` renew a live claim; prefer `PROGRESS` whenever there is a meaningful mathematical or engineering checkpoint to record;
- for a live claimed session, publish `HANDOFF` before exit when the write path is non-blocking. If scheduler writes are unavailable or require interaction, finish the user-facing response normally, preserve the concrete `next_action` in the available branch/PR/Relay/output, and allow the lease to expire naturally;
- scheduler event publication must never delay or block user-facing completion;
- if an executor disappears, claim expiry returns the task to `NEEDS_DISPATCH`; another conversation may then claim it;
- `DONE` closes only the declared scheduler frontier; it does not by itself promote a theorem to canonical `main`;
- a partial or informal blocker is invalid. Only the complete four-field mathematical/research `HARD_BLOCK` defined by the scheduling protocol and scheduler may stop dispatch. Scheduler/tool/workflow availability is never a valid `HARD_BLOCK`;
- runtime claim/heartbeat/handoff state belongs on Issue #240 when available, not in theorem prose or branch history.

Scheduling rules:

- research on L1/L2/L3 is parallel by default;
- L1/L2/L3 owners may legitimately be behind `main`; do not whole-tree synchronize moving `main` into an owner merely to keep it current;
- canonical promotion freezes the exact proved owner payload and creates/reconciles a one-shot L4 integration from a current `main` snapshot when promotion begins;
- unrelated `main` movement during validation does not create a new replay generation; perform one final current-main combination gate before merge, and rework only for a genuine semantic/file conflict or failed final gate;
- synchronization-induced off-owner files are `SCOPE_DRIFT`; route them back to their real owner/source while preserving provenance rather than continuing the synchronization;
- `defer`, `consume from`, `owner moved`, `audit against`, or `replay after` are routing instructions, not stop conditions;
- only a complete explicit mathematical/research `HARD_BLOCK` may stop a route;
- `no_new_mathematics_during_replay=true` on an owner branch constrains only the identified replay slice; only L4 integration is globally `NO NEW MATHEMATICS`.

Knowledge propagation and promotion sync:

- reusable proved results and counterexamples must be relayed across affected routes with source commit, weakest assumptions, relation class, owner, and one action class: `INFORM`, `CONSUME`, `TEST`, or `HARD_DEPENDENCY`;
- canonical theorem families and reusable executable tool families must remain discoverable through `docs/RESEARCH_COMMON_SURFACE.*` and `research_common_surface.json`;
- a canonical promotion of a reusable theorem, formalization, executable family, negative boundary, or active interface alert must include a shared-surface delta, or explicitly justify why the delta is `N/A`;
- adding/removing a root import in `EnterpriseMath.lean` requires the same PR to update the exact `lean_root_imports` machine/human indexes;
- adding/removing a repository Python tool under `tools/*.py` requires the same PR to update the exact shared repository-tool machine/human indexes;
- `tools/check_research_common_surface.py` is the mechanical shared-surface/control-plane gate: it checks declared-path existence, exact root-Lean imports, exact repository Python tools, active FQ-set agreement, active-alert validity, and Foundation FQ-to-scheduler backflow-link integrity; it does not prove theorem truth or decide semantic reusability;
- when a mature result exposes a weaker primitive, minimal sufficient state, minimal repair, reusable tool, cross-route invariant, negative boundary, or layering law, emit a Foundation Feedback Packet or route the finding to the steward rather than leaving it only in the source program;
- do not duplicate a mother theorem merely to make a program branch self-contained;
- distinguish `CANONICAL_MAIN`, `LEAN_CHECKED_MAIN`, `PROVED_WIP_RELAY`, `EXECUTABLE_CHECKED`, and conjectural claims.

Foundation stewardship and backflow:

- the foundation steward maintains and verifies shared mathematical language/notation, formula integrity, theorem statements/status/interfaces, reusable tool routing, and the research-to-foundation backflow surface;
- compress serious backflow candidates using the Foundation Feedback Packet in `docs/FOUNDATION_STEWARD_PROTOCOL.*`;
- classify each candidate as `DIRECT_FOUNDATION_MAINTENANCE`, `FOUNDATION_QUESTION`, or `APPLICATION_LOCAL_OR_NOT_READY`;
- mechanical or already-determined maintenance is fixed directly;
- a genuine unresolved contradiction, mathematical choice, missing hypothesis, cross-route incompatibility, high-value new structure, prior-art uncertainty, or tool/theorem sufficiency question is **not** solved by the steward;
- after minimum verification, such findings are posted to Issue #164 with a stable `FQ-*` ID and linked through `foundation_backflow.json` to the appropriate scheduler task;
- the static FQ-to-task link is durable recovery metadata even if live #240 reads/writes are temporarily unavailable; scheduler availability never blocks the research itself;
- mathematical FQ research runs in the compatible L1/L2/L3 research scope; steward verification/integration remains governance and must not impersonate theorem ownership;
- a researcher RETURN, scheduler `DONE`, and steward `ACCEPTED` are distinct states and none is canonical by itself;
- after a returned FQ answer, the steward independently verifies before any latest-main integration; only a gated merge to source `main` permits `CANONICALIZED` status and common-surface/global-knowledge propagation;
- application elegance, WIP status, or a physical interpretation alone never justifies foundation promotion.

If `hard_block = NONE`, continue the route's best available mathematical frontier rather than waiting for another branch, conversation, review, CI checkpoint, integration replay, scheduler event, connector workflow, or GitHub write. If the current executor cannot continue in this session, preserve a concrete continuation point and use scheduler handoff when available instead of turning scheduler availability into a stop condition.
