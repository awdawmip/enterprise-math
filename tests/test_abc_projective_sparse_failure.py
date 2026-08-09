import unittest

from enterprise_math.abc_projective_sparse_failure import (
    dyadic_square_divisor_union_bound,
    largest_square_divisor_root,
    projective_failure_large_residual_witness,
    square_divisor_dominates_residual,
)


class AbcProjectiveSparseFailureTests(unittest.TestCase):
    def test_largest_square_divisor_dominates_residual(self) -> None:
        self.assertEqual(largest_square_divisor_root(57122), 169)
        self.assertTrue(square_divisor_dominates_residual(57122))
        self.assertTrue(square_divisor_dominates_residual(242))
        self.assertTrue(square_divisor_dominates_residual(243))
        self.assertTrue(square_divisor_dominates_residual(512))

    def test_unit_hard_example_fails_pcc_three_fifths_and_forces_large_residual(self) -> None:
        data = projective_failure_large_residual_witness(1, 57121, 57122, 3, 5)
        self.assertIsNotNone(data)
        if data is None:
            raise AssertionError("stored PCC failure disappeared")
        self.assertEqual(data.component_index, 2)
        self.assertEqual(data.component_value, 57122)
        self.assertEqual(data.multiplicity_residual, 2197)
        self.assertEqual(data.square_root_divisor, 169)
        self.assertEqual(data.square_divisor, 28561)
        self.assertGreaterEqual(data.multiplicity_residual**5, 57122**3)
        self.assertGreaterEqual(data.square_divisor, data.multiplicity_residual)

    def test_projective_condition_can_hold_and_return_no_failure_witness(self) -> None:
        # 1+242=243 satisfies PCC at exponent 1/3.
        self.assertIsNone(
            projective_failure_large_residual_witness(1, 242, 243, 1, 3)
        )

    def test_dyadic_union_bound_has_power_saving_density(self) -> None:
        # For eta=1/2, the component union bound is O(X^(3/4)).
        # Compare two exact dyadic scales without using floating point.
        first_x = 2**12
        second_x = 2**20
        first = dyadic_square_divisor_union_bound(first_x, 1, 2)
        second = dyadic_square_divisor_union_bound(second_x, 1, 2)
        self.assertGreater(first, 0)
        self.assertGreater(second, first)
        # Density U(X)/X must visibly decrease on these calibration scales.
        self.assertLess(second * first_x, first * second_x)

    def test_stronger_eta_reduces_component_union_bound(self) -> None:
        X = 2**18
        half = dyadic_square_divisor_union_bound(X, 1, 2)
        three_fifths = dyadic_square_divisor_union_bound(X, 3, 5)
        self.assertLessEqual(three_fifths, half)


if __name__ == "__main__":
    unittest.main()
