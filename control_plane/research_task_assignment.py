"""Typed Driver-to-researcher selection from existing Issue 240 envelopes.

Assignments are control events, not task records or owner claims. The current
immutable TP2 remains the only task authority. No store is added by this module.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any, Mapping

import research_driver_authority
from tools import research_dispatch, research_identity, research_runtime_reducer

SCHEMA = "ENTERPRISE_MATH_ASSIGNED_RESEARCH_TASK_REQUEST_V1"
ASSIGN = "ASSIGN_RESEARCH_TASK"
REVOKE = "REVOKE_RESEARCH_TASK_ASSIGNMENT"
EVENTS = frozenset({ASSIGN, REVOKE})
SCOPE_FIELD = "research_task_delegation_scope"
_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,191}$")
_DIGEST = re.compile(r"^sha256:[0-9a-f]{64}$")
_SCOPE = ("task_id", "publication_id", "parent_objective_id")
_RECIPIENT = ("researcher_id", "session_id", "executor_role")
_REQUEST_FIELDS = frozenset({
    "schema", "assignment_comment_id", "assignment_body_sha256", "driver_id",
    "driver_authority_record_id", "driver_authority_record_sha256",
    "expected_claim_id", *_SCOPE, *_RECIPIENT,
})


class AssignmentError(ValueError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise AssignmentError(message)


def _session_id(value: Any) -> bool:
    # Match parse_session_observations: a nonblank opaque string retained exactly.
    # Existing session keys may contain colons, slashes or other non-ID syntax.
    return isinstance(value, str) and bool(value.strip())


def validate_request(request: Mapping[str, Any], *, kind: str) -> dict[str, Any]:
    _require(isinstance(request, Mapping) and set(request) == _REQUEST_FIELDS,
             "research assignment request requires exactly the typed fields")
    _require(request["schema"] == SCHEMA and kind == "RESEARCH",
             "research assignment entry requires kind RESEARCH and its own schema")
    for field in _REQUEST_FIELDS - {"assignment_comment_id", "expected_claim_id", "session_id"}:
        value = request[field]
        _require(isinstance(value, str) and bool(value) and value == value.strip(),
                 f"research assignment request missing or malformed {field}")
    _require(_session_id(request["session_id"]), "research assignment requires a nonblank opaque session_id")
    _require(type(request["assignment_comment_id"]) is int and request["assignment_comment_id"] > 0,
             "assignment_comment_id must be an actual positive server comment ID")
    for field in ("assignment_body_sha256", "driver_authority_record_sha256"):
        _require(bool(_DIGEST.fullmatch(request[field])), f"malformed {field}")
    _require(request["expected_claim_id"] is None or (
        isinstance(request["expected_claim_id"], str) and bool(request["expected_claim_id"].strip())
        and request["expected_claim_id"] == request["expected_claim_id"].strip()),
        "expected_claim_id must be null or one exact claim ID")
    recipient = request["researcher_id"]
    _require(request["executor_role"] == "RESEARCHER" and recipient == recipient.upper()
             and research_identity.valid_execution_id(recipient)
             and not recipient.startswith(("EM-DVR-", "EM-DRIVER-", "EM-STW-"))
             and recipient != request["driver_id"],
             "assignment recipient must be a distinct typed RESEARCHER identity")
    for field in _SCOPE:
        _require(bool(_ID.fullmatch(request[field])), f"malformed exact {field}")
    return dict(request)


def _parent_scope(authority: Mapping[str, Any], parent: str) -> bool:
    source = json.loads(authority["source_body"])
    if not isinstance(source, dict):
        return False
    scope = source.get(SCOPE_FIELD)
    if not isinstance(scope, dict) or set(scope) != {"parent_objective_ids"}:
        return False
    parents = scope["parent_objective_ids"]
    return (isinstance(parents, list) and bool(parents)
            and all(isinstance(item, str) and _ID.fullmatch(item) for item in parents)
            and len(set(parents)) == len(parents) and parent in parents)


def resolve(
    request: Mapping[str, Any], events: list[dict[str, Any]], *, now, root: Path
) -> dict[str, Any]:
    """Resolve one unrevoked assignment without choosing among conflicting ones.

    Event input is the existing normalized stream produced from raw GitHub
    comments by research_dispatch.load_events. Its server metadata is rechecked;
    body actor/time and an arbitrary request are never delegation authority.
    """
    authorities: dict[str, dict[str, Any] | None] = {}

    def current_authority(driver_id: str) -> dict[str, Any] | None:
        if driver_id not in authorities:
            authorities[driver_id] = research_driver_authority.active_authority_at(
                driver_id, now.isoformat(), root)
        return authorities[driver_id]

    authority = current_authority(request["driver_id"])
    _require(authority is not None and authority["authority_record_id"] == request["driver_authority_record_id"],
             "research assignment must pin the Driver's current ACTIVE authority")
    authority_bytes = root.joinpath(authority["_record_path"]).read_bytes()
    authority_digest = "sha256:" + hashlib.sha256(authority_bytes).hexdigest()
    _require(authority_digest == request["driver_authority_record_sha256"],
             "research assignment Driver authority bytes changed")
    _require(_parent_scope(authority, request["parent_objective_id"]),
             "current AUTHORIZE lacks this typed research parent delegation scope")

    relevant = [event for event in events if event.get("event") in EVENTS
                and event.get("task_id") == request["task_id"]
                and event.get("publication_id") == request["publication_id"]]
    candidates: list[dict[str, Any]] = []
    invalid: dict[int, str] = {}
    seen: set[int] = set()
    for event in relevant:
        meta = event.get(research_dispatch.GITHUB_META_KEY)
        cid = meta.get("comment_id") if isinstance(meta, dict) else None
        if type(cid) is not int or cid <= 0:
            continue
        _require(cid not in seen, "duplicate assignment server comment ID")
        seen.add(cid)
        accepted, rejected = research_dispatch._event_authentication_filter(
            {"task_id": request["task_id"]}, [event])
        if not accepted or rejected or meta.get("edited") is not False:
            invalid[cid] = "assignment requires an authorized unedited Issue 240 server envelope"
            continue
        author = {"login": meta.get("author_login"), "user_id": meta.get("author_user_id"),
                  "author_association": meta.get("author_association")}
        if not research_driver_authority._server_author_allowed(author, root):
            invalid[cid] = "assignment server actor is not control-authorized"
            continue
        try:
            created = research_runtime_reducer.parse_time(meta["created_at"])
            updated = research_runtime_reducer.parse_time(meta["updated_at"])
            driver = event.get("driver_id")
            if not isinstance(driver, str):
                raise AssignmentError("assignment has no issuing Driver")
            event_authority = current_authority(driver)
            valid = (event.get("schema") == research_dispatch.EVENT_SCHEMA
                     and created == updated and created <= now
                     and isinstance(meta.get("body_sha256"), str)
                     and bool(_DIGEST.fullmatch(meta["body_sha256"]))
                     and event_authority is not None
                     and event_authority["authority_record_id"] == event.get("driver_authority_record_id")
                     and event_authority["source_comment_id"] == event.get("driver_authority_source_comment_id")
                     and event_authority["source_comment_id"] < cid
                     and research_runtime_reducer.parse_time(event_authority["source_created_at"]) <= created
                     and event.get("parent_objective_id") == request["parent_objective_id"]
                     and _parent_scope(event_authority, request["parent_objective_id"]))
            if not valid:
                raise AssignmentError("assignment authority/time/current parent scope does not match")
        except (AssignmentError, KeyError, TypeError, ValueError) as exc:
            invalid[cid] = str(exc)
            continue
        candidates.append(event)

    active: dict[int, dict[str, Any]] = {}
    for event in sorted(candidates, key=lambda row: row[research_dispatch.GITHUB_META_KEY]["comment_id"]):
        cid = event[research_dispatch.GITHUB_META_KEY]["comment_id"]
        if event["event"] == ASSIGN:
            recipient = event.get("researcher_id")
            session = event.get("session_id")
            if (event.get("executor_role") != "RESEARCHER" or not isinstance(recipient, str)
                    or recipient != recipient.upper() or not research_identity.valid_execution_id(recipient)
                    or recipient.startswith(("EM-DVR-", "EM-DRIVER-", "EM-STW-"))
                    or recipient == event.get("driver_id")
                    or not _session_id(session)):
                invalid[cid] = "assignment requires a distinct exact researcher/session binding"
                continue
            active[cid] = event
        else:
            revoked_id = event.get("assignment_comment_id")
            prior = active.get(revoked_id) if type(revoked_id) is int else None
            if prior is not None and prior["driver_id"] == event["driver_id"]:
                active.pop(revoked_id)

    selected_id = request["assignment_comment_id"]
    _require(selected_id in active, invalid.get(selected_id,
             "requested assignment is absent, revoked, or no longer under current Driver authority"))
    selected = active[selected_id]
    _require(all(selected.get(key) == request[key] for key in (*_SCOPE, *_RECIPIENT, "driver_id")),
             "assignment source does not match the exact task and receiving researcher/session")
    _require(selected[research_dispatch.GITHUB_META_KEY]["body_sha256"] == request["assignment_body_sha256"],
             "assignment source body digest changed")
    _require(len(active) == 1, "multiple active research assignments require explicit revocation; no recency selection")
    meta = selected[research_dispatch.GITHUB_META_KEY]
    return {
        "schema": SCHEMA, **{field: request[field] for field in (*_SCOPE, *_RECIPIENT, "driver_id")},
        "assignment_comment_id": selected_id, "assignment_body_sha256": meta["body_sha256"],
        "assignment_created_at": meta["created_at"],
        "driver_authority_record_id": authority["authority_record_id"],
        "driver_authority_record_sha256": authority_digest,
        "driver_authority_source_comment_id": authority["source_comment_id"],
        "validated_at": now.isoformat(), "expected_claim_id": request["expected_claim_id"],
        "preclaim_selection_reconstructed": False, "execution_authorized": False,
        "parent_completion_granted": False, "task_authority": "CURRENT_IMMUTABLE_TP2",
    }
