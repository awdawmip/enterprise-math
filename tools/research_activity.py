#!/usr/bin/env python3
"""Lightweight research bookkeeping, never task or execution authority.

Registration needs no question and reads no mathematical catalog. Connector-only
hosts may write the same JSON schema to the unique record path using non-force
CAS. A local record is not evidence of remote publication. Imported connector
observations are checked structurally and byte-for-byte; they are not signed
server attestations, and this tool does not make a network request.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import sys
from datetime import datetime, timezone
from typing import Any, Mapping

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from tools import research_identity

REPOSITORY = "awdawmip/enterprise-math"
SCHEMA = "ENTERPRISE_MATH_RESEARCH_ACTIVITY_V1"
STORE = "research_activity_records"
MODES = ("TASK_RESEARCH", "FREE_AXIOM_DISCOVERY", "UNKNOWN_RESEARCH")
NO_AUTHORITY = {name: False for name in (
    "task_registration", "claim", "review", "working_truth", "mathematical_acceptance"
)}


class ActivityError(ValueError):
    pass


def encoded(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def blob_id(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def _text(value: Any, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ActivityError(f"{name} must be a nonempty string")
    return value


def _hex(value: Any, size: int, name: str) -> str:
    if not isinstance(value, str) or re.fullmatch("[0-9a-f]{" + str(size) + "}", value) is None:
        raise ActivityError(f"{name} must be an exact lowercase {size}-character hex value")
    return value


def _relative(value: Any) -> str:
    value = _text(value, "path")
    path = PurePosixPath(value)
    if "\\" in value or ":" in value or path.is_absolute() or any(x in ("", ".", "..") for x in value.split("/")):
        raise ActivityError("path must be a canonical repository-relative path")
    return value


def record_path(activity_id: str, root: Path = ROOT) -> Path:
    if not isinstance(activity_id, str) or re.fullmatch(r"RA-[A-Za-z0-9_-]{8,96}", activity_id) is None:
        raise ActivityError("invalid activity_id")
    return root.joinpath(STORE, activity_id + ".json")


def registration(*, mode: str, researcher_id: str | None = None,
                 session_id: str | None = None, source_tracking_key: str | None = None,
                 activity_id: str | None = None) -> dict[str, Any]:
    retrospective = source_tracking_key is not None
    if mode not in MODES or (mode == "UNKNOWN_RESEARCH" and not retrospective):
        raise ActivityError("live registration requires TASK_RESEARCH or FREE_AXIOM_DISCOVERY")
    if retrospective:
        if session_id is not None:
            raise ActivityError("retrospective unknown-session registration cannot invent a session_id")
        key = "source:" + _text(source_tracking_key, "source_tracking_key")
    else:
        key = "session:" + _text(session_id, "session_id") + ":" + mode
        if researcher_id is None:
            raise ActivityError("live registration requires the resolved researcher_id")
    if researcher_id is not None and (not isinstance(researcher_id, str) or not research_identity.valid_researcher_id(researcher_id)):
        raise ActivityError("invalid researcher_id")
    if activity_id is None:
        activity_id = "RA-" + digest(key.encode("utf-8"))[:24].upper()
    record_path(activity_id)
    return {
        "schema": SCHEMA, "activity_id": activity_id, "registration_key": key,
        "registration_origin": {
            "kind": "RETROSPECTIVE_SOURCE" if retrospective else "LIVE_SESSION",
            "source_tracking_key": source_tracking_key,
        },
        "mode": mode, "researcher_id": researcher_id, "session_id": session_id,
        "session_state": "UNKNOWN" if retrospective else "KNOWN",
        "recorded_at": datetime.now(timezone.utc).isoformat(),
        "authority": dict(NO_AUTHORITY), "checkpoints": [],
    }


def _validate_record(record: Any) -> dict[str, Any]:
    if not isinstance(record, dict) or record.get("schema") != SCHEMA:
        raise ActivityError("invalid activity record schema")
    origin = record.get("registration_origin")
    if not isinstance(origin, dict) or origin.get("kind") not in ("LIVE_SESSION", "RETROSPECTIVE_SOURCE"):
        raise ActivityError("invalid registration_origin")
    rebuilt = registration(mode=record.get("mode"), researcher_id=record.get("researcher_id"),
        session_id=record.get("session_id"), source_tracking_key=origin.get("source_tracking_key"),
        activity_id=record.get("activity_id"))
    if set(record) != set(rebuilt):
        raise ActivityError("unknown/missing activity fields; activity is not a formal task record")
    try:
        recorded_at = datetime.fromisoformat(record["recorded_at"])
        if recorded_at.tzinfo is None:
            raise ValueError("timezone missing")
    except (ValueError, TypeError) as exc:
        raise ActivityError("recorded_at must be the timezone-aware observation time") from exc
    for key in ("registration_key", "registration_origin", "mode", "researcher_id", "session_id", "session_state", "authority"):
        if record.get(key) != rebuilt[key]:
            raise ActivityError(f"activity {key} drift")
    if not isinstance(record.get("checkpoints"), list):
        raise ActivityError("checkpoints must be a list")
    return record


def read(activity_id: str, root: Path = ROOT) -> dict[str, Any]:
    path = record_path(activity_id, root)
    record = _validate_record(json.loads(path.read_bytes()))
    if record["activity_id"] != activity_id:
        raise ActivityError("activity path/identity mismatch")
    return record


def register(*, root: Path = ROOT, **kwargs: Any) -> dict[str, Any]:
    record = registration(**kwargs)
    path = record_path(record["activity_id"], root)
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with path.open("xb") as stream:
            stream.write(encoded(record))
    except FileExistsError:
        prior = read(record["activity_id"], root)
        for key in record.keys() - {"recorded_at", "checkpoints"}:
            if record[key] != prior.get(key):
                raise ActivityError("registration identity collision; no record was overwritten")
        record = prior
    return record


def verify_observation(observation: Any, pin: Mapping[str, Any]) -> dict[str, Any]:
    """Check the full observed connector response, not a caller's success flag."""
    if not isinstance(observation, dict) or observation.get("tool_name") != "github_fetch_file":
        raise ActivityError("VERIFY_EM_PUBLICATION: full github_fetch_file observation required")
    args = observation.get("arguments", {})
    if not isinstance(args, dict) or any(args.get(k) != pin[v] for k, v in (
        ("repository_full_name", "repository"), ("ref", "commit"), ("path", "path")
    )):
        raise ActivityError("connector observation repo/ref/path mismatch")
    if any(args.get(k) is not None for k in ("start_line", "end_line")):
        raise ActivityError("publication verification requires a full-file observation")
    result = observation.get("result")
    if not isinstance(result, dict) or ("isError" in result and type(result["isError"]) is not bool) or result.get("isError") is True:
        raise ActivityError("invalid connector result")
    content = result.get("structuredContent")
    if not isinstance(content, dict):
        raise ActivityError("connector structuredContent is required")
    try:
        if content.get("encoding") == "utf-8":
            data = content["content"].encode("utf-8")
        elif content.get("encoding") == "base64":
            data = base64.b64decode(content["content"], validate=True)
        else:
            raise ActivityError("unknown connector content encoding")
    except (KeyError, TypeError, AttributeError, ValueError) as exc:
        raise ActivityError("invalid connector content") from exc
    url = f"https://github.com/{pin['repository']}/blob/{pin['commit']}/{pin['path']}"
    if content.get("display_url") != url or content.get("sha") != blob_id(data) or digest(data) != pin["sha256"]:
        raise ActivityError("connector content/blob/immutable URL does not match source pin")
    observation_id = observation.get("observation_id")
    call_id = observation.get("call_id")
    if observation_id is None and call_id is None:
        raise ActivityError("an observation_id (local provenance) or original call_id is required")
    for key, value in (("observation_id", observation_id), ("call_id", call_id)):
        if value is not None:
            _text(value, key)
    return {"kind": "OBSERVED_CONNECTOR_STRUCTURE_AND_BYTES_VERIFIED", "tool_name": "github_fetch_file",
            "observation_id": observation_id, "call_id": call_id, "git_blob_sha1": blob_id(data),
            "immutable_url": url, "network_request_by_this_tool": False,
            "server_signature_authenticated": False}


