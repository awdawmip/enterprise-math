import unittest

from enterprise_math.precision_genesis import compatible_paths
from enterprise_math.precision_hierarchy_bridges import (
    boundary_minimal_bridge_edges,
    canonical_minimal_bridge_edges,
    graph_diameter,
    minimum_bridge_edge_count,
    refinement_bridge_certificate_holds,
)


class PrecisionHierarchyBridgeTests(unittest.TestCase):
    def setUp(self):
        self.scales = (1, 2, 4, 8)
        paths = compatible_paths(self.scales)
        self.signatures = {state: paths[state] for state in range(8)}

    def test_minimum_certificate_edge_count_telescopes_to_n_minus_one(self):
        self.assertEqual(minimum_bridge_edge_count(self.scales, self.signatures), 7)

    def test_canonical_minimal_bridges_connect_every_child_quotient(self):
        edges = canonical_minimal_bridge_edges(self.scales, self.signatures)
        self.assertEqual(len(edges), 7)
        self.assertTrue(
            refinement_bridge_certificate_holds(self.scales, self.signatures, tuple(edges))
        )
        self.assertEqual(
            edges,
            frozenset(
                {
                    frozenset((0, 4)),
                    frozenset((0, 2)),
                    frozenset((4, 6)),
                    frozenset((0, 1)),
                    frozenset((2, 3)),
                    frozenset((4, 5)),
                    frozenset((6, 7)),
                }
            ),
        )
        self.assertEqual(graph_diameter(tuple(self.signatures), tuple(edges)), 5)

    def test_boundary_witness_choice_gives_same_minimal_count_but_path_geometry(self):
        edges = boundary_minimal_bridge_edges(self.scales, self.signatures)
        self.assertEqual(len(edges), 7)
        self.assertTrue(
            refinement_bridge_certificate_holds(self.scales, self.signatures, tuple(edges))
        )
        self.assertEqual(
            edges,
            frozenset(
                {
                    frozenset((3, 4)),
                    frozenset((1, 2)),
                    frozenset((5, 6)),
                    frozenset((0, 1)),
                    frozenset((2, 3)),
                    frozenset((4, 5)),
                    frozenset((6, 7)),
                }
            ),
        )
        self.assertEqual(graph_diameter(tuple(self.signatures), tuple(edges)), 7)

    def test_hierarchy_alone_fails_bridge_certificate(self):
        self.assertFalse(
            refinement_bridge_certificate_holds(self.scales, self.signatures, ())
        )

    def test_missing_one_root_bridge_breaks_certificate(self):
        edges = set(canonical_minimal_bridge_edges(self.scales, self.signatures))
        edges.remove(frozenset((0, 4)))
        self.assertFalse(
            refinement_bridge_certificate_holds(self.scales, self.signatures, tuple(edges))
        )


if __name__ == "__main__":
    unittest.main()
