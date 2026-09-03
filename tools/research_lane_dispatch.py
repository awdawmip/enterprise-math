#!/usr/bin/env python3
"""Explicit scheduler surface for active parallel execution cohorts.

Task-global dispatch remains the ordinary path for tasks without a cohort. Once a
cohort is ACTIVE, this module exposes each lane as its own owner race. A lane
with at least one immutable result is evidence-complete and is not automatically
redispatched; further independent work should use a new lane so provenance stays
explicit. Existing additional results are retained if they occur.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from tools import research_cohort_runtime
    from tools import research_dispatch
    from tools import research_lane_claims
    from tools import research_runtime_reducer
except ModuleNotFoundError:
    import research_cohort_runtime  # type: ignore
    import research_dispatch  # type: ignore
    import research_lane_claims  # type: ignore
    import research_runtime_reducer  # type: ignore

ROOT = Path(__file__).resolve().parents[1]


class LaneDispatchError(ValueError):
    pass


def lane_states(
    task_id: str,
    events: list[dict[str, Any]],
    *,
    now,
    root: Path = ROOT,
) -> list[dict[str, Any]]:
    states: list[dict[str, Any]] = []
    cohorts = research_cohort_runtime.active_cohorts(task_id, root)
    for cohort in cohorts:
        cohort_id = str(cohort["cohort_id"])
        for lane in sorted(
            [row for row in cohort.get("lanes", []) if isinstance(row, dict)],
            key=lambda row: str(row.get("lane_id")),
        ):
            lane_id = lane.get("lane_id")
            if not isinstance(lane_id, str) or not lane_id:
                raise LaneDispatchError(f"{cohort_id}: malformed lane_id")
            frozen = research_cohort_runtime.lane_results(
                task_id, cohort_id, lane_id, root
            )
            if frozen:
                states.append(
                    {
                        "task_id": task_id,
                        "execution_cohort_id": cohort_id,
                        "execution_lane_id": lane_id,
                        "lane_role": lane.get("lane_role"),
                        "publication_id": lane.get("publication_id"),
                        "output_prefix": lane.get("output_prefix"),
                        "state": "LANE_RESULT_FROZEN",
                        "dispatch_state": "AWAITING_COHORT_REFERENCE",
                        "result_ids": sorted(
                            str(item.get("result_id")) for item in frozen
                        ),
                        "next_action": "WAIT_FOR_SIBLING_LANES_OR_COHORT_REFERENCE_FLOW",
                    }
                )
                continue
            reduced = research_lane_claims.reduce_lane(
                task_id,
                cohort_id,
                lane_id,
                events,
                now=now,
                root=root,
            )
            states.append(reduced)
    return states


def select_lane(
    task_id: str,
    events: list[dict[str, Any]],
    *,
    now,
    root: Path = ROOT,
) -> dict[str, Any] | None:
    candidates = [
        item
        for item in lane_states(task_id, events, now=now, root=root)
        if item.get("dispatch_state") == "NEEDS_DISPATCH"
    ]
    if not candidates:
        return None
    return min(
        candidates,
        key=lambda item: (
            str(item.get("execution_cohort_id", "")),
            str(item.get("execution_lane_id", "")),
        ),
    )


def task_lane_summary(
    task_id: str,
    events: list[dict[str, Any]],
    *,
    now,
    root: Path = ROOT,
) -> dict[str, Any]:
    lanes = lane_states(task_id, events, now=now, root=root)
    cohort_state = research_cohort_runtime.task_active_cohort_state(task_id, root)
    return {
        "task_id": task_id,
        "dispatch_authority": "EXECUTION_COHORT_LANES",
        "task_global_claim_allowed": False if lanes else True,
        "lanes": lanes,
        "cohort_state": cohort_state,
        "selected_lane": select_lane(task_id, events, now=now, root=root),
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Enterprise Math active execution-cohort lane dispatch"
    )
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("status", "select"):
        cmd = sub.add_parser(name)
        cmd.add_argument("--task-id", required=True)
        cmd.add_argument("--events", type=Path)
        cmd.add_argument("--now")
    args = parser.parse_args()
    events = research_dispatch.load_events(args.events)
    now = (
        research_runtime_reducer.now_utc(args.now)
        if args.now
        else datetime.now(timezone.utc)
    )
    if args.command == "status":
        value = task_lane_summary(args.task_id, events, now=now)
    else:
        value = select_lane(args.task_id, events, now=now)
    print(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if value is not None else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except LaneDispatchError as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
