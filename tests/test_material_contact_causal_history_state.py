import unittest

from enterprise_math.contact_cycle_witness_repair import apply_integer_matrix
from enterprise_math.material_contact_causal_history_state import (
    history_aware_causal_material_tick,
    history_state_from_exact_applied_history,
    reconstruct_applied_history_witness,
    reconstruct_committed_history_witness,
    transform_history_state_gauge,
)
from enterprise_math.material_contact_causal_tick_state import (
    CausalMaterialContactState1D,
)
from enterprise_math.material_contact_network_impulse_1d import (
    ContactChannel1D,
    ContactNetworkMomentum1D,
    apply_contact_impulse_vector,
    contact_incidence_matrix,
)
from enterprise_math.material_contact_network_tick_1d import (
    ContactMaterialImpulseState,
)


def reservoirs(count, amplitude=1, scale=1, pending=0):
    return tuple(
        ContactMaterialImpulseState(amplitude, scale, pending)
        for _ in range(count)
    )


class MaterialContactCausalHistoryStateTests(unittest.TestCase):
    def test_tree_history_has_zero_cycle_repair_but_exact_witness_reconstructs(self):
        network = ContactNetworkMomentum1D(
            masses=(1, 1, 1),
            momenta=(3, 1, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(1, 2, 1),
            ),
        )
        causal = CausalMaterialContactState1D(
            network=network,
            reservoirs=reservoirs(2),
            whole_queue=(0, 0),
        )
        history = (2, 3)
        witness = ((1, 1),)
        state = history_state_from_exact_applied_history(
            causal,
            history,
            witness,
            (0, 1),
        )
        self.assertEqual(state.history_repair, (0,))
        self.assertEqual(
            reconstruct_applied_history_witness(state, witness, (0, 1)),
            (5,),
        )

    def test_triangle_cycle_history_is_carried_only_by_repair_at_zero_body_delta(self):
        network = ContactNetworkMomentum1D(
            masses=(1, 1, 1),
            momenta=(0, 0, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(1, 2, 1),
                ContactChannel1D(2, 0, 1),
            ),
        )
        causal = CausalMaterialContactState1D(
            network=network,
            reservoirs=reservoirs(3),
            whole_queue=(1, 0, 0),
        )
        witness = ((1, 1, 1),)
        state = history_state_from_exact_applied_history(
            causal,
            (1, 1, 1),
            witness,
            (0, 1),
        )
        self.assertEqual(state.applied_body_delta, (0, 0, 0))
        self.assertEqual(state.history_repair, (3,))
        self.assertEqual(
            reconstruct_applied_history_witness(state, witness, (0, 1)),
            (3,),
        )
        self.assertEqual(
            reconstruct_committed_history_witness(state, witness, (0, 1)),
            (4,),
        )

    def test_applied_history_can_branch_while_committed_history_is_scheduler_independent(self):
        # Same-sign V: r=(-1,-2), K=[[2,1],[1,2]].  Budget (1,1) has
        # one full-consumption terminal and one terminal with queue (1,0).
        network = ContactNetworkMomentum1D(
            masses=(1, 1, 1),
            momenta=(2, 1, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(0, 2, 1),
            ),
        )
        causal = CausalMaterialContactState1D(
            network=network,
            reservoirs=reservoirs(2),
            whole_queue=(0, 0),
        )
        witness = ((1, 1),)
        state = history_state_from_exact_applied_history(
            causal,
            (0, 0),
            witness,
            (0, 1),
        )
        relation = history_aware_causal_material_tick(
            state,
            ((1,), (1,)),
            witness,
            (0, 1),
        )
        self.assertEqual(relation.newly_quantized, (1, 1))
        self.assertFalse(relation.applied_history_scheduler_independent)
        self.assertTrue(relation.committed_history_scheduler_independent)
        self.assertEqual(
            {outcome.applied_witness_increment for outcome in relation.outcomes},
            {(1,), (2,)},
        )
        self.assertEqual(
            {outcome.committed_witness_increment for outcome in relation.outcomes},
            {(2,)},
        )
        self.assertEqual(
            {outcome.after.causal.whole_queue for outcome in relation.outcomes},
            {(1, 0), (0, 0)},
        )

    def test_committed_increment_is_CJ_for_vector_witness_on_every_branch(self):
        network = ContactNetworkMomentum1D(
            masses=(1, 1, 1),
            momenta=(2, 1, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(0, 2, 1),
            ),
        )
        causal = CausalMaterialContactState1D(
            network=network,
            reservoirs=reservoirs(2),
            whole_queue=(1, 0),
        )
        witness = (
            (1, 0),
            (0, 1),
            (2, -3),
        )
        state = history_state_from_exact_applied_history(
            causal,
            (2, 1),
            witness,
            (0, 1),
        )
        relation = history_aware_causal_material_tick(
            state,
            ((1,), (1,)),
            witness,
            (0, 1),
        )
        expected = apply_integer_matrix(witness, relation.newly_quantized)
        self.assertTrue(relation.committed_history_scheduler_independent)
        for outcome in relation.outcomes:
            self.assertEqual(outcome.committed_witness_increment, expected)
            self.assertEqual(
                tuple(
                    after - before
                    for before, after in zip(
                        outcome.applied_witness_before,
                        outcome.applied_witness_after,
                        strict=True,
                    )
                ),
                outcome.applied_witness_increment,
            )

    def test_triangle_chord_application_changes_repair_but_reconstructs_one_applied_unit(self):
        base = ContactNetworkMomentum1D(
            masses=(1, 1, 1),
            momenta=(2, 1, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(1, 2, 1),
                ContactChannel1D(2, 0, 1),
            ),
        )
        causal = CausalMaterialContactState1D(
            network=base,
            reservoirs=reservoirs(3),
            whole_queue=(0, 0, 0),
        )
        witness = ((1, 1, 1),)
        # Choose tree edges (1,2), so edge 0 is the chord.  Edge 0 is closing
        # at the chosen momentum state and one new quantum can be applied.
        state = history_state_from_exact_applied_history(
            causal,
            (0, 0, 0),
            witness,
            (1, 2),
        )
        relation = history_aware_causal_material_tick(
            state,
            ((1,), (0,), (0,)),
            witness,
            (1, 2),
        )
        self.assertEqual(len(relation.outcomes), 1)
        outcome = relation.outcomes[0]
        self.assertEqual(outcome.causal_outcome.applied_impulse_vector, (1, 0, 0))
        self.assertEqual(outcome.repair_increment, (3,))
        self.assertEqual(outcome.applied_witness_increment, (1,))
        self.assertEqual(outcome.after.history_repair, (3,))
        self.assertEqual(
            reconstruct_applied_history_witness(
                outcome.after,
                witness,
                (1, 2),
            ),
            (1,),
        )

    def test_coboundary_witness_needs_no_cycle_repair_even_on_triangle(self):
        network = ContactNetworkMomentum1D(
            masses=(1, 1, 1),
            momenta=(0, 0, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(1, 2, 1),
                ContactChannel1D(2, 0, 1),
            ),
        )
        causal = CausalMaterialContactState1D(
            network=network,
            reservoirs=reservoirs(3),
            whole_queue=(0, 0, 0),
        )
        # For phi=(0,1,0), c=B^T phi=(1,-1,0), a coboundary.
        witness = ((1, -1, 0),)
        for history in ((1, 1, 1), (3, 2, 4), (0, 5, 1)):
            state = history_state_from_exact_applied_history(
                causal,
                history,
                witness,
                (0, 1),
            )
            self.assertEqual(state.history_repair, (0,))
            expected = apply_integer_matrix(witness, history)
            self.assertEqual(
                reconstruct_applied_history_witness(state, witness, (0, 1)),
                expected,
            )

    def test_forest_gauge_changes_repair_coordinate_not_witness(self):
        base = ContactNetworkMomentum1D(
            masses=(1, 1, 1),
            momenta=(2, 1, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(1, 2, 1),
                ContactChannel1D(2, 0, 1),
            ),
        )
        # Apply edge 0 once to make the causal network consistent with history e0.
        after_e0 = apply_contact_impulse_vector(base, (1, 0, 0)).after
        causal = CausalMaterialContactState1D(
            network=after_e0,
            reservoirs=reservoirs(3),
            whole_queue=(0, 0, 1),
        )
        witness = ((1, 1, 1),)
        source = history_state_from_exact_applied_history(
            causal,
            (1, 0, 0),
            witness,
            (1, 2),
        )
        target = transform_history_state_gauge(
            source,
            witness,
            (1, 2),
            (0, 2),
        )
        self.assertNotEqual(source.history_repair, target.history_repair)
        self.assertEqual(
            reconstruct_applied_history_witness(source, witness, (1, 2)),
            reconstruct_applied_history_witness(target, witness, (0, 2)),
        )
        self.assertEqual(
            reconstruct_committed_history_witness(source, witness, (1, 2)),
            reconstruct_committed_history_witness(target, witness, (0, 2)),
        )

        # Edge 1 is now closing.  Advance both gauges through the same new event;
        # reconstructed futures remain identical though repair increments differ.
        source_tick = history_aware_causal_material_tick(
            source,
            ((0,), (1,), (0,)),
            witness,
            (1, 2),
        )
        target_tick = history_aware_causal_material_tick(
            target,
            ((0,), (1,), (0,)),
            witness,
            (0, 2),
        )
        self.assertEqual(len(source_tick.outcomes), 1)
        self.assertEqual(len(target_tick.outcomes), 1)
        self.assertEqual(
            source_tick.outcomes[0].applied_witness_after,
            target_tick.outcomes[0].applied_witness_after,
        )
        self.assertEqual(
            source_tick.outcomes[0].committed_witness_after,
            target_tick.outcomes[0].committed_witness_after,
        )

    def test_queue_is_exact_difference_between_committed_and_applied_witness(self):
        network = ContactNetworkMomentum1D(
            masses=(1, 1, 1),
            momenta=(0, 0, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(1, 2, 1),
            ),
        )
        causal = CausalMaterialContactState1D(
            network=network,
            reservoirs=reservoirs(2),
            whole_queue=(2, 3),
        )
        witness = ((2, -1),)
        state = history_state_from_exact_applied_history(
            causal,
            (4, 1),
            witness,
            (0, 1),
        )
        applied = reconstruct_applied_history_witness(state, witness, (0, 1))
        committed = reconstruct_committed_history_witness(state, witness, (0, 1))
        queue_witness = apply_integer_matrix(witness, (2, 3))
        self.assertEqual(
            committed,
            tuple(
                a + q for a, q in zip(applied, queue_witness, strict=True)
            ),
        )

    def test_validation(self):
        network = ContactNetworkMomentum1D(
            masses=(1, 1),
            momenta=(0, 0),
            contacts=(ContactChannel1D(0, 1, 1),),
        )
        causal = CausalMaterialContactState1D(
            network=network,
            reservoirs=reservoirs(1),
            whole_queue=(0,),
        )
        with self.assertRaises(ValueError):
            history_state_from_exact_applied_history(
                causal,
                (0, 0),
                ((1,),),
                (0,),
            )
        state = history_state_from_exact_applied_history(
            causal,
            (0,),
            ((1,),),
            (0,),
        )
        with self.assertRaises(ValueError):
            reconstruct_applied_history_witness(
                state,
                ((1, 2),),
                (0,),
            )
        with self.assertRaises(TypeError):
            history_aware_causal_material_tick(
                object(),
                ((0,),),
                ((1,),),
                (0,),
            )


if __name__ == "__main__":
    unittest.main()
