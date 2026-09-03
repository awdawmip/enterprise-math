#!/usr/bin/env python3
"""Derived Driver queue over immutable Result/review/follow-up authority.

This is a read-only selector.  It does not create CLAIMs, reviews, publications,
follow-up packets, Working Truth, or mathematical authority.  It exists so a
Driver does not have to scan PRs or replay the full Issue #240 event history to
find the next frozen Result that genuinely needs Driver action.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
_PRIORITY = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
_LEVERAGE = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
_PHASE = {"DRIVER_REVIEW": 0, "DRIVER_REVIEW_SYNTHESIS": 1, "DRIVER_FOLLOWUP": 2}


class DriverQueueError(ValueError):
    pass


def _head_publications(root: Path) -> dict[tuple[str, str], dict[str, Any]]:
    import research_operational_publications as operational

    out: dict[tuple[str, str], dict[str, Any]] = {}
    for task_id, heads in operational.publication_heads(root).items():
        for record in heads:
            publication_id = record.get("publication_id")
            if isinstance(publication_id, str) and publication_id:
                out[(task_id, publication_id)] = record
    return out


def _phase(state: dict[str, Any]) -> str:
    if state.get("review") is not None or state.get("driver_followup_state"):
        return "DRIVER_FOLLOWUP"
    parallel = state.get("review_parallel_state") or state.get("parallel_state")
    if parallel in {
        "AWAITING_REVIEW_REFERENCE_PASS_1",
        "AWAITING_REVIEW_REFERENCE_PASS_2",
        "AWAITING_REVIEW_SYNTHESIS",
        "AWAITING_RESULT_REVIEW_AUTHORITY",
    }:
        return "DRIVER_REVIEW_SYNTHESIS"
    return "DRIVER_REVIEW"


def queue(root: Path = ROOT) -> list[dict[str, Any]]:
    from control_plane import research_control_bootstrap

    research_control_bootstrap.install(root)

    from tools import research_result_records

    heads = _head_publications(root)
    results = research_result_records.iter_results(root)
    by_generation: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for result in results:
        task_id = result.get("task_id")
        publication_id = result.get("publication_id")
        if not isinstance(task_id, str) or not isinstance(publication_id, str):
            continue
        key = (task_id, publication_id)
        if key in heads:
            by_generation.setdefault(key, []).append(result)

    rows: list[dict[str, Any]] = []
    for key, generation_results in by_generation.items():
        task_id, publication_id = key
        state = research_result_records.task_result_state(
            task_id, root, publication_id=publication_id
        )
        if not isinstance(state, dict) or state.get("state") != "AWAITING_DRIVER_REVIEW":
            continue

        record = heads[key]
        ordered_results = sorted(
            generation_results,
            key=lambda item: (str(item.get("frozen_at") or ""), str(item.get("result_id") or "")),
        )
        result_ids = [
            str(item["result_id"])
            for item in ordered_results
            if isinstance(item.get("result_id"), str)
        ]
        terminal_verdicts = sorted(
            {
                str(item.get("terminal_verdict"))
                for item in ordered_results
                if item.get("terminal_verdict") is not None
            }
        )
        frozen_at = min(
            (str(item.get("frozen_at")) for item in ordered_results if item.get("frozen_at")),
            default="",
        )
        representative = ordered_results[-1]
        phase = _phase(state)
        row = {
            "phase": phase,
            "task_id": task_id,
            "publication_id": publication_id,
            "result_ids": result_ids,
            "terminal_verdicts": terminal_verdicts,
            "priority": str(record.get("effective_priority") or "P2").upper(),
            "leverage": str(record.get("effective_leverage") or "MEDIUM").upper(),
            "frozen_at": frozen_at,
            "researcher_id": representative.get("researcher_id"),
            "execution_record_id": representative.get("execution_record_id"),
            "claim_id": representative.get("claim_id"),
            "return_path": representative.get("return_path"),
            "execution_branch": representative.get("execution_branch"),
            "hard_target_disposition": representative.get("hard_target_disposition"),
            "next_control_plane_recommendation": representative.get(
                "next_control_plane_recommendation"
            ),
            "review_parallel_state": state.get("review_parallel_state"),
            "parallel_review_ids": state.get("parallel_review_ids"),
            "driver_followup_state": state.get("driver_followup_state"),
            "pending_result_review_ids": state.get("pending_result_review_ids"),
            "pending_result_followup_ids": state.get("pending_result_followup_ids"),
        }
        rows.append(row)

    rows.sort(
        key=lambda row: (
            _PHASE.get(str(row["phase"]), 9),
            _PRIORITY.get(str(row["priority"]), 9),
            _LEVERAGE.get(str(row["leverage"]), 9),
            str(row.get("frozen_at") or "9999"),
            str(row["task_id"]),
        )
    )
    return rows


def select(root: Path = ROOT, phase: str | None = None) -> dict[str, Any] | None:
    values = queue(root)
    if phase:
        values = [row for row in values if row.get("phase") == phase]
    return values[0] if values else None


def main() -> int:
    parser = argparse.ArgumentParser(description="Enterprise Math derived Driver action queue")
    sub = parser.add_subparsers(dest="command", required=True)
    show = sub.add_parser("list")
    show.add_argument("--limit", type=int, default=20)
    show.add_argument("--phase", choices=sorted(_PHASE))
    pick = sub.add_parser("select")
    pick.add_argument("--phase", choices=sorted(_PHASE))
    args = parser.parse_args()

    values = queue()
    if args.command == "list":
        if args.phase:
            values = [row for row in values if row.get("phase") == args.phase]
        limit = max(0, int(args.limit))
        print(json.dumps(values[:limit], ensure_ascii=False, indent=2, sort_keys=True))
        return 0

    value = select(phase=args.phase)
    print(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if value is not None else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except DriverQueueError as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
