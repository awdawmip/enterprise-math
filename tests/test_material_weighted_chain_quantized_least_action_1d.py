import itertools
import unittest

from enterprise_math.material_contact_network_impulse_1d import (
    ContactChannel1D,
    ContactNetworkMomentum1D,
    contact_relative_scores,
)
from enterprise_math.material_weighted_chain_least_action_1d import (
    solve_weighted_chain_least_action,
)
from enterprise_math.material_weighted_chain_quantized_least_action_1d import (
    MATERIAL_CHAIN_RESOLVED,
    MATERIAL_CHANNEL_STALLED,
    ContactMaterialUnitChannel1D,
    solve_weighted_chain_quantized_least_action,
)


def chain_state(masses, momenta):
    masses = tuple(masses)
    momenta = tuple(momenta)
    return ContactNetworkMomentum1D(
        masses=masses,
        momenta=momenta,
        contacts=tuple(
            ContactChannel1D(index, index + 1, 1)
            for index in range(len(masses) - 1)
        ),
    )


def subquantum_channel(initial_detail=0):
    return ContactMaterialUnitChannel1D(
        amplitude=10,
        response_sample=3,
        impulse_scale_magnitude=2,
        initial_detail=initial_detail,
    )


class MaterialWeightedChainQuantizedLeastAction1DTests(unittest.TestCase):
    def test_reference_chain_has_exact_schedule_independent_material_event_counts(self):
        state = chain_state((2, 3, 5), (6, 6, 0))
        channels = (subquantum_channel(), subquantum_channel())
        left = solve_weighted_chain_quantized_least_action(
            state, channels, priority=(0, 1), retain_detail=True
        )
        right = solve_weighted_chain_quantized_least_action(
            state, channels, priority=(1, 0), retain_detail=True
        )
        self.assertEqual(left.status, MATERIAL_CHAIN_RESOLVED)
        self.assertEqual(right.status, MATERIAL_CHAIN_RESOLVED)
        self.assertEqual(left.impulse_vector, (4, 7))
        self.assertEqual(right.impulse_vector, (4, 7))
        self.assertEqual(left.evaluations_per_contact, (7, 12))
        self.assertEqual(right.evaluations_per_contact, (7, 12))
        self.assertEqual(left.expected_evaluations_per_contact, (7, 12))
        self.assertEqual(right.expected_evaluations_per_contact, (7, 12))
        self.assertEqual(left.total_material_evaluations, 19)
        self.assertEqual(right.total_material_evaluations, 19)
        self.assertEqual(left.final_details, (2, 2))
        self.assertEqual(right.final_details, (2, 2))
        self.assertEqual(left.final_scores, right.final_scores)
        self.assertNotEqual(
            tuple(event.contact_index for event in left.events),
            tuple(event.contact_index for event in right.events),
        )

    def test_initial_pending_detail_reduces_exact_evaluation_count_without_changing_final_impulse(self):
        state = chain_state((2, 3, 5), (6, 6, 0))
        channels = (subquantum_channel(initial_detail=4), subquantum_channel())
        report = solve_weighted_chain_quantized_least_action(state, channels)
        self.assertEqual(report.impulse_vector, (4, 7))
        self.assertEqual(report.evaluations_per_contact, (6, 12))
        self.assertEqual(report.total_material_evaluations, 18)
        self.assertEqual(report.final_details, (0, 2))

    def test_dropping_subquantum_detail_stalls_when_positive_impulse_is_required(self):
        state = chain_state((2, 3, 5), (6, 6, 0))
        report = solve_weighted_chain_quantized_least_action(
            state,
            (subquantum_channel(), subquantum_channel()),
            retain_detail=False,
        )
        self.assertEqual(report.status, MATERIAL_CHANNEL_STALLED)
        self.assertFalse(report.resolved)
        self.assertEqual(report.stalled_contact, 0)
        self.assertEqual(report.impulse_vector, (0, 0))
        self.assertEqual(report.events, ())

    def test_zero_response_channel_stalls_even_when_detail_is_retained(self):
        state = chain_state((2, 3, 5), (6, 6, 0))
        zero = ContactMaterialUnitChannel1D(10, 0, 2)
        report = solve_weighted_chain_quantized_least_action(
            state, (zero, subquantum_channel()), retain_detail=True
        )
        self.assertEqual(report.status, MATERIAL_CHANNEL_STALLED)
        self.assertEqual(report.stalled_contact, 0)
        self.assertIsNone(report.expected_evaluations_per_contact[0])

    def test_full_quantum_channels_resolve_without_retained_detail(self):
        state = chain_state((2, 3, 5), (6, 6, 0))
        full = ContactMaterialUnitChannel1D(
            amplitude=10,
            response_sample=5,
            impulse_scale_magnitude=2,
        )
        report = solve_weighted_chain_quantized_least_action(
            state, (full, full), retain_detail=False
        )
        self.assertTrue(report.resolved)
        self.assertEqual(report.impulse_vector, (4, 7))
        self.assertEqual(report.evaluations_per_contact, (4, 7))
        self.assertEqual(report.total_material_evaluations, 11)
        self.assertEqual(report.final_details, (0, 0))

    def test_all_priority_permutations_have_same_final_impulse_and_event_count_on_selected_chain(self):
        state = chain_state((1, 3, 2, 1), (6, 9, 4, 0))
        channels = (
            ContactMaterialUnitChannel1D(7, 2, 3),
            ContactMaterialUnitChannel1D(9, 2, 4),
            ContactMaterialUnitChannel1D(5, 1, 4),
        )
        results = []
        for priority in itertools.permutations(range(3)):
            report = solve_weighted_chain_quantized_least_action(
                state, channels, priority=priority, retain_detail=True
            )
            results.append(report)
        self.assertEqual({report.impulse_vector for report in results}, {(4, 5, 3)})
        self.assertEqual(len({report.evaluations_per_contact for report in results}), 1)
        self.assertEqual(len({report.total_material_evaluations for report in results}), 1)

    def test_per_contact_evaluation_formula_matches_final_least_impulse_on_small_equal_mass_profiles(self):
        channel = ContactMaterialUnitChannel1D(6, 2, 2)
        checked = 0
        for body_count in range(2, 5):
            for nondecreasing in itertools.combinations_with_replacement(
                range(-1, 3), body_count
            ):
                momenta = tuple(reversed(nondecreasing))
                state = chain_state((1,) * body_count, momenta)
                if any(score > 0 for score in contact_relative_scores(state)):
                    continue
                oracle = solve_weighted_chain_least_action(state)
                report = solve_weighted_chain_quantized_least_action(
                    state,
                    (channel,) * (body_count - 1),
                    retain_detail=True,
                )
                self.assertEqual(report.impulse_vector, oracle.impulse_vector)
                expected = tuple(
                    channel.evaluations_for_delivered_quanta(value)
                    for value in oracle.impulse_vector
                )
                self.assertEqual(report.evaluations_per_contact, expected)
                checked += 1
        self.assertGreater(checked, 20)

    def test_already_nonclosing_chain_needs_no_material_events_even_with_zero_channels(self):
        state = chain_state((2, 3, 5), (0, 0, 0))
        zero = ContactMaterialUnitChannel1D(10, 0, 1)
        report = solve_weighted_chain_quantized_least_action(
            state, (zero, zero), retain_detail=True
        )
        self.assertTrue(report.resolved)
        self.assertEqual(report.impulse_vector, (0, 0))
        self.assertEqual(report.events, ())
        self.assertEqual(report.total_material_evaluations, 0)

    def test_channel_validation(self):
        with self.assertRaises(ValueError):
            ContactMaterialUnitChannel1D(0, 0, 1)
        with self.assertRaises(ValueError):
            ContactMaterialUnitChannel1D(10, 11, 1)
        with self.assertRaises(ValueError):
            ContactMaterialUnitChannel1D(10, 6, 2)
        with self.assertRaises(ValueError):
            ContactMaterialUnitChannel1D(10, 1, 1, 10)
        with self.assertRaises(ValueError):
            ContactMaterialUnitChannel1D(10, 1, True)
        with self.assertRaises(ValueError):
            subquantum_channel().evaluations_for_delivered_quanta(-1)

        state = chain_state((1, 1), (1, 0))
        with self.assertRaises(ValueError):
            solve_weighted_chain_quantized_least_action(state, ())
        with self.assertRaises(ValueError):
            solve_weighted_chain_quantized_least_action(
                state, (subquantum_channel(),), retain_detail="yes"
            )


if __name__ == "__main__":
    unittest.main()
