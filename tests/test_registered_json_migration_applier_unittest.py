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

    def test_runtime_dry_run_changes_exactly_three_registered_pointers(self):
        result = applier.plan(RUNTIME_IDS, ROOT)
        proposed = result.pop("proposed_text")
        self.assertEqual(
            {
                "/composes/canonical_dispatch",
                "/lease_model/session_liveness/semantic_scope",
                "/lease_model/session_liveness/renewed_by",
            },
            set(result["changed_pointers"]),
        )
        self.assertTrue(result["non_target_structure_equal"])
        self.assertTrue(result["non_target_text_segments_byte_identical"])
        self.assertEqual(
            "tools/research_dispatch.py",
            result["protected_after"]["/dispatch/tool"],
        )
        parsed = json.loads(proposed)
        self.assertEqual("research_control_dispatch.py", parsed["composes"]["canonical_dispatch"])
        self.assertEqual(
            "EXACT_OWNER_SCOPE_CURRENT_WINNING_CLAIM",
            parsed["lease_model"]["session_liveness"]["semantic_scope"],
        )

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


if __name__ == "__main__":
    unittest.main()
