import unittest

from enterprise_math.material_measurement import (
    FiniteMaterialDataset,
    FiniteMeasurementAxis,
)
from enterprise_math.material_stress_strain_hysteresis import (
    measured_branch_trapezoid_area,
    measured_hysteresis_report,
)


class MaterialStressStrainHysteresisTests(unittest.TestCase):
    def setUp(self):
        self.strain = FiniteMeasurementAxis(
            name="engineering_strain",
            unit="1",
            scale_factor=1000,
            lower_count=0,
            upper_count=1000,
        )
        self.stress = FiniteMeasurementAxis(
            name="engineering_stress",
            unit="kPa",
            scale_factor=10,
            lower_count=-100,
            upper_count=100,
        )

    def dataset(self, source, deformations, responses):
        return FiniteMaterialDataset(
            deformation_axis=self.strain,
            response_axis=self.stress,
            deformations=tuple(deformations),
            responses=tuple(responses),
            source_id=source,
        )

    def test_irregular_loading_and_decreasing_returning_grids_integrate_exactly(self):
        loading = self.dataset("load", (0, 100, 300), (0, 20, 40))
        returning = self.dataset("return", (300, 100, 0), (20, 10, 0))
        load = measured_branch_trapezoid_area(loading)
        ret = measured_branch_trapezoid_area(returning)
        self.assertEqual(load.doubled_area_numerator, 14000)
        self.assertEqual(ret.doubled_area_numerator, 7000)
        self.assertTrue(load.input_was_increasing)
        self.assertFalse(ret.input_was_increasing)
        report = measured_hysteresis_report(loading, returning)
        self.assertEqual(report.doubled_loss_numerator, 7000)
        self.assertEqual(
            (report.relative_loss.numerator, report.relative_loss.denominator),
            (1, 2),
        )
        self.assertTrue(report.closed_deformation_interval)

    def test_interior_branch_grids_need_not_match(self):
        loading = self.dataset("load", (0, 100, 300), (0, 20, 40))
        returning = self.dataset("return", (300, 250, 50, 0), (20, 18, 4, 0))
        report = measured_hysteresis_report(loading, returning)
        self.assertTrue(report.closed_deformation_interval)
        self.assertEqual(report.loading.deformation_lower_count, 0)
        self.assertEqual(report.returning.deformation_upper_count, 300)

    def test_negative_compression_sign_can_be_normalized_explicitly(self):
        loading = self.dataset("load", (0, 100, 300), (0, -20, -40))
        returning = self.dataset("return", (300, 100, 0), (-20, -10, 0))
        report = measured_hysteresis_report(loading, returning, response_sign=-1)
        self.assertEqual(report.doubled_loss_numerator, 7000)
        self.assertEqual(
            (report.relative_loss.numerator, report.relative_loss.denominator),
            (1, 2),
        )

    def test_product_coordinate_keeps_declared_measurement_scales(self):
        loading = self.dataset("load", (0, 100, 300), (0, 20, 40))
        area = measured_branch_trapezoid_area(loading)
        # area2=14000 and denominator 2*1000*10=20000 -> 7/10 kPa.
        self.assertEqual((area.exact_area.numerator, area.exact_area.denominator), (7, 10))
        self.assertEqual(area.product_unit, "kPa*1")

    def test_endpoint_mismatch_is_explicit_and_can_only_be_allowed_as_open_branch_comparison(self):
        loading = self.dataset("load", (0, 100, 300), (0, 20, 40))
        returning = self.dataset("return", (300, 100, 20), (20, 10, 1))
        with self.assertRaises(ValueError):
            measured_hysteresis_report(loading, returning)
        open_report = measured_hysteresis_report(
            loading,
            returning,
            require_closed_deformation_interval=False,
        )
        self.assertFalse(open_report.closed_deformation_interval)

    def test_nonmonotone_branch_is_rejected_without_sorting_or_interpolation(self):
        branch = self.dataset("bad", (0, 300, 100), (0, 40, 20))
        with self.assertRaises(ValueError):
            measured_branch_trapezoid_area(branch)

    def test_response_axis_or_deformation_axis_mismatch_is_rejected(self):
        loading = self.dataset("load", (0, 100, 300), (0, 20, 40))
        other_stress = FiniteMeasurementAxis(
            name="engineering_stress",
            unit="MPa",
            scale_factor=1000,
            lower_count=-100,
            upper_count=100,
        )
        returning = FiniteMaterialDataset(
            deformation_axis=self.strain,
            response_axis=other_stress,
            deformations=(300, 100, 0),
            responses=(20, 10, 0),
            source_id="return",
        )
        with self.assertRaises(ValueError):
            measured_hysteresis_report(loading, returning)

    def test_zero_or_negative_loading_area_cannot_define_relative_loss(self):
        zero = self.dataset("zero", (0, 100), (0, 0))
        with self.assertRaises(ValueError):
            measured_hysteresis_report(zero, zero)


if __name__ == "__main__":
    unittest.main()
