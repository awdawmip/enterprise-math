"""Small finite and corruption boundaries, without map or root evaluation."""
import contextlib
import io
import tempfile
import unittest
from pathlib import Path

from research_artifacts.RB_BLIND_BRANCH_PATTERN_COMPLETION_20260908 import check_empty_fiber_obstruction as checker


class EmptyFiberObstructionBoundaries(unittest.TestCase):
    def fixture(self, root):
        directory = root.joinpath(checker.REL)
        directory.mkdir(parents=True)
        for name in checker.DEPENDENCIES:
            directory.joinpath(name).write_bytes(checker.ROOT.joinpath(checker.REL, name).read_bytes())
        return directory

    def test_degree_three_parity_forces_three_plus_one_branch_fiber(self):
        possible = {(first, second) for first in range(4) for second in range(4)
                    if first + second == 4 and 3 - first in (0, 2) and 3 - second in (0, 2)}
        self.assertEqual({(1, 3), (3, 1)}, possible)
        self.assertNotIn((2, 2), possible)
        triples = checker.branch_triples()
        self.assertEqual(20, len(triples["twenty_triples"]))
        self.assertEqual(10, len(triples["ten_possible_pole_classes"]))

    def test_pinned_corrected_checker_or_certificate_drift_is_rejected(self):
        for name in ("check_squareclass_rr.py", "squareclass_rr_certificate.json"):
            with self.subTest(name=name), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                directory = self.fixture(root)
                path = directory.joinpath(name)
                path.write_bytes(path.read_bytes() + b"\n")
                with self.assertRaisesRegex(ValueError, "dependency changed"):
                    checker.build_certificate(root)

    def test_default_replay_preserves_and_rejects_corrupted_output(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            directory = self.fixture(root)
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(0, checker.main(["--root", str(root), "--write"]))
            path = directory.joinpath("empty_fiber_obstruction_certificate.json")
            corrupted = path.read_bytes() + b"\n"
            path.write_bytes(corrupted)
            with self.assertRaisesRegex(SystemExit, "certificate bytes differ"):
                checker.main(["--root", str(root)])
            self.assertEqual(corrupted, path.read_bytes())


if __name__ == "__main__":
    unittest.main()
