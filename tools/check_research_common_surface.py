#!/usr/bin/env python3
"""Check that the shared theorem/tool router and Foundation backflow cannot drift.

This checker is intentionally mechanical. It does not decide whether a theorem
is true or whether a Python module is mathematically reusable. It enforces
objective synchronization of the common theorem/tool surface and the static
research-to-Foundation control-plane links. Live FQ and lease state remain on
GitHub Issues #164 and #240.
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
COMMON_JSON = ROOT / "research_common_surface.json"
FOUNDATION_JSON = ROOT / "foundation_steward.json"
BACKFLOW_JSON = ROOT / "foundation_backflow.json"
SCHEDULER_JSON = ROOT / "research_scheduler.json"
LEAN_ROOT = ROOT / "EnterpriseMath.lean"
COMMON_EN = ROOT / "docs" / "RESEARCH_COMMON_SURFACE.en.md"
COMMON_ZH = ROOT / "docs" / "RESEARCH_COMMON_SURFACE.zh-CN.md"
TOOLS_DIR = ROOT / "tools"

FQ_RE = re.compile(r"^FQ-\d{8}-\d{3}$")
ROLE_TO_KIND = {
    "RESEARCH": "RESEARCH",
    "STEWARD_VERIFICATION": "GOVERNANCE",
    "INTEGRATION": "GOVERNANCE",
}


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


def validate_backflow(backflow: dict[str, Any], scheduler: dict[str, Any]) -> list[str]:
    """Validate the static #82/#164/#240 backflow-to-scheduler routing contract."""
    errors: list[str] = []

    if backflow.get("schema") != "ENTERPRISE_MATH_FOUNDATION_BACKFLOW_V1":
        errors.append("unexpected foundation backflow schema")
    if backflow.get("status") != "ACTIVE":
        errors.append("foundation backflow router must be ACTIVE")

    surfaces = backflow.get("surfaces", {})
    authority = scheduler.get("authority", {})
    expected_surface_pairs = [
        ("research_relay_issue", "research_relay_issue"),
        ("foundation_problem_issue", "foundation_problem_issue"),
    ]
    for backflow_key, scheduler_key in expected_surface_pairs:
        if surfaces.get(backflow_key) != authority.get(scheduler_key):
            errors.append(
                f"surface mismatch: backflow {backflow_key}={surfaces.get(backflow_key)!r} "
                f"!= scheduler {scheduler_key}={authority.get(scheduler_key)!r}"
            )
    if surfaces.get("research_dispatch_issue") != scheduler.get("scheduler_issue"):
        errors.append("research dispatch issue does not match scheduler_issue")
    if surfaces.get("scheduler_config") != "research_scheduler.json":
        errors.append("backflow scheduler_config must be research_scheduler.json")

    required_packet = {
        "candidate_object_or_tool",
        "weakest_scope_hypotheses",
        "minimal_state",
        "minimal_repair_or_extension",
        "negative_boundary",
        "cross_route_evidence",
        "proof_status",
        "tool_surface",
        "prior_art_and_owner",
        "foundation_destination",
    }
    packet = backflow.get("feedback_packet_fields", [])
    if set(packet) != required_packet or len(packet) != len(required_packet):
        errors.append("Foundation Feedback Packet fields drifted from the canonical contract")

    handling = set(backflow.get("handling_classes", []))
    required_handling = {
        "DIRECT_FOUNDATION_MAINTENANCE",
        "FOUNDATION_QUESTION",
        "APPLICATION_LOCAL_OR_NOT_READY",
    }
    if handling != required_handling:
        errors.append("foundation handling classes drifted from the three-way classification")

    link_contract = backflow.get("scheduler_link_contract", {})
    question_field = link_contract.get("research_task_question_field")
    if question_field != "foundation_questions":
        errors.append("research_task_question_field must be 'foundation_questions'")

    task_by_id = {task.get("task_id"): task for task in scheduler.get("tasks", [])}
    seen_questions: set[str] = set()
    active_links = backflow.get("question_scheduler_links", [])
    for index, link in enumerate(active_links):
        prefix = f"question_scheduler_links[{index}]"
        question_id = link.get("question_id")
        if not isinstance(question_id, str) or not FQ_RE.fullmatch(question_id):
            errors.append(f"{prefix}: invalid question_id {question_id!r}")
            continue
        if question_id in seen_questions:
            errors.append(f"{prefix}: duplicate question link for {question_id}")
        seen_questions.add(question_id)

        task_id = link.get("scheduler_task_id")
        task = task_by_id.get(task_id)
        if task is None:
            errors.append(f"{prefix}: unknown scheduler task {task_id!r}")
            continue

        role = link.get("scheduler_role")
        expected_kind = ROLE_TO_KIND.get(role)
        if expected_kind is None:
            errors.append(f"{prefix}: invalid scheduler_role {role!r}")
        elif task.get("kind") != expected_kind:
            errors.append(
                f"{prefix}: role {role} requires task kind {expected_kind}, "
                f"got {task.get('kind')!r}"
            )

        if role == "RESEARCH":
            owner = link.get("research_owner")
            if owner != task.get("owner"):
                errors.append(
                    f"{prefix}: research_owner {owner!r} must match task owner {task.get('owner')!r}"
                )
            declared_questions = task.get(question_field, []) if isinstance(question_field, str) else []
            if not isinstance(declared_questions, list) or question_id not in declared_questions:
                errors.append(
                    f"{prefix}: research task {task_id!r} must explicitly declare "
                    f"{question_id!r} in foundation_questions"
                )

        refs = link.get("source_refs")
        if not isinstance(refs, list) or not refs or not all(
            isinstance(ref, str) and ref for ref in refs
        ):
            errors.append(f"{prefix}: source_refs must be a nonempty string list")

    canonical_examples = backflow.get("canonicalized_examples", [])
    canonical_ids: set[str] = set()
    for index, item in enumerate(canonical_examples):
        prefix = f"canonicalized_examples[{index}]"
        question_id = item.get("question_id")
        if not isinstance(question_id, str) or not FQ_RE.fullmatch(question_id):
            errors.append(f"{prefix}: invalid question_id {question_id!r}")
            continue
        if question_id in canonical_ids:
            errors.append(f"{prefix}: duplicate canonicalized example for {question_id}")
        canonical_ids.add(question_id)
        if question_id in seen_questions:
            errors.append(f"{prefix}: canonicalized question {question_id} remains actively scheduled")
        merge_ref = item.get("canonical_merge")
        if not isinstance(merge_ref, str) or not merge_ref:
            errors.append(f"{prefix}: canonical_merge must be a nonempty string")

    if backflow.get("authority_boundaries", {}).get("canonical_truth") != "gated source-repository main":
        errors.append("canonical truth boundary must remain gated source-repository main")

    return errors


