"""Prospective Result/review admission after the exact immutable cutover.

Receipts attest locally verified canonical control evidence, not platform-signed
chat identity. They prevent old-format writers and fenced executions from
silently becoming operational; arbitrary malicious repository-owner forgery is
outside this control boundary. Legacy pins never exempt the original audits.
"""
from __future__ import annotations

import copy
import base64
import hashlib
import json
import re
import tempfile
from functools import lru_cache
from pathlib import Path
from typing import Any, Mapping

CUTOVER = "control_plane/continuation_record_cutover.json"
SCHEMA = "ENTERPRISE_MATH_CONTROL_WRITE_AUTHORIZATION_V1"


def payload_digest(record: Mapping[str, Any]) -> str:
    value = {k: v for k, v in record.items() if not k.startswith("_") and k != "write_authorization"}
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


@lru_cache(maxsize=8)
def _baseline(path: str, mtime_ns: int, size: int) -> dict[str, Any]:
    value = json.loads(Path(path).read_text(encoding="utf-8"))
    if value.get("schema") != "ENTERPRISE_MATH_CONTINUATION_RECORD_CUTOVER_V1":
        raise ValueError("invalid continuation cutover schema")
    return value["records"]


def _pins(root: Path) -> dict[str, Any] | None:
    path = root / CUTOVER
    if not path.exists():
        return None
    stat = path.stat()
    return _baseline(str(path.resolve()), stat.st_mtime_ns, stat.st_size)


def record_path(record: Mapping[str, Any], kind: str) -> str:
    stored = record.get("_record_path" if kind == "RESULT" else "_review_path")
    if isinstance(stored, str):
        return stored
    if kind == "RESULT":
        return f"research_result_records/{record['task_id']}/{record['result_id']}.json"
    return f"research_result_reviews/{record['result_id']}/{record['review_id']}.json"


def build_receipt(record: Mapping[str, Any], kind: str, context: Mapping[str, Any]) -> dict[str, Any]:
    return {"schema": SCHEMA, "kind": kind,
            "evidence_kind": "CANONICAL_LOCAL_GUARD_WITH_SERVER_SOURCE_ENVELOPES_NOT_PLATFORM_ATTESTATION",
            "payload_sha256": payload_digest(record), **copy.deepcopy(dict(context))}


def _canonical_frozen_definition(publication: Mapping[str, Any], receipt: Mapping[str, Any]) -> dict[str, Any]:
    """Rebuild from immutable publication plus blob-verified historical taskbook."""
    from tools import research_dispatch
    raw = base64.b64decode(receipt["taskbook_content_base64"], validate=True)
    blob = hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()
    if str(publication.get("taskbook_blob_sha1", "")).removeprefix("sha1:") != blob:
        raise ValueError("write_authorization frozen taskbook bytes do not match immutable publication")
    with tempfile.TemporaryDirectory(prefix="em-receipt-taskbook-") as temp:
        root = Path(temp)
        path = (root / str(publication["taskbook_path"])).resolve()
        if not path.is_relative_to(root.resolve()):
            raise ValueError("unsafe immutable taskbook path")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
        return research_dispatch.registered_definition(dict(publication), root)


