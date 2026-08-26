import ast
import inspect
import unittest

import enterprise_math.p017_p018_core_mass_euler as core_mass
from enterprise_math.p017_p018_core_mass_euler import (
    anchor_core_relative_factor,
    anchor_demand_square_penalty,
    anchor_normalized_finite_mass,
    core_mass_euler_factor,
    distinct_prime_factor_count,
    finite_split_totient_mass,
    ordered_nontrivial_coprime_split_count,
    prime_power_mass_partial,
)


def pair_lt(left, right):
    return left[0] * right[1] < right[0] * left[1]


class P017P018CoreMassEulerTests(unittest.TestCase):
    def test_split_counts(self):
        self.assertEqual(distinct_prime_factor_count(81), 1)
        self.assertEqual(distinct_prime_factor_count(9 * 125), 2)
        self.assertEqual(distinct_prime_factor_count(3 * 5 * 7), 3)
        self.assertEqual(ordered_nontrivial_coprime_split_count(81), 0)
        self.assertEqual(ordered_nontrivial_coprime_split_count(9 * 125), 2)
        self.assertEqual(ordered_nontrivial_coprime_split_count(3 * 5 * 7), 6)

    def test_exact_local_euler_factors(self):
        self.assertEqual(core_mass_euler_factor(3), (5, 2))
        self.assertEqual(anchor_demand_square_penalty(3), (9, 4))
        self.assertEqual(anchor_core_relative_factor(3), (9, 10))
        self.assertEqual(core_mass_euler_factor(5), (13, 8))
        self.assertEqual(anchor_core_relative_factor(5), (25, 26))
        for prime in (3, 5, 7, 11, 13, 17, 19):
            relative = anchor_core_relative_factor(prime)
            self.assertEqual(relative, (prime * prime, prime * prime + 1))
            self.assertLess(relative[0], relative[1])

    def test_prime_power_partial_remainder(self):
        first = prime_power_mass_partial(3, 1)
        self.assertEqual(first["partial_mass"], (2, 1))
        self.assertEqual(first["tail_remainder"], (1, 2))
        self.assertEqual(first["full_euler_factor"], (5, 2))
        second = prime_power_mass_partial(3, 2)
        self.assertEqual(second["partial_mass"], (7, 3))
        self.assertEqual(second["tail_remainder"], (1, 6))
        self.assertEqual(second["full_euler_factor"], (5, 2))

    def test_finite_mass_keeps_minus_two(self):
        self.assertEqual(finite_split_totient_mass(20), (1, 4))
        self.assertEqual(finite_split_totient_mass(20, (3,)), (0, 1))

    def test_anchor_exclusion_direction_on_finite_samples(self):
        for bound in (100, 250, 500):
            unrestricted = finite_split_totient_mass(bound)
            for prime in (3, 5, 7):
                normalized = anchor_normalized_finite_mass(bound, (prime,))
                self.assertTrue(pair_lt(normalized, unrestricted))
        self.assertTrue(
            pair_lt(anchor_normalized_finite_mass(500, (3, 5)), finite_split_totient_mass(500))
        )

    def test_validation(self):
        with self.assertRaises(ValueError):
            core_mass_euler_factor(9)
        with self.assertRaises(ValueError):
            prime_power_mass_partial(3, 0)
        with self.assertRaises(ValueError):
            finite_split_totient_mass(100, (9,))

    def test_module_has_no_float_or_true_division(self):
        tree = ast.parse(inspect.getsource(core_mass))
        floats = [node for node in ast.walk(tree) if isinstance(node, ast.Constant) and isinstance(node.value, float)]
        divisions = [node for node in ast.walk(tree) if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div)]
        self.assertEqual(floats, [])
        self.assertEqual(divisions, [])


if __name__ == "__main__":
    unittest.main()
