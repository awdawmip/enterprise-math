import unittest
from itertools import combinations, product

from enterprise_math.causal_transfer_duality import (
    integer_transfer_response_duality,
    integer_unit_response_potentials,
    maximum_unit_response,
    pair_probe_range_bound,
    primal_transfer_distance,
)
from enterprise_math.causal_transfer_graph_geometry import (
    complete_transfer_edges,
    slot_shortest_path_distance,
    star_transfer_edges,
    transfer_components,
)


def _connected_graphs(slot_count):
    possible = tuple(combinations(range(slot_count), 2))
    for mask in range(1, 1 << len(possible)):
        edges = tuple(edge for index, edge in enumerate(possible) if mask & (1 << index))
        if len(transfer_components(slot_count, edges)) == 1:
            yield edges


class CausalTransferDualityTests(unittest.TestCase):
    def test_all_connected_four_slot_graphs_match_primal_and_dual_on_small_displacements(self):
        displacements = [state for state in product((-1, 0, 1), repeat=4) if sum(state) == 0]
        for edges in _connected_graphs(4):
            for displacement in displacements:
                self.assertTrue(integer_transfer_response_duality(displacement, edges))
                self.assertEqual(
                    primal_transfer_distance(displacement, edges),
                    maximum_unit_response(displacement, edges),
                )

    def test_pair_probe_range_is_exact_slot_graph_distance(self):
        graphs = (
            (4, star_transfer_edges(4, 0)),
            (4, complete_transfer_edges(4)),
            (5, ((0, 1), (1, 2), (2, 3), (3, 4))),
            (5, ((0, 1), (1, 2), (2, 3), (3, 4), (0, 4))),
        )
        for slots, edges in graphs:
            for left in range(slots):
                for right in range(slots):
                    self.assertEqual(
                        pair_probe_range_bound(slots, edges, left, right),
                        slot_shortest_path_distance(slots, edges, left, right),
                    )

    def test_full_anonymous_transfer_limits_every_pair_probe_difference_to_one(self):
        for slots in range(2, 7):
            edges = complete_transfer_edges(slots)
            potentials = integer_unit_response_potentials(slots, edges)
            self.assertTrue(potentials)
            for potential in potentials:
                self.assertLessEqual(max(potential) - min(potential), 1)

    def test_tree_hidden_topology_allows_probe_drift_across_multiple_anonymous_slots(self):
        edges = ((0, 1), (1, 2), (2, 3))
        self.assertEqual(pair_probe_range_bound(4, edges, 0, 3), 3)
        self.assertEqual(pair_probe_range_bound(4, complete_transfer_edges(4), 0, 3), 1)

    def test_dual_response_cell_is_finite_after_anchor_gauge_fixing(self):
        complete = integer_unit_response_potentials(4, complete_transfer_edges(4), anchor=0)
        star = integer_unit_response_potentials(4, star_transfer_edges(4, 0), anchor=0)
        self.assertGreater(len(star), len(complete))
        self.assertTrue(all(potential[0] == 0 for potential in complete + star))


if __name__ == "__main__":
    unittest.main()
