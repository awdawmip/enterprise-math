#!/usr/bin/env python3
"""Fail-closed immutable task-publication audit with exact legacy heading waivers.

The underlying immutable record audit remains authoritative for publication forks,
metadata, taskbook paths, Git-blob pins, parseability and body-policy failures.
This wrapper may suppress only exact mandatory-heading errors listed in a
publication+path+blob pinned compatibility waiver, after independently proving
that the corresponding legacy heading exists with non-empty non-placeholder
content. Stale or unused waivers are errors.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from tools import research_task_records, research_taskbook

ROOT = Path(__file__).resolve().parents[1]
WAIVER_FILE = "research_task_record_compatibility_waivers.json"
WAIVER_SCHEMA = "ENTERPRISE_MATH_TASK_RECORD_COMPATIBILITY_WAIVERS_V1"
WAIVER_SCOPE = "MANDATORY_BODY_SECTION_HEADING_ALIAS_ONLY"
_PLACEHOLDER = re.compile(r"^\s*<[^>\n]+>\s*$", re.MULTILINE)


class CompatibilityAuditError(ValueError):
    pass


def _load_registry(root: Path) -> list[dict[str, Any]]:
    path = root / WAIVER_FILE
    if not path.exists():
        return []
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict) or value.get("schema") != WAIVER_SCHEMA:
        raise CompatibilityAuditError(f"{WAIVER_FILE}: wrong schema")
    if value.get("status") != "ACTIVE":
        raise CompatibilityAuditError(f"{WAIVER_FILE}: status must be ACTIVE")
    rows = value.get("waivers")
    if not isinstance(rows, list):
        raise CompatibilityAuditError(f"{WAIVER_FILE}: waivers must be a list")
    seen_ids: set[str] = set()
    seen_pubs: set[str] = set()
    out: list[dict[str, Any]] = []
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise CompatibilityAuditError(f"{WAIVER_FILE}: waiver {index} must be an object")
        wid = row.get("waiver_id")
        pid = row.get("publication_id")
        if not isinstance(wid, str) or not wid:
            raise CompatibilityAuditError(f"{WAIVER_FILE}: waiver {index} missing waiver_id")
        if wid in seen_ids:
            raise CompatibilityAuditError(f"{WAIVER_FILE}: duplicate waiver_id {wid}")
        if not isinstance(pid, str) or not pid:
            raise CompatibilityAuditError(f"{WAIVER_FILE}: {wid} missing publication_id")
        if pid in seen_pubs:
            raise CompatibilityAuditError(f"{WAIVER_FILE}: duplicate publication waiver {pid}")
        if row.get("scope") != WAIVER_SCOPE:
            raise CompatibilityAuditError(f"{WAIVER_FILE}: {wid} has unsupported scope")
        for flag in (
            "working_truth_granted",
            "foundation_authority_granted",
            "canonical_promotion_granted",
            "successor_triggered",
        ):
            if row.get(flag) is not False:
                raise CompatibilityAuditError(f"{WAIVER_FILE}: {wid} cannot grant {flag}")
        aliases = row.get("legacy_section_aliases")
        if not isinstance(aliases, dict) or not aliases:
            raise CompatibilityAuditError(f"{WAIVER_FILE}: {wid} missing legacy_section_aliases")
        if any(
            not isinstance(current, str)
            or current not in research_task_records.MANDATORY_BODY_SECTIONS
            or not isinstance(legacy, str)
            or not legacy.strip()
            for current, legacy in aliases.items()
        ):
            raise CompatibilityAuditError(f"{WAIVER_FILE}: {wid} has invalid section alias mapping")
        seen_ids.add(wid)
        seen_pubs.add(pid)
        out.append(row)
    return out


def _heading_payloads(body: str) -> dict[str, str]:
    lines = body.splitlines()
    hits: list[tuple[int, str]] = []
    for index, line in enumerate(lines):
        match = re.match(r"^\s*##\s+(?:\d+(?:\.\d+)*[.)]?\s+)?(.+?)\s*$", line)
        if match:
            hits.append((index, match.group(1).strip()))
    out: dict[str, str] = {}
    for pos, (index, name) in enumerate(hits):
        end = hits[pos + 1][0] if pos + 1 < len(hits) else len(lines)
        out[name] = "\n".join(lines[index + 1 : end]).strip()
    return out


def _waiver_suppressions(root: Path) -> tuple[set[str], list[str]]:
    suppressions: set[str] = set()
    errors: list[str] = []
    try:
        waivers = _load_registry(root)
        records = research_task_records.iter_records(root)
    except Exception as exc:
        return set(), [str(exc)]
    by_pub = {
        str(item.get("publication_id")): item
        for item in records
        if isinstance(item.get("publication_id"), str)
    }
    for row in waivers:
        wid = str(row["waiver_id"])
        pid = str(row["publication_id"])
        record = by_pub.get(pid)
        if record is None:
            errors.append(f"{WAIVER_FILE}: {wid}: unknown publication_id {pid}")
            continue
        task_id = row.get("task_id")
        path_value = row.get("taskbook_path")
        blob = row.get("taskbook_blob_sha1")
        if record.get("task_id") != task_id:
            errors.append(f"{WAIVER_FILE}: {wid}: task_id does not match publication")
            continue
        if record.get("taskbook_path") != path_value:
            errors.append(f"{WAIVER_FILE}: {wid}: taskbook_path does not match publication")
            continue
        if record.get("taskbook_blob_sha1") != blob:
            errors.append(f"{WAIVER_FILE}: {wid}: taskbook_blob_sha1 does not match publication")
            continue
        if not isinstance(path_value, str):
            errors.append(f"{WAIVER_FILE}: {wid}: invalid taskbook_path")
            continue
        path = root / path_value
        if not path.exists():
            errors.append(f"{WAIVER_FILE}: {wid}: taskbook path missing")
            continue
        actual_blob = research_task_records.taskbook_blob(path)
        if actual_blob != blob:
            errors.append(f"{WAIVER_FILE}: {wid}: pinned taskbook blob drift")
            continue
        try:
            meta, body = research_taskbook.split_taskbook(path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"{WAIVER_FILE}: {wid}: taskbook parse failed: {exc}")
            continue
        if meta.get("task_id") != task_id:
            errors.append(f"{WAIVER_FILE}: {wid}: taskbook task_id mismatch")
            continue
        aliases = dict(row["legacy_section_aliases"])
        raw_body_errors = research_task_records.validate_body(body)
        expected_body_errors = {
            f"mandatory body section is missing or empty: {current}"
            for current in aliases
        }
        if set(raw_body_errors) != expected_body_errors:
            errors.append(
                f"{WAIVER_FILE}: {wid}: waiver scope does not exactly equal current body-policy errors; "
                f"expected={sorted(expected_body_errors)!r} actual={sorted(raw_body_errors)!r}"
            )
            continue
        payloads = _heading_payloads(body)
        bad_alias = False
        for current, legacy in aliases.items():
            payload = payloads.get(legacy, "")
            if not payload:
                errors.append(f"{WAIVER_FILE}: {wid}: legacy heading {legacy!r} for {current!r} is missing or empty")
                bad_alias = True
            elif _PLACEHOLDER.search(payload):
                errors.append(f"{WAIVER_FILE}: {wid}: legacy heading {legacy!r} contains placeholder text")
                bad_alias = True
        if bad_alias:
            continue
        prefix = record.get("_record_path", "<record>")
        suppressions.update(f"{prefix}: {message}" for message in expected_body_errors)
    return suppressions, errors


def audit(root: Path = ROOT) -> list[str]:
    raw_errors = research_task_records.audit(root)
    suppressions, waiver_errors = _waiver_suppressions(root)
    raw_set = set(raw_errors)
    stale = sorted(suppressions - raw_set)
    errors = list(waiver_errors)
    errors.extend(f"{WAIVER_FILE}: stale or unused suppression: {item}" for item in stale)
    errors.extend(item for item in raw_errors if item not in suppressions)
    return errors


def main() -> int:
    errors = audit(ROOT)
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    suppressions, _ = _waiver_suppressions(ROOT)
    print(
        "PASS: immutable task publication audit valid with "
        f"{len(suppressions)} exact blob-pinned legacy heading suppression(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
