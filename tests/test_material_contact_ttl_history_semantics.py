import unittest

from enterprise_math.material_contact_network_impulse_1d import (
    ContactChannel1D,
    ContactNetworkMomentum1D,
)
from enterprise_math.material_contact_network_tick_1d import ContactMaterialImpulseState
from enterprise_math.material_contact_queue_age_precision import ContactWholeQueueAgeState
from enterprise_math.material_contact_ttl_history_semantics import (
    ttl_history_relation_report,
    ttl_history_witness_increment,
)
from enterprise_math.material_contact_ttl_loss_ledger import (
    TTLMaterialContactState1D,
    ttl_material_contact_tick,
)


def empty_age_queues(count, depth=2):
    return tuple(
        ContactWholeQueueAgeState((0,) * depth)
        for _ in range(count)
    )


def unit_reservoirs(count):
    return tuple(ContactMaterialImpulseState(1, 1, 0) for _ in range(count))


class MaterialContactTTLHistorySemanticsTests(unittest.TestCase):
    def test_positive_v_scheduler_splits_applied_but_not_live_or_ever_history(self):
        network = ContactNetworkMomentum1D(
            masses=(1, 1, 1),
            momenta=(2, 1, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(0, 2, 1),
            ),
        )
        state = TTLMaterialContactState1D(
            network=network,
            reservoirs=unit_reservoirs(2),
            age_queues=empty_age_queues(2),
        )
        relation = ttl_material_contact_tick(
            state,
            ((1,), (1,)),
            ("FIFO", "FIFO"),
        )
        self.assertEqual(len(relation.outcomes), 2)
        self.assertEqual(
            {outcome.applied_impulse_vector for outcome in relation.outcomes},
            {(0, 1), (1, 1)},
        )
        self.assertEqual(
            {outcome.expired_whole_vector for outcome in relation.outcomes},
            {(0, 0)},
        )

        report = ttl_history_relation_report(relation, ((1, 1),))
        self.assertEqual(set(report.applied_values), {(1,), (2,)})
        self.assertEqual(report.live_committed_values, ((2,),))
        self.assertEqual(report.ever_quantized_values, ((2,),))
        self.assertFalse(report.applied_scheduler_independent)
        self.assertTrue(report.live_committed_policy_independent)
        self.assertTrue(report.ever_quantized_policy_independent)

    def test_q1_star_total_applied_history_is_scheduler_independent(self):
        network = ContactNetworkMomentum1D(
            masses=(1, 1, 1, 1),
            momenta=(1, 0, 0, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(0, 2, 1),
                ContactChannel1D(0, 3, 1),
            ),
        )
        state = TTLMaterialContactState1D(
            network=network,
            reservoirs=unit_reservoirs(3),
            age_queues=empty_age_queues(3),
        )
        relation = ttl_material_contact_tick(
            state,
            ((1,), (1,), (1,)),
            ("FIFO", "FIFO", "FIFO"),
        )
        self.assertEqual(len(relation.outcomes), 3)
        report = ttl_history_relation_report(
            relation,
            ((1, 1, 1),),
        )
        self.assertEqual(report.applied_values, ((1,),))
        self.assertEqual(report.live_committed_values, ((3,),))
        self.assertEqual(report.ever_quantized_values, ((3,),))
        self.assertTrue(report.applied_scheduler_independent)

    def test_fifo_lifo_can_split_live_history_with_same_applied_history(self):
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
        fifo_report = ttl_history_relation_report(fifo, ((1,),))
        lifo_report = ttl_history_relation_report(lifo, ((1,),))

        self.assertEqual(fifo_report.applied_values, ((1,),))
        self.assertEqual(lifo_report.applied_values, ((1,),))
        self.assertEqual(fifo_report.live_committed_values, ((0,),))
        self.assertEqual(lifo_report.live_committed_values, ((-1,),))
        self.assertEqual(fifo_report.ever_quantized_values, ((0,),))
        self.assertEqual(lifo_report.ever_quantized_values, ((0,),))

    def test_history_increment_closed_forms_allow_old_queue_expiry(self):
        # J-x may be negative when TTL removes old queued content; that is an
        # exact decrease of the live-commitment ledger, not an invalid count.
        increment = ttl_history_witness_increment(
            ((2,),),
            newly_quantized=(0,),
            applied=(1,),
            expired=(3,),
        )
        self.assertEqual(increment.applied, (2,))
        self.assertEqual(increment.live_committed, (-6,))
        self.assertEqual(increment.ever_quantized, (0,))

    def test_ever_quantized_history_depends_only_on_J_for_vector_readout(self):
        witness = (
            (1, 0),
            (0, 1),
            (2, -3),
        )
        expected = (4, 5, -7)
        cases = (
            ((4, 5), (0, 0)),
            ((2, 3), (1, 0)),
            ((0, 5), (4, 0)),
            ((1, 1), (0, 4)),
        )
        for applied, expired in cases:
            increment = ttl_history_witness_increment(
                witness,
                newly_quantized=(4, 5),
                applied=applied,
                expired=expired,
            )
            self.assertEqual(increment.ever_quantized, expected)

    def test_zero_expiry_reduces_live_history_to_ever_quantized_increment(self):
        witness = ((3, -2),)
        for applied in ((0, 0), (1, 0), (0, 2), (3, 4)):
            increment = ttl_history_witness_increment(
                witness,
                newly_quantized=(3, 4),
                applied=applied,
                expired=(0, 0),
            )
            self.assertEqual(
                increment.live_committed,
                increment.ever_quantized,
            )

    def test_validation(self):
        with self.assertRaises(ValueError):
            ttl_history_witness_increment(
                (),
                (1,),
                (1,),
                (0,),
            )
        with self.assertRaises(ValueError):
            ttl_history_witness_increment(
                ((1, 2),),
                (1,),
                (1,),
                (0,),
            )
        with self.assertRaises(ValueError):
            ttl_history_witness_increment(
                ((1,),),
                (-1,),
                (0,),
                (0,),
            )
        with self.assertRaises(TypeError):
            ttl_history_relation_report(object(), ((1,),))


if __name__ == "__main__":
    unittest.main()
