import unittest
from itertools import product

from enterprise_math.causal_conserved_transfer_geometry import primitive_transfers
from enterprise_math.causal_transfer_graph_geometry import (
    complete_graph_is_fully_slot_exchange_symmetric,
    complete_graph_transfer_distance,
    complete_transfer_edges,
    generated_lattice_membership,
    primitive_transfer_moves,
    projected_star_primitive_moves,
    star_transfer_distance,
    star_transfer_edges,
    transfer_components,
    transfer_relation_rank,
)


class CausalTransferGraphGeometryTests(unittest.TestCase):
    def test_any_connected_transfer_graph_has_zero_sum_relation_rank_n_minus_one(self):
        cases = (
            (4, ((0, 1), (1, 2), (2, 3))),
            (4, star_transfer_edges(4, 0)),
            (4, complete_transfer_edges(4)),
            (5, ((0, 1), (0, 2), (2, 3), (3, 4))),
        )
        for slots, edges in cases:
            self.assertEqual(transfer_components(slots, edges), (tuple(range(slots)),))
            self.assertEqual(transfer_relation_rank(slots, edges), slots - 1)
            for vector in product(range(-2, 3), repeat=slots):
                self.assertEqual(
                    generated_lattice_membership(vector, slots, edges),
                    sum(vector) == 0,
                )

    def test_disconnected_graph_preserves_one_exact_total_per_component(self):
        slots = 5
        edges = ((0, 1), (1, 2), (3, 4))
        self.assertEqual(transfer_components(slots, edges), ((0, 1, 2), (3, 4)))
        self.assertEqual(transfer_relation_rank(slots, edges), 3)
        self.assertTrue(generated_lattice_membership((1, -1, 0, 2, -2), slots, edges))
        self.assertFalse(generated_lattice_membership((1, -1, 1, 1, -2), slots, edges))

    def test_complete_graph_primitives_are_exactly_a_roots(self):
        for slots in range(2, 7):
            self.assertEqual(
                set(primitive_transfer_moves(slots, complete_transfer_edges(slots))),
                set(primitive_transfers(slots)),
            )
            self.assertTrue(complete_graph_is_fully_slot_exchange_symmetric(slots))

    def test_star_projection_is_standard_axis_geometry(self):
        for p in range(1, 7):
            moves = set(projected_star_primitive_moves(p + 1, hub=0))
            expected = set()
            for axis in range(p):
                for sign in (-1, 1):
                    vector = [0] * p
                    vector[axis] = sign
                    expected.add(tuple(vector))
            self.assertEqual(moves, expected)
            self.assertEqual(len(moves), 2 * p)

    def test_star_metric_is_visible_l1_while_complete_graph_can_transfer_leaf_to_leaf_directly(self):
        left = (0, 1, 0, 0)
        right = (0, 0, 1, 0)
        self.assertEqual(complete_graph_transfer_distance(left, right), 1)
        self.assertEqual(star_transfer_distance(left, right, hub=0), 2)

        left = (3, 0, 0, 0)
        right = (0, 1, 1, 1)
        self.assertEqual(complete_graph_transfer_distance(left, right), 3)
        self.assertEqual(star_transfer_distance(left, right, hub=0), 3)

    def test_same_zero_sum_state_lattice_can_carry_different_primitive_geometries(self):
        slots = 4
        complete = complete_transfer_edges(slots)
        star = star_transfer_edges(slots, hub=0)
        samples = (
            (1, -1, 0, 0),
            (2, -1, -1, 0),
            (3, 2, -4, -1),
        )
        for vector in samples:
            self.assertTrue(generated_lattice_membership(vector, slots, complete))
            self.assertTrue(generated_lattice_membership(vector, slots, star))
        self.assertEqual(len(primitive_transfer_moves(slots, complete)), 12)
        self.assertEqual(len(primitive_transfer_moves(slots, star)), 6)


if __name__ == "__main__":
    unittest.main()
