import unittest

from enterprise_math.causal_operation_grade_filtration import (
    composition_respects_grade_filtration,
    filtration_count_from_histogram,
    grade_histogram_on_small_system,
    grade_zero_preserves_every_depth_threshold,
    semantic_grade_matches_minimum_layer_degree,
)
from enterprise_math.causal_semantic_grade import distinguishing_depth_matrix


class CausalOperationGradeFiltrationTests(unittest.TestCase):
    def setUp(self):
        self.states = (0, 1, 2, 3)
        self.observation = {0: 0, 1: 0, 2: 0, 3: 1}
        self.g = {0: 0, 1: 0, 2: 1, 3: 0}
        self.h = {0: 0, 1: 3, 2: 0, 3: 0}
        self.generators = {"g": self.g, "h": self.h}
        self.costs = {"g": 2, "h": 5}
        self.depth = distinguishing_depth_matrix(
            self.states,
            self.observation,
            self.generators,
            self.costs,
        )

    def test_semantic_grade_is_exact_minimum_cross_layer_degree(self):
        operations = (
            self.g,
            self.h,
            {state: state for state in self.states},
            {state: 0 for state in self.states},
        )
        for operation in operations:
            self.assertTrue(
                semantic_grade_matches_minimum_layer_degree(
                    self.states, self.depth, operation
                )
            )

    def test_grade_zero_is_exactly_preservation_of_every_future_threshold(self):
        identity = {state: state for state in self.states}
        reset = {state: 0 for state in self.states}
        self.assertTrue(
            grade_zero_preserves_every_depth_threshold(
                self.states, self.depth, identity
            )
        )
        self.assertTrue(
            grade_zero_preserves_every_depth_threshold(
                self.states, self.depth, reset
            )
        )

    def test_small_system_has_exact_semantic_operation_grade_histogram(self):
        histogram = grade_histogram_on_small_system(self.states, self.depth)
        self.assertEqual(histogram, {0: 64, 2: 48, 5: 48, 7: 96})
        self.assertEqual(sum(histogram.values()), 4 ** 4)
        self.assertEqual(filtration_count_from_histogram(histogram, 0), 64)
        self.assertEqual(filtration_count_from_histogram(histogram, 2), 112)
        self.assertEqual(filtration_count_from_histogram(histogram, 5), 160)
        self.assertEqual(filtration_count_from_histogram(histogram, 7), 256)

    def test_composition_respects_additive_grade_filtration(self):
        identity = {state: state for state in self.states}
        reset = {state: 0 for state in self.states}
        operations = (self.g, self.h, identity, reset)
        for first in operations:
            for second in operations:
                self.assertTrue(
                    composition_respects_grade_filtration(
                        self.states,
                        self.depth,
                        first,
                        second,
                    )
                )


if __name__ == "__main__":
    unittest.main()
