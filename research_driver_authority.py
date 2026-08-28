#!/usr/bin/env python3
"""Source-backed Driver authority for Enterprise Math control actions.

Driver-ID syntax is an identity handle, not authority. New Driver control actions
must bind to immutable project-side records derived from GitHub Issue #240 server
comment metadata authorized by the existing control-event allowlist. Global
Knowledge and GitHub App metadata remain provenance only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
CONTRACT = "research_driver_authority_contract.json"
CONTROL_POLICY = "research_control_event_authorization.json"
LEGACY_REVIEWS = "research_driver_followup_legacy_reviews.json"
RECORD_ROOT = "research_driver_authority_records"
CONTRACT_SCHEMA = "ENTERPRISE_MATH_DRIVER_AUTHORITY_CONTRACT_V1"
RECORD_SCHEMA = "ENTERPRISE_MATH_DRIVER_AUTHORITY_RECORD_V1"
EVENT_SCHEMA = "ENTERPRISE_MATH_DRIVER_AUTH_EVENT_V1"
EVENTS = {"AUTHORIZE", "REVOKE"}
DRIVER_RE = re.compile(r"^EM-DVR-[A-Z0-9]{4,8}$")


class DriverAuthorityError(ValueError):
    pass


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise DriverAuthorityError(f"{path}: JSON object required")
    return value


def _parse_time(value: Any, label: str) -> datetime:
    if not isinstance(value, str) or not value.strip():
        raise DriverAuthorityError(f"{label} is required")
    try:
        dt = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
    except Exception as exc:
        raise DriverAuthorityError(f"invalid {label}: {value!r}") from exc
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _sha256_text(value: str) -> str:
    return "sha256:" + hashlib.sha256(value.encode("utf-8")).hexdigest()


def _record_id(driver_id: str, event: str, comment_id: int) -> str:
    raw = f"{driver_id}\0{event}\0{comment_id}".encode("utf-8")
    return "DA-" + hashlib.sha256(raw).hexdigest()[:20].upper()


def contract_enabled(root: Path = ROOT) -> bool:
    return (root / CONTRACT).exists()


def contract(root: Path = ROOT) -> dict[str, Any] | None:
    path = root / CONTRACT
    if not path.exists():
        return None
    value = _load(path)
    if value.get("schema") != CONTRACT_SCHEMA:
        raise DriverAuthorityError("unexpected Driver authority contract schema")
    if value.get("status") not in {"ACTIVE_CANONICAL_CANDIDATE", "ACTIVE_CANONICAL"}:
        raise DriverAuthorityError("Driver authority contract is not active")
    if value.get("repository") != "awdawmip/enterprise-math" or value.get("control_issue") != 240:
        raise DriverAuthorityError("Driver authority repository/issue boundary drifted")
    if value.get("source_event_schema") != EVENT_SCHEMA or value.get("record_schema") != RECORD_SCHEMA:
        raise DriverAuthorityError("Driver authority schema boundary drifted")
    if value.get("global_knowledge_runtime_authority") is not False:
        raise DriverAuthorityError("Global Knowledge may not grant project runtime authority")
    if value.get("github_app_runtime_authority") is not False:
        raise DriverAuthorityError("GitHub App metadata may not grant Driver authority")
    return value


def control_policy(root: Path = ROOT) -> dict[str, Any]:
    path = root / CONTROL_POLICY
    value = _load(path)
    if value.get("schema") != "ENTERPRISE_MATH_CONTROL_EVENT_AUTHORIZATION_V1":
        raise DriverAuthorityError("unexpected control-event authorization schema")
    if value.get("status") != "ACTIVE_CANONICAL":
        raise DriverAuthorityError("control-event authorization policy is not active")
    if value.get("repository") != "awdawmip/enterprise-math" or value.get("issue") != 240:
        raise DriverAuthorityError("control-event authorization repository/issue boundary drifted")
    if value.get("mode") != "EXACT_SERVER_AUTHOR_ALLOWLIST":
        raise DriverAuthorityError("unsupported control-event authorization mode")
    return value


def legacy_review_ids(root: Path = ROOT) -> set[str]:
    path = root / LEGACY_REVIEWS
    if not path.exists():
        return set()
    value = _load(path)
    ids = value.get("review_ids")
    if not isinstance(ids, list) or any(not isinstance(item, str) or not item for item in ids):
        raise DriverAuthorityError("legacy review baseline is invalid")
    return set(ids)


def iter_records(root: Path = ROOT) -> list[dict[str, Any]]:
    directory = root / RECORD_ROOT
    if not directory.exists():
        return []
    out: list[dict[str, Any]] = []
    for path in sorted(directory.glob("*/*.json")):
        value = _load(path)
        value["_record_path"] = path.relative_to(root).as_posix()
        out.append(value)
    return out


def _server_author_allowed(author: dict[str, Any], root: Path) -> bool:
    policy = control_policy(root)
    entries = policy.get("authorized_server_authors")
    if not isinstance(entries, list):
        return False
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        associations = entry.get("author_association")
        if (
            author.get("login") == entry.get("login")
            and author.get("user_id") == entry.get("user_id")
            and isinstance(associations, list)
            and author.get("author_association") in associations
        ):
            return True
    return False


def validate_record(record: dict[str, Any], root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    prefix = str(record.get("_record_path") or record.get("authority_record_id") or "<driver-authority>")
    if record.get("record_schema") != RECORD_SCHEMA:
        errors.append(f"{prefix}: wrong record schema")
    driver_id = record.get("driver_id")
    if not isinstance(driver_id, str) or not DRIVER_RE.fullmatch(driver_id):
        errors.append(f"{prefix}: driver_id must use EM-DVR-* syntax")
    event = record.get("event")
    if event not in EVENTS:
        errors.append(f"{prefix}: invalid authority event")
    if record.get("scope") != "CONTROL_PLANE" or record.get("authority") != "RESEARCH_DRIVER":
        errors.append(f"{prefix}: invalid Driver authority scope")
    comment_id = record.get("source_comment_id")
    if type(comment_id) is not int or comment_id <= 0:
        errors.append(f"{prefix}: source_comment_id must be positive integer")
    if isinstance(driver_id, str) and isinstance(event, str) and type(comment_id) is int:
        expected = _record_id(driver_id, event, comment_id)
        if record.get("authority_record_id") != expected:
            errors.append(f"{prefix}: authority_record_id mismatch")
    if record.get("source_repository") != "awdawmip/enterprise-math" or record.get("source_issue") != 240:
        errors.append(f"{prefix}: source repository/issue boundary mismatch")
    expected_issue_url = "https://api.github.com/repos/awdawmip/enterprise-math/issues/240"
    if record.get("source_issue_url") != expected_issue_url:
        errors.append(f"{prefix}: source_issue_url mismatch")
    if type(comment_id) is int:
        expected_comment_url = f"https://api.github.com/repos/awdawmip/enterprise-math/issues/comments/{comment_id}"
        if record.get("source_comment_url") != expected_comment_url:
            errors.append(f"{prefix}: source_comment_url mismatch")
    body = record.get("source_body")
    if not isinstance(body, str):
        errors.append(f"{prefix}: source_body is required")
    else:
        if record.get("source_body_sha256") != _sha256_text(body):
            errors.append(f"{prefix}: source body digest mismatch")
        try:
            payload = json.loads(body)
        except json.JSONDecodeError:
            payload = None
            errors.append(f"{prefix}: source body is not JSON")
        if isinstance(payload, dict):
            if payload.get("schema") != EVENT_SCHEMA:
                errors.append(f"{prefix}: source event schema mismatch")
            for field in ("event", "driver_id", "scope", "authority"):
                if payload.get(field) != record.get(field):
                    errors.append(f"{prefix}: source body field mismatch: {field}")
    try:
        created = _parse_time(record.get("source_created_at"), "source_created_at")
        updated = _parse_time(record.get("source_updated_at"), "source_updated_at")
        if created != updated or record.get("edited") is not False:
            errors.append(f"{prefix}: edited Driver authority event is not valid authority")
    except DriverAuthorityError as exc:
        errors.append(f"{prefix}: {exc}")
    author = record.get("source_server_author")
    if not isinstance(author, dict) or not _server_author_allowed(author, root):
        errors.append(f"{prefix}: source server author is not control-authorized")
    if record.get("server_authenticated") is not True or record.get("control_authorized") is not True:
        errors.append(f"{prefix}: server authentication/control authorization missing")
    if record.get("github_app_is_authority") is not False:
        errors.append(f"{prefix}: GitHub App metadata cannot be authority")
    if record.get("global_knowledge_is_authority") is not False:
        errors.append(f"{prefix}: Global Knowledge cannot be project authority")
    for field in ("working_truth_granted", "foundation_authority_granted", "canonical_promotion_granted"):
        if record.get(field) is not False:
            errors.append(f"{prefix}: {field} must be false")
    return errors


def valid_records(root: Path = ROOT) -> list[dict[str, Any]]:
    rows = iter_records(root)
    errors: list[str] = []
    seen_ids: set[str] = set()
    seen_comments: set[int] = set()
    for row in rows:
        errors.extend(validate_record(row, root))
        rid = row.get("authority_record_id")
        cid = row.get("source_comment_id")
        if isinstance(rid, str):
            if rid in seen_ids:
                errors.append(f"duplicate authority_record_id: {rid}")
            seen_ids.add(rid)
        if type(cid) is int:
            if cid in seen_comments:
                errors.append(f"duplicate source_comment_id: {cid}")
            seen_comments.add(cid)
    if errors:
        raise DriverAuthorityError("; ".join(errors))
    return rows


def active_authority_at(driver_id: str, at: str, root: Path = ROOT) -> dict[str, Any] | None:
    if not contract_enabled(root):
        return None
    contract(root)
    normalized = driver_id.strip().upper()
    if not DRIVER_RE.fullmatch(normalized):
        return None
    instant = _parse_time(at, "authority check time")
    rows = []
    for row in valid_records(root):
        if row.get("driver_id") != normalized:
            continue
        created = _parse_time(row.get("source_created_at"), "source_created_at")
        if created <= instant:
            rows.append(row)
    rows.sort(key=lambda item: int(item["source_comment_id"]))
    if not rows or rows[-1].get("event") != "AUTHORIZE":
        return None
    return rows[-1]


def require_active_driver(driver_id: str, at: str, root: Path = ROOT) -> dict[str, Any] | None:
    if not contract_enabled(root):
        return None
    authority = active_authority_at(driver_id, at, root)
    if authority is None:
        raise DriverAuthorityError(
            f"Driver {driver_id!r} has no source-backed ACTIVE authority at {at}"
        )
    return authority


def review_authority_errors(review: dict[str, Any], root: Path = ROOT) -> list[str]:
    if not contract_enabled(root):
        return []
    review_id = review.get("review_id")
    if isinstance(review_id, str) and review_id in legacy_review_ids(root):
        return []
    prefix = str(review.get("_review_path") or review_id or "<review>")
    driver_id = review.get("driver_id")
    reviewed_at = review.get("reviewed_at")
    if not isinstance(driver_id, str) or not DRIVER_RE.fullmatch(driver_id.strip().upper()):
        return [f"{prefix}: post-cutover review driver_id must use EM-DVR-* syntax"]
    if not isinstance(reviewed_at, str) or not reviewed_at:
        return [f"{prefix}: post-cutover review reviewed_at is required"]
    try:
        authority = require_active_driver(driver_id, reviewed_at, root)
    except DriverAuthorityError as exc:
        return [f"{prefix}: {exc}"]
    if authority is None:
        return [f"{prefix}: Driver authority enforcement unexpectedly disabled"]
    if review.get("driver_authority_record_id") != authority.get("authority_record_id"):
        return [f"{prefix}: driver_authority_record_id does not pin active authority"]
    if review.get("driver_authority_source_comment_id") != authority.get("source_comment_id"):
        return [f"{prefix}: driver_authority_source_comment_id does not pin active authority"]
    return []


def audit(root: Path = ROOT) -> list[str]:
    if not contract_enabled(root):
        return []
    errors: list[str] = []
    try:
        contract(root)
        rows = valid_records(root)
    except Exception as exc:
        return [str(exc)]
    if not rows:
        errors.append("Driver authority contract is active but no authority records exist")
    try:
        from tools import research_result_records as result_records
        reviews = result_records.iter_reviews(root)
    except Exception as exc:
        errors.append(f"cannot load canonical review view: {exc}")
        return errors
    for review in reviews:
        errors.extend(review_authority_errors(review, root))
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Enterprise Math source-backed Driver authority")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("audit")
    check = sub.add_parser("check")
    check.add_argument("--driver-id", required=True)
    check.add_argument("--at", required=True)
    args = parser.parse_args(argv)
    if args.command == "audit":
        errors = audit(ROOT)
        if errors:
            for error in errors:
                print("ERROR:", error)
            return 1
        print(f"PASS: source-backed Driver authority valid ({len(iter_records(ROOT))} record(s)).")
        return 0
    authority = require_active_driver(args.driver_id, args.at, ROOT)
    print(json.dumps(authority, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except DriverAuthorityError as exc:
        print("ERROR:", exc, file=sys.stderr)
        raise SystemExit(1)
