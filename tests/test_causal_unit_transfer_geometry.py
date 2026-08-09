import unittest

from enterprise_math.causal_lattice_direction_link import (
    a_direction_link_degree,
    a_edge_common_neighbor_graph_signature,
)
from enterprise_math.causal_unit_transfer_geometry import (
    a_p_shadow_identity,
    apply_transfer,
    canonical_transfer_decomposition,
    causal_dimension_from_conserved_slots,
    primitive_transfer_vectors,
    primitive_transfers,
    transfer_distance,
    transfer_distance_half_l1,
    transfer_edge_context_channel_sizes,
    transfer_link_degree,
    transfer_link_neighbors,
)
from enterprise_math.lattice_geometry import a_graph_distance


class CausalUnitTransferGeometryTests(unittest.TestCase):
    def test_unit_transfer_grammar_generates_exact_a_p_root_set(self):
        for slot_count in range(2, 9):
            self.assertTrue(a_p_shadow_identity(slot_count))
            self.assertEqual(
                len(primitive_transfer_vectors(slot_count)),
                slot_count * (slot_count - 1),
            )
            self.assertEqual(causal_dimension_from_conserved_slots(slot_count), slot_count - 1)

    def test_transfer_distance_is_exact_minimum_and_half_l1(self):
        cases = (
            ((0, 0, 0, 0), (2, -1, 0, -1)),
            ((3, -2, -1, 0), (0, 1, -3, 2)),
            ((5, -5), (-4, 4)),
        )
        for left, right in cases:
            distance = transfer_distance(left, right)
            self.assertEqual(distance, transfer_distance_half_l1(left, right))
            self.assertEqual(distance, a_graph_distance(left, right))
            moves = canonical_transfer_decomposition(left, right)
            self.assertEqual(len(moves), distance)
            state = left
            for move in moves:
                state = apply_transfer(state, move)
            self.assertEqual(state, right)

    def test_primitive_transfer_link_is_receiver_or_donor_sharing(self):
        for slot_count in range(3, 8):
            p = slot_count - 1
            transfer = (0, 1)
            neighbors = transfer_link_neighbors(slot_count, transfer)
            self.assertEqual(len(neighbors), 2 * (slot_count - 2))
            self.assertEqual(len(neighbors), transfer_link_degree(slot_count))
            self.assertEqual(transfer_link_degree(slot_count), a_direction_link_degree(p))
            self.assertEqual(
                transfer_edge_context_channel_sizes(slot_count, transfer),
                (slot_count - 2, slot_count - 2),
            )

    def test_receiver_donor_channel_split_is_exact_a_p_edge_context(self):
        for slot_count in range(3, 8):
            p = slot_count - 1
            receiver_size, donor_size = transfer_edge_context_channel_sizes(
                slot_count, (0, 1)
            )
            signature = a_edge_common_neighbor_graph_signature(p, (0, 1))
            self.assertEqual(signature[0], receiver_size + donor_size)
            self.assertEqual(signature[2], (receiver_size, donor_size))

    def test_three_dimensional_case_is_twelve_directed_unit_transfers(self):
        slot_count = 4
        self.assertEqual(len(primitive_transfers(slot_count)), 12)
        self.assertEqual(transfer_link_degree(slot_count), 4)
        self.assertEqual(transfer_edge_context_channel_sizes(slot_count, (0, 1)), (2, 2))


if __name__ == "__main__":
    unittest.main()
