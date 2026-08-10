import unittest

from enterprise_math.material_contact_network_impulse_1d import (
    ContactChannel1D,
    ContactNetworkMomentum1D,
)
from enterprise_math.material_contact_network_tick_1d import (
    ContactMaterialImpulseState,
    apply_contact_material_tick,
)
from enterprise_math.material_contact_tick_causal_queue import (
    guarded_terminal_prefix_relation,
    material_tick_causal_queue_relation,
)


class MaterialContactTickCausalQueueTests(unittest.TestCase):
    def test_z_path_realisable_target_has_single_full_terminal(self):
        relation = guarded_terminal_prefix_relation(
            (-1, -1),
            ((2, -1), (-1, 2)),
            (1, 1),
        )
        self.assertTrue(relation.z_coupled)
        self.assertTrue(relation.full_consumption_possible)
        self.assertTrue(relation.scheduler_independent_full_consumption)
        self.assertEqual(len(relation.terminals), 1)
        terminal = relation.terminals[0]
        self.assertEqual(terminal.applied_counts, (1, 1))
        self.assertEqual(terminal.queued_counts, (0, 0))

    def test_positive_coupling_can_mix_full_and_stuck_terminal_outcomes(self):
        relation = guarded_terminal_prefix_relation(
            (-1, -2),
            ((2, 1), (1, 2)),
            (1, 1),
        )
        self.assertFalse(relation.z_coupled)
        self.assertTrue(relation.full_consumption_possible)
        self.assertFalse(relation.scheduler_independent_full_consumption)
        self.assertEqual(
            {terminal.applied_counts for terminal in relation.terminals},
            {(0, 1), (1, 1)},
        )
        self.assertEqual(
            {terminal.queued_counts for terminal in relation.terminals},
            {(1, 0), (0, 0)},
        )

    def test_q1_star_terminal_relation_is_three_unit_choices(self):
        relation = guarded_terminal_prefix_relation(
            (-1, -1, -1),
            (
                (2, 1, 1),
                (1, 2, 1),
                (1, 1, 2),
            ),
            (1, 1, 1),
        )
        self.assertFalse(relation.full_consumption_possible)
        self.assertEqual(
            {terminal.applied_counts for terminal in relation.terminals},
            {(1, 0, 0), (0, 1, 0), (0, 0, 1)},
        )
        self.assertEqual(
            {terminal.queued_counts for terminal in relation.terminals},
            {(0, 1, 1), (1, 0, 1), (1, 1, 0)},
        )
        self.assertEqual(
            {terminal.terminal_scores for terminal in relation.terminals},
            {
                (1, 0, 0),
                (0, 1, 0),
                (0, 0, 1),
            },
        )

    def test_prequantized_whole_queue_preserves_exact_material_ledger(self):
        network = ContactNetworkMomentum1D(
            masses=(1, 1, 1, 1),
            momenta=(1, 0, 0, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(0, 2, 1),
                ContactChannel1D(0, 3, 1),
            ),
        )
        reservoirs = tuple(
            ContactMaterialImpulseState(10, 1, 0)
            for _ in range(3)
        )
        tick = apply_contact_material_tick(
            network,
            reservoirs,
            (10, 10, 10),
        )
        self.assertEqual(tick.delivered_impulse_vector, (1, 1, 1))
        self.assertEqual(
            tuple(state.pending_numerator for state in tick.reservoir_after),
            (0, 0, 0),
        )

        relation = material_tick_causal_queue_relation(tick)
        self.assertTrue(relation.has_nonzero_queue)
        self.assertEqual(len(relation.outcomes), 3)
        for outcome in relation.outcomes:
            self.assertEqual(outcome.local_ledger_residuals, (0, 0, 0))
            for applied, queued in zip(
                outcome.terminal.applied_counts,
                outcome.terminal.queued_counts,
                strict=True,
            ):
                # Each channel produced exactly one whole quantum and zero
                # subquantum remainder: it must be either applied or queued.
                self.assertEqual(applied + queued, 1)

    def test_whole_queue_cannot_be_silently_folded_into_canonical_subquantum_remainder(self):
        network = ContactNetworkMomentum1D(
            masses=(1, 1, 1),
            momenta=(2, 1, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(0, 2, 1),
            ),
        )
        # Same-sign V coupling is positive.  Initial scores are (-1,-2), so one
        # legal schedule consumes both units while the other stops after contact 1.
        tick = apply_contact_material_tick(
            network,
            (
                ContactMaterialImpulseState(10, 1, 0),
                ContactMaterialImpulseState(10, 1, 0),
            ),
            (10, 10),
        )
        relation = material_tick_causal_queue_relation(tick)
        queued_outcome = next(
            outcome
            for outcome in relation.outcomes
            if outcome.terminal.queued_counts == (1, 0)
        )
        self.assertEqual(
            tick.reservoir_after[0].pending_numerator,
            0,
        )
        self.assertEqual(queued_outcome.terminal.queued_counts[0], 1)
        # Folding the queued whole quantum back into the canonical remainder
        # would require numerator amplitude itself, outside 0..A-1.
        self.assertEqual(
            tick.reservoir_before[0].amplitude
            * queued_outcome.terminal.queued_counts[0],
            10,
        )
        self.assertGreaterEqual(
            10,
            tick.reservoir_before[0].amplitude,
        )

    def test_z_realisable_target_has_no_early_terminal_under_any_legal_prefix(self):
        coupling = (
            (2, -1, 0),
            (-1, 2, -1),
            (0, -1, 2),
        )
        cases = (
            ((-1, -1, -1), (1, 1, 1)),
            ((-2, 0, -1), (1, 1, 0)),
            ((-1, -2, 0), (1, 1, 1)),
        )
        for initial, target in cases:
            relation = guarded_terminal_prefix_relation(
                initial,
                coupling,
                target,
            )
            if relation.full_consumption_possible:
                self.assertTrue(
                    relation.scheduler_independent_full_consumption,
                    (initial, target, relation.terminals),
                )

    def test_zero_budget_is_one_fully_consumed_terminal(self):
        relation = guarded_terminal_prefix_relation(
            (4, -2),
            ((2, 1), (1, 2)),
            (0, 0),
        )
        self.assertEqual(len(relation.terminals), 1)
        self.assertEqual(relation.terminals[0].applied_counts, (0, 0))
        self.assertEqual(relation.terminals[0].queued_counts, (0, 0))
        self.assertEqual(relation.terminals[0].representative_word, ())
        self.assertTrue(relation.scheduler_independent_full_consumption)

    def test_validation(self):
        with self.assertRaises(ValueError):
            guarded_terminal_prefix_relation((), (), ())
        with self.assertRaises(ValueError):
            guarded_terminal_prefix_relation((-1,), ((1,),), (-1,))
        with self.assertRaises(ValueError):
            guarded_terminal_prefix_relation((-1,), ((1, 0),), (1,))
        with self.assertRaises(TypeError):
            material_tick_causal_queue_relation(object())


if __name__ == "__main__":
    unittest.main()
