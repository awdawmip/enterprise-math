#!/usr/bin/env python3
"""Repository-backed authorization guard for the Enterprise Math runtime.

The historical tools/research_runtime.py remains the pure liveness/terminal
primitive. This wrapper authenticates TASK_REGISTRATION against repository
state and reconstructs execution authority from GitHub Issue #240.

Ordinary registered tasks use one authorized winning task-level CLAIM. Optional
parallel execution cohorts switch owner authority to exact
``task + execution_cohort_id + execution_lane_id`` fibers: sibling lanes may run
concurrently, while a task-global owner cannot bypass an active cohort.
"""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
from typing import Any, Mapping

try:
    from tools import research_cohort_runtime
    from tools import research_dispatch
    from tools import research_execution_records
    from tools import research_lane_claims
    from tools import research_result_records
    from tools import research_runtime
    from tools import research_runtime_reducer
    from tools import research_task_records
except ModuleNotFoundError:
    import research_cohort_runtime  # type: ignore
    import research_dispatch  # type: ignore
    import research_execution_records  # type: ignore
    import research_lane_claims  # type: ignore
    import research_result_records  # type: ignore
    import research_runtime  # type: ignore
    import research_runtime_reducer  # type: ignore
    import research_task_records  # type: ignore

ROOT = Path(__file__).resolve().parents[1]


class RuntimeAuthorizationError(ValueError):
    pass


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _execution_scope(state: Mapping[str, Any]) -> dict[str, str] | None:
    raw = state.get("execution_scope")
    if raw is None:
        return None
    if not isinstance(raw, Mapping):
        raise RuntimeAuthorizationError("execution_scope must be an object")
    cohort_id = raw.get("execution_cohort_id")
    lane_id = raw.get("execution_lane_id")
    cohort = cohort_id.strip() if isinstance(cohort_id, str) and cohort_id.strip() else None
    lane = lane_id.strip() if isinstance(lane_id, str) and lane_id.strip() else None
    if cohort is None and lane is None and not raw:
        return None
    if cohort is None or lane is None:
        raise RuntimeAuthorizationError(
            "execution_scope requires both execution_cohort_id and execution_lane_id"
        )
    return {"execution_cohort_id": cohort, "execution_lane_id": lane}


def _active_cohort_ids(task_id: str, root: Path) -> list[str]:
    try:
        return [
            str(item["cohort_id"])
            for item in research_cohort_runtime.active_cohorts(task_id, root)
        ]
    except Exception as exc:
        raise RuntimeAuthorizationError(f"cannot resolve active execution cohorts: {exc}") from exc


def _lane_registration(
    task_id: str, scope: Mapping[str, str], root: Path
) -> tuple[dict[str, Any], dict[str, Any]]:
    try:
        lane = research_lane_claims.lane_scope(
            task_id,
            scope["execution_cohort_id"],
            scope["execution_lane_id"],
            root,
        )
        cohort_state = research_cohort_runtime.cohort_state(
            task_id, scope["execution_cohort_id"], root
        )
    except Exception as exc:
        raise RuntimeAuthorizationError(f"invalid execution lane scope: {exc}") from exc
    if cohort_state.get("terminal") is True:
        raise RuntimeAuthorizationError(
            "execution cohort is terminal after exact two-pass synthesis"
        )
    record = lane.get("publication_record")
    if not isinstance(record, dict):
        raise RuntimeAuthorizationError("execution lane has no immutable publication record")
    return record, cohort_state


