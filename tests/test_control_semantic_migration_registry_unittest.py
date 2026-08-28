import json
import unittest
from pathlib import Path

from control_plane import check_control_semantic_migration_registry as migration


ROOT = Path(__file__).resolve().parents[1]


class ControlSemanticMigrationRegistryTests(unittest.TestCase):
    def test_registered_control_debt_has_no_third_state_drift(self):
        reports = migration.check(ROOT)
        self.assertGreaterEqual(len(reports), 5)
        self.assertTrue(any("CSM-ARCHITECTURE-TASK-PUBLICATION-003" in row for row in reports))
        self.assertTrue(any("CSM-ROLEPOLICY-CANONICAL-DISPATCH-001" in row for row in reports))
        self.assertTrue(any("CSM-STEWARD-CANONICAL-DISPATCH-005" in row for row in reports))

    def test_mixed_semantics_are_not_marked_mechanically_safe(self):
        data = json.loads(
            (ROOT / "control_plane" / "control_semantic_migration_registry.json").read_text(
                encoding="utf-8"
            )
        )
        by_id = {row["migration_id"]: row for row in data["entries"]}
        self.assertEqual(
            "REQUIRES_GOVERNANCE_VERIFICATION",
            by_id["CSM-ARCHITECTURE-TASK-PUBLICATION-003"]["state"],
        )
        self.assertEqual(
            "MIXED_MATHEMATICAL_GOVERNANCE_FILE",
            by_id["CSM-ARCHITECTURE-TASK-PUBLICATION-003"]["risk_class"],
        )
        self.assertFalse(
            by_id["CSM-ARCHITECTURE-TASK-PUBLICATION-003"]["execution_authority_while_open"]
        )

    def test_low_risk_pointers_migrated_but_ambiguous_nested_dispatch_remains_blocked(self):
        data = json.loads(
            (ROOT / "control_plane" / "control_semantic_migration_registry.json").read_text(
                encoding="utf-8"
            )
        )
        by_id = {row["migration_id"]: row for row in data["entries"]}
        self.assertEqual(
            "TARGET_MIGRATED",
            by_id["CSM-ROLEPOLICY-CANONICAL-DISPATCH-001"]["state"],
        )
        self.assertEqual(
            "TARGET_MIGRATED",
            by_id["CSM-STEWARD-CANONICAL-DISPATCH-005"]["state"],
        )
        self.assertEqual(
            "REQUIRES_GOVERNANCE_VERIFICATION",
            by_id["CSM-ROLEPOLICY-PUBLICATION-DISPATCH-002"]["state"],
        )
        self.assertIn(
            "ONLY /canonical_dispatch CHANGED",
            by_id["CSM-ROLEPOLICY-CANONICAL-DISPATCH-001"]["migration_scope"],
        )
        self.assertIn(
            "backflow.task_definition_authority",
            by_id["CSM-STEWARD-CANONICAL-DISPATCH-005"]["migration_scope"],
        )


if __name__ == "__main__":
    unittest.main()
