import unittest
from itertools import product

from enterprise_math.causal_conserved_transfer_geometry import a3_to_d3_fcc
from enterprise_math.causal_transfer_graph_geometry import complete_transfer_edges, star_transfer_edges
from enterprise_math.causal_transfer_quadratic_shadow import (
    complete_dispersion_identity,
    complete_edge_dispersion,
    complete_zero_sum_bilinear_identity,
    complete_zero_sum_bilinear_shadow,
    complete_zero_sum_quadratic_shadow,
    edge_dispersion,
    polarized_edge_dispersion,
    primitive_second_moment_matrix,
    quadratic_from_second_moment,
    second_moment_matches_edge_dispersion,
)


class CausalTransferQuadraticShadowTests(unittest.TestCase):
    def test_complete_graph_pair_dispersion_identity_is_exact_integer(self):
        for slots in range(2, 7):
            for state in product(range(-2, 3), repeat=slots):
                self.assertTrue(complete_dispersion_identity(state))

    def test_zero_sum_complete_graph_reduces_to_slot_count_times_square_grade(self):
        for slots in range(2, 6):
            for state in product(range(-2, 3), repeat=slots):
                if sum(state) != 0:
                    continue
                self.assertEqual(complete_edge_dispersion(state), slots * sum(value * value for value in state))
                self.assertEqual(complete_zero_sum_quadratic_shadow(state), sum(value * value for value in state))

    def test_polarization_recovers_complete_zero_sum_bilinear_shadow(self):
        states = [state for state in product((-1, 0, 1), repeat=4) if sum(state) == 0]
        edges = complete_transfer_edges(4)
        for left in states:
            for right in states:
                self.assertEqual(
                    polarized_edge_dispersion(left, right, edges),
                    4 * sum(a * b for a, b in zip(left, right)),
                )
                self.assertTrue(complete_zero_sum_bilinear_identity(left, right))
                self.assertEqual(
                    complete_zero_sum_bilinear_shadow(left, right),
                    4 * sum(a * b for a, b in zip(left, right)),
                )

    def test_a3_to_d3_fcc_bridge_preserves_integer_square_grade(self):
        for state in product(range(-2, 3), repeat=4):
            if sum(state) != 0:
                continue
            image = a3_to_d3_fcc(state)
            self.assertEqual(
                sum(value * value for value in state),
                sum(value * value for value in image),
            )

    def test_star_mark_is_visible_in_second_order_relation_observation(self):
        edges = star_transfer_edges(4, hub=0)
        hub_aligned = (1, -1, 0, 0)
        leaf_internal = (0, 1, -1, 0)
        self.assertEqual(sum(value * value for value in hub_aligned), 2)
        self.assertEqual(sum(value * value for value in leaf_internal), 2)
        self.assertEqual(edge_dispersion(hub_aligned, edges), 6)
        self.assertEqual(edge_dispersion(leaf_internal, edges), 2)
        self.assertEqual(complete_edge_dispersion(hub_aligned), 8)
        self.assertEqual(complete_edge_dispersion(leaf_internal), 8)

    def test_second_moment_matrix_is_only_a_shadow_of_edge_relations(self):
        for slots, edges in (
            (4, star_transfer_edges(4, 0)),
            (4, complete_transfer_edges(4)),
            (5, ((0, 1), (1, 2), (2, 3), (3, 4))),
        ):
            matrix = primitive_second_moment_matrix(slots, edges)
            for state in product((-1, 0, 1), repeat=slots):
                self.assertEqual(quadratic_from_second_moment(state, matrix), edge_dispersion(state, edges))
                self.assertTrue(second_moment_matches_edge_dispersion(state, edges))

    def test_complete_second_moment_has_expected_integer_entries(self):
        matrix = primitive_second_moment_matrix(4, complete_transfer_edges(4))
        self.assertEqual(
            matrix,
            (
                (3, -1, -1, -1),
                (-1, 3, -1, -1),
                (-1, -1, 3, -1),
                (-1, -1, -1, 3),
            ),
        )


if __name__ == "__main__":
    unittest.main()
