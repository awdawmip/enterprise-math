import unittest
from itertools import product

from enterprise_math.causal_dimension_descent_pressure import (
    a_directional_boundary_count,
    a_directional_boundary_lift,
    a_directional_boundary_project,
    d3_a3_ball_count,
    d4_coordinate_cap_boundary_count,
    d4_directional_boundary_count,
    d4_directional_boundary_count_bruteforce,
    d4_l1_face_boundary_count,
    d4_same_family_descent_defect,
    e7_orthogonal_root_count_inside_e8,
    e7_root_ball_radius_one_inside_e8,
    e8_fixed_direction_boundary_radius_one,
    e8_to_e7_radius_one_descent_defect,
    z_directional_boundary_bijection,
    z_directional_boundary_count,
    z_l1_ball_count,
)
from enterprise_math.lattice_geometry import a_ball_count


class CausalDimensionDescentPressureTests(unittest.TestCase):
    def test_standard_axis_z_d_has_exact_same_family_directional_descent(self):
        for dimension in range(1, 7):
            for radius in range(0, 7):
                self.assertEqual(
                    z_directional_boundary_count(dimension, radius),
                    z_l1_ball_count(dimension - 1, radius),
                )

        # Explicit bijection y -> (r-||y||_1,y).
        radius = 4
        lower = [
            y
            for y in product(range(-radius, radius + 1), repeat=2)
            if sum(abs(value) for value in y) <= radius
        ]
        lifted = {z_directional_boundary_bijection(y, radius) for y in lower}
        self.assertEqual(len(lifted), z_l1_ball_count(2, radius))
        self.assertTrue(
            all(
                sum(abs(value) for value in x) == radius and x[0] >= 0
                for x in lifted
            )
        )

    def test_a_p_has_exact_same_family_directional_descent_and_explicit_bijection(self):
        for p in range(2, 6):
            for radius in range(0, 6):
                self.assertEqual(
                    a_directional_boundary_count(p, radius),
                    a_ball_count(p - 1, radius),
                )

        # Exhaust the A2 radius-3 ball, lift it to the +e0-e1 boundary sector
        # of A3, and project back exactly.
        radius = 3
        lower = [
            y
            for y in product(range(-radius, radius + 1), repeat=3)
            if sum(y) == 0 and sum(value for value in y if value > 0) <= radius
        ]
        lifted = [a_directional_boundary_lift(y, radius) for y in lower]
        self.assertEqual(len(set(lifted)), a_ball_count(2, radius))
        self.assertTrue(
            all(a_directional_boundary_project(x) == y for x, y in zip(lifted, lower))
        )

    def test_d4_directional_boundary_closed_formula_matches_bruteforce(self):
        expected = (1, 15, 65, 175, 369, 671)
        self.assertEqual(
            tuple(d4_directional_boundary_count(radius) for radius in range(6)),
            expected,
        )
        for radius in range(0, 5):
            self.assertEqual(
                d4_directional_boundary_count(radius),
                d4_directional_boundary_count_bruteforce(radius),
            )
            self.assertEqual(
                d4_directional_boundary_count(radius),
                d4_l1_face_boundary_count(radius)
                + d4_coordinate_cap_boundary_count(radius),
            )

    def test_d4_fails_natural_same_family_descent_to_d3(self):
        d3 = tuple(d3_a3_ball_count(radius) for radius in range(6))
        d4_boundary = tuple(d4_directional_boundary_count(radius) for radius in range(6))
        self.assertEqual(d3, (1, 13, 55, 147, 309, 561))
        self.assertNotEqual(d4_boundary, d3)
        for radius in range(1, 7):
            self.assertEqual(
                d4_same_family_descent_defect(radius),
                radius * (radius + 1) * (2 * radius + 1) // 3,
            )
            self.assertGreater(d4_same_family_descent_defect(radius), 0)

    def test_e8_radius_one_directional_boundary_fails_natural_e7_root_ball_descent(self):
        self.assertEqual(e7_orthogonal_root_count_inside_e8(), 126)
        self.assertEqual(e7_root_ball_radius_one_inside_e8(), 127)
        self.assertEqual(e8_fixed_direction_boundary_radius_one(), 183)
        self.assertEqual(e8_to_e7_radius_one_descent_defect(), 56)

    def test_recursive_descent_is_independent_of_local_direction_link_connectedness(self):
        # Z^d passes exact recursive directional descent even though the separate
        # local-isotropy pressure test shows its first-direction link is edgeless.
        # D4/E8 have strong connected uniform local links but fail the natural
        # recursive descent candidate. These axes must therefore remain separate.
        self.assertEqual(z_directional_boundary_count(4, 3), z_l1_ball_count(3, 3))
        self.assertGreater(d4_same_family_descent_defect(3), 0)
        self.assertGreater(e8_to_e7_radius_one_descent_defect(), 0)


if __name__ == "__main__":
    unittest.main()
