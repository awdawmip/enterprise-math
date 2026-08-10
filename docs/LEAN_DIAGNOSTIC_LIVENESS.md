# Lean diagnostic liveness protocol

Status: `ACTIVE / GOVERNANCE`
Effective: 2026-08-10
Scope: Lean theorem diagnosis, import repair, local compilation, root-import registration, and final repository Lean validation.

## Purpose

Lean diagnosis must be local, bounded, and evidence-driven. A missing symbol, tactic, instance, or import is a local compilation problem; it must not automatically expand into repeated root builds or repeated umbrella-import experiments.

## Diagnostic invariant

**Use the smallest compilation surface that can answer the current question. Escalate validation only after the local question is resolved.**

`Adding Imports for <module> Diagnosis` is a bounded diagnostic phase, not an open-ended search loop.

## Import diagnosis budget

1. Start from the failing owner-local `.lean` module, not `EnterpriseMath.lean` and not the whole repository.
2. Diagnose the exact missing identifier / tactic / instance first. Prefer an already-used narrow Mathlib or EnterpriseMath import that exports that object.
3. Do not repeatedly add broad umbrella imports such as `Mathlib`, `Mathlib.Tactic`, or unrelated large modules merely to see whether the error disappears. A broad import may be used once only when it is already the established project convention or when the exact dependency cannot reasonably be isolated from available evidence; record that as a temporary diagnostic choice rather than proliferating further imports.
4. In one uninterrupted diagnostic phase, do not perform an unbounded sequence of `add import -> rebuild -> add import -> rebuild`. After at most one import adjustment for the same unresolved missing-object diagnosis, inspect the new concrete compiler error before making another import change.
5. Never modify the root `EnterpriseMath.lean` import list merely to diagnose whether an owner-local module compiles. Root registration happens only after the module itself is locally coherent.

## Validation ladder

Use this order:

1. **local module check** — compile/check only the changed `.lean` module or the smallest target that imports it;
2. **minimal dependency check** — if needed, compile the immediate EnterpriseMath module family that consumes it;
3. **root registration check** — only after local success, add/update the root import and its required common-surface index;
4. **final root/repository gate** — run one warnings-fatal root/Lean gate on the frozen candidate state before canonical promotion or when repository policy requires it.

Do not rerun a higher validation layer after every diagnostic edit. A new local error returns to the local layer, not automatically to the root layer.

## Liveness rules

- A slow or pending full-root build is not a reason to stop mathematical work or user-facing completion.
- Do not poll a pending Lean workflow repeatedly; the CI polling budget in `docs/RESEARCH_SCHEDULER_NONBLOCKING_STARTUP.md` applies unchanged.
- If local compilation cannot be executed in the current environment, preserve the exact module/import change and compiler evidence available, mark local verification as unavailable/pending, and continue other non-conflicting work. Do not compensate by speculative import accumulation.
- A true compile failure may justify one targeted diagnostic pass. It does not justify repeated root builds with unchanged semantic input.

## Import hygiene

- Prefer the narrowest stable import compatible with maintainability; avoid dependency-minimization theater when the project already standardizes a broader module.
- Remove temporary diagnostic-only imports before canonical promotion when they are not semantically required.
- Import changes do not constitute new mathematics and should not restart a research generation.

## Root-index boundary

Adding/removing a root import in `EnterpriseMath.lean` remains subject to the exact `lean_root_imports` human/machine index rule in `AGENTS.md`. This protocol changes only **when** root registration and validation occur: after local module coherence, not as part of exploratory diagnosis.
