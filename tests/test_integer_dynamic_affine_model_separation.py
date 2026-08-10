import unittest

from enterprise_math.integer_dynamic_affine_model_separation import (
    dynamic_affine_difference_content,
    dynamic_affine_difference_module_basis,
    dynamic_affine_model_separation_horizon_report,
    dynamic_affine_model_separation_report,
    dynamic_affine_models_indistinguishable_modulus,
    homogeneous_affine_action,
    homogeneous_affine_observation_rows,
)


class IntegerDynamicAffineModelSeparationTests(unittest.TestCase):
    def test_homogeneous_compilers(self):
        self.assertEqual(
            homogeneous_affine_action(
                ((2, 1), (0, 3)),
                (5, -2),
            ),
            (
                (2, 1, 5),
                (0, 3, -2),
                (0, 0, 1),
            ),
        )
        self.assertEqual(
            homogeneous_affine_observation_rows(
                ((1, 2), (3, 4)),
                (7, -1),
            ),
            ((1, 2, 7), (3, 4, -1)),
        )

    def test_same_linear_dynamics_but_plus_six_drift_has_dynamic_content_six(self):
        left_actions = (
            (((1,),), (0,)),
        )
        right_actions = (
            (((1,),), (6,)),
        )
        observation = ((1,),)
        offset = (0,)
        self.assertEqual(
            dynamic_affine_difference_content(
                left_actions,
                observation,
                offset,
                right_actions,
                observation,
                offset,
            ),
            6,
        )
        for modulus in range(1, 10):
            self.assertEqual(
                dynamic_affine_models_indistinguishable_modulus(
                    left_actions,
                    observation,
                    offset,
                    right_actions,
                    observation,
                    offset,
                    modulus,
                ),
                6 % modulus == 0,
            )

    def test_affine_drift_first_appears_at_future_horizon_one(self):
        left_actions = ((((1,),), (0,)),)
        right_actions = ((((1,),), (6,)),)
        report = dynamic_affine_model_separation_horizon_report(
            left_actions,
            ((1,),),
            (0,),
            right_actions,
            ((1,),),
            (0,),
        )
        by_horizon = {step.horizon: step for step in report.steps}
        self.assertEqual(by_horizon[0].difference_content, 0)
        self.assertEqual(by_horizon[1].difference_content, 6)
        self.assertEqual(report.first_distinguishing_horizon(4), 1)
        self.assertIsNone(report.first_distinguishing_horizon(2))
        self.assertIsNone(report.first_distinguishing_horizon(3))

    def test_observation_offset_difference_is_visible_at_horizon_zero(self):
        actions = ((((1,),), (0,)),)
        report = dynamic_affine_model_separation_horizon_report(
            actions,
            ((1,),),
            (0,),
            actions,
            ((1,),),
            (10,),
        )
        self.assertEqual(report.steps[0].difference_content, 10)
        self.assertEqual(report.first_distinguishing_horizon(4), 0)
        self.assertIsNone(report.first_distinguishing_horizon(2))
        self.assertIsNone(report.first_distinguishing_horizon(5))

    def test_internal_affine_difference_can_be_exactly_unobservable_forever(self):
        # Observation sees x1 only.  Models differ only by a translation in x2,
        # and neither action couples x2 back into x1.
        left_actions = (
            (
                ((1, 0), (0, 1)),
                (0, 0),
            ),
        )
        right_actions = (
            (
                ((1, 0), (0, 1)),
                (0, 7),
            ),
        )
        report = dynamic_affine_model_separation_report(
            left_actions,
            ((1, 0),),
            (0,),
            right_actions,
            ((1, 0),),
            (0,),
        )
        self.assertTrue(report.exactly_future_equivalent)
        self.assertEqual(report.difference_module_basis, ())
        self.assertEqual(report.difference_content, 0)

    def test_hidden_offset_becomes_visible_when_future_linear_action_couples_coordinate(self):
        # x2 translation is initially hidden from observation x1.  A future
        # action copies x2 into x1, so the same offset difference becomes visible.
        left_actions = (
            (
                ((0, 1), (0, 0)),
                (0, 0),
            ),
            (
                ((1, 0), (0, 1)),
                (0, 0),
            ),
        )
        right_actions = (
            (
                ((0, 1), (0, 0)),
                (0, 0),
            ),
            (
                ((1, 0), (0, 1)),
                (0, 6),
            ),
        )
        report = dynamic_affine_model_separation_horizon_report(
            left_actions,
            ((1, 0),),
            (0,),
            right_actions,
            ((1, 0),),
            (0,),
        )
        self.assertEqual(report.steps[0].difference_content, 0)
        self.assertEqual(report.steps[1].difference_content, 0)
        # Word: translate hidden x2, then copy x2 into x1.
        self.assertEqual(report.first_distinguishing_horizon(4), 2)
        self.assertEqual(report.final_difference_content, 6)

    def test_module_basis_contains_state_and_constant_affine_difference_coefficients(self):
        left_actions = ((((1,),), (0,)),)
        right_actions = ((((2,),), (3,)),)
        basis = dynamic_affine_difference_module_basis(
            left_actions,
            ((1,),),
            (0,),
            right_actions,
            ((1,),),
            (0,),
        )
        self.assertTrue(basis)
        # Homogeneous state dimension is two: coefficient of x and constant 1.
        self.assertTrue(all(len(row) == 2 for row in basis))

    def test_validation(self):
        with self.assertRaises(ValueError):
            homogeneous_affine_action(((1, 0),), (0,))
        with self.assertRaises(ValueError):
            homogeneous_affine_action(((1,),), ())
        with self.assertRaises(ValueError):
            homogeneous_affine_observation_rows(((1,),), ())


if __name__ == "__main__":
    unittest.main()
