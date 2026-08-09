import unittest

from enterprise_math.causal_graded_precision_transport import (
    all_depth_loss_bounds_hold,
    layer_map_for_word,
    layer_transport_property,
    word_cost,
    word_layer_composition_is_exact,
)


class CausalGradedPrecisionTransportTests(unittest.TestCase):
    def setUp(self):
        self.states = (0, 1, 2, 3)
        self.observation = {0: 0, 1: 0, 2: 0, 3: 1}
        self.generators = {
            "g": {0: 0, 1: 0, 2: 1, 3: 0},
            "h": {0: 0, 1: 3, 2: 0, 3: 0},
        }
        self.costs = {"g": 2, "h": 5}

    def test_generator_cost_consumes_exact_future_budget(self):
        for label in self.generators:
            word = (label,)
            for target_budget in range(8):
                self.assertTrue(
                    layer_transport_property(
                        self.states,
                        self.observation,
                        self.generators,
                        self.costs,
                        word,
                        target_budget,
                    )
                )
                mapping = layer_map_for_word(
                    self.states,
                    self.observation,
                    self.generators,
                    self.costs,
                    word,
                    target_budget,
                )
                self.assertTrue(mapping)

    def test_operation_word_costs_add_and_quotient_maps_compose(self):
        cases = (
            (("g",), ("h",)),
            (("h",), ("g",)),
            (("g", "g"), ("h",)),
            (("g",), ("h", "g")),
        )
        for first, second in cases:
            self.assertEqual(
                word_cost(first + second, self.costs),
                word_cost(first, self.costs) + word_cost(second, self.costs),
            )
            for budget in range(5):
                self.assertTrue(
                    word_layer_composition_is_exact(
                        self.states,
                        self.observation,
                        self.generators,
                        self.costs,
                        first,
                        second,
                        budget,
                    )
                )

    def test_agreement_depth_can_drop_by_at_most_operation_cost(self):
        words = (
            (),
            ("g",),
            ("h",),
            ("g", "h"),
            ("h", "g"),
            ("g", "g", "h"),
        )
        self.assertTrue(
            all_depth_loss_bounds_hold(
                self.states,
                self.observation,
                self.generators,
                self.costs,
                words,
            )
        )

    def test_permanently_equivalent_states_remain_permanently_equivalent_after_operations(self):
        states = (0, 1, 2)
        observation = {0: 0, 1: 0, 2: 1}
        generators = {
            "id": {0: 0, 1: 1, 2: 2},
            "reset": {0: 0, 1: 0, 2: 0},
        }
        costs = {"id": 3, "reset": 2}
        words = ((), ("id",), ("reset",), ("id", "reset"))
        self.assertTrue(
            all_depth_loss_bounds_hold(
                states,
                observation,
                generators,
                costs,
                words,
            )
        )

    def test_zero_cost_words_are_excluded_by_positive_primitive_cost_discipline(self):
        # The empty word is the only cost-zero word; every primitive generator has
        # strictly positive cost, so future-budget levels cannot be traversed by a
        # hidden zero-cost cycle.
        self.assertEqual(word_cost((), self.costs), 0)
        self.assertGreater(word_cost(("g",), self.costs), 0)
        self.assertGreater(word_cost(("h",), self.costs), 0)


if __name__ == "__main__":
    unittest.main()
