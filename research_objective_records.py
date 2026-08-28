#!/usr/bin/env python3
"""Immutable objective generations plus one operational per-objective head.

Objective generations are retained history/proposals. They do not become runtime
control merely by existing. ``research_objective_heads/<objective-id>.json`` is
the small per-objective operational CAS point. Historical task publications may
bind to an exact OPEN objective generation through an immutable sidecar without
rewriting the task publication itself.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping

try:
    from tools import research_identity
    from tools import research_task_records
except ModuleNotFoundError:
    from tools import research_identity  # type: ignore
    from tools import research_task_records  # type: ignore

import research_driver_authority
import research_objective_driver_authority

ROOT = Path(__file__).resolve().parent
OBJECTIVE_SCHEMA = "ENTERPRISE_MATH_RESEARCH_OBJECTIVE_RECORD_V1"
HEAD_SCHEMA = "ENTERPRISE_MATH_RESEARCH_OBJECTIVE_HEAD_V1"
BINDING_SCHEMA = "ENTERPRISE_MATH_TASK_OBJECTIVE_BINDING_V1"
STATUSES = {"OPEN", "PARKED", "CLOSED"}
PUBLISHER_ROLE = "RESEARCH_DRIVER"


class ObjectiveRecordError(ValueError):
    pass


def _load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ObjectiveRecordError(f"JSON object required: {path}")
    return value


def _safe_id(value: str, label: str) -> str:
    text = value.strip()
    if not text or not re.fullmatch(r"[A-Za-z0-9._-]+", text):
        raise ObjectiveRecordError(f"{label} contains unsupported characters")
    return text


def _parse_time(value: str) -> datetime:
    try:
        dt = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
    except Exception as exc:
        raise ObjectiveRecordError(f"invalid timestamp: {value!r}") from exc
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _now(value: str | None) -> str:
    return (_parse_time(value) if value else datetime.now(timezone.utc)).isoformat()


def _sha256(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def _exclusive_json(path: Path, value: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(dict(value), ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    try:
        with path.open("x", encoding="utf-8") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
    except FileExistsError as exc:
        raise ObjectiveRecordError(f"immutable record already exists: {path}") from exc


def _atomic_replace_json(path: Path, value: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(dict(value), ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    fd, temp_name = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)


def _driver_identity(value: str, label: str) -> str:
    text = value.strip().upper()
    if not research_identity.valid_execution_id(text) or not text.startswith("EM-DVR-"):
        raise ObjectiveRecordError(f"{label} must use Driver-ID syntax")
    return text


def _driver_authority_fields(driver_id: str, at: str, root: Path) -> dict[str, Any]:
    try:
        return research_objective_driver_authority.authority_fields(driver_id, at, root)
    except research_driver_authority.DriverAuthorityError as exc:
        raise ObjectiveRecordError(str(exc)) from exc


def objective_generation_path(
    objective_id: str, objective_generation_id: str, root: Path = ROOT
) -> Path:
    return (
        root
        / "research_objective_records"
        / _safe_id(objective_id, "objective_id")
        / f"{_safe_id(objective_generation_id, 'objective_generation_id')}.json"
    )


def objective_head_path(objective_id: str, root: Path = ROOT) -> Path:
    return root / "research_objective_heads" / f"{_safe_id(objective_id, 'objective_id')}.json"


def task_binding_path(task_id: str, publication_id: str, root: Path = ROOT) -> Path:
    return (
        root
        / "research_task_objective_bindings"
        / _safe_id(task_id, "task_id")
        / f"{_safe_id(publication_id, 'publication_id')}.json"
    )


def iter_objective_records(root: Path = ROOT) -> list[dict[str, Any]]:
    directory = root / "research_objective_records"
    if not directory.exists():
        return []
    out: list[dict[str, Any]] = []
    for path in sorted(directory.glob("*/*.json")):
        value = _load_json(path)
        value["_record_path"] = path.relative_to(root).as_posix()
        value["_record_sha256"] = _sha256(path)
        out.append(value)
    return out


def objective_record_map(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for item in iter_objective_records(root):
        gid = item.get("objective_generation_id")
        if not isinstance(gid, str) or not gid:
            raise ObjectiveRecordError("objective record missing objective_generation_id")
        if gid in out:
            raise ObjectiveRecordError(f"duplicate objective_generation_id: {gid}")
        out[gid] = item
    return out


def iter_heads(root: Path = ROOT) -> list[dict[str, Any]]:
    directory = root / "research_objective_heads"
    if not directory.exists():
        return []
    out: list[dict[str, Any]] = []
    for path in sorted(directory.glob("*.json")):
        value = _load_json(path)
        value["_head_path"] = path.relative_to(root).as_posix()
        out.append(value)
    return out


def head_map(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for item in iter_heads(root):
        oid = item.get("objective_id")
        if not isinstance(oid, str) or not oid:
            raise ObjectiveRecordError("objective head missing objective_id")
        if oid in out:
            raise ObjectiveRecordError(f"duplicate objective head: {oid}")
        out[oid] = item
    return out


def current_head(objective_id: str, root: Path = ROOT) -> dict[str, Any] | None:
    return head_map(root).get(objective_id)


def generation_id(payload: Mapping[str, Any]) -> str:
    raw = json.dumps(dict(payload), sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return "OG-" + hashlib.sha256(raw).hexdigest()[:20].upper()


def _string_list(value: Any, label: str) -> list[str]:
    if not isinstance(value, list) or not value:
        raise ObjectiveRecordError(f"{label} must be a nonempty string list")
    out: list[str] = []
    for item in value:
        if not isinstance(item, str) or not item.strip():
            raise ObjectiveRecordError(f"{label} must contain nonempty strings")
        out.append(item.strip())
    if len(set(out)) != len(out):
        raise ObjectiveRecordError(f"{label} contains duplicates")
    return out


def build_generation(
    *,
    objective_id: str,
    objective_status: str,
    title: str,
    scope: str,
    success_criteria: list[str],
    closure_criteria: list[str],
    research_value: str,
    publisher_id: str,
    created_at: str,
    disposition_reason: str | None = None,
    closure_evidence_refs: list[str] | None = None,
    reopen_reason: str | None = None,
    root: Path = ROOT,
) -> dict[str, Any]:
    oid = _safe_id(objective_id, "objective_id")
    status = objective_status.strip().upper()
    if status not in STATUSES:
        raise ObjectiveRecordError(f"invalid objective_status: {objective_status}")
    if not isinstance(title, str) or not title.strip():
        raise ObjectiveRecordError("title is required")
    if not isinstance(scope, str) or not scope.strip():
        raise ObjectiveRecordError("scope is required")
    if not isinstance(research_value, str) or not research_value.strip():
        raise ObjectiveRecordError("research_value is required")
    driver_id = _driver_identity(publisher_id, "publisher_id")
    created = _parse_time(created_at).isoformat()
    authority_fields = _driver_authority_fields(driver_id, created, root)
    success = _string_list(success_criteria, "success_criteria")
    closure = _string_list(closure_criteria, "closure_criteria")

    head = current_head(oid, root)
    previous_id = head.get("objective_generation_id") if head else None
    previous = None
    generation = 1
    if previous_id is not None:
        previous = objective_record_map(root).get(str(previous_id))
        if previous is None:
            raise ObjectiveRecordError("current objective head references missing generation")
        generation = int(previous.get("generation", 0)) + 1
    elif status != "OPEN":
        raise ObjectiveRecordError("initial objective generation must be OPEN")

    if previous is not None and previous.get("objective_status") == "CLOSED" and status == "OPEN":
        if not isinstance(reopen_reason, str) or not reopen_reason.strip():
            raise ObjectiveRecordError("CLOSED -> OPEN requires reopen_reason")
    if status == "CLOSED":
        if not isinstance(disposition_reason, str) or not disposition_reason.strip():
            raise ObjectiveRecordError("CLOSED objective generation requires disposition_reason")
        evidence = _string_list(closure_evidence_refs or [], "closure_evidence_refs")
    else:
        evidence = []

    value: dict[str, Any] = {
        "record_schema": OBJECTIVE_SCHEMA,
        "objective_id": oid,
        "generation": generation,
        "previous_objective_generation_id": previous_id,
        "objective_status": status,
        "title": title.strip(),
        "scope": scope.strip(),
        "success_criteria": success,
        "closure_criteria": closure,
        "research_value": research_value.strip(),
        "publisher_role": PUBLISHER_ROLE,
        "publisher_id": driver_id,
        "created_at": created,
        **authority_fields,
        "working_truth_granted": False,
        "foundation_authority_granted": False,
        "canonical_promotion_granted": False,
    }
    if status == "CLOSED":
        value["disposition_reason"] = disposition_reason.strip()
        value["closure_evidence_refs"] = evidence
    if reopen_reason is not None and reopen_reason.strip():
        value["reopen_reason"] = reopen_reason.strip()
    value["objective_generation_id"] = generation_id(value)
    return value


def write_generation(record: Mapping[str, Any], root: Path = ROOT) -> Path:
    oid = str(record.get("objective_id", ""))
    gid = str(record.get("objective_generation_id", ""))
    path = objective_generation_path(oid, gid, root)
    _exclusive_json(path, record)
    return path


def select_head(
    *,
    objective_id: str,
    objective_generation_id: str,
    expected_previous_generation_id: str | None,
    updated_by: str,
    updated_at: str,
    root: Path = ROOT,
) -> dict[str, Any]:
    oid = _safe_id(objective_id, "objective_id")
    gid = _safe_id(objective_generation_id, "objective_generation_id")
    driver_id = _driver_identity(updated_by, "updated_by")
    updated = _parse_time(updated_at).isoformat()
    authority_fields = _driver_authority_fields(driver_id, updated, root)
    records = objective_record_map(root)
    candidate = records.get(gid)
    if candidate is None or candidate.get("objective_id") != oid:
        raise ObjectiveRecordError("objective head candidate is unknown for objective_id")
    path = objective_head_path(oid, root)
    current = _load_json(path) if path.exists() else None
    actual_previous = current.get("objective_generation_id") if current else None
    if actual_previous != expected_previous_generation_id:
        raise ObjectiveRecordError(
            f"objective head CAS mismatch: expected {expected_previous_generation_id!r}, current {actual_previous!r}"
        )
    if candidate.get("previous_objective_generation_id") != expected_previous_generation_id:
        raise ObjectiveRecordError(
            "candidate generation was not created from the expected current objective head; create a new generation instead of rolling back"
        )
    record_path = objective_generation_path(oid, gid, root)
    head = {
        "record_schema": HEAD_SCHEMA,
        "objective_id": oid,
        "objective_generation_id": gid,
        "generation": candidate.get("generation"),
        "objective_status": candidate.get("objective_status"),
        "previous_objective_generation_id": expected_previous_generation_id,
        "objective_record_sha256": _sha256(record_path),
        "updated_by": driver_id,
        "updated_at": updated,
        **authority_fields,
        "authority": "OPERATIONAL_OBJECTIVE_CONTROL_ONLY",
        "retained_non_head_generations_rejected": False,
        "working_truth_granted": False,
        "foundation_authority_granted": False,
        "canonical_promotion_granted": False,
    }
    _atomic_replace_json(path, head)
    return head


def create_and_select(
    *,
    expected_previous_generation_id: str | None,
    root: Path = ROOT,
    **kwargs: Any,
) -> tuple[dict[str, Any], dict[str, Any]]:
    generation = build_generation(root=root, **kwargs)
    write_generation(generation, root)
    head = select_head(
        objective_id=generation["objective_id"],
        objective_generation_id=generation["objective_generation_id"],
        expected_previous_generation_id=expected_previous_generation_id,
        updated_by=generation["publisher_id"],
        updated_at=generation["created_at"],
        root=root,
    )
    return generation, head


def _task_record(task_id: str, publication_id: str, root: Path) -> dict[str, Any]:
    matches = [
        item
        for item in research_task_records.iter_records(root)
        if item.get("task_id") == task_id and item.get("publication_id") == publication_id
    ]
    if len(matches) != 1:
        raise ObjectiveRecordError("task publication is unknown or ambiguous")
    return matches[0]


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
    oid = _safe_id(objective_id, "objective_id")
    if task.get("parent_objective_id") != oid:
        raise ObjectiveRecordError("objective_id differs from task publication parent_objective_id")
    objective = objective_record_map(root).get(objective_generation_id)
    if objective is None or objective.get("objective_id") != oid:
        raise ObjectiveRecordError("objective generation is unknown for objective_id")
    if objective.get("objective_status") != "OPEN":
        raise ObjectiveRecordError("historical task binding requires an OPEN objective generation")
    driver_id = _driver_identity(bound_by, "bound_by")
    bound = _parse_time(bound_at).isoformat()
    authority_fields = _driver_authority_fields(driver_id, bound, root)
    objective_path = objective_generation_path(oid, objective_generation_id, root)
    value = {
        "record_schema": BINDING_SCHEMA,
        "task_id": task_id,
        "publication_id": publication_id,
        "taskbook_path": task.get("taskbook_path"),
        "taskbook_blob_sha1": task.get("taskbook_blob_sha1"),
        "objective_id": oid,
        "objective_generation_id": objective_generation_id,
        "objective_record_sha256": _sha256(objective_path),
        "bound_by": driver_id,
        "bound_at": bound,
        **authority_fields,
        "binding_authority": "EXACT_TASK_PUBLICATION_TO_IMMUTABLE_OBJECTIVE_GENERATION",
        "working_truth_granted": False,
        "foundation_authority_granted": False,
        "final_permission_granted": False,
    }
    path = task_binding_path(task_id, publication_id, root)
    _exclusive_json(path, value)
    return value


def iter_bindings(root: Path = ROOT) -> list[dict[str, Any]]:
    directory = root / "research_task_objective_bindings"
    if not directory.exists():
        return []
    out: list[dict[str, Any]] = []
    for path in sorted(directory.glob("*/*.json")):
        value = _load_json(path)
        value["_binding_path"] = path.relative_to(root).as_posix()
        out.append(value)
    return out


def binding_map(root: Path = ROOT) -> dict[tuple[str, str], dict[str, Any]]:
    out: dict[tuple[str, str], dict[str, Any]] = {}
    for item in iter_bindings(root):
        key = (str(item.get("task_id")), str(item.get("publication_id")))
        if key in out:
            raise ObjectiveRecordError(f"duplicate task objective binding: {key}")
        out[key] = item
    return out


def resolve_task_parent_binding(
    task_record: Mapping[str, Any], root: Path = ROOT
) -> dict[str, Any]:
    task_id = task_record.get("task_id")
    publication_id = task_record.get("publication_id")
    objective_id = task_record.get("parent_objective_id")
    direct_generation = task_record.get("parent_objective_generation_id")
    if not all(isinstance(value, str) and value for value in (task_id, publication_id, objective_id)):
        raise ObjectiveRecordError("task publication lacks task/publication/parent objective identity")
    records = objective_record_map(root)
    if isinstance(direct_generation, str) and direct_generation:
        objective = records.get(direct_generation)
        if objective is None or objective.get("objective_id") != objective_id:
            raise ObjectiveRecordError("direct parent objective generation is unavailable or mismatched")
        return {
            "binding_source": "TASK_PUBLICATION_DIRECT",
            "task_id": task_id,
            "publication_id": publication_id,
            "objective_id": objective_id,
            "objective_generation_id": direct_generation,
            "objective": objective,
        }
    sidecar = binding_map(root).get((task_id, publication_id))
    if sidecar is None:
        return {
            "binding_source": "LEGACY_UNBOUND",
            "task_id": task_id,
            "publication_id": publication_id,
            "objective_id": objective_id,
            "objective_generation_id": None,
            "objective": None,
        }
    objective = records.get(str(sidecar.get("objective_generation_id")))
    if objective is None or objective.get("objective_id") != objective_id:
        raise ObjectiveRecordError("sidecar objective generation is unavailable or mismatched")
    return {
        "binding_source": "IMMUTABLE_LEGACY_SIDECAR",
        "task_id": task_id,
        "publication_id": publication_id,
        "objective_id": objective_id,
        "objective_generation_id": sidecar.get("objective_generation_id"),
        "objective": objective,
        "binding": sidecar,
    }


def audit(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    try:
        records = objective_record_map(root)
        heads = head_map(root)
        bindings = binding_map(root)
    except Exception as exc:
        return [str(exc)]

    for gid, item in records.items():
        prefix = item.get("_record_path", gid)
        if item.get("record_schema") != OBJECTIVE_SCHEMA:
            errors.append(f"{prefix}: wrong objective record schema")
        if item.get("objective_status") not in STATUSES:
            errors.append(f"{prefix}: invalid objective_status")
        if item.get("publisher_role") != PUBLISHER_ROLE:
            errors.append(f"{prefix}: publisher_role must be RESEARCH_DRIVER")
        try:
            _driver_identity(str(item.get("publisher_id", "")), "publisher_id")
        except Exception as exc:
            errors.append(f"{prefix}: {exc}")
        for field in ("working_truth_granted", "foundation_authority_granted", "canonical_promotion_granted"):
            if item.get(field) is not False:
                errors.append(f"{prefix}: {field} must be false")
        generation = item.get("generation")
        if type(generation) is not int or generation <= 0:
            errors.append(f"{prefix}: generation must be positive integer")
            continue
        previous_id = item.get("previous_objective_generation_id")
        if previous_id is None:
            if generation != 1 or item.get("objective_status") != "OPEN":
                errors.append(f"{prefix}: initial generation must be generation=1 OPEN")
        else:
            previous = records.get(str(previous_id))
            if previous is None:
                errors.append(f"{prefix}: previous objective generation missing")
            else:
                if previous.get("objective_id") != item.get("objective_id"):
                    errors.append(f"{prefix}: previous generation belongs to another objective")
                if generation != int(previous.get("generation", -1)) + 1:
                    errors.append(f"{prefix}: generation is not previous+1")
                if previous.get("objective_status") == "CLOSED" and item.get("objective_status") == "OPEN":
                    if not isinstance(item.get("reopen_reason"), str) or not item["reopen_reason"].strip():
                        errors.append(f"{prefix}: CLOSED -> OPEN missing reopen_reason")
        if item.get("objective_status") == "CLOSED":
            if not isinstance(item.get("disposition_reason"), str) or not item["disposition_reason"].strip():
                errors.append(f"{prefix}: CLOSED missing disposition_reason")
            refs = item.get("closure_evidence_refs")
            if not isinstance(refs, list) or not refs or any(not isinstance(x, str) or not x.strip() for x in refs):
                errors.append(f"{prefix}: CLOSED requires closure_evidence_refs")

    for oid, head in heads.items():
        prefix = head.get("_head_path", oid)
        if head.get("record_schema") != HEAD_SCHEMA:
            errors.append(f"{prefix}: wrong objective head schema")
        candidate = records.get(str(head.get("objective_generation_id")))
        if candidate is None or candidate.get("objective_id") != oid:
            errors.append(f"{prefix}: head candidate missing or objective mismatch")
            continue
        if head.get("generation") != candidate.get("generation"):
            errors.append(f"{prefix}: head generation mismatch")
        if head.get("objective_status") != candidate.get("objective_status"):
            errors.append(f"{prefix}: head objective_status mismatch")
        if head.get("previous_objective_generation_id") != candidate.get("previous_objective_generation_id"):
            errors.append(f"{prefix}: head previous generation mismatch")
        record_path = objective_generation_path(oid, candidate["objective_generation_id"], root)
        if head.get("objective_record_sha256") != _sha256(record_path):
            errors.append(f"{prefix}: objective record digest drift")
        if head.get("retained_non_head_generations_rejected") is not False:
            errors.append(f"{prefix}: head may not reject retained generations")
        for field in ("working_truth_granted", "foundation_authority_granted", "canonical_promotion_granted"):
            if head.get(field) is not False:
                errors.append(f"{prefix}: {field} must be false")

    task_records = {
        (str(item.get("task_id")), str(item.get("publication_id"))): item
        for item in research_task_records.iter_records(root)
        if isinstance(item.get("task_id"), str) and isinstance(item.get("publication_id"), str)
    }
    for key, binding in bindings.items():
        prefix = binding.get("_binding_path", str(key))
        if binding.get("record_schema") != BINDING_SCHEMA:
            errors.append(f"{prefix}: wrong task-objective binding schema")
        task = task_records.get(key)
        if task is None:
            errors.append(f"{prefix}: bound task publication missing")
            continue
        if binding.get("taskbook_path") != task.get("taskbook_path"):
            errors.append(f"{prefix}: taskbook path differs from task publication")
        if binding.get("taskbook_blob_sha1") != task.get("taskbook_blob_sha1"):
            errors.append(f"{prefix}: taskbook blob differs from task publication")
        if binding.get("objective_id") != task.get("parent_objective_id"):
            errors.append(f"{prefix}: objective_id differs from task parent_objective_id")
        objective = records.get(str(binding.get("objective_generation_id")))
        if objective is None or objective.get("objective_id") != binding.get("objective_id"):
            errors.append(f"{prefix}: bound objective generation missing or mismatched")
            continue
        if objective.get("objective_status") != "OPEN":
            errors.append(f"{prefix}: historical task binding must target OPEN objective generation")
        record_path = objective_generation_path(
            str(binding.get("objective_id")),
            str(binding.get("objective_generation_id")),
            root,
        )
        if binding.get("objective_record_sha256") != _sha256(record_path):
            errors.append(f"{prefix}: objective record digest drift")
        for field in ("working_truth_granted", "foundation_authority_granted", "final_permission_granted"):
            if binding.get(field) is not False:
                errors.append(f"{prefix}: {field} must be false")

    try:
        errors.extend(research_objective_driver_authority.audit(root))
    except Exception as exc:
        errors.append(f"Objective Driver authority audit failed: {exc}")
    return errors


def _payload(args: argparse.Namespace) -> dict[str, Any]:
    if args.payload_json:
        value = json.loads(args.payload_json)
    else:
        value = json.loads(Path(args.payload_file).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ObjectiveRecordError("objective payload must be a JSON object")
    return value


def command_create(args: argparse.Namespace) -> int:
    payload = _payload(args)
    previous = args.expected_previous_generation_id
    generation, head = create_and_select(
        expected_previous_generation_id=previous,
        root=ROOT,
        objective_id=payload["objective_id"],
        objective_status=payload["objective_status"],
        title=payload["title"],
        scope=payload["scope"],
        success_criteria=payload["success_criteria"],
        closure_criteria=payload["closure_criteria"],
        research_value=payload["research_value"],
        publisher_id=payload["publisher_id"],
        created_at=_now(payload.get("created_at")),
        disposition_reason=payload.get("disposition_reason"),
        closure_evidence_refs=payload.get("closure_evidence_refs"),
        reopen_reason=payload.get("reopen_reason"),
    )
    print(json.dumps({"generation": generation, "head": head}, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


def command_bind(args: argparse.Namespace) -> int:
    value = bind_historical_task(
        task_id=args.task_id,
        publication_id=args.publication_id,
        objective_id=args.objective_id,
        objective_generation_id=args.objective_generation_id,
        bound_by=args.bound_by,
        bound_at=_now(args.bound_at),
    )
    print(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


def command_audit(args: argparse.Namespace) -> int:
    errors = audit()
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print(
        f"PASS: objective generations valid ({len(iter_objective_records())} generation(s), "
        f"{len(iter_heads())} operational head(s), {len(iter_bindings())} legacy task binding(s))."
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Enterprise Math immutable objective generation registry")
    sub = parser.add_subparsers(dest="command", required=True)
    create = sub.add_parser("create-and-select")
    group = create.add_mutually_exclusive_group(required=True)
    group.add_argument("--payload-json")
    group.add_argument("--payload-file")
    create.add_argument("--expected-previous-generation-id")
    create.set_defaults(func=command_create)
    bind = sub.add_parser("bind-historical-task")
    bind.add_argument("--task-id", required=True)
    bind.add_argument("--publication-id", required=True)
    bind.add_argument("--objective-id", required=True)
    bind.add_argument("--objective-generation-id", required=True)
    bind.add_argument("--bound-by", required=True)
    bind.add_argument("--bound-at")
    bind.set_defaults(func=command_bind)
    audit_parser = sub.add_parser("audit")
    audit_parser.set_defaults(func=command_audit)
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ObjectiveRecordError as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
