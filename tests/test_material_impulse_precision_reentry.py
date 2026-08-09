import unittest

from enterprise_math.material_impulse_precision_reentry import (
    REVERSE,
    UNDERRESOLVED,
    precision_reentry_witness,
)


class MaterialImpulsePrecisionReentryTests(unittest.TestCase):
    def test_reference_sequence_is_reverse_underresolved_reverse(self):
        witness = precision_reentry_witness(
            inward_drift_cells=2,
            material_max_depth=6,
            primitive_gap=3,
        )
        self.assertEqual(
            (witness.hit_factor, witness.underresolved_factor, witness.reentry_factor),
            (7, 8, 9),
        )
        self.assertEqual(witness.outcome_pattern, (REVERSE, UNDERRESOLVED, REVERSE))
        self.assertEqual(witness.hit_history.first_reversal_tick, 2)
        self.assertEqual(witness.underresolved_history.halted_kind, UNDERRESOLVED)
        self.assertEqual(witness.reentry_history.first_reversal_tick, 1)

    def test_infinite_integer_family_holds_on_bounded_parameter_box(self):
        for q in range(2, 6):
            for K in range(q + 1, 10):
                for gap in range(q + 1, q + 6):
                    witness = precision_reentry_witness(q, K, gap)
                    self.assertEqual(
                        witness.outcome_pattern,
                        (REVERSE, UNDERRESOLVED, REVERSE),
                    )
                    self.assertLess(witness.hit_factor, witness.underresolved_factor)
                    self.assertLess(witness.underresolved_factor, witness.reentry_factor)

    def test_loading_branch_is_monotone_despite_dynamic_reentry(self):
        witness = precision_reentry_witness(3, 8, 5)
        samples = witness.profile.loading
        self.assertEqual(samples, tuple(sorted(samples)))
        self.assertEqual(samples[-1], 1)
        self.assertTrue(all(sample == 0 for sample in samples[:-1]))
        self.assertEqual(witness.outcome_pattern, (REVERSE, UNDERRESOLVED, REVERSE))

    def test_underresolved_middle_factor_is_caused_by_saved_depth_overshoot(self):
        witness = precision_reentry_witness(2, 6, 3)
        under = witness.underresolved_history
        self.assertEqual(len(under.transitions), 2)
        first = under.transitions[0]
        second = under.transitions[1]
        self.assertIsNone(first.impulse)
        self.assertEqual(first.drift_cells, 2)
        self.assertEqual(first.after.center, -1)
        self.assertEqual(second.layer_depth, 7)
        self.assertEqual(witness.material_max_depth, 6)
        self.assertEqual(second.kind, UNDERRESOLVED)

    def test_reentry_factor_acts_before_any_inward_drift(self):
        witness = precision_reentry_witness(2, 6, 3)
        first = witness.reentry_history.transitions[0]
        self.assertEqual(first.layer_depth, 6)
        self.assertEqual(first.response_sample, 1)
        self.assertEqual(first.before.momentum_quanta, 2)
        self.assertEqual(first.after.momentum_quanta, 0)
        self.assertEqual(first.drift_cells, 0)

    def test_parameter_constraints_are_explicit(self):
        with self.assertRaises(ValueError):
            precision_reentry_witness(1, 4, 4)
        with self.assertRaises(ValueError):
            precision_reentry_witness(3, 3, 5)
        with self.assertRaises(ValueError):
            precision_reentry_witness(3, 6, 3)


if __name__ == "__main__":
    unittest.main()
