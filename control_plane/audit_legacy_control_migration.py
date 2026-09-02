#!/usr/bin/env python3
"""Inventory legacy control-plane tasks and physical prompt/file debt.

This is a read-only migration audit.  It does not publish tasks, mutate Issue #240,
or select mathematical truth.  The report is intended to support an atomic V2
cutover that preserves task/frontier provenance before legacy files leave main.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

TERMINAL_DISPOSITIONS = {"ACCEPTED", "REJECTED", "PARKED", "CLOSED", "SUPERSEDED"}
LEGACY_FILES = [
    "research_scheduler.json",
    "tools/research_scheduler.py",
    "research_task_registry.json",
    "tools/research_task_registry.py",
    "research_task_publication_contract.json",
    "tools/check_task_registry_cutover.py",
    "docs/RESEARCH_SCHEDULER.md",
    "docs/RESEARCH_TASK_PUBLICATION_PROTOCOL_V1.md",
]
PROMPT_PHRASES = [
    "do not read",
    "must not read",
    "do not preload",
    "must not preload",
    "forbidden read",
    "legacy scheduler",
    "legacy registry",
    "old-route",
    "旧文件",
    "不要读",
    "不得读取",
    "禁止读取",
]
TEXT_SUFFIXES = {".md", ".json", ".py", ".yml", ".yaml", ".toml"}


def load_json(path: Path, default: Any = None) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def iso(value: Any) -> datetime:
    if not isinstance(value, str) or not value.strip():
        return datetime(1970, 1, 1, tzinfo=timezone.utc)
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return datetime(1970, 1, 1, tzinfo=timezone.utc)
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)


def task_rows(payload: Any) -> dict[str, dict[str, Any]]:
    if not isinstance(payload, dict):
        return {}
    out: dict[str, dict[str, Any]] = {}
    for row in payload.get("tasks", []):
        if isinstance(row, dict) and isinstance(row.get("task_id"), str):
            out[row["task_id"]] = row
    return out


def flatten_comments(payload: Any) -> list[dict[str, Any]]:
    if not isinstance(payload, list):
        return []
    if payload and all(isinstance(page, list) for page in payload):
        payload = [item for page in payload for item in page]
    return [item for item in payload if isinstance(item, dict)]


def taskbook_index() -> tuple[dict[str, list[str]], list[str]]:
    by_task: dict[str, list[str]] = defaultdict(list)
    errors: list[str] = []
    try:
        from tools import research_taskbook
    except Exception as exc:  # pragma: no cover - report boundary
        return {}, [f"cannot import research_taskbook: {exc}"]
    for path in sorted((ROOT / "research_tasks").glob("*.md")):
        try:
            meta, _ = research_taskbook.split_taskbook(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        task_id = meta.get("task_id")
        if isinstance(task_id, str) and task_id:
            by_task[task_id].append(path.relative_to(ROOT).as_posix())
    return dict(by_task), errors


def v2_records() -> tuple[dict[str, dict[str, Any]], list[str]]:
    try:
        from tools import research_task_records
        return research_task_records.current_records(ROOT), []
    except Exception as exc:
        return {}, [f"cannot resolve V2 current task records: {exc}"]


def raw_result_state() -> dict[str, dict[str, Any]]:
    results: dict[str, list[dict[str, Any]]] = defaultdict(list)
    reviews: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for path in sorted((ROOT / "research_result_records").glob("*/*.json")):
        try:
            row = load_json(path)
        except Exception:
            continue
        if isinstance(row, dict) and isinstance(row.get("task_id"), str):
            row = dict(row)
            row["_path"] = path.relative_to(ROOT).as_posix()
            results[row["task_id"]].append(row)
    for path in sorted((ROOT / "research_result_reviews").glob("*/*.json")):
        try:
            row = load_json(path)
        except Exception:
            continue
        if isinstance(row, dict) and isinstance(row.get("result_id"), str):
            row = dict(row)
            row["_path"] = path.relative_to(ROOT).as_posix()
            reviews[row["result_id"]].append(row)
    out: dict[str, dict[str, Any]] = {}
    for task_id, rows in results.items():
        rows.sort(key=lambda item: (iso(item.get("frozen_at")), str(item.get("result_id", ""))))
        latest = rows[-1]
        rid = latest.get("result_id")
        rrows = reviews.get(str(rid), [])
        rrows.sort(key=lambda item: (iso(item.get("reviewed_at")), str(item.get("review_id", ""))))
        review = rrows[-1] if rrows else None
        disposition = review.get("disposition") if isinstance(review, dict) else None
        out[task_id] = {
            "result_id": rid,
            "result_path": latest.get("_path"),
            "review_id": review.get("review_id") if isinstance(review, dict) else None,
            "review_path": review.get("_path") if isinstance(review, dict) else None,
            "disposition": disposition,
            "terminal": bool(
                isinstance(review, dict)
                and (review.get("terminal") is True or disposition in TERMINAL_DISPOSITIONS)
            ),
        }
    return out


def dispatch_states(comments: list[dict[str, Any]]) -> tuple[dict[str, dict[str, Any]], list[str]]:
    try:
        from control_plane import research_control_bootstrap
        research_control_bootstrap.install(ROOT)
        from tools import research_dispatch
        events = research_dispatch.events_from_github_comments(comments, root=ROOT)
        states = research_dispatch.effective_states(
            events, now=datetime.now(timezone.utc), root=ROOT
        )
        return {
            str(row["task_id"]): row
            for row in states
            if isinstance(row, dict) and isinstance(row.get("task_id"), str)
        }, []
    except Exception as exc:
        return {}, [f"cannot build authenticated dispatch states: {exc}"]


def inbound_references(target: str) -> list[dict[str, Any]]:
    hits: list[dict[str, Any]] = []
    needle = target.lower()
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel == target or rel.startswith(".git/"):
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except Exception:
            continue
        for number, line in enumerate(lines, 1):
            if needle in line.lower():
                hits.append({"path": rel, "line": number, "text": line.strip()[:300]})
                if len(hits) >= 80:
                    return hits
    return hits


def prompt_debt() -> list[dict[str, Any]]:
    hits: list[dict[str, Any]] = []
    roots = [ROOT / "AGENTS.md", ROOT / "docs", ROOT / "definitions", ROOT / "control_plane"]
    paths: list[Path] = []
    for item in roots:
        if item.is_file():
            paths.append(item)
        elif item.is_dir():
            paths.extend(path for path in item.rglob("*") if path.is_file())
    for path in sorted(set(paths)):
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except Exception:
            continue
        rel = path.relative_to(ROOT).as_posix()
        for number, line in enumerate(lines, 1):
            lowered = line.lower()
            matched = [phrase for phrase in PROMPT_PHRASES if phrase in lowered]
            if matched:
                hits.append(
                    {"path": rel, "line": number, "phrases": matched, "text": line.strip()[:400]}
                )
    return hits


def classify(
    task_id: str,
    scheduler: dict[str, dict[str, Any]],
    registry: dict[str, dict[str, Any]],
    v2: dict[str, dict[str, Any]],
    books: dict[str, list[str]],
    result: dict[str, dict[str, Any]],
    state: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    old = dict(scheduler.get(task_id, {}))
    old.update(registry.get(task_id, {}))
    current_state = state.get(task_id, {})
    result_state = result.get(task_id)
    sources = []
    if task_id in scheduler:
        sources.append("FROZEN_SCHEDULER")
    if task_id in registry:
        sources.append("V1_SHARED_REGISTRY")
    if task_id in v2:
        action = "ALREADY_MIGRATED_V2"
    elif result_state and result_state.get("terminal"):
        action = "RETIRE_TERMINAL_HISTORY"
    elif str(current_state.get("dispatch_state")) == "COMPLETE" or str(old.get("base_state")) in {"DONE", "SUPERSEDED"}:
        action = "RETIRE_TERMINAL_HISTORY"
    elif current_state.get("claim_id"):
        action = "MIGRATE_ACTIVE_PRESERVE_EXISTING_CLAIM"
    else:
        action = "MIGRATE_ACTIVE_TO_V2"
    return {
        "task_id": task_id,
        "title": old.get("title"),
        "sources": sources,
        "legacy_base_state": old.get("base_state"),
        "legacy_priority": old.get("priority"),
        "legacy_leverage": old.get("leverage"),
        "owner": old.get("owner"),
        "frontier": old.get("frontier"),
        "next_action": old.get("next_action"),
        "taskbook_candidates": books.get(task_id, []),
        "v2_publication_id": v2.get(task_id, {}).get("publication_id"),
        "dispatch_state": current_state.get("dispatch_state"),
        "runtime_state": current_state.get("state"),
        "claim_id": current_state.get("claim_id"),
        "lease_until": current_state.get("lease_until"),
        "result": result_state,
        "migration_action": action,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--comments", type=Path, required=True)
    parser.add_argument("--json-out", type=Path, required=True)
    parser.add_argument("--md-out", type=Path, required=True)
    args = parser.parse_args()

    errors: list[str] = []
    scheduler_payload = load_json(ROOT / "research_scheduler.json", {})
    registry_payload = load_json(ROOT / "research_task_registry.json", {})
    scheduler = task_rows(scheduler_payload)
    registry = task_rows(registry_payload)
    books, book_errors = taskbook_index()
    v2, v2_errors = v2_records()
    results = raw_result_state()
    comments = flatten_comments(load_json(args.comments, []))
    states, state_errors = dispatch_states(comments)
    errors.extend(book_errors + v2_errors + state_errors)

    legacy_ids = sorted(set(scheduler) | set(registry))
    rows = [
        classify(task_id, scheduler, registry, v2, books, results, states)
        for task_id in legacy_ids
    ]
    counts: dict[str, int] = defaultdict(int)
    for row in rows:
        counts[row["migration_action"]] += 1

    legacy_files = []
    for target in LEGACY_FILES:
        path = ROOT / target
        if path.exists():
            legacy_files.append(
                {
                    "path": target,
                    "size": path.stat().st_size,
                    "references": inbound_references(target),
                }
            )

    state_machine_files = sorted(
        path.relative_to(ROOT).as_posix()
        for path in ROOT.glob("*state_machine*.json")
    )
    report = {
        "schema": "ENTERPRISE_MATH_LEGACY_CONTROL_MIGRATION_AUDIT_V1",
        "snapshot": {
            "github_sha": __import__("os").environ.get("GITHUB_SHA"),
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "issue_240_comments": len(comments),
        },
        "counts": {
            "scheduler_tasks": len(scheduler),
            "v1_registry_tasks": len(registry),
            "legacy_union_tasks": len(legacy_ids),
            "v2_current_tasks": len(v2),
            **dict(sorted(counts.items())),
        },
        "tasks": rows,
        "legacy_files": legacy_files,
        "state_machine_files": state_machine_files,
        "prompt_debt": prompt_debt(),
        "errors": errors,
    }
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Legacy control-plane migration audit",
        "",
        f"Snapshot: `{report['snapshot']['github_sha']}`",
        f"Issue #240 comments consumed: {len(comments)}",
        "",
        "## Counts",
        "",
    ]
    for key, value in report["counts"].items():
        lines.append(f"- `{key}`: {value}")
    lines.extend(["", "## Tasks requiring action", ""])
    for row in rows:
        if row["migration_action"] != "ALREADY_MIGRATED_V2":
            lines.append(
                f"- `{row['task_id']}` — **{row['migration_action']}**; "
                f"state={row.get('dispatch_state') or row.get('legacy_base_state')}; "
                f"claim={row.get('claim_id') or 'none'}; taskbooks={len(row['taskbook_candidates'])}"
            )
    lines.extend(["", "## Legacy file reference surface", ""])
    for row in legacy_files:
        lines.append(f"- `{row['path']}` — {len(row['references'])} inbound reference(s), {row['size']} bytes")
    lines.extend(["", "## Prompt debt", "", f"- matched lines: {len(report['prompt_debt'])}"])
    if errors:
        lines.extend(["", "## Audit errors", ""])
        lines.extend(f"- {item}" for item in errors)
    args.md_out.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps(report["counts"], sort_keys=True))
    if errors:
        print("AUDIT_COMPLETED_WITH_REPORTED_ERRORS")
    else:
        print("AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
