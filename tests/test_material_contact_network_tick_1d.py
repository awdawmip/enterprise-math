import unittest

from enterprise_math.material_contact_lifted_reservoir import (
    pooled_remainder_comparator,
)
from enterprise_math.material_contact_network_impulse_1d import (
    ContactChannel1D,
    ContactNetworkMomentum1D,
    contact_coupling_gram,
    contact_relative_scores,
)
from enterprise_math.material_contact_network_tick_1d import (
    ContactMaterialImpulseState,
    apply_contact_material_response_sequence,
    apply_contact_material_response_sequences,
    apply_contact_material_tick,
    contact_material_segmentation_invariant,
)


CHAIN = ContactNetworkMomentum1D(
    masses=(1, 1, 1),
    momenta=(3, 0, 0),
    contacts=(
        ContactChannel1D(0, 1, 1),
        ContactChannel1D(1, 2, 1),
    ),
)

STAR = ContactNetworkMomentum1D(
    masses=(1, 1, 1, 1),
    momenta=(3, 0, 0, 0),
    contacts=(
        ContactChannel1D(0, 1, 1),
        ContactChannel1D(0, 2, 1),
        ContactChannel1D(0, 3, 1),
    ),
)


def reservoirs(contact_count, amplitude=10, scale=2, pending=0):
    return tuple(
        ContactMaterialImpulseState(
            amplitude=amplitude,
            impulse_scale=scale,
            pending_numerator=pending,
        )
        for _ in range(contact_count)
    )


