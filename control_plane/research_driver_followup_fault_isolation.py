#!/usr/bin/env python3
"""Exact isolation for automatic follow-up derived from nonoperational reviews.

A follow-up packet cannot retain operational control authority after its source
Driver review has been removed from the operational review view. This layer keeps
the immutable packet/publication bytes in place, filters the exact packet from the
runtime packet view, and locally blocks the exact solely-derived task publication.
No task content or review disposition is changed.
"""
from __future__ import annotations

import copy
import hashlib
import json
from collections import defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
QUARANTINE_FILE = "research_driver_followup_authority_quarantines.json"
QUARANTINE_SCHEMA = "ENTERPRISE_MATH_DRIVER_FOLLOWUP_AUTHORITY_QUARANTINE_V1"
QUARANTINE_STATE = "NONOPERATIONAL_SOURCE_REVIEW"
_AUTHORITY_FLAGS = (
    "working_truth_granted",
    "foundation_authority_granted",
    "canonical_promotion_granted",
    "successor_triggered",
)


class DriverFollowupIsolationError(ValueError):
    pass


def _load(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise DriverFollowupIsolationError(f"{path}: cannot load JSON: {exc}") from exc
    if not isinstance(value, dict):
        raise DriverFollowupIsolationError(f"{path}: JSON root must be object")
    return value


def _git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return "sha1:" + hashlib.sha1(header + data).hexdigest()


def quarantine_rows(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    path = root / QUARANTINE_FILE
    if not path.exists():
        return {}
    payload = _load(path)
    if payload.get("schema") != QUARANTINE_SCHEMA:
        raise DriverFollowupIsolationError(f"{QUARANTINE_FILE}: wrong schema")
    if payload.get("status") != "ACTIVE":
        raise DriverFollowupIsolationError(f"{QUARANTINE_FILE}: status must be ACTIVE")
    rows = payload.get("entries")
    if not isinstance(rows, list):
        raise DriverFollowupIsolationError(f"{QUARANTINE_FILE}: entries must be list")
    out: dict[str, dict[str, Any]] = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise DriverFollowupIsolationError(
                f"{QUARANTINE_FILE}: entry {index} must be object"
            )
        packet_id = row.get("packet_id")
        if not isinstance(packet_id, str) or not packet_id:
            raise DriverFollowupIsolationError(
                f"{QUARANTINE_FILE}: entry {index} missing packet_id"
            )
        if packet_id in out:
            raise DriverFollowupIsolationError(
                f"{QUARANTINE_FILE}: duplicate packet_id {packet_id}"
            )
        for field in ("review_id", "result_id", "packet_path", "packet_blob_sha1"):
            if not isinstance(row.get(field), str) or not row[field]:
                raise DriverFollowupIsolationError(
                    f"{QUARANTINE_FILE}: {packet_id} missing {field}"
                )
        if row.get("state") != QUARANTINE_STATE:
            raise DriverFollowupIsolationError(
                f"{QUARANTINE_FILE}: {packet_id} wrong state"
            )
        if row.get("operational") is not False or row.get("history_preserved") is not True:
            raise DriverFollowupIsolationError(
                f"{QUARANTINE_FILE}: {packet_id} must be nonoperational preserved history"
            )
        expected_error = row.get("expected_post_review_isolation_error")
        if not isinstance(expected_error, str) or not expected_error:
            raise DriverFollowupIsolationError(
                f"{QUARANTINE_FILE}: {packet_id} missing expected isolation error"
            )
        derived = row.get("derived_task_publications")
        if not isinstance(derived, list) or not derived:
            raise DriverFollowupIsolationError(
                f"{QUARANTINE_FILE}: {packet_id} derived_task_publications must be nonempty"
            )
        seen_publications: set[str] = set()
        for j, task in enumerate(derived):
            if not isinstance(task, dict):
                raise DriverFollowupIsolationError(
                    f"{QUARANTINE_FILE}: {packet_id} derived row {j} must be object"
                )
            for field in (
                "task_id",
                "publication_id",
                "publication_record_path",
                "publication_record_blob_sha1",
                "taskbook_path",
                "taskbook_blob_sha1",
            ):
                if not isinstance(task.get(field), str) or not task[field]:
                    raise DriverFollowupIsolationError(
                        f"{QUARANTINE_FILE}: {packet_id} derived row {j} missing {field}"
                    )
            publication_id = task["publication_id"]
            if publication_id in seen_publications:
                raise DriverFollowupIsolationError(
                    f"{QUARANTINE_FILE}: {packet_id} duplicate derived publication {publication_id}"
                )
            seen_publications.add(publication_id)
        reason = row.get("reason")
        if not isinstance(reason, str) or not reason.strip():
            raise DriverFollowupIsolationError(
                f"{QUARANTINE_FILE}: {packet_id} reason is required"
            )
        for flag in _AUTHORITY_FLAGS:
            if row.get(flag) is not False:
                raise DriverFollowupIsolationError(
                    f"{QUARANTINE_FILE}: {packet_id} cannot grant {flag}"
                )
        out[packet_id] = row
    return out


def _active_publication_heads(root: Path) -> dict[str, set[str]]:
    from tools import research_task_records

    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in research_task_records.iter_records(root):
        task_id = record.get("task_id")
        if isinstance(task_id, str) and task_id:
            grouped[task_id].append(record)
    out: dict[str, set[str]] = {}
    terminal = set(research_task_records.TERMINAL_RECORD_STATES)
    for task_id, records in grouped.items():
        superseded = {
            item.get("supersedes_publication_id")
            for item in records
            if isinstance(item.get("supersedes_publication_id"), str)
            and item.get("supersedes_publication_id")
        }
        out[task_id] = {
            str(item.get("publication_id"))
            for item in records
            if item.get("publication_id") not in superseded
            and item.get("record_state", "ACTIVE") not in terminal
            and isinstance(item.get("publication_id"), str)
        }
    return out


def validated_quarantines(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    from control_plane import research_driver_review_authority_fault_isolation as review_isolation

    rows = quarantine_rows(root)
    review_rows = review_isolation.validated_quarantines(root)
    active_heads = _active_publication_heads(root)
    seen_task_ids: set[str] = set()

    for packet_id, row in rows.items():
        review_id = row["review_id"]
        review_row = review_rows.get(review_id)
        if review_row is None:
            raise DriverFollowupIsolationError(
                f"{QUARANTINE_FILE}: {packet_id} source review is not review-authority quarantined"
            )
        if review_row["result_id"] != row["result_id"]:
            raise DriverFollowupIsolationError(
                f"{QUARANTINE_FILE}: {packet_id} result_id differs from source-review quarantine"
            )
        packet_path = root / row["packet_path"]
        if not packet_path.exists():
            raise DriverFollowupIsolationError(
                f"{QUARANTINE_FILE}: {packet_id} packet path missing"
            )
        actual_packet_blob = _git_blob_sha1(packet_path.read_bytes())
        if actual_packet_blob != row["packet_blob_sha1"]:
            raise DriverFollowupIsolationError(
                f"{QUARANTINE_FILE}: {packet_id} packet blob drift; "
                f"declared={row['packet_blob_sha1']} actual={actual_packet_blob}"
            )
        packet = _load(packet_path)
        for field in ("packet_id", "review_id", "result_id"):
            if packet.get(field) != row[field]:
                raise DriverFollowupIsolationError(
                    f"{QUARANTINE_FILE}: {packet_id} packet {field} mismatch"
                )
        packet_publications = {
            str(item.get("publication_id"))
            for item in packet.get("task_publications", [])
            if isinstance(item, dict) and isinstance(item.get("publication_id"), str)
        }
        declared_publications = {
            item["publication_id"] for item in row["derived_task_publications"]
        }
        if packet_publications != declared_publications:
            raise DriverFollowupIsolationError(
                f"{QUARANTINE_FILE}: {packet_id} derived publication set drift; "
                f"packet={sorted(packet_publications)!r} declared={sorted(declared_publications)!r}"
            )

        for task in row["derived_task_publications"]:
            task_id = task["task_id"]
            publication_id = task["publication_id"]
            if task_id in seen_task_ids:
                raise DriverFollowupIsolationError(
                    f"{QUARANTINE_FILE}: duplicate derived task quarantine {task_id}"
                )
            seen_task_ids.add(task_id)
            if active_heads.get(task_id, set()) != {publication_id}:
                raise DriverFollowupIsolationError(
                    f"{QUARANTINE_FILE}: {task_id} derived quarantine requires exactly the pinned active head; "
                    f"expected={[publication_id]!r} actual={sorted(active_heads.get(task_id, set()))!r}"
                )
            record_path = root / task["publication_record_path"]
            if not record_path.exists():
                raise DriverFollowupIsolationError(
                    f"{QUARANTINE_FILE}: {publication_id} publication record missing"
                )
            if _git_blob_sha1(record_path.read_bytes()) != task["publication_record_blob_sha1"]:
                raise DriverFollowupIsolationError(
                    f"{QUARANTINE_FILE}: {publication_id} publication record blob drift"
                )
            record = _load(record_path)
            if record.get("task_id") != task_id or record.get("publication_id") != publication_id:
                raise DriverFollowupIsolationError(
                    f"{QUARANTINE_FILE}: {publication_id} publication identity mismatch"
                )
            if record.get("taskbook_path") != task["taskbook_path"]:
                raise DriverFollowupIsolationError(
                    f"{QUARANTINE_FILE}: {publication_id} taskbook_path mismatch"
                )
            taskbook_path = root / task["taskbook_path"]
            if not taskbook_path.exists():
                raise DriverFollowupIsolationError(
                    f"{QUARANTINE_FILE}: {publication_id} taskbook missing"
                )
            if _git_blob_sha1(taskbook_path.read_bytes()) != task["taskbook_blob_sha1"]:
                raise DriverFollowupIsolationError(
                    f"{QUARANTINE_FILE}: {publication_id} taskbook blob drift"
                )
    return rows


def derived_task_rows(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for packet_id, row in validated_quarantines(root).items():
        for task in row["derived_task_publications"]:
            value = dict(task)
            value["source_packet_id"] = packet_id
            value["source_review_id"] = row["review_id"]
            out[task["task_id"]] = value
    return out


def operational_packets(
    packets: list[dict[str, Any]], root: Path = ROOT
) -> list[dict[str, Any]]:
    rows = validated_quarantines(root)
    if not rows:
        return packets
    available = {
        str(item.get("packet_id"))
        for item in packets
        if isinstance(item.get("packet_id"), str)
    }
    missing = sorted(set(rows) - available)
    if missing:
        raise DriverFollowupIsolationError(
            f"{QUARANTINE_FILE}: quarantined packet(s) absent from pre-isolation view: {missing}"
        )
    return [item for item in packets if item.get("packet_id") not in rows]


def _blocked_definition(task_id: str, task: dict[str, Any], prior: dict[str, Any] | None) -> dict[str, Any]:
    value = copy.deepcopy(prior or {})
    value.update(
        {
            "task_id": task_id,
            "title": value.get("title", task_id),
            "kind": value.get("kind", "RESEARCH"),
            "owner": "control-plane/review-followup-authority-quarantine",
            "base_state": "BLOCKED",
            "priority": value.get("priority", "P2"),
            "leverage": value.get("leverage", "MEDIUM"),
            "frontier": "NONOPERATIONAL_SOURCE_REVIEW_FOLLOWUP",
            "next_action": "AWAIT_AUTHORIZED_SOURCE_REVIEW_BEFORE_DERIVED_TASK_REACTIVATION",
            "dependencies": copy.deepcopy(value.get("dependencies", [])),
            "source_refs": sorted(
                set(value.get("source_refs", []))
                | {
                    task["source_packet_id"],
                    task["source_review_id"],
                    task["publication_id"],
                    task["publication_record_path"],
                }
            ),
            "evidence_status": "CONTROL_PLANE_QUARANTINED_REVIEW_DERIVED_PUBLICATION",
            "last_progress_ref": QUARANTINE_FILE,
            "last_progress_at": value.get("last_progress_at", "1970-01-01T00:00:00+00:00"),
            "hard_block": {
                "code": "NONOPERATIONAL_SOURCE_REVIEW_FOLLOWUP",
                "source_review_id": task["source_review_id"],
                "source_packet_id": task["source_packet_id"],
                "publication_id": task["publication_id"],
                "missing_object": "one source-backed operational Driver review authorizing this follow-up chain",
                "owner": "control-plane/driver-review-authority-repair",
                "necessity": "A task derived solely from a nonoperational review cannot remain claimable independently of that source review.",
                "unblock_condition": "Create an ordinary source-backed replacement Driver review and a valid follow-up authority chain, then retire this exact quarantine.",
            },
            "tags": sorted(set(value.get("tags", [])) | {"CONTROL_PLANE_REVIEW_DERIVATION_QUARANTINE"}),
            "claim_lease_minutes": int(value.get("claim_lease_minutes") or 120),
            "publication_id": None,
            "publication_ids": [task["publication_id"]],
            "registration_source": "DRIVER_FOLLOWUP_AUTHORITY_QUARANTINE",
        }
    )
    return value


def install(root: Path = ROOT) -> None:
    """Filter exact packets and locally block their exact solely-derived task heads."""
    rows = validated_quarantines(root)
    derived = derived_task_rows(root)

    import research_driver_followup as followup
    from control_plane import research_task_records_impl as task_core
    from tools import research_dispatch, research_task_records

    if not getattr(followup, "_followup_authority_isolation_installed", False):
        base_iter_packets = followup.iter_packets

        def iter_packets(local_root: Path = followup.ROOT) -> list[dict[str, Any]]:
            return operational_packets(base_iter_packets(local_root), local_root)

        followup.iter_packets = iter_packets
        followup._followup_authority_isolation_installed = True

    if not getattr(task_core, "_followup_authority_isolation_installed", False):
        base_current = research_task_records.current_records

        def current_records(local_root: Path = root) -> dict[str, dict[str, Any]]:
            current = dict(base_current(local_root))
            for task_id in derived_task_rows(local_root):
                current.pop(task_id, None)
            return current

        research_task_records.current_records = current_records
        task_core.current_records = current_records
        task_core._followup_authority_isolation_installed = True

    if not getattr(research_dispatch, "_followup_authority_isolation_installed", False):
        base_merged = research_dispatch.merged_definitions

        def merged_definitions(local_root: Path = research_dispatch.ROOT) -> list[dict[str, Any]]:
            values = base_merged(local_root)
            by_id = {
                item["task_id"]: item
                for item in values
                if isinstance(item, dict) and isinstance(item.get("task_id"), str)
            }
            for task_id, task in derived_task_rows(local_root).items():
                by_id[task_id] = _blocked_definition(task_id, task, by_id.get(task_id))
            return [by_id[key] for key in sorted(by_id)]

        research_dispatch.merged_definitions = merged_definitions
        research_dispatch._followup_authority_isolation_installed = True

    if not rows and derived:
        raise DriverFollowupIsolationError("derived task quarantine exists without packet quarantine")


def audit(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    try:
        from control_plane import research_driver_review_authority_fault_isolation as review_isolation

        review_isolation.install(root)
        rows = validated_quarantines(root)
        install(root)

        import research_driver_followup as followup
        from tools import research_dispatch, research_task_records

        packet_ids = {
            str(item.get("packet_id"))
            for item in followup.iter_packets(root)
            if isinstance(item.get("packet_id"), str)
        }
        leaked_packets = sorted(set(rows) & packet_ids)
        if leaked_packets:
            errors.append(
                f"{QUARANTINE_FILE}: quarantined packets remain operational: {leaked_packets}"
            )

        current = research_task_records.current_records(root)
        definitions = {
            item["task_id"]: item for item in research_dispatch.merged_definitions(root)
        }
        for task_id, task in derived_task_rows(root).items():
            if task_id in current:
                errors.append(f"{task_id}: review-derived quarantined task remains current")
            definition = definitions.get(task_id)
            if definition is None:
                errors.append(f"{task_id}: review-derived quarantine missing from dispatch view")
                continue
            if definition.get("base_state") != "BLOCKED":
                errors.append(f"{task_id}: review-derived quarantine is not BLOCKED")
            if definition.get("publication_id") is not None:
                errors.append(f"{task_id}: review-derived quarantine selected a publication")
    except Exception as exc:
        errors.append(str(exc))
    return errors


def main() -> int:
    errors = audit()
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print(
        "PASS: follow-up authority derived from nonoperational reviews is locally isolated "
        f"({len(quarantine_rows())} packet(s))."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
