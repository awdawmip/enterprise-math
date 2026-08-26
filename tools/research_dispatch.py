#!/usr/bin/env python3
"""Canonical registered-plus-legacy Enterprise Math dispatch view.

Post-cutover task definitions come from immutable task publication records.
The frozen research_scheduler.json remains a compatibility baseline only.
Issue #240 events are reduced by tools/research_scheduler.py only after the
canonical layer has authenticated current live events from GitHub server comment
metadata and authorized the server actor. For registered tasks, the CLAIM comment
itself is the execution envelope; no separate pre-claim repository write is
required.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from tools import research_execution_records
    from tools import research_result_records
    from tools import research_scheduler
    from tools import research_task_records
    from tools import research_taskbook
except ModuleNotFoundError:
    import research_execution_records  # type: ignore
    import research_result_records  # type: ignore
    import research_scheduler  # type: ignore
    import research_task_records  # type: ignore
    import research_taskbook  # type: ignore

ROOT = Path(__file__).resolve().parents[1]
LEGACY = ROOT / "research_scheduler.json"
OWNERS = ROOT / "branch_governance_overrides.json"
CONTROL_AUTHORIZATION = ROOT / "research_control_event_authorization.json"
EVENT_SCHEMA = "ENTERPRISE_MATH_SCHEDULER_EVENT_V1"
CONTROL_AUTH_SCHEMA = "ENTERPRISE_MATH_CONTROL_EVENT_AUTHORIZATION_V1"
GITHUB_META_KEY = "_github"
GITHUB_ISSUE_URL = "https://api.github.com/repos/awdawmip/enterprise-math/issues/240"


class DispatchError(ValueError):
    pass


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def control_authorization_policy(root: Path = ROOT) -> dict[str, Any]:
    path = root / "research_control_event_authorization.json"
    try:
        policy = load_json(path)
    except Exception as exc:
        raise DispatchError(f"cannot load control-event authorization policy: {exc}") from exc
    if policy.get("schema") != CONTROL_AUTH_SCHEMA:
        raise DispatchError("unexpected control-event authorization schema")
    if policy.get("status") != "ACTIVE_CANONICAL":
        raise DispatchError("control-event authorization policy must be ACTIVE_CANONICAL")
    if policy.get("repository") != "awdawmip/enterprise-math" or policy.get("issue") != 240:
        raise DispatchError("control-event authorization policy repository/issue boundary drifted")
    if policy.get("mode") != "EXACT_SERVER_AUTHOR_ALLOWLIST":
        raise DispatchError("unsupported control-event authorization mode")
    authors = policy.get("authorized_server_authors")
    if not isinstance(authors, list) or not authors:
        raise DispatchError("control-event authorization allowlist must be nonempty")
    for index, item in enumerate(authors):
        if not isinstance(item, dict):
            raise DispatchError(f"authorized_server_authors[{index}] must be an object")
        if not isinstance(item.get("login"), str) or not item["login"].strip():
            raise DispatchError(f"authorized_server_authors[{index}].login is required")
        if type(item.get("user_id")) is not int or item["user_id"] <= 0:
            raise DispatchError(f"authorized_server_authors[{index}].user_id must be positive integer")
        associations = item.get("author_association")
        if (
            not isinstance(associations, list)
            or not associations
            or any(not isinstance(value, str) or not value.strip() for value in associations)
        ):
            raise DispatchError(
                f"authorized_server_authors[{index}].author_association must be a nonempty string list"
            )
    return policy


def control_event_authorized(comment: dict[str, Any], *, root: Path = ROOT) -> bool:
    """Authorize the GitHub server actor without trusting event-body identity."""
    policy = control_authorization_policy(root)
    user = comment.get("user")
    if not isinstance(user, dict):
        return False
    login = user.get("login")
    user_id = user.get("id")
    association = comment.get("author_association")
    if not isinstance(login, str) or type(user_id) is not int or not isinstance(association, str):
        return False
    for entry in policy["authorized_server_authors"]:
        if (
            login == entry["login"]
            and user_id == entry["user_id"]
            and association in entry["author_association"]
        ):
            return True
    return False


def _parse_taskbook(record: dict[str, Any], root: Path) -> dict[str, Any]:
    path_value = record.get("taskbook_path")
    if not isinstance(path_value, str) or not path_value:
        raise DispatchError(f"{record.get('task_id')}: task record missing taskbook_path")
    path = root / path_value
    if not path.exists():
        raise DispatchError(f"{record.get('task_id')}: taskbook does not exist")
    meta, _ = research_taskbook.split_taskbook(path.read_text(encoding="utf-8"))
    if meta.get("task_id") != record.get("task_id"):
        raise DispatchError(f"{record.get('task_id')}: taskbook task_id mismatch")
    return meta


def registered_definition(record: dict[str, Any], root: Path = ROOT) -> dict[str, Any]:
    meta = _parse_taskbook(record, root)
    state = str(meta.get("base_state") or "READY")
    if record.get("claimable") is True and state in {"DRAFT", "BACKLOG"}:
        state = "READY"
    if state not in {"BACKLOG", "READY", "HANDOFF_READY", "BLOCKED", "DONE", "SUPERSEDED"}:
        state = "READY" if record.get("claimable") is True else "BACKLOG"
    last_progress_at = meta.get("last_progress_at") or record.get("published_at")
    if not isinstance(last_progress_at, str) or not last_progress_at:
        last_progress_at = "1970-01-01T00:00:00+00:00"
    return {
        "task_id": record["task_id"],
        "title": meta.get("title", record["task_id"]),
        "kind": record.get("kind", meta.get("kind", "RESEARCH")),
        "owner": record.get("owner", meta.get("owner", "taskbook/unassigned")),
        "base_state": state,
        "priority": record.get("effective_priority", meta.get("priority", "P2")),
        "leverage": record.get("effective_leverage", meta.get("leverage", "MEDIUM")),
        "frontier": record.get("frontier", meta.get("frontier", "")),
        "next_action": record.get("next_action", meta.get("next_action", "")),
        "dependencies": copy.deepcopy(meta.get("dependencies", [])),
        "source_refs": copy.deepcopy(meta.get("source_refs", [])),
        "evidence_status": meta.get("evidence_status", "REGISTERED_TASK"),
        "last_progress_ref": meta.get("last_progress_ref") or record.get("publication_id"),
        "last_progress_at": last_progress_at,
        "hard_block": copy.deepcopy(meta.get("hard_block")),
        "tags": copy.deepcopy(meta.get("tags", [])),
        "claim_lease_minutes": int(meta.get("claim_lease_minutes") or 120),
        "identity_lane": meta.get("identity_lane"),
        "publication_id": record.get("publication_id"),
        "taskbook_blob_sha1": record.get("taskbook_blob_sha1"),
        "registration_source": "IMMUTABLE_TASK_RECORD",
    }


def merged_definitions(root: Path = ROOT) -> list[dict[str, Any]]:
    legacy = load_json(root / "research_scheduler.json")
    by_id: dict[str, dict[str, Any]] = {}
    for task in legacy.get("tasks", []):
        if isinstance(task, dict) and isinstance(task.get("task_id"), str):
            value = copy.deepcopy(task)
            value["registration_source"] = "FROZEN_LEGACY_BASELINE"
            by_id[task["task_id"]] = value
    for task_id, record in research_task_records.current_records(root).items():
        by_id[task_id] = registered_definition(record, root)
    return [by_id[key] for key in sorted(by_id)]


def _is_registered(task: dict[str, Any]) -> bool:
    return task.get("registration_source") == "IMMUTABLE_TASK_RECORD"


def _server_time(value: Any, field: str) -> datetime:
    if not isinstance(value, str) or not value.strip():
        raise DispatchError(f"GitHub comment {field} is required")
    try:
        return research_scheduler.parse_time(value)
    except Exception as exc:
        raise DispatchError(f"GitHub comment {field} is invalid") from exc


def github_comment_event(
    comment: dict[str, Any], *, root: Path = ROOT
) -> dict[str, Any] | None:
    """Convert one raw GitHub Issue #240 comment into an authenticated event.

    Non-event human comments return None. Event JSON receives a server envelope.
    The body-provided actor/at remain descriptive provenance only; comment id
    orders the stream, GitHub created_at is the reducer clock, and control authority
    is independently derived from the exact server actor allowlist.
    """
    body = comment.get("body")
    if not isinstance(body, str):
        return None
    try:
        payload = json.loads(body)
    except json.JSONDecodeError:
        return None
    if not isinstance(payload, dict) or payload.get("schema") != EVENT_SCHEMA:
        return None

    comment_id = comment.get("id")
    if type(comment_id) is not int or comment_id <= 0:
        raise DispatchError("scheduler event comment requires positive GitHub comment id")
    issue_url = comment.get("issue_url")
    if issue_url != GITHUB_ISSUE_URL:
        raise DispatchError("scheduler event comment must come from Enterprise Math Issue #240")
    user = comment.get("user")
    author_login = user.get("login") if isinstance(user, dict) else None
    author_user_id = user.get("id") if isinstance(user, dict) else None
    if not isinstance(author_login, str) or not author_login.strip():
        raise DispatchError("scheduler event comment requires GitHub author login")
    created = _server_time(comment.get("created_at"), "created_at")
    updated = _server_time(comment.get("updated_at"), "updated_at")
    app = comment.get("performed_via_github_app")
    app_slug = app.get("slug") if isinstance(app, dict) and isinstance(app.get("slug"), str) else None

    normalized = copy.deepcopy(payload)
    if "at" in normalized:
        normalized["_declared_at"] = normalized.get("at")
    if "actor" in normalized:
        normalized["_declared_actor"] = normalized.get("actor")
    normalized["at"] = created.isoformat()
    normalized[GITHUB_META_KEY] = {
        "server_authenticated": True,
        "issue_number": 240,
        "comment_id": comment_id,
        "author_login": author_login,
        "author_user_id": author_user_id,
        "author_association": comment.get("author_association"),
        "control_authorized": control_event_authorized(comment, root=root),
        "created_at": created.isoformat(),
        "updated_at": updated.isoformat(),
        "body_sha256": "sha256:" + hashlib.sha256(body.encode("utf-8")).hexdigest(),
        "edited": updated != created,
        "performed_via_github_app": app_slug,
    }
    return normalized


def events_from_github_comments(
    comments: list[dict[str, Any]], *, root: Path = ROOT
) -> list[dict[str, Any]]:
    """Extract Issue #240 events in authoritative GitHub comment-id order."""
    ids: set[int] = set()
    ordered: list[dict[str, Any]] = []
    for comment in comments:
        if not isinstance(comment, dict):
            raise DispatchError("GitHub comment export must contain objects")
        comment_id = comment.get("id")
        if type(comment_id) is not int or comment_id <= 0:
            raise DispatchError("GitHub comment export contains invalid comment id")
        if comment_id in ids:
            raise DispatchError(f"duplicate GitHub comment id: {comment_id}")
        ids.add(comment_id)
        ordered.append(comment)
    ordered.sort(key=lambda item: item["id"])
    events: list[dict[str, Any]] = []
    for comment in ordered:
        event = github_comment_event(comment, root=root)
        if event is not None:
            events.append(event)
    return events


