"""Source-backed continuation; a conversation is never the durable task owner.

These read/prepare APIs do not publish events or authorize execution. ``events``
is the canonical normalized server-comment stream; ``source_commit`` is supplied
by the trusted snapshot loader, never by an untrusted MCP argument. Existing V2
publication, Result, review, cohort and discovery gates remain authoritative.
"""
from __future__ import annotations

import copy
import base64
import hashlib
import json
import os
import re
import subprocess
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path, PurePosixPath
from typing import Any, Mapping
from urllib.parse import unquote, urlsplit

SCHEMA = "ENTERPRISE_MATH_CLAIM_CONTINUATION_V1"
REPOSITORY = "awdawmip/enterprise-math"
POLICY = "control_plane/executor_succession_policy.json"
HEX40 = re.compile(r"^[0-9a-f]{40}$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")


class ContinuationError(ValueError):
    pass


def write_gate_enabled(root: Path) -> bool:
    path = root / POLICY
    return path.exists() and json.loads(path.read_text(encoding="utf-8")).get("canonical_freeze_requires_current_runtime_authorization") is True


def require_freeze_authority(record: Mapping[str, Any], args: Any, *, root: Path) -> dict[str, Any] | None:
    """Prospective writer gate; immutable historical results are never rejudged."""
    if not write_gate_enabled(root):
        return
    from tools import research_dispatch, research_runtime_guard
    state_file, events_file = getattr(args, "runtime_state_file", None), getattr(args, "events", None)
    _require(bool(state_file) and bool(events_file), "canonical freeze requires --runtime-state-file and --events with current authenticated ownership")
    state = json.loads(Path(state_file).read_text(encoding="utf-8"))
    authorized_at = datetime.now(timezone.utc)
    decision = research_runtime_guard.authorize_execution(state,
        events=research_dispatch.load_events(Path(events_file)), now=authorized_at, root=root)
    binding = decision["execution_binding"]
    _require(decision.get("authorized") is True and decision["task_id"] == record["task_id"], "freeze task is not currently authorized")
    for key in ("claim_id", "publication_id", "researcher_id", "execution_branch", "taskbook_blob_sha1"):
        _require(record.get(key) == binding.get(key), f"freeze {key} belongs to a fenced or different execution")
    source = verify_source_snapshot(root, getattr(args, "source_commit", None))
    raw = json.loads(Path(events_file).read_text(encoding="utf-8"))
    _require(isinstance(raw, list), "freeze receipt requires the raw GitHub comment JSON array")
    comments = []
    for comment in raw:
        try:
            body = json.loads(comment.get("body", ""))
        except (ValueError, TypeError):
            continue
        if isinstance(body, dict) and body.get("task_id") == record["task_id"]:
            comments.append(comment)
    session = (state.get("session") or {}).get("session_id")
    _require(_text(session), "freeze requires the current execution session identity")
    context = {"source_commit": source, "authorized_at": authorized_at.isoformat(),
            "principal": {"claim_id": record["claim_id"], "researcher_id": record["researcher_id"],
                          "session_id": session, "ownership_epoch": binding.get("ownership_epoch", binding.get("server_comment_id")),
                          "executor_role": binding.get("executor_role", "RESEARCHER"),
                          "driver_authority_record_id": binding.get("driver_authority_record_id")},
            "server_comments": comments, "task_definition": _definition(record["task_id"], root),
            "taskbook_content_base64": base64.b64encode(_path(root, record["taskbook_path"]).read_bytes()).decode()}
    if binding.get("executor_role") == "RESEARCH_DRIVER":
        import research_driver_authority
        context["authority_observed_through_comment_id"] = max(row["source_comment_id"] for row in research_driver_authority.valid_records(root))
    return context


def require_review_authority(result: Mapping[str, Any], args: Any, *, root: Path) -> dict[str, Any] | None:
    if not write_gate_enabled(root):
        return None
    import research_driver_authority
    _require(_text(getattr(args, "reviewer_session_id", None)), "review requires its current declared execution session")
    authority = research_driver_authority.require_active_driver(args.driver_id, datetime.now(timezone.utc).isoformat(), root)
    _require(authority is not None, "canonical review requires current source-backed Driver authority")
    payload = json.loads(authority["source_body"])
    succession = payload.get("succession")
    session = payload.get("session_id") or (succession.get("session_id") if succession is not None else None)
    _require(_text(session), "new review requires explicitly session-bound Driver authority; historical sessionless DA must be replaced by a real new activation")
    _require(getattr(args, "reviewer_session_id", None) == session, "successor Driver review requires exact current session binding")
    declared = getattr(args, "reviewer_contribution_ids_json", None)
    _require(declared is not None, "review requires explicit --reviewer-contribution-ids-json; a new identity does not erase authorship")
    try:
        identities = json.loads(declared)
    except (ValueError, TypeError) as exc:
        raise ContinuationError("reviewer contribution identities must be JSON") from exc
    _require(isinstance(identities, list) and all(_text(item) for item in identities), "reviewer contribution identities must be an explicit string list")
    authors = set(result.get("contributor_ids", [])) | {result.get("researcher_id")}
    overlapping = authors & (set(identities) | {args.driver_id})
    _require(not overlapping, "reviewer contributed to this result; obtain a distinct decisive reviewer before canonical review")
    return authority


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ContinuationError(message)


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _source(source_commit: str) -> str:
    _require(isinstance(source_commit, str) and bool(HEX40.fullmatch(source_commit)),
             "trusted source_commit must be a 40-hex immutable snapshot")
    return source_commit


def verify_source_snapshot(root: Path, source_commit: str) -> str:
    """Bind control source to the host's actual checkout or trusted loader marker."""
    _source(source_commit)
    if (root / ".git").exists():
        env = {**os.environ, "GIT_NO_LAZY_FETCH": "1"}
        result = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"], capture_output=True,
                                text=True, check=False, env=env, timeout=10)
        _require(result.returncode == 0 and result.stdout.strip() == source_commit,
                 "control source_commit differs from actual local Git HEAD")
        return source_commit
    marker = root / "EM_SNAPSHOT_READY.json"
    if marker.exists():
        _require(json.loads(marker.read_text(encoding="utf-8")).get("sha") == source_commit,
                 "control source_commit differs from the trusted Source loader snapshot")
        return source_commit
    # The service creates this marker only after copying its verified immutable
    # snapshot; it is an operator assertion, never a platform identity signature.
    sandbox = root / "EM_CONTINUATION_WRITE_SANDBOX.json"
    if sandbox.exists():
        value = json.loads(sandbox.read_text(encoding="utf-8"))
        _require(value == {"schema": "ENTERPRISE_MATH_ISOLATED_WRITE_SANDBOX_V1", "source_commit": source_commit, "isolated": True},
                 "control source_commit differs from isolated trusted writer snapshot")
        return source_commit
    raise ContinuationError("control source requires an actual Git HEAD or trusted loader snapshot marker")


