#!/usr/bin/env python3
"""Canonical objective authority wrapper for Enterprise Math.

The underlying ``research_objective_records.py`` stores immutable objective
versions plus the mutable per-objective operational head.  This wrapper adds an
immutable receipt for every operational head selection and requires task/objective
bindings to prove that the task publication occurred while the pinned objective
generation was actually operational.

A retained OPEN proposal is therefore not enough.  Likewise, an old generation
that really was operational remains bindable for a historical task only when the
task's immutable ``published_at`` falls inside that generation's proven
operational tenure.

This module governs control provenance only.  It grants no Working Truth,
Foundation authority, canonical promotion, or PRE_FINAL permission.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import research_objective_records as core  # noqa: E402
from tools import research_task_records  # noqa: E402

SELECTION_SCHEMA = "ENTERPRISE_MATH_OBJECTIVE_HEAD_SELECTION_RECEIPT_V1"
SELECTION_AUTHORITY = "IMMUTABLE_OPERATIONAL_OBJECTIVE_HEAD_SELECTION_RECEIPT"
BINDING_AUTHORITY = "EXACT_TASK_PUBLICATION_TO_PROVEN_OPERATIONAL_OPEN_OBJECTIVE_GENERATION"


class ObjectiveAuthorityError(ValueError):
    pass


def _load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ObjectiveAuthorityError(f"JSON object required: {path}")
    return value


def _sha256(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def _parse_time(value: str, label: str) -> datetime:
    if not isinstance(value, str) or not value.strip():
        raise ObjectiveAuthorityError(f"{label} must be a nonempty timestamp")
    try:
        dt = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
    except Exception as exc:
        raise ObjectiveAuthorityError(f"invalid {label}: {value!r}") from exc
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _exclusive_json(path: Path, value: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(dict(value), ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    try:
        with path.open("x", encoding="utf-8") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
    except FileExistsError as exc:
        raise ObjectiveAuthorityError(f"immutable authority record already exists: {path}") from exc


def selection_receipt_path(
    objective_id: str, objective_generation_id: str, root: Path = ROOT
) -> Path:
    return (
        root
        / "research_objective_head_events"
        / objective_id
        / f"{objective_generation_id}.json"
    )


def iter_selection_receipts(root: Path = ROOT) -> list[dict[str, Any]]:
    directory = root / "research_objective_head_events"
    if not directory.exists():
        return []
    out: list[dict[str, Any]] = []
    for path in sorted(directory.glob("*/*.json")):
        value = _load_json(path)
        value["_receipt_path"] = path.relative_to(root).as_posix()
        value["_receipt_sha256"] = _sha256(path)
        out.append(value)
    return out


def selection_receipt_map(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for item in iter_selection_receipts(root):
        gid = item.get("objective_generation_id")
        if not isinstance(gid, str) or not gid:
            raise ObjectiveAuthorityError("selection receipt missing objective_generation_id")
        if gid in out:
            raise ObjectiveAuthorityError(f"duplicate objective selection receipt: {gid}")
        out[gid] = item
    return out


def _build_selection_receipt(
    generation: Mapping[str, Any], head: Mapping[str, Any], root: Path
) -> dict[str, Any]:
    oid = generation.get("objective_id")
    gid = generation.get("objective_generation_id")
    if not isinstance(oid, str) or not isinstance(gid, str):
        raise ObjectiveAuthorityError("objective generation identity is missing")
    objective_path = core.objective_generation_path(oid, gid, root)
    if head.get("objective_id") != oid or head.get("objective_generation_id") != gid:
        raise ObjectiveAuthorityError("operational head does not select the new objective generation")
    if head.get("objective_record_sha256") != _sha256(objective_path):
        raise ObjectiveAuthorityError("operational head objective digest mismatch")
    return {
        "record_schema": SELECTION_SCHEMA,
        "objective_id": oid,
        "objective_generation_id": gid,
        "generation": generation.get("generation"),
        "objective_status": generation.get("objective_status"),
        "previous_objective_generation_id": generation.get("previous_objective_generation_id"),
        "objective_record_sha256": _sha256(objective_path),
        "selected_by": head.get("updated_by"),
        "selected_at": head.get("updated_at"),
        "head_authority": head.get("authority"),
        "selection_authority": SELECTION_AUTHORITY,
        "working_truth_granted": False,
        "foundation_authority_granted": False,
        "canonical_promotion_granted": False,
        "final_permission_granted": False,
    }


def create_and_select(
    *, expected_previous_generation_id: str | None, root: Path = ROOT, **kwargs: Any
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    """Create/select through the core and freeze an immutable selection receipt.

    If receipt persistence fails after the core head update, canonical audit fails
    closed until the missing receipt is repaired; no silent authority is granted.
    """
    generation, head = core.create_and_select(
        expected_previous_generation_id=expected_previous_generation_id,
        root=root,
        **kwargs,
    )
    receipt = _build_selection_receipt(generation, head, root)
    path = selection_receipt_path(
        str(generation["objective_id"]), str(generation["objective_generation_id"]), root
    )
    _exclusive_json(path, receipt)
    return generation, head, receipt


def _task_record(task_id: str, publication_id: str, root: Path) -> dict[str, Any]:
    matches = [
        item
        for item in research_task_records.iter_records(root)
        if item.get("task_id") == task_id and item.get("publication_id") == publication_id
    ]
    if len(matches) != 1:
        raise ObjectiveAuthorityError("task publication is unknown or ambiguous")
    return matches[0]


def _receipt_for_generation(
    objective_id: str, objective_generation_id: str, root: Path
) -> dict[str, Any]:
    receipt = selection_receipt_map(root).get(objective_generation_id)
    if receipt is None or receipt.get("objective_id") != objective_id:
        raise ObjectiveAuthorityError(
            "objective generation lacks immutable operational-head selection provenance"
        )
    if receipt.get("record_schema") != SELECTION_SCHEMA:
        raise ObjectiveAuthorityError("objective selection receipt has wrong schema")
    if receipt.get("selection_authority") != SELECTION_AUTHORITY:
        raise ObjectiveAuthorityError("objective selection receipt has wrong authority")
    objective = core.objective_record_map(root).get(objective_generation_id)
    if objective is None or objective.get("objective_id") != objective_id:
        raise ObjectiveAuthorityError("objective generation is unavailable or mismatched")
    objective_path = core.objective_generation_path(objective_id, objective_generation_id, root)
    if receipt.get("objective_record_sha256") != _sha256(objective_path):
        raise ObjectiveAuthorityError("objective selection receipt digest drift")
    if receipt.get("objective_status") != objective.get("objective_status"):
        raise ObjectiveAuthorityError("objective selection receipt status mismatch")
    return receipt


def _successor_receipt(
    objective_id: str, objective_generation_id: str, root: Path
) -> dict[str, Any] | None:
    matches = [
        item
        for item in iter_selection_receipts(root)
        if item.get("objective_id") == objective_id
        and item.get("previous_objective_generation_id") == objective_generation_id
    ]
    if len(matches) > 1:
        raise ObjectiveAuthorityError(
            "objective operational selection history forks from one previous generation"
        )
    return matches[0] if matches else None


def prove_publication_within_operational_tenure(
    task_record: Mapping[str, Any],
    objective_id: str,
    objective_generation_id: str,
    root: Path = ROOT,
) -> dict[str, Any]:
    receipt = _receipt_for_generation(objective_id, objective_generation_id, root)
    if receipt.get("objective_status") != "OPEN":
        raise ObjectiveAuthorityError(
            "task binding requires an objective generation selected while OPEN"
        )
    published_at = _parse_time(str(task_record.get("published_at", "")), "task published_at")
    selected_at = _parse_time(str(receipt.get("selected_at", "")), "objective selected_at")
    if published_at < selected_at:
        raise ObjectiveAuthorityError(
            "task publication predates the objective generation operational selection"
        )
    successor = _successor_receipt(objective_id, objective_generation_id, root)
    if successor is not None:
        successor_at = _parse_time(
            str(successor.get("selected_at", "")), "successor objective selected_at"
        )
        if successor_at <= selected_at:
            raise ObjectiveAuthorityError("objective selection receipt timestamps are not monotone")
        if published_at >= successor_at:
            raise ObjectiveAuthorityError(
                "task publication occurred after the target objective generation stopped being operational"
            )
    return {
        "receipt": receipt,
        "receipt_path": receipt.get("_receipt_path"),
        "receipt_sha256": receipt.get("_receipt_sha256"),
        "operational_from": receipt.get("selected_at"),
        "operational_until": successor.get("selected_at") if successor else None,
    }


def bind_historical_task(
    *,
    task_id: str,
    publication_id: str,
    objective_id: str,
    objective_generation_id: str,
    bound_by: str,
    bound_at: str,
    root: Path = ROOT,
) -> dict[str, Any]:
    task = _task_record(task_id, publication_id, root)
    if task.get("parent_objective_id") != objective_id:
        raise ObjectiveAuthorityError(
            "objective_id differs from task publication parent_objective_id"
        )
    proof = prove_publication_within_operational_tenure(
        task, objective_id, objective_generation_id, root
    )
    bound_time = _parse_time(bound_at, "bound_at")
    selected_time = _parse_time(str(proof["operational_from"]), "objective selected_at")
    if bound_time < selected_time:
        raise ObjectiveAuthorityError("binding timestamp predates objective selection")
    objective_path = core.objective_generation_path(objective_id, objective_generation_id, root)
    value = {
        "record_schema": core.BINDING_SCHEMA,
        "task_id": task_id,
        "publication_id": publication_id,
        "taskbook_path": task.get("taskbook_path"),
        "taskbook_blob_sha1": task.get("taskbook_blob_sha1"),
        "objective_id": objective_id,
        "objective_generation_id": objective_generation_id,
        "objective_record_sha256": _sha256(objective_path),
        "bound_by": bound_by.strip().upper(),
        "bound_at": bound_time.isoformat(),
        "binding_authority": BINDING_AUTHORITY,
        "operational_selection_provenance": SELECTION_AUTHORITY,
        "operational_selection_receipt_path": proof["receipt_path"],
        "operational_selection_receipt_sha256": proof["receipt_sha256"],
        "operational_from": proof["operational_from"],
        "operational_until": proof["operational_until"],
        "working_truth_granted": False,
        "foundation_authority_granted": False,
        "final_permission_granted": False,
    }
    # Reuse the core identity validator while retaining the richer canonical record.
    core._driver_identity(value["bound_by"], "bound_by")
    path = core.task_binding_path(task_id, publication_id, root)
    _exclusive_json(path, value)
    return value


def resolve_authoritative_task_parent_binding(
    task_record: Mapping[str, Any], root: Path = ROOT
) -> dict[str, Any]:
    resolved = core.resolve_task_parent_binding(task_record, root)
    gid = resolved.get("objective_generation_id")
    if resolved.get("binding_source") == "LEGACY_UNBOUND" or not isinstance(gid, str):
        return {**resolved, "objective_authority_verified": False}
    proof = prove_publication_within_operational_tenure(
        task_record, str(resolved["objective_id"]), gid, root
    )
    if resolved.get("binding_source") == "IMMUTABLE_LEGACY_SIDECAR":
        binding = resolved.get("binding")
        if not isinstance(binding, Mapping):
            raise ObjectiveAuthorityError("historical binding record is missing")
        if binding.get("binding_authority") != BINDING_AUTHORITY:
            raise ObjectiveAuthorityError(
                "historical task binding lacks canonical operational-head authority"
            )
        if binding.get("operational_selection_receipt_sha256") != proof["receipt_sha256"]:
            raise ObjectiveAuthorityError("historical task binding selection receipt digest mismatch")
    return {
        **resolved,
        "objective_authority_verified": True,
        "operational_selection": proof,
    }


def audit(root: Path = ROOT) -> list[str]:
    errors = list(core.audit(root))
    try:
        receipts = selection_receipt_map(root)
        records = core.objective_record_map(root)
        heads = core.head_map(root)
        bindings = core.binding_map(root)
    except Exception as exc:
        return errors + [str(exc)]

    for gid, receipt in receipts.items():
        prefix = receipt.get("_receipt_path", gid)
        objective = records.get(gid)
        if receipt.get("record_schema") != SELECTION_SCHEMA:
            errors.append(f"{prefix}: wrong selection receipt schema")
        if receipt.get("selection_authority") != SELECTION_AUTHORITY:
            errors.append(f"{prefix}: wrong selection authority")
        if objective is None or objective.get("objective_id") != receipt.get("objective_id"):
            errors.append(f"{prefix}: selected objective generation missing or mismatched")
            continue
        objective_path = core.objective_generation_path(
            str(objective["objective_id"]), gid, root
        )
        if receipt.get("objective_record_sha256") != _sha256(objective_path):
            errors.append(f"{prefix}: objective record digest drift")
        for field in (
            "generation",
            "objective_status",
            "previous_objective_generation_id",
        ):
            if receipt.get(field) != objective.get(field):
                errors.append(f"{prefix}: {field} differs from objective generation")
        for field in (
            "working_truth_granted",
            "foundation_authority_granted",
            "canonical_promotion_granted",
            "final_permission_granted",
        ):
            if receipt.get(field) is not False:
                errors.append(f"{prefix}: {field} must be false")

    for oid, head in heads.items():
        gid = str(head.get("objective_generation_id"))
        receipt = receipts.get(gid)
        if receipt is None or receipt.get("objective_id") != oid:
            errors.append(
                f"research_objective_heads/{oid}.json: current operational head lacks immutable selection receipt"
            )
            continue
        if receipt.get("selected_at") != head.get("updated_at"):
            errors.append(f"research_objective_heads/{oid}.json: selected_at differs from current head")
        if receipt.get("selected_by") != head.get("updated_by"):
            errors.append(f"research_objective_heads/{oid}.json: selected_by differs from current head")

    task_records = {
        (str(item.get("task_id")), str(item.get("publication_id"))): item
        for item in research_task_records.iter_records(root)
        if isinstance(item.get("task_id"), str)
        and isinstance(item.get("publication_id"), str)
    }
    for key, binding in bindings.items():
        prefix = binding.get("_binding_path", str(key))
        if binding.get("binding_authority") != BINDING_AUTHORITY:
            errors.append(f"{prefix}: binding lacks canonical operational-head authority")
            continue
        task = task_records.get(key)
        if task is None:
            continue
        try:
            proof = prove_publication_within_operational_tenure(
                task,
                str(binding.get("objective_id")),
                str(binding.get("objective_generation_id")),
                root,
            )
            if binding.get("operational_selection_receipt_sha256") != proof["receipt_sha256"]:
                errors.append(f"{prefix}: selection receipt digest mismatch")
            if binding.get("operational_from") != proof["operational_from"]:
                errors.append(f"{prefix}: operational_from mismatch")
            if binding.get("operational_until") != proof["operational_until"]:
                errors.append(f"{prefix}: operational_until mismatch")
        except Exception as exc:
            errors.append(f"{prefix}: {exc}")
    return errors


def _payload(args: argparse.Namespace) -> dict[str, Any]:
    if args.payload_json:
        value = json.loads(args.payload_json)
    else:
        value = json.loads(Path(args.payload_file).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ObjectiveAuthorityError("objective payload must be a JSON object")
    return value


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Enterprise Math canonical objective selection/binding authority"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    create = sub.add_parser("create-and-select")
    source = create.add_mutually_exclusive_group(required=True)
    source.add_argument("--payload-json")
    source.add_argument("--payload-file")
    create.add_argument("--expected-previous-generation-id")

    bind = sub.add_parser("bind-historical-task")
    bind.add_argument("--task-id", required=True)
    bind.add_argument("--publication-id", required=True)
    bind.add_argument("--objective-id", required=True)
    bind.add_argument("--objective-generation-id", required=True)
    bind.add_argument("--bound-by", required=True)
    bind.add_argument("--bound-at", required=True)

    sub.add_parser("audit")
    args = parser.parse_args()

    if args.command == "create-and-select":
        payload = _payload(args)
        generation, head, receipt = create_and_select(
            expected_previous_generation_id=args.expected_previous_generation_id,
            root=ROOT,
            **payload,
        )
        out = {"generation": generation, "head": head, "selection_receipt": receipt}
        print(json.dumps(out, ensure_ascii=False, indent=2, sort_keys=True))
        return 0
    if args.command == "bind-historical-task":
        value = bind_historical_task(
            task_id=args.task_id,
            publication_id=args.publication_id,
            objective_id=args.objective_id,
            objective_generation_id=args.objective_generation_id,
            bound_by=args.bound_by,
            bound_at=args.bound_at,
            root=ROOT,
        )
        print(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True))
        return 0
    errors = audit(ROOT)
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print(
        f"PASS: canonical objective authority valid ({len(iter_selection_receipts(ROOT))} selection receipt(s))."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ObjectiveAuthorityError, core.ObjectiveRecordError) as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
