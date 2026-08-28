from __future__ import annotations

from control_plane import research_publication_fault_isolation as isolation


def test_unresolved_fork_selects_no_operational_publication() -> None:
    rows = isolation.validated_quarantines()
    row = rows["RS-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M-PROOF"]
    assert row["operational_publication_id"] is None
    assert set(row["publication_ids"]) == {
        "TP2-4EE2618ABEBB6D097023",
        "TP2-5547117E54D7A556279B",
    }


def test_unresolved_fork_is_omitted_from_current_record_selection() -> None:
    current = isolation.isolated_current_records()
    assert "RS-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M-PROOF" not in current
    assert current  # unrelated task definitions still reduce normally


def test_unresolved_fork_projects_to_task_local_block() -> None:
    isolation.install()
    from tools import research_dispatch

    definitions = {item["task_id"]: item for item in research_dispatch.merged_definitions()}
    item = definitions["RS-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M-PROOF"]
    assert item["base_state"] == "BLOCKED"
    assert item["publication_id"] is None
    assert item["registration_source"] == "PUBLICATION_FORK_QUARANTINE"
    assert item["hard_block"]["code"] == "UNRESOLVED_PUBLICATION_FORK"
