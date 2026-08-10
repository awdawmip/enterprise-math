import unittest

from enterprise_math.material_contact_network_impulse_1d import (
    ContactChannel1D,
    ContactNetworkMomentum1D,
)
from enterprise_math.material_contact_network_tick_1d import ContactMaterialImpulseState
from enterprise_math.material_contact_queue_age_precision import (
    ContactWholeQueueAgeState,
)
from enterprise_math.material_contact_ttl_loss_ledger import (
    TTLMaterialContactState1D,
    accumulated_ttl_material_ledger,
    ttl_material_contact_tick,
)


class MaterialContactTTLLossLedgerTests(unittest.TestCase):
    def test_fifo_lifo_same_current_impulse_can_have_different_ttl_loss(self):
        network = ContactNetworkMomentum1D(
            masses=(1, 1),
            momenta=(1, 0),
            contacts=(ContactChannel1D(0, 1, 1),),
        )
        state = TTLMaterialContactState1D(
            network=network,
            reservoirs=(ContactMaterialImpulseState(10, 1, 0),),
            age_queues=(ContactWholeQueueAgeState((1, 0, 1)),),
        )

        fifo = ttl_material_contact_tick(state, ((),), ("FIFO",))
        lifo = ttl_material_contact_tick(state, ((),), ("LIFO",))
        self.assertEqual(len(fifo.outcomes), 1)
        self.assertEqual(len(lifo.outcomes), 1)
        fifo_out = fifo.outcomes[0]
        lifo_out = lifo.outcomes[0]

        self.assertEqual(fifo_out.applied_impulse_vector, (1,))
        self.assertEqual(lifo_out.applied_impulse_vector, (1,))
        self.assertEqual(fifo_out.after.network, lifo_out.after.network)
        self.assertEqual(fifo_out.after.network.momenta, (0, 1))

        self.assertEqual(fifo_out.expired_whole_vector, (0,))
        self.assertEqual(lifo_out.expired_whole_vector, (1,))
        self.assertEqual(fifo_out.after.whole_queue, (1,))
        self.assertEqual(lifo_out.after.whole_queue, (0,))
        self.assertEqual(fifo_out.omitted_expiry_defects, (0,))
        self.assertEqual(lifo_out.omitted_expiry_defects, (10,))
        self.assertEqual(fifo_out.local_ledger_residuals, (0,))
        self.assertEqual(lifo_out.local_ledger_residuals, (0,))

    def test_expiry_without_application_moves_whole_impulse_to_loss_sink(self):
        network = ContactNetworkMomentum1D(
            masses=(1, 1),
            momenta=(0, 1),
            contacts=(ContactChannel1D(0, 1, 1),),
        )
        state = TTLMaterialContactState1D(
            network=network,
            reservoirs=(ContactMaterialImpulseState(7, 2, 3),),
            age_queues=(ContactWholeQueueAgeState((0, 0, 1)),),
        )
        tick = ttl_material_contact_tick(state, ((),), ("FIFO",))
        outcome = tick.outcomes[0]
        self.assertEqual(outcome.applied_impulse_vector, (0,))
        self.assertEqual(outcome.expired_whole_vector, (1,))
        self.assertEqual(outcome.after.whole_queue, (0,))
        self.assertEqual(outcome.after.network, network)
        self.assertEqual(outcome.after.reservoirs[0].pending_numerator, 3)
        self.assertEqual(outcome.omitted_expiry_defects, (7,))
        self.assertEqual(outcome.local_ledger_residuals, (0,))

    def test_new_material_quantization_and_ttl_sink_close_same_tick_ledger(self):
        network = ContactNetworkMomentum1D(
            masses=(1, 1),
            momenta=(1, 0),
            contacts=(ContactChannel1D(0, 1, 1),),
        )
        state = TTLMaterialContactState1D(
            network=network,
            reservoirs=(ContactMaterialImpulseState(10, 2, 4),),
            age_queues=(ContactWholeQueueAgeState((0, 0, 1)),),
        )
        # response 3 contributes raw numerator 6; old delta 4 makes one new whole
        # quantum and resets subquantum remainder to zero.  Available whole budget
        # is therefore 2, but the one-contact closing guard permits only one unit.
        tick = ttl_material_contact_tick(state, ((3,),), ("FIFO",))
        self.assertEqual(tick.newly_quantized, (1,))
        outcome = tick.outcomes[0]
        self.assertEqual(outcome.applied_impulse_vector, (1,))
        self.assertEqual(outcome.after.reservoirs[0].pending_numerator, 0)
        # FIFO consumes the old age-2 unit, leaving the new age-0 unit to age.
        self.assertEqual(outcome.expired_whole_vector, (0,))
        self.assertEqual(outcome.after.whole_queue, (1,))
        self.assertEqual(outcome.local_ledger_residuals, (0,))
        self.assertEqual(outcome.omitted_expiry_defects, (0,))

    def test_lifo_same_tick_can_expire_old_unit_instead_of_new_unit(self):
        network = ContactNetworkMomentum1D(
            masses=(1, 1),
            momenta=(1, 0),
            contacts=(ContactChannel1D(0, 1, 1),),
        )
        state = TTLMaterialContactState1D(
            network=network,
            reservoirs=(ContactMaterialImpulseState(10, 2, 4),),
            age_queues=(ContactWholeQueueAgeState((0, 0, 1)),),
        )
        fifo = ttl_material_contact_tick(state, ((3,),), ("FIFO",)).outcomes[0]
        lifo = ttl_material_contact_tick(state, ((3,),), ("LIFO",)).outcomes[0]
        self.assertEqual(fifo.applied_impulse_vector, lifo.applied_impulse_vector)
        self.assertEqual(fifo.after.network, lifo.after.network)
        self.assertEqual(fifo.expired_whole_vector, (0,))
        self.assertEqual(lifo.expired_whole_vector, (1,))
        self.assertEqual(fifo.after.whole_queue, (1,))
        self.assertEqual(lifo.after.whole_queue, (0,))
        self.assertEqual(lifo.omitted_expiry_defects, (10,))

    def test_multicontact_each_local_ledger_closes_independently(self):
        network = ContactNetworkMomentum1D(
            masses=(1, 1, 1),
            momenta=(2, 1, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(1, 2, 1),
            ),
        )
        state = TTLMaterialContactState1D(
            network=network,
            reservoirs=(
                ContactMaterialImpulseState(10, 2, 4),
                ContactMaterialImpulseState(7, 3, 1),
            ),
            age_queues=(
                ContactWholeQueueAgeState((1, 0, 0)),
                ContactWholeQueueAgeState((0, 1, 0)),
            ),
        )
        relation = ttl_material_contact_tick(
            state,
            ((3,), (2,)),
            ("FIFO", "LIFO"),
        )
        for outcome in relation.outcomes:
            self.assertEqual(outcome.local_ledger_residuals, (0, 0))
            self.assertEqual(
                outcome.after.network.total_momentum,
                network.total_momentum,
            )
            for defect, reservoir, expired in zip(
                outcome.omitted_expiry_defects,
                state.reservoirs,
                outcome.expired_whole_vector,
                strict=True,
            ):
                self.assertEqual(defect, reservoir.amplitude * expired)

    def test_accumulated_telescope_requires_expired_sink(self):
        # Initial whole content is 2 and new raw numerator 26 plus remainder 4
        # produces three more whole quanta.  With 2 applied and 1 expired, two
        # whole quanta must remain queued.
        self.assertTrue(
            accumulated_ttl_material_ledger(
                initial_queue=2,
                initial_remainder=4,
                amplitude=10,
                impulse_scale=2,
                response_total=13,
                applied_total=2,
                expired_total=1,
                final_queue=2,
                final_remainder=0,
            )
        )
        self.assertFalse(
            accumulated_ttl_material_ledger(
                initial_queue=2,
                initial_remainder=4,
                amplitude=10,
                impulse_scale=2,
                response_total=13,
                applied_total=2,
                expired_total=0,
                final_queue=2,
                final_remainder=0,
            )
        )

    def test_zero_expiry_reduces_to_parent_causal_material_telescope(self):
        # Q0=1, delta0=3 and raw increment 12 yield one new whole quantum,
        # remainder 5.  After applying one, one whole quantum remains queued.
        self.assertTrue(
            accumulated_ttl_material_ledger(
                initial_queue=1,
                initial_remainder=3,
                amplitude=10,
                impulse_scale=2,
                response_total=6,
                applied_total=1,
                expired_total=0,
                final_queue=1,
                final_remainder=5,
            )
        )

    def test_validation(self):
        network = ContactNetworkMomentum1D(
            masses=(1, 1),
            momenta=(1, 0),
            contacts=(ContactChannel1D(0, 1, 1),),
        )
        with self.assertRaises(ValueError):
            TTLMaterialContactState1D(
                network=network,
                reservoirs=(),
                age_queues=(ContactWholeQueueAgeState((0,)),),
            )
        state = TTLMaterialContactState1D(
            network=network,
            reservoirs=(ContactMaterialImpulseState(1, 1, 0),),
            age_queues=(ContactWholeQueueAgeState((0,)),),
        )
        with self.assertRaises(ValueError):
            ttl_material_contact_tick(state, ((),), ())
        with self.assertRaises(ValueError):
            ttl_material_contact_tick(state, ((),), ("RANDOM",))
        with self.assertRaises(ValueError):
            accumulated_ttl_material_ledger(
                initial_queue=0,
                initial_remainder=0,
                amplitude=0,
                impulse_scale=1,
                response_total=0,
                applied_total=0,
                expired_total=0,
                final_queue=0,
                final_remainder=0,
            )


if __name__ == "__main__":
    unittest.main()
