import unittest

from enterprise_math.collision_phase_diagram import (
    coarse_clearance,
    collision_phase_1d,
    contact_half_width_1d,
    finest_contact_factor,
    first_resolving_factor,
    interaction_band_states_1d,
    macro_contact_from_gap,
    minimum_factor_for_static_no_skip_1d,
    primitive_clearance,
    static_no_skip_guaranteed_1d,
    static_skip_witness_1d,
)
from enterprise_math.engineering_collision import (
    COLLIDES,
    UNRESOLVED,
    Body2D,
    collision_certificate_at_scale,
    exact_collision,
)
from enterprise_math.motion_collapse import BodyMotion2D, motion_conflict


def sampled_crossing_hits_band(start, relative_step, half_width):
    """Independent arithmetic-progression oracle for a monotone decreasing crossing."""
    position = start
    while position > half_width:
        position -= relative_step
    return -half_width <= position <= half_width


class CollisionPhaseDiagramTests(unittest.TestCase):
    def test_primitive_clearance_zero_exactly_matches_terminal_collision(self):
        bodies = []
        body_id = 0
        for x in range(-4, 5, 2):
            for y in range(-4, 5, 2):
                for radius in range(3):
                    bodies.append(Body2D(body_id, x, y, radius))
                    body_id += 1
        for left_index, left in enumerate(bodies):
            for right in bodies[left_index + 1 :]:
                self.assertEqual(
                    primitive_clearance(left, right) == 0,
                    exact_collision(left, right),
                )

    def test_positive_gap_contact_extinguishes_at_exact_integer_factor(self):
        for gap in range(1, 10):
            self.assertEqual(finest_contact_factor(gap), gap + 1)
            self.assertEqual(first_resolving_factor(gap), gap)
            self.assertTrue(macro_contact_from_gap(gap, gap + 1))
            self.assertFalse(macro_contact_from_gap(gap, gap))
            for factor in range(1, 13):
                self.assertEqual(macro_contact_from_gap(gap, factor), gap < factor)
                self.assertEqual(coarse_clearance(gap, factor), gap // factor)

    def test_collapse_contact_is_not_the_must_terminal_truth_certificate(self):
        left = Body2D(0, 0, 0, 0)
        right = Body2D(1, 1, 0, 0)
        gap = primitive_clearance(left, right)
        self.assertEqual(gap, 1)
        self.assertTrue(macro_contact_from_gap(gap, collapse_factor=2))

        must = collision_certificate_at_scale(left, right, cell_size=2)
        self.assertEqual(must.status, UNRESOLVED)
        self.assertNotEqual(must.status, COLLIDES)
        self.assertFalse(exact_collision(left, right))

    def test_primitive_contact_persists_at_every_factor(self):
        self.assertIsNone(finest_contact_factor(0))
        self.assertIsNone(first_resolving_factor(0))
        for factor in range(1, 20):
            self.assertTrue(macro_contact_from_gap(0, factor))

    def test_interaction_band_cardinality_is_exact(self):
        for radius_sum in range(5):
            for factor in range(1, 8):
                half_width = contact_half_width_1d(radius_sum, factor)
                band = list(range(-half_width, half_width + 1))
                self.assertEqual(len(band), interaction_band_states_1d(radius_sum, factor))
                self.assertEqual(len(band), 2 * (radius_sum + factor) - 1)

    def test_no_skip_criterion_is_phase_independently_exact_on_small_domain(self):
        for radius_sum in range(4):
            for factor in range(1, 6):
                half_width = contact_half_width_1d(radius_sum, factor)
                band_size = interaction_band_states_1d(radius_sum, factor)
                for step in range(1, 13):
                    all_phases_hit = all(
                        sampled_crossing_hits_band(start, step, half_width)
                        for start in range(half_width + 1, half_width + step + 1)
                    )
                    self.assertEqual(all_phases_hit, step <= band_size)
                    self.assertEqual(
                        static_no_skip_guaranteed_1d(radius_sum, factor, step),
                        all_phases_hit,
                    )

    def test_skip_witness_crosses_from_above_to_below_without_sampling_band(self):
        for radius_sum in range(3):
            for factor in range(1, 5):
                half_width = contact_half_width_1d(radius_sum, factor)
                band_size = interaction_band_states_1d(radius_sum, factor)
                for step in range(1, 12):
                    witness = static_skip_witness_1d(radius_sum, factor, step)
                    if step <= band_size:
                        self.assertIsNone(witness)
                    else:
                        self.assertIsNotNone(witness)
                        start, end = witness
                        self.assertGreater(start, half_width)
                        self.assertLess(end, -half_width)
                        self.assertEqual(start - end, step)

    def test_minimum_factor_for_static_no_skip_is_sharp(self):
        for radius_sum in range(5):
            for step in range(0, 16):
                factor = minimum_factor_for_static_no_skip_1d(radius_sum, step)
                self.assertTrue(
                    static_no_skip_guaranteed_1d(radius_sum, factor, step)
                )
                if factor > 1:
                    self.assertFalse(
                        static_no_skip_guaranteed_1d(radius_sum, factor - 1, step)
                    )

    def test_point_swap_is_static_skip_at_terminal_factor_but_transition_conflict(self):
        phase = collision_phase_1d(radius_sum=0, collapse_factor=1, relative_step=2)
        self.assertEqual(phase.contact_half_width, 0)
        self.assertEqual(phase.interaction_band_states, 1)
        self.assertFalse(phase.static_no_skip_guaranteed)
        self.assertEqual(phase.skip_witness, (1, -1))

        left = BodyMotion2D(Body2D(0, 0, 0, 0), (1, 0))
        right = BodyMotion2D(Body2D(1, 1, 0, 0), (-1, 0))
        self.assertTrue(motion_conflict(left, right))

    def test_coarser_factor_widens_band_and_restores_static_no_skip_for_point_swap(self):
        terminal = collision_phase_1d(radius_sum=0, collapse_factor=1, relative_step=2)
        coarse = collision_phase_1d(radius_sum=0, collapse_factor=2, relative_step=2)
        self.assertFalse(terminal.static_no_skip_guaranteed)
        self.assertTrue(coarse.static_no_skip_guaranteed)
        self.assertEqual(coarse.interaction_band_states, 3)

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            coarse_clearance(-1, 2)
        with self.assertRaises(ValueError):
            coarse_clearance(1, 0)
        with self.assertRaises(ValueError):
            static_no_skip_guaranteed_1d(0, 1, -1)


if __name__ == "__main__":
    unittest.main()
