import unittest

from enterprise_math.precision_genesis import compatible_paths
from enterprise_math.precision_hierarchy_geometry import (
    hierarchy_ball,
    hierarchy_distance,
    hierarchy_shell,
    minimum_distance_adjacency,
    ultrametric_holds,
)


class PrecisionHierarchyGeometryTests(unittest.TestCase):
    def setUp(self):
        self.scales = (1, 2, 4, 8)
        paths = compatible_paths(self.scales)
        self.signatures = {state: paths[state] for state in range(8)}

    def test_precision_one_has_only_trivial_geometry(self):
        signatures = {0: (0,)}
        self.assertEqual(hierarchy_distance((1,), signatures, 0, 0), 0)
        self.assertEqual(minimum_distance_adjacency((1,), signatures), frozenset())
        self.assertTrue(ultrametric_holds((1,), signatures))

    def test_exact_divisibility_weighted_distances(self):
        self.assertEqual(hierarchy_distance(self.scales, self.signatures, 0, 1), 2)
        self.assertEqual(hierarchy_distance(self.scales, self.signatures, 0, 2), 4)
        self.assertEqual(hierarchy_distance(self.scales, self.signatures, 0, 4), 8)
        self.assertEqual(hierarchy_distance(self.scales, self.signatures, 3, 3), 0)

    def test_strong_triangle_inequality_holds_exhaustively(self):
        self.assertTrue(ultrametric_holds(self.scales, self.signatures))

    def test_ball_and_shell_growth_can_mimic_one_dimensional_growth(self):
        self.assertEqual(
            tuple(len(hierarchy_ball(self.scales, self.signatures, 0, radius)) for radius in (1, 2, 4, 8)),
            (1, 2, 4, 8),
        )
        self.assertEqual(
            tuple(len(hierarchy_shell(self.scales, self.signatures, 0, radius)) for radius in (2, 4, 8)),
            (1, 2, 4),
        )

    def test_minimum_distance_graph_is_not_a_macroscopic_line(self):
        self.assertEqual(
            minimum_distance_adjacency(self.scales, self.signatures),
            frozenset(
                {
                    frozenset((0, 1)),
                    frozenset((2, 3)),
                    frozenset((4, 5)),
                    frozenset((6, 7)),
                }
            ),
        )

    def test_bad_chain_fails_closed(self):
        with self.assertRaises(ValueError):
            hierarchy_distance((1, 3, 4), self.signatures, 0, 1)


if __name__ == "__main__":
    unittest.main()
