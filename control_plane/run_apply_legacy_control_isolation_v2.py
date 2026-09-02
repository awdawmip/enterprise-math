#!/usr/bin/env python3
"""Run the isolation transaction with semantic runtime-registration rewrites."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from control_plane import apply_legacy_control_isolation as apply
from control_plane import run_apply_legacy_control_isolation as v1


def patch_runtime_guard() -> None:
    rel = "control_plane/research_runtime_guard_core.py"
    text = apply.read(rel)
    text = text.replace("from tools import research_scheduler", "from tools import research_runtime_reducer")
    text = text.replace("import research_scheduler  # type: ignore", "import research_runtime_reducer  # type: ignore")
    text = text.replace("research_scheduler.", "research_runtime_reducer.")

    if "def legacy_task_ids(" in text:
        text = apply.replace_region(
            text,
            "def legacy_task_ids(",
            "def _execution_scope(",
            "",
            rel + ":legacy-task-loader",
        )

    anchor = text.find("        return updated\n")
    if anchor < 0:
        raise apply.CutoverError(rel + ": current-publication return boundary missing")
    legacy_start = text.find("\n    if scope is not None:\n", anchor)
    legacy_end = text.find("\n\ndef _registered_definition(", legacy_start)
    if legacy_start < 0 or legacy_end < 0:
        raise apply.CutoverError(rel + ": legacy registration fallback boundary missing")
    text = (
        text[:legacy_start]
        + '''
    if scope is not None:
        raise RuntimeAuthorizationError("execution cohorts require an immutable registered task")
    raise RuntimeAuthorizationError(
        f"task {task_id!r} has no current immutable V2 publication"
    )
'''
        + text[legacy_end:]
    )

    pre_final = '''def pre_final_gate(state: Mapping[str, Any], *, root: Path = ROOT) -> dict[str, Any]:
    safe = _delegate_safe_state(state, purpose="pre_final", root=root)
    decision = research_runtime.pre_final_gate(safe)
    decision["registration_authenticated"] = True
    decision["registration_authority"] = "IMMUTABLE_TASK_RECORD"
    return decision


'''
    text = apply.replace_region(
        text,
        "def pre_final_gate(",
        "def apply_terminal_event(",
        pre_final,
        rel + ":pre-final",
    )

    authorize = '''def authorize_execution(
    state: Mapping[str, Any],
    *,
    events: list[dict[str, Any]] | None = None,
    now=None,
    root: Path = ROOT,
) -> dict[str, Any]:
    safe = canonicalize_registration(state, purpose="execution", root=root)
    task_id = safe["task"]["task_id"]
    if events is None:
        raise RuntimeAuthorizationError(
            "registered execution requires canonical Issue #240 event evidence"
        )
    resolved_now = now if now is not None else research_runtime_reducer.now_utc(None)
    scope = _execution_scope(state)
    binding = _binding_for_scope(
        task_id, scope, events, now=resolved_now, root=root
    )
    _reconcile_caller_owner_claim(state, binding)
    return {
        "authorized": True,
        "task_id": task_id,
        "task_registration": safe["task_registration"],
        "owner_claim": _canonical_owner_claim(binding),
        "execution_binding": binding,
        "authorization_authority": (
            "CURRENT_AUTHORIZED_WINNING_ISSUE_240_LANE_CLAIM"
            if scope is not None
            else "CURRENT_AUTHORIZED_WINNING_ISSUE_240_CLAIM"
        ),
    }


'''
    text = apply.replace_region(
        text,
        "def authorize_execution(",
        "def _load_state(",
        authorize,
        rel + ":authorize",
    )

    if "LEGACY_BASELINE_REGISTERED" in text or "legacy_task_ids" in text:
        raise apply.CutoverError(rel + ": legacy registration semantics remain after rewrite")
    apply.write(rel, text)

    wrapper = apply.read("tools/research_runtime_guard.py").replace(
        "_core.research_scheduler.", "_core.research_runtime_reducer."
    )
    apply.write("tools/research_runtime_guard.py", wrapper)

    runtime_rel = "tools/research_runtime.py"
    runtime = apply.read(runtime_rel)
    runtime = runtime.replace('    "LEGACY_BASELINE_REGISTERED",\n', "")
    registration = '''def require_task_registration(state: Mapping[str, Any]) -> None:
    registration = state.get("task_registration")
    task = state.get("task")
    if not isinstance(registration, Mapping):
        raise RuntimeStateError("task_registration must be an object; unregistered tasks cannot execute")
    if not isinstance(task, Mapping):
        raise RuntimeStateError("task must be an object")
    registration_state = str(registration.get("state", "")).upper()
    if registration_state not in TASK_REGISTRATION_STATES:
        raise RuntimeStateError(
            "task registration is not executable: "
            f"{registration_state or 'MISSING'}; publish the task before READY/CLAIM/execution"
        )
    task_id = task.get("task_id")
    registry_key = registration.get("registry_key")
    if not isinstance(registry_key, str) or not registry_key.strip():
        raise RuntimeStateError("registered task requires nonempty task_registration.registry_key")
    if registry_key != task_id:
        raise RuntimeStateError("task_registration.registry_key must equal task.task_id")


'''
    runtime = apply.replace_region(
        runtime,
        "def require_task_registration(",
        "def require_canonical_state(",
        registration,
        runtime_rel + ":registration",
    )
    runtime = runtime.replace(
        '"""Map legacy scheduler claim fields to the owner-lease layer only."""',
        '"""Map reduced runtime claim fields to the owner-lease layer only."""',
    )
    runtime = runtime.replace(
        '"""Legacy scheduler conversation dispatch; new task existence is registry-owned."""',
        '"""Derive conversation dispatch from reduced runtime state."""',
    )
    if "LEGACY_BASELINE_REGISTERED" in runtime:
        raise apply.CutoverError(runtime_rel + ": legacy registration state remains")
    apply.write(runtime_rel, runtime)


def main() -> int:
    apply.patch_dispatch = v1.patch_dispatch
    apply.patch_runtime_guard = patch_runtime_guard
    return apply.main()


if __name__ == "__main__":
    raise SystemExit(main())
