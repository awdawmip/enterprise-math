import unittest

from enterprise_math.material_mass_drift import (
    first_retained_drift_tick,
    project_mass_drift,
    repeated_constant_mass_drift,
)


class MaterialMassDriftTests(unittest.TestCase):
    def test_projection_is_exact_on_both_signs(self):
        for mass in range(1, 10):
            for momentum in range(-20, 21):
                for detail in range(-(mass - 1), mass):
                    report = project_mass_drift(momentum, mass, detail, True)
                    self.assertEqual(
                        report.total_drift_numerator,
                        mass * report.drift_cells + report.projection_detail,
                    )
                    self.assertLess(abs(report.projection_detail), mass)
                    self.assertEqual(report.next_position_detail, report.projection_detail)

    def test_retained_constant_drift_matches_one_batched_projection(self):
        for mass in range(1, 9):
            for momentum in range(-10, 11):
                for ticks in range(0, 20):
                    displacement, detail = repeated_constant_mass_drift(
                        ticks,
                        momentum,
                        mass,
                        True,
                    )
                    total = ticks * momentum
                    if total >= 0:
                        expected_displacement = total // mass
                    else:
                        expected_displacement = -((-total) // mass)
                    expected_detail = total - mass * expected_displacement
                    self.assertEqual(
                        (displacement, detail),
                        (expected_displacement, expected_detail),
                    )

    def test_submass_momentum_eventually_moves_with_detail_but_freezes_when_dropped(self):
        for mass in range(2, 10):
            for magnitude in range(1, mass):
                threshold = first_retained_drift_tick(magnitude, mass)
                self.assertEqual(
                    repeated_constant_mass_drift(
                        threshold - 1,
                        magnitude,
                        mass,
                        True,
                    )[0],
                    0,
                )
                self.assertEqual(
                    repeated_constant_mass_drift(
                        threshold,
                        magnitude,
                        mass,
                        True,
                    )[0],
                    1,
                )
                self.assertEqual(
                    repeated_constant_mass_drift(
                        threshold,
                        -magnitude,
                        mass,
                        True,
                    )[0],
                    -1,
                )
                for ticks in (1, threshold, threshold + 5, 50):
                    self.assertEqual(
                        repeated_constant_mass_drift(
                            ticks,
                            magnitude,
                            mass,
                            False,
                        ),
                        (0, 0),
                    )
                    self.assertEqual(
                        repeated_constant_mass_drift(
                            ticks,
                            -magnitude,
                            mass,
                            False,
                        ),
                        (0, 0),
                    )

    def test_mass_one_has_no_position_detail_and_both_policies_coincide(self):
        for momentum in range(-10, 11):
            for ticks in range(0, 10):
                retained = repeated_constant_mass_drift(ticks, momentum, 1, True)
                dropped = repeated_constant_mass_drift(ticks, momentum, 1, False)
                self.assertEqual(retained, dropped)
                self.assertEqual(retained, (ticks * momentum, 0))

    def test_first_drift_tick_formula(self):
        self.assertIsNone(first_retained_drift_tick(0, 5))
        self.assertEqual(first_retained_drift_tick(1, 5), 5)
        self.assertEqual(first_retained_drift_tick(2, 5), 3)
        self.assertEqual(first_retained_drift_tick(5, 5), 1)
        self.assertEqual(first_retained_drift_tick(9, 5), 1)

    def test_drop_policy_zeros_incoming_and_outgoing_position_detail(self):
        report = project_mass_drift(
            momentum_quanta=2,
            mass_quanta=5,
            incoming_position_detail=4,
            retain_detail=False,
        )
        self.assertEqual(report.incoming_position_detail, 0)
        self.assertEqual(report.drift_cells, 0)
        self.assertEqual(report.projection_detail, 2)
        self.assertEqual(report.next_position_detail, 0)

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            project_mass_drift(1, 0)
        with self.assertRaises(ValueError):
            project_mass_drift(1, 5, 5)
        with self.assertRaises(ValueError):
            repeated_constant_mass_drift(-1, 1, 5)
        with self.assertRaises(ValueError):
            first_retained_drift_tick(1, 0)


if __name__ == "__main__":
    unittest.main()
