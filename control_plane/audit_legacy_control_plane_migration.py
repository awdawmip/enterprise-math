#!/usr/bin/env python3
"""Inventory legacy task/state surfaces before physical isolation.

This audit is deliberately conservative. It never rewrites immutable task,
execution, result, review, authority, or research artifact records. It builds a
machine-readable migration plan by comparing mutable/legacy task registries with
current immutable task records and by finding prompt-only legacy exclusions.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "control_plane" / "migrations"
OUT_JSON = OUT_DIR / "legacy-control-plane-inventory-20260902.json"
OUT_MD = OUT_DIR / "LEGACY_CONTROL_PLANE_INVENTORY_20260902.md"

TASK_RE = re.compile(r"\bRS-[A-Z0-9][A-Z0-9-]{2,}\b")
TERMINAL = {
    "ACCEPTED", "ARCHIVED", "BLOCKED_TERMINAL", "CLOSED", "COMPLETED",
    "DEPRECATED", "DONE", "PARKED", "REJECTED", "RETIRED", "SUPERSEDED",
    "TERMINAL", "VERIFIED_COMPLETE",
}
EVIDENCE_PREFIXES = (
    "research_task_records/",
    "research_execution_records/",
    "research_result_records/",
    "research_result_reviews/",
    "research_driver_authority_records/",
    "research_driver_followups/",
    "research_artifacts/",
    "research_returns/",
    "driver_reviews/",
)
CURRENT_CONTROL_PREFIXES = (
    "infrastructure/cloudflare-supervisor/",
    "control_plane/migrations/",
)
PROMPT_NAMES = {
    "AGENTS.md", "00_BOOTSTRAP.md", "OPERATING_MANUAL.md",
    "PROJECT_BOOTSTRAP.md", "PROJECT_ROUTER.md", "README.md",
}
LEGACY_NAME_MARKERS = (
    "legacy", "deprecated", "superseded", "old_control", "old-control",
    "session_liveness", "session-liveness", "conversation_liveness",
    "conversation-liveness", "chat_only", "chat-only",
)
LEGACY_DECL_RE = re.compile(
    r"(?im)^\s*(?:status|lifecycle|control_status)\s*[:=]\s*[`\"']?"
    r"(LEGACY|DEPRECATED|SUPERSEDED|ARCHIVED|RETIRED|READ_ONLY)\b"
)
PROMPT_EXCLUSION_RE = re.compile(
    r"(?i)(do\s+not\s+read|must\s+not\s+read|never\s+read|禁止读取|不得读取|"
    r"不要读取|旧控制面|legacy\s+(?:file|state|control)|superseded\s+(?:file|state))"
)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def sha256(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def walk_objects(value: Any) -> Iterable[dict[str, Any]]:
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk_objects(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_objects(child)


def task_id_from(row: dict[str, Any]) -> str | None:
    for key in ("task_id", "research_task_id", "id"):
        value = row.get(key)
        if isinstance(value, str) and TASK_RE.fullmatch(value.strip().upper()):
            return value.strip().upper()
    return None


def state_from(row: dict[str, Any]) -> str | None:
    for key in ("state", "status", "lifecycle", "task_state", "control_state"):
        value = row.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip().upper()
    return None


def collect_new_task_records() -> tuple[dict[str, list[dict[str, Any]]], list[str]]:
    by_task: dict[str, list[dict[str, Any]]] = {}
    errors: list[str] = []
    root = ROOT / "research_task_records"
    if not root.exists():
        return by_task, ["research_task_records directory is missing"]
    for path in sorted(root.glob("*/*.json")):
        value = load_json(path)
        if not isinstance(value, dict):
            errors.append(f"unreadable task record: {rel(path)}")
            continue
        task_id = task_id_from(value)
        if task_id is None:
            errors.append(f"task record missing task_id: {rel(path)}")
            continue
        by_task.setdefault(task_id, []).append({
            "path": rel(path),
            "publication_id": value.get("publication_id"),
            "record_schema": value.get("record_schema") or value.get("schema"),
            "status": state_from(value),
            "sha256": sha256(path),
        })
    return by_task, errors


def likely_legacy_state_file(path: Path) -> bool:
    rp = rel(path).lower()
    name = path.name.lower()
    if rp.startswith(EVIDENCE_PREFIXES) or rp.startswith(CURRENT_CONTROL_PREFIXES):
        return False
    if any(marker in rp for marker in LEGACY_NAME_MARKERS):
        return True
    if name in {"research_task_registry.json", "research_task_registry.yaml", "research_task_registry.yml"}:
        return True
    if path.suffix.lower() in {".json", ".yaml", ".yml", ".md", ".py"}:
        try:
            head = path.read_text(encoding="utf-8", errors="replace")[:16000]
        except Exception:
            return False
        if LEGACY_DECL_RE.search(head):
            return True
    return False


def collect_legacy_tasks() -> tuple[dict[str, dict[str, Any]], list[dict[str, Any]]]:
    tasks: dict[str, dict[str, Any]] = {}
    source_files: list[dict[str, Any]] = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or ".git" in path.parts or not likely_legacy_state_file(path):
            continue
        rp = rel(path)
        entry = {"path": rp, "sha256": sha256(path), "task_ids": []}
        text = path.read_text(encoding="utf-8", errors="replace")
        ids = set(TASK_RE.findall(text.upper()))
        value = load_json(path) if path.suffix.lower() == ".json" else None
        if value is not None:
            for row in walk_objects(value):
                tid = task_id_from(row)
                if tid is None:
                    continue
                ids.add(tid)
                item = tasks.setdefault(tid, {
                    "task_id": tid,
                    "legacy_sources": [],
                    "legacy_states": [],
                    "taskbook_candidates": [],
                })
                state = state_from(row)
                item["legacy_sources"].append(rp)
                if state:
                    item["legacy_states"].append(state)
        for tid in sorted(ids):
            item = tasks.setdefault(tid, {
                "task_id": tid,
                "legacy_sources": [],
                "legacy_states": [],
                "taskbook_candidates": [],
            })
            if rp not in item["legacy_sources"]:
                item["legacy_sources"].append(rp)
        entry["task_ids"] = sorted(ids)
        source_files.append(entry)

    taskbooks = sorted((ROOT / "research_tasks").glob("*.md")) if (ROOT / "research_tasks").exists() else []
    for tid, item in tasks.items():
        needle = tid.removeprefix("RS-").replace("-", "_")
        matches = [rel(p) for p in taskbooks if needle in p.stem.upper()]
        if not matches:
            for path in taskbooks:
                head = path.read_text(encoding="utf-8", errors="replace")[:12000]
                if tid in head.upper():
                    matches.append(rel(path))
        item["taskbook_candidates"] = sorted(set(matches))
        item["legacy_sources"] = sorted(set(item["legacy_sources"]))
        item["legacy_states"] = sorted(set(item["legacy_states"]))
    return tasks, source_files


def classify_tasks(
    legacy: dict[str, dict[str, Any]],
    new_records: dict[str, list[dict[str, Any]]],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for tid in sorted(legacy):
        item = dict(legacy[tid])
        states = set(item.get("legacy_states") or [])
        nonterminal = not states or any(state not in TERMINAL for state in states)
        current = new_records.get(tid, [])
        if current:
            disposition = "ALREADY_PRESENT_NEW_CONTROL"
        elif nonterminal and item.get("taskbook_candidates"):
            disposition = "MIGRATE_ACTIVE_TASK"
        elif nonterminal:
            disposition = "LEGACY_ORPHAN_REQUIRES_EXACT_SOURCE"
        else:
            disposition = "TERMINAL_HISTORY_ONLY"
        item.update({
            "legacy_nonterminal": nonterminal,
            "new_control_records": current,
            "migration_disposition": disposition,
        })
        rows.append(item)
    return rows


def collect_prompt_exclusions() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        rp = rel(path)
        if path.name not in PROMPT_NAMES and "bootstrap" not in path.name.lower() and "prompt" not in rp.lower() and "protocol" not in rp.lower():
            continue
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        hits = [i for i, line in enumerate(lines, start=1) if PROMPT_EXCLUSION_RE.search(line)]
        if hits:
            rows.append({
                "path": rp,
                "sha256": sha256(path),
                "line_numbers": hits,
                "hit_count": len(hits),
            })
    return rows


def referenced_elsewhere(candidate: Path, candidates: set[str]) -> list[str]:
    rp = rel(candidate)
    names = {rp, candidate.name, candidate.stem}
    hits: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        other = rel(path)
        if other == rp or other in candidates or other.startswith(EVIDENCE_PREFIXES):
            continue
        if path.suffix.lower() not in {".py", ".ts", ".js", ".mjs", ".json", ".yaml", ".yml", ".md", ".toml"}:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if any(name and name in text for name in names):
            hits.append(other)
            if len(hits) >= 20:
                break
    return sorted(set(hits))


def classify_legacy_files(source_files: list[dict[str, Any]]) -> list[dict[str, Any]]:
    candidates = {row["path"] for row in source_files}
    rows: list[dict[str, Any]] = []
    for row in source_files:
        path = ROOT / row["path"]
        refs = referenced_elsewhere(path, candidates)
        evidence = row["path"].startswith(EVIDENCE_PREFIXES)
        keep_reason = None
        if evidence:
            keep_reason = "IMMUTABLE_EVIDENCE"
        elif refs:
            keep_reason = "CURRENT_REFERENCE_EXISTS"
        elif row.get("task_ids"):
            keep_reason = "TASK_MIGRATION_MUST_COMPLETE_FIRST"
        disposition = "KEEP_ON_MAIN" if keep_reason else "ELIGIBLE_FOR_ISOLATION_AFTER_REVIEW"
        rows.append({**row, "references": refs, "disposition": disposition, "keep_reason": keep_reason})
    return rows


def main() -> int:
    new_records, record_errors = collect_new_task_records()
    legacy, source_files = collect_legacy_tasks()
    tasks = classify_tasks(legacy, new_records)
    files = classify_legacy_files(source_files)
    prompt_exclusions = collect_prompt_exclusions()

    summary = {
        "new_control_task_count": len(new_records),
        "legacy_task_count": len(tasks),
        "already_present_new_control": sum(x["migration_disposition"] == "ALREADY_PRESENT_NEW_CONTROL" for x in tasks),
        "migrate_active_task": sum(x["migration_disposition"] == "MIGRATE_ACTIVE_TASK" for x in tasks),
        "legacy_orphan": sum(x["migration_disposition"] == "LEGACY_ORPHAN_REQUIRES_EXACT_SOURCE" for x in tasks),
        "terminal_history_only": sum(x["migration_disposition"] == "TERMINAL_HISTORY_ONLY" for x in tasks),
        "legacy_source_file_count": len(files),
        "eligible_for_isolation": sum(x["disposition"] == "ELIGIBLE_FOR_ISOLATION_AFTER_REVIEW" for x in files),
        "prompt_files_with_exclusions": len(prompt_exclusions),
        "task_record_errors": len(record_errors),
    }
    payload = {
        "schema": "ENTERPRISE_MATH_LEGACY_CONTROL_PLANE_INVENTORY_V1",
        "status": "AUDIT_ONLY_NO_AUTHORITY",
        "generated_from": "repository working tree",
        "summary": summary,
        "task_record_errors": record_errors,
        "tasks": tasks,
        "legacy_files": files,
        "prompt_exclusions": prompt_exclusions,
        "safety": {
            "immutable_evidence_rewritten": False,
            "working_truth_granted": False,
            "foundation_authority_granted": False,
            "canonical_promotion_granted": False,
        },
    }
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Legacy control-plane inventory — 2026-09-02",
        "",
        "This is an audit-only inventory. It grants no mathematical or control authority.",
        "",
        "## Summary",
        "",
    ]
    for key, value in summary.items():
        lines.append(f"- `{key}`: {value}")
    lines += ["", "## Task migration classes", ""]
    for name in (
        "MIGRATE_ACTIVE_TASK", "LEGACY_ORPHAN_REQUIRES_EXACT_SOURCE",
        "ALREADY_PRESENT_NEW_CONTROL", "TERMINAL_HISTORY_ONLY",
    ):
        selected = [x for x in tasks if x["migration_disposition"] == name]
        lines.append(f"### {name} ({len(selected)})")
        lines.append("")
        for row in selected:
            states = ", ".join(row.get("legacy_states") or ["UNKNOWN"])
            lines.append(f"- `{row['task_id']}` — states: `{states}`")
        if not selected:
            lines.append("- None")
        lines.append("")
    lines += ["## Files eligible for physical isolation", ""]
    selected = [x for x in files if x["disposition"] == "ELIGIBLE_FOR_ISOLATION_AFTER_REVIEW"]
    for row in selected:
        lines.append(f"- `{row['path']}`")
    if not selected:
        lines.append("- None")
    lines += ["", "## Prompt files containing legacy read exclusions", ""]
    for row in prompt_exclusions:
        lines.append(f"- `{row['path']}` — {row['hit_count']} hit(s), lines {row['line_numbers']}")
    if not prompt_exclusions:
        lines.append("- None")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps(summary, ensure_ascii=False, sort_keys=True))
    if record_errors:
        print("FAIL: immutable task-record inventory contained parse/schema defects")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
