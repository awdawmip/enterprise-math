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
TASK_ISOLATION = "PACKET_AND_DERIVED_TASKS"
PACKET_ONLY = "PACKET_ONLY_NO_DERIVED_TASK_AUTHORITY"
AUTHORITY_SOURCE = "DRIVER_REVIEW_AUTHORITY"
AUDIT_SOURCE = "INVALID_REVIEW_RECORD_AUDIT"
RESULT_SOURCE = "RESULT_CONTROL_AUTHORITY"
_TASK_PINS = (
    "task_id", "publication_id", "publication_record_path",
    "publication_record_blob_sha1", "taskbook_path", "taskbook_blob_sha1",
)
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
        basis = row.get("source_review_basis", AUTHORITY_SOURCE)
        if basis not in {AUTHORITY_SOURCE, AUDIT_SOURCE, RESULT_SOURCE}:
            raise DriverFollowupIsolationError(f"{packet_id}: unsupported source review basis")
        kind = row.get("isolation_kind", TASK_ISOLATION)
        if kind not in {TASK_ISOLATION, PACKET_ONLY}:
            raise DriverFollowupIsolationError(f"{packet_id}: unsupported isolation kind")
        derived = row.get("derived_task_publications")
        if not isinstance(derived, list) or (kind == TASK_ISOLATION and not derived):
            raise DriverFollowupIsolationError(
                f"{QUARANTINE_FILE}: {packet_id} derived_task_publications must be nonempty"
            )
        if kind == PACKET_ONLY and (
            derived != [] or row.get("packet_decision") not in {
                "PARENT_CLOSED", "PARENT_OBJECTIVE_CLOSURE",
            }
        ):
            raise DriverFollowupIsolationError(f"{packet_id}: packet-only isolation requires exact empty closure task set")
        seen_publications: set[str] = set()
        seen_tasks: set[str] = set()
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
            if task["task_id"] in seen_tasks:
                raise DriverFollowupIsolationError(f"{packet_id}: duplicate derived task identity")
            seen_tasks.add(task["task_id"])
            if basis == RESULT_SOURCE and "source_packet_ids" not in task:
                raise DriverFollowupIsolationError(f"{packet_id}: Result basis requires explicit complete source set")
            if "source_packet_ids" in task:
                sources = task["source_packet_ids"]
                if (
                    not isinstance(sources, list) or not sources
                    or any(not isinstance(source, str) or not source for source in sources)
                    or len(sources) != len(set(sources)) or packet_id not in sources
                ):
                    raise DriverFollowupIsolationError(f"{packet_id}: invalid explicit source packet set")
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


def _raw_packets(root: Path) -> list[dict[str, Any]]:
    """Read source evidence before any operational packet filtering."""
    directory = root / "research_driver_followups"
    out = []
    for path in sorted(directory.glob("*/*.json")) if directory.exists() else []:
        packet = _load(path)
        packet["_path"] = path.relative_to(root).as_posix()
        out.append(packet)
    return out