class MaterialContactNetworkTickTests(unittest.TestCase):
    def test_single_channel_sequence_obeys_exact_ledger(self):
        state = ContactMaterialImpulseState(
            amplitude=10,
            impulse_scale=2,
            pending_numerator=0,
        )
        sequence = apply_contact_material_response_sequence(
            state,
            (3, 3, 3, 3),
        )
        self.assertEqual(sequence.delivered_impulse_total, 2)
        self.assertEqual(sequence.after.pending_numerator, 4)
        self.assertEqual(
            10 * sequence.delivered_impulse_total
            + sequence.after.pending_numerator,
            2 * 12,
        )

    def test_bridge_wrapper_matches_canonical_quantizer_event_by_event(self):
        state = ContactMaterialImpulseState(10, 3, 7)
        sequence = apply_contact_material_response_sequence(state, (2, 1, 3))
        self.assertEqual(
            tuple(event.delivered_impulse for event in sequence.events),
            tuple(event.quantization.impulse_quanta for event in sequence.events),
        )
        self.assertEqual(sequence.after.pending_numerator, 5)
        self.assertEqual(sequence.delivered_impulse_total, 2)

    def test_two_subquantum_contacts_do_not_pool_before_network(self):
        tick = apply_contact_material_tick(
            CHAIN,
            reservoirs(2),
            (3, 3),
        )
        self.assertEqual(tick.delivered_impulse_vector, (0, 0))
        self.assertEqual(
            tuple(state.pending_numerator for state in tick.reservoir_after),
            (6, 6),
        )
        self.assertEqual(tick.after, CHAIN)

        pooled = pooled_remainder_comparator((6, 6), 10)
        self.assertEqual(pooled.pooled_delivered_quanta, 1)
        self.assertTrue(pooled.creates_spurious_delivered_quantum)

    def test_second_tick_delivers_each_contact_independently(self):
        first = apply_contact_material_tick(
            CHAIN,
            reservoirs(2),
            (3, 3),
        )
        second = apply_contact_material_tick(
            first.after,
            first.reservoir_after,
            (3, 3),
        )
        self.assertEqual(second.delivered_impulse_vector, (1, 1))
        self.assertEqual(
            tuple(state.pending_numerator for state in second.reservoir_after),
            (2, 2),
        )
        self.assertEqual(second.after.total_momentum, CHAIN.total_momentum)

    def test_network_update_matches_exact_Bj_and_Kj_identities(self):
        tick = apply_contact_material_response_sequences(
            CHAIN,
            reservoirs(2, amplitude=5, scale=2),
            (
                (2, 2),
                (1, 1, 1),
            ),
        )
        delivered = tick.delivered_impulse_vector
        self.assertEqual(delivered, (1, 1))

        before_scores = contact_relative_scores(CHAIN)
        after_scores = contact_relative_scores(tick.after)
        gram = contact_coupling_gram(CHAIN)
        expected = tuple(
            before_scores[row]
            + sum(
                gram[row][column] * delivered[column]
                for column in range(len(delivered))
            )
            for row in range(len(delivered))
        )
        self.assertEqual(after_scores, expected)
        self.assertEqual(tick.network_step.relative_scores_after, expected)
        self.assertEqual(tick.after.total_momentum, CHAIN.total_momentum)

    def test_response_segmentation_is_exactly_irrelevant_when_remainder_is_retained(self):
        left = (
            (1, 2, 3, 4),
            (3, 1, 2),
        )
        right = (
            (10,),
            (6,),
        )
        self.assertTrue(
            contact_material_segmentation_invariant(
                CHAIN,
                reservoirs(2, amplitude=10, scale=3),
                left,
                right,
            )
        )

    def test_segmentation_invariance_holds_with_nonzero_local_remainders(self):
        initial = (
            ContactMaterialImpulseState(10, 3, 7),
            ContactMaterialImpulseState(10, 2, 4),
        )
        self.assertTrue(
            contact_material_segmentation_invariant(
                CHAIN,
                initial,
                ((2, 1, 3), (4, 2)),
                ((6,), (6,)),
            )
        )

    def test_cross_contact_quantization_is_independent_before_batched_network_application(self):
        tick = apply_contact_material_response_sequences(
            STAR,
            reservoirs(3, amplitude=10, scale=3),
            (
                (1, 2, 3),
                (6,),
                (2, 2, 2),
            ),
        )
        self.assertEqual(tick.delivered_impulse_vector, (1, 1, 1))
        self.assertEqual(
            tuple(state.pending_numerator for state in tick.reservoir_after),
            (8, 8, 8),
        )
        self.assertEqual(tick.after.total_momentum, STAR.total_momentum)

    def test_empty_response_sequence_preserves_that_contact_reservoir(self):
        initial = reservoirs(2)
        tick = apply_contact_material_response_sequences(
            CHAIN,
            initial,
            ((), (3, 3)),
        )
        self.assertEqual(tick.channel_sequences[0].events, ())
        self.assertEqual(tick.reservoir_after[0], initial[0])
        self.assertEqual(tick.delivered_impulse_vector[0], 0)

    def test_different_contact_material_parameters_are_allowed(self):
        initial = (
            ContactMaterialImpulseState(10, 2, 0),
            ContactMaterialImpulseState(7, 3, 0),
        )
        tick = apply_contact_material_tick(
            CHAIN,
            initial,
            (5, 5),
        )
        self.assertEqual(tick.delivered_impulse_vector, (1, 2))
        self.assertEqual(
            tuple(state.pending_numerator for state in tick.reservoir_after),
            (0, 1),
        )

    def test_batched_tick_does_not_claim_guarded_causal_equivalence(self):
        tick = apply_contact_material_response_sequences(
            STAR,
            reservoirs(3, amplitude=2, scale=1),
            ((2,), (2,), (2,)),
        )
        self.assertEqual(tick.delivered_impulse_vector, (1, 1, 1))
        self.assertEqual(tick.after.total_momentum, STAR.total_momentum)

    def test_validation(self):
        with self.assertRaises(ValueError):
            ContactMaterialImpulseState(0, 1, 0)
        with self.assertRaises(ValueError):
            ContactMaterialImpulseState(10, 0, 0)
        with self.assertRaises(ValueError):
            ContactMaterialImpulseState(10, 1, 10)
        with self.assertRaises(ValueError):
            apply_contact_material_tick(
                CHAIN,
                reservoirs(1),
                (1, 1),
            )
        with self.assertRaises(ValueError):
            apply_contact_material_tick(
                CHAIN,
                reservoirs(2),
                (1,),
            )
        with self.assertRaises(ValueError):
            apply_contact_material_tick(
                CHAIN,
                reservoirs(2),
                (1, -1),
            )
        with self.assertRaises(ValueError):
            contact_material_segmentation_invariant(
                CHAIN,
                reservoirs(2),
                ((1,), (2,)),
                ((2,), (2,)),
            )


if __name__ == "__main__":
    unittest.main()
