import json
import unittest
from pathlib import Path

from control_plane import check_control_semantic_migration_registry as migration


ROOT = Path(__file__).resolve().parents[1]


class ControlSemanticMigrationRegistryTests(unittest.TestCase):
    def test_registered_control_debt_and_protected_selectors_have_no_drift(self):
        reports = migration.check(ROOT)
        self.assertGreaterEqual(len(reports), 12)
        self.assertTrue(any("CSM-ARCHITECTURE-TASK-PUBLICATION-003" in row for row in reports))
        self.assertTrue(any("CSM-ROLEPOLICY-CANONICAL-DISPATCH-001" in row for row in reports))
        self.assertTrue(any("CSM-STEWARD-CANONICAL-DISPATCH-005" in row for row in reports))
        self.assertTrue(any("CSM-RUNTIME-OWNER-SCOPE-LIVENESS-006" in row for row in reports))
        self.assertTrue(any("CSM-STEWARD-CANONICAL-DISPATCH-TOOL-007" in row for row in reports))
        self.assertTrue(any("CSP-FOUNDATION-BACKFLOW-SURFACE-001" in row for row in reports))
        self.assertTrue(any("CSP-FOUNDATION-BACKFLOW-LINK-002" in row for row in reports))
        self.assertTrue(any("CSP-STEWARD-BACKFLOW-AUTHORITY-003" in row for row in reports))
        self.assertTrue(any("CSP-RUNTIME-FRESH-SELECTOR-004" in row for row in reports))
        self.assertTrue(any("CSP-ROLEPOLICY-PUBLICATION-DISPATCH-005" in row for row in reports))

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
        self.assertEqual(
            "REQUIRES_GOVERNANCE_VERIFICATION",
            by_id["CSM-STEWARD-CANONICAL-DISPATCH-TOOL-007"]["state"],
        )

    def test_low_risk_pointers_migrated_and_publication_dispatch_is_resolved_selector(self):
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
        resolved = by_id["CSM-ROLEPOLICY-PUBLICATION-DISPATCH-002"]
        self.assertEqual(
            "RESOLVED_AS_PROTECTED_SELECTOR_NO_MIGRATION",
            resolved["state"],
        )
        self.assertEqual("tools/research_dispatch.py", resolved["canonical_target_value"])
        self.assertEqual(
            "CSP-ROLEPOLICY-PUBLICATION-DISPATCH-005",
            resolved["resolution_evidence"]["protected_selector_id"],
        )
        self.assertIn(
            "ONLY /canonical_dispatch CHANGED",
            by_id["CSM-ROLEPOLICY-CANONICAL-DISPATCH-001"]["migration_scope"],
        )
        self.assertIn(
            "backflow.task_definition_authority",
            by_id["CSM-STEWARD-CANONICAL-DISPATCH-005"]["migration_scope"],
        )

    def test_runtime_bundle_is_proven_but_waits_for_safe_write_mechanism(self):
        data = json.loads(
            (ROOT / "control_plane" / "control_semantic_migration_registry.json").read_text(
                encoding="utf-8"
            )
        )
        by_id = {row["migration_id"]: row for row in data["entries"]}
        dispatch = by_id["CSM-RUNTIME-CANONICAL-DISPATCH-004"]
        liveness = by_id["CSM-RUNTIME-OWNER-SCOPE-LIVENESS-006"]
        self.assertEqual(
            "FIELD_LOCALITY_PROOF_PASSED_AWAITING_SAFE_WRITE_MECHANISM",
            dispatch["state"],
        )
        self.assertEqual(
            33221974090,
            dispatch["reference_evidence"]["production_consumer_reference_integrity_run_id"],
        )
        self.assertEqual(
            33222148731,
            dispatch["reference_evidence"]["field_locality_reference_integrity_run_id"],
        )
        self.assertEqual(
            "FIELD_LOCALITY_PROOF_PASSED_AWAITING_SAFE_WRITE_MECHANISM",
            liveness["state"],
        )
        self.assertEqual(
            33222148731,
            liveness["reference_evidence"]["field_locality_reference_integrity_run_id"],
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
            "CSP-ROLEPOLICY-PUBLICATION-DISPATCH-005",
        ):
            self.assertEqual("tools/research_dispatch.py", protected[protection_id]["required_value"])
            self.assertTrue(protected[protection_id]["semantic_role"])
            self.assertTrue(protected[protection_id]["reason"])


if __name__ == "__main__":
    unittest.main()
