import unittest

from enterprise_math.causal_horizon_grade_duality import (
    horizon_semantic_grade_witness,
    shortest_distinguishing_word,
    shortest_witness_is_semantic_grade_tight,
    word_declared_cost,
)
from enterprise_math.causal_weighted_horizon import weighted_composition_horizon


class CausalHorizonGradeDualityTests(unittest.TestCase):
    def setUp(self):
        self.states = (0, 1, 2, 3)
        self.observation = {0: 0, 1: 0, 2: 0, 3: 1}
        self.generators = {
            "g": {0: 0, 1: 0, 2: 1, 3: 0},
            "h": {0: 0, 1: 3, 2: 0, 3: 0},
        }
        self.costs = {"g": 2, "h": 5}

    def test_every_finitely_distinguishable_pair_has_grade_tight_shortest_witness(self):
        for left in self.states:
            for right in self.states:
                self.assertTrue(
                    shortest_witness_is_semantic_grade_tight(
                        self.states,
                        self.observation,
                        self.generators,
                        self.costs,
                        left,
                        right,
                    )
                )

    def test_hardest_pair_witness_realizes_weighted_horizon_as_semantic_grade(self):
        horizon = weighted_composition_horizon(
            self.states,
            self.observation,
            self.generators,
            self.costs,
        )
        self.assertEqual(horizon, 7)
        witness = horizon_semantic_grade_witness(
            self.states,
            self.observation,
            self.generators,
            self.costs,
        )
        self.assertIsNotNone(witness)
        left, right, word, grade = witness
        self.assertEqual(grade, horizon)
        result = shortest_distinguishing_word(
            self.states,
            self.observation,
            self.generators,
            self.costs,
            left,
            right,
        )
        self.assertIsNotNone(result)
        distance, shortest_word = result
        self.assertEqual(distance, horizon)
        self.assertEqual(word_declared_cost(shortest_word, self.costs), horizon)

    def test_currently_distinguishable_pair_has_empty_zero_grade_witness(self):
        result = shortest_distinguishing_word(
            self.states,
            self.observation,
            self.generators,
            self.costs,
            0,
            3,
        )
        self.assertEqual(result, (0, ()))
        self.assertTrue(
            shortest_witness_is_semantic_grade_tight(
                self.states,
                self.observation,
                self.generators,
                self.costs,
                0,
                3,
            )
        )

    def test_permanently_equivalent_pair_has_no_witness(self):
        states = (0, 1, 2)
        observation = {0: 0, 1: 0, 2: 1}
        generators = {"id": {0: 0, 1: 1, 2: 2}}
        costs = {"id": 4}
        self.assertIsNone(
            shortest_distinguishing_word(
                states, observation, generators, costs, 0, 1
            )
        )


if __name__ == "__main__":
    unittest.main()
