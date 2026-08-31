from __future__ import annotations

import unittest

from control_plane import research_publication_fault_isolation as isolation


class PublicationFaultIsolationTests(unittest.TestCase):
    def test_unresolved_forks_select_no_operational_publication(self) -> None:
        rows = isolation.validated_quarantines()
        self.assertTrue(rows)
        for row in rows.values():
            self.assertIsNone(row["operational_publication_id"])
            self.assertGreaterEqual(len(set(row["publication_ids"])), 2)

    def test_unresolved_forks_are_omitted_from_current_record_selection(self) -> None:
        rows = isolation.validated_quarantines()
        current = isolation.isolated_current_records()
        self.assertTrue(current)
        for task_id in rows:
            self.assertNotIn(task_id, current)

    def test_unresolved_forks_project_to_task_local_blocks(self) -> None:
        rows = isolation.validated_quarantines()
        isolation.install()
        from tools import research_dispatch

        definitions = {
            item["task_id"]: item for item in research_dispatch.merged_definitions()
        }
        for task_id in rows:
            item = definitions[task_id]
            self.assertEqual(item["base_state"], "BLOCKED")
            self.assertIsNone(item["publication_id"])
            self.assertEqual(
                item["registration_source"], "PUBLICATION_FORK_QUARANTINE"
            )
            self.assertEqual(item["hard_block"]["code"], "UNRESOLVED_PUBLICATION_FORK")


if __name__ == "__main__":
    unittest.main()
