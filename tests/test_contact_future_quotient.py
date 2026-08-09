import unittest
from itertools import product

from enterprise_math.contact_future_quotient import (
    contact_exit_signature,
    contact_future_quotient,
    future_class_for_detail,
    reachable_subfactor_sums,
)


def brute_word_sums(increments, max_length):
    sums = {0}
    for length in range(1, max_length + 1):
        for word in product(increments, repeat=length):
            sums.add(sum(word))
    return sums


class ContactFutureQuotientTests(unittest.TestCase):
    def test_unit_increment_requires_full_detail(self):
        for factor in range(1, 9):
            quotient = contact_future_quotient(factor, (1,))
            self.assertEqual(
                quotient.classes,
                tuple((detail,) for detail in range(factor)),
            )

    def test_increment_two_merges_adjacent_details_by_reachable_boundary(self):
        quotient = contact_future_quotient(6, (2,))
        self.assertEqual(quotient.reachable_subfactor_sums, (0, 2, 4))
        self.assertEqual(quotient.classes, ((0, 1), (2, 3), (4, 5)))

    def test_increment_two_three_has_missing_unit_boundary_only(self):
        quotient = contact_future_quotient(6, (2, 3))
        self.assertEqual(quotient.reachable_subfactor_sums, (0, 2, 3, 4, 5))
        self.assertEqual(quotient.classes, ((0, 1), (2,), (3,), (4,), (5,)))

    def test_zero_or_full_factor_actions_do_not_refine_contact_detail(self):
        for factor in range(1, 8):
            quotient = contact_future_quotient(factor, (0, factor, factor + 3))
            self.assertEqual(quotient.reachable_subfactor_sums, (0,))
            self.assertEqual(quotient.classes, (tuple(range(factor)),))

    def test_signatures_are_constant_exactly_on_reported_classes(self):
        for factor in range(2, 8):
            for increments in ((1,), (2,), (3,), (2, 3), (0, 2, 4)):
                quotient = contact_future_quotient(factor, increments)
                signatures = {
                    detail: contact_exit_signature(detail, factor, increments)
                    for detail in range(factor)
                }
                for left in range(factor):
                    for right in range(factor):
                        same_class = future_class_for_detail(
                            quotient, left
                        ) == future_class_for_detail(quotient, right)
                        self.assertEqual(
                            same_class,
                            signatures[left] == signatures[right],
                            (factor, increments, left, right, quotient),
                        )

    def test_reachable_sum_solver_matches_bounded_word_enumeration(self):
        for factor in range(2, 8):
            for increments in ((1,), (2,), (3,), (2, 3), (0, 2, 4)):
                exact = set(reachable_subfactor_sums(factor, increments))
                positive = [value for value in increments if value > 0]
                if positive:
                    max_length = factor // min(positive) + 1
                    brute = {
                        total
                        for total in brute_word_sums(tuple(increments), max_length)
                        if 0 <= total < factor
                    }
                else:
                    brute = {0}
                self.assertEqual(exact, brute, (factor, increments))

    def test_reported_partition_is_minimal_for_reachable_exit_language(self):
        for factor in range(2, 8):
            for increments in ((2,), (3,), (2, 3)):
                quotient = contact_future_quotient(factor, increments)
                sums = quotient.reachable_subfactor_sums
                for left_class, right_class in zip(
                    quotient.classes, quotient.classes[1:]
                ):
                    left = left_class[-1]
                    right = right_class[0]
                    self.assertTrue(
                        any(
                            (left + cumulative >= factor)
                            != (right + cumulative >= factor)
                            for cumulative in sums
                        ),
                        (factor, increments, left_class, right_class),
                    )

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            contact_future_quotient(0, (1,))
        with self.assertRaises(ValueError):
            contact_future_quotient(3, (-1,))
        quotient = contact_future_quotient(3, (1,))
        with self.assertRaises(ValueError):
            future_class_for_detail(quotient, 3)


if __name__ == "__main__":
    unittest.main()
