#!/usr/bin/env python3
"""Immutable post-cutover task publication records."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import tempfile
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from tools import research_taskbook
except ModuleNotFoundError:
    import research_taskbook  # type: ignore

ROOT = Path(__file__).resolve().parents[1]
RECORD_SCHEMA = "ENTERPRISE_MATH_TASK_PUBLICATION_RECORD_V2"
TASKBOOK_PUBLICATION_CONTRACT = "RESEARCH_TASK_PUBLICATION_V1"
TASKBOOK_TEMPLATE = "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1"
PUBLICATION_TRANSACTION_V2 = "RESEARCH_TASK_IMMUTABLE_PUBLICATION_V2"
RESOLUTION_SCHEMA = "ENTERPRISE_MATH_TASK_PUBLICATION_RESOLUTION_REGISTRY_V1"
RESOLUTION_FILE = "research_task_publication_resolutions.json"
PUBLISHER_ROLES = {"RESEARCHER", "RESEARCH_DRIVER", "FOUNDATION_STEWARD"}
MANDATORY_BODY_SECTIONS = (
    "Mother question",
    "Frozen inputs and scope",
    "Hard target and required outputs",
    "Research value to preserve",
    "Success, kill, and return criteria",
)
TERMINAL_RECORD_STATES = {"PARKED", "SUPERSEDED", "CLOSED"}
_PLACEHOLDER = re.compile(r"^\s*<[^>\n]+>\s*$", re.MULTILINE)


class TaskRecordError(ValueError):
    pass


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def git_blob_sha1_bytes(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return "sha1:" + hashlib.sha1(header + data).hexdigest()


def taskbook_blob(path: Path) -> str:
    return git_blob_sha1_bytes(path.read_bytes())


def _safe_task_id(task_id: str) -> str:
    if not re.fullmatch(r"[A-Za-z0-9._-]+", task_id):
        raise TaskRecordError("task_id contains unsupported characters")
    return task_id


def _parse_time(value: str) -> datetime:
    dt = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _now(value: str | None) -> str:
    return (_parse_time(value) if value else datetime.now(timezone.utc)).isoformat()


def publication_id(task_id: str, blob: str, publisher_id: str, parent: str) -> str:
    raw = "\0".join((task_id, blob, publisher_id, parent)).encode("utf-8")
    return "TP2-" + hashlib.sha256(raw).hexdigest()[:20].upper()


def _save_json_exclusive(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(value, ensure_ascii=False, indent=2) + "\n"
    try:
        with path.open("x", encoding="utf-8") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
    except FileExistsError as exc:
        raise TaskRecordError(f"immutable record already exists: {path}") from exc


def record_path(root: Path, task_id: str, pub_id: str) -> Path:
    return root / "research_task_records" / _safe_task_id(task_id) / f"{pub_id}.json"


def iter_records(root: Path = ROOT) -> list[dict[str, Any]]:
    directory = root / "research_task_records"
    if not directory.exists():
        return []
    out: list[dict[str, Any]] = []
    for path in sorted(directory.glob("*/*.json")):
        value = _load_json(path)
        value["_record_path"] = path.relative_to(root).as_posix()
        out.append(value)
    return out


def publication_resolutions(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    path = root / RESOLUTION_FILE
    if not path.exists():
        return {}
    payload = _load_json(path)
    if payload.get("schema") != RESOLUTION_SCHEMA:
        raise TaskRecordError(f"{RESOLUTION_FILE}: wrong schema")
    if payload.get("status") != "ACTIVE":
        raise TaskRecordError(f"{RESOLUTION_FILE}: status must be ACTIVE")
    rows = payload.get("resolutions")
    if not isinstance(rows, list):
        raise TaskRecordError(f"{RESOLUTION_FILE}: resolutions must be a list")
    out: dict[str, dict[str, Any]] = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise TaskRecordError(f"{RESOLUTION_FILE}: resolution {index} must be an object")
        task_id = row.get("task_id")
        canonical = row.get("canonical_publication_id")
        quarantined = row.get("quarantined_publication_ids")
        if not isinstance(task_id, str) or not task_id:
            raise TaskRecordError(f"{RESOLUTION_FILE}: resolution {index} missing task_id")
        if task_id in out:
            raise TaskRecordError(f"{RESOLUTION_FILE}: duplicate resolution for {task_id}")
        if not isinstance(canonical, str) or not canonical:
            raise TaskRecordError(f"{RESOLUTION_FILE}: {task_id} missing canonical_publication_id")
        if not isinstance(quarantined, list) or not all(isinstance(item, str) and item for item in quarantined):
            raise TaskRecordError(f"{RESOLUTION_FILE}: {task_id} quarantined_publication_ids invalid")
        if canonical in quarantined:
            raise TaskRecordError(f"{RESOLUTION_FILE}: {task_id} canonical head cannot be quarantined")
        if row.get("working_truth_granted") is not False:
            raise TaskRecordError(f"{RESOLUTION_FILE}: {task_id} resolution cannot grant Working Truth")
        if row.get("canonical_promotion_granted") is not False:
            raise TaskRecordError(f"{RESOLUTION_FILE}: {task_id} resolution cannot grant canonical promotion")
        if row.get("successor_triggered") is not False:
            raise TaskRecordError(f"{RESOLUTION_FILE}: {task_id} resolution cannot trigger successor research")
        out[task_id] = row
    return out


def current_records(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in iter_records(root):
        task_id = record.get("task_id")
        if isinstance(task_id, str):
            grouped[task_id].append(record)
    resolutions = publication_resolutions(root)
    unknown_resolutions = sorted(set(resolutions) - set(grouped))
    if unknown_resolutions:
        raise TaskRecordError(
            f"publication resolution references unknown task(s): {unknown_resolutions}"
        )
    current: dict[str, dict[str, Any]] = {}
    for task_id, values in grouped.items():
        superseded = {
            item.get("supersedes_publication_id")
            for item in values
            if item.get("supersedes_publication_id")
        }
        heads = [
            item
            for item in values
            if item.get("publication_id") not in superseded
            and item.get("record_state", "ACTIVE") not in TERMINAL_RECORD_STATES
        ]
        resolution = resolutions.get(task_id)
        if len(heads) > 1:
            if resolution is None:
                raise TaskRecordError(
                    f"publication fork for {task_id}: "
                    f"{[item.get('publication_id') for item in heads]}"
                )
            head_by_id = {str(item.get("publication_id")): item for item in heads}
            canonical = str(resolution["canonical_publication_id"])
            quarantined = set(resolution["quarantined_publication_ids"])
            if canonical not in head_by_id:
                raise TaskRecordError(
                    f"publication resolution for {task_id} selects non-head {canonical}"
                )
            unresolved = set(head_by_id) - {canonical} - quarantined
            missing_quarantine = quarantined - set(head_by_id)
            if unresolved:
                raise TaskRecordError(
                    f"publication resolution for {task_id} leaves unresolved heads: {sorted(unresolved)}"
                )
            if missing_quarantine:
                raise TaskRecordError(
                    f"publication resolution for {task_id} quarantines non-heads: {sorted(missing_quarantine)}"
                )
            current[task_id] = head_by_id[canonical]
            continue
        if heads:
            if resolution is not None and resolution.get("canonical_publication_id") != heads[0].get("publication_id"):
                raise TaskRecordError(
                    f"stale publication resolution for {task_id}: canonical head no longer matches"
                )
            current[task_id] = heads[0]
    return current


def _section_payloads(body: str) -> dict[str, str]:
    lines = body.splitlines()
    hits: list[tuple[int, str]] = []
    for index, line in enumerate(lines):
        if not line.lstrip().startswith("##"):
            continue
        for required in MANDATORY_BODY_SECTIONS:
            if required.lower() in line.lower():
                hits.append((index, required))
                break
    hits.sort()
    out: dict[str, str] = {}
    for pos, (index, name) in enumerate(hits):
        end = hits[pos + 1][0] if pos + 1 < len(hits) else len(lines)
        out[name] = "\n".join(lines[index + 1 : end]).strip()
    return out


def validate_body(body: str) -> list[str]:
    errors: list[str] = []
    payloads = _section_payloads(body)
    for section in MANDATORY_BODY_SECTIONS:
        payload = payloads.get(section, "")
        if not payload:
            errors.append(f"mandatory body section is missing or empty: {section}")
        elif _PLACEHOLDER.search(payload):
            errors.append(f"mandatory body section contains placeholder text: {section}")
    return errors


def _prepared(path: Path, root: Path = ROOT) -> tuple[dict[str, Any], str]:
    meta, body = research_taskbook.split_taskbook(path.read_text(encoding="utf-8"))
    expected = {
        "task_authority": "PUBLISHED_REGISTERED",
        "publication_contract": TASKBOOK_PUBLICATION_CONTRACT,
        "publication_template": TASKBOOK_TEMPLATE,
        "registry_key": meta.get("task_id"),
        "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
        "final_response_identity_policy": "INHERIT_GLOBAL",
    }
    for field, value in expected.items():
        if meta.get(field) != value:
            raise TaskRecordError(f"taskbook not prepared: {field} must equal {value!r}")
    if not isinstance(meta.get("parent_objective_id"), str) or not meta["parent_objective_id"].strip():
        raise TaskRecordError("parent_objective_id is required")
    if not isinstance(meta.get("frontier"), str) or not meta["frontier"].strip():
        raise TaskRecordError("frontier is required")
    if not isinstance(meta.get("next_action"), str) or not meta["next_action"].strip():
        raise TaskRecordError("next_action is required")
    body_errors = validate_body(body)
    if body_errors:
        raise TaskRecordError("; ".join(body_errors))
    review = meta.get("policy_review")
    if (
        not isinstance(review, dict)
        or review.get("review_state") != "PASS"
        or review.get("policy_digest") != research_taskbook.policy_digest(root)
    ):
        raise TaskRecordError("taskbook requires current machine policy PASS")
    findings = research_taskbook.audit_taskbook(path, root=root, dispatch=True)
    hard = [item for item in findings if item["severity"] == "ERROR"]
    if hard:
        raise TaskRecordError(
            "taskbook lint failed: "
            + "; ".join(f"{item['code']}:{item['message']}" for item in hard)
        )
    return meta, body


def prepare_taskbook(
    path: Path, *, publisher_role: str, parent_objective_id: str, root: Path = ROOT
) -> dict[str, Any]:
    if publisher_role not in PUBLISHER_ROLES:
        raise TaskRecordError(f"unsupported publisher role: {publisher_role}")
    meta, body = research_taskbook.split_taskbook(path.read_text(encoding="utf-8"))
    body_errors = validate_body(body)
    if body_errors:
        raise TaskRecordError("; ".join(body_errors))
    prepared = dict(meta)
    prepared.update(
        {
            "created_by_role": publisher_role,
            "task_authority": "PUBLISHED_REGISTERED",
            "publication_contract": TASKBOOK_PUBLICATION_CONTRACT,
            "publication_template": TASKBOOK_TEMPLATE,
            "registry_key": meta.get("task_id"),
            "parent_objective_id": parent_objective_id,
            "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
            "final_response_identity_policy": "INHERIT_GLOBAL",
        }
    )
    if prepared.get("base_state") in {None, "DRAFT", "BACKLOG"}:
        prepared["base_state"] = "READY"
    review = prepared.get("policy_review")
    if not isinstance(review, dict):
        review = {"temporary_overrides": []}
    review = dict(review)
    review["policy_set"] = "research_taskbook_policy.json"
    review["policy_digest"] = research_taskbook.policy_digest(root)
    review["review_state"] = "PENDING_POLICY_REVIEW"
    review.setdefault("temporary_overrides", [])
    prepared["policy_review"] = review

    with tempfile.TemporaryDirectory() as td:
        candidate = Path(td) / path.name
        candidate.write_text(
            research_taskbook.render_taskbook(prepared, body), encoding="utf-8"
        )
        first = research_taskbook.audit_taskbook(candidate, root=root, dispatch=False)
        hard = [item for item in first if item["severity"] == "ERROR"]
        if hard:
            raise TaskRecordError(
                "machine review failed: "
                + "; ".join(f"{item['code']}:{item['message']}" for item in hard)
            )
        prepared["policy_review"]["review_state"] = "PASS"
        candidate.write_text(
            research_taskbook.render_taskbook(prepared, body), encoding="utf-8"
        )
        final = research_taskbook.audit_taskbook(candidate, root=root, dispatch=True)
        hard = [item for item in final if item["severity"] == "ERROR"]
        if hard:
            raise TaskRecordError(
                "post-review lint failed: "
                + "; ".join(f"{item['code']}:{item['message']}" for item in hard)
            )
        final_text = candidate.read_text(encoding="utf-8")

    temp = path.with_suffix(path.suffix + ".prepare-tmp")
    temp.write_text(final_text, encoding="utf-8")
    os.replace(temp, path)
    return prepared


def build_record(
    meta: dict[str, Any],
    *,
    path: Path,
    publisher_role: str,
    publisher_id: str,
    research_value: str,
    published_at: str,
    supersedes_publication_id: str | None,
    root: Path = ROOT,
) -> dict[str, Any]:
    if publisher_role not in PUBLISHER_ROLES:
        raise TaskRecordError("invalid publisher role")
    if not publisher_id.strip() or not research_value.strip():
        raise TaskRecordError("publisher_id and research_value are required")
    task_id = _safe_task_id(str(meta["task_id"]))
    existing = [item for item in iter_records(root) if item.get("task_id") == task_id]
    if existing and not supersedes_publication_id:
        raise TaskRecordError(
            "task already published; explicit supersedes_publication_id is required"
        )
    if supersedes_publication_id and supersedes_publication_id not in {
        item.get("publication_id") for item in existing
    }:
        raise TaskRecordError("supersedes_publication_id is not an existing generation")
    generation = (
        max(int(item.get("publication_generation", 1)) for item in existing) + 1
        if existing
        else 1
    )
    if publisher_role == "RESEARCHER":
        priority, leverage, source = "P2", "MEDIUM", "RESEARCHER_DEFAULT"
    else:
        priority = str(meta.get("priority") or "P2").upper()
        leverage = str(meta.get("leverage") or "MEDIUM").upper()
        source = "PUBLISHER_DECLARED"
    blob = taskbook_blob(path)
    pub_id = publication_id(task_id, blob, publisher_id, meta["parent_objective_id"])
    return {
        "record_schema": RECORD_SCHEMA,
        "record_state": "ACTIVE",
        "task_id": task_id,
        "registry_key": task_id,
        "publication_id": pub_id,
        "publication_generation": generation,
        "supersedes_publication_id": supersedes_publication_id,
        "publication_contract": TASKBOOK_PUBLICATION_CONTRACT,
        "template_version": TASKBOOK_TEMPLATE,
        "publication_transaction": PUBLICATION_TRANSACTION_V2,
        "taskbook_path": path.relative_to(root).as_posix(),
        "taskbook_blob_sha1": blob,
        "publisher_role": publisher_role,
        "publisher_id": publisher_id,
        "published_at": published_at,
        "parent_objective_id": meta["parent_objective_id"],
        "origin_kind": meta.get("origin_kind"),
        "origin_candidate_id": meta.get("origin_candidate_id"),
        "origin_candidate_state": meta.get("origin_candidate_state"),
        "kind": meta.get("kind", "RESEARCH"),
        "task_lineage": meta.get("task_lineage"),
        "parent_task_id": meta.get("parent_task_id"),
        "claimable": True,
        "effective_priority": priority,
        "effective_leverage": leverage,
        "priority_source": source,
        "publisher_priority_request": meta.get("priority"),
        "publisher_leverage_request": meta.get("leverage"),
        "owner": meta.get("owner"),
        "frontier": meta.get("frontier"),
        "next_action": meta.get("next_action"),
        "research_value": research_value,
        "terminal_scope": "TASK",
        "working_truth_granted": False,
        "canonical_promotion_granted": False,
    }


def audit(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    try:
        all_records = iter_records(root)
        current_records(root)
    except Exception as exc:
        return [str(exc)]
    task_ids: set[str] = set()
    publications: set[str] = set()
    for item in all_records:
        prefix = item.get("_record_path", "<record>")
        if item.get("record_schema") != RECORD_SCHEMA:
            errors.append(f"{prefix}: wrong record_schema")
        task_id = item.get("task_id")
        pub_id = item.get("publication_id")
        if not isinstance(task_id, str) or not task_id:
            errors.append(f"{prefix}: missing task_id")
            continue
        task_ids.add(task_id)
        if not isinstance(pub_id, str) or not pub_id:
            errors.append(f"{prefix}: missing publication_id")
        elif pub_id in publications:
            errors.append(f"{prefix}: duplicate publication_id")
        publications.add(pub_id)
        if item.get("registry_key") != task_id:
            errors.append(f"{prefix}: registry_key mismatch")
        if item.get("working_truth_granted") is not False:
            errors.append(f"{prefix}: publication cannot grant Working Truth")
        if item.get("canonical_promotion_granted") is not False:
            errors.append(f"{prefix}: publication cannot grant canonical promotion")
        path_value = item.get("taskbook_path")
        if not isinstance(path_value, str):
            errors.append(f"{prefix}: missing taskbook_path")
            continue
        path = root / path_value
        if not path.exists():
            errors.append(f"{prefix}: taskbook path missing")
            continue
        if taskbook_blob(path) != item.get("taskbook_blob_sha1"):
            errors.append(f"{prefix}: taskbook blob drift")
        try:
            meta, body = research_taskbook.split_taskbook(path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"{prefix}: taskbook parse failed: {exc}")
            continue
        if meta.get("task_id") != task_id:
            errors.append(f"{prefix}: taskbook task_id mismatch")
        if meta.get("parent_objective_id") != item.get("parent_objective_id"):
            errors.append(f"{prefix}: parent objective mismatch")
        if item.get("publication_transaction") == PUBLICATION_TRANSACTION_V2:
            errors.extend(f"{prefix}: {msg}" for msg in validate_body(body))

    task_dir = root / "research_tasks"
    if task_dir.exists():
        for path in sorted(task_dir.glob("*.md")):
            try:
                meta, _ = research_taskbook.split_taskbook(path.read_text(encoding="utf-8"))
            except Exception:
                continue
            if (
                meta.get("task_authority") == "PUBLISHED_REGISTERED"
                and meta.get("base_state") not in {"DRAFT", "BACKLOG"}
                and meta.get("task_id") not in task_ids
            ):
                errors.append(
                    f"{path.relative_to(root)}: published taskbook has no immutable publication record"
                )
    return errors


def _taskbook_path(value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else ROOT / path


def command_new(args: argparse.Namespace) -> int:
    path = _taskbook_path(args.output)
    if path.exists():
        raise TaskRecordError(f"refusing to overwrite {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    successor = None
    if args.lineage == "CONTINUATION":
        if not args.parent_task_id:
            raise TaskRecordError("CONTINUATION requires --parent-task-id")
        successor = {
            "new_information_gap": "",
            "why_parent_result_does_not_close_it": "",
            "discriminating_outcomes": [],
            "kill_condition": "",
            "alternative_route_or_free_exploration_considered": "",
            "why_new_stage_or_task_is_better_than_same_task_or_closure": "",
        }
    meta = {
        "task_id": args.task_id,
        "title": args.title,
        "kind": args.kind,
        "owner": args.owner,
        "base_state": "DRAFT",
        "priority": args.priority,
        "leverage": args.leverage,
        "frontier": "",
        "next_action": "",
        "dependencies": [],
        "source_refs": [],
        "evidence_status": "TASKBOOK_DRAFT_V2",
        "last_progress_ref": None,
        "last_progress_at": None,
        "hard_block": None,
        "tags": [],
        "claim_lease_minutes": args.claim_lease_minutes,
        "created_by_role": args.publisher_role,
        "task_authority": "PENDING_PUBLICATION",
        "publication_contract": TASKBOOK_PUBLICATION_CONTRACT,
        "publication_template": TASKBOOK_TEMPLATE,
        "registry_key": args.task_id,
        "parent_objective_id": args.parent_objective_id,
        "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
        "final_response_identity_policy": "INHERIT_GLOBAL",
        "identity_lane": args.lane,
        "origin_kind": args.origin_kind,
        "task_lineage": args.lineage,
        "parent_task_id": args.parent_task_id,
        "successor_gate": successor,
        "policy_review": {
            "policy_set": "research_taskbook_policy.json",
            "policy_digest": research_taskbook.policy_digest(ROOT),
            "review_state": "PENDING_POLICY_REVIEW",
            "temporary_overrides": [],
        },
    }
    body = f"""# {args.title}

