#!/usr/bin/env python3
"""Unified task publication/registry gate for Enterprise Math.

Publication is a control-plane transaction: a taskbook is not an official task
until it is registered here. Researchers and Drivers use the same publication
record/template. Publication does not promote mathematical truth or Working Truth.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from tools import research_taskbook
except ModuleNotFoundError:  # direct script execution from tools/
    import research_taskbook  # type: ignore

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "research_task_registry.json"
CONTRACT_PATH = ROOT / "research_task_publication_contract.json"
TEMPLATE_PATH = ROOT / "templates" / "RESEARCH_TASK_PUBLICATION_TEMPLATE.json"

SCHEMA = "ENTERPRISE_MATH_RESEARCH_TASK_REGISTRY_V1"
PUBLICATION_CONTRACT = "RESEARCH_TASK_PUBLICATION_V1"
TEMPLATE_VERSION = "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1"
PUBLISHER_ROLES = {"RESEARCHER", "RESEARCH_DRIVER", "FOUNDATION_STEWARD"}
REGISTRY_STATES = {
    "REGISTERED", "CLAIMABLE", "CLAIMED", "IN_PROGRESS", "HANDOFF_READY",
    "BLOCKED", "FROZEN", "DONE", "PARKED", "SUPERSEDED",
}
RESEARCHER_DEFAULT_PRIORITY = "P2"
RESEARCHER_DEFAULT_LEVERAGE = "MEDIUM"


class RegistryError(ValueError):
    pass


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, value: dict[str, Any]) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def parse_time(value: str) -> datetime:
    normalized = value.strip().replace("Z", "+00:00")
    dt = datetime.fromisoformat(normalized)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def now_iso(value: str | None) -> str:
    return (parse_time(value) if value else datetime.now(timezone.utc)).isoformat()


def blob_sha1(path: Path) -> str:
    return "sha1:" + research_taskbook.git_blob_identity(path.read_bytes()).hex()


def publication_id(task_id: str, taskbook_blob: str, publisher_id: str, parent_objective_id: str) -> str:
    raw = "\0".join((task_id, taskbook_blob, publisher_id, parent_objective_id)).encode("utf-8")
    return "TP-" + hashlib.sha256(raw).hexdigest()[:16].upper()


def taskbook_path(value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else ROOT / path


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix() if path.is_relative_to(ROOT) else path.as_posix()


def effective_rank(meta: dict[str, Any], publisher_role: str) -> tuple[str, str, str]:
    requested_priority = str(meta.get("priority") or "P2").upper()
    requested_leverage = str(meta.get("leverage") or "MEDIUM").upper()
    if publisher_role == "RESEARCHER":
        return RESEARCHER_DEFAULT_PRIORITY, RESEARCHER_DEFAULT_LEVERAGE, "RESEARCHER_DEFAULT"
    if requested_priority not in {"P0", "P1", "P2", "P3"}:
        raise RegistryError("priority must be P0/P1/P2/P3")
    if requested_leverage not in {"HIGH", "MEDIUM", "LOW"}:
        raise RegistryError("leverage must be HIGH/MEDIUM/LOW")
    return requested_priority, requested_leverage, "PUBLISHER_DECLARED"


def validate_publication_origin(meta: dict[str, Any], publisher_role: str) -> None:
    origin = meta.get("origin_kind")
    if publisher_role == "RESEARCHER" and origin == "FREE_AXIOM_CANDIDATE":
        contract = load_json(ROOT / "research_taskbook_contract.json")
        allowed = set(contract["task_origin_contract"]["free_candidate_allowed_states"])
        if meta.get("origin_candidate_state") not in allowed or not meta.get("origin_candidate_id"):
            raise RegistryError(
                "free-research task publication requires an audited candidate id/state; "
                "raw Phase-A candidates cannot publish tasks"
            )


def publication_entry(
    meta: dict[str, Any],
    *,
    path: Path,
    publisher_role: str,
    publisher_id: str,
    parent_objective_id: str,
    research_value: str,
    published_at: str,
) -> dict[str, Any]:
    if publisher_role not in PUBLISHER_ROLES:
        raise RegistryError(f"publisher_role must be one of {sorted(PUBLISHER_ROLES)}")
    if not publisher_id.strip():
        raise RegistryError("publisher_id is required")
    if not parent_objective_id.strip():
        raise RegistryError("parent_objective_id is required; orphan tasks are forbidden")
    if not research_value.strip():
        raise RegistryError("research_value is required; preserve why this task is worth keeping")

    validate_publication_origin(meta, publisher_role)
    priority, leverage, priority_source = effective_rank(meta, publisher_role)
    task_blob = blob_sha1(path)
    task_id = str(meta.get("task_id") or "").strip()
    if not task_id:
        raise RegistryError("taskbook requires task_id")
    lineage = str(meta.get("task_lineage") or "").strip()
    if not lineage:
        raise RegistryError("taskbook requires task_lineage")
    return {
        "task_id": task_id,
        "registry_key": task_id,
        "publication_id": publication_id(task_id, task_blob, publisher_id, parent_objective_id),
        "publication_contract": PUBLICATION_CONTRACT,
        "template_version": TEMPLATE_VERSION,
        "taskbook_path": relative(path),
        "taskbook_blob_sha1": task_blob,
        "publisher_role": publisher_role,
        "publisher_id": publisher_id,
        "published_at": published_at,
        "parent_objective_id": parent_objective_id,
        "origin_kind": meta.get("origin_kind"),
        "kind": meta.get("kind", "RESEARCH"),
        "task_lineage": lineage,
        "parent_task_id": meta.get("parent_task_id"),
        "registry_state": "CLAIMABLE",
        "claimable": True,
        "effective_priority": priority,
        "effective_leverage": leverage,
        "priority_source": priority_source,
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


def registry_task_map(registry: dict[str, Any]) -> dict[str, dict[str, Any]]:
    items = registry.get("tasks", [])
    if not isinstance(items, list):
        raise RegistryError("registry.tasks must be an array")
    out: dict[str, dict[str, Any]] = {}
    for item in items:
        if not isinstance(item, dict) or not isinstance(item.get("task_id"), str):
            raise RegistryError("every registry task must be an object with task_id")
        if item["task_id"] in out:
            raise RegistryError(f"duplicate registry task_id: {item['task_id']}")
        out[item["task_id"]] = item
    return out


def audit_registry(*, root: Path = ROOT, strict: bool = True) -> list[str]:
    registry = load_json(root / "research_task_registry.json")
    errors: list[str] = []
    if registry.get("schema") != SCHEMA:
        errors.append("unexpected task registry schema")
    if registry.get("status") != "ACTIVE_CANONICAL_TASK_REGISTRY":
        errors.append("task registry must be ACTIVE_CANONICAL_TASK_REGISTRY")

    try:
        by_id = registry_task_map(registry)
    except RegistryError as exc:
        return [str(exc)]

    required = set(load_json(root / "research_task_publication_contract.json")["publication_record_required_fields"])
    for task_id, item in by_id.items():
        missing = sorted(field for field in required if field not in item or item[field] in (None, ""))
        if missing:
            errors.append(f"{task_id}: registry record missing {missing}")
            continue
        if item.get("publication_contract") != PUBLICATION_CONTRACT:
            errors.append(f"{task_id}: wrong publication_contract")
        if item.get("template_version") != TEMPLATE_VERSION:
            errors.append(f"{task_id}: wrong template_version")
        if item.get("publisher_role") not in PUBLISHER_ROLES:
            errors.append(f"{task_id}: invalid publisher_role")
        if item.get("registry_state") not in REGISTRY_STATES:
            errors.append(f"{task_id}: invalid registry_state")
        if item.get("terminal_scope") != "TASK":
            errors.append(f"{task_id}: published task terminal_scope must be TASK")
        if item.get("working_truth_granted") is not False:
            errors.append(f"{task_id}: publication may not grant Working Truth")
        if item.get("canonical_promotion_granted") is not False:
            errors.append(f"{task_id}: publication may not grant canonical promotion")
        if item.get("publisher_role") == "RESEARCHER":
            if item.get("effective_priority") != RESEARCHER_DEFAULT_PRIORITY:
                errors.append(f"{task_id}: researcher-published task effective_priority must default to P2")
            if item.get("effective_leverage") != RESEARCHER_DEFAULT_LEVERAGE:
                errors.append(f"{task_id}: researcher-published task effective_leverage must default to MEDIUM")

        p = root / item["taskbook_path"]
        if not p.exists():
            errors.append(f"{task_id}: registered taskbook path does not exist: {item['taskbook_path']}")
            continue
        try:
            meta, _ = research_taskbook.split_taskbook(p.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"{task_id}: taskbook parse failed: {exc}")
            continue
        if meta.get("task_id") != task_id:
            errors.append(f"{task_id}: taskbook task_id mismatch")
        if meta.get("publication_contract") != PUBLICATION_CONTRACT:
            errors.append(f"{task_id}: taskbook missing publication contract")
        if meta.get("registry_key") != task_id:
            errors.append(f"{task_id}: taskbook registry_key mismatch")
        if meta.get("task_authority") != "PUBLISHED_REGISTERED":
            errors.append(f"{task_id}: task_authority must be PUBLISHED_REGISTERED")
        if meta.get("parent_objective_id") != item.get("parent_objective_id"):
            errors.append(f"{task_id}: parent_objective_id mismatch")
        actual_blob = blob_sha1(p)
        if item.get("taskbook_blob_sha1") != actual_blob:
            errors.append(f"{task_id}: taskbook blob drift; republish or restore the pinned taskbook")

    current_digest = research_taskbook.policy_digest(root)
    task_dir = root / "research_tasks"
    if task_dir.exists():
        for p in sorted(task_dir.glob("*.md")):
            try:
                meta, _ = research_taskbook.split_taskbook(p.read_text(encoding="utf-8"))
            except Exception:
                continue
            review = meta.get("policy_review")
            current_pass = (
                isinstance(review, dict)
                and review.get("policy_digest") == current_digest
                and review.get("review_state") == "PASS"
                and meta.get("base_state") not in {"DRAFT", "BACKLOG"}
            )
            if current_pass:
                task_id = meta.get("task_id")
                if not isinstance(task_id, str) or task_id not in by_id:
                    errors.append(
                        f"{relative(p)}: current-policy dispatchable task is orphaned; "
                        "publish through the unified registry"
                    )

    if strict:
        template = root / "templates" / "RESEARCH_TASK_PUBLICATION_TEMPLATE.json"
        if not template.exists():
            errors.append("mandatory unified publication template missing")
        else:
            data = load_json(template)
            if data.get("schema") != TEMPLATE_VERSION:
                errors.append("publication template schema drift")
    return errors


def normalize_for_publication(
    path: Path,
    *,
    publisher_role: str,
    parent_objective_id: str,
) -> tuple[dict[str, Any], str]:
    meta, body = research_taskbook.split_taskbook(path.read_text(encoding="utf-8"))
    meta["created_by_role"] = publisher_role
    meta["task_authority"] = "PUBLISHED_REGISTERED"
    meta["publication_contract"] = PUBLICATION_CONTRACT
    meta["publication_template"] = TEMPLATE_VERSION
    meta["registry_key"] = meta.get("task_id")
    meta["parent_objective_id"] = parent_objective_id
    meta["final_response_identity_policy"] = "INHERIT_GLOBAL"
    review = meta.get("policy_review")
    if not isinstance(review, dict):
        review = {"policy_set": "research_taskbook_policy.json", "temporary_overrides": []}
    review["policy_set"] = "research_taskbook_policy.json"
    review["policy_digest"] = research_taskbook.policy_digest(ROOT)
    review["review_state"] = "PASS"
    meta["policy_review"] = review
    if meta.get("base_state") in {None, "DRAFT", "BACKLOG"}:
        meta["base_state"] = "READY"
    meta["evidence_status"] = meta.get("evidence_status") or "TASK_PUBLISHED"
    path.write_text(research_taskbook.render_taskbook(meta, body), encoding="utf-8")
    return meta, body


def command_publish(args: argparse.Namespace) -> int:
    path = taskbook_path(args.taskbook)
    if not path.exists():
        raise RegistryError(f"taskbook does not exist: {path}")
    published_at = now_iso(args.published_at)
    meta, _ = normalize_for_publication(
        path,
        publisher_role=args.publisher_role,
        parent_objective_id=args.parent_objective_id,
    )
    findings = research_taskbook.audit_taskbook(path, dispatch=False)
    hard = [
        f for f in findings
        if f["severity"] == "ERROR"
        and f["code"] not in {"TB-META"}
    ]
    if hard:
        for f in hard:
            print(f"ERROR {f['code']}: {f['message']}")
        raise RegistryError("taskbook failed structural/policy lint")

    registry = load_json(REGISTRY_PATH)
    by_id = registry_task_map(registry)
    task_id = str(meta["task_id"])
    if task_id in by_id and not args.replace:
        raise RegistryError(f"task_id already registered: {task_id}; use --replace for a deliberate republication")
    entry = publication_entry(
        meta,
        path=path,
        publisher_role=args.publisher_role,
        publisher_id=args.publisher_id,
        parent_objective_id=args.parent_objective_id,
        research_value=args.research_value,
        published_at=published_at,
    )
    if task_id in by_id:
        registry["tasks"] = [entry if item.get("task_id") == task_id else item for item in registry["tasks"]]
    else:
        registry.setdefault("tasks", []).append(entry)
    registry["tasks"] = sorted(registry["tasks"], key=lambda item: item["task_id"])
    save_json(REGISTRY_PATH, registry)
    entry["taskbook_blob_sha1"] = blob_sha1(path)
    registry["tasks"] = [entry if item.get("task_id") == task_id else item for item in registry["tasks"]]
    save_json(REGISTRY_PATH, registry)

    errors = audit_registry(strict=True)
    if errors:
        raise RegistryError("publication left invalid registry state: " + "; ".join(errors))
    print(json.dumps(entry, ensure_ascii=False, indent=2))
    return 0


def command_new(args: argparse.Namespace) -> int:
    path = taskbook_path(args.output)
    if path.exists():
        raise RegistryError(f"refusing to overwrite {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    successor_gate = None
    if args.lineage == "CONTINUATION":
        if not args.parent_task_id:
            raise RegistryError("CONTINUATION requires --parent-task-id")
        successor_gate = {
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
        "evidence_status": "TASKBOOK_DRAFT",
        "last_progress_ref": None,
        "last_progress_at": None,
        "hard_block": None,
        "tags": [],
        "claim_lease_minutes": args.claim_lease_minutes,
        "created_by_role": args.publisher_role,
        "task_authority": "PENDING_PUBLICATION",
        "publication_contract": PUBLICATION_CONTRACT,
        "publication_template": TEMPLATE_VERSION,
        "registry_key": args.task_id,
        "parent_objective_id": args.parent_objective_id,
        "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
        "final_response_identity_policy": "INHERIT_GLOBAL",
        "identity_lane": args.lane,
        "origin_kind": args.origin_kind,
        "task_lineage": args.lineage,
        "parent_task_id": args.parent_task_id,
        "successor_gate": successor_gate,
        "policy_review": {
            "policy_set": "research_taskbook_policy.json",
            "policy_digest": research_taskbook.policy_digest(ROOT),
            "review_state": "PENDING_POLICY_REVIEW",
            "temporary_overrides": [],
        },
    }
    if args.origin_candidate_id:
        meta["origin_candidate_id"] = args.origin_candidate_id
    if args.origin_candidate_state:
        meta["origin_candidate_state"] = args.origin_candidate_state
    if args.origin_foundation_question_id:
        meta["origin_foundation_question_id"] = args.origin_foundation_question_id
    body = f"""# {args.title}