def check() -> None:
    common = _load_json(COMMON_JSON)
    foundation = _load_json(FOUNDATION_JSON)
    backflow = _load_json(BACKFLOW_JSON)
    scheduler = _load_json(SCHEDULER_JSON)

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
    actual_lean = _lean_root_import_paths(LEAN_ROOT.read_text(encoding="utf-8"))
    declared_lean = sorted(common.get("lean_root_imports", []))
    _require_equal("Lean root import index", declared_lean, actual_lean)
    _require_human_visibility("English Lean root index", actual_lean, en_text)
    _require_human_visibility("Chinese Lean root index", actual_lean, zh_text)

    # 3. Every repository Python tool is shared operational infrastructure.
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

    # 5. Foundation backflow links are static control-plane contracts.
    backflow_errors = validate_backflow(backflow, scheduler)
    if backflow_errors:
        raise AssertionError("foundation backflow drift: " + "; ".join(backflow_errors))

    common_backflow = common.get("foundation_steward", {})
    if common_backflow.get("backflow_router") != "foundation_backflow.json":
        raise AssertionError("common surface must expose foundation_backflow.json")
    if common_backflow.get("backflow_validator") != "tools/check_research_common_surface.py":
        raise AssertionError("common surface must route backflow validation through the shared checker")

    print(
        "research common surface: OK "
        f"({len(actual_lean)} Lean root imports, {len(actual_tools)} repo tools, "
        f"{len(common_active)} active foundation questions, "
        f"{len(backflow.get('question_scheduler_links', []))} active FQ scheduler links)"
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