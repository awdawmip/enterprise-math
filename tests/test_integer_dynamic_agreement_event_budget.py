import unittest

from enterprise_math.integer_dynamic_affine_agreement_horizon import (
    dynamic_affine_agreement_horizon_report,
)
from enterprise_math.integer_dynamic_agreement_event_budget import (
    agreement_event_budget_report,
)


class IntegerDynamicAgreementEventBudgetTests(unittest.TestCase):
    def test_exact_free_rank_bound(self):
        left_actions = (
            (
                ((0, 1), (0, 0)),
                (0, 0),
            ),
        )
        right_actions = (
            (
                ((0, 0), (0, 0)),
                (0, 0),
            ),
        )
        report = dynamic_affine_agreement_horizon_report(
            left_actions,
            ((1, 0),),
            (0,),
            right_actions,
            ((1, 0),),
            (0,),
        )
        budget = agreement_event_budget_report(report)
        self.assertEqual(budget.initial_exact_free_rank, 2)
        self.assertEqual(budget.strict_nonempty_event_bound, 2)
        self.assertEqual(budget.observed_strict_nonempty_events, 1)
        self.assertTrue(budget.within_bound)

    def test_mod_four_two_state_fiber_can_strictly_shrink_at_most_once_before_singleton(self):
        left_actions = ((((1,),), (0,)),)
        right_actions = ((((0,),), (0,)),)
        report = dynamic_affine_agreement_horizon_report(
            left_actions,
            ((1,),),
            (0,),
            right_actions,
            ((-1,),),
            (0,),
            modulus=4,
        )
        budget = agreement_event_budget_report(report)
        self.assertEqual(budget.initial_modular_state_count, 2)
        self.assertEqual(budget.strict_nonempty_event_bound, 1)
        self.assertEqual(budget.observed_strict_nonempty_events, 1)
        self.assertTrue(budget.within_bound)

    def test_full_modular_state_space_has_Omega_Mn_event_budget_not_horizon_bound(self):
        # Current models are identical, so all 8 states mod2 agree in dimension3.
        # A nilpotent future action later reveals one coordinate.  The arithmetic
        # event budget is Omega(8)=3, although only one strict change occurs here.
        left_actions = (
            (
                ((0, 1, 0), (0, 0, 0), (0, 0, 0)),
                (0, 0, 0),
            ),
        )
        right_actions = (
            (
                ((0, 0, 0), (0, 0, 0), (0, 0, 0)),
                (0, 0, 0),
            ),
        )
        report = dynamic_affine_agreement_horizon_report(
            left_actions,
            ((1, 0, 0),),
            (0,),
            right_actions,
            ((1, 0, 0),),
            (0,),
            modulus=2,
        )
        budget = agreement_event_budget_report(report)
        self.assertEqual(budget.initial_modular_state_count, 8)
        self.assertEqual(budget.strict_nonempty_event_bound, 3)
        self.assertLessEqual(budget.observed_strict_nonempty_events, 3)

    def test_empty_collapse_can_occur_only_once_then_is_absorbing(self):
        actions = ((((1,),), (-1,)),)
        report = dynamic_affine_agreement_horizon_report(
            actions,
            ((2,),),
            (2,),
            actions,
            ((0,),),
            (0,),
            modulus=4,
        )
        budget = agreement_event_budget_report(report)
        self.assertEqual(budget.empty_collapse_bound, 1)
        self.assertEqual(budget.observed_empty_collapses, 1)
        self.assertTrue(budget.within_bound)

    def test_identical_models_have_zero_strict_events_even_with_positive_budget(self):
        actions = ((((1,),), (3,)),)
        report = dynamic_affine_agreement_horizon_report(
            actions,
            ((1,),),
            (7,),
            actions,
            ((1,),),
            (7,),
            modulus=6,
        )
        budget = agreement_event_budget_report(report)
        self.assertEqual(budget.observed_strict_nonempty_events, 0)
        self.assertEqual(budget.observed_empty_collapses, 0)
        self.assertGreaterEqual(budget.strict_nonempty_event_bound, 0)

    def test_validation(self):
        with self.assertRaises(TypeError):
            agreement_event_budget_report(object())


if __name__ == "__main__":
    unittest.main()
