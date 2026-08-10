import unittest

from enterprise_math.abc_cube_eisenstein_tail import (
    cube_eisenstein_tail_state,
    divisor_count,
    eisenstein_representation_upper_bound,
)


class CubeEisensteinTailTests(unittest.TestCase):
    def test_divisor_envelope_is_exactly_six_tau(self) -> None:
        self.assertEqual(divisor_count(1), 1)
        self.assertEqual(divisor_count(3 * 37**2), 6)
        self.assertEqual(eisenstein_representation_upper_bound(3 * 37**2), 36)

    def test_small_linear_radical_branch(self) -> None:
        state = cube_eisenstein_tail_state(11, 13, 100, "sum")
        self.assertTrue(state.projective_threshold_holds)
        self.assertTrue(state.small_linear_radical_branch)
        self.assertEqual(state.linear_factor, 24)
        self.assertEqual(state.linear_radical, 6)
        self.assertEqual(state.cyclotomic_factor, 3 * 7**2)
        self.assertEqual(state.cyclotomic_residual, 7)
        self.assertGreaterEqual(
            state.cyclotomic_residual,
            state.linear_radical,
        )

    def test_large_linear_radical_sum_branch_forces_large_norm_residual(self) -> None:
        state = cube_eisenstein_tail_state(47, 73, 100, "sum")
        self.assertTrue(state.projective_threshold_holds)
        self.assertFalse(state.small_linear_radical_branch)
        self.assertEqual(state.linear_factor, 120)
        self.assertEqual(state.linear_radical, 30)
        self.assertEqual(state.cyclotomic_factor, 3 * 37**2)
        self.assertEqual(state.cyclotomic_residual, 37)
        self.assertGreaterEqual(
            state.cyclotomic_residual,
            state.linear_radical,
        )

    def test_large_linear_radical_difference_branch_is_strict(self) -> None:
        state = cube_eisenstein_tail_state(17, 73, 100, "difference")
        self.assertTrue(state.projective_threshold_holds)
        self.assertFalse(state.small_linear_radical_branch)
        self.assertEqual(state.linear_factor, 56)
        self.assertEqual(state.linear_radical, 14)
        self.assertEqual(state.cyclotomic_factor, 19**3)
        self.assertEqual(state.cyclotomic_residual, 19**2)
        self.assertGreater(
            state.cyclotomic_residual,
            state.linear_radical,
        )

    def test_nontrivial_power_threshold_uses_exact_integer_powers(self) -> None:
        # rho=1372/47 > 10 = 100^(1/2).
        state = cube_eisenstein_tail_state(
            23,
            71,
            100,
            "difference",
            threshold_numerator=1,
            threshold_denominator=2,
        )
        self.assertTrue(state.projective_threshold_holds)
        self.assertFalse(state.small_linear_radical_branch)
        self.assertEqual(state.linear_factor, 48)
        self.assertEqual(state.linear_radical, 6)
        self.assertEqual(state.cyclotomic_residual, 7**3)
        # d > P^(1/2) * rad(L) = 60.
        self.assertGreater(state.cyclotomic_residual, 60)

    def test_endpoint_tau_one_has_empty_small_radical_branch_for_active_state(self) -> None:
        # Use a height small enough that rho exceeds P but still height>=p.
        state = cube_eisenstein_tail_state(
            23,
            71,
            71,
            "difference",
            threshold_numerator=1,
            threshold_denominator=1,
        )
        self.assertFalse(state.projective_threshold_holds)
        self.assertFalse(state.small_linear_radical_branch)


if __name__ == "__main__":
    unittest.main()
