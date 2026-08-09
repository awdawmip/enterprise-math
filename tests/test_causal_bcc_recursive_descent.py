import unittest

from enterprise_math.causal_bcc_recursive_descent import (
    bcc_ball_count,
    bcc_boundary_equals_a2_ball,
    bcc_directional_boundary_count,
    bcc_directional_boundary_count_bruteforce,
    bcc_first_direction_link_edge_count,
    bcc_primitive_directions,
)
from enterprise_math.lattice_geometry import a_ball_count


class CausalBCCRecursiveDescentTests(unittest.TestCase):
    def test_scaled_bcc_has_eight_primitive_directions_and_edgeless_first_link(self):
        self.assertEqual(len(bcc_primitive_directions()), 8)
        self.assertEqual(bcc_first_direction_link_edge_count(), 0)

    def test_bcc_ball_closed_formula(self):
        self.assertEqual(
            tuple(bcc_ball_count(radius) for radius in range(6)),
            (1, 9, 35, 91, 189, 341),
        )

    def test_bcc_directional_boundary_is_exact_a2_ball(self):
        expected = (1, 7, 19, 37, 61, 91)
        self.assertEqual(
            tuple(bcc_directional_boundary_count(radius) for radius in range(6)),
            expected,
        )
        for radius in range(8):
            self.assertTrue(bcc_boundary_equals_a2_ball(radius))
            self.assertEqual(
                bcc_directional_boundary_count(radius),
                a_ball_count(2, radius),
            )

    def test_closed_directional_boundary_formula_matches_bruteforce(self):
        for radius in range(5):
            self.assertEqual(
                bcc_directional_boundary_count(radius),
                bcc_directional_boundary_count_bruteforce(radius),
            )

    def test_recursive_descent_does_not_imply_local_direction_link_connectedness(self):
        self.assertTrue(bcc_boundary_equals_a2_ball(4))
        self.assertEqual(bcc_first_direction_link_edge_count(), 0)


if __name__ == "__main__":
    unittest.main()
