#!/usr/bin/env python3
"""Apply a guarded migration from legacy mutable state to current control records.

The script is designed for a fresh worktree at the latest main commit. It will
refuse destructive changes unless every nonterminal legacy task is already
represented by at least one immutable current task record. Terminal-only legacy
rows remain preserved on the isolation branch as provenance and do not enter the
runtime task set.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "control_plane" / "migrations" / "legacy-control-plane-inventory-20260902.json"
MIGRATION_JSON = ROOT / "control_plane" / "migrations" / "legacy-control-plane-migration-20260902.json"
MIGRATION_MD = ROOT / "control_plane" / "migrations" / "LEGACY_CONTROL_PLANE_MIGRATION_20260902.md"
SURFACE = ROOT / "control_plane" / "current_control_plane_surface.json"
ISOLATION_BRANCH = "archive/legacy-control-plane-state-machine-20260902"

EVIDENCE_PREFIXES = (
    "research_task_records/", "research_execution_records/",
    "research_result_records/", "research_result_reviews/",
    "research_driver_authority_records/", "research_driver_followups/",
    "research_artifacts/", "research_returns/", "driver_reviews/",
)
PROTECTED_FILES = {
    "AGENTS.md", "research_task_records.py", "research_execution_records.py",
    "research_result_records.py", "research_control_dispatch.py",
}
LEGACY_READ_RE = re.compile(
    r"(?i)(do\s+not\s+read|must\s+not\s+read|never\s+read|禁止读取|不得读取|"
    r"不要读取).{0,160}(legacy|旧控制面|superseded|deprecated|旧状态机)|"
    r"(legacy|旧控制面|superseded|deprecated|旧状态机).{0,160}"
    r"(do\s+not\s+read|must\s+not\s+read|never\s+read|禁止读取|不得读取|不要读取)"
)
TASK_RE = re.compile(r"\bRS-[A-Z0-9][A-Z0-9-]{2,}\b")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def file_sha256(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def run(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=ROOT, text=True, capture_output=True, check=check)


def load_inventory() -> dict[str, Any]:
    value = json.loads(INVENTORY.read_text(encoding="utf-8"))
    if value.get("schema") != "ENTERPRISE_MATH_LEGACY_CONTROL_PLANE_INVENTORY_V1":
        raise RuntimeError("unexpected inventory schema")
    if value.get("task_record_errors"):
        raise RuntimeError("task-record inventory errors forbid migration")
    return value


def evidence_digest() -> dict[str, str]:
    out: dict[str, str] = {}
    for prefix in EVIDENCE_PREFIXES:
        root = ROOT / prefix
        if not root.exists():
            continue
        for path in sorted(root.rglob("*")):
            if path.is_file():
                out[rel(path)] = file_sha256(path)
    return out


def all_task_ids_in_file(path: Path) -> set[str]:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return set()
    return set(TASK_RE.findall(text.upper()))


def choose_isolation_paths(inventory: dict[str, Any]) -> list[str]:
    task_class = {row["task_id"]: row["migration_disposition"] for row in inventory["tasks"]}
    allowed_task_classes = {"ALREADY_PRESENT_NEW_CONTROL", "TERMINAL_HISTORY_ONLY"}
    paths: list[str] = []
    for row in inventory["legacy_files"]:
        rp = row["path"]
        path = ROOT / rp
        if not path.is_file() or rp.startswith(EVIDENCE_PREFIXES):
            continue
        if path.name in PROTECTED_FILES or rp.startswith("infrastructure/cloudflare-supervisor/"):
            continue
        refs = [x for x in row.get("references") or [] if not x.endswith("AGENTS.md")]
        task_ids = set(row.get("task_ids") or []) | all_task_ids_in_file(path)
        tasks_safe = all(task_class.get(tid) in allowed_task_classes for tid in task_ids)
        explicit_eligible = row.get("disposition") == "ELIGIBLE_FOR_ISOLATION_AFTER_REVIEW"
        migrated_state_file = bool(task_ids) and tasks_safe
        mutable_registry = path.name in {
            "research_task_registry.json", "research_task_registry.yaml", "research_task_registry.yml"
        }
        if refs:
            continue
        if explicit_eligible or migrated_state_file or (mutable_registry and tasks_safe):
            paths.append(rp)
    return sorted(set(paths))


def simplify_prompt(path: Path, isolation_paths: list[str]) -> tuple[bool, int]:
    original = path.read_text(encoding="utf-8", errors="strict")
    basenames = {Path(x).name.lower() for x in isolation_paths}
    blocks = re.split(r"(\n\s*\n)", original)
    out: list[str] = []
    removed = 0
    for block in blocks:
        low = block.lower()
        named = any(name and name in low for name in basenames)
        legacy_read = bool(LEGACY_READ_RE.search(block))
        generic_quarantine = (
            ("legacy" in low or "旧控制面" in low or "旧状态机" in low or "superseded" in low)
            and ("read" in low or "读取" in low)
            and ("must not" in low or "do not" in low or "禁止" in low or "不得" in low or "不要" in low)
        )
        if legacy_read or (named and generic_quarantine):
            removed += block.count("\n") + 1
            continue
        out.append(block)
    updated = "".join(out)
    while "\n\n\n" in updated:
        updated = updated.replace("\n\n\n", "\n\n")
    marker = "CURRENT_CONTROL_SURFACE_PHYSICALLY_ISOLATED"
    if marker not in updated:
        note = (
            "\n\n## Current control-plane file boundary\n\n"
            f"`{marker}`: runtime control authority is read only from the current main-tree "
            "surfaces named in `control_plane/current_control_plane_surface.json`. Legacy mutable "
            f"state-machine files are physically preserved on `{ISOLATION_BRANCH}` and are absent "
            "from main. Do not recreate prompt-level legacy-file deny lists.\n"
        )
        first_break = updated.find("\n## ")
        if first_break > 0:
            updated = updated[:first_break] + note + updated[first_break:]
        else:
            updated = updated.rstrip() + note + "\n"
    changed = updated != original
    if changed:
        path.write_text(updated, encoding="utf-8")
    return changed, removed


def validate_no_live_references(isolation_paths: list[str]) -> list[str]:
    errors: list[str] = []
    needles = {rp: {rp, Path(rp).name, Path(rp).stem} for rp in isolation_paths}
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        rp = rel(path)
        if rp in isolation_paths or rp.startswith(EVIDENCE_PREFIXES):
            continue
        if path.suffix.lower() not in {".py", ".ts", ".js", ".mjs", ".json", ".yaml", ".yml", ".md", ".toml"}:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for old, names in needles.items():
            if any(name and name in text for name in names):
                if rp in {
                    rel(MIGRATION_JSON), rel(MIGRATION_MD), rel(SURFACE),
                }:
                    continue
                errors.append(f"{rp} still references isolated file {old}")
    return sorted(set(errors))


def main() -> int:
    inventory = load_inventory()
    blockers = [
        row for row in inventory["tasks"]
        if row["migration_disposition"] in {
            "MIGRATE_ACTIVE_TASK", "LEGACY_ORPHAN_REQUIRES_EXACT_SOURCE"
        }
    ]
    if blockers:
        ids = ", ".join(row["task_id"] for row in blockers)
        raise RuntimeError(
            "nonterminal legacy tasks lack current immutable task records; "
            f"no destructive isolation performed: {ids}"
        )

    before_evidence = evidence_digest()
    isolation_paths = choose_isolation_paths(inventory)
    if not isolation_paths:
        raise RuntimeError("no safely isolatable legacy files were identified")

    prompt_changes: list[dict[str, Any]] = []
    for row in inventory.get("prompt_exclusions") or []:
        path = ROOT / row["path"]
        if not path.is_file() or rel(path) in isolation_paths:
            continue
        changed, removed_lines = simplify_prompt(path, isolation_paths)
        if changed:
            prompt_changes.append({"path": rel(path), "legacy_prompt_lines_removed": removed_lines})

    for rp in isolation_paths:
        path = ROOT / rp
        if path.exists():
            path.unlink()
            parent = path.parent
            while parent != ROOT and parent.exists() and not any(parent.iterdir()):
                parent.rmdir()
                parent = parent.parent

    active_mappings = []
    terminal_history = []
    for row in inventory["tasks"]:
        mapping = {
            "task_id": row["task_id"],
            "legacy_states": row.get("legacy_states") or [],
            "legacy_sources": row.get("legacy_sources") or [],
            "new_control_records": row.get("new_control_records") or [],
            "migration_disposition": row["migration_disposition"],
        }
        if row["migration_disposition"] == "ALREADY_PRESENT_NEW_CONTROL":
            active_mappings.append(mapping)
        else:
            terminal_history.append(mapping)

    surface = {
        "schema": "ENTERPRISE_MATH_CURRENT_CONTROL_PLANE_SURFACE_V1",
        "status": "ACTIVE_CANONICAL",
        "runtime_roots": [
            "infrastructure/cloudflare-supervisor/",
            "research_task_records/",
            "research_execution_records/",
            "research_result_records/",
            "research_result_reviews/",
            "research_control_dispatch.py",
            "control_plane/",
        ],
        "legacy_isolation_branch": ISOLATION_BRANCH,
        "legacy_files_present_on_main": False,
        "prompt_level_file_quarantine_required": False,
        "working_truth_granted": False,
        "foundation_authority_granted": False,
        "canonical_promotion_granted": False,
    }
    SURFACE.write_text(json.dumps(surface, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    migration = {
        "schema": "ENTERPRISE_MATH_LEGACY_CONTROL_PLANE_MIGRATION_V1",
        "status": "MIGRATED_AND_PHYSICALLY_ISOLATED",
        "isolation_branch": ISOLATION_BRANCH,
        "active_task_mappings": active_mappings,
        "terminal_history_only": terminal_history,
        "isolated_paths": isolation_paths,
        "prompt_changes": prompt_changes,
        "summary": {
            "active_tasks_mapped": len(active_mappings),
            "terminal_history_tasks": len(terminal_history),
            "isolated_file_count": len(isolation_paths),
            "prompt_file_count_simplified": len(prompt_changes),
        },
        "safety": {
            "immutable_evidence_rewritten": False,
            "history_preserved_on_isolation_branch": True,
            "working_truth_granted": False,
            "foundation_authority_granted": False,
            "canonical_promotion_granted": False,
        },
    }
    MIGRATION_JSON.parent.mkdir(parents=True, exist_ok=True)
    MIGRATION_JSON.write_text(json.dumps(migration, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Legacy control-plane migration — 2026-09-02",
        "",
        f"Isolation branch: `{ISOLATION_BRANCH}`",
        "",
        "## Result",
        "",
        f"- Active legacy tasks mapped to current immutable task records: {len(active_mappings)}",
        f"- Terminal/history-only task rows preserved off main: {len(terminal_history)}",
        f"- Legacy mutable/state files removed from main: {len(isolation_paths)}",
        f"- Prompt/router files simplified: {len(prompt_changes)}",
        "",
        "No immutable task, execution, result, review, Driver-authority, return, or research-artifact bytes were rewritten.",
        "",
        "## Isolated paths",
        "",
    ]
    lines.extend(f"- `{rp}`" for rp in isolation_paths)
    lines += ["", "## Active task mappings", ""]
    lines.extend(
        f"- `{row['task_id']}` -> {len(row['new_control_records'])} current record(s)"
        for row in active_mappings
    )
    if not active_mappings:
        lines.append("- None")
    lines += ["", "## Prompt simplification", ""]
    lines.extend(
        f"- `{row['path']}` — removed approximately {row['legacy_prompt_lines_removed']} legacy-quarantine line(s)"
        for row in prompt_changes
    )
    if not prompt_changes:
        lines.append("- None")
    MIGRATION_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    after_evidence = evidence_digest()
    if before_evidence != after_evidence:
        changed = sorted(set(before_evidence) | set(after_evidence))
        changed = [p for p in changed if before_evidence.get(p) != after_evidence.get(p)]
        raise RuntimeError(f"immutable evidence drift detected: {changed[:20]}")

    reference_errors = validate_no_live_references(isolation_paths)
    if reference_errors:
        raise RuntimeError("live references to isolated files remain: " + "; ".join(reference_errors[:20]))

    for row in prompt_changes:
        text = (ROOT / row["path"]).read_text(encoding="utf-8", errors="replace")
        if LEGACY_READ_RE.search(text):
            raise RuntimeError(f"legacy prompt-level read prohibition remains in {row['path']}")

    compile_result = run(sys.executable, "-m", "compileall", "-q", "control_plane", "tools", check=False)
    if compile_result.returncode != 0:
        raise RuntimeError("Python compile validation failed: " + compile_result.stderr[-4000:])

    print(json.dumps(migration["summary"], ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
