import unittest

from enterprise_math.contact_cycle_modular_precision import (
    coarse_cycle_operation_modular_period,
    modular_additive_period,
    modular_additive_phase,
    modular_cycle_power_phases,
    scalar_cycle_modular_repair_report,
)


TRIANGLE_B = (
    (-1, 0, 1),
    (1, -1, 0),
    (0, 1, -1),
)

PATH_B = (
    (-1, 0),
    (1, -1),
    (0, 1),
)


class ContactCycleModularPrecisionTests(unittest.TestCase):
    def test_additive_period_formula_matches_direct_orbit(self):
        for modulus in range(1, 31):
            for shift in range(-20, 21):
                period = modular_additive_period(modulus, shift)
                phases = modular_cycle_power_phases(shift, modulus)
                self.assertEqual(len(phases), period)
                self.assertEqual(len(set(phases)), period)
                self.assertEqual(phases[0], 0)
                self.assertEqual(
                    modular_additive_phase(
                        modulus,
                        shift,
                        period,
                    ),
                    0,
                )
                if period > 1:
                    self.assertNotEqual(
                        modular_additive_phase(
                            modulus,
                            shift,
                            period - 1,
                        ),
                        0,
                    )

    def test_triangle_total_witness_has_exact_modular_repair_spectrum(self):
        expected = {
            1: 1,
            2: 2,
            3: 1,
            4: 4,
            5: 5,
            6: 2,
            7: 7,
            8: 8,
            9: 3,
            10: 10,
            12: 4,
        }
        for modulus, phase_count in expected.items():
            report = scalar_cycle_modular_repair_report(
                TRIANGLE_B,
                (1, 1, 1),
                modulus,
            )
            self.assertEqual(report.exact_hidden_grain, 3)
            self.assertEqual(
                report.modular_hidden_phase_count,
                phase_count,
            )
            self.assertEqual(
                report.coarse_body_state_is_modular_future_safe,
                phase_count == 1,
            )

    def test_triangle_difference_witness_is_safe_at_every_modulus(self):
        for modulus in range(1, 21):
            report = scalar_cycle_modular_repair_report(
                TRIANGLE_B,
                (1, -1, 0),
                modulus,
            )
            self.assertEqual(report.exact_hidden_grain, 0)
            self.assertEqual(report.modular_hidden_phase_count, 1)
            self.assertTrue(report.coarse_body_state_is_modular_future_safe)
            self.assertFalse(report.requires_modular_repair)

    def test_tree_has_no_modular_cycle_repair_for_any_scalar_readout(self):
        witness_rows = (
            (1, 0),
            (0, 1),
            (3, -5),
            (-7, 11),
        )
        for witness in witness_rows:
            for modulus in range(1, 13):
                report = scalar_cycle_modular_repair_report(
                    PATH_B,
                    witness,
                    modulus,
                )
                self.assertEqual(report.cycle_rank, 0)
                self.assertEqual(report.exact_hidden_grain, 0)
                self.assertEqual(report.modular_hidden_phase_count, 1)

    def test_static_hidden_group_and_dynamic_cycle_period_are_same_formula(self):
        # One triangle cycle changes total-contact witness by 3.  The hidden
        # witness subgroup in one body-state fiber is therefore 3Z, and the
        # dynamic witnessed partial identity has the same modular phase count.
        for modulus in range(1, 25):
            static = scalar_cycle_modular_repair_report(
                TRIANGLE_B,
                (1, 1, 1),
                modulus,
            )
            dynamic = coarse_cycle_operation_modular_period(
                3,
                modulus,
            )
            self.assertEqual(
                static.modular_hidden_phase_count,
                dynamic,
            )

    def test_modulus_can_erase_or_reveal_the_same_exact_cycle_history(self):
        self.assertEqual(
            scalar_cycle_modular_repair_report(
                TRIANGLE_B,
                (1, 1, 1),
                3,
            ).modular_hidden_phase_count,
            1,
        )
        self.assertEqual(
            scalar_cycle_modular_repair_report(
                TRIANGLE_B,
                (1, 1, 1),
                6,
            ).modular_hidden_phase_count,
            2,
        )
        self.assertEqual(
            scalar_cycle_modular_repair_report(
                TRIANGLE_B,
                (1, 1, 1),
                5,
            ).modular_hidden_phase_count,
            5,
        )

    def test_reference_dynamic_phase_orbits(self):
        self.assertEqual(modular_cycle_power_phases(3, 3), (0,))
        self.assertEqual(modular_cycle_power_phases(3, 6), (0, 3))
        self.assertEqual(
            modular_cycle_power_phases(3, 5),
            (0, 3, 1, 4, 2),
        )

    def test_validation(self):
        with self.assertRaises(ValueError):
            modular_additive_period(0, 1)
        with self.assertRaises(TypeError):
            modular_additive_period(5, True)
        with self.assertRaises(ValueError):
            scalar_cycle_modular_repair_report(
                TRIANGLE_B,
                (1, 1, 1),
                0,
            )


if __name__ == "__main__":
    unittest.main()
