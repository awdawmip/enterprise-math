"""Offline professional-source cache gate. No network, scheduling or remote writes."""
from __future__ import annotations
import argparse
from datetime import datetime, timedelta, timezone
import hashlib
import json
from pathlib import Path
import re
from typing import Any
import unicodedata

SCHEMA = "PROFESSIONAL_SOURCE_RECORD_V1"
IDENTITY_FIELDS = {"source", "operation", "subject", "parameters", "scope", "version"}


def timestamp(value: str) -> datetime:
    dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        raise ValueError("Timezone required")
    return dt.astimezone(timezone.utc)


def canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":"), allow_nan=False).encode("utf-8")


def normal(value: Any) -> Any:
    if isinstance(value, str):
        return unicodedata.normalize("NFC", value).strip()
    if isinstance(value, dict):
        return {k: normal(v) for k, v in value.items()}
    if isinstance(value, list):
        return [normal(v) for v in value]
    return value


def cache_key(identity: dict, category: str) -> str:
    if set(identity) != IDENTITY_FIELDS or not identity["subject"]:
        raise ValueError("Exact identity fields and a resolved subject are required")
    if identity["scope"] not in {"current", "fixed_version"}:
        raise ValueError("Invalid scope")
    if identity["scope"] == "fixed_version" and not identity["version"]:
        raise ValueError("Fixed-version requests need an explicit version")
    if identity["scope"] == "current" and identity["version"] is not None:
        raise ValueError("Current-state requests must not impersonate a fixed version")
    return hashlib.sha256(canonical({"identity": normal(identity),
                                     "category": category})).hexdigest()


def expiry(observed_at: str, category: str, policy: dict,
           state: str = "VALID") -> str | None:
    start = timestamp(observed_at)
    seconds = (policy["negative_ttl_seconds"] if state == "NO_HIT"
               else policy["classes"][category]["ttl_seconds"])
    return None if seconds is None else (start + timedelta(seconds=seconds)).isoformat()


def safe_path(root: Path, relative: str) -> Path:
    p = Path(relative)
    if p.is_absolute() or ".." in p.parts:
        raise ValueError("Path escape")
    resolved = (root / p).resolve()
    if not resolved.is_relative_to(root.resolve()):
        raise ValueError("Path escape")
    return resolved


def validate_record(record: dict, policy: dict, root: Path | None = None) -> None:
    required = {"schema", "id", "identity", "category", "cache_key", "observed_at",
                "ingested_at", "expires_at", "state", "coverage", "raw", "evidence"}
    if not required <= record.keys() or record["schema"] != SCHEMA:
        raise ValueError("Record schema/fields")
    category = record["category"]
    if category not in policy["classes"]:
        raise ValueError("Unknown information class")
    if record["identity"]["scope"] != policy["classes"][category]["scope"]:
        raise ValueError("Scope/class mismatch")
    if record["cache_key"] != cache_key(record["identity"], category):
        raise ValueError("Cache-key mismatch")
    if record["state"] not in {"VALID", "NO_HIT", "CONFLICT", "SUPERSEDED"}:
        raise ValueError("Invalid record state")
    if timestamp(record["ingested_at"]) < timestamp(record["observed_at"]):
        raise ValueError("Ingestion precedes observation")
    expected = expiry(record["observed_at"], category, policy, record["state"])
    actual = record["expires_at"]
    if (expected is None) != (actual is None) or (
            expected is not None and timestamp(expected) != timestamp(actual)):
        raise ValueError("Expiry must derive from original observation")
    raw = record["raw"]
    if raw["representation"] not in {"provider_result_json", "official_document",
                                     "public_web_snapshot", "user_file"}:
        raise ValueError("Reference-only or model summary cannot be raw evidence")
    if raw["completeness"] not in {"FULL_RETURNED_RESULT", "PARTIAL", "REDACTED"}:
        raise ValueError("Unspecified coverage boundary")
    if not re.fullmatch(r"[a-f0-9]{64}", raw["sha256"]):
        raise ValueError("Invalid raw digest")
    if not isinstance(record["coverage"], list) or not all(
            isinstance(x, str) for x in record["coverage"]):
        raise ValueError("Field coverage must be explicit")
    evidence = record["evidence"]
    if not evidence.get("url") or not evidence.get("source_status"):
        raise ValueError("Missing source provenance")
    if raw["representation"] == "provider_result_json":
        for field in ("batch_id", "request_id", "provider_request_id"):
            if not evidence.get(field):
                raise ValueError("Missing matched provider-result identifier")
        if record["state"] == "VALID" and evidence["source_status"] != "COMPLETED":
            raise ValueError("Unfinished result is not valid evidence")
    if record["state"] == "NO_HIT" and evidence["source_status"] != "NO_HIT":
        raise ValueError("Errors are not negative search results")
    if root is not None:
        data = safe_path(root, raw["path"]).read_bytes()
        if hashlib.sha256(data).hexdigest() != raw["sha256"]:
            raise ValueError("Raw-payload digest mismatch")


def assert_no_reage(old: dict, new: dict) -> None:
    """Changing an observation creates a new record, never refreshes an old ID."""
    for key in ("id", "identity", "category", "cache_key", "observed_at", "expires_at", "raw"):
        if old[key] != new[key]:
            raise ValueError("Existing evidence identity/clock/payload is immutable")


