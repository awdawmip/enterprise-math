import unittest
from itertools import combinations

from enterprise_math.causal_transfer_ehrhart_shadow import (
    ball_growth_sequence,
    difference_table,
    ehrhart_shadow_statement,
    exact_polynomial_degree_from_samples,
    shell_growth_sequence,
    transfer_growth_rank_matches_difference_degree,
)
from enterprise_math.causal_transfer_graph_geometry import (
    complete_transfer_edges,
    star_transfer_edges,
    transfer_components,
    transfer_relation_rank,
)


def _connected_graphs(slot_count):
    possible = tuple(combinations(range(slot_count), 2))
    for mask in range(1, 1 << len(possible)):
        edges = tuple(edge for index, edge in enumerate(possible) if mask & (1 << index))
        if len(transfer_components(slot_count, edges)) == 1:
            yield edges


class CausalTransferEhrhartShadowTests(unittest.TestCase):
    def test_all_connected_graphs_on_up_to_four_slots_have_ball_degree_equal_relation_rank(self):
        for slots in range(2, 5):
            for edges in _connected_graphs(slots):
                self.assertTrue(transfer_growth_rank_matches_difference_degree(slots, edges))
                rank, degree = ehrhart_shadow_statement(slots, edges)
                self.assertEqual(rank, slots - 1)
                self.assertEqual(degree, rank)

    def test_complete_a_p_growth_degree_is_p(self):
        for p in range(1, 6):
            slots = p + 1
            edges = complete_transfer_edges(slots)
            self.assertEqual(transfer_relation_rank(slots, edges), p)
            self.assertTrue(transfer_growth_rank_matches_difference_degree(slots, edges))

    def test_tree_simple_cubic_type_has_same_degree_but_different_counts(self):
        slots = 4
        star = star_transfer_edges(slots, 0)
        complete = complete_transfer_edges(slots)
        star_growth = ball_growth_sequence(slots, star, 5)
        complete_growth = ball_growth_sequence(slots, complete, 5)
        self.assertEqual(exact_polynomial_degree_from_samples(star_growth), 3)
        self.assertEqual(exact_polynomial_degree_from_samples(complete_growth), 3)
        self.assertNotEqual(star_growth, complete_growth)
        self.assertTrue(all(left <= right for left, right in zip(star_growth, complete_growth)))

    def test_shell_is_first_difference_of_ball_count(self):
        slots = 4
        edges = complete_transfer_edges(slots)
        balls = ball_growth_sequence(slots, edges, 6)
        shells = shell_growth_sequence(slots, edges, 6)
        self.assertEqual(shells[0], 1)
        self.assertEqual(shells[1:], tuple(balls[i] - balls[i - 1] for i in range(1, len(balls))))
        table = difference_table(balls)
        self.assertEqual(len(set(table[3])), 1)

    def test_disconnected_graph_degree_is_n_minus_component_count(self):
        slots = 5
        edges = ((0, 1), (1, 2), (3, 4))
        rank = transfer_relation_rank(slots, edges)
        self.assertEqual(rank, 3)
        self.assertTrue(transfer_growth_rank_matches_difference_degree(slots, edges))


if __name__ == "__main__":
    unittest.main()
