# Enterprise Math Test Discovery Liveness

Status: `ACTIVE / CANONICAL TEST-DISCOVERY OVERRIDE`  
Effective: 2026-08-10  
Scope: locating, selecting, reading, and running tests during research, diagnosis, validation, and promotion.

This is a narrow liveness override under `docs/GITHUB_INTERACTION_BUDGET.md`.

## Core rule

> **Do not use GitHub repository-tree traversal as the default way to discover tests.**

`Inspecting Repository Tree for Test Files`, recursive directory enumeration, repeated contents listing, and broad remote `test*` exploration are not normal research steps.

The canonical Python test root is already fixed by `.github/workflows/quality.yml`:

```text
tests/
```

and the repository-wide Python acceptance command is:

```text
PYTHONPATH=src python -m unittest discover -s tests -v
```

Therefore test discovery normally starts from known paths and changed artifacts, not from a fresh remote tree scan.

## Selection ladder

Use this order and stop as soon as the required test surface is identified:

1. **Changed/target artifact first.** If the task names a source module, theorem, tool, test, PR file, or failure, use that exact artifact and its already-known companion test path when available.
2. **Local checkout second.** When a checkout exists, use local filesystem search (`find`, `rg`, IDE index, unittest discovery, Lean module compilation). Do not call GitHub to enumerate the same tree.
3. **Canonical test root / workflow third.** For Python repository validation, use `tests/` and the canonical unittest command above. No additional discovery is needed merely to run the suite.
4. **One targeted lexical lookup only when necessary.** In connector-only execution where the companion test filename is genuinely unknown, make at most one targeted repository search keyed by the exact source module/theorem/tool identifier. Do not recursively inspect the repository tree.
5. **Final acceptance only.** Full repository test execution belongs at a bounded validation/promotion boundary. It is not a discovery mechanism.

## Prohibited hot-path behavior

During ordinary L1/L2/L3 research or diagnosis, do not:

- recursively enumerate repository directories to locate tests;
- list `tests/` repeatedly after its root is already known;
- fetch many test files merely to learn what tests exist;
- search separately for `test`, `tests`, `unittest`, `pytest`, and neighboring naming variants for the same task;
- inspect GitHub Actions repeatedly to infer the test command once the workflow has already been read;
- run the entire repository suite after every small edit;
- treat absence of an immediately found companion test as a reason to broaden into repository-wide remote exploration.

If no exact companion test is found after one targeted lookup, continue with the changed module and create/modify the task-local regression when appropriate. Record broader validation as pending until the normal validation boundary rather than exploring GitHub indefinitely.

## Python

- Canonical root: `tests/`.
- Canonical full-suite command: `PYTHONPATH=src python -m unittest discover -s tests -v`.
- During development, prefer the exact affected test module/class/method when known.
- A full `unittest discover` run is a validation action, not a prerequisite to every research step.

## Lean

Lean test/diagnostic work follows `docs/LEAN_DIAGNOSTIC_LIVENESS.md`:

- changed owner-local module first;
- immediate family only if needed;
- root registration only after local success;
- one final root/repository Lean gate at the validation boundary.

Do not inspect the GitHub tree looking for generic Lean "test files" when the changed module itself is the relevant proof/compile surface.

## Connector-only budget

For test discovery on one unchanged task object:

- repository-tree enumeration: **0 by default**;
- targeted repository searches for the companion test: **at most 1**;
- workflow reads to recover an already-known test command: **0 after the command is cached/loaded**;
- repeated test-file listing: **0**;
- workflow status polling: governed separately by the one-snapshot/no-polling rule.

Exceeding this budget requires a concrete missing evidence dependency. General caution is not sufficient.

## State labels

If broader validation has not yet run, use a precise pending label such as `LOCAL_TEST_PENDING`, `FULL_SUITE_PENDING`, or `CI_PENDING`. Pending validation may defer promotion/merge, but it does not block mathematical research or the user-facing response.

## Relationship to final gates

This protocol changes discovery and hot-path execution only. It does not weaken required final validation. At the proper acceptance boundary, the canonical suite/gates still run against the frozen payload.
