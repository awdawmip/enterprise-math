# Enterprise Math Research Tool Surface

Status: `ACTIVE / STABLE ROUTER`
Purpose: stable tool/protocol entrypoint for Enterprise Math researcher roles.

This file names stable tool surfaces. It does not duplicate mutable project facts, task status, current SHAs, or topic-specific instructions.

## Mandatory startup tool/protocol knowledge

Before an Enterprise Math researcher declares bootstrap complete, it must know and, where marked, read the following current repository surfaces.

### MANDATORY — repository interaction and liveness

Read:

- `AGENTS.md`
- `docs/GITHUB_INTERACTION_BUDGET.md`

These govern sparse remote interaction, publication cadence, no-polling behavior, owner isolation, task execution, and liveness.

### MANDATORY — researcher identity

Read:

- `research_identity_state_machine.json`
- `docs/RESEARCH_IDENTITY_PROTOCOL.md`

Reference helper:

- `tools/research_identity.py`

Identity is visible and role-specific. A free researcher uses the `EM-FREE-*` identity lane unless an existing identity is being continued.

### MANDATORY — current mathematical routing

Read:

- `research_common_surface.json` OR the current human Common Surface selected by `AGENTS.md`;
- `PROJECT_DEFINITION.zh-CN.md` (or the English equivalent when appropriate);
- `project_definition.json` when machine-readable project authority matters;
- `definitions/00_CURRENT_NATIVE_FOUNDATION.md`;
- `FOUNDATIONAL_LOGIC.md` and `foundational_logic.json`;
- `GEOMETRIC_TOOL_REFOUNDATION_POLICY.md`;
- `native_semantics_admissibility.json`.

The source current-native-foundation router and the current global Enterprise foundation router may require additional canonical definitions. Those routed files are mandatory when listed as current `Read first` inputs.

Do not infer current authority from an older definition file merely because that file still exists in Git history or because its historical text once used the word `CANONICAL`.

### CONDITIONAL — taskbook tooling

When an explicit taskbook exists, inspect and use the taskbook protocol/helper as needed, including:

- `tools/research_taskbook.py`
- the exact `research_tasks/<taskbook>.md`
- its frozen source SHA and owner lane.

A `FREE_RESEARCHER` waiting for a topic does not create or claim a taskbook merely to bootstrap.

### CONDITIONAL — scheduler

Scheduler surfaces are used only when the role/task explicitly opts into scheduling. They are not a waiting-role startup gate.

A `FREE_RESEARCHER` in `WAITING_FOR_TOPIC` MUST NOT auto-claim Issue #240 or `research_scheduler.json` work.

### CONDITIONAL — Lean, tests, diagnostics, computation

Read the relevant liveness/diagnostic protocol before repeated tool use, including when applicable:

- `docs/LEAN_DIAGNOSTIC_LIVENESS.md`
- `docs/TEST_DISCOVERY_LIVENESS.md`

Use repository Python/Lean/checker tooling, symbolic computation, brute force, or external tools according to the supplied topic and current rules. Do not infer native semantics from an implementation tool merely because the tool is convenient.

## Runtime connected tools

At role startup, inspect the actually available runtime tool surface before promising an operation. Connected GitHub access may be used for current canonical reads and authorized writes. Web, Python, file, or other tools are used only when available and appropriate.

Do not claim access to an unavailable tool. Tool availability is not mathematical evidence.

## Stability invariant

The Project suffix should point to stable bootstrap files rather than copying this list. This file may evolve as tools change without requiring the host Project suffix or visible EM badge configuration to change.
