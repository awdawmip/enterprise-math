# Enterprise Math Research Tool Surface

Status: `ACTIVE / STABLE ROUTER / HOT-PATH V2`
Purpose: stable tool/protocol entrypoint for Enterprise Math research roles without recreating a remote-preflight tax.

## Liveness invariant

`RESEARCH_HOT_PATH > REMOTE_PREFLIGHT`

For an explicit user task, obey the current `AGENTS.md` / GitHub interaction budget:

`MAX_ROUTINE_SOURCE_READS_BEFORE_SUBSTANTIVE_WORK = 3`

A missing concrete dependency may trigger another read later; that is different from universally preloading every governance file.

## Explicit-task hot start

Before substantive work, normally use only:

1. `AGENTS.md` — role, working-truth, ownership and liveness contract;
2. **one** common/router surface when needed — normally `research_common_surface.json` OR the human Common Surface selected by `AGENTS.md`, not both;
3. **one exact task entry** — supplied `research_tasks/<taskbook>.md`, `definitions/00_CURRENT_NATIVE_FOUNDATION.md`, or the exact theorem/spec/code file required to begin.

Then work. Do not wait to read an unrelated protocol merely because it exists.

This explicit-task packet is not the discovery packet for `EM_FREE_RESEARCHER`.

## Triggered reads — binding when relevant, not universal

- `docs/GITHUB_INTERACTION_BUDGET.md` — before expanded remote/PR/Issue/CI preflight or when liveness details are materially needed;
- `docs/RESEARCH_IDENTITY_PROTOCOL.md` + `research_identity_state_machine.json` — when a visible role identity cannot already be resolved or identity mechanics are the task;
- `FOUNDATIONAL_LOGIC.md` / `foundational_logic.json` — foundation-facing inverse/recovery reasoning;
- `native_semantics_admissibility.json` — before freezing a native/intrinsic/base-world ontology claim;
- `GEOMETRIC_TOOL_REFOUNDATION_POLICY.md` — geometry/refoundation-policy work;
- `project_definition.json` — when machine-readable project mission/authority is materially needed;
- exact current definition(s) routed by `definitions/00_CURRENT_NATIVE_FOUNDATION.md` — only for the mathematical objects actually used;
- scheduler, relay, Foundation/Lean/test diagnostics — only when that function is active in the current task.

Triggered dependencies are not optional. Lazy loading means **avoid irrelevant reads**, not “ignore relevant rules.”

## Current native authority

`definitions/00_CURRENT_NATIVE_FOUNDATION.md` selects the current mathematical generation. For exact statements, follow it to the exact task-relevant canonical definition.

Do not infer current authority from an older file merely because it still exists or historically used `ACTIVE`, `CANONICAL`, or `FOUNDATIONAL`.

## Taskbooks

When the user supplies an explicit taskbook, the taskbook is the normal third hot-start read. Use its frozen source/ref/owner lane exactly. Helper tooling such as `tools/research_taskbook.py` is conditional on actual need.

## Free researcher — foundation-only axiom discovery

`EM_FREE_RESEARCHER` is not a waiting queue role.

Its default state is `AXIOM_DISCOVERY`, and its default objective is to discover new axiom candidates from the current foundation before seeing the current research agenda.

Before the first `BLIND_AXIOM_CANDIDATE_PACKET` is frozen, do not load current scheduler/Issue #240, current taskbooks, Research Relay, recent commit/PR titles, R063/R064/current route material, another branch's `WORKING_TRUTH`, theorem-family success catalogs, or suggested questions merely for inspiration.

Role-specific source contract:

- `research_roles/EM_FREE_RESEARCHER_ROLE.md`;
- `research_roles/EM_FREE_RESEARCHER_ANTI_ANCHORING_PROTOCOL.md` once promoted.

The generic no-user-task scheduler rule does not apply to this role during Phase-A axiom discovery. After the blind candidate freeze, prior/current work may be opened for deduplication, contradiction, prior-art and integration audits.

## Tests / Lean / computation

Use relevant diagnostics only when actual repeated test/Lean/tool work begins. Do not poll CI. Python, Lean, symbolic/brute-force tooling and external tools are evidence/mechanics surfaces, never a substitute for native semantic typing.

## Runtime tools

Inspect the actually available runtime tool surface before promising an operation. Connected GitHub may be used for canonical reads and authorized writes. Web/Python/file tools are used only when available and appropriate.

## Read stability

Within one execution phase, reuse immutable content already fetched at a known SHA/ref. Re-reading unchanged routers or PR metadata merely for reassurance is a performance defect. Refresh only when freshness/concurrency can materially change the result or immediately before a concurrency-sensitive write.

For free research, loading more current-route context before Phase-A freeze is not an optimization; it is an anchoring defect.

## Stability invariant

Host Project instructions should point to stable bootstrap/router files instead of copying this list. Mutable tool details remain behind this stable router.
