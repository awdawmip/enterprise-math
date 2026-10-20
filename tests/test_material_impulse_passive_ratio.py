import unittest

from enterprise_math.material_hysteresis import LOADING
from enterprise_math.material_impulse_calibration import MaterialImpulseKey
from enterprise_math.material_impulse_passive_ratio import (
    PASSIVE_RATIO_CALIBRATED,
    PASSIVE_RATIO_UNDERRESOLVED,
    explicit_passive_impulse_ratio_calibration,
    minimum_momentum_for_ratio_rebound,
    passive_impulse_from_material_state,
)
from enterprise_math.material_impulse_passivity import (
    DISSIPATIVE_REBOUND,
    ELASTIC_REFLECTION,
    STALL,
)


class MaterialImpulsePassiveRatioTests(unittest.TestCase):
    def test_ratio_domain_guarantees_nonamplifying_squared_momentum(self):
        key = MaterialImpulseKey(1, LOADING, 50)
        for amplitude in range(1, 10):
            for ratio in range(0, 2 * amplitude + 1):
                calibration = explicit_passive_impulse_ratio_calibration(
                    material_amplitude=100,
                    ratio_amplitude=amplitude,
                    ratio_entries={key: ratio},
                )
                for momentum in range(1, 20):
                    outcome = passive_impulse_from_material_state(
                        calibration,
                        1,
                        LOADING,
                        50,
                        momentum,
                    )
                    self.assertEqual(outcome.status, PASSIVE_RATIO_CALIBRATED)
                    self.assertLessEqual(outcome.impulse, 2 * momentum)
                    self.assertTrue(outcome.passivity.passive_nonamplifying)
                    self.assertEqual(
                        momentum * ratio,
                        amplitude * outcome.impulse + outcome.ratio_remainder,
                    )
                    self.assertLess(outcome.ratio_remainder, amplitude)

    def test_unit_ratio_stalls_exactly_and_double_ratio_reflects_exactly(self):
        key = MaterialImpulseKey(1, LOADING, 50)
        stall = explicit_passive_impulse_ratio_calibration(100, 10, {key: 10})
        reflect = explicit_passive_impulse_ratio_calibration(100, 10, {key: 20})
        for momentum in range(1, 20):
            stalled = passive_impulse_from_material_state(stall, 1, LOADING, 50, momentum)
            reflected = passive_impulse_from_material_state(reflect, 1, LOADING, 50, momentum)
            self.assertEqual(stalled.impulse, momentum)
            self.assertEqual(stalled.passivity.regime, STALL)
            self.assertEqual(reflected.impulse, 2 * momentum)
            self.assertEqual(reflected.passivity.regime, ELASTIC_REFLECTION)
            self.assertTrue(reflected.momentum_reversed)

    def test_ratio_above_stall_has_exact_minimum_momentum_for_quantized_rebound(self):
        for amplitude in range(1, 15):
            for ratio in range(amplitude + 1, 2 * amplitude + 1):
                threshold = minimum_momentum_for_ratio_rebound(ratio, amplitude)
                self.assertIsNotNone(threshold)
                key = MaterialImpulseKey(1, LOADING, 50)
                calibration = explicit_passive_impulse_ratio_calibration(
                    100,
                    amplitude,
                    {key: ratio},
                )
                at = passive_impulse_from_material_state(
                    calibration, 1, LOADING, 50, threshold
                )
                self.assertTrue(at.momentum_reversed)
                self.assertIn(at.passivity.regime, (DISSIPATIVE_REBOUND, ELASTIC_REFLECTION))
                if threshold > 1:
                    below = passive_impulse_from_material_state(
                        calibration, 1, LOADING, 50, threshold - 1
                    )
                    self.assertFalse(below.momentum_reversed)

    def test_reference_ratio_can_stall_at_low_momentum_then_rebound_at_higher_momentum(self):
        key = MaterialImpulseKey(1, LOADING, 50)
        calibration = explicit_passive_impulse_ratio_calibration(
            100,
            10,
            {key: 15},
        )
        low = passive_impulse_from_material_state(calibration, 1, LOADING, 50, 1)
        high = passive_impulse_from_material_state(calibration, 1, LOADING, 50, 2)
        self.assertEqual(minimum_momentum_for_ratio_rebound(15, 10), 2)
        self.assertEqual(low.impulse, 1)
        self.assertFalse(low.momentum_reversed)
        self.assertEqual(low.passivity.regime, STALL)
        self.assertEqual(high.impulse, 3)
        self.assertTrue(high.momentum_reversed)
        self.assertEqual(high.passivity.regime, DISSIPATIVE_REBOUND)

    def test_sparse_missing_state_is_explicitly_underresolved(self):
        key = MaterialImpulseKey(1, LOADING, 50)
        calibration = explicit_passive_impulse_ratio_calibration(100, 10, {key: 15})
        missing = passive_impulse_from_material_state(
            calibration,
            2,
            LOADING,
            50,
            4,
        )
        self.assertEqual(missing.status, PASSIVE_RATIO_UNDERRESOLVED)
        self.assertIsNone(missing.impulse)
        self.assertIsNone(missing.passivity)

    def test_zero_response_and_ratio_bounds_are_strictly_validated(self):
        zero = MaterialImpulseKey(1, LOADING, 0)
        with self.assertRaises(ValueError):
            explicit_passive_impulse_ratio_calibration(100, 10, {zero: 1})
        key = MaterialImpulseKey(1, LOADING, 50)
        with self.assertRaises(ValueError):
            explicit_passive_impulse_ratio_calibration(100, 10, {key: 21})
        with self.assertRaises(ValueError):
            minimum_momentum_for_ratio_rebound(21, 10)


if __name__ == "__main__":
    unittest.main()
