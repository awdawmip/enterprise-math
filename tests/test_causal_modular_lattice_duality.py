import unittest
from math import gcd

from enterprise_math.causal_modular_lattice_duality import (
    generated_changes_are_gcd_multiples,
    generated_operation_modulus,
    intersection_identity,
    simultaneous_constraint_modulus,
)


class CausalModularLatticeDualityTests(unittest.TestCase):
    def test_constraint_intersection_is_lcm_law(self):
        cases = ((2, 3, 6), (4, 6, 12), (6, 10, 30), (8, 12, 24))
        for left, right, expected in cases:
            self.assertEqual(simultaneous_constraint_modulus(left, right), expected)
            for value in range(-100, 101):
                self.assertTrue(intersection_identity(value, left, right))

    def test_operation_generation_has_gcd_total_change_quantum(self):
        cases = ((6, 10), (8, 12), (9, 15), (14, 21))
        for left, right in cases:
            self.assertEqual(generated_operation_modulus(left, right), gcd(left, right))
            self.assertTrue(generated_changes_are_gcd_multiples(left, right, 8))

    def test_more_constraints_and_more_operations_move_modulus_in_opposite_directions(self):
        left, right = 6, 10
        self.assertEqual(simultaneous_constraint_modulus(left, right), 30)
        self.assertEqual(generated_operation_modulus(left, right), 2)


if __name__ == "__main__":
    unittest.main()
