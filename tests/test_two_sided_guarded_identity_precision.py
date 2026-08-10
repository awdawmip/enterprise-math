import unittest

from enterprise_math.guarded_translation_precision import (
    apply_guarded_translation_word,
    guarded_translation_profiles,
    guarded_word_profile,
)
from enterprise_math.two_sided_guarded_identity_precision import (
    shortest_balanced_pair_cost,
    unit_signed_general_compiler_matches_closed_form,
    unit_signed_infinite_future_equivalent,
    unit_signed_legality_class_count,
    unit_signed_legality_cuts,
    zero_translation_block_witness,
    zero_translation_profile_lower_bound,
    zero_translation_witness_guard_cut,
)


class TwoSidedGuardedIdentityPrecisionTests(unittest.TestCase):
    def test_balanced_block_witness_has_zero_total_and_exact_peak(self):
        cases = (
            (1, -1),
            (2, -3),
            (4, -6),
            (5, -2),
        )
        for positive, negative in cases:
            for multiplier in range(1, 5):
                witness = zero_translation_block_witness(
                    positive, negative, multiplier
                )
                word = (
                    (positive,) * witness.positive_count
                    + (negative,) * witness.negative_count
                )
                self.assertEqual(sum(word), 0)
                self.assertEqual(
                    guarded_word_profile(word),
                    witness.profile,
                )
                self.assertEqual(
                    witness.guard_peak,
                    multiplier * witness.balance_lcm,
                )

    def test_same_net_identity_words_have_strictly_nested_guard_domains(self):
        guard = 7
        first = zero_translation_block_witness(2, -3, 1)
        second = zero_translation_block_witness(2, -3, 2)
        self.assertEqual(first.profile.total_translation, 0)
        self.assertEqual(second.profile.total_translation, 0)
        self.assertLess(
            zero_translation_witness_guard_cut(second, guard),
            zero_translation_witness_guard_cut(first, guard),
        )

        boundary = zero_translation_witness_guard_cut(second, guard)
        first_word = (
            (first.positive_action,) * first.positive_count
            + (first.negative_action,) * first.negative_count
        )
        second_word = (
            (second.positive_action,) * second.positive_count
            + (second.negative_action,) * second.negative_count
        )
        self.assertTrue(
            apply_guarded_translation_word(
                boundary, first_word, guard
            ).defined
        )
        self.assertFalse(
            apply_guarded_translation_word(
                boundary, second_word, guard
            ).defined
        )

    def test_zero_translation_profile_lower_bound_is_realized(self):
        action_sets = (
            (-1, 1),
            (-2, 3),
            (-3, 2, 5),
            (-6, -4, 3, 5),
        )
        for actions in action_sets:
            cycle_length, positive, negative = shortest_balanced_pair_cost(actions)
            for horizon in range(0, 13):
                lower = zero_translation_profile_lower_bound(
                    actions, horizon
                )
                profiles = {
                    profile
                    for profile in guarded_translation_profiles(
                        actions, horizon
                    )
                    if profile.total_translation == 0
                }
                self.assertGreaterEqual(len(profiles), lower)
                self.assertEqual(lower, 1 + horizon // cycle_length)
                for multiplier in range(1, horizon // cycle_length + 1):
                    witness = zero_translation_block_witness(
                        positive, negative, multiplier
                    )
                    self.assertLessEqual(witness.word_length, horizon)
                    self.assertIn(witness.profile, profiles)

    def test_unit_signed_legality_cut_formula_is_exact(self):
        for guard in (-3, 0, 4):
            for horizon in range(8):
                self.assertTrue(
                    unit_signed_general_compiler_matches_closed_form(
                        guard, horizon
                    )
                )
                if horizon == 0:
                    self.assertEqual(
                        unit_signed_legality_cuts(guard, horizon),
                        (),
                    )
                else:
                    self.assertEqual(
                        unit_signed_legality_cuts(guard, horizon),
                        tuple(range(guard - horizon + 1, guard + 1)),
                    )

    def test_unit_signed_future_class_count_is_h_plus_one(self):
        # With h consecutive integer cuts there are exactly h+1 interval classes
        # on Z.  Sample one representative from each cell and verify that the
        # direct legality signatures are all distinct.
        guard = 2
        for horizon in range(8):
            self.assertEqual(
                unit_signed_legality_class_count(horizon),
                horizon + 1,
            )
            if horizon == 0:
                representatives = (0,)
            else:
                bottom = guard - horizon
                representatives = (
                    bottom,
                    *range(bottom + 1, guard),
                    guard,
                )
            signatures = []
            words = [()]
            for length in range(1, horizon + 1):
                # It is enough to query every literal +/-1 word at this small
                # horizon; the closed-form theorem is tested independently.
                import itertools

                words.extend(itertools.product((-1, 1), repeat=length))
            for state in representatives:
                signatures.append(
                    tuple(
                        apply_guarded_translation_word(
                            state, word, guard
                        ).defined
                        for word in words
                    )
                )
            self.assertEqual(len(set(signatures)), horizon + 1)

    def test_infinite_unit_signed_language_recovers_exact_state_below_guard(self):
        guard = 0
        for left in range(-8, 4):
            for right in range(-8, 4):
                expected = (
                    (left >= guard and right >= guard)
                    or left == right
                )
                self.assertEqual(
                    unit_signed_infinite_future_equivalent(
                        left, right, guard
                    ),
                    expected,
                )

    def test_algebraic_identity_class_splits_without_terminal_observation(self):
        guard = 0
        profiles = [
            zero_translation_block_witness(1, -1, multiplier)
            for multiplier in range(1, 6)
        ]
        self.assertEqual(
            {witness.profile.total_translation for witness in profiles},
            {0},
        )
        self.assertEqual(
            {witness.guard_peak for witness in profiles},
            {1, 2, 3, 4, 5},
        )
        for witness in profiles:
            cut = zero_translation_witness_guard_cut(witness, guard)
            self.assertEqual(cut, -witness.multiplier)

    def test_validation(self):
        with self.assertRaises(ValueError):
            zero_translation_block_witness(0, -1)
        with self.assertRaises(ValueError):
            zero_translation_block_witness(1, 0)
        with self.assertRaises(ValueError):
            zero_translation_block_witness(1, -1, 0)
        with self.assertRaises(ValueError):
            zero_translation_profile_lower_bound((1, 2), 4)
        with self.assertRaises(ValueError):
            zero_translation_profile_lower_bound((-1, -2), 4)
        with self.assertRaises(ValueError):
            zero_translation_profile_lower_bound((-1, 1), -1)
        with self.assertRaises(TypeError):
            unit_signed_legality_cuts(False, 2)


if __name__ == "__main__":
    unittest.main()
