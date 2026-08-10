import unittest

from enterprise_math.contact_critical_precision_phase import (
    contact_graph_critical_phase_signature,
    critical_precision_average_denominator,
    critical_precision_phase_histogram_direct,
    critical_precision_phase_spectrum,
    euler_totient,
    graph_uniform_repetition_denominator_from_edges,
    positive_divisors,
    repeated_critical_denominator,
    repetition_refinement_respects_divisibility,
)


def incidence(body_count, edges):
    rows = [[0] * len(edges) for _ in range(body_count)]
    for edge, (source, target) in enumerate(edges):
        rows[source][edge] = -1
        rows[target][edge] = 1
    return tuple(tuple(row) for row in rows)


def cycle_incidence(size):
    return incidence(
        size,
        tuple((index, (index + 1) % size) for index in range(size)),
    )


def complete_graph_incidence(size):
    return incidence(
        size,
        tuple(
            (left, right)
            for left in range(size)
            for right in range(left + 1, size)
        ),
    )


class ContactCriticalPrecisionPhaseTests(unittest.TestCase):
    def test_divisors_and_totients_partition_every_small_period(self):
        for order in range(1, 61):
            divisors = positive_divisors(order)
            self.assertEqual(divisors[0], 1)
            self.assertEqual(divisors[-1], order)
            self.assertTrue(all(order % value == 0 for value in divisors))
            self.assertEqual(
                sum(euler_totient(value) for value in divisors),
                order,
            )

    def test_phase_spectrum_matches_direct_residue_enumeration(self):
        for order in range(1, 61):
            formula = tuple(
                (phase.denominator, phase.phase_count)
                for phase in critical_precision_phase_spectrum(order)
            )
            self.assertEqual(
                formula,
                critical_precision_phase_histogram_direct(order),
            )

    def test_reference_phase_spectra(self):
        expected = {
            1: ((1, 1),),
            3: ((1, 1), (3, 2)),
            6: ((1, 1), (2, 1), (3, 2), (6, 2)),
            12: (
                (1, 1),
                (2, 1),
                (3, 2),
                (4, 2),
                (6, 2),
                (12, 4),
            ),
        }
        for order, target in expected.items():
            self.assertEqual(
                tuple(
                    (phase.denominator, phase.phase_count)
                    for phase in critical_precision_phase_spectrum(order)
                ),
                target,
            )

    def test_repetition_denominator_sequence_is_periodic(self):
        for order in range(1, 31):
            first = tuple(
                repeated_critical_denominator(order, repetition)
                for repetition in range(order)
            )
            second = tuple(
                repeated_critical_denominator(order, repetition + order)
                for repetition in range(order)
            )
            self.assertEqual(first, second)

        self.assertEqual(
            tuple(repeated_critical_denominator(6, repetition) for repetition in range(1, 7)),
            (6, 3, 2, 3, 6, 1),
        )

    def test_average_denominator_matches_direct_period_average(self):
        from fractions import Fraction

        for order in range(1, 41):
            direct = Fraction(
                sum(
                    repeated_critical_denominator(order, repetition)
                    for repetition in range(order)
                ),
                order,
            )
            self.assertEqual(
                critical_precision_average_denominator(order),
                direct,
            )

    def test_true_divisibility_refinement_only_lowers_denominator(self):
        for order in range(1, 31):
            for coarse in range(1, 13):
                for multiplier in range(1, 8):
                    fine = coarse * multiplier
                    self.assertTrue(
                        repetition_refinement_respects_divisibility(
                            order,
                            coarse,
                            fine,
                        )
                    )
                    self.assertEqual(
                        repeated_critical_denominator(order, coarse)
                        % repeated_critical_denominator(order, fine),
                        0,
                    )

    def test_cycle_graph_signature(self):
        for size in range(3, 10):
            signature = contact_graph_critical_phase_signature(
                cycle_incidence(size)
            )
            self.assertEqual(signature.cycle_rank, 1)
            self.assertEqual(signature.critical_group_order, size)
            self.assertEqual(signature.critical_group_exponent, size)
            self.assertEqual(signature.edge_class_orders, (size,) * size)
            self.assertEqual(signature.uniform_potential_denominator, size)

    def test_complete_graph_separates_rank_exponent_and_group_order(self):
        for size in range(3, 7):
            signature = contact_graph_critical_phase_signature(
                complete_graph_incidence(size)
            )
            self.assertEqual(
                signature.cycle_rank,
                (size - 1) * (size - 2) // 2,
            )
            self.assertEqual(
                signature.critical_group_order,
                size ** (size - 2),
            )
            self.assertEqual(signature.critical_group_exponent, size)
            self.assertEqual(set(signature.edge_class_orders), {size})

    def test_tree_signature_is_topologically_trivial(self):
        for size in range(2, 8):
            graph = incidence(
                size,
                tuple((index, index + 1) for index in range(size - 1)),
            )
            signature = contact_graph_critical_phase_signature(graph)
            self.assertEqual(signature.cycle_rank, 0)
            self.assertEqual(signature.critical_group_order, 1)
            self.assertEqual(signature.critical_group_exponent, 1)
            self.assertEqual(signature.edge_class_orders, (1,) * (size - 1))

    def test_graph_uniform_repetition_phase_matches_lcm_of_edge_classes(self):
        graphs = (
            cycle_incidence(6),
            complete_graph_incidence(4),
            incidence(
                4,
                ((0, 1), (1, 2), (2, 3), (3, 0), (0, 2)),
            ),
        )
        for graph in graphs:
            signature = contact_graph_critical_phase_signature(graph)
            for repetition in range(0, 2 * signature.critical_group_exponent + 1):
                self.assertEqual(
                    graph_uniform_repetition_denominator_from_edges(
                        signature,
                        repetition,
                    ),
                    repeated_critical_denominator(
                        signature.critical_group_exponent,
                        repetition,
                    ),
                )

    def test_graph_phase_counts_use_critical_exponent_not_group_order(self):
        signature = contact_graph_critical_phase_signature(
            complete_graph_incidence(6)
        )
        self.assertEqual(signature.critical_group_exponent, 6)
        self.assertEqual(signature.critical_group_order, 1296)
        self.assertEqual(
            tuple(
                (phase.denominator, phase.phase_count)
                for phase in signature.phase_spectrum
            ),
            ((1, 1), (2, 1), (3, 2), (6, 2)),
        )

    def test_validation(self):
        with self.assertRaises(ValueError):
            positive_divisors(0)
        with self.assertRaises(ValueError):
            euler_totient(0)
        with self.assertRaises(ValueError):
            repeated_critical_denominator(0, 1)
        with self.assertRaises(ValueError):
            repetition_refinement_respects_divisibility(6, 4, 6)
        with self.assertRaises(TypeError):
            repeated_critical_denominator(6, True)


if __name__ == "__main__":
    unittest.main()
