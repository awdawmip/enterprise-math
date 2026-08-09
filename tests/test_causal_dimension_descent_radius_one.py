import unittest

from enterprise_math.causal_dimension_descent_pressure import (
    a_radius_one_descent_defect,
    d_radius_one_descent_defect,
    e7_root_ball_radius_one_inside_e8,
    e8_fixed_direction_boundary_radius_one,
    e8_to_e7_radius_one_descent_defect,
    radius_one_directional_boundary_from_local_link,
    radius_one_descent_defect,
    z_radius_one_descent_defect,
)


class CausalDimensionDescentRadiusOneTests(unittest.TestCase):
    def test_generic_radius_one_boundary_formula_uses_only_first_link_data(self):
        # A3/FCC local data: N1=12, link degree=4 -> directional B1 size 7.
        self.assertEqual(
            radius_one_directional_boundary_from_local_link(12, 4),
            7,
        )
        # D4 local data: N1=24, link degree=8 -> directional B1 size 15.
        self.assertEqual(
            radius_one_directional_boundary_from_local_link(24, 8),
            15,
        )
        # E8 local data: N1=240, link degree=56 -> directional B1 size 183.
        self.assertEqual(
            radius_one_directional_boundary_from_local_link(240, 56),
            183,
        )

    def test_a_family_and_standard_axis_z_pass_radius_one_recursive_descent_gate(self):
        for p in range(2, 10):
            self.assertEqual(a_radius_one_descent_defect(p), 0)
        for dimension in range(2, 10):
            self.assertEqual(z_radius_one_descent_defect(dimension), 0)

    def test_d_family_fails_natural_same_family_radius_one_descent_by_exactly_two(self):
        for n in range(4, 12):
            self.assertEqual(d_radius_one_descent_defect(n), 2)

    def test_e8_to_e7_radius_one_defect_is_fifty_six(self):
        self.assertEqual(e8_fixed_direction_boundary_radius_one(), 183)
        self.assertEqual(e7_root_ball_radius_one_inside_e8(), 127)
        self.assertEqual(e8_to_e7_radius_one_descent_defect(), 56)
        self.assertEqual(
            radius_one_descent_defect(
                primitive_direction_count=240,
                direction_link_degree=56,
                lower_primitive_direction_count=126,
            ),
            56,
        )

    def test_radius_one_descent_and_local_link_connectedness_are_independent_axes(self):
        # Z^d has link degree zero yet passes the recursive boundary gate.
        self.assertEqual(radius_one_descent_defect(8, 0, 6), 0)
        # D4 has a connected 8-regular direction link but fails the D3 descent gate.
        self.assertEqual(radius_one_descent_defect(24, 8, 12), 2)


if __name__ == "__main__":
    unittest.main()