def _complete_source_sets(
    rows: dict[str, dict[str, Any]], root: Path,
) -> None:
    """Prove each exact publication's entire packet source set is registered.

    Unrelated historical packet formats do not acquire new authority here. Any
    packet naming a covered review or exact derived publication is relevant,
    including a newly added source whose review is not quarantined.
    """
    groups: dict[str, list[tuple[str, dict[str, Any]]]] = defaultdict(list)
    by_review: dict[str, set[str]] = defaultdict(set)
    for packet_id, row in rows.items():
        by_review[row["review_id"]].add(packet_id)
        for task in row["derived_task_publications"]:
            groups[task["task_id"]].append((packet_id, task))
    by_publication: dict[str, str] = {}
    for task_id, values in groups.items():
        for _, task in values:
            publication_id = task["publication_id"]
            if publication_id in by_publication and by_publication[publication_id] != task_id:
                raise DriverFollowupIsolationError(f"{publication_id}: shared publication has conflicting task identities")
            by_publication[publication_id] = task_id
    actual_sources: dict[str, set[str]] = defaultdict(set)
    actual_reviews: dict[str, set[str]] = defaultdict(set)
    seen_ids: set[str] = set()
    for packet in _raw_packets(root):
        task_rows = packet.get("task_publications", [])
        mentions = [
            item for item in task_rows if isinstance(item, dict)
            and item.get("publication_id") in by_publication
        ] if isinstance(task_rows, list) else []
        review_id = packet.get("review_id")
        if review_id not in by_review and not mentions:
            continue
        packet_id = packet.get("packet_id")
        if not isinstance(packet_id, str) or not packet_id or packet_id in seen_ids:
            raise DriverFollowupIsolationError("covered source has missing or duplicate packet_id")
        seen_ids.add(packet_id)
        if packet_id in rows and packet.get("_path") != rows[packet_id]["packet_path"]:
            raise DriverFollowupIsolationError(f"{packet_id}: exact source packet path mismatch")
        if review_id in by_review:
            actual_reviews[review_id].add(packet_id)
        for item in mentions:
            task_id = by_publication[item["publication_id"]]
            if item.get("task_id") != task_id:
                raise DriverFollowupIsolationError(f"{packet_id}: derived source task identity drift")
            actual_sources[task_id].add(packet_id)
    for review_id, expected in by_review.items():
        if actual_reviews[review_id] != expected:
            raise DriverFollowupIsolationError(f"{review_id}: direct review packet set drift")
    for task_id, values in groups.items():
        first = values[0][1]
        expected = {packet_id for packet_id, _ in values}
        for packet_id, task in values:
            if any(task[field] != first[field] for field in _TASK_PINS):
                raise DriverFollowupIsolationError(f"{task_id}: shared derived publication pin mismatch")
            explicit = task.get("source_packet_ids")
            if len(expected) > 1 and explicit is None:
                raise DriverFollowupIsolationError(f"{task_id}: shared publication requires explicit complete source set")
            if set(explicit if explicit is not None else [packet_id]) != expected:
                raise DriverFollowupIsolationError(f"{task_id}: declared source packet set drift")
        if actual_sources[task_id] != expected:
            raise DriverFollowupIsolationError(f"{task_id}: derived source packet set drift")


