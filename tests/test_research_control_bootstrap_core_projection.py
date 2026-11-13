"""Regression: the native inventory must consume installed control gates.

The original Source publications remain immutable historical bytes. A packet
isolated for invalid Driver authority is not claimable, but its Task must
remain visible to maintenance as BLOCKED in the canonical dispatch view.
"""
from datetime import datetime, timezone
import unittest

from control_plane import research_control_bootstrap
from tools import research_dispatch, research_dispatch_core


TARGETS = {
    "RS-N-COUPLED-CRT-PRODUCT-NATURALITY-BREAK-WITHOUT-SUPPORT-EXPOSURE",
    "RS-N-COUPLED-NONRING-SINGULARIZATION-PRIOR-ART-AUDIT",
}


class BootstrapCoreProjectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        research_control_bootstrap.install()

    def test_core_inventory_uses_the_fully_installed_control_gates(self):
        self.assertIs(
            research_dispatch_core.merged_definitions,
            research_dispatch.merged_definitions,
        )
        self.assertIs(
            research_dispatch_core.reduce_definition,
            research_dispatch.reduce_definition,
        )

    def test_quarantined_followup_tasks_are_blocked_not_invisible(self):
        definitions = {
            row["task_id"]: row
            for row in research_dispatch.merged_definitions()
        }
        self.assertTrue(TARGETS <= definitions.keys())
        for task_id in TARGETS:
            definition = definitions[task_id]
            self.assertEqual("BLOCKED", definition["base_state"])
            self.assertIsNone(definition["publication_id"])
            self.assertEqual(
                "DRIVER_FOLLOWUP_AUTHORITY_QUARANTINE",
                definition["registration_source"],
            )
            self.assertEqual(
                "NONOPERATIONAL_SOURCE_REVIEW_FOLLOWUP",
                definition["hard_block"]["code"],
            )

        states = {
            row["task_id"]: row
            for row in research_dispatch.effective_states(
                [], now=datetime(2026, 11, 13, tzinfo=timezone.utc),
            )
        }
        self.assertTrue(TARGETS <= states.keys())
        for task_id in TARGETS:
            self.assertEqual("BLOCKED", states[task_id]["dispatch_state"])
            self.assertIsNone(states[task_id]["publication_id"])
            self.assertIsNone(states[task_id]["claim_id"])


if __name__ == "__main__":
    unittest.main()
