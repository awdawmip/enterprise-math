#!/usr/bin/env python3
"""Run the physical-isolation transaction with a function-boundary dispatch rewrite."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from control_plane import apply_legacy_control_isolation as apply


def patch_dispatch() -> None:
    rel = "tools/research_dispatch.py"
    text = apply.read(rel)
    text = re.sub(
        r'\A#!/usr/bin/env python3\n""".*?"""\n',
        '#!/usr/bin/env python3\n"""Canonical immutable-V2 Enterprise Math dispatch view.\n\nTask definitions come only from current immutable V2 publication records. Issue\n#240 events are accepted only through authenticated GitHub comment envelopes and\nare reduced by tools/research_runtime_reducer.py. No task-table or pre-V2\ndefinition fallback is present on main.\n"""\n',
        text,
        count=1,
        flags=re.S,
    )
    text = text.replace("from tools import research_scheduler", "from tools import research_runtime_reducer")
    text = text.replace("import research_scheduler  # type: ignore", "import research_runtime_reducer  # type: ignore")
    text = text.replace(
        'LEGACY = ROOT / "research_scheduler.json"\nOWNERS = ROOT / "branch_governance_overrides.json"\n',
        'RUNTIME_POLICY = ROOT / "research_runtime_policy_v2.json"\n',
    )
    text = text.replace("research_scheduler.", "research_runtime_reducer.")

    merged = '''def merged_definitions(root: Path = ROOT) -> list[dict[str, Any]]:
    by_id: dict[str, dict[str, Any]] = {}
    for task_id, record in research_task_records.current_records(root).items():
        by_id[task_id] = registered_definition(record, root)
    return [by_id[key] for key in sorted(by_id)]


'''
    text = apply.replace_region(
        text,
        "def merged_definitions(",
        "def _is_registered(",
        merged,
        rel + ":merged",
    )

    auth = '''def _event_authentication_filter(
    task: dict[str, Any], events: list[dict[str, Any]]
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Fail closed unless a live event carries an authorized server envelope."""
    accepted: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []
    for index, event in enumerate(events):
        if event.get("task_id") != task.get("task_id"):
            accepted.append(event)
            continue
        meta = event.get(GITHUB_META_KEY)
        if not isinstance(meta, dict) or meta.get("server_authenticated") is not True:
            rejected.append({
                "index": index,
                "reason": "runtime event requires server-authenticated GitHub Issue #240 comment envelope",
            })
            continue
        if meta.get("issue_number") != 240 or type(meta.get("comment_id")) is not int:
            rejected.append({
                "index": index,
                "reason": "GitHub event envelope issue/comment identity is invalid",
            })
            continue
        if meta.get("control_authorized") is not True:
            rejected.append({
                "index": index,
                "reason": "GitHub event author is authenticated but not authorized for control-plane mutation",
            })
            continue
        if meta.get("edited") is True:
            rejected.append({
                "index": index,
                "reason": "edited runtime event is not authority; append a correction event",
            })
            continue
        accepted.append(event)
    return accepted, rejected


'''
    text = apply.replace_region(
        text,
        "def _event_authentication_filter(",
        "def _inline_claim_envelope(",
        auth,
        rel + ":auth",
    )

    summary = '''def _authentication_summary(task: dict[str, Any], events: list[dict[str, Any]]) -> dict[str, Any]:
    matching = [event for event in events if event.get("task_id") == task.get("task_id")]
    server = [event for event in matching if isinstance(event.get(GITHUB_META_KEY), dict)]
    if server:
        latest = max(server, key=lambda event: event[GITHUB_META_KEY].get("comment_id", -1))
        meta = latest[GITHUB_META_KEY]
        return {
            "event_authentication": "GITHUB_SERVER_COMMENT_ENVELOPE",
            "last_server_comment_id": meta.get("comment_id"),
            "last_server_author_login": meta.get("author_login"),
        }
    return {
        "event_authentication": "UNAUTHENTICATED_EVENT_REJECTED" if matching else "NO_RUNTIME_EVENT",
        "last_server_comment_id": None,
        "last_server_author_login": None,
    }


'''
    text = apply.replace_region(
        text,
        "def _authentication_summary(",
        "def reduce_definition(",
        summary,
        rel + ":summary",
    )

    selector = '''def select_task(
    events: list[dict[str, Any]],
    *,
    now: datetime,
    kind: str = "RESEARCH",
    root: Path = ROOT,
) -> dict[str, Any] | None:
    states = effective_states(events, now=now, root=root)
    policy = research_runtime_reducer.load_policy(root)
    return research_runtime_reducer.select_state(states, policy, kind=kind)


'''
    text = apply.replace_region(
        text,
        "def select_task(",
        "def validate(",
        selector,
        rel + ":selector",
    )

    validation = '''def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    try:
        policy = research_runtime_reducer.load_policy(root)
        errors.extend(research_runtime_reducer.validate_policy(policy))
    except Exception as exc:
        errors.append(f"V2 runtime policy failure: {exc}")
    try:
        control_authorization_policy(root)
    except Exception as exc:
        errors.append(f"control-event authorization policy failure: {exc}")
    try:
        definitions = merged_definitions(root)
    except Exception as exc:
        errors.append(f"V2 dispatch definition failure: {exc}")
        return errors
    ids = [item.get("task_id") for item in definitions]
    if len(ids) != len(set(ids)):
        errors.append("canonical V2 dispatch view contains duplicate task IDs")
    for item in definitions:
        if item.get("registration_source") not in {
            "IMMUTABLE_TASK_RECORD",
            "TASK_DEFINITION_FAULT_QUARANTINE",
        }:
            errors.append(f"{item.get('task_id')}: non-V2 task definition entered live dispatch")
    return errors


'''
    text = apply.replace_region(
        text,
        "def validate(",
        "def _decode_event_input(",
        validation,
        rel + ":validate",
    )

    text = apply.require_replace(
        text,
        "    return research_runtime_reducer.load_events(path)\n",
        '    raise DispatchError("runtime input must be raw authenticated Issue #240 comment objects")\n',
        rel + ":bare-events",
    )
    text = text.replace(
        "canonical registered-plus-legacy dispatch",
        "canonical immutable-V2 dispatch",
    )
    text = text.replace("merged task definition(s)", "V2 task definition(s)")
    apply.write(rel, text)


def main() -> int:
    apply.patch_dispatch = patch_dispatch
    return apply.main()


if __name__ == "__main__":
    raise SystemExit(main())
