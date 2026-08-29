#!/usr/bin/env python3
"""Read-only V1 task-registry compatibility surface.

Post-cutover publication authority is tools/research_task_records.py and
canonical selection is tools/research_dispatch.py. This module retains the V1
pure helpers/audit used by historical records and regressions, but it no longer
creates, publishes, replaces, or selects official work.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

try:
    from tools import research_task_records
    from tools import research_taskbook
except ModuleNotFoundError:
    import research_task_records  # type: ignore
    import research_taskbook  # type: ignore

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "research_task_registry.json"
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


def blob_sha1(path: Path) -> str:
    return "sha1:" + research_taskbook.git_blob_identity(path.read_bytes()).hex()


def publication_id(task_id: str, taskbook_blob: str, publisher_id: str, parent_objective_id: str) -> str:
    raw = "\0".join((task_id, taskbook_blob, publisher_id, parent_objective_id)).encode("utf-8")
    return "TP-" + hashlib.sha256(raw).hexdigest()[:16].upper()


def relative(path: Path, root: Path = ROOT) -> str:
    return path.relative_to(root).as_posix() if path.is_relative_to(root) else path.as_posix()


def retained_parallel_publication_ids(root: Path = ROOT) -> set[str]:
    """Return publications explicitly retained by the parallel-resolution overlay.

    This compatibility bridge exists so the V1 orphan audit can recognize an
    exact immutable publication that is intentionally non-operational. It does
    not grant dispatch/current authority to that publication.
    """
    resolver = getattr(research_task_records, "publication_resolutions", None)
    if resolver is None:
        return set()
    try:
        resolutions = resolver(root)
    except Exception as exc:
        raise RegistryError(f"cannot resolve publication retention overlay: {exc}") from exc
    out: set[str] = set()
    for row in resolutions.values():
        retained = row.get("retained_parallel_publication_ids", [])
        if isinstance(retained, list):
            out.update(item for item in retained if isinstance(item, str) and item)
        # Backward-compatible field consumed by the current reducer. Semantically
        # these are retained parallel publications, not rejected data.
        compat = row.get("quarantined_publication_ids", [])
        if isinstance(compat, list):
            out.update(item for item in compat if isinstance(item, str) and item)
    return out


def has_exact_v2_publication_authority(
    path: Path,
    meta: dict[str, Any],
    all_v2_records: list[dict[str, Any]],
    retained_parallel_ids: set[str],
    *,
    root: Path = ROOT,
) -> bool:
    """Recognize exact immutable publication provenance, not only current dispatch.

    Orphan detection answers whether this taskbook has an exact immutable
    publication object. Current operational selection is a separate dispatch
    question. Normal ACTIVE or terminal V2 publications are valid provenance even
    when they are not current/claimable. A nonstandard migration transaction is
    accepted only when the parallel-resolution overlay explicitly retains its
    publication id.
    """
    task_id = meta.get("task_id")
    if not isinstance(task_id, str) or not task_id:
        return False
    expected_path = relative(path, root)
    expected_blob = blob_sha1(path)
    valid_standard_states = {"ACTIVE"} | set(
        getattr(research_task_records, "TERMINAL_RECORD_STATES", set())
    )
    for record in all_v2_records:
        if not isinstance(record, dict):
            continue
        pub_id = record.get("publication_id")
        retained = isinstance(pub_id, str) and pub_id in retained_parallel_ids
        if record.get("record_schema") != research_task_records.RECORD_SCHEMA:
            continue
        if record.get("task_id") != task_id:
            continue
        if record.get("taskbook_path") != expected_path:
            continue
        if record.get("taskbook_blob_sha1") != expected_blob:
            continue
        if record.get("record_state", "ACTIVE") not in valid_standard_states and not retained:
            continue
        if (
            record.get("publication_transaction")
            != research_task_records.PUBLICATION_TRANSACTION_V2
            and not retained
        ):
            continue
        return True
    return False


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
    if publisher_role == "RESEARCHER" and meta.get("origin_kind") == "FREE_AXIOM_CANDIDATE":
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
    """Historical pure record constructor retained for compatibility tests only."""
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
    task_id = str(meta.get("task_id") or "").strip()
    if not task_id:
        raise RegistryError("taskbook requires task_id")
    lineage = str(meta.get("task_lineage") or "").strip()
    if not lineage:
        raise RegistryError("taskbook requires task_lineage")
    task_blob = blob_sha1(path)
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
    """Validate the frozen/shared V1 mirror without granting it write authority."""
    registry = load_json(root / "research_task_registry.json")
    errors: list[str] = []
    if registry.get("schema") != SCHEMA:
        errors.append("unexpected task registry schema")
    if registry.get("status") != "ACTIVE_CANONICAL_TASK_REGISTRY":
        errors.append("task registry must retain V1 compatibility status")
    try:
        by_id = registry_task_map(registry)
    except RegistryError as exc:
        return [str(exc)]
    try:
        # Resolve current heads to ensure the operational overlay itself is valid,
        # but use every immutable record for historical/orphan provenance checks.
        research_task_records.current_records(root)
        all_v2_records = research_task_records.iter_records(root)
        retained_parallel_ids = retained_parallel_publication_ids(root)
    except Exception as exc:
        return errors + [f"cannot resolve immutable V2 task authority: {exc}"]
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
            errors.append(f"{task_id}: terminal_scope must be TASK")
        if item.get("working_truth_granted") is not False:
            errors.append(f"{task_id}: publication may not grant Working Truth")
        if item.get("canonical_promotion_granted") is not False:
            errors.append(f"{task_id}: publication may not grant canonical promotion")
        if item.get("publisher_role") == "RESEARCHER":
            if item.get("effective_priority") != RESEARCHER_DEFAULT_PRIORITY:
                errors.append(f"{task_id}: researcher-published V1 record effective_priority must be P2")
            if item.get("effective_leverage") != RESEARCHER_DEFAULT_LEVERAGE:
                errors.append(f"{task_id}: researcher-published V1 record effective_leverage must be MEDIUM")
        path_value = item.get("taskbook_path")
        if not isinstance(path_value, str):
            errors.append(f"{task_id}: missing taskbook_path")
            continue
        path = root / path_value
        if not path.exists():
            errors.append(f"{task_id}: registered taskbook path does not exist: {path_value}")
            continue
        try:
            meta, _ = research_taskbook.split_taskbook(path.read_text(encoding="utf-8"))
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
        if blob_sha1(path) != item.get("taskbook_blob_sha1"):
            errors.append(f"{task_id}: taskbook blob drift")

    # V1 compatibility orphan detection is about provenance existence, not
    # current operational selection. Exact retained parallel publications are
    # therefore valid authority even when another head is selected for runtime.
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
                and meta.get("task_id") not in by_id
                and not has_exact_v2_publication_authority(
                    path,
                    meta,
                    all_v2_records,
                    retained_parallel_ids,
                    root=root,
                )
            ):
                errors.append(
                    f"{relative(path, root)}: orphaned published taskbook has neither a V1 compatibility mirror "
                    "nor exact immutable V2/retained-parallel publication provenance"
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


def _forbid(command: str) -> int:
    raise RegistryError(
        f"V1 shared-registry command {command!r} is read-only after immutable cutover; "
        "use tools/research_task_records.py for publication and tools/research_dispatch.py for selection"
    )


def command_audit(args: argparse.Namespace) -> int:
    errors = audit_registry(strict=True)
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print(f"PASS: V1 compatibility registry valid; {len(load_json(REGISTRY_PATH).get('tasks', []))} mirrored task(s).")
    return 0


def command_show(args: argparse.Namespace) -> int:
    by_id = registry_task_map(load_json(REGISTRY_PATH))
    if args.task_id:
        item = by_id.get(args.task_id)
        if item is None:
            raise RegistryError(f"unknown V1 compatibility task_id: {args.task_id}")
        print(json.dumps(item, ensure_ascii=False, indent=2))
    else:
        print(json.dumps(list(by_id.values()), ensure_ascii=False, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Enterprise Math V1 shared task-registry compatibility surface")
    sub = parser.add_subparsers(dest="command", required=True)
    audit = sub.add_parser("audit")
    audit.set_defaults(func=command_audit)
    show = sub.add_parser("show")
    show.add_argument("--task-id")
    show.set_defaults(func=command_show)
    for name in ("new", "publish", "select"):
        item = sub.add_parser(name)
        item.set_defaults(func=lambda args, command=name: _forbid(command))
    return parser


def main() -> int:
    args = build_parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RegistryError as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