def _path(root: Path, relative: str) -> Path:
    _require(_text(relative) and "\\" not in relative, "artifact requires repository-relative POSIX path")
    parts = PurePosixPath(relative)
    _require(not parts.is_absolute() and not set(parts.parts) & {"..", ".git"}, "unsafe artifact path")
    resolved = (root / relative).resolve()
    _require(resolved.is_relative_to(root.resolve()) and resolved.is_file(), "artifact is absent or outside snapshot")
    return resolved


def artifact_pin(root: Path, relative: str, source_commit: str, *,
                 evidence_roots: Mapping[str, Path] | None = None) -> dict[str, str]:
    """Pin actual immutable bytes, never relabel dirty working bytes as HEAD."""
    _source(source_commit)
    _require(_text(relative) and "\\" not in relative and not PurePosixPath(relative).is_absolute()
             and not set(PurePosixPath(relative).parts) & {"..", ".git"}, "unsafe immutable artifact path")
    evidence_root = Path((evidence_roots or {}).get(source_commit, root))
    if (evidence_root / ".git").exists():
        env = {**os.environ, "GIT_NO_LAZY_FETCH": "1"}
        result = subprocess.run(["git", "-C", str(evidence_root), "cat-file", "blob", f"{source_commit}:{relative}"],
                                capture_output=True, check=False, env=env, timeout=10)
        _require(result.returncode == 0, "DRAFT_OR_UNVERIFIED: artifact has no available immutable Git object; obtain an actual readback")
        data = result.stdout
        head = subprocess.run(["git", "-C", str(evidence_root), "rev-parse", "HEAD"], capture_output=True,
                              text=True, check=False, env=env, timeout=10)
        if head.returncode == 0 and head.stdout.strip() == source_commit:
            _require(_path(evidence_root, relative).read_bytes() == data,
                     "DRAFT_OR_UNVERIFIED: working bytes differ from the immutable HEAD artifact")
    else:
        manifest_path = evidence_root / "EM_SOURCE_BLOBS.json"
        _require(manifest_path.is_file(), "DRAFT_OR_UNVERIFIED: immutable artifact requires the trusted loader blob manifest")
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        _require(manifest.get("schema") == "ENTERPRISE_MATH_SOURCE_BLOB_MANIFEST_V1"
                 and manifest.get("source_commit") == source_commit, "artifact source commit differs from trusted loader manifest")
        expected = manifest.get("blobs", {}).get(relative)
        _require(isinstance(expected, str) and bool(HEX40.fullmatch(expected)), "DRAFT_OR_UNVERIFIED: artifact absent from immutable source manifest")
        data = _path(evidence_root, relative).read_bytes()
        _require(hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest() == expected,
                 "DRAFT_OR_UNVERIFIED: working bytes differ from trusted immutable source manifest")
    return {"repository": REPOSITORY, "source_commit": _source(source_commit), "path": relative,
            "git_blob_sha1": hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest(),
            "sha256": hashlib.sha256(data).hexdigest()}


def validate_frontier(frontier: Mapping[str, Any], *, root: Path,
                      source_commit: str | None = None, verify_artifacts: bool = True,
                      evidence_roots: Mapping[str, Path] | None = None) -> None:
    _require(isinstance(frontier, Mapping), "continuation frontier must be an object")
    commit = _source(frontier.get("source_commit"))
    if source_commit is not None:
        verify_source_snapshot(root, source_commit)
    for key in ("current_unfinished_unit", "next_action"):
        _require(_text(frontier.get(key)), f"frontier requires {key}")
    pins = frontier.get("artifacts")
    _require(isinstance(pins, list) and bool(pins) and len(pins) <= 64, "frontier requires 1..64 immutable artifact pins")
    seen = set()
    for pin in pins:
        _require(isinstance(pin, dict), "frontier artifact pin must be an object")
        relative = pin.get("path")
        _require(_text(relative), "frontier artifact path must be a string")
        key = (pin.get("source_commit"), relative)
        _require(key not in seen, "duplicate frontier artifact")
        seen.add(key)
        _require(_text(relative) and not PurePosixPath(relative).is_absolute() and ".." not in PurePosixPath(relative).parts,
                 "invalid frontier artifact path")
        _require(pin.get("repository") == REPOSITORY and bool(HEX40.fullmatch(str(pin.get("source_commit", ""))))
                 and bool(HEX40.fullmatch(str(pin.get("git_blob_sha1", ""))))
                 and bool(HEX64.fullmatch(str(pin.get("sha256", "")))), "invalid immutable frontier pin")
        if verify_artifacts:
            expected = artifact_pin(root, relative, pin["source_commit"], evidence_roots=evidence_roots)
            _require(all(pin.get(key) == value for key, value in expected.items()), "frontier artifact bytes or immutable source binding changed")
    for key in ("completed_units", "do_not_repeat", "contributor_ids"):
        value = frontier.get(key)
        _require(isinstance(value, list) and all(_text(item) for item in value), f"frontier requires explicit {key} list")
    _require(bool(frontier["contributor_ids"]), "frontier must preserve predecessor contribution provenance")


def validate_claim_continuation(task: Mapping[str, Any], event: Mapping[str, Any], *, root: Path,
                                verify_artifacts: bool = False,
                                evidence_roots: Mapping[str, Path] | None = None) -> None:
    """Validate static scope/bytes; the reducer applies the winning-owner CAS."""
    value = event.get("continuation")
    _require(isinstance(value, Mapping) and value.get("schema") == SCHEMA, "invalid typed CLAIM continuation")
    _require(value.get("mode") in {"TAKEOVER", "RESUME"}, "invalid continuation mode")
    _require(event.get("publication_id") == task.get("publication_id"), "continuation publication mismatch")
    for key in ("expected_previous_claim_id", "previous_researcher_id", "session_id", "reason"):
        _require(_text(value.get(key)), f"continuation requires {key}")
    cid = value.get("expected_previous_comment_id")
    _require(type(cid) is int and cid > 0, "continuation requires actual predecessor server comment ID")
    _require(event.get("claim_id") != value["expected_previous_claim_id"], "successor must use a fresh claim ID")
    _require(event.get("researcher_id") != value["previous_researcher_id"], "new conversation must use its own identity")
    _require(event.get("session_id") == value["session_id"], "continuation session binding mismatch")
    validate_frontier(value.get("frontier"), root=root, verify_artifacts=verify_artifacts, evidence_roots=evidence_roots)
    _require(value["previous_researcher_id"] in value["frontier"]["contributor_ids"], "predecessor contribution provenance cannot be erased")
    if value["mode"] == "TAKEOVER":
        validate_recovery_evidence(value.get("recovery_evidence"), value["frontier"])


