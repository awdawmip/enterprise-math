#!/usr/bin/env python3
"""Rollback-safe Driver follow-up materialization.

The historical materializer writes taskbooks, publication records and the final
follow-up packet in several filesystem steps.  A later validation failure can
therefore leave a durable partial taskset even though the operation returned an
error.  This adapter preserves the existing review/follow-up semantics but makes
one invocation failure-atomic at the repository working-tree boundary:

* every taskbook is fully policy-prepared in a temporary directory first;
* final taskbook paths are created exclusively from those frozen bytes;
* all publication records are built before any publication record is persisted;
* publication records are then created exclusively;
* the follow-up packet is created last;
* any later failure removes only paths created by this invocation whose bytes
  still exactly equal the frozen candidate bytes.

An already-persisted immutable Driver review is not rolled back.  If follow-up
materialization fails, that review remains explicit `AWAITING_DRIVER_FOLLOWUP`
authority and is surfaced by the Driver queue.  Existing immutable history is
never rewritten or deleted.
"""
from __future__ import annotations

import json
import tempfile
from pathlib import Path
from typing import Any

from control_plane import immutable_write_transaction as _tx

ROOT = Path(__file__).resolve().parents[1]


class DriverFollowupTransactionError(ValueError):
    pass


def _task_record_bytes(value: dict[str, Any]) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def _packet_bytes(value: dict[str, Any]) -> bytes:
    return (
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")


def _rollback_owned(created: list[_tx.PlannedFile]) -> list[str]:
    """Remove only unchanged bytes created by this invocation."""
    errors: list[str] = []
    for row in reversed(created):
        try:
            if not row.path.exists():
                continue
            if row.path.read_bytes() != row.content:
                errors.append(
                    f"refused rollback because candidate changed after creation: {row.path}"
                )
                continue
            row.path.unlink()
        except Exception as exc:  # pragma: no cover - defensive filesystem path
            errors.append(f"rollback failed for {row.path}: {exc}")
    return errors


def _raise_with_rollback(
    exc: Exception, created: list[_tx.PlannedFile]
) -> None:
    rollback_errors = _rollback_owned(created)
    detail = str(exc)
    if rollback_errors:
        detail += "; " + "; ".join(rollback_errors)
    raise DriverFollowupTransactionError(detail) from exc


def _prepared_taskbook_bytes(
    impl,
    task_spec: dict[str, Any],
    parent: str,
    root: Path,
) -> tuple[dict[str, Any], bytes]:
    from tools import research_task_records, research_taskbook

    raw = impl._taskbook_text(task_spec, parent)
    with tempfile.TemporaryDirectory() as td:
        candidate = Path(td) / "task.md"
        candidate.write_text(raw, encoding="utf-8")
        meta = research_task_records.prepare_taskbook(
            candidate,
            publisher_role="RESEARCH_DRIVER",
            parent_objective_id=parent,
            root=root,
        )
        prepared = candidate.read_bytes()
        parsed, body = research_taskbook.split_taskbook(prepared.decode("utf-8"))
        if parsed != meta:
            raise DriverFollowupTransactionError(
                "prepared taskbook metadata differs from returned canonical metadata"
            )
        errors = research_task_records.validate_body(body)
        if errors:
            raise DriverFollowupTransactionError("; ".join(errors))
        return meta, prepared


def materialize(
    *,
    review_id: str,
    spec: dict[str, Any],
    created_at: str | None = None,
    root: Path = ROOT,
) -> dict[str, Any]:
    """Materialize one follow-up invocation with rollback-safe final paths."""
    import research_driver_followup as impl
    from tools import research_task_records

    review = impl.review_map(root).get(review_id)
    if review is None:
        raise DriverFollowupTransactionError(f"unknown review_id: {review_id}")
    if not impl.review_requires_followup(review):
        raise DriverFollowupTransactionError(
            "review predates automatic follow-up policy cutover"
        )
    result = impl.result_map(root).get(str(review.get("result_id")))
    if result is None:
        raise DriverFollowupTransactionError("reviewed result is unavailable")
    parent = impl._source_parent_objective(review, result, root)
    decision = spec.get("decision")
    gates = spec.get("gate_decisions")
    task_specs = spec.get("tasks", [])
    if decision not in impl.DECISIONS:
        raise DriverFollowupTransactionError("spec decision is invalid")
    if not isinstance(task_specs, list):
        raise DriverFollowupTransactionError("spec tasks must be a list")

    normalized_gates = impl._gate_map(gates)
    impl._forced_gate_rules(review, result, normalized_gates)
    timestamp = impl._now(created_at)

    if decision == "PARENT_OBJECTIVE_CLOSURE":
        if task_specs:
            raise DriverFollowupTransactionError(
                "parent closure spec cannot include tasks"
            )
        head = impl._objective_head(parent, root)
        if head is None or head.get("objective_status") != "CLOSED":
            raise DriverFollowupTransactionError(
                "parent Objective must already be canonically CLOSED before no-task exception"
            )
        if any(row["decision"] == "REQUIRED" for row in normalized_gates.values()):
            raise DriverFollowupTransactionError(
                "parent closure cannot leave REQUIRED gates"
            )
        packet = impl.build_packet(
            review_id=review_id,
            decision=decision,
            gate_decisions=[normalized_gates[name] for name in impl.GATES],
            task_publications=[],
            driver_id=str(review["driver_id"]),
            created_at=timestamp,
            root=root,
        )
        out = root / "research_driver_followups" / review_id / f"{packet['packet_id']}.json"
        planned = _tx.PlannedFile(out, _packet_bytes(packet))
        try:
            _tx.commit([planned], postcheck=lambda: impl.audit(root))
        except Exception as exc:
            raise DriverFollowupTransactionError(str(exc)) from exc
        return {**packet, "record_path": out.relative_to(root).as_posix()}

    if not task_specs:
        raise DriverFollowupTransactionError(
            "TASK_SET_PUBLISHED requires one or more task specs"
        )

    suffix = review_id.replace("DR-", "").lower()[:8]
    seen_paths: set[Path] = set()
    seen_task_ids: set[str] = set()
    prepared: list[tuple[dict[str, Any], dict[str, Any], Path, bytes]] = []
    for raw_spec in task_specs:
        if not isinstance(raw_spec, dict):
            raise DriverFollowupTransactionError("each task spec must be an object")
        task_id = impl._safe(raw_spec.get("task_id"), "task_id")
        if task_id in seen_task_ids:
            raise DriverFollowupTransactionError(
                f"one follow-up invocation cannot publish task_id twice: {task_id}"
            )
        seen_task_ids.add(task_id)
        filename = str(
            raw_spec.get("taskbook_filename") or f"{task_id}_{suffix}.md"
        )
        if "/" in filename or "\\" in filename or not filename.endswith(".md"):
            raise DriverFollowupTransactionError(
                "taskbook_filename must be one repository-local .md filename"
            )
        final_path = root / "research_tasks" / filename
        if final_path in seen_paths or final_path.exists():
            raise DriverFollowupTransactionError(
                f"follow-up taskbook path already exists: {final_path}"
            )
        seen_paths.add(final_path)
        meta, prepared_bytes = _prepared_taskbook_bytes(
            impl, raw_spec, parent, root
        )
        prepared.append((raw_spec, meta, final_path, prepared_bytes))

    taskbook_files = [
        _tx.PlannedFile(final_path, prepared_bytes)
        for _, _, final_path, prepared_bytes in prepared
    ]
    created: list[_tx.PlannedFile] = []
    try:
        _tx.commit(taskbook_files)
        created.extend(taskbook_files)

        record_files: list[_tx.PlannedFile] = []
        published_rows: list[dict[str, Any]] = []
        for task_spec, meta, path, _ in prepared:
            record = research_task_records.build_record(
                meta,
                path=path,
                publisher_role="RESEARCH_DRIVER",
                publisher_id=str(review["driver_id"]),
                research_value=str(task_spec["research_value"]).strip(),
                published_at=timestamp,
                supersedes_publication_id=task_spec.get(
                    "supersedes_publication_id"
                ),
                root=root,
            )
            record_path = research_task_records.record_path(
                root, record["task_id"], record["publication_id"]
            )
            record_files.append(
                _tx.PlannedFile(record_path, _task_record_bytes(record))
            )
            published_rows.append(
                {
                    "task_id": record["task_id"],
                    "publication_id": record["publication_id"],
                    "task_role": task_spec["task_role"],
                }
            )

        _tx.commit(record_files)
        created.extend(record_files)

        publication_errors = research_task_records.audit(root)
        if publication_errors:
            raise DriverFollowupTransactionError(
                "follow-up task publication audit failed: "
                + "; ".join(publication_errors)
            )

        packet = impl.build_packet(
            review_id=review_id,
            decision="TASK_SET_PUBLISHED",
            gate_decisions=[normalized_gates[name] for name in impl.GATES],
            task_publications=published_rows,
            driver_id=str(review["driver_id"]),
            created_at=timestamp,
            root=root,
        )
        packet_path = (
            root
            / "research_driver_followups"
            / review_id
            / f"{packet['packet_id']}.json"
        )
        packet_file = _tx.PlannedFile(packet_path, _packet_bytes(packet))
        _tx.commit([packet_file])
        created.append(packet_file)

        errors = impl.audit(root)
        if errors:
            raise DriverFollowupTransactionError(
                "follow-up audit failed: " + "; ".join(errors)
            )
        return {
            **packet,
            "record_path": packet_path.relative_to(root).as_posix(),
        }
    except Exception as exc:
        _raise_with_rollback(exc, created)
    raise AssertionError("unreachable")


def install(root: Path = ROOT) -> None:
    import research_driver_followup as impl

    if getattr(impl, "_rollback_safe_materialize_installed", False):
        return
    impl.nontransactional_materialize = impl.materialize
    impl.materialize = materialize
    impl._rollback_safe_materialize_installed = True


def audit(root: Path = ROOT) -> list[str]:
    try:
        install(root)
        import research_driver_followup as impl

        if impl.materialize is not materialize:
            return ["rollback-safe Driver follow-up materializer is not installed"]
    except Exception as exc:
        return [str(exc)]
    return []


if __name__ == "__main__":
    errors = audit()
    if errors:
        for error in errors:
            print("ERROR:", error)
        raise SystemExit(1)
    print("PASS: Driver follow-up materialization is rollback-safe.")
