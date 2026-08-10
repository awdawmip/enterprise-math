import unittest

from enterprise_math.integer_dynamic_affine_agreement import (
    dynamic_affine_exact_agreement_report,
    dynamic_affine_modular_agreement_report,
)
from enterprise_math.integer_dynamic_affine_agreement_horizon import (
    dynamic_affine_agreement_horizon_report,
)


def translate_minus_one_action():
    return ((((1,),), (-1,)),)


def identity_affine_action():
    return ((((1,),), (0,)),)


class IntegerDynamicAffineAgreementLocalGlobalBridgeTests(unittest.TestCase):
    def test_future_depth_and_modulus_are_independent_requirements(self):
        actions = translate_minus_one_action()

        exact_horizon = dynamic_affine_agreement_horizon_report(
            actions,
            ((2,),),
            (2,),
            actions,
            ((0,),),
            (0,),
        )
        exact_steps = {step.horizon: step for step in exact_horizon.steps}
        self.assertTrue(exact_steps[0].solvable)
        self.assertFalse(exact_steps[1].solvable)

        mod2 = dynamic_affine_agreement_horizon_report(
            actions,
            ((2,),),
            (2,),
            actions,
            ((0,),),
            (0,),
            modulus=2,
        )
        mod2_steps = {step.horizon: step for step in mod2.steps}
        self.assertTrue(mod2_steps[0].solvable)
        # Even after the future equation has appeared, mod2 is too coarse: both
        # 2x+2 and 2x collapse to 0=0.
        self.assertTrue(mod2_steps[1].solvable)
        self.assertEqual(mod2_steps[1].modular_agreement_state_count, 2)

        mod4 = dynamic_affine_agreement_horizon_report(
            actions,
            ((2,),),
            (2,),
            actions,
            ((0,),),
            (0,),
            modulus=4,
        )
        mod4_steps = {step.horizon: step for step in mod4.steps}
        self.assertTrue(mod4_steps[0].solvable)
        self.assertFalse(mod4_steps[1].solvable)
        self.assertEqual(mod4_steps[1].modular_agreement_state_count, 0)

    def test_mod_four_is_the_sharp_small_certificate_on_reference_pair(self):
        actions = translate_minus_one_action()
        exact = dynamic_affine_exact_agreement_report(
            actions,
            ((2,),),
            (2,),
            actions,
            ((0,),),
            (0,),
        )
        self.assertFalse(exact.solvable)

        mod2 = dynamic_affine_modular_agreement_report(
            actions,
            ((2,),),
            (2,),
            actions,
            ((0,),),
            (0,),
            2,
        )
        self.assertTrue(mod2.solvable)

        mod4 = dynamic_affine_modular_agreement_report(
            actions,
            ((2,),),
            (2,),
            actions,
            ((0,),),
            (0,),
            4,
        )
        self.assertFalse(mod4.solvable)

    def test_full_row_rank_scalar_constraint_has_uniform_mod_two_offset_certificate(self):
        actions = identity_affine_action()
        # Stabilized linear constraint is 2x=-c.  Its cokernel exponent is2, so
        # mod2 decides exact solvability for every scalar offset c.
        for constant in range(-8, 9):
            exact = dynamic_affine_exact_agreement_report(
                actions,
                ((2,),),
                (constant,),
                actions,
                ((0,),),
                (0,),
            )
            modular = dynamic_affine_modular_agreement_report(
                actions,
                ((2,),),
                (constant,),
                actions,
                ((0,),),
                (0,),
                2,
            )
            self.assertEqual(exact.solvable, modular.solvable, constant)

    def test_fiber_count_remains_separate_after_image_certificate(self):
        actions = identity_affine_action()
        # x+y+1=0 has exact agreement and one free direction; modulo5 the
        # nonempty agreement coset contains five states.
        two_dimensional_actions = (
            (
                ((1, 0), (0, 1)),
                (0, 0),
            ),
        )
        exact = dynamic_affine_exact_agreement_report(
            two_dimensional_actions,
            ((1, 1),),
            (1,),
            two_dimensional_actions,
            ((0, 0),),
            (0,),
        )
        self.assertTrue(exact.solvable)
        self.assertEqual(exact.agreement_free_rank, 1)

        modular = dynamic_affine_modular_agreement_report(
            two_dimensional_actions,
            ((1, 1),),
            (1,),
            two_dimensional_actions,
            ((0, 0),),
            (0,),
            5,
        )
        self.assertTrue(modular.solvable)
        self.assertEqual(modular.agreement_state_count, 5)
        self.assertEqual(modular.total_state_count, 25)


if __name__ == "__main__":
    unittest.main()
