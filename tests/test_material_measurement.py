import unittest

from enterprise_math.material_measurement import (
    FiniteMaterialDataset,
    FiniteMeasurementAxis,
    model_precision_is_independent,
)


class MaterialMeasurementTests(unittest.TestCase):
    def test_exact_measurement_reduces_without_float(self):
        axis = FiniteMeasurementAxis("stretch", "1", 100, 100, 761)
        value = axis.exact_value(250)
        self.assertEqual((value.numerator, value.denominator, value.unit), (5, 2, "1"))

    def test_dataset_keeps_observation_scale_separate_from_model_precision(self):
        deformation = FiniteMeasurementAxis("stretch", "1", 100, 100, 761)
        response = FiniteMeasurementAxis("pk1", "source-pk1-unit", 100, 0, 630)
        dataset = FiniteMaterialDataset(
            deformation,
            response,
            (100, 250, 761),
            (0, 100, 630),
            "SRC-TRELOAR-1944-RUBBER",
        )
        self.assertEqual(dataset.observation_count, 3)
        self.assertEqual(dataset.deformation_axis.scale_factor, 100)
        self.assertTrue(model_precision_is_independent(dataset, 64))
        self.assertTrue(model_precision_is_independent(dataset, 8192))

    def test_signed_axes_are_allowed_but_bounds_are_enforced(self):
        axis = FiniteMeasurementAxis("signed-response", "u", 10, -20, 20)
        self.assertTrue(axis.contains(-7))
        self.assertEqual(axis.exact_value(-15).numerator, -3)
        self.assertEqual(axis.exact_value(-15).denominator, 2)
        with self.assertRaises(ValueError):
            axis.exact_value(21)

    def test_invalid_dataset_observation_is_rejected(self):
        deformation = FiniteMeasurementAxis("x", "u", 1, 0, 10)
        response = FiniteMeasurementAxis("y", "v", 1, 0, 10)
        with self.assertRaises(ValueError):
            FiniteMaterialDataset(deformation, response, (0, 11), (0, 1), "SRC-X")


if __name__ == "__main__":
    unittest.main()
