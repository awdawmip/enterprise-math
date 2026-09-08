"""Finite coverage and rejection checks; no elliptic-map evaluator."""
import contextlib
import io
import tempfile
import unittest
from pathlib import Path

from scripts import check_rb_blind_branch_patterns_20260908 as checker


class BlindBranchAssignments(unittest.TestCase):
    def fixture(self, root):
        directory = root.joinpath(checker.ARTIFACT_REL)
        directory.mkdir(parents=True)
        directory.joinpath("source_binding.json").write_bytes(
            checker.ROOT.joinpath(checker.ARTIFACT_REL, "source_binding.json").read_bytes())
        return directory

    def test_fixed_parameter_candidates_are_not_cover_only_candidates(self):
        result = checker.build_certificate(checker.ROOT)
        for pattern, fixed, cover in (("4+2+0+0", 45, 33), ("2+2+2+0", 90, 54)):
            partitions = result["patterns"][pattern]["partitions"]
            self.assertEqual(fixed, len(partitions["fixed_lambda_fixed_k_V4"]))
            self.assertEqual(cover, len(partitions["cover_only_V4_and_source_flip"]))
            self.assertGreater(fixed, cover)

    def test_source_binding_drift_is_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            directory = self.fixture(root)
            source = directory.joinpath("source_binding.json")
            source.write_bytes(source.read_bytes() + b"\n")
            with self.assertRaisesRegex(ValueError, "source binding changed"):
                checker.build_certificate(root)

    def test_default_replay_rejects_tampered_certificate_without_rewriting(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            directory = self.fixture(root)
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(0, checker.main(["--root", str(root), "--write"]))
            output = directory.joinpath("branch_assignment_classification.json")
            tampered = output.read_bytes() + b"\n"
            output.write_bytes(tampered)
            with self.assertRaisesRegex(SystemExit, "certificate bytes differ"):
                checker.main(["--root", str(root)])
            self.assertEqual(tampered, output.read_bytes())


if __name__ == "__main__":
    unittest.main()
