import unittest

from enterprise_math.integer_dynamic_affine_agreement_horizon import (
    dynamic_affine_agreement_horizon_report,
)
from enterprise_math.integer_dynamic_agreement_events import (
    EMPTY_ABSORBED,
    EMPTY_COLLAPSE,
    FREE_RANK_SHRINK,
    MODULAR_TORSION_SHRINK,
    UNCHANGED,
    agreement_filtration_events,
)


class IntegerDynamicAgreementEventsTests(unittest.TestCase):
    def test_exact_future_difference_causes_free_rank_shrink(self):
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
        events = agreement_filtration_events(report)
        self.assertEqual(events[0].event, FREE_RANK_SHRINK)
        self.assertEqual(report.steps[0].exact_agreement_free_rank, 2)
        self.assertEqual(report.steps[1].exact_agreement_free_rank, 1)

    def test_modular_same_rank_smith_purification_is_torsion_shrink(self):
        # Current output difference is 2x.  Future left action keeps x while the
        # right action maps everything to zero, so horizon one also adds x.
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
        events = agreement_filtration_events(report)
        self.assertEqual(events[0].event, MODULAR_TORSION_SHRINK)
        self.assertEqual(report.steps[0].linear_rank, 1)
        self.assertEqual(report.steps[1].linear_rank, 1)
        self.assertEqual(report.steps[0].linear_smith_factors, (2,))
        self.assertEqual(report.steps[1].linear_smith_factors, (1,))
        self.assertEqual(report.steps[0].modular_agreement_state_count, 2)
        self.assertEqual(report.steps[1].modular_agreement_state_count, 1)

    def test_affine_image_inconsistency_is_empty_collapse_then_absorbing(self):
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
        events = agreement_filtration_events(report)
        self.assertEqual(events[0].event, EMPTY_COLLAPSE)
        self.assertTrue(
            all(event.event == EMPTY_ABSORBED for event in events[1:])
        )
        self.assertEqual(report.first_empty_agreement_horizon, 1)

    def test_identical_models_only_emit_unchanged_events(self):
        actions = ((((1,),), (3,)),)
        report = dynamic_affine_agreement_horizon_report(
            actions,
            ((1,),),
            (7,),
            actions,
            ((1,),),
            (7,),
            modulus=5,
        )
        self.assertTrue(
            all(event.event == UNCHANGED for event in agreement_filtration_events(report))
        )

    def test_modular_free_rank_shrink_takes_priority_when_rational_rank_grows(self):
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
            modulus=3,
        )
        event = agreement_filtration_events(report)[0]
        self.assertEqual(event.event, FREE_RANK_SHRINK)
        self.assertGreater(event.next_linear_rank, event.previous_linear_rank)
        self.assertLess(event.next_modular_count, event.previous_modular_count)

    def test_empty_set_never_resurrects_under_added_constraints(self):
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
        saw_empty = False
        for step in report.steps:
            if not step.solvable:
                saw_empty = True
            if saw_empty:
                self.assertFalse(step.solvable)

    def test_validation(self):
        with self.assertRaises(TypeError):
            agreement_filtration_events(object())


if __name__ == "__main__":
    unittest.main()
