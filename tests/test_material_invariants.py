import unittest
from math import isqrt

from enterprise_math.material_invariants import (
    axis_dead_zone_orbit,
    first_resolved_loading_lobe,
    hardening_composition_defect,
    minimum_transverse_amplitude,
    parameter_rotation,
    parameter_rotation_minimum_transverse_amplitude,
    projection_history_comparison,
    softening_composition_defect,
    toward_zero_loss_certificate,
)
from enterprise_math.material_oscillator import (
    TOWARD_ZERO,
    projected_rotation_step,
)
from enterprise_math.material_response import hardening_sample, softening_sample


class MaterialInvariantTests(unittest.TestCase):
    def test_parameter_rotation_is_pythagorean_and_threshold_has_closed_form(self):
        for m in range(2, 41):
            rotation = parameter_rotation(m)
            self.assertEqual(
                rotation.a * rotation.a + rotation.b * rotation.b,
                rotation.c * rotation.c,
            )
            threshold = parameter_rotation_minimum_transverse_amplitude(m)
            self.assertEqual(threshold, m // 2 + 1)
            self.assertEqual(threshold, minimum_transverse_amplitude(rotation))

    def test_exact_collapse_loss_certificate_matches_squared_radius_loss(self):
        for m in range(2, 9):
            rotation = parameter_rotation(m)
            for x in range(-10, 11):
                for y in range(-10, 11):
                    report = projected_rotation_step(x, y, rotation, TOWARD_ZERO)
                    certificate = toward_zero_loss_certificate(x, y, rotation)
                    self.assertEqual(
                        certificate,
                        rotation.c * rotation.c * report.norm_sq_loss,
                    )
                    self.assertGreaterEqual(certificate, 0)

    def test_below_threshold_transverse_motion_never_starts(self):
        for m in range(2, 31):
            rotation = parameter_rotation(m)
            threshold = minimum_transverse_amplitude(rotation)
            for amplitude in range(threshold):
                orbit = axis_dead_zone_orbit(amplitude, rotation)
                self.assertEqual(orbit[-1], (0, 0))
                self.assertTrue(all(y == 0 for _x, y in orbit))
                xs = [x for x, _y in orbit]
                self.assertEqual(xs, sorted(xs, reverse=True))
            first = projected_rotation_step(threshold, 0, rotation, TOWARD_ZERO).after
            self.assertGreaterEqual(first[1], 1)

    def test_resolution_condition_is_equivalent_to_m_less_than_twice_amplitude(self):
        for amplitude in range(1, 25):
            for m in range(2, 50):
                resolved = amplitude >= parameter_rotation_minimum_transverse_amplitude(m)
                self.assertEqual(resolved, m < 2 * amplitude)

    def test_reference_loading_lobe_is_intrinsic_and_finite(self):
        rotation = parameter_rotation(20)
        self.assertEqual(
            first_resolved_loading_lobe(1000, rotation),
            (0, 99, 197, 293, 386, 475, 560, 639, 712, 777, 835, 884, 924, 955, 977, 989, 991),
        )
        self.assertEqual(first_resolved_loading_lobe(10, rotation), (0,))

    def test_intermediate_projection_creates_history_defect(self):
        rotation = parameter_rotation(20)
        comparison = projection_history_comparison(100, rotation, 16)
        self.assertEqual(comparison.terminal, (-2, 99))
        self.assertEqual(comparison.stepwise, (-1, 90))
        self.assertEqual(comparison.defect, (1, -9))
        self.assertEqual(comparison.l1_defect, 10)

    def test_hardening_and_softening_staged_composition_never_exceeds_direct_product_order(self):
        for amplitude in range(1, 31):
            for sample in range(amplitude + 1):
                for outer in range(1, 5):
                    for inner in range(1, 5):
                        self.assertGreaterEqual(
                            hardening_composition_defect(sample, amplitude, outer, inner),
                            0,
                        )
                        self.assertGreaterEqual(
                            softening_composition_defect(sample, amplitude, outer, inner),
                            0,
                        )

    def test_curve_composition_order_can_matter_because_of_intermediate_collapse(self):
        amplitude = 5
        sample = 4
        h_2_after_3 = hardening_sample(
            hardening_sample(sample, amplitude, 3), amplitude, 2
        )
        h_3_after_2 = hardening_sample(
            hardening_sample(sample, amplitude, 2), amplitude, 3
        )
        self.assertEqual((h_2_after_3, h_3_after_2), (0, 1))

        amplitude = 4
        sample = 1
        g_2_after_3 = softening_sample(
            softening_sample(sample, amplitude, 3), amplitude, 2
        )
        g_3_after_2 = softening_sample(
            softening_sample(sample, amplitude, 2), amplitude, 3
        )
        self.assertEqual((g_2_after_3, g_3_after_2), (2, 3))

    def test_small_state_search_finds_no_nonzero_cycle_for_parameter_rotations(self):
        for m in range(2, 9):
            rotation = parameter_rotation(m)
            for start_x in range(-7, 8):
                for start_y in range(-7, 8):
                    state = (start_x, start_y)
                    if state == (0, 0):
                        continue
                    radius = isqrt(start_x * start_x + start_y * start_y)
                    bound = (2 * radius + 3) ** 2 + 1
                    seen = set()
                    for _ in range(bound):
                        if state == (0, 0):
                            break
                        self.assertNotIn(state, seen)
                        seen.add(state)
                        state = projected_rotation_step(*state, rotation, TOWARD_ZERO).after
                    self.assertEqual(state, (0, 0))


if __name__ == "__main__":
    unittest.main()