def canonicalize_registration(
    state: Mapping[str, Any], *, purpose: str, root: Path = ROOT
) -> dict[str, Any]:
    task = state.get("task")
    if not isinstance(task, Mapping):
        raise RuntimeAuthorizationError("task must be an object")
    task_id = task.get("task_id")
    if not isinstance(task_id, str) or not task_id:
        raise RuntimeAuthorizationError("task.task_id is required")
    scope = _execution_scope(state)

    try:
        current = research_task_records.current_records(root)
    except Exception as exc:
        raise RuntimeAuthorizationError(
            f"cannot resolve canonical task records: {exc}"
        ) from exc

    updated = copy.deepcopy(dict(state))
    if task_id in current:
        record = current[task_id]
        cohort_state = None
        if purpose in {"execution", "adopt"}:
            active_ids = _active_cohort_ids(task_id, root)
            if active_ids:
                if scope is None:
                    raise RuntimeAuthorizationError(
                        "active execution cohort requires exact lane execution_scope"
                    )
                if scope["execution_cohort_id"] not in active_ids:
                    raise RuntimeAuthorizationError(
                        "execution_scope does not reference an ACTIVE cohort for task"
                    )
                record, cohort_state = _lane_registration(task_id, scope, root)
            elif scope is not None:
                raise RuntimeAuthorizationError(
                    "execution_scope supplied but task has no ACTIVE execution cohort"
                )

        if record.get("claimable") is not True and purpose in {"execution", "adopt"}:
            raise RuntimeAuthorizationError("registered task publication is not execution-eligible")
        if record.get("record_state", "ACTIVE") != "ACTIVE" and purpose in {"execution", "adopt"}:
            raise RuntimeAuthorizationError("registered task publication generation is not ACTIVE")

        # A deliberate ACTIVE cohort is its own execution-control lifecycle.
        # Do not let an older task-global result close sibling replication/audit
        # lanes; cohort terminalization is controlled only by cohort synthesis.
        if purpose in {"execution", "adopt"} and scope is None:
            result_state = research_result_records.task_result_state(task_id, root)
            if (
                result_state is not None
                and result_state.get("state") in {"AWAITING_DRIVER_REVIEW", "TERMINAL"}
            ):
                raise RuntimeAuthorizationError(
                    f"task execution is closed by result state {result_state.get('state')}"
                )

        updated["task_registration"] = {
            "state": "IMMUTABLE_REGISTERED",
            "registry_key": task_id,
            "publication_id": record.get("publication_id"),
            "record_path": record.get("_record_path"),
            "claimable": record.get("claimable"),
        }
        if scope is not None and purpose in {"execution", "adopt"}:
            updated["task_registration"]["execution_scope"] = dict(scope)
            updated["task_registration"]["cohort_state"] = cohort_state
        return updated

    if scope is not None:
        raise RuntimeAuthorizationError("execution cohorts require an immutable registered task")
    raise RuntimeAuthorizationError(
        f"task {task_id!r} has no current immutable V2 publication"
    )


def _registered_definition(task_id: str, root: Path) -> dict[str, Any]:
    try:
        record = research_task_records.current_records(root).get(task_id)
    except Exception as exc:
        raise RuntimeAuthorizationError(f"cannot resolve current task publication: {exc}") from exc
    if record is None:
        raise RuntimeAuthorizationError("registered execution has no current immutable publication")
    try:
        return research_dispatch.registered_definition(record, root)
    except Exception as exc:
        raise RuntimeAuthorizationError(f"cannot construct canonical registered task definition: {exc}") from exc


