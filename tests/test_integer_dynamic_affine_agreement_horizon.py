import unittest

from enterprise_math.integer_dynamic_affine_agreement_horizon import (
    dynamic_affine_agreement_horizon_report,
)


def translate_minus_one_action():
    return ((((1,),), (-1,)),)


class IntegerDynamicAffineAgreementHorizonTests(unittest.TestCase):
    def test_affine_consistency_can_destroy_agreement_without_changing_linear_kernel_rank(self):
        actions = translate_minus_one_action()
        report = dynamic_affine_agreement_horizon_report(
            actions,
            ((2,),),
            (2,),
            actions,
            ((0,),),
            (0,),
            modulus=4,
        )
        by_horizon = {step.horizon: step for step in report.steps}

        # h0: 2x+2=0 mod4 -> two odd residues.
        self.assertTrue(by_horizon[0].solvable)
        self.assertEqual(by_horizon[0].linear_rank, 1)
        self.assertEqual(by_horizon[0].linear_smith_factors, (2,))
        self.assertEqual(by_horizon[0].modular_agreement_state_count, 2)

        # h1 adds the future equation 2x=0 mod4.  Linear rank and Smith factor
        # remain the same, but the affine equation family becomes inconsistent.
        self.assertFalse(by_horizon[1].solvable)
        self.assertEqual(by_horizon[1].linear_rank, 1)
        self.assertEqual(by_horizon[1].linear_smith_factors, (2,))
        self.assertEqual(by_horizon[1].modular_agreement_state_count, 0)
        self.assertEqual(report.first_empty_agreement_horizon, 1)

    def test_exact_integer_agreement_coset_can_also_disappear_by_future_offset_constraint(self):
        actions = translate_minus_one_action()
        report = dynamic_affine_agreement_horizon_report(
            actions,
            ((2,),),
            (2,),
            actions,
            ((0,),),
            (0,),
        )
        by_horizon = {step.horizon: step for step in report.steps}
        self.assertTrue(by_horizon[0].solvable)   # x=-1
        self.assertEqual(by_horizon[0].exact_agreement_free_rank, 0)
        self.assertFalse(by_horizon[1].solvable)  # also demands x=0
        self.assertIsNone(by_horizon[1].exact_agreement_free_rank)
        self.assertEqual(report.first_empty_agreement_horizon, 1)

    def test_modular_agreement_counts_never_increase_with_horizon(self):
        actions = translate_minus_one_action()
        for modulus in range(1, 9):
            report = dynamic_affine_agreement_horizon_report(
                actions,
                ((2,),),
                (2,),
                actions,
                ((0,),),
                (0,),
                modulus=modulus,
            )
            counts = tuple(
                step.modular_agreement_state_count
                for step in report.steps
            )
            self.assertTrue(
                all(
                    left is not None and right is not None and left >= right
                    for left, right in zip(counts, counts[1:])
                )
            )

    def test_identical_affine_models_keep_full_agreement_every_horizon(self):
        actions = translate_minus_one_action()
        for modulus in (2, 3, 5):
            report = dynamic_affine_agreement_horizon_report(
                actions,
                ((1,),),
                (7,),
                actions,
                ((1,),),
                (7,),
                modulus=modulus,
            )
            self.assertIsNone(report.first_empty_agreement_horizon)
            self.assertTrue(
                all(
                    step.modular_agreement_state_count == modulus
                    for step in report.steps
                )
            )

    def test_validation(self):
        actions = translate_minus_one_action()
        with self.assertRaises(ValueError):
            dynamic_affine_agreement_horizon_report(
                actions,
                ((1,),),
                (0,),
                actions,
                ((1,),),
                (0,),
                modulus=0,
            )
        with self.assertRaises(TypeError):
            dynamic_affine_agreement_horizon_report(
                actions,
                ((1,),),
                (0,),
                actions,
                ((1,),),
                (0,),
                modulus=False,
            )


if __name__ == "__main__":
    unittest.main()
