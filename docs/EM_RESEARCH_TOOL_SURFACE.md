# Enterprise Math Research Tool Surface

Status: `ACTIVE / STABLE ROUTER / HOT-PATH V3`
Purpose: stable tool/protocol entrypoint without recreating a remote-preflight tax or a research-agenda preload.

## Liveness invariant

`RESEARCH_HOT_PATH > REMOTE_PREFLIGHT`.

For an explicit selected task:

`MAX_ROUTINE_SOURCE_READS_BEFORE_SUBSTANTIVE_WORK = 3`.

A missing concrete dependency may trigger another read later; that is different from universally preloading governance/catalog files.

## Research-mode precedence

When current source contains `research_architecture.json` with schema `ENTERPRISE_MATH_RESEARCH_ARCHITECTURE_V2`, its role/mode contract controls research-context visibility:

- `FREE_AXIOM_DISCOVERY` uses foundation-only discovery before candidate freeze;
- `TASK_RESEARCH` uses exact-task-first execution.

Until that source governance is promoted, current GLOBAL_KNOWLEDGE role bootstraps provide the ChatGPT-side transition guard.

This tool surface does not itself choose the research question.

## Explicit TASK_RESEARCH hot start

Before substantive work, normally use only:

1. `AGENTS.md` — role/safety/liveness contract;
2. **the exact task entry** — supplied `research_tasks/<taskbook>.md`, exact theorem/spec/code object, or `definitions/00_CURRENT_NATIVE_FOUNDATION.md` when foundation selection is itself the task;
3. **the first exact dependency actually needed to begin**.

Then work.

Do **not** make `research_common_surface.json` or the human Common Surface an automatic second read. They are triggered ownership/theorem/tool/conflict lookup surfaces, not default context dumps.

This explicit-task packet is not the discovery packet for `EM_FREE_RESEARCHER`.

## Triggered reads — binding when relevant, not universal

- Common Surface — cross-owner theorem/tool lookup, de-dup/conflict routing, executable-module registry;
- `docs/GITHUB_INTERACTION_BUDGET.md` — expanded remote/PR/Issue/CI operations;
- `docs/RESEARCH_IDENTITY_PROTOCOL.md` + `research_identity_state_machine.json` — unresolved identity/mode mechanics;
- `FOUNDATIONAL_LOGIC.md` / `foundational_logic.json` — foundation-facing inverse/recovery reasoning;
- `native_semantics_admissibility.json` — before freezing native/intrinsic/base-world claims;
- `GEOMETRIC_TOOL_REFOUNDATION_POLICY.md` — geometry/refoundation-policy work;
- `project_definition.json` — machine-readable project mission/authority when materially needed;
- exact definitions routed by `definitions/00_CURRENT_NATIVE_FOUNDATION.md` — only for mathematical objects actually used;
- scheduler, Relay, Foundation, owner isolation, Lean/test diagnostics — only when that function becomes active.

Triggered dependencies are not optional. Lazy loading means avoid irrelevant reads, not ignore relevant rules.

## Current native authority

`definitions/00_CURRENT_NATIVE_FOUNDATION.md` selects the current mathematical generation. For exact statements, follow it to the exact task-relevant canonical definition.

Do not infer current authority from an older file merely because it exists or historically used `ACTIVE`, `CANONICAL`, or `FOUNDATIONAL`.

## Taskbooks

When an explicit taskbook is supplied, it is the normal second task-research read. Use its frozen source/ref/owner lane exactly.

When current taskbook V5 governance is present, new/re-dispatched tasks also preserve task origin/lineage and enforce the continuation successor gate. Legacy already-running tasks are not retroactively erased merely because governance advanced.

## Free researcher — foundation-only axiom discovery

`EM_FREE_RESEARCHER` is not a waiting queue role.

Its default mode is `FREE_AXIOM_DISCOVERY`, state `AXIOM_DISCOVERY`, objective `DISCOVER_NEW_AXIOM_CANDIDATES`.

Before candidate freeze, do not load current scheduler/taskbooks/Relay/PR/recent commit context, Driver Continuity, recent route success/failure catalogs, other-branch `WORKING_TRUTH`, suggested questions, ambient recent-project memory, or existing tools/representations merely for inspiration.

Use a fresh clean context for a genuine blind-discovery claim when practical; preexisting agenda exposure cannot literally be unread and must be disclosed as `ANCHOR_EXPOSED`.

Do not repeatedly name a salient route merely to say it is forbidden; negative instructions can themselves prime it. Use generic agenda categories during Phase A.

Role-specific source contracts when current:

- `research_roles/EM_FREE_RESEARCHER_ROLE.md`;
- `research_roles/EM_FREE_RESEARCHER_ANTI_ANCHORING_PROTOCOL.md`;
- `research_axiom_candidate_state_machine.json`.

The generic no-user-task scheduler rule does not apply during Phase-A free axiom discovery. After candidate freeze, prior/current work may be opened for falsification, de-duplication, prior-art and integration audits.

## Tests / Lean / computation

Use relevant diagnostics only when actual repeated formal/test/tool work begins. Do not poll CI.

Python, Lean, symbolic/brute-force tooling and external tools are evidence/mechanics surfaces, never a substitute for native semantic typing or a reason to select an ontology/question merely because the tool exists.

## Runtime tools

Inspect the actually available runtime tool surface before promising an operation. Connected GitHub may be used for canonical reads and authorized writes. Web/Python/file tools are used only when available and appropriate.

## Read stability

Within one execution phase, reuse immutable content already fetched at a known SHA/ref. Re-reading unchanged routers/PR metadata merely for reassurance is a performance defect.

Refresh only when freshness/concurrency can materially change the result or immediately before a concurrency-sensitive write.

For free research, loading more current-route context before Phase-A freeze is an anchoring defect, not an optimization.

## Stability invariant

Host Project instructions should point to stable bootstrap/router files instead of copying this list. Mutable tool details remain behind this stable router.