def canonical_live_claim_binding(
    task_id: str,
    events: list[dict[str, Any]],
    *,
    now,
    root: Path = ROOT,
) -> dict[str, Any]:
    """Return the exact currently winning non-cohort CLAIM or fail closed."""
    task = _registered_definition(task_id, root)
    authenticated, _ = research_dispatch._event_authentication_filter(task, events)
    filtered, _ = research_dispatch._filter_registered_events(task, authenticated, root)
    lease = int(task.get("claim_lease_minutes") or 120)
    reduced = research_runtime_reducer.reduce_task(
        task,
        filtered,
        default_lease_minutes=lease,
        now=now,
    )
    if reduced.get("dispatch_state") != "LEASED" or not isinstance(reduced.get("claim_id"), str):
        raise RuntimeAuthorizationError(
            "registered execution requires a current winning live Issue #240 CLAIM"
        )

    ignored = {
        item.get("index")
        for item in reduced.get("ignored_events", [])
        if isinstance(item, dict) and type(item.get("index")) is int
    }
    accepted_claims = [
        event
        for index, event in enumerate(filtered)
        if index not in ignored
        and event.get("task_id") == task_id
        and event.get("event") == "CLAIM"
        and event.get("claim_id") == reduced.get("claim_id")
    ]
    if len(accepted_claims) != 1:
        raise RuntimeAuthorizationError(
            "live owner state has no unique accepted CLAIM provenance"
        )
    claim = accepted_claims[0]
    claim_id = str(reduced["claim_id"])

    try:
        intent = research_execution_records.intent_for_claim(task_id, claim_id, root)
    except Exception as exc:
        raise RuntimeAuthorizationError(f"execution intent lookup failed: {exc}") from exc

    if intent is not None:
        if intent.get("publication_id") != task.get("publication_id"):
            raise RuntimeAuthorizationError("historical execution intent is not bound to current publication")
        if intent.get("taskbook_blob_sha1") != task.get("taskbook_blob_sha1"):
            raise RuntimeAuthorizationError("historical execution intent taskbook pin is stale")
        binding = {
            "publication_id": intent.get("publication_id"),
            "claim_id": claim_id,
            "researcher_id": intent.get("researcher_id"),
            "theorem_owner": intent.get("theorem_owner"),
            "execution_branch": intent.get("execution_branch"),
            "execution_branch_base": intent.get("execution_branch_base"),
            "allowed_outputs": copy.deepcopy(intent.get("allowed_outputs")),
            "taskbook_blob_sha1": intent.get("taskbook_blob_sha1"),
            "binding_source": "IMMUTABLE_EXECUTION_RECORD_COMPATIBILITY",
        }
    else:
        binding = {
            "publication_id": claim.get("publication_id"),
            "claim_id": claim_id,
            "researcher_id": claim.get("researcher_id"),
            "theorem_owner": claim.get("theorem_owner"),
            "execution_branch": claim.get("execution_branch"),
            "execution_branch_base": claim.get("execution_branch_base"),
            "allowed_outputs": copy.deepcopy(claim.get("allowed_outputs")),
            "taskbook_blob_sha1": claim.get("taskbook_blob_sha1"),
            "binding_source": "LIVE_SELF_CONTAINED_CLAIM",
        }

    if binding["publication_id"] != task.get("publication_id"):
        raise RuntimeAuthorizationError("winning CLAIM publication_id is not current")
    if binding["taskbook_blob_sha1"] != task.get("taskbook_blob_sha1"):
        raise RuntimeAuthorizationError("winning CLAIM taskbook pin is not current")
    if binding["researcher_id"] != reduced.get("researcher_id"):
        raise RuntimeAuthorizationError("winning CLAIM researcher identity differs from reduced owner state")
    if not isinstance(binding.get("execution_branch"), str) or not binding["execution_branch"].strip():
        raise RuntimeAuthorizationError("winning CLAIM has no execution_branch")
    if not isinstance(binding.get("execution_branch_base"), str) or len(binding["execution_branch_base"]) != 40:
        raise RuntimeAuthorizationError("winning CLAIM has invalid execution_branch_base")
    outputs = binding.get("allowed_outputs")
    if not isinstance(outputs, list) or not outputs:
        raise RuntimeAuthorizationError("winning CLAIM has no allowed_outputs scope")

    meta = claim.get(research_dispatch.GITHUB_META_KEY)
    if not isinstance(meta, Mapping) or meta.get("control_authorized") is not True:
        raise RuntimeAuthorizationError("winning CLAIM lacks authorized GitHub control provenance")
    binding.update(
        {
            "owner_lease_until": reduced.get("lease_until"),
            "server_comment_id": meta.get("comment_id"),
            "server_author_login": meta.get("author_login"),
            "server_author_user_id": meta.get("author_user_id"),
        }
    )
    return binding


def _binding_for_scope(
    task_id: str,
    scope: dict[str, str] | None,
    events: list[dict[str, Any]],
    *,
    now,
    root: Path,
) -> dict[str, Any]:
    if scope is None:
        return canonical_live_claim_binding(task_id, events, now=now, root=root)
    try:
        return research_lane_claims.winning_lane_claim_binding(
            task_id,
            scope["execution_cohort_id"],
            scope["execution_lane_id"],
            events,
            now=now,
            root=root,
        )
    except Exception as exc:
        raise RuntimeAuthorizationError(f"lane execution authorization failed: {exc}") from exc


def _reconcile_caller_owner_claim(
    state: Mapping[str, Any], binding: Mapping[str, Any]
) -> None:
    supplied = state.get("owner_claim")
    if not isinstance(supplied, Mapping):
        return
    for caller_field, binding_field in (
        ("claim_id", "claim_id"),
        ("researcher_id", "researcher_id"),
        ("execution_cohort_id", "execution_cohort_id"),
        ("execution_lane_id", "execution_lane_id"),
    ):
        value = supplied.get(caller_field)
        if value not in (None, "") and value != binding.get(binding_field):
            raise RuntimeAuthorizationError(
                f"caller owner_claim.{caller_field} does not match canonical winning CLAIM"
            )


def _canonical_owner_claim(binding: Mapping[str, Any]) -> dict[str, Any]:
    value = {
        "claim_id": binding.get("claim_id"),
        "researcher_id": binding.get("researcher_id"),
        "owner_lease_until": binding.get("owner_lease_until"),
        "server_comment_id": binding.get("server_comment_id"),
        "server_author_login": binding.get("server_author_login"),
    }
    if binding.get("execution_cohort_id") is not None:
        value["execution_cohort_id"] = binding.get("execution_cohort_id")
        value["execution_lane_id"] = binding.get("execution_lane_id")
    return value


