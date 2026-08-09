import unittest

from enterprise_math.material_midpoint_time_sampling import (
    COARSE_TRANSMIT,
    FINE_REVERSE,
    midpoint_time_sampling_witness,
)
from enterprise_math.material_physical_midpoint_world_1d import (
    CROSSING_TRANSMIT,
    MATERIAL_MIDPOINT_FORCE,
)


class MaterialMidpointTimeSamplingTests(unittest.TestCase):
    def test_reference_midpoint_family_transmits_coarse_and_reverses_fine(self):
        witness = midpoint_time_sampling_witness(4, 2, 4)
        self.assertEqual(witness.initial_center, -6)
        self.assertEqual(witness.initial_momentum, 2)
        self.assertEqual(witness.coarse_transition.kind, CROSSING_TRANSMIT)
        self.assertEqual(witness.coarse_transition.after.center_count, 2)
        self.assertEqual(witness.outcome_pair, (COARSE_TRANSMIT, FINE_REVERSE))
        self.assertEqual(witness.first_fine_reversal_tick, 3)

    def test_reference_fine_saved_states_show_force_sampling_not_integrator_error(self):
        witness = midpoint_time_sampling_witness(4, 2, 4)
        transitions = witness.fine_transitions
        self.assertEqual([step.before.center_count for step in transitions], [-6, -4, -2, -1])
        self.assertIsNone(transitions[0].response_sample)
        self.assertIsNone(transitions[1].response_sample)
        self.assertEqual(transitions[2].kind, MATERIAL_MIDPOINT_FORCE)
        self.assertEqual(transitions[2].layer_depth, 2)
        self.assertEqual(transitions[2].whole_momentum_after, 0)
        self.assertEqual(transitions[2].displacement_cells, 1)
        self.assertEqual(transitions[3].whole_momentum_after, -2)
        self.assertEqual(transitions[3].displacement_cells, -1)
        self.assertTrue(transitions[3].lifted_momentum_reversed)

    def test_family_is_remainder_free_over_bounded_parameter_box(self):
        witnesses = []
        for m in range(4, 8):
            for s in (2, 4, 6):
                for d in range(3 * s // 2 + 1, (m - 1) * s):
                    witness = midpoint_time_sampling_witness(m, s, d)
                    witnesses.append(witness)
                    self.assertEqual(witness.outcome_pair, (COARSE_TRANSMIT, FINE_REVERSE))
                    for transition in witness.fine_transitions:
                        self.assertIn(transition.momentum_detail_after, (None, 0))
                        self.assertIn(transition.midpoint_position_detail_after, (None, 0))
        self.assertGreater(len(witnesses), 20)

    def test_coarse_and_fine_share_total_physical_duration_and_force_scale(self):
        witness = midpoint_time_sampling_witness(5, 2, 4)
        # Coarse free drift: p=2 over duration 5 -> 10 cells.
        self.assertEqual(witness.coarse_transition.displacement_cells, 10)
        # Fine ticks each use duration 1 and the same full-scale force count 2;
        # divergence comes solely from which saved states sample the force.
        force_steps = [t for t in witness.fine_transitions if t.response_sample]
        self.assertGreaterEqual(len(force_steps), 2)
        self.assertTrue(all(abs(t.raw_impulse_numerator) == 2 for t in force_steps))

    def test_invalid_family_parameters_are_rejected(self):
        with self.assertRaises(ValueError):
            midpoint_time_sampling_witness(3, 2, 4)
        with self.assertRaises(ValueError):
            midpoint_time_sampling_witness(4, 1, 3)
        with self.assertRaises(ValueError):
            midpoint_time_sampling_witness(4, 2, 3)
        with self.assertRaises(ValueError):
            midpoint_time_sampling_witness(4, 2, 6)


if __name__ == "__main__":
    unittest.main()
