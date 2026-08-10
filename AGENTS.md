# Enterprise Math agent operating rules

These are execution rules, not a research roadmap.

## Remote-liveness rule comes first

Read and follow `docs/GITHUB_INTERACTION_BUDGET.md` before expanding repository/Issue/PR preflight. It is the later narrow authority for **when GitHub must be touched**. Older documents remain authoritative for mathematical ownership, status, scheduler semantics, Foundation stewardship, and final gates, but their long preflight lists must not be executed as an unconditional sequence of remote calls.

Core invariant:

> **Research is the hot path. GitHub is a sparse persistence and integration boundary.**

For an explicit current user task, start from the smallest sufficient packet:

1. `AGENTS.md` / `docs/GITHUB_INTERACTION_BUDGET.md` if not already loaded;
2. one common router — normally `research_common_surface.json` **or** `docs/RESEARCH_COMMON_SURFACE.en.md`, not both by default;
3. the exact relevant canonical theorem/spec/code/test/Lean files needed to begin.

Then work. Do not load scheduler, Issue #240, Relay #82, `PROBLEM_STATUS`, owner-isolation, Foundation surfaces, or Lean diagnostic governance unless the current task actually needs that surface. The explicit-task startup soft budget is at most three routine Enterprise Math GitHub reads before substantive work begins.

Use local checkout/search/tests when available. In connector-only environments, fetch a minimal task packet once and reuse it. Do not refetch unchanged blobs/SHAs/PRs/Issues in one uninterrupted execution phase.

## Conditional routing surfaces

Load these only when their function is material:

- `docs/RESEARCH_SCHEDULING_PROTOCOL.en.md`, `research_scheduler.json`, Issue #240: auto-dispatch, scheduler reconciliation/event semantics;
- `docs/RESEARCH_SCHEDULER_NONBLOCKING_STARTUP.md`: scheduler/CI/review liveness or when those paths are actually used;
- `docs/RESEARCH_OWNER_ISOLATION.en.md`: branch creation/reconciliation, scope audit, or promotion;
- `docs/PROBLEM_STATUS.en.md`: numbered status/canonical scope/promotion;
- latest relevant Research Relay #82 entries: when consuming relevant WIP or publishing a reusable cross-route result;
- `docs/LEAN_DIAGNOSTIC_LIVENESS.md`: Lean theorem diagnosis/import/root-registration failures;
- `docs/TEST_DISCOVERY_LIVENESS.md`: test discovery, test-file lookup, or repeated test-related GitHub operations;
- `docs/FOUNDATION_STEWARD_PROTOCOL.en.md`, `docs/FOUNDATION_BACKFLOW_LOOP.en.md`, `foundation_backflow.json`, Issue #164: foundation-facing work, flagged contradictions, or mature backflow candidates.

Inspect overlapping executable specs/tests/Lean modules before inventing a parallel tool or theorem family, but only within the task-relevant owner/interface surface. **Do not satisfy this rule by recursively traversing the GitHub repository tree.** Use known paths, the local checkout/index, or one targeted lexical lookup.

## GitHub publication cadence

L1/L2/L3 research is `REMOTE_SILENT` between semantic checkpoints:

- no routine remote write for proof search, small edits, import diagnosis, heartbeat bookkeeping, PR-body narration, workflow checking, or chasing moving `main`;
- publish when a coherent semantic checkpoint, handoff, loss-risk boundary, user-requested publication, or frozen promotion payload exists;
- batch related changes at the checkpoint; remote publication need not mirror local commit frequency;
- one bounded owner generation normally has one branch and at most one **Draft PR**;
- research PRs stay Draft by default. Do not toggle ready-for-review merely to get CI;
- emit at most one coordination packet per checkpoint by default instead of duplicating the same progress across scheduler, Relay, PRs, and downstream Issues.

Canonical promotion is serialized in the control plane as well as mathematically: default to **one active ready-for-review L4 promotion lane**. Other mature payloads freeze/queue until that lane is available. Promotion performs one current-main admission refresh, one conflict snapshot, one frozen-head validation cycle, then one final current-main combination check when merge is actually attempted.

## Scheduler and handoff

- an explicit current user task always overrides automatic dispatch;
- scheduler availability is never a startup gate;
- with no user-selected task, select from live Issue #240 when available non-blockingly or from static `research_scheduler.json` otherwise;
- no scheduler write is required to start research. `CLAIM`, `PROGRESS`, `HEARTBEAT`, `HANDOFF` are best-effort coordination signals;
- post scheduler events only when the write path is immediately available and the event adds real coordination value; do not retry solely for bookkeeping;
- a successfully published `CLAIM` still obeys the live-lease race/reduction rule;
- if an unleased session later sees an overlapping live lease, preserve the mathematics and route it as non-conflicting owner-local/Relay `TEST` evidence rather than discarding work or blocking the user;
- `DONE` closes only the scheduler frontier; it does not promote theorem truth;
- only the complete four-field mathematical/research `HARD_BLOCK` (`missing_object`, `owner`, `necessity`, `unblock_condition`) may stop a route. Scheduler/tool/workflow availability is never a `HARD_BLOCK`.

## Scheduling and owner isolation

- research on L1/L2/L3 is parallel by default; canonical promotion is serialized;
- L1/L2/L3 owners may legitimately be behind `main`; never whole-tree synchronize moving `main` merely to stay current;
- canonical promotion freezes the exact proved owner payload and replays only that payload on a fresh current-main L4 integration;
- unrelated `main` movement during validation does not create a new replay generation; only a genuine semantic/file conflict or failed final gate requires rework;
- synchronization-induced off-owner files are `SCOPE_DRIFT`; route them back to their real owner/source while preserving provenance;
- `defer`, `consume from`, `owner moved`, `audit against`, `replay after` are routing instructions, not stop conditions;
- `no_new_mathematics_during_replay=true` on L1/L2/L3 constrains only that replay slice; L4 integration is globally `NO NEW MATHEMATICS`.

