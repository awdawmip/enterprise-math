#!/usr/bin/env python3
"""Verify the main-tree control surface after legacy physical isolation."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SURFACE = ROOT / "control_plane" / "current_control_plane_surface.json"
MIGRATION = ROOT / "control_plane" / "migrations" / "legacy-control-plane-migration-20260902.json"
LEGACY_READ_RE = re.compile(
    r"(?i)(do\s+not\s+read|must\s+not\s+read|never\s+read|禁止读取|不得读取|不要读取)"
    r".{0,160}(legacy|旧控制面|superseded|deprecated|旧状态机)|"
    r"(legacy|旧控制面|superseded|deprecated|旧状态机).{0,160}"
    r"(do\s+not\s+read|must\s+not\s+read|never\s+read|禁止读取|不得读取|不要读取)"
)
PROMPT_CANDIDATES = {
    "AGENTS.md", "00_BOOTSTRAP.md", "OPERATING_MANUAL.md",
    "PROJECT_BOOTSTRAP.md", "PROJECT_ROUTER.md",
}


def load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: JSON object required")
    return value


def main() -> int:
    errors: list[str] = []
    try:
        surface = load(SURFACE)
        migration = load(MIGRATION)
    except Exception as exc:
        print("ERROR:", exc)
        return 1

    if surface.get("schema") != "ENTERPRISE_MATH_CURRENT_CONTROL_PLANE_SURFACE_V1":
        errors.append("wrong current-control surface schema")
    if surface.get("status") != "ACTIVE_CANONICAL":
        errors.append("current-control surface is not ACTIVE_CANONICAL")
    if surface.get("legacy_files_present_on_main") is not False:
        errors.append("legacy_files_present_on_main must be false")
    if surface.get("prompt_level_file_quarantine_required") is not False:
        errors.append("prompt_level_file_quarantine_required must be false")
    if migration.get("status") != "MIGRATED_AND_PHYSICALLY_ISOLATED":
        errors.append("migration status is not terminal")
    if surface.get("legacy_isolation_branch") != migration.get("isolation_branch"):
        errors.append("isolation branch mismatch")

    isolated = migration.get("isolated_paths")
    if not isinstance(isolated, list) or not isolated:
        errors.append("isolated_paths must be a nonempty list")
        isolated = []
    for item in isolated:
        if not isinstance(item, str) or not item:
            errors.append("invalid isolated path")
            continue
        if (ROOT / item).exists():
            errors.append(f"isolated path still exists on main: {item}")

    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        if path.name not in PROMPT_CANDIDATES and "bootstrap" not in path.name.lower() and "prompt" not in path.as_posix().lower():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if LEGACY_READ_RE.search(text):
            errors.append(f"prompt-level legacy read prohibition remains: {path.relative_to(ROOT)}")

    for flag in ("working_truth_granted", "foundation_authority_granted", "canonical_promotion_granted"):
        if surface.get(flag) is not False:
            errors.append(f"surface cannot grant {flag}")
        if (migration.get("safety") or {}).get(flag) is not False:
            errors.append(f"migration cannot grant {flag}")

    if errors:
        for error in sorted(set(errors)):
            print("ERROR:", error)
        return 1
    print(
        "PASS: current control-plane surface is physical, legacy state is absent from main, "
        f"and {len(isolated)} isolated path(s) remain governed by the archive branch."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
