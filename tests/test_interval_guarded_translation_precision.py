import itertools
import unittest

from enterprise_math.interval_guarded_translation_precision import (
    IntervalGuardedProfile,
    append_interval_guarded_action,
    apply_interval_guarded_profile,
    apply_interval_guarded_word,
    compose_interval_guarded_profiles,
    empty_interval_guarded_profile,
    interval_guarded_breakpoint_cell_equivalent,
    interval_guarded_domain,
    interval_guarded_future_equivalent,
    interval_guarded_future_signature,
    interval_guarded_profile_breakpoints,
    interval_guarded_profile_count_upper_bound,
    interval_guarded_profiles,
    interval_guarded_reachable_breakpoints,
    interval_guarded_word_profile,
)


def literal_words(actions, horizon):
    values = tuple(sorted(set(actions)))
    result = [()]
    for length in range(1, horizon + 1):
        result.extend(itertools.product(values, repeat=length))
    return tuple(result)


def direct_signature(value, actions, horizon, lower, upper, boundaries):
    return tuple(
        (
            word,
            apply_interval_guarded_word(
                value, word, lower, upper, boundaries
            ).defined,
            apply_interval_guarded_word(
                value, word, lower, upper, boundaries
            ).observation,
        )
        for word in literal_words(actions, horizon)
    )


