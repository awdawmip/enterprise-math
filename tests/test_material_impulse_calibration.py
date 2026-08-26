import unittest

from enterprise_math.material_hysteresis import LOADING, RETURNING
from enterprise_math.material_impulse_calibration import (
    IMPULSE_CALIBRATED,
    IMPULSE_UNDERRESOLVED,
    MaterialImpulseKey,
    calibrated_material_impulse,
    explicit_impulse_calibration,
)


class MaterialImpulseCalibrationTests(unittest.TestCase):
    def test_depth_branch_and_response_all_remain_part_of_calibration_key(self):
        calibration = explicit_impulse_calibration(
            material_amplitude=100,
            impulse_entries={
                MaterialImpulseKey(1, LOADING, 20): 3,
                MaterialImpulseKey(2, LOADING, 20): 5,
                MaterialImpulseKey(1, RETURNING, 20): 2,
            },
        )
        self.assertEqual(
            calibrated_material_impulse(calibration, 1, LOADING, 20).impulse_count,
            3,
        )
        self.assertEqual(
            calibrated_material_impulse(calibration, 2, LOADING, 20).impulse_count,
            5,
        )
        self.assertEqual(
            calibrated_material_impulse(calibration, 1, RETURNING, 20).impulse_count,
            2,
        )

    def test_sparse_missing_material_state_is_explicitly_underresolved(self):
        calibration = explicit_impulse_calibration(
            100,
            {MaterialImpulseKey(1, LOADING, 20): 3},
        )
        outcome = calibrated_material_impulse(calibration, 2, LOADING, 40)
        self.assertEqual(outcome.status, IMPULSE_UNDERRESOLVED)
        self.assertIsNone(outcome.impulse_count)

    def test_zero_material_response_cannot_hide_nonzero_impulse(self):
        with self.assertRaises(ValueError):
            explicit_impulse_calibration(
                100,
                {MaterialImpulseKey(1, LOADING, 0): 1},
            )
        calibration = explicit_impulse_calibration(
            100,
            {MaterialImpulseKey(1, LOADING, 0): 0},
        )
        outcome = calibrated_material_impulse(calibration, 1, LOADING, 0)
        self.assertEqual(outcome.status, IMPULSE_CALIBRATED)
        self.assertEqual(outcome.impulse_count, 0)

    def test_impulse_magnitude_is_not_bounded_by_material_amplitude(self):
        calibration = explicit_impulse_calibration(
            10,
            {MaterialImpulseKey(1, LOADING, 10): 37},
        )
        outcome = calibrated_material_impulse(calibration, 1, LOADING, 10)
        self.assertEqual(outcome.impulse_count, 37)

    def test_duplicate_and_invalid_entries_are_rejected(self):
        key = MaterialImpulseKey(1, LOADING, 20)
        with self.assertRaises(ValueError):
            explicit_impulse_calibration(100, ((key, 1), (key, 2)))
        with self.assertRaises(ValueError):
            explicit_impulse_calibration(100, {MaterialImpulseKey(1, LOADING, 101): 1})
        with self.assertRaises(ValueError):
            explicit_impulse_calibration(100, {MaterialImpulseKey(1, LOADING, 20): -1})
        with self.assertRaises(ValueError):
            explicit_impulse_calibration(100, {})
        with self.assertRaises(ValueError):
            MaterialImpulseKey(0, LOADING, 1)
        with self.assertRaises(ValueError):
            MaterialImpulseKey(1, "UNKNOWN", 1)


if __name__ == "__main__":
    unittest.main()
