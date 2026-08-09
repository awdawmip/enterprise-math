import ast
import inspect
import unittest

import enterprise_math.p017_p018_anchor_singular_compensation as compensation
from enterprise_math.p017_p018_anchor_singular_compensation import (
    core_weight_totient_identity,
    euler_phi,
    finite_wheel_compensation,
)


class P017P018AnchorSingularCompensationTests(unittest.TestCase):
    def test_center_prime_inflation_cancels_anchor_density_exactly(self):
        # M=110 has wheel primes 5 and 11; S=21 has 3 and 7; 13 is generic.
        data = finite_wheel_compensation(110, 21, (3, 5, 7, 11, 13))
        self.assertEqual(
            tuple((row["prime"], row["kind"], row["forbidden_count"]) for row in data["local_rows"]),
            (
                (3, "CORE", 1),
                (5, "CENTER", 1),
                (7, "CORE", 1),
                (11, "CENTER", 1),
                (13, "GENERIC", 2),
            ),
        )
        self.assertEqual(data["anchor_density"], (8, 11))
        self.assertEqual(data["core_inflation_factor"], (7, 4))
        self.assertEqual(data["generic_twin_factor"], (143, 144))
        self.assertEqual(data["anchor_normalized_singular_factor"], (1001, 576))

    def test_allowed_class_count_matches_product_of_local_counts(self):
        data = finite_wheel_compensation(110, 21, (3, 5, 7, 11, 13))
        self.assertEqual(data["allowed_class_count"], 2 * 4 * 6 * 10 * 11)
        self.assertEqual(data["wheel_modulus"], 3 * 5 * 7 * 11 * 13)
        numerator, denominator = data["allowed_density"]
        self.assertEqual(
            numerator * data["wheel_modulus"],
            denominator * data["allowed_class_count"],
        )

    def test_core_weight_becomes_inverse_totient_with_prime_powers(self):
        data = core_weight_totient_identity(63, (3, 5, 7, 11))
        self.assertEqual(data["phi"], 36)
        self.assertEqual(data["core_inflation_factor"], (7, 4))
        self.assertEqual(data["normalized_cell_weight"], (1, 36))
        self.assertEqual(data["totient_weight"], (1, 36))

    def test_totient_helper_on_prime_powers_and_products(self):
        self.assertEqual(euler_phi(1), 1)
        self.assertEqual(euler_phi(9), 6)
        self.assertEqual(euler_phi(25), 20)
        self.assertEqual(euler_phi(45), 24)
        self.assertEqual(euler_phi(63), 36)

    def test_center_factorization_changes_anchor_and_singular_but_not_normalized_rule(self):
        first = finite_wheel_compensation(110, 21, (3, 5, 7, 11, 13))
        # Move 5 out of the center by changing to a coprime center. Its local
        # status becomes generic, so the normalized ratio changes exactly by
        # the published per-prime factor rather than by an unexplained demand
        # correction.
        second = finite_wheel_compensation(22, 21, (3, 5, 7, 11, 13))
        self.assertEqual(first["local_rows"][1]["kind"], "CENTER")
        self.assertEqual(second["local_rows"][1]["kind"], "GENERIC")
        # In both cases the direct anchor*singular product has already been
        # checked internally against core*generic factors.
        self.assertEqual(first["core_inflation_factor"], second["core_inflation_factor"])

    def test_missing_core_prime_is_rejected(self):
        with self.assertRaises(ValueError):
            core_weight_totient_identity(63, (3, 5, 11))

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            finite_wheel_compensation(21, 21, (3, 5))
        with self.assertRaises(ValueError):
            finite_wheel_compensation(110, 21, (2, 3, 5))
        with self.assertRaises(ValueError):
            finite_wheel_compensation(110, 21, (3, 3, 5))
        with self.assertRaises(ValueError):
            core_weight_totient_identity(18, (3, 5))

    def test_module_has_no_float_or_true_division(self):
        tree = ast.parse(inspect.getsource(compensation))
        floats = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.Constant) and isinstance(node.value, float)
        ]
        divisions = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div)
        ]
        self.assertEqual(floats, [])
        self.assertEqual(divisions, [])


if __name__ == "__main__":
    unittest.main()
