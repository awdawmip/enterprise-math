#!/usr/bin/env python3
"""Audit exact immutable provenance of published taskbooks after V1 retirement.

The V1 mirror and writer were physically retired by the approved control-plane
migration. This check retains exact taskbook provenance, template integrity and
the canonical strict record/error boundary. Provenance grants no operational
selection: terminal history and blocked parallel publications remain history.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from control_plane import research_control_bootstrap as bootstrap  # noqa: E402
from control_plane import research_publication_fault_isolation as fork  # noqa: E402
from control_plane import research_task_integrity_fault_isolation as integrity  # noqa: E402
from control_plane import research_task_record_audit_fault_isolation as record_audit  # noqa: E402
from control_plane import research_task_records_impl as core  # noqa: E402
from tools import research_taskbook  # noqa: E402

ORPHAN_SUFFIX = (
    "published taskbook has no exact immutable V2/retained publication "
    "or validated nonoperational audit-only provenance"
)

# Exact legacy-source handover objects already named ALREADY_CURRENT_V2 in the
# approved ce629e24 physical-migration manifest. These pins preserve two objects;
# they are not a transaction-name whitelist or a new operational selection.
LEGACY_HANDOVERS = (
    (
        "RS-DIAGONAL-GAUGE-REFOUNDATION-INDEPENDENT-REVIEW",
        "TP-0DE08FED8E3F3C9B",
        "research_task_records/RS-DIAGONAL-GAUGE-REFOUNDATION-INDEPENDENT-REVIEW/TP-0DE08FED8E3F3C9B.json",
        "sha1:ebf870c747b4bd74a7211e39d099e53109118a0b",
        "research_tasks/DIAGONAL_GAUGE_REFOUNDATION_INDEPENDENT_REVIEW_20260825.md",
        "sha1:10497cb4c43187ac1fc76bf22c3667407c2a9782",
    ),
    (
        "RS-QUADRATIC-PACKET-HIGHER-JET-AUTOMORPHISM-NO-SECTION-INDEPENDENT-AUDIT",
        "TP-FECD22B637D89CFD",
        "research_task_records/RS-QUADRATIC-PACKET-HIGHER-JET-AUTOMORPHISM-NO-SECTION-INDEPENDENT-AUDIT/TP-FECD22B637D89CFD.json",
        "sha1:3a7d38967a6d07b111b905c8c7f9a04395754f1d",
        "research_tasks/QUADRATIC_PACKET_HIGHER_JET_AUTOMORPHISM_NO_SECTION_INDEPENDENT_AUDIT_20260825.md",
        "sha1:2d5fe1867191d05e905be5b719cc225a6fe312cd",
    ),
)


def has_exact_v2_publication_authority(
    path: Path,
    meta: dict[str, Any],
    records: list[dict[str, Any]],
    retained_parallel_ids: set[str],
    *,
    root: Path = ROOT,
) -> bool:
    """Match original path/task/blob/state/transaction provenance conditions.

    The caller must validate records and retained authority before using this
    predicate as an audit verdict. A match is not a current-head selection.
    """
    task_id = meta.get("task_id")
    if not isinstance(task_id, str) or not task_id:
        return False
    expected_path = path.relative_to(root).as_posix()
    expected_blob = core.taskbook_blob(path)
    standard_states = {"ACTIVE"} | core.TERMINAL_RECORD_STATES
    for record in records:
        if not isinstance(record, dict):
            continue
        publication_id = record.get("publication_id")
        retained = isinstance(publication_id, str) and publication_id in retained_parallel_ids
        if record.get("record_schema") != core.RECORD_SCHEMA:
            continue
        if record.get("task_id") != task_id or record.get("taskbook_path") != expected_path:
            continue
        if record.get("taskbook_blob_sha1") != expected_blob:
            continue
        if record.get("record_state", "ACTIVE") not in standard_states and not retained:
            continue
        if record.get("publication_transaction") != core.PUBLICATION_TRANSACTION_V2 and not retained:
            continue
        return True
    return False


def _validated_retained_ids(root: Path) -> set[str]:
    import research_operational_publications as operational

    retained: set[str] = set()
    # Only explicit resolutions may admit the historical nonstandard state or
    # transaction branch. The canonical selector validates synthesis/head sets;
    # a quarantined task yielding None cannot provide retained authority.
    for task_id in operational.resolution_map(root):
        selection = operational.selection(task_id, root)
        if selection is None:
            raise ValueError(f"{task_id}: resolution has no valid operational selection")
        retained.update(selection["retained_parallel_publication_ids"])
    return retained


def _legacy_handover_keys(root: Path) -> set[tuple[str, str, str]]:
    path = root / "control_plane/legacy_control_migration_manifest.json"
    if not path.is_file():
        return set()
    manifest = json.loads(path.read_text(encoding="utf-8"))
    source = manifest.get("source", {})
    if (
        manifest.get("schema") != "ENTERPRISE_MATH_LEGACY_CONTROL_MIGRATION_MANIFEST_V1"
        or manifest.get("status") != "COMPLETE"
        or source.get("commit") != "ce629e24e5af59128e25af87075c6622413684e0"
        or source.get("archive_branch") != "archive/legacy-control-plane-pre-v2-20260902"
    ):
        raise ValueError("legacy handover manifest source/schema/status drift")
    keys: set[tuple[str, str, str]] = set()
    for task_id, publication_id, record_path, record_pin, book_path, book_pin in LEGACY_HANDOVERS:
        matches = [row for row in manifest.get("tasks", []) if row.get("task_id") == task_id]
        expected = {
            "task_id": task_id, "disposition": "ALREADY_CURRENT_V2",
            "publication_id": publication_id, "record_path": record_path,
        }
        if matches != [expected]:
            raise ValueError(f"{task_id}: exact legacy handover manifest row drift")
        raw = (root / record_path).read_bytes()
        if core.git_blob_sha1_bytes(raw) != record_pin:
            raise ValueError(f"{task_id}: legacy handover record blob drift")
        record = json.loads(raw)
        if (
            record.get("record_schema") != core.RECORD_SCHEMA
            or record.get("task_id") != task_id
            or record.get("publication_id") != publication_id
            or record.get("taskbook_path") != book_path
            or record.get("taskbook_blob_sha1") != book_pin
            or record.get("record_state", "ACTIVE") not in {"ACTIVE"} | core.TERMINAL_RECORD_STATES
            or core.taskbook_blob(root / book_path) != book_pin
        ):
            raise ValueError(f"{task_id}: exact legacy handover publication/book binding drift")
        keys.add((task_id, book_path, book_pin))
    return keys


def _blocked_fork_keys(root: Path, records: list[dict[str, Any]]) -> set[tuple[str, str, str]]:
    rows = fork.validated_quarantines(root)
    keys: set[tuple[str, str, str]] = set()
    for record in records:
        row = rows.get(record.get("task_id"))
        if row is None or row["state"] != fork.QUARANTINE_STATE:
            continue
        if record.get("publication_id") not in row["publication_ids"]:
            continue
        if record.get("record_schema") != core.RECORD_SCHEMA:
            continue
        if record.get("record_state", "ACTIVE") not in {"ACTIVE"} | core.TERMINAL_RECORD_STATES:
            continue
        book_path = record.get("taskbook_path")
        if not isinstance(book_path, str) or not book_path:
            continue
        actual_pin = core.taskbook_blob(root / book_path)
        if record.get("taskbook_blob_sha1") == actual_pin:
            keys.add((record["task_id"], book_path, actual_pin))
    return keys


def _provenance_errors(
    root: Path,
    records: list[dict[str, Any]],
    retained: set[str],
    validated_audit_rows: list[dict[str, Any]],
    historical_keys: set[tuple[str, str, str]] | None = None,
) -> list[str]:
    errors: list[str] = []
    audit_keys = {
        (row["task_id"], row["taskbook_path"], row["taskbook_blob_sha1"])
        for row in validated_audit_rows
    }
    for path in sorted((root / "research_tasks").glob("*.md")):
        try:
            meta, _ = research_taskbook.split_taskbook(path.read_text(encoding="utf-8"))
        except (ValueError, UnicodeError):
            # Preserve the original parsed published-taskbook domain. Strict
            # record audit independently rejects malformed registered sources.
            continue
        if not isinstance(meta, dict):
            continue
        if meta.get("task_authority") != "PUBLISHED_REGISTERED":
            continue
        if meta.get("base_state") in {"DRAFT", "BACKLOG"}:
            continue
        relative = path.relative_to(root).as_posix()
        key = (meta.get("task_id"), relative, core.taskbook_blob(path))
        if has_exact_v2_publication_authority(path, meta, records, retained, root=root):
            continue
        if key in audit_keys or key in (historical_keys or set()):
            continue
        errors.append(f"{relative}: {ORPHAN_SUFFIX}")
    return errors


def audit(root: Path = ROOT) -> list[str]:
    try:
        bootstrap.install(root)
        # validated_rows alone does not establish that its declared errors are
        # present. Apply the actual strict error comparison before using any row.
        errors = record_audit.audit_against(integrity.audit_task_records(root), root)
        if errors:
            return errors
        rows = record_audit.validated_rows(root)
        records = core.iter_records(root)
        retained = _validated_retained_ids(root)
        historical = _legacy_handover_keys(root) | _blocked_fork_keys(root, records)
        errors = _provenance_errors(root, records, retained, rows, historical)
        template = root / "templates/RESEARCH_TASK_PUBLICATION_TEMPLATE.json"
        if not template.is_file():
            errors.append("mandatory unified publication template missing")
        elif json.loads(template.read_text(encoding="utf-8")).get("schema") != core.TASKBOOK_TEMPLATE:
            errors.append("publication template schema drift")
        return errors
    except Exception as exc:
        return [f"cannot validate exact taskbook publication provenance: {exc}"]


def main() -> int:
    errors = audit(ROOT)
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print("PASS: published taskbooks have exact immutable publication provenance; no runtime authority granted.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
