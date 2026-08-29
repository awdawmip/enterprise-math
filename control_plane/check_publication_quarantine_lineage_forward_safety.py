#!/usr/bin/env python3
"""Prove that a publication-fork quarantine can follow only linear descendants.

This module is evidence-only.  It does not modify the quarantine registry and it
selects no publication as operational.  Given a task and exact post-fork anchor
publication ids, it proves that each anchor has exactly one current active head
reachable through a single-child supersedes chain and that every current active
head belongs to exactly one anchored lineage.

The proof fails closed on:
- any new unanchored active head;
- branching below an anchor, even if one child later becomes non-current;
- a missing anchor;
- cycles or broken supersedes ancestry;
- two anchors converging onto the same current head;
- any ambiguity in the current head partition.

This is control-plane topology only.  It does not compare task content, research
quality, Driver decisions, Working Truth, Foundation status, or theorem truth.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


class LineageForwardSafetyError(ValueError):
    pass


def _records(task_id: str, root: Path = ROOT) -> dict[str, dict[str, Any]]:
    from tools import research_task_records

    out: dict[str, dict[str, Any]] = {}
    for row in research_task_records.iter_records(root):
        if row.get("task_id") != task_id:
            continue
        publication_id = row.get("publication_id")
        if not isinstance(publication_id, str) or not publication_id:
            raise LineageForwardSafetyError(f"{task_id}: record missing publication_id")
        if publication_id in out:
            raise LineageForwardSafetyError(f"{task_id}: duplicate publication_id {publication_id}")
        out[publication_id] = row
    if not out:
        raise LineageForwardSafetyError(f"{task_id}: no immutable publication records")
    return out


def _active_heads(records: dict[str, dict[str, Any]]) -> set[str]:
    from tools import research_task_records

    superseded = {
        row.get("supersedes_publication_id")
        for row in records.values()
        if isinstance(row.get("supersedes_publication_id"), str)
        and row.get("supersedes_publication_id")
    }
    terminal = set(research_task_records.TERMINAL_RECORD_STATES)
    return {
        publication_id
        for publication_id, row in records.items()
        if publication_id not in superseded
        and row.get("record_state", "ACTIVE") not in terminal
    }


def prove(task_id: str, anchors: list[str], root: Path = ROOT) -> dict[str, Any]:
    if len(anchors) < 2 or len(set(anchors)) != len(anchors):
        raise LineageForwardSafetyError("at least two distinct lineage anchors are required")

    records = _records(task_id, root)
    missing = [anchor for anchor in anchors if anchor not in records]
    if missing:
        raise LineageForwardSafetyError(f"{task_id}: missing anchor publication(s): {missing}")

    children: dict[str, list[str]] = defaultdict(list)
    for publication_id, row in records.items():
        parent = row.get("supersedes_publication_id")
        if parent is None:
            continue
        if not isinstance(parent, str) or not parent:
            raise LineageForwardSafetyError(
                f"{task_id}: {publication_id} has malformed supersedes_publication_id"
            )
        if parent not in records:
            raise LineageForwardSafetyError(
                f"{task_id}: {publication_id} supersedes unknown publication {parent}"
            )
        children[parent].append(publication_id)

    # Once a fork branch is anchored, it must remain a single chain. Historical
    # sibling creation below the anchor is enough to reject lineage-forward mode.
    for anchor in anchors:
        stack = [anchor]
        seen: set[str] = set()
        while stack:
            publication_id = stack.pop()
            if publication_id in seen:
                raise LineageForwardSafetyError(
                    f"{task_id}: cycle in anchored lineage at {publication_id}"
                )
            seen.add(publication_id)
            branch_children = children.get(publication_id, [])
            if len(branch_children) > 1:
                raise LineageForwardSafetyError(
                    f"{task_id}: anchored lineage branches below {publication_id}: "
                    f"{sorted(branch_children)}"
                )
            stack.extend(branch_children)

    active_heads = _active_heads(records)
    head_to_anchor: dict[str, str] = {}
    anchor_to_heads: dict[str, list[str]] = {anchor: [] for anchor in anchors}

    for head in sorted(active_heads):
        current = head
        seen: set[str] = set()
        matched: list[str] = []
        while True:
            if current in seen:
                raise LineageForwardSafetyError(f"{task_id}: ancestry cycle from head {head}")
            seen.add(current)
            if current in anchors:
                matched.append(current)
            parent = records[current].get("supersedes_publication_id")
            if not isinstance(parent, str) or not parent:
                break
            if parent not in records:
                raise LineageForwardSafetyError(
                    f"{task_id}: ancestry from {head} reaches unknown parent {parent}"
                )
            current = parent

        if len(matched) != 1:
            raise LineageForwardSafetyError(
                f"{task_id}: active head {head} belongs to {len(matched)} anchored lineages: {matched}"
            )
        anchor = matched[0]
        head_to_anchor[head] = anchor
        anchor_to_heads[anchor].append(head)

    for anchor, heads in anchor_to_heads.items():
        if len(heads) != 1:
            raise LineageForwardSafetyError(
                f"{task_id}: anchor {anchor} must have exactly one active descendant head; got {heads}"
            )

    if set(head_to_anchor) != active_heads:
        raise LineageForwardSafetyError(f"{task_id}: active head partition is incomplete")

    return {
        "status": "SAFE_LINEAR_DESCENDANT_FORWARD_EVIDENCE_ONLY",
        "task_id": task_id,
        "lineage_anchor_publication_ids": anchors,
        "current_active_head_publication_ids": sorted(active_heads),
        "head_to_anchor": head_to_anchor,
        "anchor_to_current_head": {
            anchor: heads[0] for anchor, heads in anchor_to_heads.items()
        },
        "operational_publication_selected": False,
        "working_truth_granted": False,
        "foundation_authority_granted": False,
        "canonical_promotion_granted": False,
        "successor_triggered": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--task-id", required=True)
    parser.add_argument("--anchor", action="append", required=True)
    args = parser.parse_args()
    try:
        evidence = prove(args.task_id, args.anchor)
    except (LineageForwardSafetyError, OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}")
        return 1
    print(json.dumps(evidence, ensure_ascii=False, indent=2, sort_keys=True))
    print("PASS: anchored publication fork advances only through unique linear descendants.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
