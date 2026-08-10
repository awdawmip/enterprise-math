import itertools
import unittest

from enterprise_math.integer_action_module_closure import (
    action_module_closure_report,
    integer_row_hermite_basis,
)
from enterprise_math.integer_dynamic_model_separation import (
    block_diagonal_action,
    block_difference_observation_rows,
    dynamic_difference_content,
    dynamic_difference_module_basis,
    dynamic_model_separation_report,
    dynamic_models_indistinguishable_modulus,
    finite_horizon_dynamic_difference_content,
    first_dynamic_distinguishing_prime_power_exponent,
    literal_dynamic_difference_rows_through_horizon,
    project_block_difference_rows,
)


class IntegerDynamicModelSeparationTests(unittest.TestCase):
    def test_block_HNF_projection_matches_literal_words_at_exact_augmented_closure_horizon(self):
        model_pairs = (
            (
                (((0, 1), (0, 0)),),
                (((0, 2), (0, 0)),),
            ),
            (
                (
                    ((1, 1), (0, 1)),
                    ((0, 1), (1, 0)),
                ),
                (
                    ((1, 0), (1, 1)),
                    ((1, 1), (0, 0)),
                ),
            ),
        )
        left_obs = ((1, 0),)
        right_obs = ((1, 0),)

        for left_actions, right_actions in model_pairs:
            block_actions = tuple(
                block_diagonal_action(left, right)
                for left, right in zip(left_actions, right_actions, strict=True)
            )
            block_rows = block_difference_observation_rows(left_obs, right_obs)
            block_report = action_module_closure_report(block_actions, block_rows)
            literal = literal_dynamic_difference_rows_through_horizon(
                left_actions,
                left_obs,
                right_actions,
                right_obs,
                block_report.exact_stabilization_horizon,
            )
            expected = integer_row_hermite_basis(literal)
            actual = dynamic_difference_module_basis(
                left_actions,
                left_obs,
                right_actions,
                right_obs,
            )
            self.assertEqual(actual, expected)
            self.assertEqual(
                actual,
                project_block_difference_rows(
                    block_report.final_basis,
                    2,
                ),
            )

    def test_horizon_difference_content_is_a_divisibility_filtration(self):
        left_actions = (
            ((1, 0), (0, 1)),
        )
        right_actions = (
            ((1, 6), (0, 1)),
        )
        left_obs = right_obs = ((1, 0),)

        contents = tuple(
            finite_horizon_dynamic_difference_content(
                left_actions,
                left_obs,
                right_actions,
                right_obs,
                horizon,
            )
            for horizon in range(6)
        )
        self.assertEqual(contents[0], 0)
        self.assertEqual(contents[1:], (6, 6, 6, 6, 6))
        for earlier, later in zip(contents, contents[1:]):
            self.assertTrue(earlier == 0 or earlier % later == 0)

    def test_dynamic_modular_indistinguishability_region_is_divisors_of_final_content(self):
        left_actions = (
            ((1, 0), (0, 1)),
        )
        right_actions = (
            ((1, 6), (0, 1)),
        )
        observation = ((1, 0),)
        self.assertEqual(
            dynamic_difference_content(
                left_actions,
                observation,
                right_actions,
                observation,
            ),
            6,
        )
        for modulus in range(1, 15):
            self.assertEqual(
                dynamic_models_indistinguishable_modulus(
                    left_actions,
                    observation,
                    right_actions,
                    observation,
                    modulus,
                ),
                6 % modulus == 0,
            )
        self.assertEqual(
            first_dynamic_distinguishing_prime_power_exponent(
                left_actions,
                observation,
                right_actions,
                observation,
                2,
            ),
            2,
        )
        self.assertEqual(
            first_dynamic_distinguishing_prime_power_exponent(
                left_actions,
                observation,
                right_actions,
                observation,
                3,
            ),
            2,
        )

    def test_internally_different_models_can_be_exactly_future_output_equivalent(self):
        left_actions = (
            ((1, 0), (0, 1)),
        )
        right_actions = (
            ((1, 0), (1, 0)),
        )
        observation = ((1, 0),)
        report = dynamic_model_separation_report(
            left_actions,
            observation,
            right_actions,
            observation,
        )
        self.assertTrue(report.exactly_future_equivalent)
        self.assertEqual(report.difference_module_basis, ())
        self.assertEqual(report.difference_content, 0)
        for horizon in range(5):
            literal = literal_dynamic_difference_rows_through_horizon(
                left_actions,
                observation,
                right_actions,
                observation,
                horizon,
            )
            self.assertTrue(all(all(value == 0 for value in row) for row in literal))

    def test_same_current_observation_can_first_separate_at_future_horizon(self):
        left_actions = (
            ((0, 1), (0, 0)),
        )
        right_actions = (
            ((0, 0), (0, 0)),
        )
        observation = ((1, 0),)
        self.assertEqual(
            finite_horizon_dynamic_difference_content(
                left_actions,
                observation,
                right_actions,
                observation,
                0,
            ),
            0,
        )
        self.assertEqual(
            finite_horizon_dynamic_difference_content(
                left_actions,
                observation,
                right_actions,
                observation,
                1,
            ),
            1,
        )
        self.assertEqual(
            dynamic_difference_module_basis(
                left_actions,
                observation,
                right_actions,
                observation,
            ),
            ((0, 1),),
        )

    def test_small_single_action_pairs_match_literal_module_at_bounded_closure(self):
        actions = tuple(
            (
                (entries[0], entries[1]),
                (entries[2], entries[3]),
            )
            for entries in itertools.product((0, 1), repeat=4)
        )
        observation = ((1, 0),)
        for left in actions:
            for right in actions:
                block_action = block_diagonal_action(left, right)
                block_rows = block_difference_observation_rows(observation, observation)
                horizon = action_module_closure_report(
                    (block_action,),
                    block_rows,
                ).exact_stabilization_horizon
                literal_basis = integer_row_hermite_basis(
                    literal_dynamic_difference_rows_through_horizon(
                        (left,),
                        observation,
                        (right,),
                        observation,
                        horizon,
                    )
                )
                self.assertEqual(
                    dynamic_difference_module_basis(
                        (left,),
                        observation,
                        (right,),
                        observation,
                    ),
                    literal_basis,
                    (left, right),
                )

    def test_validation(self):
        with self.assertRaises(ValueError):
            dynamic_difference_module_basis(
                (((1,),),),
                ((1,),),
                (((1, 0), (0, 1)),),
                ((1, 0),),
            )
        with self.assertRaises(ValueError):
            dynamic_models_indistinguishable_modulus(
                (((1,),),),
                ((1,),),
                (((1,),),),
                ((1,),),
                0,
            )
        with self.assertRaises(ValueError):
            finite_horizon_dynamic_difference_content(
                (((1,),),),
                ((1,),),
                (((1,),),),
                ((1,),),
                -1,
            )


if __name__ == "__main__":
    unittest.main()
