import unittest

from enterprise_math.precision_ordered_geometry import (
    dyadic_interval_hierarchy,
    hierarchy_matches_declared_order,
    integer_path_edges,
    interval_hierarchy,
    ordered_boundary_edges,
    ordered_boundary_edges_for_scales,
    ordered_boundary_path_theorem_holds,
    ordered_boundary_path_theorem_holds_for_scales,
    ordered_path_ball,
    ordered_path_distance,
    ordered_path_distance_for_scales,
)


class PrecisionOrderedGeometryTests(unittest.TestCase):
    def test_dyadic_boundary_union_is_exact_integer_path(self):
        for size in (1, 2, 4, 8, 16, 32, 64):
            self.assertTrue(ordered_boundary_path_theorem_holds(size))
            self.assertEqual(ordered_boundary_edges(size), integer_path_edges(size))
            self.assertEqual(len(ordered_boundary_edges(size)), size - 1)

    def test_general_divisibility_chains_also_give_exact_path(self):
        chains = (
            (1,),
            (1, 3, 6),
            (1, 2, 6, 12),
            (1, 4, 12),
            (1, 5, 10, 30),
            (1, 2, 10, 30),
            (1, 3, 15, 60),
        )
        for scales in chains:
            self.assertTrue(ordered_boundary_path_theorem_holds_for_scales(scales))
            self.assertEqual(
                ordered_boundary_edges_for_scales(scales),
                integer_path_edges(scales[-1]),
            )

    def test_path_distance_is_absolute_integer_difference(self):
        self.assertEqual(ordered_path_distance(0, 7, 8), 7)
        self.assertEqual(ordered_path_distance(2, 5, 8), 3)
        self.assertEqual(ordered_path_distance_for_scales(4, 19, (1, 5, 10, 30)), 15)

    def test_path_balls_have_expected_boundary_truncation(self):
        self.assertEqual(ordered_path_ball(3, 2, 8), frozenset({1, 2, 3, 4, 5}))
        self.assertEqual(ordered_path_ball(0, 2, 8), frozenset({0, 1, 2}))
        self.assertEqual(ordered_path_ball(7, 3, 8), frozenset({4, 5, 6, 7}))

    def test_canonical_hierarchy_matches_declared_order(self):
        scales, signatures = interval_hierarchy((1, 3, 6))
        self.assertTrue(hierarchy_matches_declared_order(scales, signatures))
        malformed = dict(signatures)
        malformed[0] = malformed[1]
        self.assertFalse(hierarchy_matches_declared_order(scales, malformed))

    def test_dyadic_wrapper_matches_general_interval_hierarchy(self):
        self.assertEqual(dyadic_interval_hierarchy(8), interval_hierarchy((1, 2, 4, 8)))

    def test_invalid_chains_and_states_fail_closed(self):
        with self.assertRaises(ValueError):
            interval_hierarchy((2, 4, 8))
        with self.assertRaises(ValueError):
            interval_hierarchy((1, 3, 8))
        with self.assertRaises(ValueError):
            dyadic_interval_hierarchy(6)
        with self.assertRaises(ValueError):
            ordered_path_distance(0, 8, 8)


if __name__ == "__main__":
    unittest.main()
