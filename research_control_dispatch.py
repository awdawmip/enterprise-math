#!/usr/bin/env python3
"""Enterprise Math recover-before-fresh canonical control-plane router.

This module composes the existing fresh task/lane selectors with the independent
10-minute conversation-liveness watchdog. It never creates a CLAIM and never
changes owner-lease semantics. A valid owner lease and a stale conversation are
routed to stale-session adoption with the existing winning CLAIM preserved.

Unresolved immutable-publication forks are isolated task-locally before the
fresh selectors run. The affected task is BLOCKED with no operational
publication selected; unrelated tasks remain dispatchable.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Mapping

from control_plane import research_publication_fault_isolation
from tools import research_dispatch
from tools import research_lane_dispatch
from tools import research_runtime
from tools import research_scheduler

ROOT = Path(__file__).resolve().parent
research_publication_fault_isolation.install(ROOT)

SESSION_OBSERVATION_SCHEMA = "ENTERPRISE_MATH_SESSION_LIVENESS_OBSERVATIONS_V1"
ORDINARY_TASK = "ORDINARY_TASK"
COHORT_LANE = "COHORT_LANE"


class ControlDispatchError(ValueError):
    pass


def _target_key(
    task_id: str,
    execution_cohort_id: str | None = None,
    execution_lane_id: str | None = None,
) -> str:
    if execution_cohort_id is None and execution_lane_id is None:
        return task_id
    if not execution_cohort_id or not execution_lane_id:
        raise ControlDispatchError(
            "session observation lane identity requires both execution_cohort_id and execution_lane_id"
        )
    return f"{task_id}::{execution_cohort_id}::{execution_lane_id}"


def _state_target_key(state: Mapping[str, Any]) -> str:
    task_id = state.get("task_id")
    if not isinstance(task_id, str) or not task_id:
        raise ControlDispatchError("dispatch state missing task_id")
    cohort_id = state.get("execution_cohort_id")
    lane_id = state.get("execution_lane_id")
    if cohort_id is None and lane_id is None:
        return _target_key(task_id)
    if not isinstance(cohort_id, str) or not isinstance(lane_id, str):
        raise ControlDispatchError("lane dispatch state has malformed execution scope")
    return _target_key(task_id, cohort_id, lane_id)


def parse_session_observations(value: Mapping[str, Any] | None) -> dict[str, str]:
    """Validate ephemeral liveness observations keyed by exact owner scope.

    ``last_verified_activity_at`` means the latest independently verified
    conversation response or durable execution progress. A CLAIM timestamp by
    itself is not session-liveness evidence.
    """
    if value is None:
        return {}
    if value.get("schema") != SESSION_OBSERVATION_SCHEMA:
        raise ControlDispatchError("unexpected session-liveness observation schema")
    rows = value.get("observations")
    if not isinstance(rows, list):
        raise ControlDispatchError("session-liveness observations must be a list")
    result: dict[str, str] = {}
    for index, row in enumerate(rows):
        if not isinstance(row, Mapping):
            raise ControlDispatchError(f"observations[{index}] must be an object")
        task_id = row.get("task_id")
        if not isinstance(task_id, str) or not task_id.strip():
            raise ControlDispatchError(f"observations[{index}].task_id is required")
        cohort_id = row.get("execution_cohort_id")
        lane_id = row.get("execution_lane_id")
        if cohort_id is not None and (not isinstance(cohort_id, str) or not cohort_id.strip()):
            raise ControlDispatchError(f"observations[{index}].execution_cohort_id is invalid")
        if lane_id is not None and (not isinstance(lane_id, str) or not lane_id.strip()):
            raise ControlDispatchError(f"observations[{index}].execution_lane_id is invalid")
        key = _target_key(task_id.strip(), cohort_id, lane_id)
        if key in result:
            raise ControlDispatchError(f"duplicate session-liveness observation for {key}")
        activity = row.get("last_verified_activity_at")
        if not isinstance(activity, str) or not activity.strip():
            raise ControlDispatchError(
                f"observations[{index}].last_verified_activity_at is required"
            )
        research_runtime.parse_time(activity)
        result[key] = activity
    return result


def _leased_targets(
    events: list[dict[str, Any]], *, now, kind: str, root: Path
) -> list[dict[str, Any]]:
    targets: list[dict[str, Any]] = []
    states = research_dispatch.effective_states(events, now=now, root=root)
    for state in states:
        if kind != "ANY" and state.get("kind") != kind:
            continue
        if state.get("dispatch_state") == "LEASED":
            targets.append({"surface": ORDINARY_TASK, "state": state})
            continue
        if state.get("dispatch_state") != "COHORT_ACTIVE":
            continue
        task_id = state.get("task_id")
        if not isinstance(task_id, str) or not task_id:
            raise ControlDispatchError("COHORT_ACTIVE state missing task_id")
        for lane in research_lane_dispatch.lane_states(
            task_id, events, now=now, root=root
        ):
            if lane.get("dispatch_state") == "LEASED":
                targets.append({"surface": COHORT_LANE, "state": lane})
    return targets


def _fresh_lane(
    events: list[dict[str, Any]], *, now, kind: str, root: Path
) -> dict[str, Any] | None:
    candidates: list[dict[str, Any]] = []
    for state in research_dispatch.effective_states(events, now=now, root=root):
        if kind != "ANY" and state.get("kind") != kind:
            continue
        if state.get("dispatch_state") != "COHORT_ACTIVE":
            continue
        task_id = state.get("task_id")
        if not isinstance(task_id, str) or not task_id:
            continue
        lane = research_lane_dispatch.select_lane(task_id, events, now=now, root=root)
        if lane is not None:
            candidates.append(lane)
    if not candidates:
        return None
    return min(
        candidates,
        key=lambda item: (
            str(item.get("task_id", "")),
            str(item.get("execution_cohort_id", "")),
            str(item.get("execution_lane_id", "")),
        ),
    )


def _adoption_result(target: Mapping[str, Any], decision: Mapping[str, Any]) -> dict[str, Any]:
    state = target["state"]
    return {
        "action": research_runtime.ADOPT_OWNER_CLAIM,
        "surface": target["surface"],
        "target": dict(state),
        "target_key": _state_target_key(state),
        "claim_id": state.get("claim_id"),
        "researcher_id": state.get("researcher_id"),
        "owner_lease_until": state.get("owner_lease_until", state.get("lease_until")),
        "owner_claim_preserved": True,
        "new_claim_required": False,
        "session_state": decision.get("session_state"),
        "stale_at": decision.get("stale_at"),
        "required_guard": "tools/research_runtime_guard.py adopt",
        "reason": "valid owner lease remains authoritative but the owning conversation is stale",
    }


def route_from_candidates(
    leased_targets: list[dict[str, Any]],
    *,
    observations: Mapping[str, str],
    now,
    fresh_task: Mapping[str, Any] | None,
    fresh_lane: Mapping[str, Any] | None,
) -> dict[str, Any]:
    """Pure routing core used by the repository-backed wrapper and regression tests."""
    recoverable: list[tuple[str, dict[str, Any], dict[str, Any]]] = []
    unknown: list[dict[str, Any]] = []
    active: list[str] = []

    for target in leased_targets:
        state = target.get("state")
        if not isinstance(state, Mapping):
            raise ControlDispatchError("leased target missing state object")
        key = _state_target_key(state)
        activity = observations.get(key)
        decision = research_runtime.dispatch_decision(
            state,
            session_last_activity_at=activity,
            now=now,
        )
        action = decision.get("action")
        if action == research_runtime.ADOPT_OWNER_CLAIM:
            recoverable.append((key, dict(target), decision))
        elif action == "VERIFY_SESSION_LIVENESS":
            unknown.append(
                {
                    "target_key": key,
                    "surface": target.get("surface"),
                    "task_id": state.get("task_id"),
                    "execution_cohort_id": state.get("execution_cohort_id"),
                    "execution_lane_id": state.get("execution_lane_id"),
                    "claim_id": state.get("claim_id"),
                    "owner_lease_until": state.get("owner_lease_until", state.get("lease_until")),
                }
            )
        elif action == research_runtime.KEEP_CURRENT_SESSION:
            active.append(key)
        elif action == research_runtime.CLAIM_NEW_OWNER:
            raise ControlDispatchError(
                f"{key}: leased-state/session decision is inconsistent; recompute canonical state"
            )

    if recoverable:
        _, target, decision = min(recoverable, key=lambda item: item[0])
        return _adoption_result(target, decision)

    if fresh_task is not None:
        return {
            "action": research_runtime.CLAIM_NEW_OWNER,
            "surface": ORDINARY_TASK,
            "target": dict(fresh_task),
            "target_key": _state_target_key(fresh_task),
            "owner_claim_preserved": False,
            "new_claim_required": True,
            "reason": "fresh canonical task selector returned a dispatchable target",
        }

    if fresh_lane is not None:
        return {
            "action": research_runtime.CLAIM_NEW_OWNER,
            "surface": COHORT_LANE,
            "target": dict(fresh_lane),
            "target_key": _state_target_key(fresh_lane),
            "owner_claim_preserved": False,
            "new_claim_required": True,
            "reason": "active execution cohort has an evidence-incomplete unowned lane",
        }

    if unknown:
        return {
            "action": "VERIFY_SESSION_LIVENESS",
            "owner_claim_preserved": True,
            "new_claim_required": False,
            "targets": sorted(unknown, key=lambda item: item["target_key"]),
            "reason": (
                "fresh dispatch is empty, but at least one valid owner lease has unknown "
                "conversation liveness; NO_DISPATCH is not yet justified"
            ),
        }

    return {
        "action": research_runtime.NO_DISPATCH,
        "owner_claim_preserved": bool(active),
        "new_claim_required": False,
        "active_owned_targets": sorted(active),
        "reason": "no stale-recoverable owner and no fresh task/lane target",
    }


def route_control(
    events: list[dict[str, Any]],
    *,
    now,
    observations: Mapping[str, str] | None = None,
    kind: str = "RESEARCH",
    root: Path = ROOT,
) -> dict[str, Any]:
    observations = observations or {}
    leased = _leased_targets(events, now=now, kind=kind, root=root)
    fresh_task = research_dispatch.select_task(events, now=now, kind=kind, root=root)
    fresh_lane = _fresh_lane(events, now=now, kind=kind, root=root)
    result = route_from_candidates(
        leased,
        observations=observations,
        now=now,
        fresh_task=fresh_task,
        fresh_lane=fresh_lane,
    )
    quarantined = sorted(research_publication_fault_isolation.validated_quarantines(root))
    if quarantined:
        result["quarantined_tasks"] = quarantined
    return result


def _load_observation_payload(args: argparse.Namespace) -> dict[str, str]:
    if args.session_observations_json:
        raw = json.loads(args.session_observations_json)
    elif args.session_observations:
        raw = json.loads(args.session_observations.read_text(encoding="utf-8"))
    else:
        return {}
    if not isinstance(raw, Mapping):
        raise ControlDispatchError("session-liveness payload must decode to an object")
    return parse_session_observations(raw)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Enterprise Math fault-isolated recover-before-fresh canonical control dispatch"
    )
    parser.add_argument("--events", type=Path)
    parser.add_argument("--now")
    parser.add_argument(
        "--kind", choices=["RESEARCH", "GOVERNANCE", "ANY"], default="RESEARCH"
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--session-observations", type=Path)
    group.add_argument("--session-observations-json")
    args = parser.parse_args()

    events = research_dispatch.load_events(args.events)
    now = research_scheduler.now_utc(args.now)
    observations = _load_observation_payload(args)
    result = route_control(events, now=now, observations=observations, kind=args.kind)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 2 if result.get("action") == research_runtime.NO_DISPATCH else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (
        ControlDispatchError,
        research_runtime.RuntimeStateError,
        research_publication_fault_isolation.PublicationFaultIsolationError,
    ) as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
