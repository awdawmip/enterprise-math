import unittest

from enterprise_math.material_impulse_thresholds import (
    CELL_AWAY,
    CELL_HOLD,
    CELL_TOWARD,
    MOMENTUM_REVERSED,
    MOMENTUM_STALLED,
    MOMENTUM_TOWARD,
    classify_impulse_motion,
    impulse_reversal_thresholds,
)


class MaterialImpulseThresholdTests(unittest.TestCase):
    def test_exact_threshold_formulas_match_direct_classification_exhaustively(self):
        for mass in range(1, 9):
            for momentum in range(1, 13):
                for remainder in range(-(mass - 1), mass):
                    thresholds = impulse_reversal_thresholds(
                        momentum,
                        mass,
                        remainder,
                    )
                    self.assertEqual(
                        thresholds.first_momentum_reversal_impulse,
                        momentum + 1,
                    )
                    self.assertEqual(
                        thresholds.first_cell_away_impulse,
                        momentum + remainder + mass,
                    )
                    self.assertEqual(
                        thresholds.reversed_momentum_without_away_cell_count,
                        remainder + mass - 1,
                    )
                    for impulse in range(0, momentum + 2 * mass + 4):
                        momentum_class, cell_class, displacement = classify_impulse_motion(
                            momentum,
                            mass,
                            remainder,
                            impulse,
                        )
                        if impulse < momentum:
                            self.assertEqual(momentum_class, MOMENTUM_TOWARD)
                        elif impulse == momentum:
                            self.assertEqual(momentum_class, MOMENTUM_STALLED)
                        else:
                            self.assertEqual(momentum_class, MOMENTUM_REVERSED)

                        total = remainder + momentum - impulse
                        if total >= mass:
                            self.assertEqual(cell_class, CELL_TOWARD)
                            self.assertGreater(displacement, 0)
                        elif total <= -mass:
                            self.assertEqual(cell_class, CELL_AWAY)
                            self.assertLess(displacement, 0)
                        else:
                            self.assertEqual(cell_class, CELL_HOLD)
                            self.assertEqual(displacement, 0)

    def test_reversal_band_ranges_from_zero_to_two_m_minus_two(self):
        for mass in range(1, 10):
            low = impulse_reversal_thresholds(7, mass, -(mass - 1))
            high = impulse_reversal_thresholds(7, mass, mass - 1)
            self.assertEqual(low.reversed_momentum_without_away_cell_count, 0)
            self.assertEqual(
                high.reversed_momentum_without_away_cell_count,
                2 * mass - 2,
            )

    def test_dropping_detail_has_exact_m_minus_one_reversal_band(self):
        for mass in range(1, 10):
            for momentum in range(1, 10):
                thresholds = impulse_reversal_thresholds(momentum, mass, 0)
                self.assertEqual(
                    thresholds.reversed_momentum_without_away_cell_count,
                    mass - 1,
                )
                self.assertEqual(
                    thresholds.first_cell_away_impulse,
                    momentum + mass,
                )
                self.assertEqual(
                    thresholds.dropped_detail_first_cell_away_impulse,
                    momentum + mass,
                )

    def test_retained_remainder_shifts_cell_away_threshold_by_exact_remainder(self):
        mass = 5
        momentum = 4
        for remainder in range(-4, 5):
            thresholds = impulse_reversal_thresholds(momentum, mass, remainder)
            self.assertEqual(
                thresholds.first_cell_away_impulse
                - thresholds.dropped_detail_first_cell_away_impulse,
                remainder,
            )

    def test_reference_positive_phase_reverses_momentum_before_position(self):
        thresholds = impulse_reversal_thresholds(
            oriented_momentum=4,
            mass=5,
            oriented_remainder=4,
        )
        self.assertEqual(thresholds.first_momentum_reversal_impulse, 5)
        self.assertEqual(thresholds.first_cell_away_impulse, 13)
        self.assertEqual(thresholds.reversed_momentum_without_away_cell_count, 8)
        momentum_class, cell_class, displacement = classify_impulse_motion(4, 5, 4, 9)
        self.assertEqual(momentum_class, MOMENTUM_REVERSED)
        self.assertEqual(cell_class, CELL_HOLD)
        self.assertEqual(displacement, 0)

    def test_most_negative_phase_can_make_first_momentum_reversal_move_away_immediately(self):
        momentum_class, cell_class, displacement = classify_impulse_motion(
            oriented_momentum=4,
            mass=5,
            oriented_remainder=-4,
            impulse=5,
        )
        self.assertEqual(momentum_class, MOMENTUM_REVERSED)
        self.assertEqual(cell_class, CELL_AWAY)
        self.assertEqual(displacement, -1)

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            impulse_reversal_thresholds(0, 5, 0)
        with self.assertRaises(ValueError):
            impulse_reversal_thresholds(1, 0, 0)
        with self.assertRaises(ValueError):
            impulse_reversal_thresholds(1, 5, 5)
        with self.assertRaises(ValueError):
            classify_impulse_motion(1, 5, 0, -1)


if __name__ == "__main__":
    unittest.main()
