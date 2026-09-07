import json
import unittest
from pathlib import Path

from control_plane import check_control_semantic_migration_registry as migration


ROOT = Path(__file__).resolve().parents[1]


class ControlSemanticMigrationRegistryTests(unittest.TestCase):
    def test_registered_control_debt_and_protected_selectors_have_no_drift(self):
        reports = migration.check(ROOT)
        self.assertGreaterEqual(len(reports), 13)
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
        self.assertTrue(any("CSP-STEWARD-SCHEDULING-TOOL-006" in row for row in reports))

    def test_architecture_pointers_are_verified_without_reopening_mixed_semantic_debt(self):
        data = json.loads(
            (ROOT / "control_plane" / "control_semantic_migration_registry.json").read_text(
                encoding="utf-8"
            )
        )
        by_id = {row["migration_id"]: row for row in data["entries"]}
        self.assertEqual(
            "VERIFIED_NO_POINTER_CHANGE_REQUIRED",
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
            "RESOLVED_AS_PROTECTED_SELECTOR_NO_MIGRATION",
            by_id["CSM-STEWARD-CANONICAL-DISPATCH-TOOL-007"]["state"],
        )

    def test_low_risk_pointers_migrated_and_selector_fields_resolved(self):
        data = json.loads(
            (ROOT / "control_plane" / "control_semantic_migration_registry.json").read_text(
                encoding="utf-8"
            )
        )
        by_id = {row["migration_id"]: row for row in data["entries"]}
        self.assertEqual("TARGET_MIGRATED", by_id["CSM-ROLEPOLICY-CANONICAL-DISPATCH-001"]["state"])
        self.assertEqual("TARGET_MIGRATED", by_id["CSM-STEWARD-CANONICAL-DISPATCH-005"]["state"])

        role_selector = by_id["CSM-ROLEPOLICY-PUBLICATION-DISPATCH-002"]
        self.assertEqual("RESOLVED_AS_PROTECTED_SELECTOR_NO_MIGRATION", role_selector["state"])
        self.assertEqual("tools/research_dispatch.py", role_selector["canonical_target_value"])
        self.assertEqual(
            "CSP-ROLEPOLICY-PUBLICATION-DISPATCH-005",
            role_selector["resolution_evidence"]["protected_selector_id"],
        )

        steward_selector = by_id["CSM-STEWARD-CANONICAL-DISPATCH-TOOL-007"]
        self.assertEqual("RESOLVED_AS_PROTECTED_SELECTOR_NO_MIGRATION", steward_selector["state"])
        self.assertEqual("tools/research_dispatch.py", steward_selector["canonical_target_value"])
        self.assertEqual(
            "CSP-STEWARD-SCHEDULING-TOOL-006",
            steward_selector["resolution_evidence"]["protected_selector_id"],
        )

    def test_post_v2_runtime_bundle_retains_exact_physical_cutover_provenance(self):
        data = json.loads(
            (ROOT / "control_plane" / "control_semantic_migration_registry.json").read_text(
                encoding="utf-8"
            )
        )
        by_id = {row["migration_id"]: row for row in data["entries"]}
        dispatch = by_id["CSM-RUNTIME-CANONICAL-DISPATCH-004"]
        liveness = by_id["CSM-RUNTIME-OWNER-SCOPE-LIVENESS-006"]
        for row in (dispatch, liveness):
            self.assertEqual("TARGET_MIGRATED", row["state"])
            self.assertEqual(
                "9e8dcf5dd44ea4d7eb5aaf7e160a28d5266ebfc9",
                row["migrated_commit"],
            )
            self.assertEqual("research_runtime_state_machine.json", row["path"])
            self.assertTrue(row["exact_diff_verified"])
            self.assertFalse(row["execution_authority_while_open"])
        self.assertEqual(
            "/canonical_live_dispatch", dispatch["json_pointer"],
        )
        self.assertEqual(
            ["/owner_lease_is_session_liveness", "/stale_valid_owner_action"],
            liveness["json_pointers"],
        )
        reference = dispatch["reference_evidence"]
        self.assertEqual(
            "control_plane/legacy_control_migration_manifest.json",
            reference["physical_cutover_manifest"],
        )
        manifest = json.loads((ROOT / reference["physical_cutover_manifest"]).read_text(encoding="utf-8"))
        self.assertEqual("COMPLETE", manifest["status"])
        self.assertEqual(manifest["source"]["archive_branch"], reference["archive_branch"])
        self.assertEqual(
            "CSP-RUNTIME-FRESH-SELECTOR-004", reference["protected_runtime_selector"],
        )
        self.assertEqual(
            ["TASK_RESEARCH_RESPONSE", "DURABLE_EXECUTION_PROGRESS"],
            liveness["canonical_evidence"]["allowed_evidence_kinds"],
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
            "CSP-STEWARD-SCHEDULING-TOOL-006",
        ):
            self.assertEqual("tools/research_dispatch.py", protected[protection_id]["required_value"])
            self.assertTrue(protected[protection_id]["semantic_role"])
            self.assertTrue(protected[protection_id]["reason"])


if __name__ == "__main__":
    unittest.main()
