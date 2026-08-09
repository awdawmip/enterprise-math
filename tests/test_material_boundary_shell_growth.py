import unittest
from math import factorial

from enterprise_math.material_boundary_shell_growth import (
    boundary_shell_degree_certificate,
    coarse_only_contact_states,
    forward_difference,
    represented_boundary_shell_states,
)


class MaterialBoundaryShellGrowthTests(unittest.TestCase):
    def test_closed_form_matches_direct_sum_of_depth_shells(self):
        for dimension in range(1, 6):
            for depth in range(1, 6):
                for factor in range(depth, depth + 8):
                    direct = sum(
                        (factor - k + 1) ** dimension - (factor - k) ** dimension
                        for k in range(1, depth + 1)
                    )
                    self.assertEqual(
                        represented_boundary_shell_states(dimension, depth, factor),
                        direct,
                    )

    def test_exact_discrete_degree_certificate(self):
        for dimension in range(1, 7):
            for depth in range(1, 5):
                lower, upper = boundary_shell_degree_certificate(dimension, depth)
                self.assertTrue(lower)
                self.assertTrue(upper)
                self.assertTrue(
                    all(value == factorial(dimension) * depth for value in lower)
                )
                self.assertTrue(all(value == 0 for value in upper))

    def test_full_coarse_box_keeps_one_higher_discrete_degree(self):
        for dimension in range(1, 6):
            values = tuple(
                coarse_only_contact_states(dimension, factor)
                for factor in range(1, dimension + 3)
            )
            nth = forward_difference(values, dimension)
            self.assertTrue(all(value == factorial(dimension) for value in nth))

    def test_fixed_depth_shell_is_strictly_smaller_than_full_box_once_inner_core_exists(self):
        for dimension in range(1, 5):
            for depth in range(1, 5):
                for factor in range(depth + 1, depth + 7):
                    represented = represented_boundary_shell_states(
                        dimension, depth, factor
                    )
                    full = coarse_only_contact_states(dimension, factor)
                    self.assertLessEqual(represented, full)
                    if factor - depth >= 2:
                        self.assertLess(represented, full)

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            represented_boundary_shell_states(0, 1, 1)
        with self.assertRaises(ValueError):
            represented_boundary_shell_states(1, 0, 1)
        with self.assertRaises(ValueError):
            represented_boundary_shell_states(1, 2, 1)
        with self.assertRaises(ValueError):
            coarse_only_contact_states(1, 0)
        with self.assertRaises(ValueError):
            forward_difference((), 0)
        with self.assertRaises(ValueError):
            forward_difference((1, 2), 2)
        with self.assertRaises(ValueError):
            boundary_shell_degree_certificate(2, 3, 2)


if __name__ == "__main__":
    unittest.main()
