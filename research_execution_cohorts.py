#!/usr/bin/env python3
"""Audit optional Enterprise Math parallel execution cohorts."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
COHORT_ROOT = ROOT / "research_execution_cohorts"
SCHEMA = "ENTERPRISE_MATH_PARALLEL_EXECUTION_COHORT_V1"
STATES = {"ACTIVE", "COMPLETE", "CLOSED"}
LANE_ROLES = {"RESEARCH", "REPLICATION", "AUDIT"}
ID_RE = re.compile(r"^[A-Za-z0-9._-]+$")


class CohortError(ValueError):
    pass


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise CohortError(f"{path}: JSON root must be object")
    return value


def publication_map(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    directory = root / "research_task_records"
    if not directory.exists():
        return out
    for path in sorted(directory.glob("*/*.json")):
        item = _load(path)
        pid = item.get("publication_id")
        if isinstance(pid, str) and pid:
            if pid in out:
                raise CohortError(f"duplicate publication_id: {pid}")
            out[pid] = item
    return out


def iter_cohorts(root: Path = ROOT) -> list[dict[str, Any]]:
    directory = root / "research_execution_cohorts"
    if not directory.exists():
        return []
    out: list[dict[str, Any]] = []
    for path in sorted(directory.glob("*/*.json")):
        item = _load(path)
        item["_path"] = path.relative_to(root).as_posix()
        out.append(item)
    return out


def _safe_id(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value or not ID_RE.fullmatch(value):
        raise CohortError(f"{label} invalid")
    return value


def _safe_prefix(value: Any) -> str:
    if not isinstance(value, str) or not value.strip():
        raise CohortError("lane output_prefix required")
    text = value.strip().replace("\\", "/")
    path = Path(text)
    if path.is_absolute() or ".." in path.parts or not text.endswith("/"):
        raise CohortError("lane output_prefix must be safe repository-relative directory ending in /")
    return text


def _prefixes_overlap(left: str, right: str) -> bool:
    return left == right or left.startswith(right) or right.startswith(left)


def cohort_map(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for item in iter_cohorts(root):
        cid = item.get("cohort_id")
        if isinstance(cid, str) and cid:
            if cid in out:
                raise CohortError(f"duplicate cohort_id: {cid}")
            out[cid] = item
    return out


def lane(task_id: str, cohort_id: str, lane_id: str, root: Path = ROOT) -> dict[str, Any]:
    cohort = cohort_map(root).get(cohort_id)
    if cohort is None or cohort.get("task_id") != task_id:
        raise CohortError("unknown cohort for task")
    matches = [row for row in cohort.get("lanes", []) if isinstance(row, dict) and row.get("lane_id") == lane_id]
    if len(matches) != 1:
        raise CohortError("unknown or ambiguous execution lane")
    return matches[0]


def audit(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    try:
        pubs = publication_map(root)
        cohorts = iter_cohorts(root)
    except Exception as exc:
        return [str(exc)]
    seen_cohorts: set[str] = set()
    active_lane_keys: set[tuple[str, str]] = set()
    for item in cohorts:
        prefix = item.get("_path", "<cohort>")
        try:
            if item.get("schema") != SCHEMA:
                raise CohortError("wrong cohort schema")
            cid = _safe_id(item.get("cohort_id"), "cohort_id")
            task_id = _safe_id(item.get("task_id"), "task_id")
            if cid in seen_cohorts:
                raise CohortError("duplicate cohort_id")
            seen_cohorts.add(cid)
            state = item.get("record_state")
            if state not in STATES:
                raise CohortError("invalid record_state")
            lanes = item.get("lanes")
            if not isinstance(lanes, list) or len(lanes) < 2:
                raise CohortError("parallel cohort requires at least two lanes")
            lane_ids: set[str] = set()
            lane_prefixes: list[str] = []
            for index, row in enumerate(lanes):
                if not isinstance(row, dict):
                    raise CohortError(f"lanes[{index}] must be object")
                lid = _safe_id(row.get("lane_id"), f"lanes[{index}].lane_id")
                if lid in lane_ids:
                    raise CohortError(f"duplicate lane_id {lid}")
                lane_ids.add(lid)
                if state == "ACTIVE":
                    key = (task_id, lid)
                    if key in active_lane_keys:
                        raise CohortError(f"active lane reused across cohorts: {lid}")
                    active_lane_keys.add(key)
                pid = row.get("publication_id")
                publication = pubs.get(pid)
                if publication is None:
                    raise CohortError(f"unknown lane publication_id {pid}")
                if publication.get("task_id") != task_id:
                    raise CohortError(f"lane publication belongs to different task: {pid}")
                if row.get("lane_role") not in LANE_ROLES:
                    raise CohortError(f"invalid lane_role for {lid}")
                if not isinstance(row.get("purpose"), str) or not row["purpose"].strip():
                    raise CohortError(f"lane purpose missing for {lid}")
                output_prefix = _safe_prefix(row.get("output_prefix"))
                for prior in lane_prefixes:
                    if _prefixes_overlap(output_prefix, prior):
                        raise CohortError(f"lane output namespaces overlap: {output_prefix} / {prior}")
                lane_prefixes.append(output_prefix)
            if item.get("two_reference_passes_required") is not True:
                raise CohortError("parallel cohort requires two_reference_passes_required=true")
            if item.get("synthesis_required") is not True:
                raise CohortError("parallel cohort requires synthesis_required=true")
            if not isinstance(item.get("opened_by"), str) or not item["opened_by"].strip():
                raise CohortError("opened_by missing")
            if not isinstance(item.get("opened_at"), str) or not item["opened_at"].strip():
                raise CohortError("opened_at missing")
            if item.get("working_truth_granted") is not False or item.get("canonical_promotion_granted") is not False:
                raise CohortError("cohort cannot grant truth/promotion")
        except Exception as exc:
            errors.append(f"{prefix}: {exc}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Enterprise Math parallel execution cohort audit")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("audit")
    show = sub.add_parser("lane")
    show.add_argument("--task-id", required=True)
    show.add_argument("--cohort-id", required=True)
    show.add_argument("--lane-id", required=True)
    args = parser.parse_args()
    if args.command == "audit":
        errors = audit()
        if errors:
            for error in errors:
                print("ERROR:", error)
            return 1
        print(f"PASS: parallel execution cohorts valid ({len(iter_cohorts())} cohort(s)).")
        return 0
    print(json.dumps(lane(args.task_id, args.cohort_id, args.lane_id), ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except CohortError as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
