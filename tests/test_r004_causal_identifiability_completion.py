from fractions import Fraction
from itertools import product
import unittest

from enterprise_math.r004_causal_identifiability_completion import (
    compile_rational_master_measure,
    compile_support_masters,
    direct_policy_history_law,
    master_measure_policy_history_law,
    master_measure_word_law,
    masters_word_support,
    rational_word_law,
    raw_relation_word_support,
    support_completion_holds,
)


class CounterfactualSupportCompletionTests(unittest.TestCase):
    def test_exhaustive_two_state_relation_pairs_through_horizon_two(self) -> None:
        states = (0, 1)
        edges = ((0, 0), (0, 1), (1, 0), (1, 1))
        relations = [
            frozenset(edge for index, edge in enumerate(edges) if mask & (1 << index))
            for mask in range(16)
        ]

        checked = 0
        for left in relations:
            for right in relations:
                family = {"a": left, "b": right}
                for source in states:
                    self.assertTrue(support_completion_holds(states, family, source, 2))
                    checked += 1

        self.assertEqual(checked, 512)

    def test_disabled_words_remain_absent_from_master_support(self) -> None:
        states = (0, 1, 2)
        relations = {
            "a": frozenset({(0, 1)}),
            "b": frozenset({(1, 2)}),
        }
        masters = compile_support_masters(states, relations, 0, 2)

        self.assertEqual(masters_word_support(masters, ("a", "b")), frozenset({2}))
        self.assertEqual(masters_word_support(masters, ("b",)), frozenset())
        self.assertEqual(
            masters_word_support(masters, ("b",)),
            raw_relation_word_support(states, relations, 0, ("b",)),
        )

    def test_hidden_branching_is_absorbed_into_counterfactual_masters(self) -> None:
        states = (0, 1, 2, 3, 4)
        relations = {
            "split": frozenset({(0, 1), (0, 2)}),
            "read": frozenset({(1, 3), (2, 4)}),
        }
        masters = compile_support_masters(states, relations, 0, 2)

        self.assertEqual(
            masters_word_support(masters, ("split", "read")),
            frozenset({3, 4}),
        )
        self.assertEqual(
            masters_word_support(masters, ("split", "read")),
            raw_relation_word_support(states, relations, 0, ("split", "read")),
        )


class CounterfactualRationalCompletionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.states = (0, 1)
        self.kernels = {
            "a": {
                0: {0: Fraction(1, 3), 1: Fraction(2, 3)},
                1: {0: Fraction(1, 2), 1: Fraction(1, 2)},
            },
            "b": {
                0: {0: Fraction(3, 4), 1: Fraction(1, 4)},
                1: {0: Fraction(1, 5), 1: Fraction(4, 5)},
            },
        }

    def test_one_master_measure_reproduces_every_word_through_horizon_three(self) -> None:
        measure = compile_rational_master_measure(self.states, self.kernels, 0, 3)
        self.assertEqual(sum(measure.values(), Fraction(0)), Fraction(1))

        for depth in range(4):
            for word in product(("a", "b"), repeat=depth):
                self.assertEqual(
                    master_measure_word_law(measure, word),
                    rational_word_law(self.states, self.kernels, 0, word),
                )

    def test_same_ex_ante_measure_reproduces_adaptive_policy_history_law(self) -> None:
        measure = compile_rational_master_measure(self.states, self.kernels, 0, 3)

        def policy(history: tuple[int, ...]) -> str:
            return "a" if sum(history) % 2 == 0 else "b"

        direct = direct_policy_history_law(
            self.states,
            self.kernels,
            0,
            3,
            policy,
        )
        presampled = master_measure_policy_history_law(measure, 3, policy)

        self.assertEqual(presampled, direct)
        self.assertEqual(sum(presampled.values(), Fraction(0)), Fraction(1))

    def test_exact_fraction_arithmetic_is_retained(self) -> None:
        measure = compile_rational_master_measure(self.states, self.kernels, 0, 2)
        law = master_measure_word_law(measure, ("a", "b"))

        self.assertTrue(all(isinstance(weight, Fraction) for weight in measure.values()))
        self.assertEqual(law, rational_word_law(self.states, self.kernels, 0, ("a", "b")))
        self.assertEqual(sum(law.values(), Fraction(0)), Fraction(1))

    def test_invalid_kernel_rows_are_rejected(self) -> None:
        bad_sum = {
            "a": {
                0: {0: Fraction(1, 3), 1: Fraction(1, 3)},
                1: {1: Fraction(1)},
            }
        }
        with self.assertRaisesRegex(ValueError, "sum exactly to one"):
            compile_rational_master_measure(self.states, bad_sum, 0, 1)

        missing_source = {
            "a": {
                0: {0: Fraction(1)},
            }
        }
        with self.assertRaisesRegex(ValueError, "missing a declared source"):
            compile_rational_master_measure(self.states, missing_source, 0, 1)


if __name__ == "__main__":
    unittest.main()