def _source(source: Any, activity_id: str) -> tuple[dict[str, Any], tuple[str, bytes] | None]:
    if not isinstance(source, dict) or source.get("repository") != REPOSITORY:
        raise ActivityError("EM source must name awdawmip/enterprise-math")
    pin = {"repository": REPOSITORY, "commit": _hex(source.get("commit"), 40, "commit"),
           "path": _relative(source.get("path")), "sha256": _hex(source.get("sha256"), 64, "sha256")}
    if pin["path"].startswith(STORE + "/"):
        raise ActivityError("activity bookkeeping is not a semantic research checkpoint")
    observation = source.get("readback")
    if observation is None:
        return {**pin, "publication_state": "VERIFY_EM_PUBLICATION"}, None
    verified = verify_observation(observation, pin)
    data = encoded(observation)
    receipt = f"{STORE}/{activity_id}/readbacks/{digest(data)}.json"
    return {**pin, "publication_state": "EM_SOURCE_OBSERVED", "verification": verified,
            "verification_receipt": receipt, "verification_receipt_sha256": digest(data)}, (receipt, data)


def _checked_source(source: Any, activity_id: str, root: Path) -> str:
    if not isinstance(source, dict):
        raise ActivityError("invalid stored source")
    base, _ = _source(source, activity_id)
    if source.get("publication_state") == "VERIFY_EM_PUBLICATION":
        if source != base:
            raise ActivityError("unverified source fields drift")
        return "VERIFY_EM_PUBLICATION"
    receipt = _relative(source.get("verification_receipt"))
    receipt_sha = _hex(source.get("verification_receipt_sha256"), 64, "receipt sha256")
    expected = f"{STORE}/{activity_id}/readbacks/{receipt_sha}.json"
    if receipt != expected:
        raise ActivityError("verification receipt must be exact and activity-local")
    data = root.joinpath(receipt).read_bytes()
    if digest(data) != receipt_sha:
        raise ActivityError("verification receipt bytes drift")
    rebuilt, _ = _source({**base, "readback": json.loads(data)}, activity_id)
    if source != rebuilt:
        raise ActivityError("stored source/verification fields drift")
    return "EM_SOURCE_OBSERVED"


