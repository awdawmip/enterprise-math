import unittest

from enterprise_math.material_contact_capacity_feasibility import (
    BALANCED,
    OVERPOWERED,
    UNDERPOWERED,
    material_contact_capacity_feasibility,
    verify_capacity_feasibility_under_divisibility_refinement,
)
from enterprise_math.material_contact_capacity_physical import (
    exact_material_impulse_capacity,
)
from enterprise_math.material_physical_projection import ForceImpulseCountScale


def unit_scale():
    return ForceImpulseCountScale(
        force_scale_factor=1,
        time_scale_factor=1,
        momentum_scale_factor=1,
        tick_duration_count=1,
        force_unit="F",
        time_unit="T",
        momentum_unit="P",
    )


def exact_fraction(numerator: int, denominator: int):
    # r/A * Fmax with unit physical scales.
    return exact_material_impulse_capacity(
        response_sample=numerator,
        response_amplitude=denominator,
        full_scale_force_count=1,
        scale=unit_scale(),
    )


class MaterialContactCapacityFeasibilityTests(unittest.TestCase):
    def test_physically_underpowered_material_never_becomes_feasible_by_refinement(self):
        exact = exact_fraction(1, 4)  # C=1/4 < demand q/K=1/3.
        for denominator in range(1, 40):
            report = material_contact_capacity_feasibility(
                exact, closing_score=1, self_coupling=3, contact_denominator=denominator
            )
            self.assertEqual(report.strength_regime, UNDERPOWERED)
            self.assertLess(report.strength_cross_difference, 0)
            self.assertFalse(report.feasible)
            self.assertTrue(report.physically_underpowered)
            self.assertFalse(report.precision_caused_capacity_deficit)

    def test_exactly_balanced_strength_is_feasible_only_on_its_divisibility_sublattice(self):
        exact = exact_fraction(1, 3)  # C=demand=1/3.
        for denominator in range(1, 20):
            report = material_contact_capacity_feasibility(
                exact, 1, 3, denominator
            )
            self.assertEqual(report.strength_regime, BALANCED)
            self.assertEqual(report.balanced_exact_base_denominator, 3)
            self.assertEqual(report.feasible, denominator % 3 == 0)
            self.assertIsNone(report.exact_permanent_feasibility_denominator)

    def test_physically_stronger_material_can_still_look_too_weak_at_coarse_precision(self):
        exact = exact_fraction(1, 2)  # C=1/2 > demand=1/3.
        reports = [
            material_contact_capacity_feasibility(exact, 1, 3, denominator)
            for denominator in range(1, 7)
        ]
        self.assertEqual([item.strength_regime for item in reports], [OVERPOWERED] * 6)
        self.assertEqual([item.feasible for item in reports], [False, True, True, True, True, True])
        self.assertTrue(reports[0].precision_caused_capacity_deficit)
        self.assertEqual(reports[0].sufficient_eventual_feasibility_denominator, 3)
        self.assertEqual(reports[0].exact_permanent_feasibility_denominator, 2)

    def test_numerically_adjacent_denominators_can_reenter_capacity_deficit_before_permanent_region(self):
        # C=1/2 is physically stronger than demand 2/5, yet s=2 is feasible
        # and s=3 is not.  Numeric growth is not the refinement order.
        exact = exact_fraction(1, 2)
        reports = [
            material_contact_capacity_feasibility(exact, 2, 5, denominator)
            for denominator in range(1, 8)
        ]
        self.assertEqual(
            [item.feasible for item in reports],
            [False, True, False, True, True, True, True],
        )
        self.assertEqual(reports[0].strength_regime, OVERPOWERED)
        self.assertEqual(reports[0].sufficient_eventual_feasibility_denominator, 5)
        self.assertEqual(reports[0].exact_permanent_feasibility_denominator, 4)
        self.assertTrue(
            verify_capacity_feasibility_under_divisibility_refinement(
                exact, 2, 5, coarse_denominator=2, refinement_multiplier=2
            )
        )

    def test_true_divisibility_refinement_never_loses_a_feasible_material_response(self):
        examples = (
            (exact_fraction(1, 2), 1, 3),
            (exact_fraction(1, 2), 2, 5),
            (exact_fraction(3, 4), 2, 3),
            (exact_fraction(1, 3), 1, 3),
        )
        for exact, q, coupling in examples:
            for coarse in range(1, 10):
                for multiplier in (2, 3, 5):
                    self.assertTrue(
                        verify_capacity_feasibility_under_divisibility_refinement(
                            exact,
                            q,
                            coupling,
                            coarse,
                            multiplier,
                        )
                    )

    def test_integer_exact_capacity_can_be_permanently_feasible_from_denominator_one(self):
        exact = exact_material_impulse_capacity(
            response_sample=1,
            response_amplitude=1,
            full_scale_force_count=2,
            scale=unit_scale(),
        )
        report = material_contact_capacity_feasibility(exact, 1, 3, 1)
        self.assertEqual(report.strength_regime, OVERPOWERED)
        self.assertTrue(report.feasible)
        self.assertEqual(report.sufficient_eventual_feasibility_denominator, 1)
        self.assertEqual(report.exact_permanent_feasibility_denominator, 1)

    def test_invalid_contact_inputs_are_rejected(self):
        exact = exact_fraction(1, 2)
        with self.assertRaises(ValueError):
            material_contact_capacity_feasibility(exact, 0, 2, 1)
        with self.assertRaises(ValueError):
            material_contact_capacity_feasibility(exact, 1, 0, 1)
        with self.assertRaises(ValueError):
            material_contact_capacity_feasibility(exact, 1, 2, 0)


if __name__ == "__main__":
    unittest.main()
