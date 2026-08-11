import unittest

from enterprise_math.future_word_cache_pareto import (
    block_decompose_word,
    cache_execution_rounds,
    execute_from_cache,
    free_fixture_hits_literal_storage_bound,
    literal_word_count,
    minimum_cache_depth_for_round_budget,
    minimum_literal_storage_for_round_budget,
    prefix_append_free_effect_fixture,
    unique_effect_count,
    word_cache_pareto_frontier,
    word_transformation,
)


class FutureWordCacheParetoTests(unittest.TestCase):
    def test_literal_storage_formula(self):
        self.assertEqual(literal_word_count(1, 5), 5)
        self.assertEqual(literal_word_count(2, 1), 2)
        self.assertEqual(literal_word_count(2, 2), 6)
        self.assertEqual(literal_word_count(2, 3), 14)
        self.assertEqual(literal_word_count(3, 2), 12)

    def test_block_round_formula_and_decomposition(self):
        word = tuple("abcdefgh")
        for depth, expected_rounds in ((1, 8), (2, 4), (3, 3), (4, 2), (5, 2), (8, 1)):
            blocks = block_decompose_word(word, depth)
            self.assertEqual(len(blocks), expected_rounds)
            self.assertEqual(cache_execution_rounds(len(word), depth), expected_rounds)
            self.assertEqual(tuple(symbol for block in blocks for symbol in block), word)
            self.assertTrue(all(1 <= len(block) <= depth for block in blocks))

    def test_minimum_cache_depth_for_runtime_budget(self):
        horizon = 8
        expected = {
            1: 8,
            2: 4,
            3: 3,
            4: 2,
            5: 2,
            8: 1,
            20: 1,
        }
        for rounds, depth in expected.items():
            self.assertEqual(minimum_cache_depth_for_round_budget(horizon, rounds), depth)
            self.assertLessEqual(cache_execution_rounds(horizon, depth), rounds)
            if depth > 1:
                self.assertGreater(cache_execution_rounds(horizon, depth - 1), rounds)

    def test_minimum_storage_for_round_budget(self):
        self.assertEqual(minimum_literal_storage_for_round_budget(2, 8, 8), 2)
        self.assertEqual(minimum_literal_storage_for_round_budget(2, 8, 4), 6)
        self.assertEqual(minimum_literal_storage_for_round_budget(2, 8, 3), 14)
        self.assertEqual(minimum_literal_storage_for_round_budget(2, 8, 2), 30)
        self.assertEqual(minimum_literal_storage_for_round_budget(2, 8, 1), 510)

    def test_binary_horizon_eight_pareto_frontier(self):
        frontier = word_cache_pareto_frontier(2, 8)
        depths = tuple(point.cache_depth for point in frontier)
        self.assertEqual(depths, (1, 2, 3, 4, 8))
        resources = tuple(
            (point.literal_cache_entries, point.worst_case_execution_rounds)
            for point in frontier
        )
        self.assertEqual(
            resources,
            ((2, 8), (6, 4), (14, 3), (30, 2), (510, 1)),
        )

    def test_cached_execution_matches_literal_transformation(self):
        states, operations = prefix_append_free_effect_fixture(2, 4)
        word = (0, 1, 1, 0)
        direct = word_transformation(states, operations, word)
        for depth in (1, 2, 3, 4):
            self.assertEqual(
                execute_from_cache(states, operations, word, depth),
                direct,
            )

    def test_free_prefix_fixture_makes_literal_storage_bound_sharp(self):
        self.assertTrue(free_fixture_hits_literal_storage_bound(2, 3))
        self.assertTrue(free_fixture_hits_literal_storage_bound(3, 2))

    def test_semantic_effect_count_can_be_far_smaller_than_literal_table(self):
        states = (0, 1)
        identity = {0: 0, 1: 1}
        operations = {
            "a": identity,
            "b": identity,
        }
        self.assertEqual(literal_word_count(2, 4), 30)
        self.assertEqual(unique_effect_count(states, operations, 4), 1)

    def test_small_semigroup_collapses_many_words(self):
        states = (0, 1)
        operations = {
            "id": {0: 0, 1: 1},
            "flip": {0: 1, 1: 0},
        }
        self.assertEqual(literal_word_count(2, 5), 62)
        self.assertEqual(unique_effect_count(states, operations, 5), 2)

    def test_validation(self):
        with self.assertRaises(ValueError):
            literal_word_count(0, 1)
        with self.assertRaises(ValueError):
            cache_execution_rounds(1, 0)
        with self.assertRaises(ValueError):
            minimum_cache_depth_for_round_budget(0, 1)


if __name__ == "__main__":
    unittest.main()
