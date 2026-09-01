#!/usr/bin/env python3
"""Canonical control-plane bootstrap for resilient runtime views.

Order is intentional:
1. isolate unresolved immutable publication forks without selecting a head;
2. isolate exact pinned current task-integrity faults;
3. isolate exact stale result-review bindings from the operational review view;
4. isolate exact invalid immutable review records from operational authority;
5. isolate exact nonconforming Driver-review provenance from the operational view;
6. compose all nonoperational-review causes for follow-up isolation;
7. isolate follow-up packets and task heads derived solely from those reviews;
8. normalize every other isolated task to a state-machine-complete hard block;
9. expose fault-isolated operational task/publication audits while retaining
   explicit strict/raw audit handles;
10. leave every unrelated task/review under the original strict rules.

IMPORTANT LIVENESS BOUNDARY
---------------------------
This bootstrap repairs repository control views only. It is NOT a turn-level
watchdog and cannot preempt a model turn or an in-flight external tool call.
Repository PRE_FINAL liveness is therefore insufficient to guarantee that the
current conversation will return control to the user. A product/harness-level
PRE_TOOL/IN_TOOL/POST_TOOL deadman is required for physical enforcement.

Until such an external watchdog is installed, the control plane must be
reported as P0 OPEN for conversation-stall prevention even when repository
runtime, dispatch, recovery, and integrity gates are green.

This bootstrap grants no research, review, publication, Working Truth, Foundation,
or successor authority. Quarantine is exact and fail-closed: it may withhold
operational authority, never manufacture replacement authority.
"""
from __future__ import annotations

import copy
from pathlib import Path
from typing import Any

from control_plane import research_driver_followup_fault_isolation
from control_plane import research_driver_review_authority_fault_isolation
from control_plane import research_nonoperational_review_source_adapter
from control_plane import research_publication_fault_isolation
from control_plane import research_result_review_audit_fault_isolation
from control_plane import research_result_review_binding_fault_isolation
from control_plane import research_task_integrity_fault_isolation
from control_plane import research_task_record_audit_fault_isolation

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


def _install_operational_audit_views(root: Path) -> None:
    """Make post-bootstrap public audits match the operational runtime view.

    Strict/raw validators are preserved on ``strict_audit`` / ``strict_selection`` /
    ``strict_selections``. The public operational surface subtracts only errors
    pinned by exact validated quarantine records. New or drifted faults still
    fail closed.
    """
    from tools import research_task_records

    if not getattr(research_task_records, "_canonical_operational_audit_installed", False):
        base_task_audit = research_task_records.audit

        def task_audit(local_root: Path = research_task_records.ROOT) -> list[str]:
            raw = list(base_task_audit(local_root))
            current_suppressions = set(
                research_task_integrity_fault_isolation.suppression_strings(local_root)
            )
            after_current = [error for error in raw if error not in current_suppressions]
            return research_task_record_audit_fault_isolation.audit_against(
                after_current, local_root
            )

        research_task_records.strict_audit = base_task_audit
        research_task_records.audit = task_audit
        research_task_records._canonical_operational_audit_installed = True

    import research_operational_publications as operational

    if not getattr(operational, "_canonical_operational_view_installed", False):
        base_selection = operational.selection
        base_selections = operational.selections
        base_audit = operational.audit

        def isolated_ids(local_root: Path) -> set[str]:
            return set(research_publication_fault_isolation.validated_quarantines(local_root)) | set(
                research_task_integrity_fault_isolation.validated_quarantines(local_root)
            )

        def selection(task_id: str, local_root: Path = operational.ROOT):
            if task_id in isolated_ids(local_root):
                return None
            return base_selection(task_id, local_root)

        def selections(local_root: Path = operational.ROOT) -> dict[str, dict[str, Any]]:
            isolated = isolated_ids(local_root)
            tasks = set(operational.publication_heads(local_root))
            unknown_resolutions = sorted(set(operational.resolution_map(local_root)) - tasks)
            if unknown_resolutions:
                raise operational.OperationalPublicationError(
                    f"publication resolution references task without active head: {unknown_resolutions}"
                )
            out: dict[str, dict[str, Any]] = {}
            for task_id in sorted(tasks - isolated):
                value = base_selection(task_id, local_root)
                if value is not None:
                    out[task_id] = value
            return out

        def audit(local_root: Path = operational.ROOT) -> list[str]:
            errors: list[str] = []
            try:
                integrity_rows = research_task_integrity_fault_isolation.validated_quarantines(local_root)
                ignored_record_paths = {
                    row["record_path"]
                    for row in integrity_rows.values()
                    if isinstance(row.get("record_path"), str)
                }
                pubs = operational.iter_publications(local_root)
                for item in pubs:
                    prefix = item.get("_record_path", "<publication>")
                    if item.get("record_schema") != operational.RECORD_SCHEMA and prefix not in ignored_record_paths:
                        errors.append(f"{prefix}: wrong record_schema")
                selections(local_root)
            except Exception as exc:
                errors.append(str(exc))
            return errors

        operational.strict_selection = base_selection
        operational.strict_selections = base_selections
        operational.strict_audit = base_audit
        operational.selection = selection
        operational.selections = selections
        operational.audit = audit
        operational._canonical_operational_view_installed = True


def install(root: Path = ROOT) -> None:
    research_publication_fault_isolation.install(root)
    research_task_integrity_fault_isolation.install(root)
    research_result_review_binding_fault_isolation.install(root)
    research_result_review_audit_fault_isolation.install(root)
    research_driver_review_authority_fault_isolation.install(root)
    research_nonoperational_review_source_adapter.install(root)
    research_driver_followup_fault_isolation.install(root)

    from tools import research_dispatch

    if not getattr(research_dispatch, "_canonical_control_bootstrap_installed", False):
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

    _install_operational_audit_views(root)


if __name__ == "__main__":
    install()
    print("PASS: canonical control-plane runtime bootstrap installed.")
