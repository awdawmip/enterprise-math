import math
import unittest

from enterprise_math.abc_projective_paired_square_tail import (
    dyadic_paired_square_product_threshold,
    dyadic_paired_square_triple_union_bound,
    projective_failure_paired_residual_witness,
)
from enterprise_math.abc_projective_sparse_failure import (
    dyadic_square_divisor_union_bound,
)


class ProjectivePairedSquareTailTests(unittest.TestCase):
    def test_small_exact_nonunit_failure_forces_two_residuals(self) -> None:
        # 3+125=128 has c-oriented sigma=32/7 and fails PCC_(1/10).
        witness = projective_failure_paired_residual_witness(3, 125, 128, 1, 10)
        self.assertIsNotNone(witness)
        assert witness is not None
        self.assertEqual(witness.component_indices, (2, 1))
        self.assertEqual(witness.component_values, (128, 125))
        self.assertEqual(witness.residuals, (64, 25))
        self.assertEqual(witness.residual_product, 1600)
        self.assertEqual(witness.square_root_divisors, (8, 5))
        self.assertEqual(witness.square_root_product, 40)
        self.assertGreaterEqual(
            (2 * witness.residual_product) ** 10,
            128 ** 11,
        )

    def test_nonfailure_returns_none(self) -> None:
        self.assertIsNone(
            projective_failure_paired_residual_witness(2, 3, 5, 1, 2)
        )

    def test_unit_slice_is_deliberately_separate(self) -> None:
        with self.assertRaises(ValueError):
            projective_failure_paired_residual_witness(1, 8, 9, 1, 3)

    def test_dyadic_product_threshold_is_minimal(self) -> None:
        X, p, q = 10_000, 1, 2
        Y = dyadic_paired_square_product_threshold(X, p, q)
        factor = 2 ** (2 * q + p)
        target = X ** (q + p)
        self.assertGreaterEqual(factor * Y ** (2 * q), target)
        if Y > 1:
            self.assertLess(factor * (Y - 1) ** (2 * q), target)

    def test_paired_union_bound_improves_the_stage50_shape(self) -> None:
        # This is a finite calibration, not an asymptotic proof.
        X, p, q = 10_000, 1, 2
        paired = dyadic_paired_square_triple_union_bound(X, p, q)
        single_components = dyadic_square_divisor_union_bound(X, p, q)
        old_triple_envelope = 3 * X * single_components
        self.assertGreater(paired, 0)
        self.assertLess(paired, old_triple_envelope)


if __name__ == "__main__":
    unittest.main()