Status: `DRAFT / UNREGISTERED / NOT CLAIMABLE`

## 0. Mother question

<task-specific question>

## 1. Frozen inputs and scope

<task-specific inputs, source pins, assumptions, exclusions>

## 2. Hard target and required outputs

<exact theorem / counterexample / computation / formalization / audit outputs>

## 3. Research value to preserve

<why this task is worth registering even if it is not immediately selected>

## 4. Success, kill, and return criteria

<exact success/kill conditions and frozen return/stop behavior>
"""
    path.write_text(research_taskbook.render_taskbook(meta, body), encoding="utf-8")
    print(relative(path))
    print("DRAFT created from the mandatory publication template; edit it, then run publish.")
    return 0


def command_audit(args: argparse.Namespace) -> int:
    errors = audit_registry(strict=True)
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    registry = load_json(REGISTRY_PATH)
    print(f"PASS: task registry valid; {len(registry.get('tasks', []))} explicitly registered task(s).")
    return 0


def command_show(args: argparse.Namespace) -> int:
    registry = load_json(REGISTRY_PATH)
    by_id = registry_task_map(registry)
    if args.task_id:
        item = by_id.get(args.task_id)
        if item is None:
            raise RegistryError(f"unknown task_id: {args.task_id}")
        print(json.dumps(item, ensure_ascii=False, indent=2))
        return 0
    print(json.dumps(registry.get("tasks", []), ensure_ascii=False, indent=2))
    return 0


def command_select(args: argparse.Namespace) -> int:
    registry = load_json(REGISTRY_PATH)
    candidates = [
        item for item in registry.get("tasks", [])
        if item.get("registry_state") in {"REGISTERED", "CLAIMABLE", "HANDOFF_READY"}
        and item.get("claimable") is True
        and (args.kind == "ANY" or item.get("kind", "RESEARCH") == args.kind)
    ]
    priority = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
    leverage = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
    candidates.sort(
        key=lambda x: (
            priority.get(x.get("effective_priority"), 99),
            leverage.get(x.get("effective_leverage"), 99),
            x.get("published_at", ""),
            x.get("task_id", ""),
        )
    )
    chosen = candidates[0] if candidates else None
    print(json.dumps(chosen, ensure_ascii=False, indent=2))
    return 0 if chosen else 2


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Enterprise Math unified task publication registry")
    sp = p.add_subparsers(dest="cmd", required=True)

    new = sp.add_parser("new")
    new.add_argument("--task-id", required=True)
    new.add_argument("--title", required=True)
    new.add_argument("--publisher-role", choices=sorted(PUBLISHER_ROLES), required=True)
    new.add_argument("--parent-objective-id", required=True)
    new.add_argument("--kind", default="RESEARCH")
    new.add_argument("--owner", default="taskbook/unassigned")
    new.add_argument("--priority", default="P2")
    new.add_argument("--leverage", default="MEDIUM")
    new.add_argument("--lane", default="")
    new.add_argument("--origin-kind", default="DRIVER_ROADMAP")
    new.add_argument("--origin-candidate-id")
    new.add_argument("--origin-candidate-state")
    new.add_argument("--origin-foundation-question-id")
    new.add_argument("--lineage", default="NEW_DIRECTION")
    new.add_argument("--parent-task-id")
    new.add_argument("--claim-lease-minutes", type=int, default=120)
    new.add_argument("--output", required=True)
    new.set_defaults(func=command_new)

    pub = sp.add_parser("publish")
    pub.add_argument("--taskbook", required=True)
    pub.add_argument("--publisher-role", choices=sorted(PUBLISHER_ROLES), required=True)
    pub.add_argument("--publisher-id", required=True)
    pub.add_argument("--parent-objective-id", required=True)
    pub.add_argument("--research-value", required=True)
    pub.add_argument("--published-at")
    pub.add_argument("--replace", action="store_true")
    pub.set_defaults(func=command_publish)

    audit = sp.add_parser("audit")
    audit.set_defaults(func=command_audit)

    show = sp.add_parser("show")
    show.add_argument("--task-id")
    show.set_defaults(func=command_show)

    select = sp.add_parser("select")
    select.add_argument("--kind", choices=["RESEARCH", "GOVERNANCE", "ANY"], default="RESEARCH")
    select.set_defaults(func=command_select)
    return p


def main() -> int:
    args = build_parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RegistryError as exc:
        print(f"ERROR: {exc}")
        raise SystemExit(1)
