import unittest

from enterprise_math.collapse_relation_limits import (
    common_target_count,
    graph_as_edge_target_supports,
    intersection_pairs,
)


class CollapseRelationLimitsTests(unittest.TestCase):
    def test_any_simple_graph_can_be_encoded_as_support_intersections(self):
        vertices = ("a", "b", "c", "d", "e")
        edges = (("a", "b"), ("b", "c"), ("c", "d"), ("a", "d"))
        supports = graph_as_edge_target_supports(vertices, edges)
        expected = frozenset(frozenset(edge) for edge in edges)
        self.assertEqual(intersection_pairs(supports), expected)

    def test_same_pair_collision_graph_can_hide_different_triple_structure(self):
        edge_supports = {
            "a": frozenset({"ab", "ac"}),
            "b": frozenset({"ab", "bc"}),
            "c": frozenset({"ac", "bc"}),
        }
        one_shared_target = {
            "a": frozenset({"z"}),
            "b": frozenset({"z"}),
            "c": frozenset({"z"}),
        }
        self.assertEqual(intersection_pairs(edge_supports), intersection_pairs(one_shared_target))
        self.assertEqual(common_target_count(edge_supports, ("a", "b", "c")), 0)
        self.assertEqual(common_target_count(one_shared_target, ("a", "b", "c")), 1)

    def test_edge_target_encoding_preserves_isolated_vertices_without_fake_edges(self):
        supports = graph_as_edge_target_supports((0, 1, 2), ((0, 1),))
        self.assertEqual(intersection_pairs(supports), frozenset({frozenset((0, 1))}))
        self.assertEqual(supports[2], frozenset())

    def test_invalid_simple_graph_is_rejected(self):
        with self.assertRaises(ValueError):
            graph_as_edge_target_supports((0, 1), ((0, 0),))
        with self.assertRaises(ValueError):
            graph_as_edge_target_supports((0, 1), ((0, 2),))
        with self.assertRaises(ValueError):
            graph_as_edge_target_supports((0, 1), ((0, 1), (1, 0)))


if __name__ == "__main__":
    unittest.main()