def validate_recovery_evidence(evidence: Any, frontier: Mapping[str, Any], now: datetime | None = None) -> None:
    from tools.research_runtime_reducer import parse_time
    _require(isinstance(evidence, Mapping), "live takeover requires explicit stale/termination/handoff evidence")
    _require(evidence.get("basis") == "STALE_SESSION", "live TAKEOVER requires stale-session evidence; owner termination or explicit handoff requires a real authenticated HANDOFF(CONTINUATION), then RESUME")
    _require(evidence.get("active_session_confirmed") is False, "an active exact session cannot be preempted")
    _require(_text(evidence.get("previous_session_id")), "recovery requires previous session identity or explicit UNKNOWN_LEGACY_SESSION")
    _require(evidence.get("source_ref") in frontier["artifacts"], "recovery authorization must bind one verified immutable frontier artifact")
    observed = parse_time(evidence.get("observed_at"))
    if now is not None:
        _require(0 <= (now - observed).total_seconds() <= 300, "recovery observation is stale or from the future")
    if evidence["basis"] == "STALE_SESSION":
        last = parse_time(evidence.get("last_activity_at"))
        _require((observed - last).total_seconds() >= 600, "exact predecessor session has not reached the stale threshold")


def validate_owner_activity(state: Mapping[str, Any], evidence: Mapping[str, Any], now: datetime) -> None:
    from tools.research_runtime_reducer import parse_time
    actual = parse_time(state.get("last_owner_activity_at"))
    observed_last = parse_time(evidence.get("last_activity_at"))
    retry_after = (actual + timedelta(seconds=600)).isoformat()
    _require(observed_last >= actual, f"STALE_NOT_READY: recovery observation predates actual canonical owner activity; retry_after={retry_after}")
    _require((now - actual).total_seconds() >= 600, f"STALE_NOT_READY: actual canonical owner activity is still protected; retry_after={retry_after}")


def continuation_cas_reason(state: Mapping[str, Any], event: Mapping[str, Any]) -> str | None:
    value = event.get("continuation")
    if not isinstance(value, Mapping) or value.get("schema") != SCHEMA:
        return "CLAIM requires a valid typed continuation"
    meta = event.get("_github")
    if not isinstance(meta, Mapping) or meta.get("server_authenticated") is not True or meta.get("control_authorized") is not True or meta.get("edited") is not False:
        return "continuation requires an authenticated unedited control-authorized server event"
    if (value.get("expected_previous_claim_id") != state.get("last_claim_id")
            or value.get("expected_previous_comment_id") != state.get("last_claim_comment_id")):
        return "continuation predecessor CLAIM CAS changed"
    if value.get("previous_researcher_id") != (state.get("researcher_id") or state.get("last_researcher_id")):
        return "continuation predecessor identity changed"
    if event.get("claim_id") == state.get("last_claim_id") or event.get("researcher_id") == value.get("previous_researcher_id"):
        return "continuation must use a new claim and real new execution identity"
    if not _text(value.get("session_id")) or event.get("session_id") != value["session_id"]:
        return "continuation requires exact successor session binding"
    if value.get("mode") == "TAKEOVER":
        if state.get("claim_id") != value.get("expected_previous_claim_id") or state.get("state") not in {"CLAIMED", "IN_PROGRESS"}:
            return "TAKEOVER requires the exact live predecessor claim"
        try:
            from tools.research_runtime_reducer import parse_time
            validate_recovery_evidence(value.get("recovery_evidence"), value["frontier"], parse_time(event["at"]))
            validate_owner_activity(state, value["recovery_evidence"], parse_time(event["at"]))
        except (ContinuationError, ValueError, KeyError, TypeError) as exc:
            return str(exc)
        if state.get("session_id") is not None and value["recovery_evidence"].get("previous_session_id") != state["session_id"]:
            return "recovery evidence does not name the exact predecessor session"
    elif value.get("mode") == "RESUME":
        if state.get("claim_id") or state.get("state") not in {"READY", "HANDOFF_READY"}:
            return "RESUME requires a released or expired predecessor claim"
    else:
        return "unknown continuation mode"
    return None


def _definition(task_id: str, root: Path) -> dict[str, Any]:
    from tools import research_dispatch, research_task_records
    records = research_task_records.current_records(root)
    _require(task_id in records, "unknown current immutable task publication")
    return research_dispatch.registered_definition(records[task_id], root)


def authorize_executor_role(task_id: str, *, executor_id: str, session_id: str,
                            executor_role: str, now: datetime, root: Path) -> dict[str, Any]:
    """Driver GOV execution is distinct from Researcher activity registration."""
    from tools import research_identity
    _require(_text(session_id), "execution requires its actual declared session identity")
    _require(research_identity.valid_execution_id(executor_id), "execution requires a valid actual role identity")
    definition = _definition(task_id, root)
    if definition.get("kind") == "GOVERNANCE":
        import research_driver_authority as driver
        _require(executor_role == "RESEARCH_DRIVER", "GOVERNANCE execution requires an actual RESEARCH_DRIVER role, not a Researcher activity")
        authority = driver.require_active_driver(executor_id, now.isoformat(), root)
        _require(authority is not None, "GOVERNANCE execution requires current Source Driver authority")
        payload = json.loads(authority["source_body"])
        bound_session = payload.get("session_id") or (payload.get("succession") or {}).get("session_id")
        _require(_text(bound_session), "new GOVERNANCE execution requires explicitly session-bound Driver authority")
        _require(session_id == bound_session, "GOVERNANCE execution Driver session differs from current DA")
        return {"executor_role": "RESEARCH_DRIVER", "driver_id": executor_id,
                "driver_authority_record_id": authority["authority_record_id"],
                "driver_authority_source_comment_id": authority["source_comment_id"],
                "mathematical_acceptance_granted": False}
    _require(executor_role == "RESEARCHER" and not executor_id.startswith(("EM-DVR-", "EM-DRIVER-", "EM-STW-")),
             "RESEARCH task execution requires its actual Researcher identity and role")
    return {"executor_role": "RESEARCHER", "mathematical_acceptance_granted": False}


