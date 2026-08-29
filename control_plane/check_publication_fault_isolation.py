#!/usr/bin/env python3
"""Reference-integrity checker for task-local publication fault isolation."""
from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from control_plane import research_control_bootstrap  # noqa: E402
from control_plane import research_publication_fault_isolation as fork_isolation  # noqa: E402
from control_plane import research_task_integrity_fault_isolation as integrity_isolation  # noqa: E402
from control_plane import research_task_record_audit_fault_isolation as record_audit_isolation  # noqa: E402


def _audit_operational_publications(operational, isolated_tasks: set[str]) -> list[str]:
    """Validate operational selection from one cached publication snapshot.

    The historical selector's public ``selection()`` helper reloads all publication
    records for every task. That is appropriate for one interactive lookup but is
    quadratic when used as a repository-wide audit. This checker preserves its
    exact normalization rules while loading heads/resolutions/syntheses once.
    """
    errors: list[str] = []
    heads = operational.publication_heads(ROOT)
    resolutions = operational.resolution_map(ROOT)
    syntheses = operational.synthesis_map(ROOT)

    unknown_resolutions = sorted(set(resolutions) - set(heads))
    if unknown_resolutions:
        errors.append(
            f"publication resolution references task without active head: {unknown_resolutions}"
        )

    for task_id in sorted(heads):
        task_heads = heads[task_id]
        head_by_id = {str(item.get("publication_id")): item for item in task_heads}
        if len(head_by_id) != len(task_heads) or any(not key for key in head_by_id):
            errors.append(f"{task_id}: active head missing/duplicating publication_id")
            continue
        head_ids = set(head_by_id)
        row = resolutions.get(task_id)

        if task_id in isolated_tasks:
            if row is not None:
                errors.append(
                    f"{task_id}: locally isolated task cannot coexist with operational resolution"
                )
            continue

        if len(head_ids) == 1 and row is None:
            continue
        if row is None:
            errors.append(
                f"{task_id}: multiple active publication heads require explicit operational "
                f"selection; retained={sorted(head_ids)}"
            )
            continue
        try:
            operational._normalized_resolution(task_id, row, head_ids, syntheses)
        except Exception as exc:
            errors.append(str(exc))
    return errors


def audit() -> list[str]:
    errors: list[str] = []

    # Current-task integrity isolation runs first and may suppress only exact
    # defects on one pinned sole current head, projecting that task to BLOCKED.
    # A second, audit-only layer may then suppress exact remaining defects only
    # on independently nonoperational immutable records (directly superseded
    # history or a current head already blocked by unresolved fork quarantine).
    # The second layer never participates in runtime projection.
    task_record_errors = integrity_isolation.audit_task_records(ROOT)
    task_record_errors = record_audit_isolation.audit_against(task_record_errors, ROOT)
    if task_record_errors:
        return task_record_errors

    try:
        research_control_bootstrap.install(ROOT)
        import research_operational_publications as operational
        from tools import research_dispatch

        fork_quarantines = fork_isolation.validated_quarantines(ROOT)
        integrity_quarantines = integrity_isolation.validated_quarantines(ROOT)
        isolated_tasks = set(fork_quarantines) | set(integrity_quarantines)

        errors.extend(_audit_operational_publications(operational, isolated_tasks))

        definitions = research_dispatch.merged_definitions(ROOT)
        by_id = {item["task_id"]: item for item in definitions}
        now = datetime(2026, 8, 28, 8, 0, tzinfo=timezone.utc)
        state_by_id = {}
        for task_id in sorted(isolated_tasks):
            definition = by_id.get(task_id)
            if definition is None:
                errors.append(f"{task_id}: isolated task missing from dispatch definition view")
                continue
            state_by_id[task_id] = research_dispatch.reduce_definition(
                definition, [], now=now, root=ROOT
            )

        for task_id in isolated_tasks:
            if by_id.get(task_id, {}).get("base_state") != "BLOCKED":
                errors.append(f"{task_id}: dispatch definition is not locally BLOCKED")
            if state_by_id.get(task_id, {}).get("dispatch_state") != "BLOCKED":
                errors.append(f"{task_id}: effective dispatch state is not BLOCKED")
            if by_id.get(task_id, {}).get("publication_id") is not None:
                errors.append(f"{task_id}: locally isolated task selected publication_id")

        errors.extend(integrity_isolation.audit_runtime_projection(ROOT))
    except Exception as exc:
        errors.append(str(exc))
    return errors


def main() -> int:
    errors = audit()
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print(
        "PASS: strict publication integrity preserved with exact task-local "
        "fork/current-integrity isolation plus audit-only nonoperational record "
        "containment; no operational selection for isolated tasks."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