class IntervalGuardedTranslationPrecisionTests(unittest.TestCase):
    def test_word_profile_and_append_match_literal_prefix_envelope(self):
        for actions in ((-2, 3), (-1, 1), (0, 2), (1, 2)):
            for horizon in range(5):
                words = literal_words(actions, horizon)
                self.assertEqual(
                    set(interval_guarded_profiles(actions, horizon)),
                    {interval_guarded_word_profile(word) for word in words},
                )
                for word in words:
                    profile = empty_interval_guarded_profile()
                    for action in word:
                        profile = append_interval_guarded_action(
                            profile, action
                        )
                    self.assertEqual(
                        profile,
                        interval_guarded_word_profile(word),
                    )

    def test_profile_composition_matches_word_concatenation(self):
        words = literal_words((-2, 1, 3), 3)
        for left in words:
            for right in words:
                self.assertEqual(
                    compose_interval_guarded_profiles(
                        interval_guarded_word_profile(left),
                        interval_guarded_word_profile(right),
                    ),
                    interval_guarded_word_profile(left + right),
                )

    def test_interval_domain_is_exact_prefix_legality_envelope(self):
        word = (-2, 4, -1)
        profile = interval_guarded_word_profile(word)
        self.assertEqual(profile.total_translation, 1)
        self.assertEqual(profile.preterminal_minimum, -2)
        self.assertEqual(profile.preterminal_maximum, 2)
        self.assertEqual(interval_guarded_domain(profile, 0, 7), (2, 5))
        for value in range(-1, 8):
            direct = apply_interval_guarded_word(value, word, 0, 7)
            self.assertEqual(direct.defined, 2 <= value < 5)

    def test_profile_execution_equals_literal_word_execution(self):
        boundaries = (-2, 1, 5)
        for word in literal_words((-2, 1, 3), 3):
            profile = interval_guarded_word_profile(word)
            for lower, upper in ((-3, 2), (0, 5), (2, 9)):
                for value in range(-6, 11):
                    self.assertEqual(
                        apply_interval_guarded_profile(
                            value,
                            profile,
                            lower,
                            upper,
                            boundaries,
                        ),
                        apply_interval_guarded_word(
                            value,
                            word,
                            lower,
                            upper,
                            boundaries,
                        ),
                    )

    def test_word_can_be_nowhere_legal_when_prefix_span_exceeds_guard_width(self):
        profile = interval_guarded_word_profile((3, -3))
        self.assertEqual(profile, IntervalGuardedProfile(0, 0, 3))
        self.assertIsNone(interval_guarded_domain(profile, 0, 2))
        self.assertEqual(
            interval_guarded_profile_breakpoints(
                profile, (0, 1), 0, 2
            ),
            (),
        )
        for value in range(-4, 6):
            self.assertFalse(
                apply_interval_guarded_word(
                    value, (3, -3), 0, 2, (0, 1)
                ).defined
            )

    def test_breakpoints_keep_domain_edges_and_only_interior_thresholds(self):
        profile = interval_guarded_word_profile((2,))
        # Domain is [0,5); final shift is +2.  Boundaries 1 and 7 shift to -1
        # and 5 and are masked by the domain edges; boundary 4 shifts to 2 and
        # remains visible in the interior.
        self.assertEqual(interval_guarded_domain(profile, 0, 5), (0, 5))
        self.assertEqual(
            interval_guarded_profile_breakpoints(
                profile, (1, 4, 7), 0, 5
            ),
            (0, 2, 5),
        )

    def test_profile_signature_equals_complete_literal_future_signature(self):
        cases = (
            ((-1, 1), -2, 3, (0,)),
            ((-2, 3), 0, 5, (-1, 2)),
            ((0, 2), -1, 4, ()),
        )
        for actions, lower, upper, boundaries in cases:
            for horizon in range(4):
                values = tuple(range(-6, 8))
                direct = {
                    value: direct_signature(
                        value,
                        actions,
                        horizon,
                        lower,
                        upper,
                        boundaries,
                    )
                    for value in values
                }
                compiled = {
                    value: interval_guarded_future_signature(
                        value,
                        boundaries,
                        actions,
                        lower,
                        upper,
                        horizon,
                    )
                    for value in values
                }
                for left in values:
                    for right in values:
                        self.assertEqual(
                            direct[left] == direct[right],
                            compiled[left] == compiled[right],
                        )
                        self.assertEqual(
                            interval_guarded_future_equivalent(
                                left,
                                right,
                                boundaries,
                                actions,
                                lower,
                                upper,
                                horizon,
                            ),
                            direct[left] == direct[right],
                        )

    def test_breakpoint_arrangement_refines_but_need_not_equal_future_quotient(self):
        cases = (
            ((-1, 1), -2, 3, (0,)),
            ((-2, 3), 0, 5, (-1, 2)),
            ((0, 2), -1, 4, ()),
        )
        for actions, lower, upper, boundaries in cases:
            for horizon in range(4):
                breakpoints = interval_guarded_reachable_breakpoints(
                    boundaries,
                    actions,
                    lower,
                    upper,
                    horizon,
                )
                values = tuple(range(-6, 8))
                signatures = {
                    value: interval_guarded_future_signature(
                        value,
                        boundaries,
                        actions,
                        lower,
                        upper,
                        horizon,
                    )
                    for value in values
                }
                for left in values:
                    for right in values:
                        same_cell = interval_guarded_breakpoint_cell_equivalent(
                            left,
                            right,
                            boundaries,
                            actions,
                            lower,
                            upper,
                            horizon,
                        )
                        lo, hi = sorted((left, right))
                        self.assertEqual(
                            same_cell,
                            not any(lo < cut <= hi for cut in breakpoints),
                        )
                        if same_cell:
                            self.assertEqual(signatures[left], signatures[right])

    def test_interval_guard_can_have_disconnected_future_fiber(self):
        # With no terminal observation, every one-step action is undefined both
        # below the lower edge and at/above the upper edge.  Those two exterior
        # regions are future-equivalent even though the breakpoint arrangement
        # separates them by the entire legal interval.
        actions = (0, 2)
        lower, upper = -1, 4
        boundaries = ()
        horizon = 1
        self.assertEqual(
            interval_guarded_reachable_breakpoints(
                boundaries, actions, lower, upper, horizon
            ),
            (-1, 4),
        )
        left, right = -6, 4
        self.assertTrue(
            interval_guarded_future_equivalent(
                left,
                right,
                boundaries,
                actions,
                lower,
                upper,
                horizon,
            )
        )
        self.assertFalse(
            interval_guarded_breakpoint_cell_equivalent(
                left,
                right,
                boundaries,
                actions,
                lower,
                upper,
                horizon,
            )
        )
        self.assertEqual(
            direct_signature(
                left, actions, horizon, lower, upper, boundaries
            ),
            direct_signature(
                right, actions, horizon, lower, upper, boundaries
            ),
        )

    def test_profile_count_has_cubic_horizon_bound(self):
        for actions in ((-3, 2), (-1, 1), (0,), (0, 2), (1, 4)):
            for horizon in range(7):
                self.assertLessEqual(
                    len(interval_guarded_profiles(actions, horizon)),
                    interval_guarded_profile_count_upper_bound(
                        actions, horizon
                    ),
                )

    def test_positive_words_have_zero_preterminal_minimum(self):
        for word in literal_words((1, 2, 4), 4):
            if not word:
                continue
            profile = interval_guarded_word_profile(word)
            self.assertEqual(profile.preterminal_minimum, 0)
            self.assertEqual(
                profile.preterminal_maximum,
                profile.total_translation - word[-1],
            )

    def test_empty_word_ignores_action_guard(self):
        empty = empty_interval_guarded_profile()
        self.assertIsNone(interval_guarded_domain(empty, 0, 1))
        self.assertEqual(
            interval_guarded_profile_breakpoints(
                empty, (-2, 3), 0, 1
            ),
            (-2, 3),
        )
        for value in (-10, 0, 10):
            outcome = apply_interval_guarded_profile(
                value, empty, 0, 1, (-2, 3)
            )
            self.assertTrue(outcome.defined)
            self.assertEqual(outcome.final_value, value)

    def test_validation(self):
        with self.assertRaises(ValueError):
            interval_guarded_profiles((), 2)
        with self.assertRaises(ValueError):
            interval_guarded_profiles((1,), -1)
        with self.assertRaises(ValueError):
            interval_guarded_domain(
                interval_guarded_word_profile((1,)), 2, 2
            )
        with self.assertRaises(ValueError):
            interval_guarded_profile_breakpoints(
                IntervalGuardedProfile(0, 1, 0), (), 0, 3
            )
        with self.assertRaises(ValueError):
            interval_guarded_profile_breakpoints(
                IntervalGuardedProfile(1, None, None), (), 0, 3
            )
        with self.assertRaises(TypeError):
            apply_interval_guarded_word(0, (1,), False, 3)


if __name__ == "__main__":
    unittest.main()
