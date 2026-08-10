import itertools
import unittest

from enterprise_math.guarded_translation_precision import (
    GuardedTranslationProfile,
    guarded_translation_profiles,
    guarded_word_profile,
)
from enterprise_math.guarded_word_normal_form import (
    guarded_profile_partial_affine_outcome,
    guarded_profile_product,
    guarded_profile_separating_witness,
    guarded_profiles_extensionally_equal,
    guarded_requirement_composition_identity,
    guarded_requirement_transform,
)


def literal_words(actions, horizon):
    values = tuple(sorted(set(actions)))
    result = [()]
    for length in range(1, horizon + 1):
        result.extend(itertools.product(values, repeat=length))
    return tuple(result)


class GuardedWordNormalFormTests(unittest.TestCase):
    def test_every_distinct_small_profile_has_constructive_separating_state(self):
        action_sets = ((-2, 3), (-1, 1), (0, 2), (1, 2))
        checked = 0
        for actions in action_sets:
            profiles = guarded_translation_profiles(actions, 4)
            for guard in (-3, 0, 5):
                for left in profiles:
                    for right in profiles:
                        witness = guarded_profile_separating_witness(
                            left, right, guard
                        )
                        if left == right:
                            self.assertIsNone(witness)
                            continue
                        self.assertIsNotNone(witness)
                        assert witness is not None
                        self.assertTrue(
                            witness.left.defined != witness.right.defined
                            or witness.left.final_value != witness.right.final_value
                        )
                        checked += 1
        self.assertGreater(checked, 1000)

    def test_equal_profiles_are_extensionally_equal_for_all_sampled_states(self):
        words = literal_words((-2, 1, 3), 4)
        buckets = {}
        for word in words:
            buckets.setdefault(guarded_word_profile(word), []).append(word)
        guard = 2
        for profile, bucket in buckets.items():
            for value in range(-8, 8):
                expected = guarded_profile_partial_affine_outcome(
                    value, profile, guard
                )
                for word in bucket:
                    self.assertEqual(
                        guarded_word_profile(word),
                        profile,
                    )
                    self.assertTrue(
                        guarded_profiles_extensionally_equal(
                            profile, guarded_word_profile(word)
                        )
                    )
                    self.assertEqual(
                        guarded_profile_partial_affine_outcome(
                            value, guarded_word_profile(word), guard
                        ),
                        expected,
                    )

    def test_empty_word_is_not_same_as_nonempty_partial_identity(self):
        empty = GuardedTranslationProfile(0, None)
        partial_identity = guarded_word_profile((1, -1))
        self.assertEqual(partial_identity.total_translation, 0)
        self.assertEqual(partial_identity.preterminal_peak, 1)
        self.assertFalse(
            guarded_profiles_extensionally_equal(empty, partial_identity)
        )
        witness = guarded_profile_separating_witness(
            empty, partial_identity, 0
        )
        self.assertIsNotNone(witness)
        assert witness is not None
        self.assertEqual(witness.state, -1)
        self.assertTrue(witness.left.defined)
        self.assertFalse(witness.right.defined)

    def test_different_peak_same_total_separates_by_definedness(self):
        left = guarded_word_profile((1, 2))
        right = guarded_word_profile((2, 1))
        self.assertEqual(left.total_translation, right.total_translation)
        self.assertNotEqual(left.preterminal_peak, right.preterminal_peak)
        witness = guarded_profile_separating_witness(left, right, 0)
        self.assertIsNotNone(witness)
        assert witness is not None
        self.assertEqual(witness.reason, "different_guard_domain")
        self.assertNotEqual(witness.left.defined, witness.right.defined)

    def test_same_peak_different_total_separates_by_final_value(self):
        left = guarded_word_profile((1, 1))
        right = guarded_word_profile((1, 2))
        self.assertEqual(left.preterminal_peak, right.preterminal_peak)
        self.assertNotEqual(left.total_translation, right.total_translation)
        witness = guarded_profile_separating_witness(left, right, 4)
        self.assertIsNotNone(witness)
        assert witness is not None
        self.assertEqual(witness.reason, "different_final_translation")
        self.assertTrue(witness.left.defined)
        self.assertTrue(witness.right.defined)
        self.assertNotEqual(witness.left.final_value, witness.right.final_value)

    def test_profile_product_is_associative_and_empty_is_identity(self):
        profiles = guarded_translation_profiles((-2, 1, 3), 3)
        empty = GuardedTranslationProfile(0, None)
        for profile in profiles:
            self.assertEqual(
                guarded_profile_product(empty, profile),
                profile,
            )
            self.assertEqual(
                guarded_profile_product(profile, empty),
                profile,
            )
        for left in profiles:
            for middle in profiles:
                for right in profiles:
                    self.assertEqual(
                        guarded_profile_product(
                            guarded_profile_product(left, middle),
                            right,
                        ),
                        guarded_profile_product(
                            left,
                            guarded_profile_product(middle, right),
                        ),
                    )

    def test_profile_product_matches_literal_word_concatenation(self):
        words = literal_words((-2, 1, 3), 3)
        for left_word in words:
            for right_word in words:
                self.assertEqual(
                    guarded_profile_product(
                        guarded_word_profile(left_word),
                        guarded_word_profile(right_word),
                    ),
                    guarded_word_profile(left_word + right_word),
                )

    def test_requirement_transform_is_exact_max_plus_homomorphism(self):
        profiles = guarded_translation_profiles((-2, 1, 3), 3)
        suffixes = (None, 0, 1, 4, 9)
        checked = 0
        for left in profiles:
            for right in profiles:
                for suffix in suffixes:
                    self.assertTrue(
                        guarded_requirement_composition_identity(
                            left, right, suffix
                        )
                    )
                    checked += 1
        self.assertGreater(checked, 1000)

    def test_requirement_transform_recovers_profile_peak_from_empty_suffix(self):
        for profile in guarded_translation_profiles((-2, 1, 3), 4):
            self.assertEqual(
                guarded_requirement_transform(profile, None),
                profile.preterminal_peak,
            )

    def test_validation(self):
        with self.assertRaises(ValueError):
            guarded_profile_separating_witness(
                GuardedTranslationProfile(1, None),
                GuardedTranslationProfile(0, None),
                0,
            )
        with self.assertRaises(ValueError):
            guarded_requirement_transform(
                GuardedTranslationProfile(0, 0), -1
            )
        with self.assertRaises(TypeError):
            guarded_profile_partial_affine_outcome(
                0, GuardedTranslationProfile(0, None), False
            )


if __name__ == "__main__":
    unittest.main()
