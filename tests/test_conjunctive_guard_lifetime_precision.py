import itertools
import unittest

from enterprise_math.conjunctive_guard_lifetime_precision import (
    capped_conjunctive_guard_lifetime,
    conjunctive_definedness_signature,
    conjunctive_guard_lifetime,
    conjunctive_guard_lifetimes,
    lifetime_class_count_upper_bound,
    repeated_action_defined_closed_form,
    repeated_action_defined_direct,
    single_guard_lifetime,
)
from enterprise_math.lattice_guard_precision import IntegerGuard


class ConjunctiveGuardLifetimePrecisionTests(unittest.TestCase):
    def test_single_guard_closed_form_matches_direct_repetition(self):
        guard = IntegerGuard((2, 4), 5)
        actions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        for point in itertools.product(range(-4, 5), repeat=2):
            for action in actions:
                lifetime = single_guard_lifetime(point, guard, action)
                for repetitions in range(7):
                    expected = (
                        lifetime.legal_repetitions is None
                        or repetitions <= lifetime.legal_repetitions
                    )
                    self.assertEqual(
                        repeated_action_defined_direct(
                            point, (guard,), action, repetitions
                        ),
                        expected,
                    )

    def test_positive_zero_negative_projected_shift_trichotomy(self):
        guard = IntegerGuard((1, 0), 0)
        point = (-3, 7)
        positive = single_guard_lifetime(point, guard, (1, 5))
        zero = single_guard_lifetime(point, guard, (0, 9))
        negative = single_guard_lifetime(point, guard, (-2, 4))
        self.assertEqual(positive.action_shift, 1)
        self.assertEqual(positive.legal_repetitions, 3)
        self.assertEqual(zero.action_shift, 0)
        self.assertIsNone(zero.legal_repetitions)
        self.assertLess(negative.action_shift, 0)
        self.assertIsNone(negative.legal_repetitions)

        disabled = single_guard_lifetime((0, 7), guard, (-2, 4))
        self.assertEqual(disabled.legal_repetitions, 0)

    def test_conjunctive_lifetime_is_minimum_of_guard_lifetimes(self):
        guards = (
            IntegerGuard((1, 0), 0),
            IntegerGuard((0, 1), 0),
            IntegerGuard((1, 1), 1),
        )
        action = (1, 0)
        for point in itertools.product(range(-5, 2), repeat=2):
            individual = conjunctive_guard_lifetimes(
                point, guards, action
            )
            finite = [
                item.legal_repetitions
                for item in individual
                if item.legal_repetitions is not None
            ]
            expected = None if not finite else min(finite)
            self.assertEqual(
                conjunctive_guard_lifetime(point, guards, action),
                expected,
            )

    def test_closed_form_matches_direct_conjunctive_words_exhaustively(self):
        guard_families = (
            (
                IntegerGuard((1, 0), 0),
                IntegerGuard((0, 1), 0),
            ),
            (
                IntegerGuard((2, 0), 1),
                IntegerGuard((0, 3), 2),
                IntegerGuard((1, 1), 1),
            ),
        )
        actions = ((1, 0), (0, 1), (-1, 1), (1, -2))
        checked = 0
        for guards in guard_families:
            for point in itertools.product(range(-4, 3), repeat=2):
                for action in actions:
                    for repetitions in range(6):
                        self.assertEqual(
                            repeated_action_defined_direct(
                                point,
                                guards,
                                action,
                                repetitions,
                            ),
                            repeated_action_defined_closed_form(
                                point,
                                guards,
                                action,
                                repetitions,
                            ),
                        )
                        checked += 1
        self.assertGreater(checked, 2000)

    def test_capped_lifetime_is_complete_definedness_future_signature(self):
        guards = (
            IntegerGuard((1, 0), 0),
            IntegerGuard((0, 1), 0),
        )
        action = (1, 0)
        for horizon in range(6):
            by_lifetime = {}
            by_signature = {}
            for point in itertools.product(range(-6, 3), repeat=2):
                capped = capped_conjunctive_guard_lifetime(
                    point, guards, action, horizon
                )
                signature = tuple(
                    repeated_action_defined_direct(
                        point, guards, action, repetitions
                    )
                    for repetitions in range(horizon + 1)
                )
                by_lifetime[point] = capped
                by_signature[point] = signature
                self.assertEqual(
                    signature,
                    conjunctive_definedness_signature(
                        point, guards, action, horizon
                    ),
                )
            for left in by_lifetime:
                for right in by_lifetime:
                    self.assertEqual(
                        by_lifetime[left] == by_lifetime[right],
                        by_signature[left] == by_signature[right],
                    )

    def test_two_orthogonal_guards_realize_exact_h_plus_one_classes(self):
        guards = (
            IntegerGuard((1, 0), 0),
            IntegerGuard((0, 1), 0),
        )
        action = (1, 0)
        for horizon in range(7):
            representatives = [(0, -1)]  # lifetime 0: already disabled
            representatives.extend(
                [(-lifetime, -1) for lifetime in range(1, horizon)]
            )
            representatives.append((-(horizon + 2), -1))  # capped lifetime h
            classes = {
                capped_conjunctive_guard_lifetime(
                    point, guards, action, horizon
                )
                for point in representatives
            }
            self.assertEqual(
                len(classes),
                lifetime_class_count_upper_bound(horizon),
            )

    def test_full_current_guard_bit_vector_can_overrefine_same_future_class(self):
        guards = (
            IntegerGuard((1, 0), 0),
            IntegerGuard((0, 1), 0),
        )
        action = (1, 0)
        # Both states cannot execute even one action, but for different guard
        # reasons.  A language observing only action definedness must merge them.
        left = (0, -1)
        right = (-1, 0)
        left_bits = tuple(not guard.evaluate(left) for guard in guards)
        right_bits = tuple(not guard.evaluate(right) for guard in guards)
        self.assertNotEqual(left_bits, right_bits)
        for horizon in range(1, 6):
            self.assertEqual(
                capped_conjunctive_guard_lifetime(
                    left, guards, action, horizon
                ),
                capped_conjunctive_guard_lifetime(
                    right, guards, action, horizon
                ),
            )
            self.assertEqual(
                conjunctive_definedness_signature(
                    left, guards, action, horizon
                ),
                conjunctive_definedness_signature(
                    right, guards, action, horizon
                ),
            )

    def test_invariant_guard_needs_only_current_pass_fail_bit(self):
        guards = (
            IntegerGuard((1, 0), 0),
            IntegerGuard((0, 1), 0),
        )
        action = (1, 0)
        first = conjunctive_guard_lifetimes((-3, -1), guards, action)
        second = conjunctive_guard_lifetimes((-3, -100), guards, action)
        self.assertEqual(first[0].legal_repetitions, 3)
        self.assertEqual(second[0].legal_repetitions, 3)
        self.assertIsNone(first[1].legal_repetitions)
        self.assertIsNone(second[1].legal_repetitions)
        self.assertEqual(
            conjunctive_guard_lifetime((-3, -1), guards, action),
            conjunctive_guard_lifetime((-3, -100), guards, action),
        )

    def test_validation(self):
        with self.assertRaises(ValueError):
            conjunctive_guard_lifetime((0,), (), (1,))
        with self.assertRaises(ValueError):
            conjunctive_guard_lifetime(
                (0,), (IntegerGuard((0,), 1),), (1,)
            )
        with self.assertRaises(ValueError):
            conjunctive_guard_lifetime(
                (0, 0),
                (IntegerGuard((1, 0), 1), IntegerGuard((1,), 1)),
                (1, 0),
            )
        with self.assertRaises(ValueError):
            conjunctive_guard_lifetime(
                (0,), (IntegerGuard((1,), 1),), (1, 0)
            )
        with self.assertRaises(ValueError):
            capped_conjunctive_guard_lifetime(
                (0,), (IntegerGuard((1,), 1),), (1,), -1
            )
        with self.assertRaises(TypeError):
            repeated_action_defined_direct(
                (0,), (IntegerGuard((1,), 1),), (1,), True
            )


if __name__ == "__main__":
    unittest.main()
