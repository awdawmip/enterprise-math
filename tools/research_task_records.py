#!/usr/bin/env python3
"""Public immutable task-publication facade with exact historical compatibility.

The strict V2 implementation lives in ``control_plane.research_task_records_impl``.
This facade preserves that implementation unchanged for current publication and
runtime semantics, and adds one fail-closed compatibility boundary for immutable
historical taskbooks whose semantic sections predate today's exact heading names.

Compatibility is keyed by exact publication + taskbook path + Git blob. It may
suppress only the enumerated missing-current-heading errors after proving that
all declared legacy aliases exist with non-empty, non-placeholder payloads. No
metadata, lineage, path, blob, publication-authority, or other integrity error
can be waived.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

_BOOT_ROOT = Path(__file__).resolve().parents[1]
if str(_BOOT_ROOT) not in sys.path:
    sys.path.insert(0, str(_BOOT_ROOT))

from control_plane import research_task_records_impl as _core  # noqa: E402
from tools import research_taskbook  # noqa: E402

# Preserve the historical public API, including helper names used by tests and
# downstream runtime modules. Only audit semantics are wrapped below.
for _name in dir(_core):
    if not _name.startswith("__"):
        globals()[_name] = getattr(_core, _name)

_STRICT_AUDIT = _core.audit
ROOT = _core.ROOT
COMPATIBILITY_FILE = "research_task_record_compatibility_waivers.json"
COMPATIBILITY_SCHEMA = "ENTERPRISE_MATH_TASK_RECORD_COMPATIBILITY_WAIVERS_V1"
COMPATIBILITY_SCOPE = "MANDATORY_BODY_SECTION_HEADING_ALIAS_ONLY"
_PLACEHOLDER = re.compile(r"^\s*<[^>\n]+>\s*$", re.MULTILINE)


def _load_compatibility_waivers(root: Path = ROOT) -> list[dict[str, Any]]:
    path = root / COMPATIBILITY_FILE
    if not path.exists():
        return []
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or payload.get("schema") != COMPATIBILITY_SCHEMA:
        raise _core.TaskRecordError(f"{COMPATIBILITY_FILE}: wrong schema")
    if payload.get("status") != "ACTIVE":
        raise _core.TaskRecordError(f"{COMPATIBILITY_FILE}: status must be ACTIVE")
    rows = payload.get("waivers")
    if not isinstance(rows, list):
        raise _core.TaskRecordError(f"{COMPATIBILITY_FILE}: waivers must be a list")
    seen_ids: set[str] = set()
    seen_publications: set[str] = set()
    out: list[dict[str, Any]] = []
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise _core.TaskRecordError(
                f"{COMPATIBILITY_FILE}: waiver {index} must be an object"
            )
        waiver_id = row.get("waiver_id")
        publication_id = row.get("publication_id")
        if not isinstance(waiver_id, str) or not waiver_id:
            raise _core.TaskRecordError(
                f"{COMPATIBILITY_FILE}: waiver {index} missing waiver_id"
            )
        if waiver_id in seen_ids:
            raise _core.TaskRecordError(
                f"{COMPATIBILITY_FILE}: duplicate waiver_id {waiver_id}"
            )
        if not isinstance(publication_id, str) or not publication_id:
            raise _core.TaskRecordError(
                f"{COMPATIBILITY_FILE}: {waiver_id} missing publication_id"
            )
        if publication_id in seen_publications:
            raise _core.TaskRecordError(
                f"{COMPATIBILITY_FILE}: duplicate publication waiver {publication_id}"
            )
        if row.get("scope") != COMPATIBILITY_SCOPE:
            raise _core.TaskRecordError(
                f"{COMPATIBILITY_FILE}: {waiver_id} has unsupported scope"
            )
        if row.get("operational") is not False or row.get("history_preserved") is not True:
            raise _core.TaskRecordError(
                f"{COMPATIBILITY_FILE}: {waiver_id} must be nonoperational retained history"
            )
        for flag in (
            "working_truth_granted",
            "foundation_authority_granted",
            "canonical_promotion_granted",
            "successor_triggered",
        ):
            if row.get(flag) is not False:
                raise _core.TaskRecordError(
                    f"{COMPATIBILITY_FILE}: {waiver_id} cannot grant {flag}"
                )
        aliases = row.get("legacy_section_aliases")
        if not isinstance(aliases, dict) or not aliases:
            raise _core.TaskRecordError(
                f"{COMPATIBILITY_FILE}: {waiver_id} missing legacy_section_aliases"
            )
        if any(
            not isinstance(current, str)
            or current not in _core.MANDATORY_BODY_SECTIONS
            or not isinstance(legacy, str)
            or not legacy.strip()
            for current, legacy in aliases.items()
        ):
            raise _core.TaskRecordError(
                f"{COMPATIBILITY_FILE}: {waiver_id} has invalid alias mapping"
            )
        seen_ids.add(waiver_id)
        seen_publications.add(publication_id)
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


def _compatibility_suppressions(root: Path = ROOT) -> tuple[set[str], list[str]]:
    suppressions: set[str] = set()
    errors: list[str] = []
    try:
        waivers = _load_compatibility_waivers(root)
        records = _core.iter_records(root)
        resolutions = _core.publication_resolutions(root)
        current = _core.current_records(root)
    except Exception as exc:
        return set(), [str(exc)]

    by_publication = {
        str(item.get("publication_id")): item
        for item in records
        if isinstance(item.get("publication_id"), str)
    }
    for row in waivers:
        waiver_id = str(row["waiver_id"])
        publication_id = str(row["publication_id"])
        record = by_publication.get(publication_id)
        if record is None:
            errors.append(
                f"{COMPATIBILITY_FILE}: {waiver_id}: unknown publication_id {publication_id}"
            )
            continue

        task_id = row.get("task_id")
        taskbook_path = row.get("taskbook_path")
        taskbook_blob_sha1 = row.get("taskbook_blob_sha1")
        if record.get("task_id") != task_id:
            errors.append(f"{COMPATIBILITY_FILE}: {waiver_id}: task_id mismatch")
            continue
        if record.get("taskbook_path") != taskbook_path:
            errors.append(f"{COMPATIBILITY_FILE}: {waiver_id}: taskbook_path mismatch")
            continue
        if record.get("taskbook_blob_sha1") != taskbook_blob_sha1:
            errors.append(f"{COMPATIBILITY_FILE}: {waiver_id}: taskbook blob pin mismatch")
            continue
        if not isinstance(taskbook_path, str) or not isinstance(taskbook_blob_sha1, str):
            errors.append(f"{COMPATIBILITY_FILE}: {waiver_id}: invalid taskbook pin")
            continue

        resolution = resolutions.get(str(task_id))
        current_record = current.get(str(task_id))
        if resolution is None:
            errors.append(
                f"{COMPATIBILITY_FILE}: {waiver_id}: historical waiver requires explicit publication resolution"
            )
            continue
        if publication_id not in set(resolution.get("quarantined_publication_ids", [])):
            errors.append(
                f"{COMPATIBILITY_FILE}: {waiver_id}: publication is not a retained nonoperational head"
            )
            continue
        if current_record is None or current_record.get("publication_id") == publication_id:
            errors.append(
                f"{COMPATIBILITY_FILE}: {waiver_id}: waiver cannot target the operational publication"
            )
            continue

        path = root / taskbook_path
        if not path.exists():
            errors.append(f"{COMPATIBILITY_FILE}: {waiver_id}: taskbook path missing")
            continue
        actual_blob = _core.taskbook_blob(path)
        if actual_blob != taskbook_blob_sha1:
            errors.append(f"{COMPATIBILITY_FILE}: {waiver_id}: pinned taskbook blob drift")
            continue
        try:
            meta, body = research_taskbook.split_taskbook(path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(
                f"{COMPATIBILITY_FILE}: {waiver_id}: taskbook parse failed: {exc}"
            )
            continue
        if meta.get("task_id") != task_id:
            errors.append(f"{COMPATIBILITY_FILE}: {waiver_id}: taskbook task_id mismatch")
            continue

        aliases = dict(row["legacy_section_aliases"])
        raw_body_errors = _core.validate_body(body)
        expected_body_errors = {
            f"mandatory body section is missing or empty: {current_name}"
            for current_name in aliases
        }
        if set(raw_body_errors) != expected_body_errors:
            errors.append(
                f"{COMPATIBILITY_FILE}: {waiver_id}: waiver scope does not exactly equal current body-policy errors; "
                f"expected={sorted(expected_body_errors)!r} actual={sorted(raw_body_errors)!r}"
            )
            continue

        payloads = _heading_payloads(body)
        alias_error = False
        for current_name, legacy_name in aliases.items():
            payload = payloads.get(legacy_name, "")
            if not payload:
                errors.append(
                    f"{COMPATIBILITY_FILE}: {waiver_id}: legacy heading {legacy_name!r} "
                    f"for {current_name!r} is missing or empty"
                )
                alias_error = True
            elif _PLACEHOLDER.search(payload):
                errors.append(
                    f"{COMPATIBILITY_FILE}: {waiver_id}: legacy heading {legacy_name!r} contains placeholder text"
                )
                alias_error = True
        if alias_error:
            continue

        prefix = record.get("_record_path", "<record>")
        suppressions.update(
            f"{prefix}: {message}" for message in expected_body_errors
        )
    return suppressions, errors


def audit(root: Path = ROOT) -> list[str]:
    """Run strict V2 audit, then apply only exact immutable-history aliases."""
    raw_errors = _STRICT_AUDIT(root)
    suppressions, compatibility_errors = _compatibility_suppressions(root)
    raw_set = set(raw_errors)
    errors = list(compatibility_errors)
    errors.extend(
        f"{COMPATIBILITY_FILE}: stale or unused suppression: {item}"
        for item in sorted(suppressions - raw_set)
    )
    errors.extend(item for item in raw_errors if item not in suppressions)
    return errors


# Core commands resolve their global ``audit`` at call time, so publication and
# CLI paths automatically consume the same compatibility boundary as imports.
_core.audit = audit


def main() -> int:
    return _core.main()


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except _core.TaskRecordError as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
