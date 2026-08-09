import unittest
from itertools import permutations

from enterprise_math.material_impulse_coupling import project_material_impulse
from enterprise_math.material_momentum_lattice_bridge import (
    DeclaredImpulseFraction,
    LiftedMomentumCoordinate,
    apply_fractional_impulse_exact,
    apply_fractional_impulses_exact,
    material_amplitude_lattice_is_sufficient,
    material_response_impulse_fraction,
    minimum_common_momentum_denominator,
    refine_lifted_momentum,
)


class MaterialMomentumLatticeBridgeTests(unittest.TestCase):
    def test_dividing_impulse_denominator_needs_no_refinement(self):
        momentum = LiftedMomentumCoordinate(17, 12)
        report = apply_fractional_impulse_exact(
            momentum,
            DeclaredImpulseFraction(5, 3),
        )
        self.assertEqual(report.common_denominator, 12)
        self.assertFalse(report.denominator_refined)
        self.assertEqual(report.refined_impulse_numerator, 20)
        self.assertEqual(report.after, LiftedMomentumCoordinate(37, 12))

    def test_noncoprime_denominators_refine_to_exact_lcm_not_product(self):
        momentum = LiftedMomentumCoordinate(7, 6)
        report = apply_fractional_impulse_exact(
            momentum,
            DeclaredImpulseFraction(-5, 4),
        )
        self.assertEqual(report.common_denominator, 12)
        self.assertEqual(report.refined_momentum_numerator, 14)
        self.assertEqual(report.refined_impulse_numerator, -15)
        self.assertEqual(report.after, LiftedMomentumCoordinate(-1, 12))

    def test_three_way_common_denominator_is_unique_least_divisibility_refinement(self):
        self.assertEqual(
            minimum_common_momentum_denominator(4, [3, 10, 6]),
            60,
        )
        momentum = LiftedMomentumCoordinate(5, 4)
        refined = refine_lifted_momentum(momentum, 60)
        self.assertEqual(refined, LiftedMomentumCoordinate(75, 60))
        with self.assertRaises(ValueError):
            refine_lifted_momentum(momentum, 6)

    def test_many_exact_impulses_are_order_independent_on_common_lift(self):
        momentum = LiftedMomentumCoordinate(-7, 4)
        impulses = (
            DeclaredImpulseFraction(1, 3),
            DeclaredImpulseFraction(5, 6),
            DeclaredImpulseFraction(-7, 10),
        )
        outcomes = {
            apply_fractional_impulses_exact(momentum, order)
            for order in permutations(impulses)
        }
        self.assertEqual(len(outcomes), 1)
        result = outcomes.pop()
        self.assertEqual(result.denominator, 60)
        self.assertEqual(result.numerator, -77)

    def test_material_amplitude_is_already_a_compatible_momentum_denominator(self):
        for amplitude in range(1, 12):
            for response in range(amplitude + 1):
                for capacity in range(0, 9):
                    self.assertTrue(
                        material_amplitude_lattice_is_sufficient(
                            response, amplitude, capacity
                        )
                    )
                    impulse = material_response_impulse_fraction(
                        response, amplitude, capacity
                    )
                    self.assertEqual(amplitude % impulse.denominator, 0)

    def test_bridge_matches_existing_retained_material_impulse_accounting(self):
        # Existing #190 state: p=2 plus detail -1 on denominator A=5.
        amplitude = 5
        response = 3
        capacity = 4
        momentum = LiftedMomentumCoordinate(2 * amplitude - 1, amplitude)
        impulse = material_response_impulse_fraction(
            response, amplitude, capacity, direction_sign=1
        )
        bridged = apply_fractional_impulse_exact(momentum, impulse).after

        old = project_material_impulse(
            response_sample=response,
            response_amplitude=amplitude,
            max_impulse_per_tick=capacity,
            outward_sign=1,
            incoming_detail_numerator=-1,
            retain_detail=True,
        )
        old_after = LiftedMomentumCoordinate(
            amplitude * (2 + old.impulse_quanta) + old.next_detail_numerator,
            amplitude,
        )
        self.assertEqual(bridged, old_after)
        self.assertEqual(bridged.whole_and_detail, (4, 1))

    def test_branching_star_denominator_can_be_physically_carried_after_lcm_lift(self):
        # q=1,k=3 symmetry research admits one-third contact impulses at s=3.
        # A material/momentum state currently on denominator 4 must lift to 12;
        # three symmetric 1/3 impulses then sum to one exact coarse momentum unit.
        momentum = LiftedMomentumCoordinate(0, 4)
        third = DeclaredImpulseFraction(1, 3)
        one = apply_fractional_impulses_exact(momentum, (third, third, third))
        self.assertEqual(one, LiftedMomentumCoordinate(12, 12))
        self.assertEqual(one.whole_and_detail, (1, 0))

    def test_invalid_denominators_and_samples_are_rejected(self):
        with self.assertRaises(ValueError):
            LiftedMomentumCoordinate(1, 0)
        with self.assertRaises(ValueError):
            DeclaredImpulseFraction(1, 0)
        with self.assertRaises(ValueError):
            material_response_impulse_fraction(3, 2, 1)
        with self.assertRaises(ValueError):
            material_response_impulse_fraction(1, 2, -1)


if __name__ == "__main__":
    unittest.main()