def _event_authentication_filter(
    task: dict[str, Any], events: list[dict[str, Any]]
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Fail closed for edited, unauthenticated, or unauthorized live events.

    Bare V1 events remain accepted only for the frozen legacy reducer/replay path.
    Live server events must independently satisfy authentication and actor
    authorization; an unauthorized event-shaped comment is ignored rather than
    allowed to mutate runtime state or abort the entire stream.
    """
    accepted: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []
    for index, event in enumerate(events):
        if event.get("task_id") != task.get("task_id"):
            accepted.append(event)
            continue
        meta = event.get(GITHUB_META_KEY)
        if meta is None:
            if _is_registered(task):
                rejected.append({
                    "index": index,
                    "reason": "live registered event requires server-authenticated GitHub Issue #240 comment envelope",
                })
                continue
            accepted.append(event)
            continue
        if not isinstance(meta, dict) or meta.get("server_authenticated") is not True:
            rejected.append({"index": index, "reason": "invalid GitHub event authentication envelope"})
            continue
        if meta.get("issue_number") != 240 or type(meta.get("comment_id")) is not int:
            rejected.append({"index": index, "reason": "GitHub event envelope issue/comment identity is invalid"})
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
                "reason": "edited scheduler event comment is not runtime authority; append a correction event instead",
            })
            continue
        accepted.append(event)
    return accepted, rejected


def _inline_claim_envelope(
    task: dict[str, Any], event: dict[str, Any]
) -> tuple[dict[str, Any] | None, str | None]:
    """Validate one self-contained registered CLAIM without another repo write."""
    claim_id = event.get("claim_id")
    if not isinstance(claim_id, str) or not claim_id:
        return None, "registered CLAIM requires claim_id"
    if event.get("publication_id") != task.get("publication_id"):
        return None, "registered CLAIM publication_id does not match current task publication"
    theorem_owner = event.get("theorem_owner")
    if not isinstance(theorem_owner, str) or not theorem_owner.strip():
        return None, "registered CLAIM requires theorem_owner"
    execution_branch = event.get("execution_branch")
    if not isinstance(execution_branch, str) or not execution_branch.strip():
        return None, "registered CLAIM requires execution_branch"
    execution_branch_base = event.get("execution_branch_base")
    if not isinstance(execution_branch_base, str) or not re.fullmatch(
        r"[0-9a-fA-F]{40}", execution_branch_base.strip()
    ):
        return None, "registered CLAIM requires a 40-hex execution_branch_base"
    allowed_outputs = event.get("allowed_outputs")
    if (
        not isinstance(allowed_outputs, list)
        or not allowed_outputs
        or any(not isinstance(item, str) or not item.strip() for item in allowed_outputs)
        or len(set(allowed_outputs)) != len(allowed_outputs)
    ):
        return None, "registered CLAIM requires unique nonempty allowed_outputs"
    lease = event.get("lease_minutes", task.get("claim_lease_minutes", 120))
    if type(lease) is not int or lease <= 0:
        return None, "registered CLAIM lease_minutes must be a positive integer"
    supplied = event.get("researcher_id")
    if supplied is None:
        try:
            researcher_id = research_scheduler.researcher_id_for_claim(task, claim_id)
        except Exception as exc:
            return None, f"registered CLAIM could not derive researcher_id: {exc}"
    elif not research_scheduler.valid_researcher_id(supplied):
        return None, "registered CLAIM researcher_id has invalid format"
    else:
        researcher_id = str(supplied).strip().upper()
    normalized = copy.deepcopy(event)
    normalized["researcher_id"] = researcher_id
    normalized["lease_minutes"] = lease
    normalized["taskbook_blob_sha1"] = task.get("taskbook_blob_sha1")
    normalized["execution_branch_base"] = execution_branch_base.lower()
    return normalized, None


def _filter_registered_events(
    task: dict[str, Any], events: list[dict[str, Any]], root: Path
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    if not _is_registered(task):
        return events, []
    result_state = research_result_records.task_result_state(task["task_id"], root)
    terminal_result_id = None
    if result_state is not None and result_state.get("terminal") is True:
        terminal_result_id = result_state["result"].get("result_id")
    accepted: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []
    for index, event in enumerate(events):
        if event.get("task_id") != task["task_id"]:
            accepted.append(event)
            continue
        kind = event.get("event")
        if kind == "CLAIM":
            claim_id = event.get("claim_id")
            if not isinstance(claim_id, str) or not claim_id:
                accepted.append(event)
                continue

            # Compatibility: an already-frozen intent may still authorize a CLAIM.
            try:
                intent = research_execution_records.intent_for_claim(task["task_id"], claim_id, root)
            except Exception as exc:
                rejected.append({"index": index, "reason": f"execution intent lookup failed: {exc}"})
                continue
            if intent is not None:
                supplied = event.get("researcher_id")
                if supplied is not None and str(supplied).strip().upper() != intent["researcher_id"]:
                    rejected.append({
                        "index": index,
                        "reason": "registered CLAIM researcher_id does not match execution intent",
                    })
                    continue
                normalized = copy.deepcopy(event)
                normalized["researcher_id"] = intent["researcher_id"]
                normalized.setdefault("lease_minutes", intent["owner_lease_minutes"])
                accepted.append(normalized)
                continue

            # Preferred low-burden path: CLAIM itself carries the execution envelope.
            normalized, reason = _inline_claim_envelope(task, event)
            if normalized is None:
                rejected.append({
                    "index": index,
                    "reason": reason or "registered CLAIM execution envelope is invalid",
                })
                continue
            accepted.append(normalized)
            continue
        if kind == "DONE":
            if not terminal_result_id:
                rejected.append({
                    "index": index,
                    "reason": "registered DONE requires a frozen result with terminal Driver review",
                })
                continue
            if event.get("result_id") != terminal_result_id:
                rejected.append({
                    "index": index,
                    "reason": "registered DONE result_id does not match terminal reviewed result",
                })
                continue
        accepted.append(event)
    return accepted, rejected


def _overlay_result_state(
    task: dict[str, Any], state: dict[str, Any], root: Path
) -> dict[str, Any]:
    if not _is_registered(task):
        return state
    result_state = research_result_records.task_result_state(task["task_id"], root)
    if result_state is None:
        return state
    value = copy.deepcopy(state)
    result = result_state["result"]
    review = result_state.get("review")
    value["result_id"] = result.get("result_id")
    value["result_record_path"] = result.get("_record_path")
    if result_state["state"] == "AWAITING_DRIVER_REVIEW":
        value["state"] = "FROZEN_RETURN"
        value["dispatch_state"] = "AWAITING_REVIEW"
        value["next_action"] = "Driver review required before terminal closure or researcher redispatch"
        return value
    if result_state["state"] == "RETURN_TO_EXECUTION":
        value["state"] = "HANDOFF_READY"
        value["dispatch_state"] = "NEEDS_DISPATCH"
        value["claim_id"] = None
        value["actor"] = None
        value["researcher_id"] = None
        value["identity_source"] = None
        value["lease_until"] = None
        value["driver_disposition"] = review.get("disposition") if review else None
        value["next_action"] = "Resume task under Driver disposition"
        return value
    if result_state["state"] == "TERMINAL":
        value["state"] = "DONE"
        value["dispatch_state"] = "COMPLETE"
        value["claim_id"] = None
        value["actor"] = None
        value["researcher_id"] = None
        value["identity_source"] = None
        value["lease_until"] = None
        value["driver_disposition"] = review.get("disposition") if review else None
        value["review_id"] = review.get("review_id") if review else None
        return value
    return value


def _authentication_summary(task: dict[str, Any], events: list[dict[str, Any]]) -> dict[str, Any]:
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
    if matching:
        return {
            "event_authentication": "LEGACY_BARE_EVENT_REPLAY",
            "last_server_comment_id": None,
            "last_server_author_login": None,
        }
    return {
        "event_authentication": "NO_RUNTIME_EVENT",
        "last_server_comment_id": None,
        "last_server_author_login": None,
    }


def reduce_definition(
    task: dict[str, Any],
    events: list[dict[str, Any]],
    *,
    now: datetime,
    default_lease_minutes: int = 120,
    root: Path = ROOT,
) -> dict[str, Any]:
    authenticated, auth_rejected = _event_authentication_filter(task, events)
    filtered, registered_rejected = _filter_registered_events(task, authenticated, root)
    lease = int(task.get("claim_lease_minutes") or default_lease_minutes)
    state = research_scheduler.reduce_task(
        task,
        filtered,
        default_lease_minutes=lease,
        now=now,
    )
    state["ignored_events"].extend(auth_rejected)
    state["ignored_events"].extend(registered_rejected)
    state.update({
        "title": task.get("title"),
        "kind": task.get("kind"),
        "owner": task.get("owner"),
        "priority": task.get("priority"),
        "leverage": task.get("leverage"),
        "frontier": task.get("frontier"),
        "source_refs": task.get("source_refs", []),
        "registration_source": task.get("registration_source"),
        "publication_id": task.get("publication_id"),
    })
    state.update(_authentication_summary(task, events))
    try:
        state["identity_lane"] = research_scheduler.identity_lane(task)
    except Exception:
        state["identity_lane"] = task.get("identity_lane")
    return _overlay_result_state(task, state, root)


def effective_states(
    events: list[dict[str, Any]], *, now: datetime, root: Path = ROOT
) -> list[dict[str, Any]]:
    return [
        reduce_definition(task, events, now=now, root=root)
        for task in merged_definitions(root)
    ]


def select_task(
    events: list[dict[str, Any]],
    *,
    now: datetime,
    kind: str = "RESEARCH",
    root: Path = ROOT,
) -> dict[str, Any] | None:
    legacy = load_json(root / "research_scheduler.json")
    policy = legacy["selection_policy"]
    states = effective_states(events, now=now, root=root)
    state_rank = {name: index for index, name in enumerate(policy["state_order"])}
    priority_rank = {name: index for index, name in enumerate(policy["priority_order"])}
    leverage_rank = {name: index for index, name in enumerate(policy["leverage_order"])}
    candidates = [
        item for item in states
        if item.get("dispatch_state") == "NEEDS_DISPATCH"
        and (kind == "ANY" or item.get("kind") == kind)
    ]
    if not candidates:
        return None

    def key(item: dict[str, Any]):
        try:
            last = research_scheduler.parse_time(item.get("last_progress_at", ""))
        except Exception:
            last = datetime(1970, 1, 1, tzinfo=timezone.utc)
        return (
            state_rank.get(item.get("state"), len(state_rank)),
            priority_rank.get(item.get("priority"), len(priority_rank)),
            leverage_rank.get(item.get("leverage"), len(leverage_rank)),
            last,
            item.get("task_id", ""),
        )

    return min(candidates, key=key)


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    legacy = load_json(root / "research_scheduler.json")
    owners = load_json(root / "branch_governance_overrides.json")
    try:
        control_authorization_policy(root)
    except Exception as exc:
        errors.append(f"control-event authorization policy failure: {exc}")
    errors.extend(research_scheduler.validate_scheduler(legacy, owners))
    errors.extend(research_task_records.audit(root))
    errors.extend(research_execution_records.audit(root))
    errors.extend(research_result_records.audit(root))
    try:
        definitions = merged_definitions(root)
    except Exception as exc:
        errors.append(f"merged dispatch definition failure: {exc}")
        return errors
    ids = [item.get("task_id") for item in definitions]
    if len(ids) != len(set(ids)):
        errors.append("canonical merged dispatch view contains duplicate task IDs")
    current = research_task_records.current_records(root)
    for task_id in current:
        matches = [item for item in definitions if item.get("task_id") == task_id]
        if len(matches) != 1 or matches[0].get("registration_source") != "IMMUTABLE_TASK_RECORD":
            errors.append(f"{task_id}: registered task is not canonical in merged dispatch view")
    return errors


def _decode_event_input(path: Path) -> list[dict[str, Any]]:
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        return []
    if text.startswith("["):
        data = json.loads(text)
        if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
            raise DispatchError("event input array must contain objects")
        return data
    values = [json.loads(line) for line in text.splitlines() if line.strip()]
    if not all(isinstance(item, dict) for item in values):
        raise DispatchError("event JSONL must contain objects")
    return values


def load_events(path: Path | None) -> list[dict[str, Any]]:
    if path is None:
        return []
    values = _decode_event_input(path)
    if not values:
        return []
    looks_like_comments = any(
        "body" in item and "id" in item and "user" in item for item in values
    )
    if looks_like_comments:
        if not all("body" in item and "id" in item and "user" in item for item in values):
            raise DispatchError("do not mix GitHub comment objects with bare scheduler events")
        return events_from_github_comments(values)
    # Explicit compatibility path for frozen historical replay and pure unit tests.
    return research_scheduler.load_events(path)


def main() -> int:
    parser = argparse.ArgumentParser(description="Enterprise Math canonical registered-plus-legacy dispatch")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate")
    status = sub.add_parser("status")
    status.add_argument("--events", type=Path)
    status.add_argument("--now")
    select = sub.add_parser("select")
    select.add_argument("--events", type=Path)
    select.add_argument("--now")
    select.add_argument("--kind", choices=["RESEARCH", "GOVERNANCE", "ANY"], default="RESEARCH")
    args = parser.parse_args()
    if args.command == "validate":
        errors = validate()
        if errors:
            for error in errors:
                print("ERROR:", error)
            return 1
        print(
            f"PASS: canonical dispatch valid; {len(merged_definitions())} merged task definition(s), "
            f"{len(research_task_records.current_records())} immutable registered task(s)."
        )
        return 0
    events = load_events(args.events)
    now = research_scheduler.now_utc(args.now)
    if args.command == "status":
        print(json.dumps(effective_states(events, now=now), ensure_ascii=False, indent=2, sort_keys=True))
        return 0
    chosen = select_task(events, now=now, kind=args.kind)
    print(json.dumps(chosen, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if chosen is not None else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except DispatchError as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
