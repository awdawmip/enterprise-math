import unittest
from itertools import product

from enterprise_math.causal_shell_boundary_incidence import (
    a_inward_degree_closed_form,
    a_inward_degree_identity,
    a_lower_ball_boundary_identity,
    a_support_signature,
    a_weighted_shell_incidence,
    relation_boundary_is_outer_shell_inward_incidence,
    word_shell,
)
from enterprise_math.causal_transfer_boundary_contraction import word_ball
from enterprise_math.causal_transfer_graph_geometry import (
    complete_transfer_edges,
    star_transfer_edges,
)


class CausalShellBoundaryIncidenceTests(unittest.TestCase):
    def test_relation_boundary_is_outer_shell_inward_incidence_for_multiple_graphs(self):
        graphs = (
            (3, complete_transfer_edges(3)),
            (4, complete_transfer_edges(4)),
            (4, star_transfer_edges(4, 0)),
            (4, ((0, 1), (1, 2), (2, 3))),
            (4, ((0, 1), (1, 2), (2, 3), (3, 0))),
        )
        for slots, edges in graphs:
            for radius in range(4):
                self.assertTrue(
                    relation_boundary_is_outer_shell_inward_incidence(
                        slots, edges, radius
                    )
                )

    def test_a_inward_degree_is_positive_support_times_negative_support(self):
        for slots in range(2, 7):
            for state in product(range(-2, 3), repeat=slots):
                if sum(state) != 0 or not any(state):
                    continue
                positive, negative, zero = a_support_signature(state)
                self.assertEqual(positive + negative + zero, slots)
                self.assertEqual(a_inward_degree_closed_form(state), positive * negative)
                self.assertTrue(a_inward_degree_identity(state))

    def test_a_weighted_shell_incidence_equals_lower_rank_ball_factor(self):
        for slots in range(2, 7):
            for radius in range(4):
                self.assertTrue(a_lower_ball_boundary_identity(slots, radius))

    def test_state_shell_count_and_relation_boundary_count_are_distinct_observations(self):
        slots = 4
        edges = complete_transfer_edges(slots)
        radius = 2
        shell = word_shell(slots, edges, radius + 1)
        shell_count = len(shell)
        weighted = a_weighted_shell_incidence(slots, radius)
        self.assertGreater(weighted, shell_count)

    def test_word_shell_is_exact_ball_difference(self):
        slots = 4
        edges = complete_transfer_edges(slots)
        for radius in range(1, 5):
            self.assertEqual(
                word_shell(slots, edges, radius),
                word_ball(slots, edges, radius) - word_ball(slots, edges, radius - 1),
            )


if __name__ == "__main__":
    unittest.main()
