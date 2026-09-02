#!/usr/bin/env python3
"""One-shot safe renderer for the immutable legacy-to-V2 task cutover."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from control_plane import materialize_legacy_tasks_v2 as migration


def safe_body_for(task: dict, state: dict, disposition: str) -> str:
    task_id = str(task["task_id"])
    runtime_state = str(state.get("state") or task.get("base_state") or "BACKLOG")
    if disposition == "TERMINAL_HISTORY":
        target = (
            "Preserve the verified terminal outcome as immutable nonclaimable history. "
            "This generation cannot authorize a new execution."
        )
        success = (
            "The V2 record preserves task identity and terminal state, remains nonclaimable, "
            "and creates no owner or execution event."
        )
    elif disposition == "BACKLOG":
        target = (
            "Preserve the dormant frontier as an immutable nonclaimable backlog generation. "
            "A later explicit publication is required before activation."
        )
        success = (
            "The V2 record keeps the exact dormant state and does not enter fresh selection."
        )
    else:
        target = (
            "Preserve the verified durable frontier as a claimable V2 generation without "
            "changing mathematical scope or creating an owner event."
        )
        success = (
            "The V2 record preserves task identity, owner boundary, priority class, frontier, "
            "and next action while creating no synthetic execution ownership."
        )
    return f"""# {task_id} — V2 Task Preservation

Status: `PUBLISHED_REGISTERED / CONTROL_MIGRATION / {runtime_state}`

## Mother question

Can this exact task be represented on the immutable V2 task surface without changing its mathematical meaning or durable frontier?

## Frozen inputs and scope

The exact source definition, task metadata, frontier, references, owner boundary, and durable state are frozen in the accompanying metadata and migration record. They are not expanded or reinterpreted in this preservation body.

This preservation envelope adds no theorem, counterexample, novelty conclusion, priority elevation, truth status, or execution ownership.

## Hard target and required outputs

{target}

## Research value to preserve

Preserve the exact identity, lineage, accumulated evidence, durable frontier, and next executable action without replaying completed work.

## Success, kill, and return criteria

{success}

Return the immutable V2 publication record and its migration-manifest row after repository integrity checks pass. Mathematical execution and review remain separate actions.
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--comments", type=Path, required=True)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    migration.body_for = safe_body_for
    migration.run(args.comments, check_only=args.check)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
