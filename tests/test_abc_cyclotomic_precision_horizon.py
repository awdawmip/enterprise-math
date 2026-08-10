import unittest
from fractions import Fraction

from enterprise_math.abc_cyclotomic_precision_horizon import (
    cyclotomic_precision_horizon_state,
    periodic_pressure_incidence_upper_bound,
    residual_modulus_identity,
)
from enterprise_math.abc_odd_prime_exponent_cyclotomic import (
    odd_prime_exponent_cyclotomic_state,
)


class CyclotomicPrecisionHorizonTests(unittest.TestCase):
    def test_residual_determines_full_repeated_modulus(self) -> None:
        self.assertEqual(residual_modulus_identity(7), 49)
        self.assertEqual(residual_modulus_identity(13), 169)
        self.assertEqual(residual_modulus_identity(49), 343)
        self.assertEqual(residual_modulus_identity(121), 1331)

    def test_periodic_cube_signature_gets_pressure_envelope(self) -> None:
        state = odd_prime_exponent_cyclotomic_state(5, 59, 3, "sum")
        horizon = cyclotomic_precision_horizon_state(
            state, 1000, Fraction(2, 1)
        )
        self.assertTrue(horizon.periodic_regime)
        self.assertEqual(horizon.repeated_modulus, 169)
        self.assertEqual(horizon.candidates_per_q_per_root, 6)
        self.assertEqual(horizon.signature_incidence_bound, 12_000)
        envelope = periodic_pressure_incidence_upper_bound(
            state, 1000, Fraction(2, 1)
        )
        self.assertEqual(envelope, Fraction(1_000_000, 7))
        self.assertLess(horizon.signature_incidence_bound, envelope)

    def test_supermodular_cube_signature_forces_sqrt_height_residual(self) -> None:
        state = odd_prime_exponent_cyclotomic_state(11, 13, 3, "sum")
        horizon = cyclotomic_precision_horizon_state(state, 20)
        self.assertFalse(horizon.periodic_regime)
        self.assertEqual(horizon.repeated_modulus, 49)
        self.assertEqual(horizon.cyclotomic_residual, 7)
        self.assertGreater(horizon.cyclotomic_residual**2, 20)
        self.assertEqual(horizon.candidates_per_q_per_root, 1)
        self.assertEqual(horizon.signature_incidence_bound, 40)

    def test_fifth_power_signature_has_same_horizon_semantics(self) -> None:
        state = odd_prime_exponent_cyclotomic_state(37, 59, 5, "sum")
        low = cyclotomic_precision_horizon_state(state, 100)
        self.assertFalse(low.periodic_regime)
        self.assertEqual(low.repeated_modulus, 31**2)
        self.assertEqual(low.root_choice_count, 4)
        self.assertEqual(low.candidates_per_q_per_root, 1)

        high = cyclotomic_precision_horizon_state(state, 2000)
        self.assertTrue(high.periodic_regime)
        self.assertEqual(high.candidates_per_q_per_root, 3)
        self.assertLess(high.signature_incidence_bound, high.ambient_ordered_pair_count)


if __name__ == "__main__":
    unittest.main()
