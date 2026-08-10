import itertools
import unittest

from enterprise_math.integer_future_affine_model_separation import (
    affine_model_difference_content,
    affine_models_indistinguishable_modulus,
    affine_observation_value,
    augmented_affine_observation_matrix,
    first_distinguishing_affine_prime_power_exponent,
)


class IntegerFutureAffineModelSeparationTests(unittest.TestCase):
    def test_common_offset_cancels_for_state_difference_but_model_offset_difference_is_visible(self):
        linear = ((2, -1),)
        common_offset = (7,)
        left_state = (3, 1)
        right_state = (0, 2)
        left_value = affine_observation_value(
            linear,
            common_offset,
            left_state,
        )[0]
        right_value = affine_observation_value(
            linear,
            common_offset,
            right_state,
        )[0]
        self.assertEqual(
            left_value - right_value,
            2 * (left_state[0] - right_state[0])
            - (left_state[1] - right_state[1]),
        )

        # Two models with equal linear part but different offsets are distinct.
        self.assertEqual(
            affine_model_difference_content(
                linear,
                (7,),
                linear,
                (11,),
            ),
            4,
        )
        self.assertTrue(
            affine_models_indistinguishable_modulus(
                linear,
                (7,),
                linear,
                (11,),
                2,
            )
        )
        self.assertFalse(
            affine_models_indistinguishable_modulus(
                linear,
                (7,),
                linear,
                (11,),
                3,
            )
        )

    def test_augmented_content_combines_linear_and_offset_differences(self):
        left_linear = (
            (1, 2),
            (3, 4),
        )
        right_linear = (
            (1, -4),
            (9, 10),
        )
        left_offset = (5, -7)
        right_offset = (-1, 5)
        # Differences are [0,6,6],[-6,-6,-12], content 6.
        self.assertEqual(
            affine_model_difference_content(
                left_linear,
                left_offset,
                right_linear,
                right_offset,
            ),
            6,
        )
        self.assertEqual(
            augmented_affine_observation_matrix(left_linear, left_offset),
            ((1, 2, 5), (3, 4, -7)),
        )

    def test_modular_indistinguishability_matches_all_bounded_states(self):
        left_linear = ((2, 4),)
        right_linear = ((8, -2),)
        left_offset = (10,)
        right_offset = (-2,)
        self.assertEqual(
            affine_model_difference_content(
                left_linear,
                left_offset,
                right_linear,
                right_offset,
            ),
            6,
        )
        for modulus in range(1, 9):
            predicted = 6 % modulus == 0
            self.assertEqual(
                affine_models_indistinguishable_modulus(
                    left_linear,
                    left_offset,
                    right_linear,
                    right_offset,
                    modulus,
                ),
                predicted,
            )
            for state in itertools.product(range(-2, 3), repeat=2):
                equal = (
                    affine_observation_value(
                        left_linear,
                        left_offset,
                        state,
                        modulus=modulus,
                    )
                    == affine_observation_value(
                        right_linear,
                        right_offset,
                        state,
                        modulus=modulus,
                    )
                )
                self.assertEqual(equal, predicted, (modulus, state))

    def test_first_prime_power_distinguishing_level_uses_augmented_content(self):
        linear = ((1,),)
        left_offset = (0,)
        right_offset = (24,)
        self.assertEqual(
            first_distinguishing_affine_prime_power_exponent(
                linear,
                left_offset,
                linear,
                right_offset,
                2,
            ),
            4,
        )
        self.assertEqual(
            first_distinguishing_affine_prime_power_exponent(
                linear,
                left_offset,
                linear,
                right_offset,
                3,
            ),
            2,
        )
        self.assertEqual(
            first_distinguishing_affine_prime_power_exponent(
                linear,
                left_offset,
                linear,
                right_offset,
                5,
            ),
            1,
        )

    def test_identical_affine_models_have_zero_content_and_no_distinguishing_prime_power(self):
        linear = ((1, 2), (3, 4))
        offset = (5, 6)
        self.assertEqual(
            affine_model_difference_content(
                linear,
                offset,
                linear,
                offset,
            ),
            0,
        )
        self.assertIsNone(
            first_distinguishing_affine_prime_power_exponent(
                linear,
                offset,
                linear,
                offset,
                2,
            )
        )

    def test_validation(self):
        with self.assertRaises(ValueError):
            augmented_affine_observation_matrix(((1, 2),), ())
        with self.assertRaises(ValueError):
            affine_model_difference_content(
                ((1,),),
                (0,),
                ((1, 2),),
                (0,),
            )
        with self.assertRaises(ValueError):
            affine_observation_value(((1, 2),), (0,), (1,))
        with self.assertRaises(ValueError):
            affine_observation_value(((1,),), (0,), (1,), modulus=0)


if __name__ == "__main__":
    unittest.main()
