import unittest

from enterprise_math.geometry import graph_distance
from enterprise_math.intrinsic_collapse import (
    graph_collapse_targets,
    graph_common_collapse,
    graph_common_collapse_targets,
)


class IntrinsicCollapseTests(unittest.TestCase):
    def setUp(self):
        self.graph = {
            "a": {"b"},
            "b": {"a", "c", "e"},
            "c": {"b", "d"},
            "d": {"c", "f"},
            "e": {"b", "f"},
            "f": {"e", "d", "g"},
            "g": {"f"},
        }

    def test_graph_ball_uses_only_primitive_steps(self):
        self.assertEqual(graph_collapse_targets(self.graph, "b", 0), frozenset({"b"}))
        self.assertEqual(
            graph_collapse_targets(self.graph, "b", 1),
            frozenset({"a", "b", "c", "e"}),
        )

    def test_common_collapse_equals_radius_sum_distance_on_unweighted_graph(self):
        vertices = tuple(self.graph)
        for left in vertices:
            for right in vertices:
                distance = graph_distance(self.graph, left, right)
                for left_radius in range(5):
                    for right_radius in range(5):
                        with self.subTest(
                            left=left,
                            right=right,
                            left_radius=left_radius,
                            right_radius=right_radius,
                        ):
                            self.assertEqual(
                                graph_common_collapse(
                                    self.graph,
                                    left,
                                    left_radius,
                                    right,
                                    right_radius,
                                ),
                                distance <= left_radius + right_radius,
                            )

    def test_shared_witnesses_are_actual_targets_of_both_bodies(self):
        shared = graph_common_collapse_targets(self.graph, "a", 2, "g", 3)
        left = graph_collapse_targets(self.graph, "a", 2)
        right = graph_collapse_targets(self.graph, "g", 3)
        self.assertEqual(shared, left.intersection(right))
        self.assertTrue(shared)

    def test_invalid_graph_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            graph_collapse_targets(self.graph, "missing", 1)
        with self.assertRaises(ValueError):
            graph_collapse_targets(self.graph, "a", -1)
        broken = {"a": {"missing"}}
        with self.assertRaises(ValueError):
            graph_collapse_targets(broken, "a", 1)


if __name__ == "__main__":
    unittest.main()
