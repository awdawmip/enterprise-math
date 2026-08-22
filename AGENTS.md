# Enterprise Math agent operating router

Status: `ACTIVE / STABLE EXECUTION ROUTER / V2.4`

`AGENTS.md` is a **current execution router**. It is not a theorem catalog, project history, old-route index, or archive.

## 1. Mode resolution

Current explicit user instruction controls scope.

Current research modes:

- `EM_FREE_RESEARCHER` -> `FREE_AXIOM_DISCOVERY`;
- explicit user task / Driver handoff / approved taskbook / scheduler dispatch -> `TASK_RESEARCH`;
- explicit Driver activation -> `RESEARCH_DRIVER`.

Exact role authority:

- `research_architecture.json`;
- `research_role_policy.json`;
- `research_identity_state_machine.json`.

## 2. Identity

Resolve the visible role identity before substantive work:

- researcher -> `Researcher-ID`;
- Driver -> `Driver-ID`.

Identity registration is nonblocking.

## 3. FREE_AXIOM_DISCOVERY

FREE Phase A receives the **primitive substrate**, not the current-result catalog and not a suggestion menu.

Canonical substrate router:

`definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md`.

Before candidate freeze:

- do not preload the general current-result router;
- do not preload current task/route/coordination/recent-history context;
- do not inherit unrelated `WORKING_TRUTH`;
- do not let existing tools, representations, filenames or current research vocabulary choose the question;
- do not supply suggested questions or discovery-lens menus;
- use generic exclusion categories rather than naming hidden current results.

Freeze:

`FOUNDATION_FOR_DISCOVERY != CATALOG_OF_CURRENT_ACHIEVEMENTS`.

`NO_DEFAULT_DISCOVERY_LENS_MENU`.

Candidate lifecycle:

`research_axiom_candidate_state_machine.json`.

## 4. TASK_RESEARCH hot start

For a selected task:

1. this router if not already loaded;
2. the **exact task entry**;
3. the first exact dependency required to begin;
4. work;
5. expand only when a concrete dependency is triggered.

Soft routine source-read budget before substantive work: `<= 3`.

The Common Surface is a lookup, not a default preload.

## 5. GitHub/service routing

In ChatGPT/Project execution with the connected GitHub capability available:

`CONNECTED_GITHUB_PLUGIN = PRIMARY_REMOTE_GITHUB_PATH`.

Use the GitHub connector/plugin for remote repository files, search, commits, branches, PRs, issues and allowed workflow/status operations.

Do **not** use ChatGPT/container networking to clone GitHub, fetch raw GitHub URLs, or reproduce remote GitHub access when the connected capability can perform the action.

A pre-existing local checkout may be used for actual local execution/tests. It is not the fallback transport for remote synchronization.

Do not repeatedly retry or report a known unavailable local GitHub network route. A remote-access problem is surfaced only when the connected GitHub route itself cannot complete a required action.

Detailed remote rules:

`docs/GITHUB_INTERACTION_BUDGET.md`.

## 6. Working Truth

`WORKING_TRUTH` is TASK execution discipline after an explicit Driver/taskbook freeze.

It is not a FREE Phase-A premise and not raw-candidate status.

## 7. Evidence integrity

Never fabricate proof, computation, hashes, validation status, novelty, provenance or tool results.

Keep claim status exact. Finite enumeration/software success is not automatically theorem proof.

Load triggered semantic policies only when the claim requires them:

- `FOUNDATIONAL_LOGIC.md` / `foundational_logic.json` — foundation-facing inverse/recovery reasoning;
- `native_semantics_admissibility.json` — native/intrinsic/base-world claims;
- geometry/refoundation policy — geometry/refoundation tasks.

## 8. Candidate / task / continuation provenance

`RAW_AXIOM_CANDIDATE != WORKING_TRUTH != CANONICAL_FOUNDATION`.

A task opened from FREE discovery preserves audited candidate origin/ID/state.

`PASS_IS_NOT_A_SUCCESSOR_TRIGGER`.

A continuation requires a genuine new information gap, discriminating outcomes, kill condition, and explicit consideration of closure/another owner/free exploration.

Exact taskbook contract:

- `research_taskbook_contract.json`;
- `research_taskbook_policy.json`;
- `docs/RESEARCH_TASKBOOK_AUTHORING_AND_REVIEW.md`;
- `tools/research_taskbook.py`.

## 9. Remote liveness

`RESEARCH_HOT_PATH > REMOTE_PREFLIGHT`.

Do not perform universal scheduler/Issue/PR/CI/tree preflight.

Do not poll CI/review/status merely to wait for change.

Do not chase moving `main` without a concrete action.

Tool/scheduler/CI availability is not a mathematical `HARD_BLOCK`.

## 10. Triggered control surfaces

Load only when relevant:

- scheduler/Relay/Foundation surfaces for actual coordination actions;
- Driver contract + continuity for actual Driver portfolio decisions;
- Common Surface for exact cross-owner theorem/tool/conflict lookup;
- current native router for current-result/generation lookup;
- test/Lean diagnostics for actual diagnosis;
- owner-isolation/promotion policy for actual publication/promotion work.

## 11. Persistence and publication

L1/L2/L3 research is remote-silent between semantic checkpoints by default.

Journal, Driver Continuity, source task/result files and source `main` have distinct roles.

Current source `main` is canonical only after applicable gates.

## 12. Promotion liveness

`READY_PR != PROMOTION_LANE_LEASE`.

Mathematical L4 is one bounded active promotion attempt at a time.

Strict `NO_NEW_MATHEMATICS` governance maintenance uses the separate bounded protocol in:

`docs/GOVERNANCE_MAINTENANCE_LIVENESS.md`.

## 13. Current-only hot path

Normal startup files describe **current behavior/current authority only**.

Closed numbered routes, superseded definitions, retired worldview models and completed governance episodes are not repeated in hot routers. Retrieve them from Git history or explicit historical records only when the task actually asks for history/provenance/comparison.
