#!/usr/bin/env python3
"""Check that the shared theorem/tool router cannot silently drift from main.

This checker is intentionally mechanical.  It does not decide whether a theorem
is true or whether a Python module is mathematically reusable.  It only enforces
that already-declared shared assets remain discoverable and that two canonical
surfaces with objective membership -- root Lean imports and repository tools --
are synchronized with ``research_common_surface.json`` and the bilingual human
router.
"""

from __future__ import annotations

import json
from pathlib import Path
import sys
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
COMMON_JSON = ROOT / "research_common_surface.json"
FOUNDATION_JSON = ROOT / "foundation_steward.json"
LEAN_ROOT = ROOT / "EnterpriseMath.lean"
COMMON_EN = ROOT / "docs" / "RESEARCH_COMMON_SURFACE.en.md"
COMMON_ZH = ROOT / "docs" / "RESEARCH_COMMON_SURFACE.zh-CN.md"
TOOLS_DIR = ROOT / "tools"


def _load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _lean_root_import_paths(text: str) -> list[str]:
    paths: list[str] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line.startswith("import EnterpriseMath."):
            continue
        module = line.split(maxsplit=1)[1]
        paths.append(module.replace(".", "/") + ".lean")
    return sorted(paths)


def _repo_python_tools() -> list[str]:
    return sorted(
        path.relative_to(ROOT).as_posix()
        for path in TOOLS_DIR.glob("*.py")
        if path.is_file()
    )


def _declared_paths(common: dict) -> Iterable[str]:
    modules = common.get("canonical_executable_modules", {})
    for family, entries in modules.items():
        if not isinstance(entries, list):
            raise AssertionError(
                f"canonical_executable_modules[{family!r}] must be a list"
            )
        for entry in entries:
            if not isinstance(entry, str):
                raise AssertionError(
                    f"canonical_executable_modules[{family!r}] contains a non-string"
                )
            yield entry

    for entry in common.get("tool_roots", {}).get("repo_tools", []):
        if not isinstance(entry, str):
            raise AssertionError("tool_roots.repo_tools contains a non-string")
        yield entry


def _require_equal(label: str, declared: list[str], actual: list[str]) -> None:
    if declared == actual:
        return
    declared_set = set(declared)
    actual_set = set(actual)
    missing = sorted(actual_set - declared_set)
    stale = sorted(declared_set - actual_set)
    raise AssertionError(
        f"{label} drift: missing_from_common_surface={missing}; "
        f"stale_in_common_surface={stale}"
    )


def _require_human_visibility(label: str, entries: Iterable[str], text: str) -> None:
    missing = [entry for entry in entries if entry not in text]
    if missing:
        raise AssertionError(f"{label} missing shared-surface entries: {missing}")


def check() -> None:
    common = _load_json(COMMON_JSON)
    foundation = _load_json(FOUNDATION_JSON)

    if common.get("schema") != "ENTERPRISE_MATH_COMMON_RESEARCH_SURFACE_V1":
        raise AssertionError("unexpected research_common_surface schema")

    en_text = COMMON_EN.read_text(encoding="utf-8")
    zh_text = COMMON_ZH.read_text(encoding="utf-8")

    # 1. Every explicitly registered executable/tool path must still exist.
    missing_paths = sorted(
        entry for entry in set(_declared_paths(common)) if not (ROOT / entry).exists()
    )
    if missing_paths:
        raise AssertionError(f"registered shared paths do not exist: {missing_paths}")

    # 2. Root Lean imports are objective canonical formalization membership.
    #    Keep an exact machine index so a newly imported proof cannot become
    #    canonical while remaining invisible to shared preflight.
    actual_lean = _lean_root_import_paths(LEAN_ROOT.read_text(encoding="utf-8"))
    declared_lean = sorted(common.get("lean_root_imports", []))
    _require_equal("Lean root import index", declared_lean, actual_lean)
    _require_human_visibility("English Lean root index", actual_lean, en_text)
    _require_human_visibility("Chinese Lean root index", actual_lean, zh_text)

    # 3. Every repository Python tool is shared operational infrastructure.
    #    Exact enumeration prevents new governance/checking tools from being
    #    added without becoming discoverable to every route.
    actual_tools = _repo_python_tools()
    declared_tools = sorted(common.get("tool_roots", {}).get("repo_tools", []))
    _require_equal("repository tool index", declared_tools, actual_tools)
    _require_human_visibility("English repository tool index", actual_tools, en_text)
    _require_human_visibility("Chinese repository tool index", actual_tools, zh_text)

    # 4. The steward and common router must expose the same active FQ set.
    foundation_active = sorted(
        foundation.get("problem_set", {}).get("active_questions", [])
    )
    common_active = sorted(
        common.get("foundation_steward", {}).get("active_foundation_questions", [])
    )
    _require_equal("active foundation-question index", common_active, foundation_active)
    _require_human_visibility("English active FQ index", foundation_active, en_text)
    _require_human_visibility("Chinese active FQ index", foundation_active, zh_text)

    alerts = set(common.get("tool_scope_alerts", {}))
    active = set(common_active)
    if not alerts <= active:
        raise AssertionError(
            "tool_scope_alerts contains resolved/non-active FQ IDs: "
            f"{sorted(alerts - active)}"
        )

    print(
        "research common surface: OK "
        f"({len(actual_lean)} Lean root imports, {len(actual_tools)} repo tools, "
        f"{len(common_active)} active foundation questions)"
    )


def main() -> int:
    try:
        check()
    except (AssertionError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(f"research common surface: FAIL: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
