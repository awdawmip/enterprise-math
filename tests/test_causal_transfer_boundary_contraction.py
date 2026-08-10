import unittest
from itertools import combinations

from enterprise_math.causal_transfer_boundary_contraction import (
    boundary_contraction_bijection_holds,
    boundary_contraction_projection,
    contract_transfer_graph,
    directional_cut_states,
    word_ball,
)
from enterprise_math.causal_transfer_graph_geometry import (
    complete_transfer_edges,
    star_transfer_edges,
    transfer_components,
)


def _all_connected_graphs(slot_count):
    possible = tuple(combinations(range(slot_count), 2))
    for mask in range(1, 1 << len(possible)):
        edges = tuple(edge for index, edge in enumerate(possible) if mask & (1 << index))
        if len(transfer_components(slot_count, edges)) == 1:
            yield edges


class CausalTransferBoundaryContractionTests(unittest.TestCase):
    def test_complete_graph_recovers_a_p_directional_lowering(self):
        for slots in range(3, 6):
            edges = complete_transfer_edges(slots)
            edge = edges[0]
            for radius in range(4):
                projection = boundary_contraction_projection(slots, edges, edge, radius)
                new_n, new_edges, _ = contract_transfer_graph(slots, edges, edge)
                self.assertEqual(len(projection), len(word_ball(new_n, new_edges, radius)))
                self.assertTrue(boundary_contraction_bijection_holds(slots, edges, edge, radius))

    def test_star_graph_recovers_simple_cubic_dimension_lowering(self):
        for slots in range(3, 7):
            edges = star_transfer_edges(slots, hub=0)
            for edge in edges:
                for radius in range(4):
                    self.assertTrue(boundary_contraction_bijection_holds(slots, edges, edge, radius))

    def test_paths_cycles_and_mixed_graphs_also_lower_by_edge_contraction(self):
        graphs = (
            (4, ((0, 1), (1, 2), (2, 3))),
            (4, ((0, 1), (1, 2), (2, 3), (0, 3))),
            (4, ((0, 1), (1, 2), (0, 2), (2, 3))),
            (5, ((0, 1), (1, 2), (2, 3), (3, 4), (0, 4))),
        )
        for slots, edges in graphs:
            for edge in edges:
                for radius in range(4):
                    self.assertTrue(boundary_contraction_bijection_holds(slots, edges, edge, radius))

    def test_all_connected_simple_graphs_on_four_slots_pass_small_radius_oracle(self):
        checked = 0
        for edges in _all_connected_graphs(4):
            checked += 1
            for edge in edges:
                for radius in range(3):
                    self.assertTrue(boundary_contraction_bijection_holds(4, edges, edge, radius))
        self.assertEqual(checked, 38)

    def test_directional_cut_has_one_state_per_contracted_ball_state(self):
        slots = 4
        edges = ((0, 1), (1, 2), (2, 3), (0, 2))
        edge = (0, 2)
        radius = 3
        cut = directional_cut_states(slots, edges, edge, radius)
        projection = boundary_contraction_projection(slots, edges, edge, radius)
        self.assertEqual(set(projection), set(cut))
        self.assertEqual(len(projection), len(set(projection.values())))


if __name__ == "__main__":
    unittest.main()
