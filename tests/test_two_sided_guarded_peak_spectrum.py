import itertools
import unittest

from enterprise_math.guarded_translation_precision import (
    apply_guarded_translation_word,
)
from enterprise_math.two_sided_guarded_identity_precision import (
    unit_signed_infinite_future_equivalent,
    unit_signed_legality_class_count,
    unit_signed_legality_cuts,
)
from enterprise_math.two_sided_guarded_peak_spectrum import (
    two_sided_guard_only_class_count,
    two_sided_guard_only_compiler_matches_closed_form,
    two_sided_guard_only_cuts,
    two_sided_guard_only_infinite_coordinate,
    two_sided_guard_only_infinite_equivalent,
    two_sided_guard_peak_values,
)


def literal_words(actions, horizon):
    result = [()]
    for length in range(1, horizon + 1):
        result.extend(itertools.product(actions, repeat=length))
    return tuple(result)


def literal_peak(word):
    if not word:
        raise ValueError("peak is defined here only for nonempty words")
    total = 0
    peak = 0
    for action in word:
        peak = max(peak, total)
        total += action
    return peak


def literal_peak_values(actions, horizon):
    return tuple(
        sorted(
            {
                literal_peak(word)
                for word in literal_words(actions, horizon)
                if word
            }
        )
    )


def definedness_signature(value, actions, guard, horizon):
    return tuple(
        apply_guarded_translation_word(value, word, guard).defined
        for word in literal_words(actions, horizon)
    )


class TwoSidedGuardedPeakSpectrumTests(unittest.TestCase):
    def test_peak_values_equal_nonnegative_h_minus_one_reachability(self):
        action_sets = (
            (-1, 1),
            (-2, 3),
            (-4, 6),
            (-5, -2, 3, 7),
            (-2, 0, 3),
        )
        for actions in action_sets:
            for horizon in range(0, 6):
                self.assertEqual(
                    two_sided_guard_peak_values(actions, horizon),
                    literal_peak_values(actions, horizon),
                )

    def test_guard_only_cut_formula_matches_general_compiler(self):
        action_sets = (
            (-1, 1),
            (-2, 3),
            (-4, 6),
            (-5, -2, 3, 7),
            (-2, 0, 3),
        )
        for guard in (-3, 0, 5):
            for actions in action_sets:
                for horizon in range(0, 6):
                    self.assertTrue(
                        two_sided_guard_only_compiler_matches_closed_form(
                            guard,
                            actions,
                            horizon,
                        )
                    )
                    self.assertEqual(
                        two_sided_guard_only_cuts(
                            guard,
                            actions,
                            horizon,
                        ),
                        tuple(
                            sorted(
                                guard - peak
                                for peak in literal_peak_values(
                                    actions, horizon
                                )
                            )
                        ),
                    )

    def test_class_count_matches_direct_definedness_signatures(self):
        guard = 1
        action_sets = (
            (-1, 1),
            (-2, 3),
            (-4, 6),
            (-2, 0, 3),
        )
        for actions in action_sets:
            for horizon in range(0, 5):
                cuts = two_sided_guard_only_cuts(
                    guard,
                    actions,
                    horizon,
                )
                expected = two_sided_guard_only_class_count(
                    actions,
                    horizon,
                )
                self.assertEqual(expected, len(cuts) + 1)
                if not cuts:
                    representatives = (guard,)
                else:
                    representatives = (cuts[0] - 1, *cuts)
                signatures = {
                    definedness_signature(
                        state,
                        actions,
                        guard,
                        horizon,
                    )
                    for state in representatives
                }
                self.assertEqual(len(signatures), expected)

    def test_infinite_coordinate_is_gcd_cell_below_guard(self):
        actions = (-4, 6)
        guard = 0
        expected = {
            -1: 1,
            -2: 1,
            -3: 2,
            -4: 2,
            -5: 3,
            -6: 3,
            0: 0,
            7: 0,
        }
        for value, coordinate in expected.items():
            self.assertEqual(
                two_sided_guard_only_infinite_coordinate(
                    value,
                    guard,
                    actions,
                ),
                coordinate,
            )

        self.assertTrue(
            two_sided_guard_only_infinite_equivalent(
                -1, -2, guard, actions
            )
        )
        self.assertFalse(
            two_sided_guard_only_infinite_equivalent(
                -2, -3, guard, actions
            )
        )
        self.assertTrue(
            two_sided_guard_only_infinite_equivalent(
                0, 100, guard, actions
            )
        )
        self.assertFalse(
            two_sided_guard_only_infinite_equivalent(
                -1, 0, guard, actions
            )
        )

    def test_unit_signed_model_is_exact_specialization(self):
        actions = (-1, 1)
        for guard in (-2, 0, 4):
            for horizon in range(0, 8):
                self.assertEqual(
                    two_sided_guard_only_cuts(
                        guard, actions, horizon
                    ),
                    unit_signed_legality_cuts(guard, horizon),
                )
                self.assertEqual(
                    two_sided_guard_only_class_count(
                        actions, horizon
                    ),
                    unit_signed_legality_class_count(horizon),
                )

            for left in range(guard - 8, guard + 4):
                for right in range(guard - 8, guard + 4):
                    self.assertEqual(
                        two_sided_guard_only_infinite_equivalent(
                            left,
                            right,
                            guard,
                            actions,
                        ),
                        unit_signed_infinite_future_equivalent(
                            left,
                            right,
                            guard,
                        ),
                    )

    def test_gcd_grain_reappears_after_word_profile_aggregation(self):
        # The word normal form still needs prefix peak.  But after *all* guarded
        # words are aggregated into a state future language, the infinite tail
        # is the uniform gcd grid.  Two different alphabets with gcd two induce
        # the same infinite guard-only coordinate.
        guard = 3
        first = (-4, 6)
        second = (-6, 10)
        for value in range(-15, 8):
            self.assertEqual(
                two_sided_guard_only_infinite_coordinate(
                    value, guard, first
                ),
                two_sided_guard_only_infinite_coordinate(
                    value, guard, second
                ),
            )

    def test_validation(self):
        with self.assertRaises(ValueError):
            two_sided_guard_peak_values((1, 2), 3)
        with self.assertRaises(ValueError):
            two_sided_guard_peak_values((-1, -2), 3)
        with self.assertRaises(ValueError):
            two_sided_guard_peak_values((-1, 1), -1)
        with self.assertRaises(TypeError):
            two_sided_guard_only_cuts(False, (-1, 1), 2)
        with self.assertRaises(TypeError):
            two_sided_guard_only_infinite_coordinate(
                False, 0, (-1, 1)
            )


if __name__ == "__main__":
    unittest.main()
