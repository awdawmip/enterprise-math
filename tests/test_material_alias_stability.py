import unittest

from enterprise_math.material_alias_stability import (
    permanent_alias_stability,
    permanent_anisotropy_visibility_2d,
)
from enterprise_math.material_anisotropy_2d import anisotropic_material_profile_2d
from enterprise_math.material_anisotropy_visibility_2d import (
    kinematic_anisotropy_visibility_2d,
)
from enterprise_math.clearance_precision import (
    ACTIVE_COUNT,
    ACTIVE_SET,
    SCALAR_DEPTH,
)
from enterprise_math.material_response import explicit_material_curve_profile


def profile(samples, amplitude):
    values = tuple(samples)
    return explicit_material_curve_profile(values, values, amplitude)


class MaterialAliasStabilityTests(unittest.TestCase):
    def test_exact_permanent_threshold_can_precede_sufficient_min_gap_bound(self):
        report = permanent_alias_stability((2, 3, 5), amplitude=5)
        self.assertEqual(report.guaranteed_injective_budget, 5)
        self.assertEqual(report.last_noninjective_budget, 3)
        self.assertEqual(report.exact_permanent_injective_budget, 4)

    def test_reference_alias_pattern_is_nonmonotone_before_permanent_stability(self):
        from enterprise_math.material_response_aliasing import kinematic_response_partition

        counts = [
            kinematic_response_partition((2, 3, 5), budget, 5).class_count
            for budget in (1, 2, 3, 4, 5)
        ]
        self.assertEqual(counts, [2, 3, 2, 3, 3])

    def test_single_response_alphabet_is_permanently_injective_from_budget_zero(self):
        report = permanent_alias_stability((3, 3, 3), amplitude=5)
        self.assertEqual(report.responses, (3,))
        self.assertIsNone(report.guaranteed_injective_budget)
        self.assertIsNone(report.last_noninjective_budget)
        self.assertEqual(report.exact_permanent_injective_budget, 0)

    def test_budget_relative_anisotropy_can_toggle_before_exact_stability(self):
        anisotropic = anisotropic_material_profile_2d(
            profile((0, 2), 5),
            profile((0, 3), 5),
            profile((0, 5), 5),
        )
        observed = [
            kinematic_anisotropy_visibility_2d(
                anisotropic,
                collapse_factor=2,
                incoming_budget=budget,
            ).minimum_clearance_observable
            for budget in (1, 2, 3, 4, 5)
        ]
        self.assertEqual(
            observed,
            [ACTIVE_COUNT, ACTIVE_SET, ACTIVE_COUNT, ACTIVE_SET, ACTIVE_SET],
        )
        stability = permanent_anisotropy_visibility_2d(anisotropic, 2)
        self.assertEqual(
            stability.reachable_raw_minimum_clearance_observable,
            ACTIVE_SET,
        )
        self.assertEqual(stability.guaranteed_response_injective_budget, 5)
        self.assertEqual(stability.last_budget_with_coarser_observable, 3)
        self.assertEqual(stability.exact_permanent_observable_budget, 4)

    def test_unreachable_deeper_anisotropy_does_not_force_current_precision(self):
        anisotropic = anisotropic_material_profile_2d(
            profile((0, 1, 2, 3), 5),
            profile((0, 1, 4, 4), 5),
            profile((0, 1, 5, 5), 5),
        )
        shallow = permanent_anisotropy_visibility_2d(
            anisotropic,
            collapse_factor=2,
        )
        self.assertEqual(shallow.represented_max_depth, 1)
        self.assertEqual(
            shallow.reachable_raw_minimum_clearance_observable,
            SCALAR_DEPTH,
        )
        self.assertEqual(shallow.exact_permanent_observable_budget, 0)
        self.assertIsNone(shallow.last_budget_with_coarser_observable)

        deeper = permanent_anisotropy_visibility_2d(
            anisotropic,
            collapse_factor=3,
        )
        self.assertEqual(deeper.represented_max_depth, 2)
        self.assertEqual(
            deeper.reachable_raw_minimum_clearance_observable,
            ACTIVE_SET,
        )

    def test_corner_only_reachable_difference_stabilizes_at_active_count(self):
        anisotropic = anisotropic_material_profile_2d(
            profile((0, 2), 5),
            profile((0, 2), 5),
            profile((0, 5), 5),
        )
        stability = permanent_anisotropy_visibility_2d(anisotropic, 2)
        self.assertEqual(
            stability.reachable_raw_minimum_clearance_observable,
            ACTIVE_COUNT,
        )
        for budget in range(stability.exact_permanent_observable_budget, 12):
            self.assertEqual(
                kinematic_anisotropy_visibility_2d(
                    anisotropic, 2, budget
                ).minimum_clearance_observable,
                ACTIVE_COUNT,
            )

    def test_invalid_alias_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            permanent_alias_stability((), 5)
        with self.assertRaises(ValueError):
            permanent_alias_stability((1, 6), 5)
        anisotropic = anisotropic_material_profile_2d(
            profile((0, 1), 2),
            profile((0, 1), 2),
            profile((0, 1), 2),
        )
        with self.assertRaises(ValueError):
            permanent_anisotropy_visibility_2d(anisotropic, 0)


if __name__ == "__main__":
    unittest.main()
