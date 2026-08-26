import tempfile
import unittest
from pathlib import Path

from tools import research_result_records as results


class HistoricalGitBlobIdentityCompatibilityTests(unittest.TestCase):
    def test_bare_and_prefixed_sha1_identify_same_git_blob(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "artifact.txt"
            path.write_text("frozen\n", encoding="utf-8")
            current = results._blob(path)
            self.assertTrue(current.startswith("sha1:"))
            bare = current.removeprefix("sha1:")
            self.assertTrue(results._same_git_blob_identity(current, bare))
            self.assertTrue(results._same_git_blob_identity(current, "sha1:" + bare))

    def test_wrong_or_malformed_digest_remains_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "artifact.txt"
            path.write_text("frozen\n", encoding="utf-8")
            current = results._blob(path)
            self.assertFalse(results._same_git_blob_identity(current, "0" * 40))
            self.assertFalse(results._same_git_blob_identity(current, "sha1:bad"))
            self.assertFalse(results._same_git_blob_identity(current, None))


if __name__ == "__main__":
    unittest.main()
