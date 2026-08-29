#!/usr/bin/env python3
"""Fail-closed lineage proof for moving unresolved publication forks.

A lineage-forward quarantine does not select an operational publication.  It pins
exact post-fork anchor publications and permits each anchor to advance only along
a unique, non-branching supersedes chain.  Any new sibling, unanchored active
head, broken ancestry, cycle, or ambiguous head partition fails closed.

This module is control-plane topology only.  It does not inspect or compare task
mathematics, review dispositions, Working Truth, Foundation status, or theorem
truth.
"""
from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


class LineageForwardSafetyError(ValueError):
    pass


def records_for_task(task_id: str, root: Path = ROOT) -> dict[str, dict[str, Any]]:
    from control_plane import research_task_records_impl as core

    out: dict[str, dict[str, Any]] = {}
    for row in core.iter_records(root):
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


def active_heads(records: dict[str, dict[str, Any]]) -> set[str]:
    from control_plane import research_task_records_impl as core

    superseded = {
        row.get("supersedes_publication_id")
        for row in records.values()
        if isinstance(row.get("supersedes_publication_id"), str)
        and row.get("supersedes_publication_id")
    }
    return {
        publication_id
        for publication_id, row in records.items()
        if publication_id not in superseded
        and row.get("record_state", "ACTIVE") not in core.TERMINAL_RECORD_STATES
    }


def prove(task_id: str, anchors: list[str], root: Path = ROOT) -> dict[str, Any]:
    if len(anchors) < 2 or len(set(anchors)) != len(anchors):
        raise LineageForwardSafetyError("at least two distinct lineage anchors are required")

    records = records_for_task(task_id, root)
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

    # Once a post-fork branch is anchored it must remain a single chain.  Even a
    # historical sibling below the anchor is enough to reject this tracking mode.
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

    heads = active_heads(records)
    head_to_anchor: dict[str, str] = {}
    anchor_to_heads: dict[str, list[str]] = {anchor: [] for anchor in anchors}

    for head in sorted(heads):
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

    for anchor, lineage_heads in anchor_to_heads.items():
        if len(lineage_heads) != 1:
            raise LineageForwardSafetyError(
                f"{task_id}: anchor {anchor} must have exactly one active descendant head; "
                f"got {lineage_heads}"
            )

    return {
        "task_id": task_id,
        "lineage_anchor_publication_ids": list(anchors),
        "current_active_head_publication_ids": sorted(heads),
        "head_to_anchor": head_to_anchor,
        "anchor_to_current_head": {
            anchor: lineage_heads[0]
            for anchor, lineage_heads in anchor_to_heads.items()
        },
        "operational_publication_selected": False,
        "working_truth_granted": False,
        "foundation_authority_granted": False,
        "canonical_promotion_granted": False,
        "successor_triggered": False,
    }
