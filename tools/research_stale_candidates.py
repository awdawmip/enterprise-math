#!/usr/bin/env python3
"""Surface live Scheduler V2 claims that need stale-conversation verification.

This helper is deliberately conservative. It does not ORPHAN or ADOPT anything.
It only identifies live claims whose last *verifiable* scheduler action is older
than the conversation-liveness threshold. A Driver must then rebuild the durable
frontier (branch/commit/return/checker/etc.) before deciding that the execution
conversation is actually stale.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys
from datetime import datetime, timezone
from typing import Any

try:
    from tools import research_scheduler as rs
except ModuleNotFoundError:  # direct `python tools/research_stale_candidates.py`
    import research_scheduler as rs

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "research_scheduler.json"


def parse_time(value: str) -> datetime:
    return rs.parse_time(value)


def _event_is_verifiable_for_live_claim(event: dict[str, Any], state: dict[str, Any]) -> bool:
    if event.get("task_id") != state.get("task_id"):
        return False
    claim_id = state.get("claim_id")
    if not claim_id or event.get("claim_id") != claim_id:
        return False

    kind = event.get("event")
    if kind in {"CLAIM", "ADOPT"}:
        return True
    if kind == "PROGRESS":
        # A PROGRESS event is a liveness proof only when it points to a durable,
        # externally checkable result. Prose/heartbeat-style progress alone is
        # intentionally ignored by this watchdog.
        return rs.nonempty(event.get("progress_ref"))
    return False


def latest_verified_action(
    state: dict[str, Any], events: list[dict[str, Any]]
) -> tuple[datetime | None, str | None]:
    latest_at: datetime | None = None
    latest_ref: str | None = None
    for event in events:
        if not _event_is_verifiable_for_live_claim(event, state):
            continue
        try:
            at = rs.event_time(event)
        except (rs.SchedulerError, ValueError):
            continue
        if latest_at is None or at >= latest_at:
            latest_at = at
            if event.get("event") == "PROGRESS":
                latest_ref = str(event.get("progress_ref"))
            elif event.get("event") == "ADOPT":
                latest_ref = str(event.get("recovery_ref") or "ADOPT")
            else:
                latest_ref = str(event.get("execution_stamp") or event.get("claim_id") or "CLAIM")
    return latest_at, latest_ref


def stale_candidates(
    config: dict[str, Any],
    events: list[dict[str, Any]],
    *,
    now: datetime,
    root: pathlib.Path = ROOT,
) -> list[dict[str, Any]]:
    threshold = int(config.get("conversation_stale_minutes", 10))
    states = rs.effective_states(config, events, now, root=root)
    out: list[dict[str, Any]] = []
    for state in states:
        if state.get("dispatch_state") != "LEASED" or not state.get("claim_id"):
            continue
        last_at, last_ref = latest_verified_action(state, events)
        if last_at is None:
            # A live claim with no reconstructable verifiable claim/adopt action
            # is itself suspicious, but this tool will not invent a timestamp.
            out.append({
                "task_id": state.get("task_id"),
                "claim_id": state.get("claim_id"),
                "execution_id": state.get("execution_id"),
                "classification": "STALE_CANDIDATE_UNKNOWN_BASELINE",
                "last_verified_action_at": None,
                "last_verified_ref": None,
                "threshold_minutes": threshold,
                "required_next_action": "REBUILD_DURABLE_FRONTIER_AND_VERIFY_LIVENESS",
                "auto_orphan_allowed": False,
            })
            continue
        age_seconds = (now.astimezone(timezone.utc) - last_at.astimezone(timezone.utc)).total_seconds()
        if age_seconds < threshold * 60:
            continue
        out.append({
            "task_id": state.get("task_id"),
            "claim_id": state.get("claim_id"),
            "execution_id": state.get("execution_id"),
            "classification": "STALE_CANDIDATE",
            "last_verified_action_at": last_at.isoformat(),
            "last_verified_ref": last_ref,
            "age_minutes": round(age_seconds / 60.0, 3),
            "threshold_minutes": threshold,
            "required_next_action": "REBUILD_DURABLE_FRONTIER_AND_VERIFY_LIVENESS",
            "auto_orphan_allowed": False,
        })
    return sorted(out, key=lambda item: (-float(item.get("age_minutes", 10**9)), str(item.get("task_id"))))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="List Scheduler V2 live claims that require stale-conversation durable-frontier verification"
    )
    parser.add_argument("--config", type=pathlib.Path, default=DEFAULT_CONFIG)
    parser.add_argument("--events", type=pathlib.Path, required=True)
    parser.add_argument("--now", help="ISO-8601 time; defaults to current UTC")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    config = rs.load_json(args.config)
    events = rs.load_events(args.events)
    current = rs.now_utc(args.now)
    root = args.config.resolve().parent
    report = {
        "schema": "ENTERPRISE_MATH_STALE_CONVERSATION_CANDIDATES_V1",
        "generated_at": current.isoformat(),
        "threshold_minutes": int(config.get("conversation_stale_minutes", 10)),
        "candidates": stale_candidates(config, events, now=current, root=root),
        "warning": "Candidates are not authority to ORPHAN. Rebuild the durable frontier first; only Driver/SYSTEM may release an evidenced stale claim.",
    }
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (rs.SchedulerError, OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
