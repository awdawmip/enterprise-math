import unittest
from itertools import combinations, product

from enterprise_math.causal_transfer_boundary_contraction import (
    directional_cut_states,
    word_ball,
)
from enterprise_math.causal_transfer_boundary_duality import (
    all_cut_states_have_supporting_probes,
    boundary_probe_partition,
    directional_boundary_probe_certificate_holds,
    directional_boundary_probe_witnesses,
    witness_forces_next_radius,
)
from enterprise_math.causal_transfer_graph_geometry import (
    complete_transfer_edges,
    star_transfer_edges,
    transfer_components,
)


def _connected_graphs(slot_count):
    possible = tuple(combinations(range(slot_count), 2))
    for mask in range(1, 1 << len(possible)):
        edges = tuple(edge for index, edge in enumerate(possible) if mask & (1 << index))
        if len(transfer_components(slot_count, edges)) == 1:
            yield edges


class CausalTransferBoundaryDualityTests(unittest.TestCase):
    def test_every_four_slot_graph_cut_state_has_integer_supporting_probe(self):
        for edges in _connected_graphs(4):
            for oriented_edge in edges:
                for radius in range(3):
                    self.assertTrue(
                        all_cut_states_have_supporting_probes(4, edges, oriented_edge, radius)
                    )
                    for state in word_ball(4, edges, radius):
                        self.assertTrue(
                            directional_boundary_probe_certificate_holds(
                                4, edges, oriented_edge, radius, state
                            )
                        )

    def test_supporting_probe_saturates_ball_and_edge_response(self):
        edges = complete_transfer_edges(4)
        edge = (0, 1)
        radius = 2
        for state in directional_cut_states(4, edges, edge, radius):
            witnesses = directional_boundary_probe_witnesses(4, edges, edge, radius, state)
            self.assertTrue(witnesses)
            self.assertTrue(
                all(
                    witness_forces_next_radius(state, witness, 4, edges, edge, radius)
                    for witness in witnesses
                )
            )

    def test_noncut_interior_state_has_no_false_boundary_certificate(self):
        edges = star_transfer_edges(4, 0)
        edge = (0, 1)
        radius = 3
        cut = directional_cut_states(4, edges, edge, radius)
        interior = next(state for state in word_ball(4, edges, radius - 1) if state not in cut)
        self.assertEqual(
            directional_boundary_probe_witnesses(4, edges, edge, radius, interior),
            (),
        )

    def test_boundary_probe_partition_exposes_multiple_normals_when_geometry_has_corner_context(self):
        edges = complete_transfer_edges(4)
        edge = (0, 1)
        partition = boundary_probe_partition(4, edges, edge, radius=2)
        self.assertTrue(partition)
        witness_counts = {len(witnesses) for witnesses in partition.values()}
        self.assertTrue(all(count >= 1 for count in witness_counts))

    def test_complete_and_tree_transfer_laws_share_same_primal_dual_boundary_rule(self):
        cases = (
            (4, complete_transfer_edges(4), (0, 1)),
            (4, star_transfer_edges(4, 0), (0, 1)),
            (5, ((0, 1), (1, 2), (2, 3), (3, 4)), (1, 2)),
        )
        for slots, edges, edge in cases:
            for radius in range(4):
                self.assertTrue(all_cut_states_have_supporting_probes(slots, edges, edge, radius))


if __name__ == "__main__":
    unittest.main()
