import unittest

from enterprise_math.material_physical_projection import (
    ForceImpulseCountScale,
    MomentumDriftCountScale,
    project_force_count_to_momentum,
    project_momentum_count_to_position,
)


class MaterialPhysicalProjectionTests(unittest.TestCase):
    def test_force_time_to_momentum_count_identity_is_exact(self):
        scale = ForceImpulseCountScale(
            force_scale_factor=10,
            time_scale_factor=1000,
            momentum_scale_factor=100,
            tick_duration_count=25,
            force_unit="N",
            time_unit="s",
            momentum_unit="N*s",
        )
        divisor = scale.projection_divisor
        for force in range(0, 30):
            for sign in (-1, 1):
                report = project_force_count_to_momentum(force, sign, scale)
                self.assertEqual(
                    report.total_momentum_count_numerator,
                    divisor * report.momentum_count_increment
                    + report.projection_detail_numerator,
                )
                self.assertLess(abs(report.projection_detail_numerator), divisor)

    def test_normalized_impulse_rule_is_a_special_case_of_explicit_count_scales(self):
        # Old normalized rule q=trunc(sign*J*r/A) is recovered with
        # F_s=A, T_s=1, P_s=J and one time-count per tick.
        A = 7
        J = 5
        scale = ForceImpulseCountScale(
            force_scale_factor=A,
            time_scale_factor=1,
            momentum_scale_factor=J,
            tick_duration_count=1,
            force_unit="response_q",
            time_unit="tick",
            momentum_unit="response_q*tick",
        )
        for response in range(A + 1):
            for sign in (-1, 1):
                report = project_force_count_to_momentum(response, sign, scale)
                raw = sign * J * response
                expected = raw // A if raw >= 0 else -((-raw) // A)
                self.assertEqual(report.momentum_count_increment, expected)

    def test_retained_force_impulse_detail_accumulates_exactly_across_ticks(self):
        scale = ForceImpulseCountScale(
            force_scale_factor=4,
            time_scale_factor=1,
            momentum_scale_factor=1,
            tick_duration_count=1,
            force_unit="F",
            time_unit="t",
            momentum_unit="F*t",
        )
        whole = 0
        detail = 0
        for _ in range(4):
            report = project_force_count_to_momentum(1, 1, scale, detail, True)
            whole += report.momentum_count_increment
            detail = report.next_detail_numerator
        self.assertEqual((whole, detail), (1, 0))

    def test_momentum_to_position_identity_is_exact(self):
        scale = MomentumDriftCountScale(
            momentum_scale_factor=100,
            mass_scale_factor=1000,
            time_scale_factor=1000,
            position_scale_factor=1000,
            tick_duration_count=10,
            mass_count=2000,
            momentum_unit="kg*m/s",
            mass_unit="kg",
            time_unit="s",
            position_unit="m",
        )
        divisor = scale.projection_divisor
        for momentum in range(-20, 21):
            report = project_momentum_count_to_position(momentum, scale)
            self.assertEqual(
                report.total_position_count_numerator,
                divisor * report.displacement_cells
                + report.projection_detail_numerator,
            )
            self.assertLess(abs(report.projection_detail_numerator), divisor)

    def test_normalized_mass_division_is_special_case_of_drift_scales(self):
        for mass in range(1, 8):
            scale = MomentumDriftCountScale(
                momentum_scale_factor=1,
                mass_scale_factor=1,
                time_scale_factor=1,
                position_scale_factor=1,
                tick_duration_count=1,
                mass_count=mass,
                momentum_unit="p",
                mass_unit="m",
                time_unit="t",
                position_unit="x",
            )
            for momentum in range(-20, 21):
                report = project_momentum_count_to_position(momentum, scale)
                expected = (
                    momentum // mass
                    if momentum >= 0
                    else -((-momentum) // mass)
                )
                self.assertEqual(report.displacement_cells, expected)

    def test_retained_spatial_subcell_detail_can_accumulate_into_one_saved_cell(self):
        scale = MomentumDriftCountScale(
            momentum_scale_factor=1,
            mass_scale_factor=1,
            time_scale_factor=4,
            position_scale_factor=1,
            tick_duration_count=1,
            mass_count=1,
            momentum_unit="p",
            mass_unit="m",
            time_unit="t",
            position_unit="x",
        )
        whole = 0
        detail = 0
        for _ in range(4):
            report = project_momentum_count_to_position(1, scale, detail, True)
            whole += report.displacement_cells
            detail = report.next_detail_numerator
        self.assertEqual((whole, detail), (1, 0))

    def test_invalid_detail_cells_are_rejected(self):
        force = ForceImpulseCountScale(2, 3, 1, 1, "F", "t", "p")
        with self.assertRaises(ValueError):
            project_force_count_to_momentum(1, 1, force, 6)
        drift = MomentumDriftCountScale(2, 1, 3, 1, 1, 1, "p", "m", "t", "x")
        with self.assertRaises(ValueError):
            project_momentum_count_to_position(1, drift, 6)


if __name__ == "__main__":
    unittest.main()