def _route(state: Mapping[str, Any], *, result_available: bool | None = None) -> dict[str, Any]:
    dispatch = state.get("dispatch_state")
    if dispatch == "COMPLETE":
        role, action = "NONE", "CONSUME_COMPLETED_RECORDS"
    elif dispatch == "AWAITING_REVIEW":
        if result_available is False:
            role, action = "CONTROL_PLANE_MAINTENANCE", "LEGACY_BRANCH_RESULT_INTAKE_REQUIRED"
        else:
            role, action = "RESEARCH_DRIVER", "ACTIVATE_NEW_DRIVER_AND_REVIEW_FROZEN_RESULT"
    elif dispatch == "LEASED":
        role, action = "RESEARCHER", "VERIFY_LIVENESS_THEN_PREPARE_EXPLICIT_TAKEOVER"
    elif dispatch == "NEEDS_DISPATCH":
        role, action = "RESEARCHER", "REGISTER_NEW_SESSION_AND_CLAIM_CURRENT_PUBLICATION"
    elif dispatch == "COHORT_ACTIVE" or state.get("execution_cohort_id") or state.get("execution_lane_id"):
        role, action = "CONTROL_PLANE_MAINTENANCE", "SUPPORTED_NATIVE_LANE_ADAPTER_REQUIRED"
    else:
        role, action = "CONTROL_PLANE_MAINTENANCE", "RESOLVE_EXACT_RECORDED_CONTROL_BLOCK"
    if dispatch != "COMPLETE" and (state.get("execution_cohort_id") or state.get("execution_lane_id")):
        role, action = "CONTROL_PLANE_MAINTENANCE", "SUPPORTED_NATIVE_LANE_ADAPTER_REQUIRED"
    if role == "RESEARCHER" and state.get("kind") == "GOVERNANCE":
        role = "RESEARCH_DRIVER"
    return {"required_role": role, "action": action, "execution_authorized": False,
            "requires_predecessor_contact": False, "requires_current_role_authorization": role != "NONE"}


