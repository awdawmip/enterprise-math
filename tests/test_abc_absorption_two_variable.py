import unittest

from enterprise_math.abc_absorption_two_variable import (
    minimum_linf_diophantine_solution,
    one_plus_two_primes_prime_power_access,
)


class AbcAbsorptionTwoVariableTests(unittest.TestCase):
    def test_generic_two_variable_minimum(self) -> None:
        solution = minimum_linf_diophantine_solution(5, 3, 32)
        self.assertEqual((solution.u, solution.v), (4, 4))
        self.assertEqual(solution.radius, 4)
        self.assertEqual(solution.triangle_lower_bound, 4)

    def test_one_plus_15_equals_16_is_sharp(self) -> None:
        data = one_plus_two_primes_prime_power_access(3, 5, 2, 4)
        self.assertEqual(data["eta_min"], 4)
        self.assertEqual(data["target"], 32)
        self.assertEqual(data["nu"], 4)
        self.assertEqual(data["triangle_lower_bound"], 4)
        self.assertTrue(data["lower_bound_is_sharp"])
        self.assertEqual(data["witness_q_r_p"], (4, 4, 1))

    def test_one_plus_511_equals_512_has_strict_triangle_gap(self) -> None:
        data = one_plus_two_primes_prime_power_access(7, 73, 2, 9)
        self.assertEqual(data["eta_min"], 9)
        self.assertEqual(data["target"], 2304)
        self.assertEqual(data["triangle_lower_bound"], 29)
        self.assertEqual(data["nu"], 33)
        self.assertFalse(data["lower_bound_is_sharp"])
        u, v, x_p = data["witness_q_r_p"]
        self.assertEqual(73 * u + 7 * v, 2304)
        self.assertEqual(x_p, 1)
        self.assertEqual(max(abs(u), abs(v), abs(x_p)), 33)

    def test_unsolvable_generic_equation_rejected(self) -> None:
        with self.assertRaises(ValueError):
            minimum_linf_diophantine_solution(6, 10, 7)

    def test_invalid_family_rejected(self) -> None:
        with self.assertRaises(ValueError):
            one_plus_two_primes_prime_power_access(3, 7, 2, 5)


if __name__ == "__main__":
    unittest.main()
