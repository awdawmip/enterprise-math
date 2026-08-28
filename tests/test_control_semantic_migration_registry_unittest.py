import json
import unittest
from pathlib import Path

from control_plane import check_control_semantic_migration_registry as migration


ROOT = Path(__file__).resolve().parents[1]


class ControlSemanticMigrationRegistryTests(unittest.TestCase):
    def test_registered_control_debt_and_protected_selectors_have_no_drift(self):
        reports = migration.check(ROOT)
        self.assertGreaterEqual(len(reports), 10)
        self.assertTrue(any("CSM-ARCHITECTURE-TASK-PUBLICATION-003" in row for row in reports))
        self.assertTrue(any("CSM-ROLEPOLICY-CANONICAL-DISPATCH-001" in row for row in reports))
        self.assertTrue(any("CSM-STEWARD-CANONICAL-DISPATCH-005" in row for row in reports))
        self.assertTrue(any("CSM-RUNTIME-OWNER-SCOPE-LIVENESS-006" in row for row in reports))
        self.assertTrue(any("CSP-FOUNDATION-BACKFLOW-SURFACE-001" in row for row in reports))
        self.assertTrue(any("CSP-FOUNDATION-BACKFLOW-LINK-002" in row for row in reports))
        self.assertTrue(any("CSP-STEWARD-BACKFLOW-AUTHORITY-003" in row for row in reports))
        self.assertTrue(any("CSP-RUNTIME-FRESH-SELECTOR-004" in row for row in reports))

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

    def test_runtime_bundle_is_ready_only_after_reference_check(self):
        data = json.loads(
            (ROOT / "control_plane" / "control_semantic_migration_registry.json").read_text(
                encoding="utf-8"
            )
        )
        by_id = {row["migration_id"]: row for row in data["entries"]}
        dispatch = by_id["CSM-RUNTIME-CANONICAL-DISPATCH-004"]
        liveness = by_id["CSM-RUNTIME-OWNER-SCOPE-LIVENESS-006"]
        self.assertEqual(
            "REFERENCE_CHECK_PASSED_READY_FOR_MECHANICAL_PATCH",
            dispatch["state"],
        )
        self.assertEqual(33221974090, dispatch["reference_evidence"]["reference_integrity_run_id"])
        self.assertEqual(
            "READY_FOR_MECHANICAL_PATCH_WITH_RUNTIME_POINTER_BUNDLE",
            liveness["state"],
        )
        self.assertFalse(
            liveness["canonical_evidence"]["generic_conversation_activity_is_owner_scope_liveness"]
        )

    def test_intentional_task_definition_and_fresh_selectors_are_protected(self):
        data = json.loads(
            (ROOT / "control_plane" / "control_semantic_migration_registry.json").read_text(
                encoding="utf-8"
            )
        )
        protected = {row["protection_id"]: row for row in data["protected_selector_fields"]}
        for protection_id in (
            "CSP-FOUNDATION-BACKFLOW-SURFACE-001",
            "CSP-FOUNDATION-BACKFLOW-LINK-002",
            "CSP-STEWARD-BACKFLOW-AUTHORITY-003",
            "CSP-RUNTIME-FRESH-SELECTOR-004",
        ):
            self.assertEqual("tools/research_dispatch.py", protected[protection_id]["required_value"])
            self.assertTrue(protected[protection_id]["semantic_role"])
            self.assertTrue(protected[protection_id]["reason"])


if __name__ == "__main__":
    unittest.main()
