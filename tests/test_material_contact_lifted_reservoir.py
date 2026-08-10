import itertools
import unittest

from enterprise_math.material_contact_lifted_reservoir import (
    contact_lifted_ambiguity_report,
    lifted_contact_reservoir_state,
    local_first_delivery_distance,
    named_local_carry_signature,
    pooled_remainder_comparator,
    remainder_from_first_delivery_distance,
    remainder_vector_from_carry_signature,
    same_body_delta_from_lifted_contacts,
)


PATH_B = (
    (-1, 0),
    (1, -1),
    (0, 1),
)

TRIANGLE_B = (
    (-1, 0, 1),
    (1, -1, 0),
    (0, 1, -1),
)


def body_state_map(incidence, amplitude, maximum_raw):
    contact_count = len(incidence[0])
    result = {}
    for raw in itertools.product(
        range(maximum_raw + 1),
        repeat=contact_count,
    ):
        state = lifted_contact_reservoir_state(
            incidence,
            raw,
            amplitude,
        )
        result.setdefault(state.body_delta, []).append(raw)
    return result


class MaterialContactLiftedReservoirTests(unittest.TestCase):
    def test_coordinatewise_lift_reconstructs_raw_numerators_exactly(self):
        for amplitude in range(1, 9):
            for raw in itertools.product(range(0, 20), repeat=2):
                state = lifted_contact_reservoir_state(
                    PATH_B,
                    raw,
                    amplitude,
                )
                self.assertEqual(
                    state.raw_numerators,
                    tuple(
                        amplitude * quotient + remainder
                        for quotient, remainder in zip(
                            state.delivered_impulse_quanta,
                            state.contact_remainders,
                            strict=True,
                        )
                    ),
                )
                self.assertTrue(
                    all(
                        0 <= remainder < amplitude
                        for remainder in state.contact_remainders
                    )
                )

    def test_same_body_delta_iff_delivered_difference_is_incidence_cycle(self):
        for amplitude in (1, 2, 5):
            raw_states = tuple(
                itertools.product(range(0, 8), repeat=3)
            )
            sample = raw_states[::23]
            for left in sample:
                for right in sample:
                    direct = (
                        lifted_contact_reservoir_state(
                            TRIANGLE_B,
                            left,
                            amplitude,
                        ).body_delta
                        == lifted_contact_reservoir_state(
                            TRIANGLE_B,
                            right,
                            amplitude,
                        ).body_delta
                    )
                    self.assertEqual(
                        same_body_delta_from_lifted_contacts(
                            TRIANGLE_B,
                            left,
                            right,
                            amplitude,
                        ),
                        direct,
                    )

    def test_forest_and_unit_amplitude_is_globally_injective(self):
        report = contact_lifted_ambiguity_report(PATH_B, 1)
        self.assertEqual(report.cycle_rank, 0)
        self.assertEqual(report.remainder_states_per_delivered_allocation, 1)
        self.assertTrue(
            report.delivered_allocation_identifiable_from_body_delta
        )
        self.assertFalse(report.subquantum_detail_present)
        self.assertTrue(
            report.lifted_state_globally_identifiable_from_body_delta
        )

        fibers = body_state_map(PATH_B, 1, 4)
        self.assertTrue(all(len(states) == 1 for states in fibers.values()))

    def test_forest_with_subquantum_amplitude_hides_remainder(self):
        report = contact_lifted_ambiguity_report(PATH_B, 10)
        self.assertEqual(report.cycle_rank, 0)
        self.assertTrue(
            report.delivered_allocation_identifiable_from_body_delta
        )
        self.assertTrue(report.subquantum_detail_present)
        self.assertFalse(
            report.lifted_state_globally_identifiable_from_body_delta
        )
        self.assertEqual(report.remainder_states_per_delivered_allocation, 100)

        zero = lifted_contact_reservoir_state(PATH_B, (0, 0), 10)
        hidden = lifted_contact_reservoir_state(PATH_B, (6, 0), 10)
        self.assertEqual(zero.body_delta, hidden.body_delta)
        self.assertNotEqual(zero.contact_remainders, hidden.contact_remainders)
        self.assertNotEqual(
            named_local_carry_signature(zero.raw_numerators, 10),
            named_local_carry_signature(hidden.raw_numerators, 10),
        )

    def test_cycle_with_unit_amplitude_hides_delivered_allocation(self):
        report = contact_lifted_ambiguity_report(TRIANGLE_B, 1)
        self.assertEqual(report.cycle_rank, 1)
        self.assertFalse(
            report.delivered_allocation_identifiable_from_body_delta
        )
        self.assertFalse(report.subquantum_detail_present)
        self.assertFalse(
            report.lifted_state_globally_identifiable_from_body_delta
        )

        zero = lifted_contact_reservoir_state(
            TRIANGLE_B,
            (0, 0, 0),
            1,
        )
        cycle = lifted_contact_reservoir_state(
            TRIANGLE_B,
            (1, 1, 1),
            1,
        )
        self.assertEqual(zero.body_delta, cycle.body_delta)
        self.assertNotEqual(
            zero.delivered_impulse_quanta,
            cycle.delivered_impulse_quanta,
        )

    def test_cycle_and_subquantum_amplitude_have_both_ambiguity_sources(self):
        report = contact_lifted_ambiguity_report(TRIANGLE_B, 10)
        self.assertEqual(report.cycle_rank, 1)
        self.assertTrue(report.subquantum_detail_present)
        self.assertFalse(
            report.delivered_allocation_identifiable_from_body_delta
        )
        self.assertEqual(
            report.remainder_states_per_delivered_allocation,
            1000,
        )

        first = lifted_contact_reservoir_state(
            TRIANGLE_B,
            (6, 0, 0),
            10,
        )
        remainder_alias = lifted_contact_reservoir_state(
            TRIANGLE_B,
            (0, 0, 0),
            10,
        )
        cycle_alias = lifted_contact_reservoir_state(
            TRIANGLE_B,
            (16, 10, 10),
            10,
        )
        self.assertEqual(first.body_delta, remainder_alias.body_delta)
        self.assertEqual(first.body_delta, cycle_alias.body_delta)
        self.assertNotEqual(
            first.contact_remainders,
            remainder_alias.contact_remainders,
        )
        self.assertEqual(
            first.contact_remainders,
            cycle_alias.contact_remainders,
        )
        self.assertNotEqual(
            first.delivered_impulse_quanta,
            cycle_alias.delivered_impulse_quanta,
        )

    def test_named_local_carry_distance_is_exact_and_invertible(self):
        for amplitude in range(1, 15):
            for remainder in range(amplitude):
                distance = local_first_delivery_distance(
                    remainder,
                    amplitude,
                )
                self.assertEqual(
                    remainder_from_first_delivery_distance(
                        distance,
                        amplitude,
                    ),
                    remainder,
                )
                raw = 3 * amplitude + remainder
                before = raw // amplitude
                for steps in range(distance):
                    self.assertEqual(
                        (raw + steps) // amplitude,
                        before,
                    )
                self.assertEqual(
                    (raw + distance) // amplitude,
                    before + 1,
                )

    def test_named_carry_signature_recovers_entire_remainder_vector(self):
        amplitude = 10
        for remainders in itertools.product(range(amplitude), repeat=3):
            raw = tuple(
                20 + remainder
                for remainder in remainders
            )
            signature = named_local_carry_signature(raw, amplitude)
            self.assertEqual(
                remainder_vector_from_carry_signature(
                    signature,
                    amplitude,
                ),
                remainders,
            )

    def test_global_pooling_can_fabricate_delivered_quanta(self):
        comparator = pooled_remainder_comparator((6, 6), 10)
        self.assertEqual(comparator.pooled_total, 12)
        self.assertEqual(comparator.pooled_delivered_quanta, 1)
        self.assertEqual(comparator.pooled_remainder, 2)
        self.assertTrue(comparator.creates_spurious_delivered_quantum)

        safe = pooled_remainder_comparator((3, 4), 10)
        self.assertEqual(safe.pooled_delivered_quanta, 0)
        self.assertFalse(safe.creates_spurious_delivered_quantum)

    def test_injectivity_criterion_is_exact_on_reference_topologies(self):
        expected = {
            ("path", 1): True,
            ("path", 2): False,
            ("triangle", 1): False,
            ("triangle", 2): False,
        }
        for (kind, amplitude), value in expected.items():
            graph = PATH_B if kind == "path" else TRIANGLE_B
            self.assertEqual(
                contact_lifted_ambiguity_report(
                    graph,
                    amplitude,
                ).lifted_state_globally_identifiable_from_body_delta,
                value,
            )

    def test_validation(self):
        with self.assertRaises(ValueError):
            lifted_contact_reservoir_state(PATH_B, (1,), 10)
        with self.assertRaises(ValueError):
            lifted_contact_reservoir_state(PATH_B, (-1, 0), 10)
        with self.assertRaises(ValueError):
            lifted_contact_reservoir_state(PATH_B, (0, 0), 0)
        with self.assertRaises(ValueError):
            local_first_delivery_distance(10, 10)
        with self.assertRaises(ValueError):
            pooled_remainder_comparator((), 10)
        with self.assertRaises(TypeError):
            contact_lifted_ambiguity_report(PATH_B, True)


if __name__ == "__main__":
    unittest.main()
