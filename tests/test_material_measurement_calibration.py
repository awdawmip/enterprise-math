import unittest

from enterprise_math.material_measurement import (
    FiniteMaterialDataset,
    FiniteMeasurementAxis,
)
from enterprise_math.material_measurement_calibration import (
    assemble_calibrated_empirical_profile,
    calibrate_measurement_branch,
    calibrate_response_count,
    response_calibration_from_axis,
)


class MaterialMeasurementCalibrationTests(unittest.TestCase):
    def setUp(self):
        self.deformation_axis = FiniteMeasurementAxis(
            name="stretch",
            unit="ratio_x1000",
            scale_factor=1000,
            lower_count=1000,
            upper_count=2000,
        )
        self.response_axis = FiniteMeasurementAxis(
            name="stress",
            unit="kPa",
            scale_factor=10,
            lower_count=100,
            upper_count=500,
        )
        self.calibration = response_calibration_from_axis(
            self.response_axis,
            model_amplitude=1000,
            lower_response_count=100,
            upper_response_count=500,
        )

    def dataset(self, source_id, responses, deformations=(1000, 1250, 1500, 1750, 2000)):
        return FiniteMaterialDataset(
            deformation_axis=self.deformation_axis,
            response_axis=self.response_axis,
            deformations=tuple(deformations),
            responses=tuple(responses),
            source_id=source_id,
        )

    def test_endpoints_map_exactly_and_detail_is_bounded(self):
        lower = calibrate_response_count(100, self.calibration)
        upper = calibrate_response_count(500, self.calibration)
        self.assertEqual((lower.model_sample, lower.doubled_projection_detail), (0, 0))
        self.assertEqual((upper.model_sample, upper.doubled_projection_detail), (1000, 0))
        span = 400
        for count in range(100, 501):
            report = calibrate_response_count(count, self.calibration)
            self.assertTrue(-span <= report.doubled_projection_detail < span)
            self.assertTrue(0 <= report.model_sample <= 1000)

    def test_nearest_projection_reconstructs_exact_doubled_accounting(self):
        span = 400
        for count in range(100, 501):
            report = calibrate_response_count(count, self.calibration)
            offset = count - 100
            self.assertEqual(
                2 * offset * 1000,
                2 * span * report.model_sample + report.doubled_projection_detail,
            )

    def test_measurement_unit_and_scale_must_match_calibration_provenance(self):
        dataset = self.dataset("load", (100, 180, 260, 360, 500))
        branch = calibrate_measurement_branch(dataset, self.calibration)
        self.assertEqual(branch.source_id, "load")
        self.assertEqual(branch.model_samples[0], 0)
        self.assertEqual(branch.model_samples[-1], 1000)

        incompatible_axis = FiniteMeasurementAxis(
            name="stress",
            unit="MPa",
            scale_factor=1000,
            lower_count=100,
            upper_count=500,
        )
        incompatible = FiniteMaterialDataset(
            deformation_axis=self.deformation_axis,
            response_axis=incompatible_axis,
            deformations=dataset.deformations,
            responses=dataset.responses,
            source_id="bad",
        )
        with self.assertRaises(ValueError):
            calibrate_measurement_branch(incompatible, self.calibration)

    def test_two_explicit_branches_assemble_only_on_same_grid_and_calibration(self):
        loading = calibrate_measurement_branch(
            self.dataset("loading", (100, 180, 260, 360, 500)),
            self.calibration,
        )
        returning = calibrate_measurement_branch(
            self.dataset("returning", (100, 150, 220, 300, 400)),
            self.calibration,
        )
        assembly = assemble_calibrated_empirical_profile(loading, returning)
        self.assertEqual(assembly.loading_source_id, "loading")
        self.assertEqual(assembly.returning_source_id, "returning")
        self.assertEqual(assembly.profile.amplitude, 1000)
        self.assertEqual(assembly.profile.loading, loading.model_samples)
        self.assertEqual(assembly.profile.returning, returning.model_samples)

        shifted = calibrate_measurement_branch(
            self.dataset(
                "shifted-return",
                (100, 150, 220, 300, 400),
                deformations=(1000, 1200, 1500, 1800, 2000),
            ),
            self.calibration,
        )
        with self.assertRaises(ValueError):
            assemble_calibrated_empirical_profile(loading, shifted)

    def test_calibration_domain_is_frozen_and_no_extrapolation_occurs(self):
        with self.assertRaises(ValueError):
            calibrate_response_count(99, self.calibration)
        with self.assertRaises(ValueError):
            calibrate_response_count(501, self.calibration)
        with self.assertRaises(ValueError):
            response_calibration_from_axis(
                self.response_axis,
                1000,
                lower_response_count=50,
                upper_response_count=500,
            )

    def test_calibration_does_not_reuse_measurement_scale_as_model_amplitude(self):
        self.assertEqual(self.response_axis.scale_factor, 10)
        self.assertEqual(self.calibration.model_amplitude, 1000)
        self.assertNotEqual(
            self.response_axis.scale_factor,
            self.calibration.model_amplitude,
        )


if __name__ == "__main__":
    unittest.main()
