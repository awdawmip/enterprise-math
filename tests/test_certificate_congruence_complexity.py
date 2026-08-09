import unittest

from enterprise_math.certificate_congruence_complexity import (
    congruence_complexity_from_factors,
)


class CertificateCongruenceComplexityTests(unittest.TestCase):
    def test_equal_order_four_has_different_guard_complexity(self) -> None:
        cyclic = congruence_complexity_from_factors((1, 4))
        klein = congruence_complexity_from_factors((2, 2))
        self.assertEqual(cyclic.defect_order, 4)
        self.assertEqual(klein.defect_order, 4)
        self.assertEqual(cyclic.independent_guard_count, 1)
        self.assertEqual(klein.independent_guard_count, 2)
        self.assertEqual(cyclic.defect_exponent, 4)
        self.assertEqual(klein.defect_exponent, 2)
        self.assertTrue(cyclic.cyclic)
        self.assertFalse(klein.cyclic)

    def test_2_4_tower_state_needs_two_guards(self) -> None:
        data = congruence_complexity_from_factors((2, 4))
        self.assertEqual(data.defect_order, 8)
        self.assertEqual(data.defect_exponent, 4)
        self.assertEqual(data.independent_guard_count, 2)
        self.assertEqual(data.prime_guard_profile, ((2, 2, (1, 2)),))

    def test_scalar_eta_defect_is_one_guard_when_nontrivial(self) -> None:
        eta_five = congruence_complexity_from_factors((5,))
        self.assertEqual(eta_five.defect_order, 5)
        self.assertEqual(eta_five.independent_guard_count, 1)
        self.assertEqual(eta_five.prime_guard_profile, ((5, 1, (1,)),))

        saturated = congruence_complexity_from_factors((1,))
        self.assertEqual(saturated.defect_order, 1)
        self.assertEqual(saturated.independent_guard_count, 0)
        self.assertTrue(saturated.cyclic)

    def test_mixed_prime_profile(self) -> None:
        data = congruence_complexity_from_factors((2, 6, 30))
        self.assertEqual(data.independent_guard_count, 3)
        self.assertEqual(data.defect_order, 360)
        self.assertEqual(
            data.prime_guard_profile,
            (
                (2, 3, (1, 1, 1)),
                (3, 2, (0, 1, 1)),
                (5, 1, (0, 0, 1)),
            ),
        )


if __name__ == "__main__":
    unittest.main()
