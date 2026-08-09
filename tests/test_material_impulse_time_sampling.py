import unittest

from enterprise_math.material_impulse_time_sampling import (
    COARSE_TRANSMIT,
    FINE_REVERSE,
    time_sampling_divergence_witness,
)
from enterprise_math.material_impulse_world_1d import CROSSING_TRANSMIT, MATERIAL_KICK


class MaterialImpulseTimeSamplingTests(unittest.TestCase):
    def test_smallest_reference_family_member_transmits_coarse_and_reverses_fine(self):
        witness = time_sampling_divergence_witness(
            substeps=4,
            free_drift_cells_per_substep=1,
            collapse_factor=2,
        )
        self.assertEqual(witness.initial_center, -3)
        self.assertEqual(witness.initial_momentum, 4)
        self.assertEqual(witness.coarse_history.transitions[0].kind, CROSSING_TRANSMIT)
        self.assertEqual(witness.coarse_history.final.center, 1)
        self.assertEqual(witness.refined_history.first_reversal_tick, 3)
        self.assertEqual(witness.outcome_pair, (COARSE_TRANSMIT, FINE_REVERSE))

    def test_refined_path_explicitly_samples_layer_before_reversal(self):
        witness = time_sampling_divergence_witness(4, 1, 2)
        transitions = witness.refined_history.transitions
        self.assertEqual([t.before.center for t in transitions[:4]], [-3, -2, -1, -1])
        self.assertEqual(transitions[2].layer_depth, 1)
        self.assertEqual(transitions[2].response_sample, 1)
        self.assertEqual(transitions[2].kind, MATERIAL_KICK)
        self.assertEqual(transitions[2].after.momentum_quanta, 0)
        self.assertEqual(transitions[3].after.momentum_quanta, -4)
        self.assertTrue(transitions[3].momentum_reversed)

    def test_all_nonzero_kicks_and_drifts_are_exactly_divisible(self):
        for m in range(4, 8):
            for q in range(1, 5):
                for d in range(q + 1, (m - 1) * q):
                    witness = time_sampling_divergence_witness(m, q, d)
                    self.assertEqual(witness.initial_momentum % witness.refined_mass_divisor, 0)
                    for transition in witness.refined_history.transitions:
                        if transition.impulse is not None:
                            self.assertEqual(transition.impulse.projection_detail_numerator, 0)
                        if transition.after is not None:
                            self.assertEqual(
                                transition.after.momentum_quanta % witness.refined_mass_divisor,
                                0,
                            )
                    self.assertEqual(witness.outcome_pair, (COARSE_TRANSMIT, FINE_REVERSE))

    def test_family_constraints_leave_an_infinite_parameter_region(self):
        witnesses = []
        for m in range(4, 7):
            for q in range(1, 4):
                d = q + 1
                if d < (m - 1) * q:
                    witnesses.append(time_sampling_divergence_witness(m, q, d))
        self.assertGreaterEqual(len(witnesses), 8)
        self.assertTrue(all(w.outcome_pair == (COARSE_TRANSMIT, FINE_REVERSE) for w in witnesses))

    def test_invalid_parameters_are_rejected(self):
        with self.assertRaises(ValueError):
            time_sampling_divergence_witness(3, 1, 2)
        with self.assertRaises(ValueError):
            time_sampling_divergence_witness(4, 0, 2)
        with self.assertRaises(ValueError):
            time_sampling_divergence_witness(4, 1, 1)
        with self.assertRaises(ValueError):
            time_sampling_divergence_witness(4, 1, 3)


if __name__ == "__main__":
    unittest.main()
