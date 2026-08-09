import unittest

from enterprise_math.material_hysteresis import LOADING, RETURNING
from enterprise_math.material_impulse_coupling import (
    project_material_impulse,
    repeated_constant_impulse,
    signed_toward_zero_divmod,
)
from enterprise_math.material_impulse_world_1d import (
    CROSSING_TRANSMIT,
    FREE_DRIFT,
    MATERIAL_KICK,
    MATERIAL_UNDERRESOLVED,
    TERMINAL_CONTACT,
    MomentumMaterialState1D,
    impulse_material_step_1d,
    run_impulse_material_world_1d,
)
from enterprise_math.material_response import explicit_material_curve_profile
from enterprise_math.scale_tunneling_1d import Wall1D


class MaterialImpulseCouplingTests(unittest.TestCase):
    def test_signed_toward_zero_divmod_is_exact_on_both_signs(self):
        for divisor in range(1, 12):
            for value in range(-50, 51):
                q, r = signed_toward_zero_divmod(value, divisor)
                self.assertEqual(value, divisor * q + r)
                self.assertLess(abs(r), divisor)
                self.assertEqual(q, abs(value) // divisor * (1 if value >= 0 else -1))

    def test_retained_subquantum_impulse_accumulates_but_drop_policy_does_not(self):
        retained = [
            repeated_constant_impulse(ticks, 1, 4, 1, -1, True)
            for ticks in range(1, 9)
        ]
        dropped = [
            repeated_constant_impulse(ticks, 1, 4, 1, -1, False)
            for ticks in range(1, 9)
        ]
        self.assertEqual(retained[0], (0, -1))
        self.assertEqual(retained[2], (0, -3))
        self.assertEqual(retained[3], (-1, 0))
        self.assertEqual(retained[7], (-2, 0))
        self.assertTrue(all(result == (0, 0) for result in dropped))

    def test_retained_constant_impulse_matches_one_batched_signed_projection(self):
        for amplitude in range(1, 8):
            for response in range(amplitude + 1):
                for maximum in range(0, 6):
                    for sign in (-1, 1):
                        for ticks in range(0, 12):
                            whole, detail = repeated_constant_impulse(
                                ticks,
                                response,
                                amplitude,
                                maximum,
                                sign,
                                True,
                            )
                            expected_q, expected_r = signed_toward_zero_divmod(
                                ticks * sign * maximum * response,
                                amplitude,
                            )
                            self.assertEqual((whole, detail), (expected_q, expected_r))

    def test_one_step_projection_retains_exact_numerator_accounting(self):
        report = project_material_impulse(3, 7, 5, -1, incoming_detail_numerator=2)
        self.assertEqual(
            report.total_signed_impulse_numerator,
            7 * report.impulse_quanta + report.projection_detail_numerator,
        )
        self.assertLess(abs(report.projection_detail_numerator), 7)


class MaterialImpulseWorld1DTests(unittest.TestCase):
    def setUp(self):
        self.wall = Wall1D(0, 0)
        self.profile = explicit_material_curve_profile(
            loading=(0, 2, 4, 4, 4),
            returning=(0, 2, 4, 4, 4),
            amplitude=4,
        )

    def test_same_initial_momentum_coarse_layer_reverses_while_fine_world_transmits(self):
        initial = MomentumMaterialState1D(center=-3, momentum_quanta=5)
        coarse = run_impulse_material_world_1d(
            initial,
            self.wall,
            radius=0,
            collapse_factor=5,
            material_profile=self.profile,
            mass_quanta=1,
            max_impulse_per_tick=4,
            ticks=2,
        )
        fine = run_impulse_material_world_1d(
            initial,
            self.wall,
            radius=0,
            collapse_factor=2,
            material_profile=self.profile,
            mass_quanta=1,
            max_impulse_per_tick=4,
            ticks=1,
        )
        self.assertEqual(
            [transition.kind for transition in coarse.transitions],
            [MATERIAL_KICK, MATERIAL_KICK],
        )
        self.assertEqual(coarse.transitions[0].after.center, -2)
        self.assertEqual(coarse.transitions[0].after.momentum_quanta, 1)
        self.assertTrue(coarse.transitions[1].momentum_reversed)
        self.assertEqual(coarse.final.center, -5)
        self.assertEqual(coarse.final.momentum_quanta, -3)
        self.assertEqual(coarse.final.branch, RETURNING)

        self.assertEqual(fine.transitions[0].kind, CROSSING_TRANSMIT)
        self.assertEqual(fine.final.center, 2)
        self.assertEqual(fine.final.momentum_quanta, 5)
        self.assertIsNone(fine.first_reversal_tick)

    def test_rebound_is_not_a_command_but_a_momentum_sign_change(self):
        initial = MomentumMaterialState1D(center=-3, momentum_quanta=5)
        history = run_impulse_material_world_1d(
            initial, self.wall, 0, 5, self.profile, 1, 4, ticks=2
        )
        self.assertEqual(history.first_reversal_tick, 1)
        self.assertGreater(history.transitions[0].after.momentum_quanta, 0)
        self.assertLess(history.transitions[1].after.momentum_quanta, 0)
        self.assertNotIn("REBOUND", [transition.kind for transition in history.transitions])

    def test_returning_branch_changes_outgoing_momentum_without_velocity_reversal_rule(self):
        weaker_return = explicit_material_curve_profile(
            loading=(0, 2, 4, 4, 4),
            returning=(0, 1, 2, 2, 2),
            amplitude=4,
        )
        initial = MomentumMaterialState1D(center=-3, momentum_quanta=5)
        symmetric = run_impulse_material_world_1d(
            initial, self.wall, 0, 5, self.profile, 3, 4, ticks=3
        )
        weak = run_impulse_material_world_1d(
            initial, self.wall, 0, 5, weaker_return, 3, 4, ticks=3
        )
        self.assertEqual(symmetric.transitions[2].before.branch, RETURNING)
        self.assertEqual(weak.transitions[2].before.branch, RETURNING)
        self.assertLess(symmetric.final.momentum_quanta, weak.final.momentum_quanta)
        self.assertEqual(symmetric.final.center, weak.final.center)

    def test_retained_impulse_detail_turns_repeated_subquantum_force_into_motion(self):
        tiny = explicit_material_curve_profile(
            loading=(0, 1),
            returning=(0, 1),
            amplitude=4,
        )
        initial = MomentumMaterialState1D(center=-1, momentum_quanta=0, branch=LOADING)
        retained = run_impulse_material_world_1d(
            initial,
            self.wall,
            0,
            2,
            tiny,
            mass_quanta=1,
            max_impulse_per_tick=1,
            ticks=4,
            retain_impulse_detail=True,
        )
        dropped = run_impulse_material_world_1d(
            initial,
            self.wall,
            0,
            2,
            tiny,
            mass_quanta=1,
            max_impulse_per_tick=1,
            ticks=4,
            retain_impulse_detail=False,
        )
        self.assertEqual(retained.final.center, -2)
        self.assertEqual(retained.final.momentum_quanta, -1)
        self.assertEqual(retained.final.impulse_detail_numerator, 0)
        self.assertEqual(dropped.final.center, -1)
        self.assertEqual(dropped.final.momentum_quanta, 0)

    def test_outside_layer_is_free_drift_until_saved_endpoint_hits_terminal_geometry(self):
        initial = MomentumMaterialState1D(center=-3, momentum_quanta=3)
        outcome = impulse_material_step_1d(
            initial, self.wall, 0, 1, self.profile, mass_quanta=1, max_impulse_per_tick=4
        )
        self.assertEqual(outcome.kind, TERMINAL_CONTACT)
        self.assertEqual(outcome.start_clearance, 3)
        self.assertEqual(outcome.end_clearance, 0)
        self.assertIsNone(outcome.after)

        free = impulse_material_step_1d(
            MomentumMaterialState1D(-5, 1),
            self.wall,
            0,
            2,
            self.profile,
            mass_quanta=1,
            max_impulse_per_tick=4,
        )
        self.assertEqual(free.kind, FREE_DRIFT)
        self.assertEqual(free.after.center, -4)

    def test_material_depth_overflow_is_explicit_underresolution(self):
        short = explicit_material_curve_profile(
            loading=(0, 1), returning=(0, 1), amplitude=1
        )
        outcome = impulse_material_step_1d(
            MomentumMaterialState1D(-1, 1),
            self.wall,
            0,
            5,
            short,
            mass_quanta=1,
            max_impulse_per_tick=1,
        )
        self.assertEqual(outcome.kind, MATERIAL_UNDERRESOLVED)
        self.assertEqual(outcome.layer_depth, 4)
        self.assertIsNone(outcome.after)


if __name__ == "__main__":
    unittest.main()
