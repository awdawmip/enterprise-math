import json
import tempfile
import unittest
from pathlib import Path

from control_plane import apply_registered_json_migration as applier


ROOT = Path(__file__).resolve().parents[1]
RUNTIME_IDS = [
    "CSM-RUNTIME-CANONICAL-DISPATCH-004",
    "CSM-RUNTIME-OWNER-SCOPE-LIVENESS-006",
]


class RegisteredJsonMigrationApplierTests(unittest.TestCase):
    def test_span_parser_records_nested_value_spans(self):
        text = '{\n  "a": {"b": [1, 2]},\n  "c": "x"\n}\n'
        spans = applier.JsonSpanParser(text).parse()
        self.assertEqual('{"b": [1, 2]}', text[spans["/a"].start : spans["/a"].end])
        self.assertEqual('[1, 2]', text[spans["/a/b"].start : spans["/a/b"].end])
        self.assertEqual('2', text[spans["/a/b/1"].start : spans["/a/b/1"].end])
        self.assertEqual('"x"', text[spans["/c"].start : spans["/c"].end])

    def test_runtime_dry_run_is_idempotent_after_registered_pointers_reach_target(self):
        result = applier.plan(RUNTIME_IDS, ROOT)
        proposed = result.pop("proposed_text")
        self.assertTrue(result["already_target"])
        self.assertEqual([], result["changed_pointers"])
        self.assertTrue(result["non_target_structure_equal"])
        self.assertTrue(result["non_target_text_segments_byte_identical"])
        self.assertEqual(
            "tools/research_dispatch.py",
            result["protected_after"]["/fresh_task_selector"],
        )
        self.assertEqual(result["protected_before"], result["protected_after"])
        parsed = json.loads(proposed)
        self.assertEqual("research_control_dispatch.py", parsed["canonical_live_dispatch"])
        self.assertFalse(parsed["owner_lease_is_session_liveness"])
        self.assertEqual(
            "PREPARE_AUTHENTICATED_SUCCESSOR_CLAIM_WITH_PREDECESSOR_CAS",
            parsed["stale_valid_owner_action"],
        )
        self.assertNotIn("dispatch", parsed)
        self.assertNotIn("composes", parsed)
        self.assertNotIn("lease_model", parsed)

    def test_write_mode_logic_can_be_exercised_on_exact_temp_copy_without_repo_mutation(self):
        # Construct a tiny standalone source to test exact span replacement and
        # prove surrounding bytes remain identical. This test never writes the
        # repository runtime file.
        text = '{\n  "route": "old",\n  "protected": "keep"\n}\n'
        spans = applier.JsonSpanParser(text).parse()
        span = spans["/route"]
        replacement = json.dumps("new")
        proposed = text[: span.start] + replacement + text[span.end :]
        self.assertEqual(
            '{\n  "route": "new",\n  "protected": "keep"\n}\n',
            proposed,
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sample.json"
            path.write_text(proposed, encoding="utf-8")
            self.assertEqual("keep", json.loads(path.read_text(encoding="utf-8"))["protected"])

    def test_unapproved_semantic_verification_entry_cannot_be_applied(self):
        with self.assertRaises(applier.MigrationApplyError):
            applier.plan(["CSM-ARCHITECTURE-TASK-PUBLICATION-003"], ROOT)

    def sample_plan(self, route, *, shared_baseline=False):
        text = json.dumps({"owner_lease_is_session_liveness": False, "route": route}) + "\n"
        baseline = applier._git_blob_sha1(text.encode())
        entries = [
            {
                "migration_id": "UNCHANGED-FLAG",
                "path": "sample.json",
                "state": "TARGET_MIGRATED",
                "baseline_blob_sha1": baseline,
                "json_pointer": "/owner_lease_is_session_liveness",
                "observed_legacy_value": False,
                "canonical_target_value": False,
            },
            {
                "migration_id": "ROUTE",
                "path": "sample.json",
                "state": "TARGET_MIGRATED",
                "baseline_blob_sha1": baseline if shared_baseline else "0" * 40,
                "json_pointer": "/route",
                "observed_legacy_value": "old",
                "canonical_target_value": "new",
            },
        ]
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "control_plane").mkdir()
            (root / "sample.json").write_text(text, encoding="utf-8")
            (root / "control_plane/control_semantic_migration_registry.json").write_text(
                json.dumps({"entries": entries}), encoding="utf-8"
            )
            return applier.plan(["UNCHANGED-FLAG", "ROUTE"], root), text

    def test_equal_old_and_target_is_noop_despite_different_historical_baselines(self):
        result, text = self.sample_plan("new")
        self.assertTrue(result["already_target"])
        self.assertEqual([], result["changed_pointers"])
        self.assertEqual(text, result["proposed_text"])

    def test_real_pending_pointer_still_requires_shared_exact_baseline(self):
        with self.assertRaisesRegex(applier.MigrationApplyError, "one exact baseline blob"):
            self.sample_plan("old")

    def test_real_pending_pointer_with_shared_exact_baseline_changes_only_that_pointer(self):
        result, _ = self.sample_plan("old", shared_baseline=True)
        self.assertFalse(result["already_target"])
        self.assertEqual(["/route"], result["changed_pointers"])
        self.assertEqual(
            {"owner_lease_is_session_liveness": False, "route": "new"},
            json.loads(result["proposed_text"]),
        )
        self.assertTrue(result["non_target_text_segments_byte_identical"])

    def test_third_state_remains_rejected(self):
        with self.assertRaisesRegex(applier.MigrationApplyError, "third-state value"):
            self.sample_plan("unknown")


if __name__ == "__main__":
    unittest.main()
