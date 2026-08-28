from __future__ import annotations

import unittest

from control_plane import research_publication_fault_isolation as isolation


class PublicationFaultIsolationTests(unittest.TestCase):
    def test_unresolved_fork_selects_no_operational_publication(self) -> None:
        rows = isolation.validated_quarantines()
        row = rows["RS-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M-PROOF"]
        self.assertIsNone(row["operational_publication_id"])
        self.assertEqual(
            set(row["publication_ids"]),
            {
                "TP2-4EE2618ABEBB6D097023",
                "TP2-5547117E54D7A556279B",
            },
        )

    def test_unresolved_fork_is_omitted_from_current_record_selection(self) -> None:
        current = isolation.isolated_current_records()
        self.assertNotIn(
            "RS-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M-PROOF", current
        )
        self.assertTrue(current)

    def test_unresolved_fork_projects_to_task_local_block(self) -> None:
        isolation.install()
        from tools import research_dispatch

        definitions = {
            item["task_id"]: item for item in research_dispatch.merged_definitions()
        }
        item = definitions["RS-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M-PROOF"]
        self.assertEqual(item["base_state"], "BLOCKED")
        self.assertIsNone(item["publication_id"])
        self.assertEqual(
            item["registration_source"], "PUBLICATION_FORK_QUARANTINE"
        )
        self.assertEqual(item["hard_block"]["code"], "UNRESOLVED_PUBLICATION_FORK")


if __name__ == "__main__":
    unittest.main()
