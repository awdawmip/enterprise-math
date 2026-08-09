import unittest

from enterprise_math.material_force_work import (
    DISSIPATIVE_REVERSAL,
    ELASTIC_REVERSAL,
    SLOWING,
    STOP,
    SUPERELASTIC_REVERSAL,
    FiniteForceLaw,
    first_force_passivity_violation,
    force_cycle_work_prefixes,
    force_cycle_work_report,
    force_law_is_cumulatively_passive,
    opposing_impulse_kinetic_report,
    uniform_force_law,
)
from enterprise_math.material_response import explicit_material_curve_profile


class MaterialForceWorkTests(unittest.TestCase):
    def test_uniform_grid_uses_explicit_two_endpoint_work_not_plain_sample_sum(self):
        profile = explicit_material_curve_profile(
            loading=(0, 2, 4, 6),
            returning=(0, 1, 3, 5),
            amplitude=6,
        )
        law = uniform_force_law(profile)
        report = force_cycle_work_report(law, 3)
        self.assertEqual(report.loading_work_numerator2, 18)
        self.assertEqual(report.returned_work_numerator2, 13)
        self.assertEqual(report.dissipated_work_numerator2, 5)
        self.assertTrue(report.passive)
        # With unit count scales, W_loss=5/2 in the declared work unit.
        self.assertEqual((report.dissipated_work.numerator, report.dissipated_work.denominator), (5, 2))

    def test_irregular_grid_widths_change_work_exactly(self):
        profile = explicit_material_curve_profile(
            loading=(0, 2, 4),
            returning=(0, 1, 2),
            amplitude=4,
        )
        irregular = FiniteForceLaw(
            profile=profile,
            deformation_counts=(0, 1, 3),
            force_scale_factor=1,
            force_unit="F",
            deformation_scale_factor=1,
            deformation_unit="x",
        )
        uniform = uniform_force_law(profile, force_unit="F", deformation_unit="x")
        ir = force_cycle_work_report(irregular, 2)
        un = force_cycle_work_report(uniform, 2)
        self.assertEqual(ir.loading_work_numerator2, 14)
        self.assertEqual(ir.returned_work_numerator2, 7)
        self.assertEqual(ir.dissipated_work_numerator2, 7)
        self.assertNotEqual(ir.loading_work_numerator2, un.loading_work_numerator2)

    def test_measurement_scales_give_exact_rational_work_coordinate(self):
        profile = explicit_material_curve_profile(
            loading=(0, 2, 4, 6),
            returning=(0, 1, 3, 5),
            amplitude=6,
        )
        law = FiniteForceLaw(
            profile=profile,
            deformation_counts=(0, 10, 20, 30),
            force_scale_factor=10,
            force_unit="N",
            deformation_scale_factor=1000,
            deformation_unit="m",
        )
        report = force_cycle_work_report(law, 3)
        # loss numerator2 = 50; denominator = 2*10*1000 = 20000 -> 1/400 N*m.
        self.assertEqual(report.dissipated_work_numerator2, 50)
        self.assertEqual(
            (report.dissipated_work.numerator, report.dissipated_work.denominator),
            (1, 400),
        )
        self.assertEqual(report.dissipated_work.unit, "N*m")

    def test_cumulative_passivity_is_weaker_than_pointwise_return_below_loading(self):
        profile = explicit_material_curve_profile(
            loading=(0, 4, 2),
            returning=(0, 1, 3),
            amplitude=4,
        )
        law = uniform_force_law(profile)
        self.assertGreater(profile.returning[2], profile.loading[2])
        prefixes = force_cycle_work_prefixes(law)
        self.assertEqual([r.dissipated_work_numerator2 for r in prefixes], [0, 3, 5])
        self.assertTrue(force_law_is_cumulatively_passive(law))
        self.assertIsNone(first_force_passivity_violation(law))

    def test_first_cumulative_passivity_violation_is_explicit(self):
        profile = explicit_material_curve_profile(
            loading=(0, 2, 2),
            returning=(0, 1, 6),
            amplitude=6,
        )
        law = uniform_force_law(profile)
        violation = first_force_passivity_violation(law)
        self.assertIsNotNone(violation)
        self.assertEqual(violation.peak_depth, 2)
        self.assertEqual(violation.dissipated_work_numerator2, -2)
        self.assertFalse(force_law_is_cumulatively_passive(law))

    def test_force_law_rejects_hidden_nonuniform_or_invalid_grid(self):
        profile = explicit_material_curve_profile((0, 1, 2), (0, 1, 2), 2)
        with self.assertRaises(ValueError):
            FiniteForceLaw(profile, (0, 1), 1, "F", 1, "x")
        with self.assertRaises(ValueError):
            FiniteForceLaw(profile, (0, 1, 1), 1, "F", 1, "x")
        with self.assertRaises(ValueError):
            FiniteForceLaw(profile, (0, 2, 1), 1, "F", 1, "x")

    def test_opposing_impulse_five_phase_partition_and_exact_kinetic_identity(self):
        p = 5
        cases = (
            (1, SLOWING),
            (5, STOP),
            (6, DISSIPATIVE_REVERSAL),
            (10, ELASTIC_REVERSAL),
            (11, SUPERELASTIC_REVERSAL),
        )
        for impulse, phase in cases:
            report = opposing_impulse_kinetic_report(p, impulse)
            self.assertEqual(report.phase, phase)
            self.assertEqual(
                report.kinetic_numerator_change,
                impulse * (impulse - 2 * p),
            )
        self.assertLess(opposing_impulse_kinetic_report(p, 6).kinetic_numerator_after, p * p)
        self.assertEqual(opposing_impulse_kinetic_report(p, 10).kinetic_numerator_after, p * p)
        self.assertGreater(opposing_impulse_kinetic_report(p, 11).kinetic_numerator_after, p * p)


if __name__ == "__main__":
    unittest.main()
