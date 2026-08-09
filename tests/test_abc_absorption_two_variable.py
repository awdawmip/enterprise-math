import unittest

from enterprise_math.abc_absorption_two_variable import (
    integrality_access_defect_bound,
    lower_bound_sharp_modular_criterion,
    minimum_linf_diophantine_solution,
    one_plus_two_primes_prime_power_access,
    sharp_integrality_defect_example,
)


class AbcAbsorptionTwoVariableTests(unittest.TestCase):
    def test_generic_two_variable_minimum(self) -> None:
        solution = minimum_linf_diophantine_solution(5, 3, 32)
        self.assertEqual((solution.u, solution.v), (4, 4))
        self.assertEqual(solution.radius, 4)
        self.assertEqual(solution.triangle_lower_bound, 4)

    def test_modular_lower_bound_sharpness_criterion(self) -> None:
        sharp = lower_bound_sharp_modular_criterion(5, 3, 32)
        self.assertTrue(sharp["sharp"])
        self.assertEqual(sharp["lower_bound"], 4)

        nonsharp = lower_bound_sharp_modular_criterion(73, 7, 2304)
        self.assertFalse(nonsharp["sharp"])
        self.assertEqual(nonsharp["lower_bound"], 29)

    def test_universal_integrality_defect_bound_exhaustive_small(self) -> None:
        for A in range(1, 16):
            for B in range(1, 16):
                for N in range(1, 40):
                    import math

                    if N % math.gcd(A, B):
                        continue
                    data = integrality_access_defect_bound(A, B, N)
                    self.assertLessEqual(
                        data["defect"], data["universal_defect_upper_bound"]
                    )

    def test_universal_defect_bound_is_sharp_for_both_parities(self) -> None:
        for reduced_max in range(2, 15):
            data = sharp_integrality_defect_example(reduced_max)
            self.assertEqual(data["defect"], (reduced_max - 1) // 2)

    def test_one_plus_15_equals_16_is_sharp(self) -> None:
        data = one_plus_two_primes_prime_power_access(3, 5, 2, 4)
        self.assertEqual(data["eta_min"], 4)
        self.assertEqual(data["target"], 32)
        self.assertEqual(data["nu"], 4)
        self.assertEqual(data["triangle_lower_bound"], 4)
        self.assertEqual(data["integrality_access_defect"], 0)
        self.assertTrue(data["lower_bound_is_sharp"])
        self.assertEqual(data["witness_q_r_p"], (4, 4, 1))

    def test_one_plus_511_equals_512_has_strict_triangle_gap(self) -> None:
        data = one_plus_two_primes_prime_power_access(7, 73, 2, 9)
        self.assertEqual(data["eta_min"], 9)
        self.assertEqual(data["target"], 2304)
        self.assertEqual(data["triangle_lower_bound"], 29)
        self.assertEqual(data["nu"], 33)
        self.assertEqual(data["integrality_access_defect"], 4)
        self.assertLessEqual(
            data["integrality_access_defect"], data["universal_defect_upper_bound"]
        )
        self.assertFalse(data["lower_bound_is_sharp"])
        u, v, x_p = data["witness_q_r_p"]
        self.assertEqual(73 * u + 7 * v, 2304)
        self.assertEqual(x_p, 1)
        self.assertEqual(max(abs(u), abs(v), abs(x_p)), 33)

    def test_unsolvable_generic_equation_rejected(self) -> None:
        with self.assertRaises(ValueError):
            minimum_linf_diophantine_solution(6, 10, 7)
        with self.assertRaises(ValueError):
            integrality_access_defect_bound(6, 10, 7)

    def test_invalid_family_rejected(self) -> None:
        with self.assertRaises(ValueError):
            one_plus_two_primes_prime_power_access(3, 7, 2, 5)


if __name__ == "__main__":
    unittest.main()
