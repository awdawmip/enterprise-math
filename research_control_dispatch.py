#!/usr/bin/env python3
"""Enterprise Math recover-before-fresh canonical control-plane router.

This module composes the existing fresh task/lane selectors with exact-owner-scope
conversation liveness. It never creates a CLAIM and never changes owner-lease
semantics. A valid owner lease and a stale owner execution session are routed to
stale-session adoption with the existing winning CLAIM preserved.

Owner-scope liveness is narrower than generic conversation activity. Only a
verified TASK_RESEARCH response or durable execution progress bound to the exact
task/lane and exact winning claim_id may refresh that owner scope. Control-plane,
Driver, Steward, FREE, unrelated-task, or generic chat activity does not keep a
research owner artificially alive.

Known task-local publication faults are isolated before the fresh selectors run:
unresolved forks select no head, exact pinned integrity faults select no invalid
publication, affected tasks are BLOCKED, and unrelated tasks remain dispatchable.

Every returned route also carries the current non-semantic startup/rebase transport.
That transport invalidates stale cached conversation workflow plans on every control
entry while preserving exact task/claim/durable-frontier authority. AGENTS.md is
obeyed when already injected by the host; it is not a remote task-start prerequisite.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping

from control_plane import research_control_bootstrap
from control_plane import research_publication_fault_isolation
from control_plane import research_task_integrity_fault_isolation
from control_plane import research_startup_transport
from tools import research_dispatch
from tools import research_lane_dispatch
from tools import research_runtime

ROOT = Path(__file__).resolve().parent
research_control_bootstrap.install(ROOT)

SESSION_OBSERVATION_SCHEMA = "ENTERPRISE_MATH_SESSION_LIVENESS_OBSERVATIONS_V2"
SESSION_ACTIVITY_KINDS = frozenset(
    {
        "TASK_RESEARCH_RESPONSE",
        "DURABLE_EXECUTION_PROGRESS",
    }
)
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


def parse_session_observations(
    value: Mapping[str, Any] | None,
) -> dict[str, dict[str, str]]:
    """Validate ephemeral liveness observations keyed by exact owner scope.

    Every observation must pin the exact ``claim_id`` and identify its evidence
    kind. ``TASK_RESEARCH_RESPONSE`` means a verified response continuing work
    under that exact owner scope. ``DURABLE_EXECUTION_PROGRESS`` means a verified
    durable frontier/output change under that exact owner scope.

    CLAIM time, generic chat activity, CONTROL_PLANE_MAINTENANCE, Driver, Steward,
    FREE, or unrelated-task messages are not accepted liveness evidence.
    """
    if value is None:
        return {}
    if value.get("schema") != SESSION_OBSERVATION_SCHEMA:
        raise ControlDispatchError("unexpected session-liveness observation schema")
    rows = value.get("observations")
    if not isinstance(rows, list):
        raise ControlDispatchError("session-liveness observations must be a list")
    result: dict[str, dict[str, str]] = {}
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

        claim_id = row.get("claim_id")
        if not isinstance(claim_id, str) or not claim_id.strip():
            raise ControlDispatchError(f"observations[{index}].claim_id is required")

        evidence_kind = row.get("activity_evidence_kind")
        if evidence_kind not in SESSION_ACTIVITY_KINDS:
            raise ControlDispatchError(
                f"observations[{index}].activity_evidence_kind must be one of {sorted(SESSION_ACTIVITY_KINDS)}"
            )

        activity = row.get("last_verified_activity_at")
        if not isinstance(activity, str) or not activity.strip():
            raise ControlDispatchError(
                f"observations[{index}].last_verified_activity_at is required"
            )
        research_runtime.parse_time(activity)
        result[key] = {
            "claim_id": claim_id.strip(),
            "activity_evidence_kind": str(evidence_kind),
            "last_verified_activity_at": activity.strip(),
        }
    return result


def _owner_scope_activity(
    state: Mapping[str, Any], observation: Mapping[str, str] | None
) -> str | None:
    """Return liveness time only when observation matches exact current owner scope.

    A stale/foreign claim observation is ignored rather than allowed to keep the
    current owner active. Direct library callers receive the same rule as the
    CLI parser, so bypassing JSON parsing cannot turn generic chat activity into
    owner-scope liveness.
    """
    if observation is None:
        return None
    claim_id = state.get("claim_id")
    if not isinstance(claim_id, str) or not claim_id:
        return None
    if observation.get("claim_id") != claim_id:
        return None
    if observation.get("activity_evidence_kind") not in SESSION_ACTIVITY_KINDS:
        return None
    activity = observation.get("last_verified_activity_at")
    if not isinstance(activity, str) or not activity:
        return None
    research_runtime.parse_time(activity)
    return activity


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
        "reason": "valid owner lease remains authoritative but the exact owner execution session is stale",
    }


def route_from_candidates(
    leased_targets: list[dict[str, Any]],
    *,
    observations: Mapping[str, Mapping[str, str]],
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
        activity = _owner_scope_activity(state, observations.get(key))
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
                "fresh dispatch is empty, but at least one valid owner lease has unknown exact "
                "owner-scope execution liveness; generic conversation activity cannot justify NO_DISPATCH"
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
    observations: Mapping[str, Mapping[str, str]] | None = None,
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
    result = research_startup_transport.attach(result)
    fork_quarantines = sorted(research_publication_fault_isolation.validated_quarantines(root))
    integrity_quarantines = sorted(research_task_integrity_fault_isolation.validated_quarantines(root))
    if fork_quarantines or integrity_quarantines:
        result["quarantined_tasks"] = sorted(set(fork_quarantines) | set(integrity_quarantines))
        result["publication_fork_quarantines"] = fork_quarantines
        result["task_integrity_quarantines"] = integrity_quarantines
    return result


def _load_observation_payload(args: argparse.Namespace) -> dict[str, dict[str, str]]:
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
        description="Enterprise Math fault-isolated exact-owner-scope recover-before-fresh control dispatch"
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
    now = research_runtime.parse_time(args.now) if args.now else datetime.now(timezone.utc)
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
        research_task_integrity_fault_isolation.TaskIntegrityIsolationError,
    ) as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
