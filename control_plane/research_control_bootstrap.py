#!/usr/bin/env python3
"""Canonical control-plane bootstrap for resilient runtime views.

Order is intentional:
1. isolate unresolved immutable publication forks without selecting a head;
2. isolate exact pinned current task-integrity faults;
3. isolate exact nonconforming Driver-review provenance from the operational view;
4. normalize every isolated task to a state-machine-complete hard block;
5. leave every unrelated task/review under the original strict rules.

This bootstrap grants no research, review, publication, Working Truth, Foundation,
or successor authority.
"""
from __future__ import annotations

import copy
from pathlib import Path
from typing import Any

from control_plane import research_driver_review_authority_fault_isolation
from control_plane import research_publication_fault_isolation
from control_plane import research_task_integrity_fault_isolation

ROOT = Path(__file__).resolve().parents[1]


def _complete_quarantine_block(
    definition: dict[str, Any], *, kind: str
) -> dict[str, Any]:
    value = copy.deepcopy(definition)
    prior = value.get("hard_block")
    details = copy.deepcopy(prior) if isinstance(prior, dict) else {}
    if kind == "PUBLICATION_FORK":
        missing_object = "one authority-valid operational publication selection for the unresolved retained head set"
        owner = "control-plane/publication-fork-resolution"
        unblock = (
            "Complete the ordinary parallel-publication resolution contract, remove the exact fork "
            "quarantine, and re-run canonical integrity gates."
        )
    else:
        missing_object = "one current task publication that passes the strict immutable-task publication contract"
        owner = "control-plane/task-publication-repair"
        unblock = (
            "Repair or republish the exact task through ordinary publication authority, remove the "
            "exact integrity quarantine, and re-run canonical integrity gates."
        )
    details.update(
        {
            "missing_object": missing_object,
            "owner": owner,
            "necessity": (
                "The task must not be selected or claimed while its current publication authority "
                "is ambiguous or fails the strict task-publication contract."
            ),
            "unblock_condition": unblock,
        }
    )
    value["base_state"] = "BLOCKED"
    value["hard_block"] = details
    return value


def install(root: Path = ROOT) -> None:
    research_publication_fault_isolation.install(root)
    research_task_integrity_fault_isolation.install(root)
    research_driver_review_authority_fault_isolation.install(root)

    from tools import research_dispatch

    if getattr(research_dispatch, "_canonical_control_bootstrap_installed", False):
        return
    base_merged = research_dispatch.merged_definitions

    def merged_definitions(local_root: Path = research_dispatch.ROOT) -> list[dict[str, Any]]:
        values = base_merged(local_root)
        fork_ids = set(research_publication_fault_isolation.validated_quarantines(local_root))
        integrity_ids = set(research_task_integrity_fault_isolation.validated_quarantines(local_root))
        out: list[dict[str, Any]] = []
        for item in values:
            task_id = item.get("task_id") if isinstance(item, dict) else None
            if task_id in fork_ids:
                out.append(_complete_quarantine_block(item, kind="PUBLICATION_FORK"))
            elif task_id in integrity_ids:
                out.append(_complete_quarantine_block(item, kind="TASK_INTEGRITY"))
            else:
                out.append(item)
        return out

    research_dispatch.merged_definitions = merged_definitions
    research_dispatch._canonical_control_bootstrap_installed = True


if __name__ == "__main__":
    install()
    print("PASS: canonical control-plane runtime bootstrap installed.")
