import unittest

from enterprise_math.causal_count_measure import (
    ExactCountRatio,
    compose_mapping,
    conditional_count_ratio,
    event_count,
    event_count_ratio,
    fiber_multiplicities,
    pushforward_multiplicities,
)


class CausalCountMeasureTests(unittest.TestCase):
    def test_singleton_weights_are_exact_fiber_multiplicities(self):
        mapping = {0: "a", 1: "a", 2: "b", 3: "c", 4: "c"}
        self.assertEqual(
            fiber_multiplicities(mapping),
            {"a": 2, "b": 1, "c": 2},
        )
        self.assertEqual(event_count(mapping, frozenset({"a", "c"})), 4)

    def test_postcomposition_is_integer_pushforward_by_addition(self):
        first = {0: "a", 1: "a", 2: "b", 3: "c", 4: "c"}
        second = {"a": "u", "b": "v", "c": "u"}
        fine_counts = fiber_multiplicities(first)
        pushed = pushforward_multiplicities(fine_counts, second)
        composed = compose_mapping(first, second)
        self.assertEqual(pushed, {"u": 4, "v": 1})
        self.assertEqual(pushed, fiber_multiplicities(composed))
        self.assertEqual(sum(pushed.values()), len(first))

    def test_event_ratio_stays_exact_without_float_or_true_division(self):
        mapping = {0: "a", 1: "a", 2: "b", 3: "c", 4: "c"}
        ratio = event_count_ratio(mapping, frozenset({"a"}))
        self.assertEqual(ratio, ExactCountRatio(2, 5))
        self.assertEqual(ratio.reduced(), ExactCountRatio(2, 5))

    def test_fraction_comparison_uses_cross_products(self):
        two_fifths = ExactCountRatio(2, 5)
        one_half = ExactCountRatio(1, 2)
        four_tenths = ExactCountRatio(4, 10)
        self.assertEqual(two_fifths.compare(one_half), -1)
        self.assertEqual(one_half.compare(two_fifths), 1)
        self.assertEqual(two_fifths.compare(four_tenths), 0)
        self.assertEqual(four_tenths.reduced(), ExactCountRatio(2, 5))

    def test_conditional_count_pair_is_exact_integer_object(self):
        fine = frozenset(range(8))
        even = frozenset({0, 2, 4, 6})
        low = frozenset({0, 1, 2, 3, 4})
        ratio = conditional_count_ratio(fine, even, low)
        self.assertEqual(ratio, ExactCountRatio(3, 5))

    def test_counting_object_does_not_require_probability_interpretation(self):
        # The same exact pair can be compared and reduced without assigning any
        # stochastic semantics to the fine-state set.
        left = ExactCountRatio(6, 10).reduced()
        right = ExactCountRatio(3, 5)
        self.assertEqual(left, right)
        self.assertEqual(left.compare(right), 0)


if __name__ == "__main__":
    unittest.main()
