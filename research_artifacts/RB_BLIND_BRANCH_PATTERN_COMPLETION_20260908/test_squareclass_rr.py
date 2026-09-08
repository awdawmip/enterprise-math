"""Scope and corruption boundaries of this task-local formal certificate."""
import contextlib
import io
import tempfile
import unittest
from pathlib import Path

from research_artifacts.RB_BLIND_BRANCH_PATTERN_COMPLETION_20260908 import check_squareclass_rr as checker


class SquareclassRRBoundaries(unittest.TestCase):
    def fixture(self, root):
        directory = root.joinpath(checker.REL)
        directory.mkdir(parents=True)
        for name in ("source_binding.json", "branch_assignment_classification.json"):
            directory.joinpath(name).write_bytes(checker.ROOT.joinpath(checker.REL, name).read_bytes())
        return directory

    def test_integer_vector_field_preserves_the_curve_relation(self):
        R, t = checker.variable(6), checker.variable(7)
        r_cubic = checker.multiply(R, R, R)
        t_squared_unreduced = list(checker.ZERO_MONOMIAL)
        t_squared_unreduced[7] = 2
        relation = checker.add({tuple(t_squared_unreduced): 1}, checker.scale(r_cubic, -1),
                               checker.scale(R, 3))
        self.assertEqual({}, checker.twice_delta(relation))

    def test_nonconstant_and_rank_degenerate_quotients_are_distinguished(self):
        R, t = checker.variable(6), checker.variable(7)
        ordinary_numerator = checker.twice_delta(t)
        self.assertNotEqual({}, checker.restrict_to_critical_divisor(ordinary_numerator))
        # This pair is proportional and represents a constant, not a degree-three map.
        numerator = checker.add(R, t)
        denominator = checker.scale(numerator, 2)
        degenerate = checker.add(checker.multiply(checker.twice_delta(numerator), denominator),
                                checker.scale(checker.multiply(numerator, checker.twice_delta(denominator)), -1))
        self.assertEqual({}, degenerate)

    def test_frozen_input_drift_is_rejected(self):
        for name in ("source_binding.json", "branch_assignment_classification.json"):
            with self.subTest(name=name), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                directory = self.fixture(root)
                source = directory.joinpath(name)
                source.write_bytes(source.read_bytes() + b"\n")
                with self.assertRaisesRegex(ValueError, "changed"):
                    checker.build_certificate(root)

    def test_rr_difference_uses_values_and_rejects_reversed_sign(self):
        R, t = checker.variable(6), checker.variable(7)
        X = checker.add(checker.multiply(R, R), checker.scale(t, 3), checker.constant(2))
        denominator_square = checker.multiply(checker.variable(3), checker.variable(3))
        for shift in (checker.constant(1), checker.constant(7), checker.variable(0)):
            with self.subTest(shift=shift):
                X_minus_a = checker.add(X, checker.scale(shift, -1))
                self.assertEqual(shift, checker.rr_fiber_difference(X, X_minus_a))
                self.assertEqual(checker.scale(shift, -1), checker.rr_fiber_difference(X_minus_a, X))
                self.assertNotEqual(shift, checker.rr_fiber_difference(X_minus_a, X))
                self.assertEqual(checker.multiply(shift, denominator_square), checker.rr_fiber_difference(
                    checker.multiply(X, denominator_square), checker.multiply(X_minus_a, denominator_square)))

    def test_default_is_byte_preserving_and_rejects_output_corruption(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            directory = self.fixture(root)
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(0, checker.main(["--root", str(root), "--write"]))
            output = directory.joinpath("squareclass_rr_certificate.json")
            corrupted = output.read_bytes() + b"\n"
            output.write_bytes(corrupted)
            with self.assertRaisesRegex(SystemExit, "certificate bytes differ"):
                checker.main(["--root", str(root)])
            self.assertEqual(corrupted, output.read_bytes())


if __name__ == "__main__":
    unittest.main()