def _events(record: Mapping[str, Any], root: Path) -> dict[str, dict[str, Any]]:
    events: dict[str, dict[str, Any]] = {}
    for row in record["checkpoints"]:
        if not isinstance(row, dict):
            raise ActivityError("invalid checkpoint")
        event_id = _text(row.get("event_id"), "event_id")
        if event_id in events:
            raise ActivityError("duplicate checkpoint event_id")
        if not isinstance(row.get("em_sources"), list) or not isinstance(row.get("kb_sources"), list):
            raise ActivityError("checkpoint sources must be lists")
        states = [_checked_source(x, record["activity_id"], root) for x in row["em_sources"]]
        status = "SYNC_DEBT" if not states else ("EM_REPRESENTED" if all(s == "EM_SOURCE_OBSERVED" for s in states) else "VERIFY_EM_PUBLICATION")
        if row.get("state") != status:
            raise ActivityError("checkpoint state must be derived from actual source evidence")
        repair = row.get("repairs_event_id")
        if repair is not None and (repair not in events or status != "EM_REPRESENTED"):
            raise ActivityError("repair must reference an earlier event and provide verified EM source")
        events[event_id] = row
    return events


def checkpoint(activity_id: str, *, event_id: str, expected_sha256: str,
               em_sources: list[Any] | None = None, kb_sources: list[Any] | None = None,
               repairs_event_id: str | None = None, root: Path = ROOT) -> dict[str, Any]:
    path = record_path(activity_id, root)
    _hex(expected_sha256, 64, "expected_sha256")
    _text(event_id, "event_id")
    if em_sources is not None and not isinstance(em_sources, list):
        raise ActivityError("em_sources must be a list")
    if kb_sources is not None and not isinstance(kb_sources, list):
        raise ActivityError("kb_sources must be a list")
    sources, receipts = [], []
    for source in em_sources or []:
        pin, receipt = _source(source, activity_id)
        sources.append(pin)
        if receipt is not None:
            receipts.append(receipt)
    journals = [_text(x, "KB source reference") for x in kb_sources or []]
    status = "SYNC_DEBT" if not sources else ("EM_REPRESENTED" if all(s["publication_state"] == "EM_SOURCE_OBSERVED" for s in sources) else "VERIFY_EM_PUBLICATION")
    row = {"event_id": event_id, "em_sources": sources, "kb_sources": journals,
           "state": status, "repairs_event_id": repairs_event_id}
    lock = path.with_suffix(".lock")
    try:
        with lock.open("x"):
            pass
    except FileExistsError as exc:
        raise ActivityError("activity write in progress; refresh and retry, do not overwrite") from exc
    try:
        data = path.read_bytes()
        record = _validate_record(json.loads(data))
        if record["activity_id"] != activity_id:
            raise ActivityError("activity path/identity mismatch; no checkpoint write")
        events = _events(record, root)
        if event_id in events:
            if events[event_id] != row:
                raise ActivityError("event_id conflict; historical checkpoint cannot be overwritten")
            return record
        if digest(data) != expected_sha256:
            raise ActivityError("expected_sha256 mismatch; refresh current activity bytes")
        if repairs_event_id is not None and (repairs_event_id not in events or status != "EM_REPRESENTED"):
            raise ActivityError("repair requires earlier exact event and observed EM source")
        for relative, receipt_data in receipts:
            receipt_path = root.joinpath(relative)
            receipt_path.parent.mkdir(parents=True, exist_ok=True)
            try:
                with receipt_path.open("xb") as stream:
                    stream.write(receipt_data)
            except FileExistsError:
                if receipt_path.read_bytes() != receipt_data:
                    raise ActivityError("immutable observation receipt collision")
        record["checkpoints"].append(row)
        temporary = path.with_suffix(".pending")
        with temporary.open("xb") as stream:
            stream.write(encoded(record))
        if path.read_bytes() != data:
            temporary.unlink()
            raise ActivityError("activity changed during write; no overwrite")
        os.replace(temporary, path)
        return record
    finally:
        lock.unlink()


