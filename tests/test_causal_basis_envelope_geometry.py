import unittest
from itertools import product

from enterprise_math.causal_basis_envelope_geometry import (
    complete_distance_is_minimum_tree_distance,
    complete_metric_has_tree_witness,
    complete_tree_count,
    fixed_edge_tree_multiplicity,
    tree_transport_distance,
)
from enterprise_math.causal_relation_independence import spanning_relation_bases
from enterprise_math.causal_transfer_graph_geometry import complete_transfer_edges
from enterprise_math.causal_transfer_quadratic_shadow import edge_dispersion
from enterprise_math.causal_conserved_transfer_geometry import transfer_distance


class CausalBasisEnvelopeGeometryTests(unittest.TestCase):
    def test_complete_metric_is_minimum_over_all_tree_basis_metrics(self):
        for slots in range(2, 6):
            states = [state for state in product(range(-2, 3), repeat=slots) if sum(state) == 0]
            for left in states[:40]:
                for right in states[:40]:
                    self.assertTrue(complete_distance_is_minimum_tree_distance(left, right))

    def test_every_pair_has_constructive_shortest_tree_chart(self):
        cases = (
            ((3, 0, 0, 0), (0, 1, 1, 1)),
            ((0, 4, 1, 0), (2, 0, 1, 2)),
            ((3, -1, -1, -1), (0, 0, 0, 0)),
            ((2, -2, 1, -1, 0), (0, 0, 0, 0, 0)),
        )
        for left, right in cases:
            tree, distance = complete_metric_has_tree_witness(left, right)
            self.assertEqual(len(tree), len(left) - 1)
            self.assertEqual(distance, transfer_distance(left, right))
            self.assertEqual(tree_transport_distance(left, right, tree), distance)

    def test_cayley_tree_count_and_fixed_edge_multiplicity(self):
        for slots in range(2, 7):
            bases = spanning_relation_bases(slots, complete_transfer_edges(slots))
            self.assertEqual(len(bases), complete_tree_count(slots))
            fixed_edge = (0, 1)
            containing = sum(fixed_edge in tree for tree in bases)
            self.assertEqual(containing, fixed_edge_tree_multiplicity(slots))

    def test_sum_of_tree_quadratic_shadows_is_symmetric_complete_shadow(self):
        for slots in range(2, 6):
            trees = spanning_relation_bases(slots, complete_transfer_edges(slots))
            multiplier = fixed_edge_tree_multiplicity(slots)
            for state in product((-1, 0, 1), repeat=slots):
                tree_sum = sum(edge_dispersion(state, tree) for tree in trees)
                complete = edge_dispersion(state, complete_transfer_edges(slots))
                self.assertEqual(tree_sum, multiplier * complete)

    def test_single_tree_can_overestimate_anonymous_pair_transfer_but_envelope_restores_one(self):
        slots = 4
        trees = spanning_relation_bases(slots, complete_transfer_edges(slots))
        left = (0, 1, 0, -1)
        right = (0, 0, 1, -1)
        complete = transfer_distance(left, right)
        distances = [tree_transport_distance(left, right, tree) for tree in trees]
        self.assertEqual(complete, 1)
        self.assertEqual(min(distances), 1)
        self.assertGreater(max(distances), 1)


if __name__ == "__main__":
    unittest.main()