## CI, workflow, review, and concurrent-governance liveness

- workflow/review status is an observation, never a wait primitive;
- for an unchanged commit/run/concurrent-PR set, take at most one routine status snapshot in one uninterrupted execution phase;
- `queued` / `pending` / `requested` / `in_progress` becomes `CI_PENDING`; stop checking that unchanged object;
- never sleep/backoff/retry/recursively refresh solely to see whether status changed;
- `Reviewing Concurrent Governance Pull Requests` is a one-snapshot conflict audit, not a loop;
- recheck only for a genuinely new SHA/run/event, explicit user refresh request, or a later turn where current status is again necessary;
- required CI/review may defer the merge/promotion action but never research or user-facing completion;
- a newly observed failure permits one targeted diagnostic/log pass, not renewed polling.

## Test discovery and test-execution liveness

- `Inspecting Repository Tree for Test Files` is **not** a normal research step; recursive GitHub tree traversal for tests is prohibited by default;
- the canonical Python test root is `tests/`, and the canonical full-suite command is `PYTHONPATH=src python -m unittest discover -s tests -v` as declared by `.github/workflows/quality.yml`;
- if a target source/test path is already known, use it directly; do not list the repository or `tests/` again;
- when a local checkout exists, use local `find`/`rg`/IDE index/unittest discovery; do not mirror discovery through GitHub;
- in connector-only execution, if the companion test filename is genuinely unknown, allow **at most one targeted repository search** using the exact module/theorem/tool identifier; no recursive tree enumeration and no series of broad `test/tests/unittest/pytest` searches;
- do not fetch many test files merely to learn the test inventory;
- full-suite execution belongs to a bounded validation/promotion boundary, not after every small research edit;
- if broader tests have not run, record `LOCAL_TEST_PENDING`, `FULL_SUITE_PENDING`, or `CI_PENDING` rather than expanding into remote exploration;
- detailed authority: `docs/TEST_DISCOVERY_LIVENESS.md`.

## Lean diagnostic liveness

- diagnose missing imports/tactics/identifiers/instances on the changed owner-local module first;
- `Adding Imports for <module> Diagnosis` is bounded, not open-ended;
- do not repeatedly add umbrella imports or perform `add import -> root build -> add import -> root build` cycles;
- after one import adjustment for the same unresolved missing object, inspect the new concrete compiler error before changing imports again;
- do not register a module in `EnterpriseMath.lean` merely to test local compilation;
- validation ladder: local module -> immediate family if needed -> root registration/common-surface update -> one final warnings-fatal root/repository Lean gate;
- if local compilation is unavailable, preserve exact evidence and mark verification pending instead of accumulating speculative imports/full-root rebuilds;
- pending Lean CI uses the same one-snapshot/no-polling rule.

## Knowledge propagation and promotion sync

- reusable proved results/counterexamples cross routes with source commit, weakest assumptions, relation class, owner, and one action class: `INFORM`, `CONSUME`, `TEST`, or `HARD_DEPENDENCY`;
- canonical theorem/executable families remain discoverable through `docs/RESEARCH_COMMON_SURFACE.*` and `research_common_surface.json`;
- canonical promotion of a reusable theorem/formalization/executable/negative boundary/interface alert includes a shared-surface delta or explicit `N/A` rationale;
- adding/removing a root import in `EnterpriseMath.lean` updates the exact `lean_root_imports` human/machine indexes in the same promotion;
- adding/removing `tools/*.py` updates the exact shared repository-tool indexes in the same promotion;
- `tools/check_research_common_surface.py` is a mechanical routing/control-plane gate, not a proof of theorem truth;
- mature weaker primitives/minimal repairs/reusable tools/cross-route invariants/negative boundaries/layering laws should emit one Foundation Feedback Packet when appropriate;
- do not duplicate a mother theorem merely to make a program branch self-contained;
- distinguish `CANONICAL_MAIN`, `LEAN_CHECKED_MAIN`, `PROVED_WIP_RELAY`, `EXECUTABLE_CHECKED`, and conjectural claims.

## Foundation stewardship

- the foundation steward verifies shared language/notation/formula integrity/theorem interfaces/tool routing/backflow; it does not seize mathematical ownership;
- classify backflow candidates as `DIRECT_FOUNDATION_MAINTENANCE`, `FOUNDATION_QUESTION`, or `APPLICATION_LOCAL_OR_NOT_READY`;
- mechanical determined maintenance is fixed directly; unresolved mathematical choices/contradictions/missing hypotheses/high-value structures/prior-art uncertainty become `FQ-*` items after minimum verification;
- static FQ-to-task links remain durable recovery metadata even if Issue #240 is unavailable;
- researcher RETURN, scheduler `DONE`, steward `ACCEPTED`, and canonical main are distinct states;
- only gated source-main integration permits `CANONICALIZED` status and common-surface/global-knowledge propagation;
- application elegance, WIP status, or physical interpretation alone never justifies foundation promotion.

## Completion rule

If `hard_block = NONE`, continue the best mathematical frontier rather than waiting for a branch, conversation, review, CI checkpoint, integration replay, scheduler event, connector workflow, GitHub write, repeated test discovery, or repeated Lean rebuild.

The default lifecycle is:

`small task packet -> remote-silent research -> semantic checkpoint batch -> Draft owner record -> frozen payload queue -> one L4 lane -> final gates -> main`.