def guard(*, activity_id: str | None = None, boundary: str = "startup",
          event_id: str | None = None, session_id: str | None = None,
          registration_source: Mapping[str, Any] | None = None,
          new_semantic_progress: bool = True,
          root: Path = ROOT) -> dict[str, Any]:
    if boundary not in ("startup", "checkpoint", "pre-final"):
        raise ActivityError("unknown activity boundary")
    if type(new_semantic_progress) is not bool:
        raise ActivityError("new_semantic_progress must be an explicit boolean")
    result = {"activity_id": activity_id, "boundary": boundary, "authority": dict(NO_AUTHORITY),
              "activity_allowed": False, "persistence_allowed": False,
              "registration_visibility": "LOCAL_RECORD_ONLY_UNTIL_IMMUTABLE_EM_READBACK",
              "required_action": "REGISTER_RESEARCH_ACTIVITY",
              "register_command": "python tools/research_activity.py register --session-id <session> --researcher-id <resolved-id> --mode <TASK_RESEARCH|FREE_AXIOM_DISCOVERY>"}
    if activity_id is None or not record_path(activity_id, root).is_file():
        return result
    record = read(activity_id, root)
    if record["session_state"] == "KNOWN" and (not isinstance(session_id, str) or not session_id.strip()):
        result["required_action"] = "BIND_CURRENT_RESEARCH_ACTIVITY_SESSION"
        return result
    if session_id is not None and session_id != record["session_id"]:
        raise ActivityError("activity belongs to a different or unknown original session")
    events = _events(record, root)
    repaired = {x["repairs_event_id"] for x in events.values() if x["repairs_event_id"] is not None}
    debts = [x for x in events.values() if x["state"] != "EM_REPRESENTED" and x["event_id"] not in repaired]
    result.update(mode=record["mode"], record_path=f"{STORE}/{activity_id}.json",
                  record_sha256=digest(record_path(activity_id, root).read_bytes()),
                  source_links=[f"https://github.com/{s['repository']}/blob/{s['commit']}/{s['path']}" for e in events.values() for s in e["em_sources"]],
                  sync_debt_events=[x["event_id"] for x in debts], required_action="CONTINUE_ACTIVITY")
    if registration_source is None:
        result["required_action"] = "PUBLISH_ACTIVITY_RECORD_WITH_CAS_AND_VERIFY_IMMUTABLE_EM_READBACK"
        return result
    if not isinstance(registration_source, Mapping):
        raise ActivityError("registration_source must be an exact EM source with full readback")
    registration_pin = {"repository": REPOSITORY,
                        "commit": _hex(registration_source.get("commit"), 40, "registration commit"),
                        "path": result["record_path"], "sha256": result["record_sha256"]}
    if any(registration_source.get(k) != v for k, v in registration_pin.items()):
        raise ActivityError("registration publication does not match current activity bytes/path/repo")
    verification = verify_observation(registration_source.get("readback"), registration_pin)
    result.update(activity_allowed=True, registration_visibility="IMMUTABLE_EM_RECORD_OBSERVED",
                  registration_source=verification["immutable_url"],
                  canonical_owner_visibility="VERIFY_CANONICAL_INTAKE_IF_PUBLISHED_ONLY_ON_A_BRANCH")
    if record["session_state"] == "UNKNOWN":
        result["activity_allowed"] = False
        result["required_action"] = "RETROSPECTIVE_TRACKING_ONLY_REGISTER_CURRENT_LIVE_SESSION_TO_RESEARCH"
    if debts:
        result["required_action"] = "PERSIST_EM_CHECKPOINT" if any(x["state"] == "SYNC_DEBT" for x in debts) else "VERIFY_EM_PUBLICATION"
    elif boundary != "startup" and new_semantic_progress and event_id not in events:
        result["required_action"] = "RECORD_SEMANTIC_CHECKPOINT"
    else:
        result["persistence_allowed"] = True
    return result


