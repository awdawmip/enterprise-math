from __future__ import annotations

from control_plane import research_control_bootstrap
from control_plane import research_task_integrity_fault_isolation as isolation


EXPECTED = {
    "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-MINUS-FINITE-CLAUSEN-SWISHER-BRIDGE": "TP2-6649B392FDDD742C0275",
    "RS-NOLLM-EISENSTEIN-ROTATION-ATLAS": "TP2-983B1B8DB12B245368D9",
    "RS-SHOR-FAST-ROUGH-INTERVAL-GCD": "TP2-C193F8CB279ADF29D4ED",
    "RS-SIMPLE-LOOP-R4-MACRO-DEPTH-CLASSIFICATION": "TP2-9AB05574C3CA5534CB39",
}


def test_integrity_quarantines_are_exact_and_select_no_publication() -> None:
    rows = isolation.validated_quarantines()
    assert set(rows) == set(EXPECTED)
    for task_id, publication_id in EXPECTED.items():
        row = rows[task_id]
        assert row["publication_id"] == publication_id
        assert row["operational_publication_id"] is None
        assert row["working_truth_granted"] is False
        assert row["foundation_authority_granted"] is False
        assert row["canonical_promotion_granted"] is False
        assert row["successor_triggered"] is False


def test_exact_known_strict_audit_errors_are_fully_accounted_for() -> None:
    assert isolation.audit_task_records() == []


def test_integrity_quarantines_are_not_current_and_project_to_blocked() -> None:
    research_control_bootstrap.install()
    from tools import research_dispatch, research_task_records

    current = research_task_records.current_records()
    definitions = {item["task_id"]: item for item in research_dispatch.merged_definitions()}
    for task_id, publication_id in EXPECTED.items():
        assert task_id not in current
        item = definitions[task_id]
        assert item["base_state"] == "BLOCKED"
        assert item["publication_id"] is None
        assert item["publication_ids"] == [publication_id]
        assert item["registration_source"] == "TASK_INTEGRITY_QUARANTINE"
        assert item["hard_block"]["code"] == "INVALID_CURRENT_TASK_PUBLICATION"
        assert item["hard_block"]["operational_publication_id"] is None


def test_runtime_projection_audit_passes() -> None:
    assert isolation.audit_runtime_projection() == []
