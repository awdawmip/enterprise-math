import unittest

from enterprise_math.precision_product_geometry import (
    equal_capacity_geometry_profiles,
    product_grid_ball,
    product_grid_diameter,
    product_grid_distance,
    product_grid_edge_count,
    product_grid_edges,
    product_grid_states,
    product_grid_vertex_count,
)


class PrecisionProductGeometryTests(unittest.TestCase):
    def test_two_ordered_axes_give_exact_finite_grid(self):
        axes = ((1, 2, 4), (1, 2, 4))
        self.assertEqual(product_grid_vertex_count(axes), 16)
        self.assertEqual(len(product_grid_states(axes)), 16)
        self.assertEqual(product_grid_edge_count(axes), 24)
        self.assertEqual(len(product_grid_edges(axes)), 24)
        self.assertEqual(product_grid_diameter(axes), 6)
        self.assertEqual(product_grid_distance((0, 0), (3, 3), axes), 6)
        self.assertEqual(product_grid_distance((1, 3), (3, 0), axes), 5)

    def test_three_axes_give_exact_l1_distance(self):
        axes = ((1, 2, 4), (1, 3), (1, 2))
        self.assertEqual(product_grid_vertex_count(axes), 24)
        self.assertEqual(product_grid_distance((0, 0, 0), (3, 2, 1), axes), 6)
        self.assertEqual(product_grid_diameter(axes), 6)

    def test_grid_ball_is_intrinsic_graph_l1_ball(self):
        axes = ((1, 2, 4), (1, 2, 4))
        self.assertEqual(
            product_grid_ball((1, 1), 1, axes),
            frozenset({(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)}),
        )
        self.assertEqual(len(product_grid_ball((0, 0), 2, axes)), 6)

    def test_same_scalar_capacity_does_not_determine_dimension_or_diameter(self):
        profiles = equal_capacity_geometry_profiles(16)
        self.assertEqual(profiles["path"], (1, 16, 15))
        self.assertEqual(profiles["square"], (2, 16, 6))
        self.assertEqual(profiles["binary_cube"], (4, 16, 4))
        self.assertEqual({profile[1] for profile in profiles.values()}, {16})
        self.assertEqual({profile[2] for profile in profiles.values()}, {15, 6, 4})

    def test_non_dyadic_axis_chains_are_allowed(self):
        axes = ((1, 3, 6), (1, 5))
        self.assertEqual(product_grid_vertex_count(axes), 30)
        self.assertEqual(product_grid_diameter(axes), 9)
        self.assertEqual(product_grid_distance((0, 0), (5, 4), axes), 9)

    def test_invalid_axes_and_states_fail_closed(self):
        with self.assertRaises(ValueError):
            product_grid_states(())
        with self.assertRaises(ValueError):
            product_grid_states(((2, 4),))
        with self.assertRaises(ValueError):
            product_grid_distance((0,), (0, 0), ((1, 2), (1, 2)))
        with self.assertRaises(ValueError):
            product_grid_distance((2, 0), (0, 0), ((1, 2), (1, 2)))
        with self.assertRaises(ValueError):
            equal_capacity_geometry_profiles(12)


if __name__ == "__main__":
    unittest.main()