def inventory_projection(*, root: Path, events: list[dict[str, Any]], now: datetime,
                         source_commit: str) -> dict[str, Any]:
    """Internal one-pass projection for service-owned snapshot pagination."""
    from tools import research_dispatch, research_result_records
    verify_source_snapshot(root, source_commit)
    states = research_dispatch.effective_states(events, now=now, root=root)
    result_scopes = {(row.get("task_id"), row.get("publication_id")) for row in research_result_records.iter_results(root)}
    counts = dict(sorted(Counter(row.get("dispatch_state", "UNKNOWN") for row in states).items()))
    version = hashlib.sha256(json.dumps({"source_commit": source_commit, "events": events,
        "states": [{k: row.get(k) for k in ("task_id", "publication_id", "state", "dispatch_state", "claim_id", "lease_until")}
                   for row in states]}, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    keys = ("task_id", "publication_id", "title", "kind", "state", "dispatch_state", "priority", "claim_id", "researcher_id", "lease_until", "next_action")
    return {"schema": "ENTERPRISE_MATH_CONTINUATION_INVENTORY_V1", "source_commit": source_commit,
            "observed_at": now.isoformat(), "counts": counts, "total": len(states), "snapshot_version": version,
            "tasks": [{**{key: row.get(key) for key in keys},
                       "continuation": _route(row, result_available=(row["task_id"], row.get("publication_id")) in result_scopes)}
                      for row in sorted(states, key=lambda row: row["task_id"])],
            "execution_authorized": False}


def inventory(*, root: Path, events: list[dict[str, Any]], now: datetime,
              source_commit: str, limit: int = 20, cursor: str | None = None,
              dispatch_state: str | None = None) -> dict[str, Any]:
    _require(type(limit) is int and 1 <= limit <= 100, "limit must be between 1 and 100")
    result = inventory_projection(root=root, events=events, now=now, source_commit=source_commit)
    selected = [row for row in result["tasks"] if dispatch_state is None or row.get("dispatch_state") == dispatch_state]
    version = hashlib.sha256((result["snapshot_version"] + str(dispatch_state)).encode()).hexdigest()
    if cursor is not None:
        _require(isinstance(cursor, str), "cursor must be a task ID")
        try:
            token = json.loads(base64.urlsafe_b64decode(cursor).decode())
        except Exception as exc:
            raise ContinuationError("invalid continuation inventory cursor") from exc
        _require(isinstance(token, dict) and token.get("version") == version, "CURSOR_STALE: source or runtime changed; restart inventory")
        _require(_text(token.get("after")), "invalid continuation inventory cursor")
        selected = [row for row in selected if row["task_id"] > token["after"]]
    page = selected[:limit]
    return {**result, "tasks": page,
            "next_cursor": base64.urlsafe_b64encode(json.dumps({"version": version, "after": page[-1]["task_id"]}, separators=(",", ":")).encode()).decode() if len(selected) > limit else None,
            "execution_authorized": False}


def checkpoint_frontier(task_id: str, publication_id: str, *, root: Path,
                        events: list[dict[str, Any]], source_commit: str) -> dict[str, Any]:
    """Read one task-local locator; checkpoint metadata grants no authority."""
    relative = f"research_artifacts/mcp/{task_id}/latest_checkpoint.json"
    if not (root / relative).is_file():
        return {"state": "NOT_FOUND", "source_artifacts": [], "execution_authorized": False}
    pins = [artifact_pin(root, relative, source_commit)]
    try:
        from tools import research_dispatch, research_runtime_reducer
        pointer = json.loads((root / relative).read_text(encoding="utf-8"))
        _require(pointer.get("schema") == "ENTERPRISE_MATH_MCP_CHECKPOINT_POINTER_V1"
                 and pointer.get("authority_granted") is False, "checkpoint locator has invalid schema or authority flag")
        _require(pointer.get("task_id") == task_id and pointer.get("publication_id") == publication_id,
                 "checkpoint locator is not for the exact current publication")
        path = pointer.get("checkpoint_path")
        _require(_text(path) and path.startswith(f"research_artifacts/mcp/{task_id}/")
                 and path != relative, "checkpoint locator escapes its exact task namespace")
        raw = _path(root, path).read_bytes()
        _require(hashlib.sha256(raw).hexdigest() == pointer.get("checkpoint_sha256"), "checkpoint bytes differ from locator digest")
        checkpoint = json.loads(raw)
        _require(checkpoint.get("schema") == "ENTERPRISE_MATH_MCP_EXECUTION_CHECKPOINT_V1", "invalid checkpoint schema")
        for key in ("task_id", "publication_id", "claim_id", "ownership_epoch", "session_id", "researcher_id"):
            _require(checkpoint.get(key) == pointer.get(key) and checkpoint.get(key) is not None,
                     f"checkpoint locator {key} binding differs")
        at = research_runtime_reducer.parse_time(pointer.get("created_at"))
        preceding = [event for event in events if event.get("task_id") == task_id
                     and research_runtime_reducer.parse_time(event["at"]) <= at]
        definition = _definition(task_id, root)
        accepted, _ = research_dispatch._event_authentication_filter(definition, preceding)
        filtered, _ = research_dispatch._filter_registered_events(definition, accepted, root, result_state=None)
        owner = research_runtime_reducer.reduce_task(definition, filtered, now=at, default_lease_minutes=120)
        _require(owner.get("dispatch_state") == "LEASED", "checkpoint has no recorded live owner at its capture time")
        for key in ("claim_id", "researcher_id", "ownership_epoch", "session_id"):
            _require(owner.get(key) == pointer.get(key), f"checkpoint {key} differs from recorded winning claim")
        pins.append(artifact_pin(root, path, source_commit))
        for output in checkpoint.get("output_manifest", []):
            _require(isinstance(output, dict) and _text(output.get("path")), "invalid checkpoint output manifest")
            pin = artifact_pin(root, output["path"], source_commit)
            _require(pin["sha256"] == str(output.get("sha256", "")).removeprefix("sha256:"), "checkpoint output bytes changed")
            pins.append(pin)
        return {"state": "SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED", "checkpoint": checkpoint,
                "source_artifacts": pins, "semantic_status": "AUTHOR_REPORTED_NOT_MATHEMATICAL_ACCEPTANCE",
                "execution_authorized": False}
    except Exception as exc:
        return {"state": "UNKNOWN", "reason": str(exc), "source_artifacts": pins, "execution_authorized": False}


def _fixed_source_candidate(ref: Any, provenance: str) -> dict[str, Any] | None:
    commit, path = None, None
    if isinstance(ref, dict):
        if ref.get("repository", REPOSITORY) != REPOSITORY:
            return None
        commit, path = ref.get("commit", ref.get("source_commit")), ref.get("path")
        if commit is None:
            ref = ref.get("url", ref.get("ref"))
    if isinstance(ref, str):
        url = urlsplit(ref)
        match = re.fullmatch(r"/awdawmip/enterprise-math/blob/([0-9a-f]{40})/(.+)", url.path)
        if url.scheme == "https" and url.netloc == "github.com" and match:
            commit, path = match[1], unquote(match[2])
        else:
            pinned_file = re.fullmatch(r"([^\s@]+)@([0-9a-f]{40})", ref)
            if pinned_file and PurePosixPath(pinned_file[1]).suffix:
                # Repository taskbooks also use explicit file@commit notation.
                # Branch-only labels and @blob: identities remain lookup hints.
                path, commit = pinned_file[1], pinned_file[2]
    if not isinstance(commit, str) or not HEX40.fullmatch(commit) or not _text(path):
        return None
    if PurePosixPath(path).is_absolute() or set(PurePosixPath(path).parts) & {"..", ".git"} or "\\" in path:
        return None
    return {"repository": REPOSITORY, "source_commit": commit, "path": path,
            "verification": "PENDING_IMMUTABLE_READBACK", "provenance": provenance}


def continuation_packet(task_id: str, *, root: Path, events: list[dict[str, Any]],
                        now: datetime, source_commit: str, reader_driver_id: str | None = None,
                        reader_session_id: str | None = None) -> dict[str, Any]:
    from tools import research_dispatch, research_task_records, research_result_records, research_taskbook
    verify_source_snapshot(root, source_commit)
    definition = _definition(task_id, root)
    record = research_task_records.current_records(root)[task_id]
    state = research_dispatch.reduce_definition(definition, events, now=now, root=root)
    refs = [record["taskbook_path"], f"research_task_records/{task_id}/{record['publication_id']}.json"]
    unresolved_refs = []
    metadata, _ = research_taskbook.split_taskbook((root / record["taskbook_path"]).read_text(encoding="utf-8"))
    from control_plane import research_source_firewall
    firewall = research_source_firewall.validate_config(metadata.get("source_firewall"))
    driver_view = False
    if reader_driver_id is not None:
        import research_driver_authority as driver
        authority = driver.require_active_driver(reader_driver_id, now.isoformat(), root)
        _require(authority is not None and _text(reader_session_id), "Driver evidence read requires current DA and a real session")
        payload = json.loads(authority["source_body"])
        bound = payload.get("session_id") or (payload.get("succession") or {}).get("session_id")
        _require(_text(bound) and bound == reader_session_id, "Driver evidence read requires explicitly matching current DA session")
        driver_view = True
    restricted = firewall is not None and not driver_view
    allowed = {(pin["commit"], pin["path"]) for pin in firewall["allowed_source_pins"]} if firewall else set()
    external = []
    withheld_count = 0
    expected_input_blobs = {}
    for field in ("required_source_reads", "source_refs", "dependencies"):
        for ref in metadata.get(field, []) if isinstance(metadata.get(field), list) else []:
            fixed = _fixed_source_candidate(ref, "CURRENT_TASKBOOK_DECLARED_INPUT")
            if fixed is not None:
                if not restricted or (fixed["source_commit"], fixed["path"]) in allowed:
                    external.append(fixed)
                else:
                    withheld_count += 1
                continue
            candidate = ref.get("path") if isinstance(ref, dict) else ref
            if isinstance(candidate, str) and candidate and not candidate.startswith(("http:", "https:")):
                declared = re.fullmatch(r"(.+?)(?:@main|#blob=([0-9a-f]{40}))", candidate)
                if declared:
                    candidate = declared[1]
                    if declared[2]:
                        expected_input_blobs.setdefault(candidate, set()).add(declared[2])
                try:
                    _path(root, candidate)
                    if not restricted or (source_commit, candidate) in allowed:
                        refs.append(candidate)
                    else:
                        withheld_count += 1
                except ContinuationError:
                    unresolved_refs.append(ref)
            else:
                unresolved_refs.append(ref)
    result_state = research_result_records.task_result_state(task_id, root, record["publication_id"])
    result_available = result_state is not None
    if isinstance(result_state, dict) and not restricted:
        result = result_state.get("result")
        if isinstance(result, dict):
            refs += [value for value in (result.get("_record_path"), result.get("return_path")) if isinstance(value, str)]
            if result.get("result_id"):
                refs.append(f"research_result_records/{task_id}/{result['result_id']}.json")
            if result.get("execution_record_id"):
                refs.append(f"research_execution_records/{task_id}/{result['execution_record_id']}.json")
            refs += [item["path"] for item in result.get("output_manifest", []) if isinstance(item, dict) and isinstance(item.get("path"), str)]
    pins, artifact_errors = [], []
    for path in dict.fromkeys(refs):
        try:
            pin = artifact_pin(root, path, source_commit)
            _require(not expected_input_blobs.get(path) or expected_input_blobs[path] == {pin["git_blob_sha1"]},
                     "declared input blob differs from current Source bytes")
            pins.append(pin)
        except ContinuationError as exc:
            artifact_errors.append({"path": path, "error": str(exc)})
    persisted_checkpoint = checkpoint_frontier(task_id, record["publication_id"], root=root, events=events, source_commit=source_commit) if not restricted else {"state": "WITHHELD_BY_SOURCE_FIREWALL", "source_artifacts": [], "execution_authorized": False}
    existing_paths = {pin["path"] for pin in pins}
    pins.extend(pin for pin in persisted_checkpoint["source_artifacts"] if pin["path"] not in existing_paths)
    progress = state.get("last_progress_ref")
    progress_readback = None
    continuation_seed = None
    fixed = _fixed_source_candidate(progress, "AUTHENTICATED_RUNTIME_LAST_PROGRESS_REF")
    if fixed and (not restricted or (fixed["source_commit"], fixed["path"]) in allowed):
        external.append(fixed)
    elif isinstance(progress, str) and progress and not progress.startswith(("http:", "https:")):
        # Legacy publications often seed last_progress_ref with a repository
        # path. Verify its current immutable bytes; do not invent a historical
        # commit or treat the input as work produced by a later CLAIM.
        if not restricted or (source_commit, progress) in allowed:
            try:
                pin = artifact_pin(root, progress, source_commit)
                _require(not expected_input_blobs.get(progress) or expected_input_blobs[progress] == {pin["git_blob_sha1"]},
                         "declared input blob differs from current Source bytes")
            except ContinuationError as exc:
                artifact_errors.append({"path": progress, "error": str(exc)})
            else:
                input_seed_unchanged = (progress == definition.get("last_progress_ref")
                    and state.get("last_progress_at") == definition.get("last_progress_at"))
                pin.update(provenance="CURRENT_TASK_DEFINITION_INPUT_READBACK" if input_seed_unchanged
                           else "CURRENT_RUNTIME_REFERENCE_READBACK",
                           verification="CURRENT_IMMUTABLE_SOURCE_BYTES_VERIFIED",
                           historical_bytes_verified=False, mathematical_acceptance_granted=False)
                if not any(p["path"] == pin["path"] and p["source_commit"] == source_commit for p in pins):
                    pins.append(pin)
                progress_readback = {"pin": pin, "original_reference": progress,
                    "historical_work_status": "UNKNOWN_NOT_ESTABLISHED_BY_CURRENT_READBACK"}
                if (input_seed_unchanged and not restricted and not state.get("claim_id")
                        and state.get("dispatch_state") == "NEEDS_DISPATCH" and state.get("last_claim_id")):
                    continuation_seed = {"state": "CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS",
                        "task_id": task_id, "publication_id": record["publication_id"],
                        "previous_claim_id": state["last_claim_id"],
                        "previous_comment_id": state.get("last_claim_comment_id"),
                        "input_artifacts": [pin], "completed_research_units_verified": False,
                        "required_action": "Read the declared input, record UNKNOWN prior private work honestly, and continue the smallest unfinished task unit under a new authorized claim."}
    if firewall:
        for source_pin in firewall["allowed_source_pins"]:
            fixed = _fixed_source_candidate(source_pin, "EXPLICIT_SOURCE_FIREWALL_ALLOWLIST")
            if fixed:
                fixed["git_blob_sha1"] = source_pin["blob_sha1"]
                external.append(fixed)
    external = list({(pin["source_commit"], pin["path"]): pin for pin in external}.values())
    if restricted:
        state = copy.deepcopy(state)
        for field in ("continuation_frontier", "continuation", "last_progress_ref", "source_refs"):
            state.pop(field, None)
        state["next_action"] = "Follow the exact task source firewall before inspecting predecessor evidence."
        unresolved_refs = []
        result_state = {"state": result_state.get("state"), "evidence": "WITHHELD_BY_SOURCE_FIREWALL"} if isinstance(result_state, dict) else None
    intake = None
    if state.get("dispatch_state") == "AWAITING_REVIEW" and not result_available:
        frozen_records = [pin for pin in external if pin["path"].startswith(f"research_result_records/{task_id}/") and pin["path"].endswith(".json")]
        intake = {"state": "LEGACY_BRANCH_RESULT_INTAKE_REQUIRED", "protocol": "docs/LEGACY_BRANCH_RESULT_INTAKE.md",
                  "native_review_ready": False, "research_reclaim_allowed": False,
                  "candidate_status": "EXACT_FROZEN_RESULT_CANDIDATE_PENDING_READBACK" if frozen_records else "NEEDS_EXACT_SOURCE_LOOKUP",
                  "frozen_result_candidates": frozen_records,
                  "lookup_hints": [] if restricted else [value for value in [state.get("last_progress_ref"), state.get("next_action"), *unresolved_refs] if value],
                  "next_action": "Verify the exact historical branch Result and its bound files; perform bytes-preserving canonical intake under the linked protocol before native Driver review.",
                  "requires_predecessor_contact": False, "mathematical_acceptance_granted": False}
    readiness = {"state": "NO_LIVE_CLAIM", "retry_after": None}
    if state.get("claim_id"):
        from tools.research_runtime_reducer import parse_time
        ready_at = parse_time(state["last_owner_activity_at"]) + timedelta(seconds=600)
        readiness = {"state": "STALE_EVIDENCE_REQUIRED" if now >= ready_at else "STALE_NOT_READY",
                     "retry_after": ready_at.isoformat(), "last_canonical_owner_activity_at": state["last_owner_activity_at"],
                     "activity_barrier_is_not_independent_session_liveness_proof": True}
    return {"schema": "ENTERPRISE_MATH_CONTINUATION_PACKET_V1", "source_commit": source_commit,
            "observed_at": now.isoformat(), "task_id": task_id, "publication_id": record["publication_id"],
            "task": copy.deepcopy(record), "runtime": state, "route": _route(state, result_available=result_available),
            "source_artifacts": pins, "artifact_errors": artifact_errors,
            "immutable_external_artifact_candidates": external,
            "takeover_readiness": readiness,
            "legacy_result_intake": intake,
            "persisted_checkpoint": persisted_checkpoint,
            "progress_reference_readback": progress_readback,
            "continuation_seed": continuation_seed,
            "source_access_policy": {"blind_firewall_active": firewall is not None, "restricted": restricted,
                                     "verified_driver_review_view": driver_view, "withheld_declared_input_count": withheld_count},
            "unresolved_source_refs": unresolved_refs, "result_state": result_state,
            "durable_frontier": copy.deepcopy(state.get("continuation_frontier")),
            "last_progress_ref": state.get("last_progress_ref"),
            "frontier_verification": "SOURCE_BYTES_ONLY_NOT_MATHEMATICAL_ACCEPTANCE",
            "recovery_rule": "Verify durable units; consume VERIFIED_COMPLETE, resolve UNKNOWN minimally, resume the smallest UNFINISHED unit.",
            "independence_rule": "New session or role never erases prior mathematical contributions or source exposure.",
            "continuation_input_contract": {
                "frontier_required": ["source_commit", "artifacts", "current_unfinished_unit", "next_action", "completed_units", "do_not_repeat", "contributor_ids"],
                "artifact_pin_required": ["repository", "source_commit", "path", "git_blob_sha1", "sha256"],
                "recovery_evidence_required_for_live_takeover": ["basis", "previous_session_id", "observed_at", "source_ref", "active_session_confirmed"],
                "recovery_basis": ["STALE_SESSION"],
                "explicit_release_route": "Authenticate a native HANDOFF(CONTINUATION) for the exact old claim, then RESUME; a taskbook pin or caller boolean is not release authority.",
                "stale_basis_extra_required": "last_activity_at",
                "active_session_may_be_preempted": False,
                "source_ref_rule": "one exact artifact pin whose content supports the claimed recovery basis",
                "freshness_seconds": 300, "stale_threshold_seconds": 600,
                "max_frontier_artifacts": 64,
                "claim_input_fields": ["new_researcher_id", "new_session_id", "new_claim_id", "execution_branch", "execution_branch_base", "allowed_outputs", "expected_previous_claim_id", "expected_previous_comment_id", "frontier", "reason"],
            },
            "frontier_template": {"source_commit": source_commit, "artifacts": pins[:64],
                "current_unfinished_unit": None, "next_action": None, "completed_units": [],
                "do_not_repeat": [], "contributor_ids": [state.get("researcher_id") or state.get("last_researcher_id")] if state.get("researcher_id") or state.get("last_researcher_id") else []},
            "capability_required": ("No computation or new research is required to consume completed records."
                if state.get("dispatch_state") == "COMPLETE" else
                "Use the authorized Source control adapter for the selected action. A client checkout or local runtime is not a general research prerequisite; perform eligible self-contained reasoning in scope and leave task-specific unexecuted computation explicitly pending."),
            "capability_requirements": {"local_environment_is_global_start_gate": False,
                "next_action": state.get("next_action"),
                "scientific_compute": "NOT_REQUIRED_FOR_COMPLETED_RECORD_CONSUMPTION" if state.get("dispatch_state") == "COMPLETE" else "ONLY_WHEN_REQUIRED_BY_THE_EXACT_TASK_STEP",
                "missing_validator": "PENDING_VALIDATION_OR_SUPPORT_REQUEST_NOT_FABRICATED_PASS",
                "changes_claim_or_mathematical_authority": False},
            "execution_authorized": False, "requires_predecessor_contact": False}


def prepare_takeover(task_id: str, *, root: Path, events: list[dict[str, Any]],
                     now: datetime, source_commit: str, new_researcher_id: str,
                     new_session_id: str, new_claim_id: str, execution_branch: str,
                     execution_branch_base: str, allowed_outputs: list[str],
                     expected_previous_claim_id: str, expected_previous_comment_id: int,
                     frontier: Mapping[str, Any], reason: str, lease_minutes: int = 120,
                     recovery_evidence: Mapping[str, Any] | None = None,
                     evidence_roots: Mapping[str, Path] | None = None) -> dict[str, Any]:
    from tools import research_dispatch, research_execution_records, research_runtime_reducer
    definition = _definition(task_id, root)
    state = research_dispatch.reduce_definition(definition, events, now=now, root=root)
    _require(state.get("dispatch_state") != "COHORT_ACTIVE" and not state.get("execution_cohort_id") and not state.get("execution_lane_id"),
             "SUPPORTED_NATIVE_LANE_ADAPTER_REQUIRED: preserve lane claim; use tools/research_lane_dispatch.py with explicit lane scope")
    _require(state.get("dispatch_state") in {"LEASED", "NEEDS_DISPATCH"}, "task lifecycle does not permit continuation execution")
    _require(state.get("last_claim_id") == expected_previous_claim_id
             and state.get("last_claim_comment_id") == expected_previous_comment_id,
             "predecessor CLAIM CAS changed; refresh continuation packet")
    previous_id = state.get("researcher_id") or state.get("last_researcher_id")
    executor_role = "RESEARCH_DRIVER" if definition.get("kind") == "GOVERNANCE" else "RESEARCHER"
    role_binding = authorize_executor_role(task_id, executor_id=new_researcher_id, session_id=new_session_id,
                                           executor_role=executor_role, now=now, root=root)
    validate_frontier(frontier, root=root, source_commit=verify_source_snapshot(root, source_commit), evidence_roots=evidence_roots)
    predecessor_intent = research_execution_records.intent_for_claim(task_id, expected_previous_claim_id, root)
    theorem_owner = predecessor_intent.get("theorem_owner") if isinstance(predecessor_intent, dict) else None
    if not _text(theorem_owner):
        accepted, _ = research_dispatch._event_authentication_filter(definition, events)
        filtered, _ = research_dispatch._filter_registered_events(definition, accepted, root, result_state=None)
        predecessor = next((event for event in filtered if event.get("event") == "CLAIM"
                            and event.get("claim_id") == expected_previous_claim_id
                            and (event.get("_github") or {}).get("comment_id") == expected_previous_comment_id), None)
        theorem_owner = predecessor.get("theorem_owner") if isinstance(predecessor, dict) else None
    owner_source = "PREDECESSOR_EXECUTION_BINDING" if _text(theorem_owner) else "CANONICAL_TASK_OWNER_LEGACY_FALLBACK"
    if not _text(theorem_owner):
        theorem_owner = definition.get("owner")
    _require(_text(theorem_owner), "continuation has no canonical theorem owner; caller cannot relabel it")
    intent = research_execution_records.prepare_intent(
        task_id=task_id, claim_id=new_claim_id, researcher_id=new_researcher_id,
        theorem_owner=theorem_owner, execution_branch=execution_branch,
        execution_branch_base=execution_branch_base, allowed_outputs=allowed_outputs,
        owner_lease_minutes=lease_minutes, prepared_at=now.isoformat(), root=root)
    continuation = {"schema": SCHEMA, "mode": "TAKEOVER" if state.get("claim_id") else "RESUME",
                    "expected_previous_claim_id": expected_previous_claim_id,
                    "expected_previous_comment_id": expected_previous_comment_id,
                    "previous_researcher_id": previous_id, "session_id": new_session_id,
                    "reason": reason, "frontier": copy.deepcopy(dict(frontier))}
    if state.get("claim_id"):
        validate_recovery_evidence(recovery_evidence, frontier, now)
        validate_owner_activity(state, recovery_evidence, now)
        continuation["recovery_evidence"] = copy.deepcopy(dict(recovery_evidence))
    event = {"schema": "ENTERPRISE_MATH_SCHEDULER_EVENT_V1", "event": "CLAIM", "task_id": task_id,
             "publication_id": intent["publication_id"], "claim_id": new_claim_id,
             "researcher_id": intent["researcher_id"], "session_id": new_session_id,
             "theorem_owner": intent["theorem_owner"], "execution_branch": execution_branch,
             "execution_branch_base": execution_branch_base, "allowed_outputs": allowed_outputs,
             "lease_minutes": lease_minutes, "continuation": continuation}
    validate_claim_continuation(definition, event, root=root)
    # Intents are prepared evidence only. The event remains stable when repeated
    # against the same authority/frontier; the server supplies its actual clock.
    intent["continuation"] = continuation
    intent["executor_role"] = executor_role
    intent["theorem_owner_source"] = owner_source
    event["executor_role"] = executor_role
    return {"schema": "ENTERPRISE_MATH_CONTINUATION_PREPARE_V1", "source_commit": source_commit,
            "intent": intent, "claim_event": event, "role_binding": role_binding, "execution_authorized": False,
            "required_guard": "tools/research_runtime_guard.py authorize AFTER authenticated event readback",
            "publication_requirement": "Persist immutable new execution intent and actual authenticated CLAIM; read back unique winner before execution."}


def validate_prepared_claim(*, root: Path, events: list[dict[str, Any]], now: datetime,
                           source_commit: str, claim_event: Mapping[str, Any],
                           intent: Mapping[str, Any], evidence_roots: Mapping[str, Path] | None = None) -> dict[str, Any]:
    """Recheck a frozen candidate after publishing its ER, without repinning it.

The evidence commit is immutable and separate from the moving control head.
This preflight grants no authority and manufactures no server comment envelope.
"""
    from tools import research_dispatch
    verify_source_snapshot(root, source_commit)
    task_id = intent.get("task_id")
    definition = _definition(task_id, root)
    state = research_dispatch.reduce_definition(definition, events, now=now, root=root)
    _require(state.get("dispatch_state") != "COHORT_ACTIVE" and not intent.get("execution_cohort_id") and not intent.get("execution_lane_id"),
             "SUPPORTED_NATIVE_LANE_ADAPTER_REQUIRED: global prepared-claim revalidation cannot authorize a lane")
    _require(definition["publication_id"] == intent.get("publication_id"), "prepared publication was superseded")
    er_path = f"research_execution_records/{task_id}/{intent.get('execution_record_id')}.json"
    actual = json.loads(_path(root, er_path).read_text(encoding="utf-8"))
    _require(actual == dict(intent), "prepared execution intent has not reached current Source with exact bytes")
    role = "RESEARCH_DRIVER" if definition.get("kind") == "GOVERNANCE" else "RESEARCHER"
    _require(claim_event.get("executor_role", role) == role and intent.get("executor_role", role) == role,
             "prepared execution role differs from Task.kind")
    authorize_executor_role(task_id, executor_id=intent["researcher_id"], session_id=claim_event.get("session_id", ""),
                            executor_role=role, now=now, root=root)
    for field in ("task_id", "publication_id", "claim_id", "researcher_id", "execution_branch", "execution_branch_base", "allowed_outputs", "theorem_owner"):
        _require(claim_event.get(field) == intent.get(field), f"prepared claim/intent {field} differs")
    value = claim_event.get("continuation")
    if value is not None:
        _require(value == intent.get("continuation"), "prepared continuation differs from immutable ER")
        validate_claim_continuation(definition, claim_event, root=root, verify_artifacts=True, evidence_roots=evidence_roots)
        _require(state.get("last_claim_id") == value["expected_previous_claim_id"]
                 and state.get("last_claim_comment_id") == value["expected_previous_comment_id"], "prepared predecessor CAS changed")
        if value["mode"] == "TAKEOVER":
            _require(state.get("dispatch_state") == "LEASED" and state.get("claim_id") == value["expected_previous_claim_id"], "prepared takeover no longer has the exact live predecessor")
            validate_recovery_evidence(value.get("recovery_evidence"), value["frontier"], now)
            validate_owner_activity(state, value["recovery_evidence"], now)
        else:
            _require(state.get("dispatch_state") == "NEEDS_DISPATCH" and not state.get("claim_id"), "prepared resume no longer has an unowned task")
    else:
        _require(state.get("dispatch_state") == "NEEDS_DISPATCH" and not state.get("claim_id"), "task is no longer dispatchable")
    return {"ready_to_submit": True, "execution_authorized": False,
            "actual_control_source_commit": source_commit, "execution_record_path": er_path,
            "claim_event_unchanged": True}
