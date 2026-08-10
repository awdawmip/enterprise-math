import itertools
import unittest

from enterprise_math.lattice_guard_precision import IntegerGuard
from enterprise_math.multi_guarded_score_profile import (
    MultiGuardedProfile,
    append_multi_guarded_action,
    apply_multi_guarded_profile,
    apply_multi_guarded_word,
    compose_multi_guarded_profiles,
    empty_multi_guarded_profile,
    multi_guarded_profile_defined,
    multi_guarded_profiles,
    multi_guarded_word_profile,
    primitive_guard_cuts,
    primitive_score_vector,
    projected_action_shift_vector,
    projected_profile_count_upper_bound,
)


def literal_words(actions, horizon):
    values = tuple(actions)
    result = [()]
    for length in range(1, horizon + 1):
        result.extend(itertools.product(values, repeat=length))
    return tuple(result)


class MultiGuardedScoreProfileTests(unittest.TestCase):
    def test_word_profile_matches_direct_projected_prefix_vectors(self):
        guards = (
            IntegerGuard((1, 0), 0),
            IntegerGuard((0, 1), 1),
            IntegerGuard((1, 1), 2),
        )
        word = ((1, 0), (0, 2), (-2, -1))
        self.assertEqual(
            projected_action_shift_vector((1, 0), guards),
            (1, 0, 1),
        )
        profile = multi_guarded_word_profile(word, guards)
        self.assertEqual(profile.total_shifts, (-1, 1, 0))
        self.assertEqual(profile.preterminal_peaks, (1, 2, 3))

    def test_append_compiler_reconstructs_every_literal_word_profile(self):
        guards = (
            IntegerGuard((1, 0), 1),
            IntegerGuard((0, 1), 2),
        )
        actions = ((1, 0), (0, 1), (-1, 2))
        for horizon in range(5):
            words = literal_words(actions, horizon)
            self.assertEqual(
                set(multi_guarded_profiles(actions, guards, horizon)),
                {multi_guarded_word_profile(word, guards) for word in words},
            )
            for word in words:
                profile = empty_multi_guarded_profile(len(guards))
                for action in word:
                    profile = append_multi_guarded_action(
                        profile, action, guards
                    )
                self.assertEqual(
                    profile,
                    multi_guarded_word_profile(word, guards),
                )

    def test_profile_composition_matches_literal_concatenation(self):
        guards = (
            IntegerGuard((1, 0), 0),
            IntegerGuard((0, 1), 0),
        )
        words = literal_words(((1, 0), (0, 1), (-1, -1)), 3)
        for left in words:
            for right in words:
                self.assertEqual(
                    compose_multi_guarded_profiles(
                        multi_guarded_word_profile(left, guards),
                        multi_guarded_word_profile(right, guards),
                    ),
                    multi_guarded_word_profile(left + right, guards),
                )

    def test_profile_definedness_and_final_scores_equal_direct_word(self):
        guards = (
            IntegerGuard((2, 0), 1),
            IntegerGuard((0, 3), 2),
            IntegerGuard((1, 1), 1),
        )
        actions = ((1, 0), (0, 1), (-1, 1))
        words = literal_words(actions, 3)
        for point in itertools.product(range(-4, 3), repeat=2):
            for word in words:
                direct = apply_multi_guarded_word(point, word, guards)
                profile = multi_guarded_word_profile(word, guards)
                compiled = apply_multi_guarded_profile(
                    point, profile, guards
                )
                self.assertEqual(compiled.defined, direct.defined)
                self.assertEqual(compiled.final_scores, direct.final_scores)
                self.assertEqual(
                    multi_guarded_profile_defined(point, profile, guards),
                    direct.defined,
                )

    def test_same_total_score_shift_can_hide_order_sensitive_peak_vector(self):
        guards = (
            IntegerGuard((1, 0), 0),
            IntegerGuard((0, 1), 0),
        )
        action_x = (1, 0)
        action_y = (0, 1)
        left = multi_guarded_word_profile((action_x, action_y), guards)
        right = multi_guarded_word_profile((action_y, action_x), guards)
        self.assertEqual(left.total_shifts, right.total_shifts)
        self.assertEqual(left.total_shifts, (1, 1))
        self.assertEqual(left.preterminal_peaks, (1, 0))
        self.assertEqual(right.preterminal_peaks, (0, 1))

        point = (-1, -2)
        self.assertFalse(
            apply_multi_guarded_word(
                point, (action_x, action_y), guards
            ).defined
        )
        self.assertTrue(
            apply_multi_guarded_word(
                point, (action_y, action_x), guards
            ).defined
        )

    def test_ambient_nullspace_detail_is_erased_when_full_score_vector_agrees(self):
        guards = (
            IntegerGuard((1, 1, 0), 2),
            IntegerGuard((0, 1, 1), 3),
        )
        actions = ((1, 0, 0), (0, 1, 0), (-1, 0, 1))
        # Difference (1,-1,1) lies in both guard-row kernels.
        left = (0, 0, 0)
        right = (1, -1, 1)
        self.assertEqual(
            primitive_score_vector(left, guards),
            primitive_score_vector(right, guards),
        )
        for profile in multi_guarded_profiles(actions, guards, 4):
            left_outcome = apply_multi_guarded_profile(
                left, profile, guards
            )
            right_outcome = apply_multi_guarded_profile(
                right, profile, guards
            )
            self.assertEqual(
                left_outcome.defined,
                right_outcome.defined,
            )
            self.assertEqual(
                left_outcome.final_scores,
                right_outcome.final_scores,
            )

    def test_profile_count_has_polynomial_guard_rank_bound(self):
        guard_sets = (
            (IntegerGuard((1, 0), 0),),
            (
                IntegerGuard((1, 0), 0),
                IntegerGuard((0, 1), 0),
            ),
            (
                IntegerGuard((1, 0), 0),
                IntegerGuard((0, 1), 0),
                IntegerGuard((1, 1), 0),
            ),
        )
        actions = ((1, 0), (-1, 1), (0, -1))
        for guards in guard_sets:
            for horizon in range(6):
                self.assertLessEqual(
                    len(multi_guarded_profiles(actions, guards, horizon)),
                    projected_profile_count_upper_bound(
                        actions, guards, horizon
                    ),
                )

    def test_primitive_guard_cuts_and_score_vector_use_existing_normalization(self):
        guards = (
            IntegerGuard((2, 4), 5),
            IntegerGuard((0, 3), -1),
        )
        self.assertEqual(primitive_guard_cuts(guards), (3, 0))
        self.assertEqual(
            primitive_score_vector((1, 2), guards),
            (5, 2),
        )

    def test_validation(self):
        with self.assertRaises(ValueError):
            empty_multi_guarded_profile(0)
        with self.assertRaises(ValueError):
            multi_guarded_word_profile((), ())
        with self.assertRaises(ValueError):
            multi_guarded_word_profile(
                (), (IntegerGuard((0, 0), 1),)
            )
        with self.assertRaises(ValueError):
            projected_action_shift_vector(
                (1,), (IntegerGuard((1, 0), 0),)
            )
        with self.assertRaises(ValueError):
            compose_multi_guarded_profiles(
                MultiGuardedProfile((0,), (0,)),
                MultiGuardedProfile((0, 0), (0, 0)),
            )
        with self.assertRaises(ValueError):
            multi_guarded_profile_defined(
                (0, 0),
                MultiGuardedProfile((0, 0), (-1, 0)),
                (
                    IntegerGuard((1, 0), 0),
                    IntegerGuard((0, 1), 0),
                ),
            )


if __name__ == "__main__":
    unittest.main()
