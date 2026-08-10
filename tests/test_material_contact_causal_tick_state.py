import unittest

from enterprise_math.material_contact_causal_tick_state import (
    CausalMaterialContactState1D,
    accumulated_causal_material_ledger,
    causal_material_contact_tick,
)
from enterprise_math.material_contact_network_impulse_1d import (
    ContactChannel1D,
    ContactNetworkMomentum1D,
)
from enterprise_math.material_contact_network_tick_1d import (
    ContactMaterialImpulseState,
)


class MaterialContactCausalTickStateTests(unittest.TestCase):
    def test_path_new_budget_consumes_fully_and_matches_queue_zero(self):
        network = ContactNetworkMomentum1D(
            masses=(1, 1, 1),
            momenta=(2, 1, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(1, 2, 1),
            ),
        )
        state = CausalMaterialContactState1D(
            network=network,
            reservoirs=(
                ContactMaterialImpulseState(1, 1, 0),
                ContactMaterialImpulseState(1, 1, 0),
            ),
            whole_queue=(0, 0),
        )
        tick = causal_material_contact_tick(state, ((1,), (1,)))
        self.assertEqual(tick.newly_quantized, (1, 1))
        self.assertEqual(tick.available_whole_budget, (1, 1))
        self.assertTrue(tick.deterministic)
        self.assertTrue(tick.every_outcome_consumes_all_budget)
        outcome = tick.outcomes[0]
        self.assertEqual(outcome.applied_impulse_vector, (1, 1))
        self.assertEqual(outcome.after.whole_queue, (0, 0))
        self.assertEqual(outcome.local_ledger_residuals, (0, 0))
        self.assertEqual(outcome.after.network.momenta, (1, 1, 1))

    def test_star_tick_is_relation_valued_and_retains_two_whole_quanta(self):
        network = ContactNetworkMomentum1D(
            masses=(1, 1, 1, 1),
            momenta=(1, 0, 0, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(0, 2, 1),
                ContactChannel1D(0, 3, 1),
            ),
        )
        state = CausalMaterialContactState1D(
            network=network,
            reservoirs=tuple(
                ContactMaterialImpulseState(10, 1, 0)
                for _ in range(3)
            ),
            whole_queue=(0, 0, 0),
        )
        tick = causal_material_contact_tick(
            state,
            ((10,), (10,), (10,)),
        )
        self.assertEqual(tick.newly_quantized, (1, 1, 1))
        self.assertFalse(tick.deterministic)
        self.assertFalse(tick.every_outcome_consumes_all_budget)
        self.assertEqual(len(tick.outcomes), 3)
        self.assertEqual(
            {outcome.applied_impulse_vector for outcome in tick.outcomes},
            {(1, 0, 0), (0, 1, 0), (0, 0, 1)},
        )
        self.assertEqual(
            {outcome.after.whole_queue for outcome in tick.outcomes},
            {(0, 1, 1), (1, 0, 1), (1, 1, 0)},
        )
        for outcome in tick.outcomes:
            self.assertEqual(outcome.local_ledger_residuals, (0, 0, 0))
            self.assertEqual(sum(outcome.applied_impulse_vector), 1)
            self.assertEqual(sum(outcome.after.whole_queue), 2)

    def test_new_material_on_helper_contact_releases_old_z_path_causal_debt(self):
        # Initial scores are (-1,0).  Old queue on contact 1 cannot move alone.
        # New contact-0 material produces one whole quantum; applying it first
        # changes contact 1 score by -1 and releases the old queued quantum.
        network = ContactNetworkMomentum1D(
            masses=(1, 1, 1),
            momenta=(1, 0, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(1, 2, 1),
            ),
        )
        state = CausalMaterialContactState1D(
            network=network,
            reservoirs=(
                ContactMaterialImpulseState(1, 1, 0),
                ContactMaterialImpulseState(1, 1, 0),
            ),
            whole_queue=(0, 1),
        )
        tick = causal_material_contact_tick(state, ((1,), (0,)))
        self.assertEqual(tick.newly_quantized, (1, 0))
        self.assertEqual(tick.available_whole_budget, (1, 1))
        self.assertTrue(tick.deterministic)
        outcome = tick.outcomes[0]
        self.assertEqual(outcome.applied_impulse_vector, (1, 1))
        self.assertEqual(outcome.after.whole_queue, (0, 0))
        self.assertEqual(outcome.after.network.momenta, (0, 0, 1))
        self.assertEqual(outcome.local_ledger_residuals, (0, 0))

    def test_extra_material_can_create_new_causal_queue_even_when_smaller_budget_was_consumable(self):
        network = ContactNetworkMomentum1D(
            masses=(1, 1, 1),
            momenta=(2, 1, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(1, 2, 1),
            ),
        )
        state = CausalMaterialContactState1D(
            network=network,
            reservoirs=(
                ContactMaterialImpulseState(1, 1, 0),
                ContactMaterialImpulseState(1, 1, 0),
            ),
            whole_queue=(1, 1),
        )
        tick = causal_material_contact_tick(state, ((1,), (0,)))
        self.assertEqual(tick.available_whole_budget, (2, 1))
        self.assertTrue(tick.deterministic)
        outcome = tick.outcomes[0]
        self.assertEqual(outcome.applied_impulse_vector, (1, 1))
        self.assertEqual(outcome.after.whole_queue, (1, 0))
        self.assertEqual(outcome.local_ledger_residuals, (0, 0))

    def test_stuck_queue_persists_without_external_or_new_enabling_action(self):
        network = ContactNetworkMomentum1D(
            masses=(1, 1, 1),
            momenta=(1, 0, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(1, 2, 1),
            ),
        )
        state = CausalMaterialContactState1D(
            network=network,
            reservoirs=(
                ContactMaterialImpulseState(1, 1, 0),
                ContactMaterialImpulseState(1, 1, 0),
            ),
            whole_queue=(0, 1),
        )
        tick = causal_material_contact_tick(state, ((), ()))
        self.assertEqual(tick.newly_quantized, (0, 0))
        self.assertTrue(tick.deterministic)
        outcome = tick.outcomes[0]
        self.assertEqual(outcome.applied_impulse_vector, (0, 0))
        self.assertEqual(outcome.after.whole_queue, (0, 1))
        self.assertEqual(outcome.after.network, network)

    def test_two_tick_scalar_telescope_with_queue(self):
        # Tick 1: one whole quantum is generated but remains queued.
        # Tick 2: a helper event changes the causal network and permits eventual
        # consumption.  The aggregate scalar identity is independent of that
        # intermediate causal allocation.
        self.assertTrue(
            accumulated_causal_material_ledger(
                initial_queue=0,
                initial_remainder=0,
                amplitude=10,
                impulse_scale=2,
                response_total=13,
                applied_total=2,
                final_queue=0,
                final_remainder=6,
            )
        )
        self.assertFalse(
            accumulated_causal_material_ledger(
                initial_queue=0,
                initial_remainder=0,
                amplitude=10,
                impulse_scale=2,
                response_total=13,
                applied_total=1,
                final_queue=0,
                final_remainder=6,
            )
        )

    def test_zero_new_material_still_attempts_old_queue(self):
        network = ContactNetworkMomentum1D(
            masses=(1, 1),
            momenta=(1, 0),
            contacts=(ContactChannel1D(0, 1, 1),),
        )
        state = CausalMaterialContactState1D(
            network=network,
            reservoirs=(ContactMaterialImpulseState(10, 1, 3),),
            whole_queue=(1,),
        )
        tick = causal_material_contact_tick(state, ((),))
        self.assertEqual(tick.newly_quantized, (0,))
        self.assertEqual(tick.available_whole_budget, (1,))
        outcome = tick.outcomes[0]
        self.assertEqual(outcome.applied_impulse_vector, (1,))
        self.assertEqual(outcome.after.whole_queue, (0,))
        self.assertEqual(outcome.after.reservoirs[0].pending_numerator, 3)

    def test_validation(self):
        network = ContactNetworkMomentum1D(
            masses=(1, 1),
            momenta=(1, 0),
            contacts=(ContactChannel1D(0, 1, 1),),
        )
        with self.assertRaises(ValueError):
            CausalMaterialContactState1D(
                network=network,
                reservoirs=(),
                whole_queue=(0,),
            )
        with self.assertRaises(ValueError):
            CausalMaterialContactState1D(
                network=network,
                reservoirs=(ContactMaterialImpulseState(1, 1, 0),),
                whole_queue=(-1,),
            )
        state = CausalMaterialContactState1D(
            network=network,
            reservoirs=(ContactMaterialImpulseState(1, 1, 0),),
            whole_queue=(0,),
        )
        with self.assertRaises(ValueError):
            causal_material_contact_tick(state, ())
        with self.assertRaises(ValueError):
            accumulated_causal_material_ledger(
                0, 0, 0, 1, 0, 0, 0, 0
            )


if __name__ == "__main__":
    unittest.main()