Status: `DRAFT / UNPUBLISHED / NOT CLAIMABLE`

## 0. Mother question

<replace with one exact task-local mother question>

## 1. Frozen inputs and scope

<replace with exact source pins, assumptions, allowed reads, and exclusions>

## 2. Hard target and required outputs

<replace with exact theorem/counterexample/computation/formalization/audit target>

## 3. Research value to preserve

<replace with why this task remains worth preserving even if not immediately selected>

## 4. Success, kill, and return criteria

<replace with exact success, kill/no-go, frozen-return, and stop criteria>
"""
    path.write_text(research_taskbook.render_taskbook(meta, body), encoding="utf-8")
    print(path.relative_to(ROOT).as_posix())
    return 0


def command_prepare(args: argparse.Namespace) -> int:
    meta = prepare_taskbook(
        _taskbook_path(args.taskbook),
        publisher_role=args.publisher_role,
        parent_objective_id=args.parent_objective_id,
    )
    print(json.dumps(meta, ensure_ascii=False, indent=2))
    return 0


def command_publish(args: argparse.Namespace) -> int:
    path = _taskbook_path(args.taskbook)
    meta, _ = _prepared(path)
    if meta.get("created_by_role") != args.publisher_role:
        raise TaskRecordError("publisher role differs from prepared taskbook")
    record = build_record(
        meta,
        path=path,
        publisher_role=args.publisher_role,
        publisher_id=args.publisher_id,
        research_value=args.research_value,
        published_at=_now(args.published_at),
        supersedes_publication_id=args.supersedes_publication_id,
    )
    out = record_path(ROOT, record["task_id"], record["publication_id"])
    _save_json_exclusive(out, record)
    errors = audit()
    if errors:
        raise TaskRecordError(
            "immutable record created but repository audit failed: " + "; ".join(errors)
        )
    print(
        json.dumps(
            {**record, "record_path": out.relative_to(ROOT).as_posix()},
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


def command_audit(args: argparse.Namespace) -> int:
    errors = audit()
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print(
        f"PASS: immutable task publication records valid "
        f"({len(iter_records())} generations)."
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Enterprise Math immutable task publication V2"
    )
    sub = parser.add_subparsers(dest="command", required=True)
    new = sub.add_parser("new")
    new.add_argument("--task-id", required=True)
    new.add_argument("--title", required=True)
    new.add_argument("--publisher-role", choices=sorted(PUBLISHER_ROLES), required=True)
    new.add_argument("--parent-objective-id", required=True)
    new.add_argument("--kind", choices=["RESEARCH", "GOVERNANCE"], default="RESEARCH")
    new.add_argument("--owner", default="taskbook/unassigned")
    new.add_argument("--priority", default="P2")
    new.add_argument("--leverage", default="MEDIUM")
    new.add_argument("--lane", default="")
    new.add_argument("--origin-kind", default="DRIVER_ROADMAP")
    new.add_argument("--lineage", default="NEW_DIRECTION")
    new.add_argument("--parent-task-id")
    new.add_argument("--claim-lease-minutes", type=int, default=120)
    new.add_argument("--output", required=True)
    new.set_defaults(func=command_new)
    prepare = sub.add_parser("prepare")
    prepare.add_argument("--taskbook", required=True)
    prepare.add_argument("--publisher-role", choices=sorted(PUBLISHER_ROLES), required=True)
    prepare.add_argument("--parent-objective-id", required=True)
    prepare.set_defaults(func=command_prepare)
    publish = sub.add_parser("publish")
    publish.add_argument("--taskbook", required=True)
    publish.add_argument("--publisher-role", choices=sorted(PUBLISHER_ROLES), required=True)
    publish.add_argument("--publisher-id", required=True)
    publish.add_argument("--research-value", required=True)
    publish.add_argument("--published-at")
    publish.add_argument("--supersedes-publication-id")
    publish.set_defaults(func=command_publish)
    audit_parser = sub.add_parser("audit")
    audit_parser.set_defaults(func=command_audit)
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TaskRecordError as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
