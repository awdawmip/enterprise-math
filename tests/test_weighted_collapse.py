import unittest

from enterprise_math.weighted_collapse import (
    compose_relations,
    weighted_common_collapse_targets,
    weighted_radius_relation,
    weighted_shortest_distances,
)


class WeightedCollapseTests(unittest.TestCase):
    def test_unit_edges_give_exact_additive_relation_composition(self):
        graph = {
            0: {1: 1},
            1: {0: 1, 2: 1, 3: 1},
            2: {1: 1, 3: 1},
            3: {1: 1, 2: 1, 4: 1},
            4: {3: 1},
        }
        for left_radius in range(4):
            for right_radius in range(4):
                left = weighted_radius_relation(graph, left_radius)
                right = weighted_radius_relation(graph, right_radius)
                total = weighted_radius_relation(graph, left_radius + right_radius)
                self.assertEqual(compose_relations(left, right), total)

    def test_atomic_weighted_edge_breaks_radius_sum_shortcut(self):
        graph = {
            "a": {"b": 2},
            "b": {"a": 2},
        }
        distances = weighted_shortest_distances(graph, "a")
        self.assertEqual(distances["b"], 2)
        self.assertLessEqual(distances["b"], 1 + 1)
        self.assertFalse(weighted_common_collapse_targets(graph, "a", 1, "b", 1))

        r1 = weighted_radius_relation(graph, 1)
        r2 = weighted_radius_relation(graph, 2)
        self.assertTrue(compose_relations(r1, r1).issubset(r2))
        self.assertNotEqual(compose_relations(r1, r1), r2)
        self.assertIn(("a", "b"), r2)
        self.assertNotIn(("a", "b"), compose_relations(r1, r1))

    def test_subdividing_atomic_edge_restores_shared_intermediate_state(self):
        graph = {
            "a": {"m": 1},
            "m": {"a": 1, "b": 1},
            "b": {"m": 1},
        }
        shared = weighted_common_collapse_targets(graph, "a", 1, "b", 1)
        self.assertEqual(shared, frozenset({"m"}))
        r1 = weighted_radius_relation(graph, 1)
        r2 = weighted_radius_relation(graph, 2)
        self.assertEqual(compose_relations(r1, r1), r2)

    def test_positive_integer_weights_are_required(self):
        with self.assertRaises(ValueError):
            weighted_radius_relation({"a": {"b": 0}, "b": {"a": 0}}, 1)
        with self.assertRaises(ValueError):
            weighted_radius_relation({"a": {"missing": 1}}, 1)


if __name__ == "__main__":
    unittest.main()
