import unittest

from enterprise_math.abc_prime_cube_modulus_pressure import (
    cube_difference_modulus_pressure,
    cube_sum_modulus_pressure,
    p018_cube_difference_modulus_pressure,
)


class PrimeCubeModulusPressureTests(unittest.TestCase):
    def test_cube_sum_threshold_forces_large_repeated_modulus(self) -> None:
        # (q,p)=(5,59) has cube-sum rho=13/6, repeated Phi_6 modulus 13^2.
        state = cube_sum_modulus_pressure(5, 59, 2)
        self.assertEqual(state.repeated_modulus, 13**2)
        self.assertEqual(state.quadratic_residual, 13)
        self.assertEqual(state.center_radical, 2)
        self.assertEqual(state.lower_bound, 28)
        self.assertGreaterEqual(state.repeated_modulus, state.lower_bound)

    def test_cube_difference_can_pay_pressure_in_radius_residual(self) -> None:
        # (5,101): A=48 has m(A)=8, Phi_3 residual is 7.
        state = cube_difference_modulus_pressure(5, 101, 1, 8)
        self.assertEqual(state.branch, "radius-residual")
        self.assertEqual(state.radius_residual, 8)
        self.assertIsNone(state.repeated_modulus)

    def test_cube_difference_can_be_forced_to_cyclotomic_modulus_branch(self) -> None:
        state = cube_difference_modulus_pressure(5, 101, 1, 9)
        self.assertEqual(state.branch, "cyclotomic-modulus")
        self.assertEqual(state.quadratic_residual, 7)
        self.assertEqual(state.repeated_modulus, 7**2)
        self.assertGreater(9 * state.repeated_modulus, 7 * 53)

    def test_split_horizon_must_fit_threshold_center(self) -> None:
        with self.assertRaises(ValueError):
            cube_difference_modulus_pressure(5, 101, 1, 54)

    def test_p018_helper_preserves_both_size_and_activation_gates(self) -> None:
        # The centered pair (73,89) satisfies the P018 size gate but its cube-
        # difference atom is subunit, so the helper rejects it at threshold one.
        with self.assertRaises(ValueError):
            p018_cube_difference_modulus_pressure(73, 89, 1)

        # (5,101) is active but far outside the P018 q>A^2 size gate.
        with self.assertRaises(ValueError):
            p018_cube_difference_modulus_pressure(5, 101, 1)


if __name__ == "__main__":
    unittest.main()
