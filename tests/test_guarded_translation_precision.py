import itertools
import unittest

from enterprise_math.action_language_precision import boundary_orbit_equivalent
from enterprise_math.guarded_translation_precision import (
    GuardedTranslationProfile,
    append_guarded_action,
    apply_guarded_translation_profile,
    apply_guarded_translation_word,
    compose_guarded_profiles,
    empty_guarded_translation_profile,
    guarded_boundary_equivalent,
    guarded_future_signature,
    guarded_profile_count_upper_bound,
    guarded_profile_effective_cuts,
    guarded_profile_guard_cut,
    guarded_reachable_boundary_cuts,
    guarded_translation_profiles,
    guarded_word_profile,
    positive_guarded_profile_count,
)


def literal_words(actions, horizon):
    values = tuple(sorted(set(actions)))
    result = [()]
    for length in range(1, horizon + 1):
        result.extend(itertools.product(values, repeat=length))
    return tuple(result)


def direct_literal_signature(value, actions, horizon, guard, boundaries):
    return tuple(
        (
            word,
            apply_guarded_translation_word(
                value, word, guard, boundaries
            ).defined,
            apply_guarded_translation_word(
                value, word, guard, boundaries
            ).observation,
        )
        for word in literal_words(actions, horizon)
    )


class GuardedTranslationPrecisionTests(unittest.TestCase):
    def test_word_profile_and_append_reconstruct_exact_prefix_peak(self):
        for actions in ((-2, 3), (-1, 1), (0, 2), (1, 2)):
            for horizon in range(5):
                literal = literal_words(actions, horizon)
                direct_profiles = {guarded_word_profile(word) for word in literal}
                compiled = set(guarded_translation_profiles(actions, horizon))
                self.assertEqual(compiled, direct_profiles)

                for word in literal:
                    profile = empty_guarded_translation_profile()
                    for action in word:
                        profile = append_guarded_action(profile, action)
                    self.assertEqual(profile, guarded_word_profile(word))

    def test_profile_composition_matches_literal_concatenation(self):
        words = literal_words((-2, 1, 3), 3)
        for left in words:
            for right in words:
                self.assertEqual(
                    compose_guarded_profiles(
                        guarded_word_profile(left),
                        guarded_word_profile(right),
                    ),
                    guarded_word_profile(left + right),
                )

    def test_profile_is_complete_for_guarded_threshold_word_behavior(self):
        boundaries = (-3, 0, 4)
        for word in literal_words((-2, 1, 3), 3):
            profile = guarded_word_profile(word)
            for guard in (-1, 0, 2):
                for value in range(-6, 7):
                    direct = apply_guarded_translation_word(
                        value, word, guard, boundaries
                    )
                    compiled = apply_guarded_translation_profile(
                        value, profile, guard, boundaries
                    )
                    self.assertEqual(compiled, direct)

    def test_guard_cut_is_exact_prefix_legality_threshold(self):
        word = (2, -3, 4)
        profile = guarded_word_profile(word)
        self.assertEqual(profile.total_translation, 3)
        self.assertEqual(profile.preterminal_peak, 2)
        self.assertEqual(guarded_profile_guard_cut(profile, 5), 3)
        self.assertTrue(
            apply_guarded_translation_word(2, word, 5).defined
        )
        self.assertFalse(
            apply_guarded_translation_word(3, word, 5).defined
        )

    def test_same_total_translation_can_have_different_guard_language(self):
        left = (1, 2)
        right = (2, 1)
        self.assertEqual(sum(left), sum(right))
        self.assertEqual(guarded_word_profile(left), GuardedTranslationProfile(3, 1))
        self.assertEqual(guarded_word_profile(right), GuardedTranslationProfile(3, 2))

        left_outcome = apply_guarded_translation_word(-2, left, 0, (0,))
        right_outcome = apply_guarded_translation_word(-2, right, 0, (0,))
        self.assertTrue(left_outcome.defined)
        self.assertFalse(right_outcome.defined)

    def test_effective_cut_masks_terminal_observation_after_undefined_boundary(self):
        profile = guarded_word_profile((2,))
        self.assertEqual(guarded_profile_guard_cut(profile, 0), 0)
        self.assertEqual(
            guarded_profile_effective_cuts(profile, (1, 2, 5), 0),
            (-1, 0),
        )
        # b=2 gives shifted cut 0, coincident with the guard; b=5 lies above
        # it.  Neither supplies an additional defined-state observation cut.

    def test_effective_cut_union_equals_complete_literal_future_partition(self):
        cases = (
            ((1, 2), 0, (-2, 1)),
            ((-1, 2), 1, (0, 3)),
            ((-2, 1), -1, ()),
        )
        for actions, guard, boundaries in cases:
            for horizon in range(4):
                cuts = guarded_reachable_boundary_cuts(
                    boundaries, actions, guard, horizon
                )
                values = tuple(range(-6, 7))
                signatures = {
                    value: direct_literal_signature(
                        value, actions, horizon, guard, boundaries
                    )
                    for value in values
                }
                for left in values:
                    for right in values:
                        direct_equal = signatures[left] == signatures[right]
                        low, high = sorted((left, right))
                        cut_equal = not any(low < cut <= high for cut in cuts)
                        self.assertEqual(direct_equal, cut_equal)
                        self.assertEqual(
                            guarded_boundary_equivalent(
                                left,
                                right,
                                boundaries,
                                actions,
                                guard,
                                horizon,
                            ),
                            direct_equal,
                        )

    def test_profile_signature_equals_literal_signature_equivalence(self):
        actions = (-2, 1, 3)
        boundaries = (-1, 2)
        guard = 1
        horizon = 3
        for left in range(-5, 6):
            for right in range(-5, 6):
                literal_equal = direct_literal_signature(
                    left, actions, horizon, guard, boundaries
                ) == direct_literal_signature(
                    right, actions, horizon, guard, boundaries
                )
                profile_equal = guarded_future_signature(
                    left, boundaries, actions, guard, horizon
                ) == guarded_future_signature(
                    right, boundaries, actions, guard, horizon
                )
                self.assertEqual(literal_equal, profile_equal)

    def test_far_below_guard_recovers_canonical_total_translation_partition(self):
        actions = (-1, 2)
        boundaries = (-2, 1, 4)
        horizon = 3
        guard = 10
        profiles = guarded_translation_profiles(actions, horizon)
        guard_cuts = tuple(
            cut
            for profile in profiles
            for cut in (guarded_profile_guard_cut(profile, guard),)
            if cut is not None
        )
        safe_high = min(guard_cuts) - 1
        values = tuple(range(safe_high - 8, safe_high + 1))
        for left in values:
            for right in values:
                self.assertEqual(
                    guarded_boundary_equivalent(
                        left,
                        right,
                        boundaries,
                        actions,
                        guard,
                        horizon,
                    ),
                    boundary_orbit_equivalent(
                        left,
                        right,
                        boundaries,
                        actions,
                        horizon,
                    ),
                )

    def test_profile_count_has_quadratic_horizon_bound(self):
        for actions in ((-3, 2), (-1, 1), (0,), (0, 2), (1, 4)):
            for horizon in range(7):
                self.assertLessEqual(
                    len(guarded_translation_profiles(actions, horizon)),
                    guarded_profile_count_upper_bound(actions, horizon),
                )

    def test_positive_actions_have_exact_prefix_total_profile_count(self):
        for actions in ((1,), (1, 2), (2, 3), (1, 3, 5)):
            for horizon in range(7):
                self.assertEqual(
                    len(guarded_translation_profiles(actions, horizon)),
                    positive_guarded_profile_count(actions, horizon),
                )

                for word in literal_words(actions, horizon):
                    if not word:
                        continue
                    profile = guarded_word_profile(word)
                    self.assertEqual(
                        profile.preterminal_peak,
                        profile.total_translation - word[-1],
                    )

    def test_empty_word_has_no_guard_cut_and_preserves_current_observation(self):
        empty = empty_guarded_translation_profile()
        self.assertIsNone(guarded_profile_guard_cut(empty, 0))
        self.assertEqual(
            guarded_profile_effective_cuts(empty, (-2, 3), 0),
            (-2, 3),
        )
        for value in (-10, 0, 10):
            outcome = apply_guarded_translation_profile(
                value, empty, 0, (-2, 3)
            )
            self.assertTrue(outcome.defined)
            self.assertEqual(outcome.final_value, value)

    def test_validation(self):
        with self.assertRaises(ValueError):
            guarded_translation_profiles((), 2)
        with self.assertRaises(ValueError):
            guarded_translation_profiles((1,), -1)
        with self.assertRaises(TypeError):
            guarded_translation_profiles((True,), 2)
        with self.assertRaises(ValueError):
            positive_guarded_profile_count((0, 1), 2)
        with self.assertRaises(ValueError):
            positive_guarded_profile_count((-1, 2), 2)
        with self.assertRaises(ValueError):
            guarded_profile_guard_cut(GuardedTranslationProfile(1, None), 0)
        with self.assertRaises(ValueError):
            guarded_profile_effective_cuts(
                GuardedTranslationProfile(0, -1), (), 0
            )
        with self.assertRaises(TypeError):
            apply_guarded_translation_word(0, (1,), False)


if __name__ == "__main__":
    unittest.main()
