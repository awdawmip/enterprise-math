import unittest

from enterprise_math.material_force_work import FiniteForceLaw, uniform_force_law
from enterprise_math.material_response import explicit_material_curve_profile
from enterprise_math.material_work_energy_oracle import (
    EXACT_TURN,
    MATERIAL_UNDERRESOLVED,
    TURN_UNDERRESOLVED,
    loading_work_prefix_numerators2,
    material_turning_report,
    static_material_rebound_report,
)


class MaterialWorkEnergyOracleTests(unittest.TestCase):
    def setUp(self):
        self.law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 2, 4),
                returning=(0, 1, 2),
                amplitude=4,
            )
        )

    def test_loading_work_prefixes_are_exact_integer_energy_thresholds(self):
        self.assertEqual(loading_work_prefix_numerators2(self.law), (0, 2, 8))

    def test_exact_turn_derives_outgoing_energy_from_return_branch_without_restitution_parameter(self):
        report = static_material_rebound_report(self.law, 8)
        self.assertEqual(report.turning.status, EXACT_TURN)
        self.assertEqual(report.turning.exact_turn_depth, 2)
        self.assertEqual(report.loading_work_numerator2, 8)
        self.assertEqual(report.returning_work_numerator2, 4)
        self.assertEqual(report.dissipated_work_numerator2, 4)
        self.assertEqual(report.outgoing_work_resource_numerator2, 4)
        self.assertTrue(report.passive_at_turn)
        self.assertEqual(
            (report.retention_ratio_numerator, report.retention_ratio_denominator),
            (1, 2),
        )

    def test_energy_between_material_grid_work_levels_is_explicitly_underresolved(self):
        turn = material_turning_report(self.law, 5)
        self.assertEqual(turn.status, TURN_UNDERRESOLVED)
        self.assertEqual(turn.lower_represented_depth, 1)
        self.assertEqual(turn.upper_represented_depth, 2)
        self.assertEqual(turn.lower_loading_work_numerator2, 2)
        self.assertEqual(turn.upper_loading_work_numerator2, 8)
        rebound = static_material_rebound_report(self.law, 5)
        self.assertIsNone(rebound.outgoing_work_resource_numerator2)

    def test_energy_beyond_finite_material_domain_is_not_clamped(self):
        turn = material_turning_report(self.law, 9)
        self.assertEqual(turn.status, MATERIAL_UNDERRESOLVED)
        self.assertEqual(turn.lower_represented_depth, 2)
        self.assertEqual(turn.deepest_loading_work_numerator2, 8)
        self.assertIsNone(static_material_rebound_report(self.law, 9).outgoing_work_resource_numerator2)

    def test_exact_elastic_curve_returns_all_work_resource(self):
        elastic = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 3, 7), returning=(0, 3, 7), amplitude=7
            )
        )
        energy = loading_work_prefix_numerators2(elastic)[2]
        report = static_material_rebound_report(elastic, energy)
        self.assertEqual(report.outgoing_work_resource_numerator2, energy)
        self.assertEqual(report.dissipated_work_numerator2, 0)
        self.assertEqual(
            (report.retention_ratio_numerator, report.retention_ratio_denominator),
            (1, 1),
        )

    def test_zero_energy_turns_at_zero_deformation(self):
        report = static_material_rebound_report(self.law, 0)
        self.assertEqual(report.turning.status, EXACT_TURN)
        self.assertEqual(report.turning.exact_turn_depth, 0)
        self.assertEqual(report.outgoing_work_resource_numerator2, 0)
        self.assertEqual(
            (report.retention_ratio_numerator, report.retention_ratio_denominator),
            (0, 1),
        )

    def test_irregular_grid_changes_energy_thresholds_exactly(self):
        profile = explicit_material_curve_profile(
            loading=(0, 2, 4), returning=(0, 1, 2), amplitude=4
        )
        law = FiniteForceLaw(
            profile=profile,
            deformation_counts=(0, 2, 5),
            force_scale_factor=1,
            force_unit="F",
            deformation_scale_factor=1,
            deformation_unit="x",
        )
        self.assertEqual(loading_work_prefix_numerators2(law), (0, 4, 22))
        self.assertEqual(material_turning_report(law, 10).status, TURN_UNDERRESOLVED)
        self.assertEqual(material_turning_report(law, 22).status, EXACT_TURN)

    def test_nonpassive_return_branch_is_reported_not_silently_clamped(self):
        active = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 2), returning=(0, 4), amplitude=4
            )
        )
        energy = loading_work_prefix_numerators2(active)[1]
        report = static_material_rebound_report(active, energy)
        self.assertFalse(report.passive_at_turn)
        self.assertGreater(
            report.outgoing_work_resource_numerator2,
            report.loading_work_numerator2,
        )

    def test_negative_energy_resource_is_rejected(self):
        with self.assertRaises(ValueError):
            material_turning_report(self.law, -1)


if __name__ == "__main__":
    unittest.main()
