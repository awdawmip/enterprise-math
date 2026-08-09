import unittest

from enterprise_math.common_collapse import iter_terminal_collapse_targets
from enterprise_math.engineering_collision import Body2D
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

    def test_pairwise_collisions_need_not_have_one_three_body_witness(self):
        cycle5 = {
            0: {1, 4},
            1: {0, 2},
            2: {1, 3},
            3: {2, 4},
            4: {3, 0},
        }
        supports = [graph_collapse_targets(cycle5, center, 1) for center in (0, 2, 4)]
        self.assertTrue(supports[0].intersection(supports[1]))
        self.assertTrue(supports[1].intersection(supports[2]))
        self.assertTrue(supports[0].intersection(supports[2]))
        self.assertFalse(supports[0].intersection(supports[1]).intersection(supports[2]))

    def test_e001_square_target_is_graph_ball_of_king_move_adjacency(self):
        points = [(x, y) for x in range(-5, 6) for y in range(-5, 6)]
        point_set = set(points)
        king_graph = {}
        for x, y in points:
            neighbors = {
                (x + dx, y + dy)
                for dx in (-1, 0, 1)
                for dy in (-1, 0, 1)
                if (dx, dy) != (0, 0) and (x + dx, y + dy) in point_set
            }
            king_graph[(x, y)] = neighbors

        body = Body2D(0, 0, 0, 3)
        graph_targets = graph_collapse_targets(king_graph, (body.x, body.y), body.radius)
        e001_targets = frozenset(iter_terminal_collapse_targets(body))
        self.assertEqual(graph_targets, e001_targets)
        for target in e001_targets:
            self.assertEqual(
                graph_distance(king_graph, (0, 0), target),
                max(abs(target[0]), abs(target[1])),
            )

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
