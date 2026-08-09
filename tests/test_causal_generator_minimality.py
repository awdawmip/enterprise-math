import unittest

from enterprise_math.causal_generator_minimality import (
    bounded_minimum_direction_count,
    direction_link_degree_set,
    edge_contexts_uniform,
    first_bounded_candidate,
    primitive_edge_context_signature,
)


class CausalGeneratorMinimalityTests(unittest.TestCase):
    def test_rank_two_box_first_regular_connected_candidate_has_six_directions(self):
        result = bounded_minimum_direction_count(2, coordinate_bound=1, maximum_direction_count=8)
        self.assertIsNotNone(result)
        count, candidate = result
        self.assertEqual(count, 6)
        self.assertEqual(direction_link_degree_set(candidate), (2,))
        self.assertTrue(edge_contexts_uniform(candidate))

    def test_rank_three_box_has_no_regular_connected_candidate_below_twelve_directions(self):
        for count in (6, 8, 10):
            self.assertIsNone(first_bounded_candidate(3, count, coordinate_bound=1))

    def test_rank_three_first_regular_connected_candidate_has_twelve_directions_and_fcc_context(self):
        candidate = first_bounded_candidate(3, 12, coordinate_bound=1)
        self.assertIsNotNone(candidate)
        self.assertEqual(direction_link_degree_set(candidate), (4,))
        self.assertTrue(edge_contexts_uniform(candidate))
        signatures = {
            primitive_edge_context_signature(candidate, direction)
            for direction in candidate
        }
        self.assertEqual(signatures, {(4, 2, (2, 2), (1, 1, 1, 1))})

    def test_bounded_search_with_edge_context_gate_still_first_hits_twelve_in_rank_three(self):
        result = bounded_minimum_direction_count(
            3,
            coordinate_bound=1,
            maximum_direction_count=12,
            require_uniform_edge_context=True,
        )
        self.assertIsNotNone(result)
        self.assertEqual(result[0], 12)


if __name__ == "__main__":
    unittest.main()
