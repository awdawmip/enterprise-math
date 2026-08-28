import unittest
from pathlib import Path

from tools import research_taskbook


ROOT = Path(__file__).resolve().parents[1]


class TaskbookPolicyDigestOperationalAddendaTests(unittest.TestCase):
    def test_context_read_addenda_preserve_preexisting_policy_input_blobs(self):
        expected = {
            "AGENTS.md": "8a0884b85c82e5c503c6ed00ab4c372e60dfcdca",
            "docs/GITHUB_INTERACTION_BUDGET.md": "1f9907ca111010230f4c46f3d18a524d8c152f35",
        }
        for rel, blob_sha in expected.items():
            stripped = research_taskbook.taskbook_policy_digest_payload(
                rel, (ROOT / rel).read_bytes()
            )
            self.assertEqual(
                blob_sha,
                research_taskbook.git_blob_identity(stripped).hex(),
                rel,
            )

    def test_only_exact_allowlisted_marker_path_is_excluded(self):
        payload = (
            "before\n"
            "<!-- TASKBOOK_POLICY_DIGEST_EXCLUDE_BEGIN: CONTEXT_READ_BUDGET -->\n"
            "runtime-only\n"
            "<!-- TASKBOOK_POLICY_DIGEST_EXCLUDE_END: CONTEXT_READ_BUDGET -->\n"
            "after\n"
        ).encode("utf-8")
        self.assertEqual(
            b"before\nafter\n",
            research_taskbook.taskbook_policy_digest_payload("AGENTS.md", payload),
        )
        with self.assertRaisesRegex(ValueError, "unauthorized"):
            research_taskbook.taskbook_policy_digest_payload("FOUNDATIONAL_LOGIC.md", payload)

    def test_malformed_or_nested_exclusions_fail_closed(self):
        unterminated = (
            "<!-- TASKBOOK_POLICY_DIGEST_EXCLUDE_BEGIN: CONTEXT_READ_BUDGET -->\n"
            "runtime-only\n"
        ).encode("utf-8")
        nested = (
            "<!-- TASKBOOK_POLICY_DIGEST_EXCLUDE_BEGIN: CONTEXT_READ_BUDGET -->\n"
            "<!-- TASKBOOK_POLICY_DIGEST_EXCLUDE_BEGIN: CONTEXT_READ_BUDGET -->\n"
            "<!-- TASKBOOK_POLICY_DIGEST_EXCLUDE_END: CONTEXT_READ_BUDGET -->\n"
            "<!-- TASKBOOK_POLICY_DIGEST_EXCLUDE_END: CONTEXT_READ_BUDGET -->\n"
        ).encode("utf-8")
        with self.assertRaisesRegex(ValueError, "unterminated"):
            research_taskbook.taskbook_policy_digest_payload("AGENTS.md", unterminated)
        with self.assertRaisesRegex(ValueError, "nested"):
            research_taskbook.taskbook_policy_digest_payload("AGENTS.md", nested)


if __name__ == "__main__":
    unittest.main()
