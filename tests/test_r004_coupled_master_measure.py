import itertools
import unittest
from fractions import Fraction

from enterprise_math.r004_causal_identifiability_completion import (
    compile_rational_master_measure,
    direct_policy_history_law,
    master_measure_policy_history_law,
    master_measure_word_law,
    rational_word_law,
)
from enterprise_math.r004_coupled_master_measure import (
    compile_coupled_rational_master_measure,
    independent_redundant_uniform_support_exponent,
    master_support_compression_ratio,
    redundant_uniform_master_support_counts,
)


class R004CoupledMasterMeasureTests(unittest.TestCase):
    def setUp(self):
        self.states = (0, 1)
        self.kernels = {
            "a": {
                0: {0: Fraction(1, 3), 1: Fraction(2, 3)},
                1: {0: Fraction(1, 4), 1: Fraction(3, 4)},
            },
            "b": {
                0: {0: Fraction(2, 5), 1: Fraction(3, 5)},
                1: {0: Fraction(3, 7), 1: Fraction(4, 7)},
            },
        }

    def test_coupled_compiler_reproduces_every_literal_word_law(self):
        horizon = 3
        measure = compile_coupled_rational_master_measure(
            self.states, self.kernels, 0, horizon
        )
        self.assertEqual(sum(measure.values(), Fraction(0)), Fraction(1))
        for depth in range(horizon + 1):
            for word in itertools.product(("a", "b"), repeat=depth):
                self.assertEqual(
                    master_measure_word_law(measure, word),
                    rational_word_law(self.states, self.kernels, 0, word),
                )

    def test_coupled_compiler_reproduces_adaptive_policy_history_law(self):
        horizon = 3
        measure = compile_coupled_rational_master_measure(
            self.states, self.kernels, 0, horizon
        )

        def policy(history):
            return "a" if (len(history) + sum(history)) % 2 == 0 else "b"

        self.assertEqual(
            master_measure_policy_history_law(measure, horizon, policy),
            direct_policy_history_law(
                self.states, self.kernels, 0, horizon, policy
            ),
        )

    def test_identical_counterfactual_actions_have_exact_closed_form_compression(self):
        fair = {
            0: {0: Fraction(1, 2), 1: Fraction(1, 2)},
            1: {0: Fraction(1, 2), 1: Fraction(1, 2)},
        }
        kernels = {"a": fair, "b": fair, "c": fair}
        horizon = 2
        independent = compile_rational_master_measure(
            self.states, kernels, 0, horizon
        )
        coupled = compile_coupled_rational_master_measure(
            self.states, kernels, 0, horizon
        )
        compressed, original = master_support_compression_ratio(
            independent, coupled
        )
        expected_coupled, expected_independent = redundant_uniform_master_support_counts(
            2, 3, horizon
        )
        self.assertEqual(independent_redundant_uniform_support_exponent(3, 2), 12)
        self.assertEqual((expected_coupled, expected_independent), (4, 4096))
        self.assertEqual((compressed, original), (4, 4096))
        self.assertEqual(sum(coupled.values(), Fraction(0)), Fraction(1))
        for depth in range(horizon + 1):
            for word in itertools.product(("a", "b", "c"), repeat=depth):
                expected = rational_word_law(self.states, kernels, 0, word)
                self.assertEqual(master_measure_word_law(independent, word), expected)
                self.assertEqual(master_measure_word_law(coupled, word), expected)

    def test_closed_form_construction_overhead_grows_with_redundant_action_labels(self):
        self.assertEqual(redundant_uniform_master_support_counts(2, 1, 4), (16, 16))
        self.assertEqual(redundant_uniform_master_support_counts(2, 2, 3), (8, 2**14))
        self.assertEqual(redundant_uniform_master_support_counts(3, 3, 2), (9, 3**12))
        self.assertEqual(independent_redundant_uniform_support_exponent(2, 3), 14)
        self.assertEqual(independent_redundant_uniform_support_exponent(3, 2), 12)

    def test_one_action_has_no_counterfactual_cross_action_product_to_remove(self):
        kernels = {"a": self.kernels["a"]}
        independent = compile_rational_master_measure(self.states, kernels, 0, 3)
        coupled = compile_coupled_rational_master_measure(self.states, kernels, 0, 3)
        self.assertEqual(len(coupled), len(independent))
        for depth in range(4):
            word = ("a",) * depth
            self.assertEqual(
                master_measure_word_law(coupled, word),
                rational_word_law(self.states, kernels, 0, word),
            )

    def test_invalid_inputs_fail_closed(self):
        with self.assertRaises(ValueError):
            compile_coupled_rational_master_measure((), self.kernels, 0, 1)
        with self.assertRaises(ValueError):
            compile_coupled_rational_master_measure(self.states, self.kernels, 2, 1)
        with self.assertRaises(ValueError):
            compile_coupled_rational_master_measure(self.states, self.kernels, 0, -1)
        bad_float = {
            "a": {
                0: {0: 0.5, 1: 0.5},
                1: {0: Fraction(1), 1: Fraction(0)},
            }
        }
        with self.assertRaisesRegex(ValueError, "int or Fraction"):
            compile_coupled_rational_master_measure(self.states, bad_float, 0, 1)
        with self.assertRaises(ValueError):
            master_support_compression_ratio({}, {"x": Fraction(1)})
        with self.assertRaises(ValueError):
            redundant_uniform_master_support_counts(0, 2, 1)
        with self.assertRaises(ValueError):
            redundant_uniform_master_support_counts(2, 0, 1)
        with self.assertRaises(ValueError):
            independent_redundant_uniform_support_exponent(2, -1)


if __name__ == "__main__":
    unittest.main()
