import itertools
import unittest

from enterprise_math.integer_dynamic_model_agreement import (
    dynamic_model_agreement_profile,
    dynamic_model_modular_agreement_report,
)
from enterprise_math.integer_dynamic_model_separation import (
    dynamic_models_indistinguishable_modulus,
    literal_dynamic_difference_rows_through_horizon,
)


class IntegerDynamicModelAgreementTests(unittest.TestCase):
    def test_rank_one_difference_module_gives_one_free_exact_agreement_direction(self):
        left_actions = (
            ((1, 0), (0, 1)),
        )
        right_actions = (
            ((1, 6), (0, 1)),
        )
        observation = ((1, 0),)
        profile = dynamic_model_agreement_profile(
            left_actions,
            observation,
            right_actions,
            observation,
        )
        self.assertEqual(profile.state_dimension, 2)
        self.assertEqual(profile.difference_rank, 1)
        self.assertEqual(profile.exact_agreement_free_rank, 1)
        self.assertEqual(profile.difference_smith_factors, (6,))
        self.assertEqual(profile.difference_content, 6)
        self.assertFalse(profile.exactly_equivalent_on_all_states)

    def test_mod_four_agreement_count_matches_M_times_gcd_smith_factor(self):
        left_actions = (((1, 0), (0, 1)),)
        right_actions = (((1, 6), (0, 1)),)
        observation = ((1, 0),)
        report = dynamic_model_modular_agreement_report(
            left_actions,
            observation,
            right_actions,
            observation,
            4,
        )
        self.assertEqual(report.total_state_count, 16)
        self.assertEqual(report.agreement_state_count, 8)
        self.assertEqual(report.disagreement_state_count, 8)
        self.assertFalse(report.all_states_agree)

        mod_two = dynamic_model_modular_agreement_report(
            left_actions,
            observation,
            right_actions,
            observation,
            2,
        )
        self.assertEqual(mod_two.agreement_state_count, 4)
        self.assertTrue(mod_two.all_states_agree)
        self.assertTrue(
            dynamic_models_indistinguishable_modulus(
                left_actions,
                observation,
                right_actions,
                observation,
                2,
            )
        )

    def test_exactly_equivalent_internal_models_have_full_agreement_fiber(self):
        left_actions = (((1, 0), (0, 1)),)
        right_actions = (((1, 0), (1, 0)),)
        observation = ((1, 0),)
        profile = dynamic_model_agreement_profile(
            left_actions,
            observation,
            right_actions,
            observation,
        )
        self.assertTrue(profile.exactly_equivalent_on_all_states)
        self.assertEqual(profile.exact_agreement_free_rank, 2)
        self.assertEqual(profile.difference_smith_factors, ())
        for modulus in range(1, 8):
            modular = dynamic_model_modular_agreement_report(
                left_actions,
                observation,
                right_actions,
                observation,
                modulus,
            )
            self.assertTrue(modular.all_states_agree)
            self.assertEqual(
                modular.agreement_state_count,
                modulus ** 2,
            )

    def test_full_rank_unimodular_difference_leaves_only_one_modular_agreement_state(self):
        # Current observations themselves differ by the identity matrix.  The
        # agreement map is full-rank unimodular before any future action.
        actions = (((1, 0), (0, 1)),)
        left_observation = ((1, 0), (0, 1))
        right_observation = ((0, 0), (0, 0))
        profile = dynamic_model_agreement_profile(
            actions,
            left_observation,
            actions,
            right_observation,
        )
        self.assertEqual(profile.difference_rank, 2)
        self.assertEqual(profile.exact_agreement_free_rank, 0)
        self.assertEqual(profile.difference_smith_factors, (1, 1))
        for modulus in (2, 3, 5):
            modular = dynamic_model_modular_agreement_report(
                actions,
                left_observation,
                actions,
                right_observation,
                modulus,
            )
            self.assertEqual(modular.agreement_state_count, 1)
            self.assertEqual(
                modular.disagreement_state_count,
                modulus ** 2 - 1,
            )

    def test_modular_agreement_count_matches_direct_literal_outputs_on_small_tori(self):
        left_actions = (((1, 0), (0, 1)),)
        right_actions = (((1, 2), (0, 1)),)
        observation = ((1, 0),)
        for modulus in (2, 3, 4):
            report = dynamic_model_modular_agreement_report(
                left_actions,
                observation,
                right_actions,
                observation,
                modulus,
            )
            agreeing = 0
            # The single-action pair closes immediately as a rank-one difference
            # module; checking literal differences through horizon two is enough
            # for this bounded independent oracle.
            rows = literal_dynamic_difference_rows_through_horizon(
                left_actions,
                observation,
                right_actions,
                observation,
                2,
            )
            for state in itertools.product(range(modulus), repeat=2):
                if all(
                    sum(coefficient * value for coefficient, value in zip(row, state, strict=True)) % modulus == 0
                    for row in rows
                ):
                    agreeing += 1
            self.assertEqual(agreeing, report.agreement_state_count)

    def test_validation(self):
        with self.assertRaises(ValueError):
            dynamic_model_modular_agreement_report(
                (((1,),),),
                ((1,),),
                (((1,),),),
                ((1,),),
                0,
            )
        with self.assertRaises(TypeError):
            dynamic_model_modular_agreement_report(
                (((1,),),),
                ((1,),),
                (((1,),),),
                ((1,),),
                False,
            )


if __name__ == "__main__":
    unittest.main()
