#!/usr/bin/env python3
"""Reduce frozen scheduler tasks against authenticated Issue #240 events only."""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def flatten(value: Any) -> list[dict[str, Any]]:
    if isinstance(value, list) and value and all(isinstance(page, list) for page in value):
        value = [item for page in value for item in page]
    return [item for item in value if isinstance(item, dict)] if isinstance(value, list) else []


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--comments", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    from tools import research_dispatch, research_scheduler

    config = load(ROOT / "research_scheduler.json")
    comments = flatten(load(args.comments))
    events = research_dispatch.events_from_github_comments(comments, root=ROOT)
    default_lease = int(config.get("claim_lease_minutes", 120))
    now = datetime.now(timezone.utc)
    states = []
    for task in config.get("tasks", []):
        if not isinstance(task, dict) or not isinstance(task.get("task_id"), str):
            continue
        state = research_scheduler.reduce_task(
            task,
            events,
            default_lease_minutes=int(task.get("claim_lease_minutes") or default_lease),
            now=now,
        )
        state.update(
            {
                "title": task.get("title"),
                "kind": task.get("kind"),
                "owner": task.get("owner"),
                "priority": task.get("priority"),
                "leverage": task.get("leverage"),
                "frontier": task.get("frontier"),
                "source_refs": task.get("source_refs", []),
                "identity_lane": research_scheduler.identity_lane(task),
            }
        )
        states.append(state)
    payload = {
        "schema": "ENTERPRISE_MATH_LEGACY_RUNTIME_STATE_AUDIT_V1",
        "snapshot_sha": __import__("os").environ.get("GITHUB_SHA"),
        "generated_at": now.isoformat(),
        "comment_count": len(comments),
        "event_count": len(events),
        "states": states,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"tasks": len(states), "events": len(events)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