def _delegate_safe_state(
    state: Mapping[str, Any], *, purpose: str, root: Path = ROOT
) -> dict[str, Any]:
    safe = canonicalize_registration(state, purpose=purpose, root=root)
    if safe["task_registration"]["state"] == "IMMUTABLE_REGISTERED":
        safe["task_registration"]["state"] = "CLAIMABLE"
    return safe


def pre_final_gate(state: Mapping[str, Any], *, root: Path = ROOT) -> dict[str, Any]:
    safe = _delegate_safe_state(state, purpose="pre_final", root=root)
    decision = research_runtime.pre_final_gate(safe)
    decision["registration_authenticated"] = True
    decision["registration_authority"] = "IMMUTABLE_TASK_RECORD"
    return decision


def apply_terminal_event(
    state: Mapping[str, Any], event: str, *, root: Path = ROOT
) -> dict[str, Any]:
    safe = _delegate_safe_state(state, purpose="terminal", root=root)
    value = research_runtime.apply_terminal_event(safe, event)
    value["registration_authenticated"] = True
    return value


def adopt_stale_session(
    state: Mapping[str, Any],
    evidence: Mapping[str, Any],
    *,
    replacement_session_id: str,
    now,
    events: list[dict[str, Any]] | None = None,
    session_liveness_minutes: int = research_runtime.DEFAULT_SESSION_LIVENESS_MINUTES,
    root: Path = ROOT,
) -> dict[str, Any]:
    safe = canonicalize_registration(state, purpose="adopt", root=root)
    if safe["task_registration"]["state"] == "IMMUTABLE_REGISTERED":
        if events is None:
            raise RuntimeAuthorizationError(
                "registered stale adoption requires canonical Issue #240 event evidence"
            )
        scope = _execution_scope(state)
        binding = _binding_for_scope(
            safe["task"]["task_id"], scope, events, now=now, root=root
        )
        _reconcile_caller_owner_claim(state, binding)
        safe["owner_claim"] = _canonical_owner_claim(binding)
        safe["task_registration"]["state"] = "CLAIMABLE"
    return research_runtime.adopt_stale_session(
        safe,
        evidence,
        replacement_session_id=replacement_session_id,
        now=now,
        session_liveness_minutes=session_liveness_minutes,
    )


def authorize_execution(
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


def _load_state(args: argparse.Namespace) -> dict[str, Any]:
    if args.state_json:
        value = json.loads(args.state_json)
    else:
        value = json.loads(Path(args.state_file).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise RuntimeAuthorizationError("state must decode to an object")
    return value


def _add_state(parser: argparse.ArgumentParser) -> None:
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--state-json")
    group.add_argument("--state-file")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Enterprise Math repository-backed runtime guard"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    authorize = sub.add_parser("authorize")
    _add_state(authorize)
    authorize.add_argument("--events", type=Path)
    authorize.add_argument("--now")

    pre = sub.add_parser("pre-final")
    _add_state(pre)

    terminal = sub.add_parser("terminal")
    _add_state(terminal)
    terminal.add_argument(
        "--event",
        choices=[
            "TASK_PUBLISHED",
            "SUBFLOW_COMPLETE",
            "TASK_FROZEN",
            "TASK_COMPLETE",
            "PARENT_OBJECTIVE_COMPLETE",
        ],
        required=True,
    )

    adopt = sub.add_parser("adopt")
    _add_state(adopt)
    adopt.add_argument("--events", type=Path)
    adopt.add_argument("--evidence-json", required=True)
    adopt.add_argument("--replacement-session-id", required=True)
    adopt.add_argument("--now", required=True)
    adopt.add_argument(
        "--session-liveness-minutes",
        type=int,
        default=research_runtime.DEFAULT_SESSION_LIVENESS_MINUTES,
    )

    args = parser.parse_args()
    state = _load_state(args)
    events = research_dispatch.load_events(args.events) if hasattr(args, "events") else None
    if args.command == "authorize":
        result = authorize_execution(
            state,
            events=events,
            now=research_runtime_reducer.now_utc(args.now),
        )
    elif args.command == "pre-final":
        result = pre_final_gate(state)
    elif args.command == "terminal":
        result = apply_terminal_event(state, args.event)
    elif args.command == "adopt":
        evidence = json.loads(args.evidence_json)
        if not isinstance(evidence, dict):
            raise RuntimeAuthorizationError("evidence must decode to an object")
        result = adopt_stale_session(
            state,
            evidence,
            replacement_session_id=args.replacement_session_id,
            now=research_runtime.parse_time(args.now),
            events=events,
            session_liveness_minutes=args.session_liveness_minutes,
        )
    else:
        raise AssertionError(args.command)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeAuthorizationError as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