def validated_quarantines(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    from control_plane import research_driver_review_authority_fault_isolation as review_isolation
    from control_plane import research_result_review_audit_fault_isolation as review_audit

    rows = quarantine_rows(root)
    review_rows = review_isolation.validated_quarantines(root)
    audit_rows = review_audit.validated_rows(root) if any(
        row.get("source_review_basis") == AUDIT_SOURCE for row in rows.values()
    ) else {}
    result_rows = {}
    if any(row.get("source_review_basis") == RESULT_SOURCE for row in rows.values()):
        from control_plane import research_result_authority_fault_isolation as result_isolation

        result_rows = result_isolation.validated_review_rows(root)
    source_rows = {
        AUTHORITY_SOURCE: review_rows, AUDIT_SOURCE: audit_rows, RESULT_SOURCE: result_rows,
    }
    source_labels = {
        AUTHORITY_SOURCE: "review-authority quarantined",
        AUDIT_SOURCE: "immutable-review-audit quarantined",
        RESULT_SOURCE: "Result-control-authority withheld",
    }
    active_heads = _active_publication_heads(root)

    for packet_id, row in rows.items():
        review_id = row["review_id"]
        basis = row.get("source_review_basis", AUTHORITY_SOURCE)
        review_row = source_rows[basis].get(review_id)
        if review_row is None:
            raise DriverFollowupIsolationError(
                f"{QUARANTINE_FILE}: {packet_id} source review is not "
                + source_labels[basis]
            )
        if review_row["result_id"] != row["result_id"]:
            raise DriverFollowupIsolationError(
                f"{QUARANTINE_FILE}: {packet_id} result_id differs from source-review quarantine"
            )
        if row["packet_path"] != f"research_driver_followups/{review_id}/{packet_id}.json":
            raise DriverFollowupIsolationError(f"{packet_id}: exact source packet path mismatch")
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
        if packet.get("decision") != row.get("packet_decision", "TASK_SET_PUBLISHED"):
            raise DriverFollowupIsolationError(f"{packet_id}: exact packet decision drift")
        task_rows = packet.get("task_publications")
        if not isinstance(task_rows, list) or any(
            not isinstance(item, dict) or any(
                not isinstance(item.get(field), str) or not item[field]
                for field in ("task_id", "publication_id")
            ) for item in task_rows
        ):
            raise DriverFollowupIsolationError(f"{packet_id}: malformed exact packet task set")
        packet_pairs = [(item["task_id"], item["publication_id"]) for item in task_rows]
        declared_pairs = [(item["task_id"], item["publication_id"]) for item in row["derived_task_publications"]]
        if len(packet_pairs) != len(set(packet_pairs)) or set(packet_pairs) != set(declared_pairs):
            raise DriverFollowupIsolationError(
                f"{QUARANTINE_FILE}: {packet_id} derived publication set drift; "
                f"packet={sorted(packet_pairs)!r} declared={sorted(declared_pairs)!r}"
            )
        if row.get("isolation_kind", TASK_ISOLATION) == PACKET_ONLY and task_rows != []:
            raise DriverFollowupIsolationError(f"{packet_id}: packet-only isolation has derived tasks")

        for task in row["derived_task_publications"]:
            task_id = task["task_id"]
            publication_id = task["publication_id"]
            if task["publication_record_path"] != f"research_task_records/{task_id}/{publication_id}.json":
                raise DriverFollowupIsolationError(f"{publication_id}: exact publication record path mismatch")
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
            if record.get("taskbook_blob_sha1") != task["taskbook_blob_sha1"]:
                raise DriverFollowupIsolationError(f"{publication_id}: publication taskbook pin mismatch")
            taskbook_path = root / task["taskbook_path"]
            if not taskbook_path.exists():
                raise DriverFollowupIsolationError(
                    f"{QUARANTINE_FILE}: {publication_id} taskbook missing"
                )
            if _git_blob_sha1(taskbook_path.read_bytes()) != task["taskbook_blob_sha1"]:
                raise DriverFollowupIsolationError(
                    f"{QUARANTINE_FILE}: {publication_id} taskbook blob drift"
                )
    _complete_source_sets(rows, root)
    return rows


def derived_task_rows(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    return _derived_task_rows(validated_quarantines(root))


def _derived_task_rows(rows: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    sources: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for packet_id, row in rows.items():
        for task in row["derived_task_publications"]:
            task_id = task["task_id"]
            # validated_quarantines already proves exact pin agreement and the
            # complete source set; retain every source instead of overwriting.
            if task_id not in out:
                out[task_id] = dict(task)
            sources[task_id].append((packet_id, row["review_id"]))
    for task_id, pairs in sources.items():
        if len(pairs) == 1:
            out[task_id]["source_packet_id"], out[task_id]["source_review_id"] = pairs[0]
        else:
            out[task_id]["source_packet_ids"] = sorted(packet_id for packet_id, _ in pairs)
            out[task_id]["source_review_ids"] = sorted({review_id for _, review_id in pairs})
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
    packet_ids = task.get("source_packet_ids") or [task["source_packet_id"]]
    review_ids = task.get("source_review_ids") or [task["source_review_id"]]
    source_identity = (
        {"source_packet_id": packet_ids[0], "source_review_id": review_ids[0]}
        if len(packet_ids) == 1 else
        {"source_packet_ids": packet_ids, "source_review_ids": review_ids}
    )
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
                | set(packet_ids) | set(review_ids)
                | {
                    task["publication_id"],
                    task["publication_record_path"],
                }
            ),
            "evidence_status": "CONTROL_PLANE_QUARANTINED_REVIEW_DERIVED_PUBLICATION",
            "last_progress_ref": QUARANTINE_FILE,
            "last_progress_at": value.get("last_progress_at", "1970-01-01T00:00:00+00:00"),
            "hard_block": {
                "code": "NONOPERATIONAL_SOURCE_REVIEW_FOLLOWUP",
                **source_identity,
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


def _integrity_overlaps(
    tasks: dict[str, dict[str, Any]], root: Path,
) -> dict[str, dict[str, Any]]:
    from control_plane import research_task_integrity_fault_isolation as integrity

    rows = integrity.validated_quarantines(root)
    overlaps = {task_id: rows[task_id] for task_id in tasks.keys() & rows.keys()}
    for task_id, row in overlaps.items():
        task = tasks[task_id]
        for followup_field, integrity_field in (
            ("task_id", "task_id"), ("publication_id", "publication_id"),
            ("publication_record_path", "record_path"),
            ("publication_record_blob_sha1", "record_blob_sha1"),
            ("taskbook_path", "taskbook_path"), ("taskbook_blob_sha1", "taskbook_blob_sha1"),
        ):
            if task[followup_field] != row[integrity_field]:
                raise DriverFollowupIsolationError(
                    f"{task_id}: integrity/follow-up exact pin conflict: {followup_field}"
                )
    return overlaps


def _followup_block_cause(
    task_id: str, task: dict[str, Any], rows: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    packet_ids = task.get("source_packet_ids") or [task["source_packet_id"]]
    return {
        "registration_source": "DRIVER_FOLLOWUP_AUTHORITY_QUARANTINE",
        "quarantine_file": QUARANTINE_FILE,
        **{field: task[field] for field in _TASK_PINS},
        "hard_block": _blocked_definition(task_id, task, None)["hard_block"],
        "source_packets": [
            {
                **{field: rows[packet_id][field] for field in (
                    "packet_id", "review_id", "result_id", "packet_path", "packet_blob_sha1",
                )},
                "source_review_basis": rows[packet_id].get("source_review_basis", AUTHORITY_SOURCE),
            }
            for packet_id in sorted(packet_ids)
        ],
    }


def _composed_blocked_definition(
    task_id: str, task: dict[str, Any], prior: dict[str, Any] | None,
    integrity_row: dict[str, Any] | None, rows: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    followup = _blocked_definition(task_id, task, prior)
    if integrity_row is None:
        return followup
    from control_plane import research_task_integrity_fault_isolation as integrity

    # Reconstruct the primary cause from the independently validated registry,
    # never from an incoming registration_source label or hard_block payload.
    value = integrity.blocked_definition(task_id, integrity_row, prior)
    value["followup_authority_block"] = _followup_block_cause(task_id, task, rows)
    value["source_refs"] = sorted(set(value["source_refs"]) | set(followup["source_refs"]))
    value["tags"] = sorted(set(value["tags"]) | set(followup["tags"]))
    return value


def install(root: Path = ROOT) -> None:
    """Filter exact packets and locally block their exact solely-derived task heads."""
    rows = validated_quarantines(root)
    derived = derived_task_rows(root)

    from control_plane import research_publication_fault_isolation as publication

    # The publication layer establishes (rather than wraps) the root selectors.
    # Install that prerequisite before our wrappers even when integrity is later.
    publication.install(root)

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
            packet_rows = validated_quarantines(local_root)
            tasks = _derived_task_rows(packet_rows)
            overlaps = _integrity_overlaps(tasks, local_root)
            for task_id, task in tasks.items():
                by_id[task_id] = _composed_blocked_definition(
                    task_id, task, by_id.get(task_id), overlaps.get(task_id), packet_rows,
                )
            return [by_id[key] for key in sorted(by_id)]

        research_dispatch.merged_definitions = merged_definitions
        research_dispatch._followup_authority_isolation_installed = True

    if not rows and derived:
        raise DriverFollowupIsolationError("derived task quarantine exists without packet quarantine")


def audit(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    try:
        from control_plane import research_driver_review_authority_fault_isolation as review_isolation
        from control_plane import research_result_review_audit_fault_isolation as review_audit
        from control_plane import research_task_integrity_fault_isolation as integrity

        review_isolation.install(root)
        review_audit.install(root)
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
        tasks = _derived_task_rows(rows)
        overlaps = _integrity_overlaps(tasks, root)
        for task_id, task in tasks.items():
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
            if task_id in overlaps:
                expected = integrity.blocked_definition(task_id, overlaps[task_id])
                if definition.get("registration_source") != expected["registration_source"]:
                    errors.append(f"{task_id}: composed integrity registration source drifted")
                hard_block = definition.get("hard_block")
                if not isinstance(hard_block, dict) or any(
                    key not in hard_block or hard_block[key] != value
                    for key, value in expected["hard_block"].items()
                ):
                    errors.append(f"{task_id}: composed integrity hard-block pin drifted")
                if definition.get("followup_authority_block") != _followup_block_cause(task_id, task, rows):
                    errors.append(f"{task_id}: composed follow-up authority cause drifted")
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
