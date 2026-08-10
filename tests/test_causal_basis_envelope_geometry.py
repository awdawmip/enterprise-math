import unittest
from itertools import combinations, product

from enterprise_math.causal_basis_envelope_geometry import (
    basis_quadratic_edge_weights,
    complete_distance_is_minimum_tree_distance,
    complete_metric_has_tree_witness,
    complete_tree_count,
    edge_tree_multiplicity,
    fixed_edge_tree_multiplicity,
    graph_metric_envelope_identity,
    graph_metric_via_tree_envelope,
    graph_word_distance_bfs,
    spanning_tree_count,
    sum_tree_edge_dispersion,
    tree_transport_distance,
)
from enterprise_math.causal_relation_independence import spanning_relation_bases
from enterprise_math.causal_transfer_graph_geometry import (
    complete_transfer_edges,
    star_transfer_edges,
    transfer_components,
)
from enterprise_math.causal_transfer_quadratic_shadow import edge_dispersion
from enterprise_math.causal_conserved_transfer_geometry import transfer_distance


def _connected_graphs(slot_count):
    possible = tuple(combinations(range(slot_count), 2))
    for mask in range(1, 1 << len(possible)):
        edges = tuple(edge for index, edge in enumerate(possible) if mask & (1 << index))
        if len(transfer_components(slot_count, edges)) == 1:
            yield edges


class CausalBasisEnvelopeGeometryTests(unittest.TestCase):
    def test_complete_metric_is_minimum_over_all_tree_basis_metrics(self):
        for slots in range(2, 6):
            states = [state for state in product(range(-2, 3), repeat=slots) if sum(state) == 0]
            for left in states[:40]:
                for right in states[:40]:
                    self.assertTrue(complete_distance_is_minimum_tree_distance(left, right))

    def test_every_pair_has_constructive_shortest_complete_tree_chart(self):
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

    def test_all_connected_four_slot_graphs_match_bfs_and_tree_envelope_on_small_states(self):
        states = [state for state in product((-1, 0, 1), repeat=4) if sum(state) == 0]
        for edges in _connected_graphs(4):
            for state in states:
                origin = (0, 0, 0, 0)
                self.assertTrue(graph_metric_envelope_identity(origin, state, edges))
                self.assertEqual(
                    graph_metric_via_tree_envelope(origin, state, edges),
                    graph_word_distance_bfs(origin, state, edges),
                )

    def test_cayley_tree_count_and_fixed_edge_multiplicity(self):
        for slots in range(2, 7):
            bases = spanning_relation_bases(slots, complete_transfer_edges(slots))
            self.assertEqual(len(bases), complete_tree_count(slots))
            self.assertEqual(len(bases), spanning_tree_count(slots, complete_transfer_edges(slots)))
            fixed_edge = (0, 1)
            containing = sum(fixed_edge in tree for tree in bases)
            self.assertEqual(containing, fixed_edge_tree_multiplicity(slots))
            self.assertEqual(
                edge_tree_multiplicity(slots, complete_transfer_edges(slots), fixed_edge),
                containing,
            )

    def test_general_tree_shadow_sum_uses_edge_basis_multiplicities(self):
        graphs = (
            (4, ((0, 1), (1, 2), (2, 3), (0, 3))),
            (4, ((0, 1), (1, 2), (2, 3), (0, 2))),
            (5, ((0, 1), (1, 2), (2, 3), (3, 4), (0, 4))),
        )
        for slots, edges in graphs:
            trees = spanning_relation_bases(slots, edges)
            weights = basis_quadratic_edge_weights(slots, edges)
            self.assertEqual(set(weights), set(tuple(sorted(edge)) for edge in edges))
            for state in product((-1, 0, 1), repeat=slots):
                direct = sum(edge_dispersion(state, tree) for tree in trees)
                self.assertEqual(sum_tree_edge_dispersion(state, edges), direct)

    def test_sum_of_complete_tree_quadratic_shadows_is_symmetric_complete_shadow(self):
        for slots in range(2, 6):
            trees = spanning_relation_bases(slots, complete_transfer_edges(slots))
            multiplier = fixed_edge_tree_multiplicity(slots)
            weights = basis_quadratic_edge_weights(slots, complete_transfer_edges(slots))
            self.assertEqual(set(weights.values()), {multiplier})
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

    def test_tree_geometry_has_single_basis_and_complete_geometry_has_many(self):
        for slots in range(2, 7):
            self.assertEqual(spanning_tree_count(slots, star_transfer_edges(slots, 0)), 1)
            self.assertEqual(spanning_tree_count(slots, complete_transfer_edges(slots)), slots ** (slots - 2))


if __name__ == "__main__":
    unittest.main()
