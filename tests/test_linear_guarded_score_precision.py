import itertools
import unittest

from enterprise_math.guarded_translation_precision import (
    apply_guarded_translation_word,
)
from enterprise_math.lattice_guard_precision import IntegerGuard
from enterprise_math.linear_guarded_score_precision import (
    apply_linear_guarded_word,
    linear_guard_enabled,
    linear_guarded_future_signature,
    linear_guarded_points_equivalent,
    linear_guarded_score_cuts,
    linear_guarded_word_profile,
    primitive_upper_guard_cut,
    projected_action_alphabet,
    projected_action_word,
)


def vector_words(actions, horizon):
    values = tuple(actions)
    result = [()]
    for length in range(1, horizon + 1):
        result.extend(itertools.product(values, repeat=length))
    return tuple(result)


def direct_signature(point, guard, actions, boundaries, horizon):
    return tuple(
        (
            word,
            apply_linear_guarded_word(
                point, word, guard, boundaries
            ).defined,
            apply_linear_guarded_word(
                point, word, guard, boundaries
            ).observation,
        )
        for word in vector_words(actions, horizon)
    )


class LinearGuardedScorePrecisionTests(unittest.TestCase):
    def test_raw_strict_guard_equals_primitive_score_cut(self):
        guard = IntegerGuard((2, 4), 5)
        self.assertEqual(guard.coefficient_gcd, 2)
        self.assertEqual(guard.primitive_row, (1, 2))
        self.assertEqual(primitive_upper_guard_cut(guard), 3)
        for x in range(-4, 5):
            for y in range(-4, 5):
                self.assertEqual(
                    linear_guard_enabled((x, y), guard),
                    x + 2 * y < 3,
                )

    def test_vector_word_profile_is_exact_projected_scalar_profile(self):
        guard = IntegerGuard((2, 4), 5)
        word = ((1, 0), (0, 1), (-3, 1))
        projected = projected_action_word(word, guard)
        self.assertEqual(projected, (1, 2, -1))
        profile = linear_guarded_word_profile(word, guard)
        self.assertEqual(profile.total_translation, 2)
        self.assertEqual(profile.preterminal_peak, 3)

    def test_direct_vector_execution_equals_one_dimensional_guarded_execution(self):
        guard = IntegerGuard((2, 4), 5)
        boundaries = (-1, 2, 5)
        words = vector_words(((1, 0), (0, 1), (-1, 0)), 3)
        for point in itertools.product(range(-3, 4), repeat=2):
            initial_score = guard.primitive_score(point)
            for word in words:
                vector_outcome = apply_linear_guarded_word(
                    point, word, guard, boundaries
                )
                scalar_outcome = apply_guarded_translation_word(
                    initial_score,
                    projected_action_word(word, guard),
                    primitive_upper_guard_cut(guard),
                    boundaries,
                )
                self.assertEqual(
                    vector_outcome.defined,
                    scalar_outcome.defined,
                )
                self.assertEqual(
                    vector_outcome.observation,
                    scalar_outcome.observation,
                )
                self.assertEqual(
                    vector_outcome.final_primitive_score,
                    scalar_outcome.final_value,
                )

    def test_nullspace_detail_is_future_invisible_for_declared_language(self):
        guard = IntegerGuard((1, 2), 3)
        actions = ((1, 0), (0, 1), (-1, 0))
        boundaries = (-2, 0, 4)
        # Difference (2,-1) lies in the primitive guard-row kernel.
        left = (0, 0)
        right = (2, -1)
        self.assertEqual(
            guard.primitive_score(left),
            guard.primitive_score(right),
        )
        for horizon in range(5):
            self.assertEqual(
                linear_guarded_future_signature(
                    left, guard, actions, boundaries, horizon
                ),
                linear_guarded_future_signature(
                    right, guard, actions, boundaries, horizon
                ),
            )
            self.assertTrue(
                linear_guarded_points_equivalent(
                    left,
                    right,
                    guard,
                    actions,
                    boundaries,
                    horizon,
                )
            )

    def test_vector_actions_with_same_score_shift_collapse_for_this_task(self):
        guard = IntegerGuard((1, 0), 2)
        actions = ((1, 0), (1, 7), (-1, 3))
        self.assertEqual(
            projected_action_alphabet(guard, actions),
            (-1, 1),
        )
        self.assertEqual(
            projected_action_word(((1, 0),), guard),
            projected_action_word(((1, 7),), guard),
        )
        for point in ((-2, 0), (0, 4), (1, -9)):
            first = apply_linear_guarded_word(
                point, ((1, 0),), guard, (0, 3)
            )
            second = apply_linear_guarded_word(
                point, ((1, 7),), guard, (0, 3)
            )
            self.assertEqual(first.defined, second.defined)
            self.assertEqual(first.observation, second.observation)
            self.assertEqual(
                first.final_primitive_score,
                second.final_primitive_score,
            )

    def test_score_cut_partition_equals_complete_literal_vector_future_partition(self):
        guard = IntegerGuard((1, 1), 1)
        actions = ((1, 0), (0, 1), (-1, 0))
        boundaries = (-1, 2)
        for horizon in range(4):
            cuts = linear_guarded_score_cuts(
                guard, actions, boundaries, horizon
            )
            points = tuple(itertools.product(range(-3, 4), repeat=2))
            signatures = {
                point: direct_signature(
                    point, guard, actions, boundaries, horizon
                )
                for point in points
            }
            for left in points:
                for right in points:
                    direct_equal = signatures[left] == signatures[right]
                    left_score = guard.primitive_score(left)
                    right_score = guard.primitive_score(right)
                    lo, hi = sorted((left_score, right_score))
                    cut_equal = not any(lo < cut <= hi for cut in cuts)
                    self.assertEqual(direct_equal, cut_equal)
                    self.assertEqual(
                        linear_guarded_points_equivalent(
                            left,
                            right,
                            guard,
                            actions,
                            boundaries,
                            horizon,
                        ),
                        direct_equal,
                    )

    def test_validation(self):
        with self.assertRaises(ValueError):
            primitive_upper_guard_cut(IntegerGuard((0, 0), 1))
        with self.assertRaises(ValueError):
            projected_action_alphabet(
                IntegerGuard((1, 0), 1),
                ((1,),),
            )
        with self.assertRaises(ValueError):
            apply_linear_guarded_word(
                (0,),
                ((1, 0),),
                IntegerGuard((1, 0), 1),
            )
        with self.assertRaises(TypeError):
            apply_linear_guarded_word(
                (0, 0),
                ((True, 0),),
                IntegerGuard((1, 0), 1),
            )


if __name__ == "__main__":
    unittest.main()