def decide(need: dict, records: list[dict], policy: dict, now: str,
           root: Path | None = None) -> dict:
    """The caller resolves task semantics and direct-user instructions first.

    Required need fields: professional_evidence_required, identity, category,
    required_fields. Optional explicit_refresh needs refresh_instruction text.
    This gate is not a substitute for provider parameter/permission validation.
    """
    def result(action: str, reason: str, record: dict | None = None) -> dict:
        out = {"action": action, "reason": reason, "provider_query": action == "QUERY_REQUIRED"}
        if record:
            out.update(record_id=record["id"], observed_at=record["observed_at"],
                       expires_at=record["expires_at"])
        return out
    if not need.get("professional_evidence_required", False):
        return result("NOT_TRIGGERED", "No new professional evidence is needed")
    if need.get("identity_ambiguous"):
        return result("RESOLVE_IDENTITY", "Do not merge or query ambiguous entities")
    if need.get("pending_batch_id"):
        return {**result("RESUME_PENDING_BATCH", "Read the existing batch; do not reissue"),
                "batch_id": need["pending_batch_id"]}
    category = need["category"]
    if category not in policy["classes"] or need["identity"]["scope"] != policy["classes"][category]["scope"]:
        raise ValueError("Unknown request category or mismatched scope")
    cache_key(need["identity"], category)
    clock = timestamp(now)
    def query(reason: str) -> dict:
        identity = need["identity"]
        if identity["operation"] not in policy["verified_operations"].get(identity["source"], []):
            return result("UNSUPPORTED_OPERATION", "Do not invent provider capabilities")
        if not need.get("query_authorized", True):
            return result("AUTHORIZATION_REQUIRED", "Do not purchase or expand access")
        if identity["source"] == "caixin" and not need.get("points_authorized", False):
            return result("POINTS_AUTHORIZATION_REQUIRED", "Explicit point-spend approval required")
        return result("QUERY_REQUIRED", reason)
    if need.get("explicit_refresh"):
        if not str(need.get("refresh_instruction", "")).strip():
            raise ValueError("Refresh needs the explicit current-user instruction")
        return query("EXPLICIT_CURRENT_USER_REFRESH")
    # Same provider query may serve multiple field lifetimes; changing a class
    # is not permission to repeat an unexpired request. Recalculate from the
    # original observation, never from the new question or import time.
    candidates = [r for r in records if normal(r.get("identity")) == normal(need["identity"])
                  and r.get("state") != "SUPERSEDED"]
    if not candidates:
        return query("CACHE_MISS")
    try:
        record = max(candidates, key=lambda r: timestamp(r["observed_at"]))
        validate_record(record, policy, root)
        if timestamp(record["observed_at"]) > clock:
            raise ValueError("Observation lies in the future")
        fields = set(record["coverage"])
        for other in candidates:
            if other["raw"] == record["raw"] and other["observed_at"] == record["observed_at"]:
                validate_record(other, policy, root)
                fields.update(other["coverage"])
        record = {**record, "category": category, "coverage": sorted(fields),
                  "expires_at": expiry(record["observed_at"], category, policy, record["state"])}
    except (ValueError, TypeError, KeyError, OSError):
        return result("RECOVER_STORED_SOURCE", "Repair/read the stored original, not a silent provider retry")
    if record["expires_at"] and clock >= timestamp(record["expires_at"]):
        return query("CACHE_EXPIRED")
    if need.get("known_conflict") or record["state"] == "CONFLICT":
        return result("CONFLICT_NEEDS_INSTRUCTION", "Do not use as current or silently requery", record)
    if record["state"] == "NO_HIT":
        return result("REUSED_NEGATIVE_CACHE", "This query found nothing; not proof of absence", record)
    if (not set(need["required_fields"]) <= set(record["coverage"]) or
            record["raw"]["completeness"] != "FULL_RETURNED_RESULT"):
        return result("GAP_NEEDS_INSTRUCTION", "Unexpired same-query result is incomplete", record)
    return result("REUSED_VALID_CACHE", "Read stored raw fields; no new provider query", record)


def load_records(root: Path) -> tuple[dict, list[dict]]:
    directory = root / "sources/professional"
    policy = json.loads((directory / "policy.json").read_text())
    catalog = json.loads((directory / "catalog.json").read_text())
    records = []
    for entry in catalog["records"]:
        record = json.loads(safe_path(root, entry["path"]).read_text())
        validate_record(record, policy, root)
        if entry["id"] != record["id"] or entry["cache_key"] != record["cache_key"]:
            raise ValueError("Catalog mismatch")
        records.append(record)
    if len({r["id"] for r in records}) != len(records):
        raise ValueError("Duplicate record ID")
    return policy, records


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--need", type=Path)
    parser.add_argument("--now", default=datetime.now(timezone.utc).isoformat())
    args = parser.parse_args()
    try:
        policy, records = load_records(args.root)
        output = (decide(json.loads(args.need.read_text()), records, policy, args.now, args.root)
                  if args.need else {"validation": "PASS", "records": len(records), "network_calls": 0})
    except (ValueError, TypeError, KeyError, OSError) as exc:
        parser.exit(2, f"Validation failed: {exc}\n")
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
