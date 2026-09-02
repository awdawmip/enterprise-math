#!/usr/bin/env python3
"""Public immutable task-publication facade with exact compatibility.

The strict V2 implementation lives in ``control_plane.research_task_records_impl``.
This facade preserves current publication/runtime semantics and adds two
fail-closed adapters for taskbooks written before today's exact section names:

* historical one-heading aliases, valid only for nonoperational publications;
* exact multi-source adapters for a finite set of byte-pinned pre-canonical
  publications whose required semantics live under several older headings
  and/or the immutable record's ``research_value`` field.

Neither adapter can waive metadata, lineage, path, Git-blob, parse,
publication-authority, placeholder, or any non-section integrity failure.
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

# Pin the byte-identical implementation audit once. The facade can be imported
# both as tools.research_task_records and as bare research_task_records by
# historical CLI entrypoints; neither path may wrap an already-wrapped audit.
if "_immutable_history_original_audit" not in _core.__dict__:
    _core.__dict__["_immutable_history_original_audit"] = _core.audit
_STRICT_AUDIT = _core.__dict__["_immutable_history_original_audit"]

ROOT = _core.ROOT
COMPATIBILITY_FILE = "research_task_record_compatibility_waivers.json"
COMPATIBILITY_SCHEMA = "ENTERPRISE_MATH_TASK_RECORD_COMPATIBILITY_WAIVERS_V1"
COMPATIBILITY_SCOPE = "MANDATORY_BODY_SECTION_HEADING_ALIAS_ONLY"
SOURCE_ADAPTER_FILE = "research_task_record_exact_source_adapters.json"
SOURCE_ADAPTER_SCHEMA = "ENTERPRISE_MATH_TASK_RECORD_EXACT_SOURCE_ADAPTERS_V1"
SOURCE_ADAPTER_SCOPE = "PRE_CANONICAL_MANDATORY_SECTION_EXACT_SOURCE_ADAPTER"
SOURCE_ADAPTER_CLASS = "EXACT_PRE_CANONICAL_SECTION_SOURCE_ADAPTER"
_ALLOWED_RECORD_FIELDS = {"research_value"}
_AUTHORITY_FLAGS = (
    "working_truth_granted",
    "foundation_authority_granted",
    "canonical_promotion_granted",
    "successor_triggered",
)
_PLACEHOLDER = re.compile(r"^\s*<[^>\n]+>\s*$", re.MULTILINE)


def _check_authority_flags(row: dict[str, Any], source: str, row_id: str) -> None:
    for flag in _AUTHORITY_FLAGS:
        if row.get(flag) is not False:
            raise _core.TaskRecordError(f"{source}: {row_id} cannot grant {flag}")


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
        _check_authority_flags(row, COMPATIBILITY_FILE, waiver_id)
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


def _load_exact_source_adapters(root: Path = ROOT) -> list[dict[str, Any]]:
    path = root / SOURCE_ADAPTER_FILE
    if not path.exists():
        return []
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or payload.get("schema") != SOURCE_ADAPTER_SCHEMA:
        raise _core.TaskRecordError(f"{SOURCE_ADAPTER_FILE}: wrong schema")
    if payload.get("status") != "ACTIVE":
        raise _core.TaskRecordError(f"{SOURCE_ADAPTER_FILE}: status must be ACTIVE")
    rows = payload.get("adapters")
    if not isinstance(rows, list):
        raise _core.TaskRecordError(f"{SOURCE_ADAPTER_FILE}: adapters must be a list")
    seen_ids: set[str] = set()
    seen_publications: set[str] = set()
    out: list[dict[str, Any]] = []
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise _core.TaskRecordError(
                f"{SOURCE_ADAPTER_FILE}: adapter {index} must be an object"
            )
        adapter_id = row.get("adapter_id")
        publication_id = row.get("publication_id")
        if not isinstance(adapter_id, str) or not adapter_id:
            raise _core.TaskRecordError(
                f"{SOURCE_ADAPTER_FILE}: adapter {index} missing adapter_id"
            )
        if adapter_id in seen_ids:
            raise _core.TaskRecordError(
                f"{SOURCE_ADAPTER_FILE}: duplicate adapter_id {adapter_id}"
            )
        if not isinstance(publication_id, str) or not publication_id:
            raise _core.TaskRecordError(
                f"{SOURCE_ADAPTER_FILE}: {adapter_id} missing publication_id"
            )
        if publication_id in seen_publications:
            raise _core.TaskRecordError(
                f"{SOURCE_ADAPTER_FILE}: duplicate publication adapter {publication_id}"
            )
        if row.get("scope") != SOURCE_ADAPTER_SCOPE:
            raise _core.TaskRecordError(
                f"{SOURCE_ADAPTER_FILE}: {adapter_id} has unsupported scope"
            )
        if row.get("compatibility_class") != SOURCE_ADAPTER_CLASS:
            raise _core.TaskRecordError(
                f"{SOURCE_ADAPTER_FILE}: {adapter_id} has unsupported compatibility_class"
            )
        if not isinstance(row.get("operational"), bool):
            raise _core.TaskRecordError(
                f"{SOURCE_ADAPTER_FILE}: {adapter_id} operational must be boolean"
            )
        if row.get("history_preserved") is not True:
            raise _core.TaskRecordError(
                f"{SOURCE_ADAPTER_FILE}: {adapter_id} must preserve immutable history"
            )
        _check_authority_flags(row, SOURCE_ADAPTER_FILE, adapter_id)
        for field in (
            "task_id",
            "record_path",
            "taskbook_path",
            "taskbook_blob_sha1",
            "published_at",
            "reason",
        ):
            if not isinstance(row.get(field), str) or not row[field].strip():
                raise _core.TaskRecordError(
                    f"{SOURCE_ADAPTER_FILE}: {adapter_id} missing {field}"
                )
        sources = row.get("section_sources")
        if not isinstance(sources, dict) or not sources:
            raise _core.TaskRecordError(
                f"{SOURCE_ADAPTER_FILE}: {adapter_id} missing section_sources"
            )
        for current_name, spec in sources.items():
            if (
                current_name not in _core.MANDATORY_BODY_SECTIONS
                or not isinstance(spec, dict)
                or not spec
                or set(spec) - {"body_headings", "record_fields"}
            ):
                raise _core.TaskRecordError(
                    f"{SOURCE_ADAPTER_FILE}: {adapter_id} has invalid source for {current_name!r}"
                )
            headings = spec.get("body_headings", [])
            fields = spec.get("record_fields", [])
            if (
                not isinstance(headings, list)
                or not all(isinstance(item, str) and item.strip() for item in headings)
                or not isinstance(fields, list)
                or not all(isinstance(item, str) and item.strip() for item in fields)
                or (not headings and not fields)
                or set(fields) - _ALLOWED_RECORD_FIELDS
            ):
                raise _core.TaskRecordError(
                    f"{SOURCE_ADAPTER_FILE}: {adapter_id} has invalid payload source "
                    f"for {current_name!r}"
                )
        seen_ids.add(adapter_id)
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


def _direct_same_task_successors(
    records: list[dict[str, Any]], task_id: str, publication_id: str
) -> list[dict[str, Any]]:
    return [
        item
        for item in records
        if item.get("task_id") == task_id
        and item.get("supersedes_publication_id") == publication_id
        and isinstance(item.get("publication_id"), str)
        and item.get("publication_id")
    ]


def _compatibility_suppressions(root: Path = ROOT) -> tuple[set[str], list[str]]:
    suppressions: set[str] = set()
    errors: list[str] = []
    try:
        waivers = _load_compatibility_waivers(root)
        adapters = _load_exact_source_adapters(root)
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

    # Existing nonoperational single-heading compatibility.
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

        task_id_text = str(task_id)
        resolution = resolutions.get(task_id_text)
        current_record = current.get(task_id_text)
        direct_successors = _direct_same_task_successors(records, task_id_text, publication_id)
        retained_parallel = (
            resolution is not None
            and publication_id in set(resolution.get("quarantined_publication_ids", []))
        )
        directly_superseded = bool(direct_successors)
        if not retained_parallel and not directly_superseded:
            errors.append(
                f"{COMPATIBILITY_FILE}: {waiver_id}: publication is neither a retained "
                "nonoperational head nor directly superseded same-task history"
            )
            continue
        if directly_superseded:
            old_generation = record.get("publication_generation")
            if not isinstance(old_generation, int) or any(
                not isinstance(item.get("publication_generation"), int)
                or item["publication_generation"] <= old_generation
                for item in direct_successors
            ):
                errors.append(
                    f"{COMPATIBILITY_FILE}: {waiver_id}: direct successor generation "
                    "is not strictly newer"
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
                f"{COMPATIBILITY_FILE}: {waiver_id}: waiver scope does not exactly equal "
                f"current body-policy errors; expected={sorted(expected_body_errors)!r} "
                f"actual={sorted(raw_body_errors)!r}"
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
                    f"{COMPATIBILITY_FILE}: {waiver_id}: legacy heading {legacy_name!r} "
                    "contains placeholder text"
                )
                alias_error = True
        if alias_error:
            continue

        prefix = record.get("_record_path", "<record>")
        suppressions.update(f"{prefix}: {message}" for message in expected_body_errors)

    # Exact source adapters for byte-pinned pre-canonical publications.
    for row in adapters:
        adapter_id = str(row["adapter_id"])
        publication_id = str(row["publication_id"])
        record = by_publication.get(publication_id)
        if record is None:
            errors.append(
                f"{SOURCE_ADAPTER_FILE}: {adapter_id}: unknown publication_id {publication_id}"
            )
            continue

        task_id = str(row["task_id"])
        record_path = str(row["record_path"])
        taskbook_path = str(row["taskbook_path"])
        taskbook_blob = str(row["taskbook_blob_sha1"])
        pins = {
            "task_id": task_id,
            "_record_path": record_path,
            "taskbook_path": taskbook_path,
            "taskbook_blob_sha1": taskbook_blob,
            "published_at": row["published_at"],
        }
        mismatches = [
            key for key, expected in pins.items() if record.get(key) != expected
        ]
        canonical_record_path = (
            Path("research_task_records") / task_id / f"{publication_id}.json"
        ).as_posix()
        if mismatches or record_path != canonical_record_path:
            errors.append(
                f"{SOURCE_ADAPTER_FILE}: {adapter_id}: exact record pin mismatch "
                f"{mismatches or ['record_path']}"
            )
            continue

        taskbook = root / taskbook_path
        if not taskbook.exists():
            errors.append(f"{SOURCE_ADAPTER_FILE}: {adapter_id}: taskbook path missing")
            continue
        if _core.taskbook_blob(taskbook) != taskbook_blob:
            errors.append(f"{SOURCE_ADAPTER_FILE}: {adapter_id}: pinned taskbook blob drift")
            continue
        try:
            meta, body = research_taskbook.split_taskbook(
                taskbook.read_text(encoding="utf-8")
            )
        except Exception as exc:
            errors.append(
                f"{SOURCE_ADAPTER_FILE}: {adapter_id}: taskbook parse failed: {exc}"
            )
            continue
        if meta.get("task_id") != task_id:
            errors.append(f"{SOURCE_ADAPTER_FILE}: {adapter_id}: taskbook task_id mismatch")
            continue

        current_record = current.get(task_id)
        successors = _direct_same_task_successors(records, task_id, publication_id)
        resolution = resolutions.get(task_id)
        retained_parallel = (
            resolution is not None
            and publication_id in set(resolution.get("quarantined_publication_ids", []))
        )
        if row["operational"]:
            if (
                current_record is None
                or current_record.get("publication_id") != publication_id
                or successors
                or retained_parallel
                or record.get("record_state", "ACTIVE") != "ACTIVE"
                or record.get("claimable") is not True
            ):
                errors.append(
                    f"{SOURCE_ADAPTER_FILE}: {adapter_id}: operational target is not "
                    "the exact active claimable current publication"
                )
                continue
        elif (
            current_record is None
            or current_record.get("publication_id") == publication_id
            or (not successors and not retained_parallel)
        ):
            errors.append(
                f"{SOURCE_ADAPTER_FILE}: {adapter_id}: nonoperational target is not "
                "exact retained/superseded history"
            )
            continue

        sources = dict(row["section_sources"])
        raw_body_errors = _core.validate_body(body)
        expected_body_errors = {
            f"mandatory body section is missing or empty: {name}" for name in sources
        }
        if set(raw_body_errors) != expected_body_errors:
            errors.append(
                f"{SOURCE_ADAPTER_FILE}: {adapter_id}: adapter scope does not exactly equal "
                f"current body-policy errors; expected={sorted(expected_body_errors)!r} "
                f"actual={sorted(raw_body_errors)!r}"
            )
            continue

        payloads = _heading_payloads(body)
        source_error = False
        for current_name, spec in sources.items():
            for heading in spec.get("body_headings", []):
                payload = payloads.get(heading, "")
                if not payload or _PLACEHOLDER.search(payload):
                    errors.append(
                        f"{SOURCE_ADAPTER_FILE}: {adapter_id}: invalid body heading "
                        f"{heading!r} for {current_name!r}"
                    )
                    source_error = True
            for field in spec.get("record_fields", []):
                payload = record.get(field)
                if (
                    not isinstance(payload, str)
                    or not payload.strip()
                    or _PLACEHOLDER.search(payload)
                ):
                    errors.append(
                        f"{SOURCE_ADAPTER_FILE}: {adapter_id}: invalid record field "
                        f"{field!r} for {current_name!r}"
                    )
                    source_error = True
        if source_error:
            continue

        prefix = record.get("_record_path", "<record>")
        suppressions.update(f"{prefix}: {message}" for message in expected_body_errors)

    return suppressions, errors


def audit(root: Path = ROOT) -> list[str]:
    """Run strict V2 audit, then apply only exact byte-pinned compatibility."""
    raw_errors = _STRICT_AUDIT(root)
    suppressions, compatibility_errors = _compatibility_suppressions(root)
    raw_set = set(raw_errors)
    errors = list(compatibility_errors)
    errors.extend(
        f"task-record compatibility: stale or unused suppression: {item}"
        for item in sorted(suppressions - raw_set)
    )
    errors.extend(item for item in raw_errors if item not in suppressions)
    return errors


def main() -> int:
    # The strict CLI resolves its global audit function dynamically. Patch only
    # for the duration of this call so duplicate facade imports never stack.
    previous = _core.audit
    _core.audit = audit
    try:
        return _core.main()
    finally:
        _core.audit = previous


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except _core.TaskRecordError as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
