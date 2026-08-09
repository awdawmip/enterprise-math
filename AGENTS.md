# Enterprise Math agent operating rules

These are execution rules, not a research roadmap.

Before substantive mathematical or engineering research:

1. read `docs/RESEARCH_COMMON_SURFACE.en.md` (or the Chinese semantic pair);
2. read `research_common_surface.json`, especially its root-Lean import index, registered executable families, active interface alerts, and repository-tool index;
3. read `docs/RESEARCH_SCHEDULING_PROTOCOL.en.md`;
4. read `research_scheduler.json` and the live Research Dispatch Board Issue #240;
5. read `docs/RESEARCH_OWNER_ISOLATION.en.md`;
6. read `docs/PROBLEM_STATUS.en.md` and the relevant canonical theorem/result documents;
7. read the latest relevant entries in Research Relay Issue #82;
8. inspect overlapping executable specs/tests/Lean modules before inventing a parallel tool or theorem family;
9. when the work touches foundational language, notation, formulas, theorem/tool interfaces, or a flagged contradiction, read `docs/FOUNDATION_STEWARD_PROTOCOL.en.md` and relevant entries in Foundation Problem Set Issue #164.

Dispatch and handoff rules:

- an explicit current user task always overrides automatic dispatch;
- when a new research conversation has no user-selected task, reduce the live Issue #240 scheduler events against `research_scheduler.json`, select the highest-ranked eligible `HANDOFF_READY`/`READY` research task, and post a valid `CLAIM` before substantive task-specific work;
- after posting `CLAIM`, immediately re-read Issue #240 through the new comment and reduce the state again; begin research only if that `claim_id` is the winning live lease. If another claim won the race, do not work that task: select the next eligible task and claim again;
- a claim is a renewable lease, not permanent ownership; the default lease duration is defined by `research_scheduler.json`;
- `PROGRESS` and `HEARTBEAT` renew a live claim; prefer `PROGRESS` whenever there is a meaningful mathematical or engineering checkpoint to record;
- an unfinished session must end with `HANDOFF` containing the last progress reference and one concrete `next_action`; do not silently abandon a route;
- if an executor disappears, claim expiry returns the task to `NEEDS_DISPATCH`; another conversation may then claim it;
- `DONE` closes only the declared scheduler frontier; it does not by itself promote a theorem to canonical `main`;
- a partial or informal blocker is invalid. Only the complete four-field `HARD_BLOCK` defined by the scheduling protocol and scheduler may stop dispatch;
- runtime claim/heartbeat/handoff state belongs on Issue #240, not in theorem prose or branch history.

Scheduling rules:

- research on L1/L2/L3 is parallel by default;
- L1/L2/L3 owners may legitimately be behind `main`; do not whole-tree synchronize moving `main` into an owner merely to keep it current;
- canonical promotion freezes the exact proved owner payload and creates/reconciles a one-shot L4 integration from a current `main` snapshot when promotion begins;
- unrelated `main` movement during validation does not create a new replay generation; perform one final current-main combination gate before merge, and rework only for a genuine semantic/file conflict or failed final gate;
- synchronization-induced off-owner files are `SCOPE_DRIFT`; route them back to their real owner/source while preserving provenance rather than continuing the synchronization;
- `defer`, `consume from`, `owner moved`, `audit against`, or `replay after` are routing instructions, not stop conditions;
- only a complete explicit `HARD_BLOCK` may stop a route;
- `no_new_mathematics_during_replay=true` on an owner branch constrains only the identified replay slice; only L4 integration is globally `NO NEW MATHEMATICS`.

Knowledge propagation and promotion sync:

- reusable proved results and counterexamples must be relayed across affected routes with source commit, weakest assumptions, relation class, owner, and one action class: `INFORM`, `CONSUME`, `TEST`, or `HARD_DEPENDENCY`;
- canonical theorem families and reusable executable tool families must remain discoverable through `docs/RESEARCH_COMMON_SURFACE.*` and `research_common_surface.json`;
- a canonical promotion of a reusable theorem, formalization, executable family, negative boundary, or active interface alert must include a shared-surface delta, or explicitly justify why the delta is `N/A`;
- adding/removing a root import in `EnterpriseMath.lean` requires the same PR to update the exact `lean_root_imports` machine/human indexes;
- adding/removing a repository Python tool under `tools/*.py` requires the same PR to update the exact shared repository-tool machine/human indexes;
- `tools/check_research_common_surface.py` is a mechanical promotion gate: it checks declared-path existence, exact root-Lean imports, exact repository Python tools, active FQ-set agreement, and active-alert validity; it does not prove theorem truth or decide semantic reusability;
- do not duplicate a mother theorem merely to make a program branch self-contained;
- distinguish `CANONICAL_MAIN`, `LEAN_CHECKED_MAIN`, `PROVED_WIP_RELAY`, `EXECUTABLE_CHECKED`, and conjectural claims.

Foundation stewardship:

- the foundation steward maintains and verifies shared mathematical language/notation, formula integrity, theorem statements/status/interfaces, and reusable tool routing;
- mechanical or already-determined maintenance is fixed directly;
- a genuine unresolved contradiction, mathematical choice, missing hypothesis, cross-route incompatibility, high-value new structure, prior-art uncertainty, or tool/theorem sufficiency question is **not** solved by the steward;
- after minimum verification, such findings are posted to Issue #164 with a stable `FQ-*` ID for other researchers to claim;
- researchers answering an `FQ-*` item supply proof/counterexample/tool evidence and scope; the steward verifies before canonicalization.

If `hard_block = NONE`, continue the route's best available mathematical frontier rather than waiting for another branch, conversation, review, CI checkpoint, or integration replay. If the current executor cannot continue in this session, hand the route back to the scheduler instead of leaving it silently unstaffed.