def overview(root: Path = ROOT, *, limit: int = 20, after: str | None = None) -> dict[str, Any]:
    if type(limit) is not int or not 1 <= limit <= 20:
        raise ActivityError("overview limit must be 1..20")
    if after is not None:
        record_path(after, root)
    paths = [p for p in sorted(root.joinpath(STORE).glob("RA-*.json")) if after is None or p.stem > after][:limit + 1]
    rows = []
    for path in paths[:limit]:
        try:
            record = read(path.stem, root)
            # The dispatch hot path reports stored bookkeeping only. It must
            # not replay every activity's full research-source observation.
            # The dedicated guard remains the strict source audit boundary.
            events = {}
            for event in record["checkpoints"]:
                if not isinstance(event, dict) or event.get("state") not in ("SYNC_DEBT", "VERIFY_EM_PUBLICATION", "EM_REPRESENTED"):
                    raise ActivityError("invalid recorded checkpoint state")
                event_id = _text(event.get("event_id"), "event_id")
                if event_id in events or not isinstance(event.get("em_sources"), list):
                    raise ActivityError("invalid recorded checkpoint metadata")
                repair = event.get("repairs_event_id")
                if repair is not None and (repair not in events or event["state"] != "EM_REPRESENTED" or not event["em_sources"]):
                    raise ActivityError("invalid recorded repair; it cannot hide earlier sync debt")
                events[event_id] = event
            # A metadata summary cannot claim it revalidated a repair. Preserve
            # the old debt and expose the recorded successor for the strict gate.
            repairs = [{"event_id": x["event_id"], "repairs_event_id": x["repairs_event_id"]}
                       for x in events.values() if x["repairs_event_id"] is not None]
            debts = [x for x in events.values() if x["state"] != "EM_REPRESENTED"]
            rows.append({"activity_id": path.stem, "mode": record["mode"],
                         "session_state": record["session_state"], "researcher_id": record["researcher_id"],
                         "registration_origin": record["registration_origin"],
                         "required_action": "VERIFY_RECORDED_DEBT_REPAIR" if repairs else (("PERSIST_EM_CHECKPOINT" if any(x["state"] == "SYNC_DEBT" for x in debts) else "VERIFY_EM_PUBLICATION") if debts else "INSPECT_RECORDED_FRONTIER"),
                         "sync_debt_events": [x["event_id"] for x in debts],
                         "recorded_repair_events": repairs,
                         "source_links": [f"https://github.com/{s['repository']}/blob/{s['commit']}/{s['path']}" for e in events.values() for s in e["em_sources"]],
                         "record_path": f"{STORE}/{path.stem}.json"})
        except (ActivityError, OSError, ValueError, KeyError, TypeError) as exc:
            rows.append({"activity_id": path.stem, "required_action": "REPAIR_ACTIVITY_RECORD", "error": str(exc)})
    return {"scope": "OWNER_BOOKKEEPING_ONLY_NOT_CLAIM_QUEUE", "items": rows,
            "has_more": len(paths) > limit, "limit": limit,
            "next_cursor": paths[limit - 1].stem if len(paths) > limit else None,
            "verification_scope": "RECORDED_METADATA_ONLY_SOURCE_BYTES_REVALIDATED_BY_ACTIVITY_GUARD",
            "visibility": "THIS_CHECKOUT_ONLY_NOT_A_REMOTE_BRANCH_DISCOVERY",
            "entrypoint": "python tools/research_activity.py list --limit 20"}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    sub = parser.add_subparsers(dest="command", required=True)
    reg = sub.add_parser("register")
    reg.add_argument("--mode", choices=MODES, required=True)
    reg.add_argument("--session-id")
    reg.add_argument("--researcher-id")
    reg.add_argument("--source-tracking-key")
    reg.add_argument("--activity-id")
    check = sub.add_parser("checkpoint")
    check.add_argument("--activity-id", required=True)
    check.add_argument("--event-id", required=True)
    check.add_argument("--expected-sha256", required=True)
    check.add_argument("--source-json", type=Path, required=True,
                       help="object with em_sources list and optional kb_sources list")
    check.add_argument("--repairs-event-id")
    gate = sub.add_parser("guard")
    gate.add_argument("--activity-id")
    gate.add_argument("--boundary", choices=("startup", "checkpoint", "pre-final"), default="startup")
    gate.add_argument("--event-id")
    gate.add_argument("--session-id")
    gate.add_argument("--registration-json", type=Path,
                      help="exact current activity publication pin with full observed connector readback")
    gate.add_argument("--no-new-semantic-progress", action="store_true",
                      help="no new research checkpoint, e.g. user stops before research; never clears existing debt")
    listing = sub.add_parser("list")
    listing.add_argument("--limit", type=int, default=20)
    listing.add_argument("--after")
    args = parser.parse_args(argv)
    if args.command == "register":
        value = register(root=args.root, mode=args.mode, researcher_id=args.researcher_id,
                         session_id=args.session_id, source_tracking_key=args.source_tracking_key,
                         activity_id=args.activity_id)
    elif args.command == "checkpoint":
        payload = json.loads(args.source_json.read_bytes())
        if not isinstance(payload, dict):
            raise ActivityError("source-json must contain an object")
        value = checkpoint(args.activity_id, root=args.root, event_id=args.event_id,
                           expected_sha256=args.expected_sha256, em_sources=payload.get("em_sources"),
                           kb_sources=payload.get("kb_sources"), repairs_event_id=args.repairs_event_id)
    elif args.command == "guard":
        value = guard(activity_id=args.activity_id, root=args.root, boundary=args.boundary,
                      event_id=args.event_id, session_id=args.session_id,
                      registration_source=json.loads(args.registration_json.read_bytes()) if args.registration_json else None,
                      new_semantic_progress=not args.no_new_semantic_progress)
    else:
        value = overview(args.root, limit=args.limit, after=args.after)
    if args.command in ("register", "checkpoint"):
        path = record_path(value["activity_id"], args.root)
        value = {"record": value, "record_path": path.relative_to(args.root).as_posix(),
                 "record_sha256": digest(path.read_bytes()),
                 "required_action": "PUBLISH_ACTIVITY_RECORD_WITH_CAS_AND_VERIFY_IMMUTABLE_EM_READBACK",
                 "canonical_owner_visibility": "NOT_ESTABLISHED_BY_LOCAL_WRITE"}
    print(encoded(value).decode("utf-8"), end="")
    return 2 if args.command == "guard" and not value["persistence_allowed"] else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ActivityError, OSError, ValueError) as exc:
        print(json.dumps({"error": str(exc), "required_action": "REPAIR_ACTIVITY_EVIDENCE"}))
        raise SystemExit(1)