def receipt_error(record: Mapping[str, Any], kind: str, root: Path) -> str | None:
    pins = _pins(root)
    if pins is None:
        return None
    path = record_path(record, kind)
    legacy = pins.get(path)
    if legacy is not None:
        data = (root / path).read_bytes()
        blob = hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()
        if legacy.get("sha256") == hashlib.sha256(data).hexdigest() and legacy.get("git_blob_sha1") == blob:
            return None
        return "immutable pre-cutover record bytes changed; cutover grants no repair authority"
    receipt = record.get("write_authorization")
    if not isinstance(receipt, dict) or receipt.get("schema") != SCHEMA or receipt.get("kind") != kind:
        return "post-cutover record requires canonical write_authorization"
    if receipt.get("payload_sha256") != payload_digest(record):
        return "write_authorization payload binding changed"
    if not isinstance(receipt.get("source_commit"), str) or not re.fullmatch(r"[0-9a-f]{40}", receipt["source_commit"]):
        return "write_authorization has no immutable source snapshot"
    try:
        from tools import research_runtime_reducer as reducer
        at = reducer.parse_time(receipt["authorized_at"])
        principal = receipt["principal"]
        if kind == "RESULT":
            from tools import research_dispatch
            comments = receipt["server_comments"]
            events = research_dispatch.events_from_github_comments(comments, root=root)
            publication = root / f"research_task_records/{record['task_id']}/{record['publication_id']}.json"
            published = json.loads(publication.read_text(encoding="utf-8"))
            if published.get("taskbook_blob_sha1") != record.get("taskbook_blob_sha1"):
                return "write_authorization publication source pin mismatch"
            definition = _canonical_frozen_definition(published, receipt)
            if definition != receipt.get("task_definition"):
                return "write_authorization task definition differs from immutable publication/taskbook authority"
            accepted, rejected = research_dispatch._event_authentication_filter(definition, events)
            filtered, _ = research_dispatch._filter_registered_events(definition, accepted, root, result_state=None)
            state = reducer.reduce_task(definition, filtered, default_lease_minutes=120, now=at)
            for field in ("claim_id", "researcher_id"):
                if state.get(field) != record.get(field) or principal.get(field) != record.get(field):
                    return f"write_authorization {field} belongs to a fenced or different execution"
            if state.get("dispatch_state") != "LEASED" or principal.get("ownership_epoch") != state.get("ownership_epoch"):
                return "write_authorization does not bind the winning live ownership epoch"
            if not isinstance(principal.get("session_id"), str) or not principal["session_id"].strip():
                return "write_authorization requires a real declared execution session"
            if state.get("session_id") is not None and principal["session_id"] != state["session_id"]:
                return "write_authorization successor session mismatch"
            if definition.get("kind") == "GOVERNANCE":
                import research_driver_authority as driver
                boundary = receipt.get("authority_observed_through_comment_id")
                if principal.get("executor_role") != "RESEARCH_DRIVER" or type(boundary) is not int:
                    return "GOVERNANCE Result requires actual Driver role and observed DA boundary"
                authority = driver.require_active_driver(record["researcher_id"], at.isoformat(), root, through_comment_id=boundary)
                if authority is None or principal.get("driver_authority_record_id") != authority["authority_record_id"]:
                    return "GOVERNANCE Result Driver authority binding changed"
                body = json.loads(authority["source_body"])
                session = body.get("session_id") or (body.get("succession") or {}).get("session_id")
                if not isinstance(session, str) or not session or principal["session_id"] != session:
                    return "GOVERNANCE Result requires explicitly session-bound DA"
        else:
            import research_driver_authority as driver
            boundary = receipt.get("authority_observed_through_comment_id")
            if type(boundary) is not int or boundary <= 0:
                return "write_authorization has no observed Driver event boundary"
            authority = driver.require_active_driver(record["driver_id"], at.isoformat(), root, through_comment_id=boundary)
            if authority is None or principal.get("authority_record_id") != authority["authority_record_id"]:
                return "write_authorization Driver authority was not active at write time"
            if record.get("driver_authority_record_id") != authority["authority_record_id"]:
                return "review binds a different historical Driver authority"
            payload = json.loads(authority["source_body"])
            if not isinstance(principal.get("session_id"), str) or not principal["session_id"].strip():
                return "write_authorization review requires its execution session"
            session = payload.get("session_id") or (payload.get("succession") or {}).get("session_id")
            if not isinstance(session, str) or not session or principal.get("session_id") != session:
                return "write_authorization Driver session mismatch"
            result_path = root / f"research_result_records/{record['task_id']}/{record['result_id']}.json"
            result = json.loads(result_path.read_text(encoding="utf-8"))
            declared = record.get("reviewer_contribution_ids")
            if not isinstance(declared, list):
                return "review has no preserved contributor declaration"
            if (set(result.get("contributor_ids", [])) | {result.get("researcher_id")}) & (set(declared) | {record["driver_id"]}):
                return "reviewer contribution overlaps result authorship"
    except Exception as exc:
        return "write_authorization evidence failed: " + str(exc)
    return None


def operational(records: list[dict[str, Any]], kind: str, root: Path) -> list[dict[str, Any]]:
    return [row for row in records if receipt_error(row, kind, root) is None]


def diagnostics(records: list[dict[str, Any]], kind: str, root: Path) -> list[dict[str, Any]]:
    out = []
    for row in records:
        error = receipt_error(row, kind, root)
        if error:
            out.append({"task_id": row.get("task_id"), "publication_id": row.get("publication_id"),
                        "record_path": record_path(row, kind), "kind": kind,
                        "result_id": row.get("result_id"), "review_id": row.get("review_id"), "reason": error})
    return out
