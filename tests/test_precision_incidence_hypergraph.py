import unittest

from enterprise_math.precision_incidence_hypergraph import (
    conditional_repair_factor,
    conditional_repair_spectrum,
    context_refinement_monotone,
    formal_joint_candidate_count,
    joint_tuple_multiplicities,
    pairwise_intersection_counts,
    realized_joint_class_count,
    realized_joint_tuples,
    unrealized_joint_tuple_defect,
)
from enterprise_math.precision_incidence_geometry import directed_repair_factor


def partitions_from_triples(triples):
    states = tuple(range(len(triples)))
    partitions = []
    for coordinate in range(3):
        partitions.append(
            {state: triples[state][coordinate] for state in states}
        )
    return states, tuple(partitions)


class PrecisionIncidenceHypergraphTests(unittest.TestCase):
    def setUp(self) -> None:
        # Every even-parity tuple occurs twice.
        even_triples = (
            (0, 0, 0),
            (0, 0, 0),
            (0, 1, 1),
            (0, 1, 1),
            (1, 0, 1),
            (1, 0, 1),
            (1, 1, 0),
            (1, 1, 0),
        )
        # Every binary triple occurs once.
        full_triples = tuple(
            (a, b, c)
            for a in (0, 1)
            for b in (0, 1)
            for c in (0, 1)
        )
        self.even_states, self.even = partitions_from_triples(even_triples)
        self.full_states, self.full = partitions_from_triples(full_triples)

    def test_hyperedges_are_exact_joint_precision_classes(self) -> None:
        self.assertEqual(realized_joint_class_count(self.even_states, self.even), 4)
        self.assertEqual(realized_joint_class_count(self.full_states, self.full), 8)
        self.assertEqual(formal_joint_candidate_count(self.even_states, self.even), 8)
        self.assertEqual(unrealized_joint_tuple_defect(self.even_states, self.even), 4)
        self.assertEqual(unrealized_joint_tuple_defect(self.full_states, self.full), 0)

    def test_pairwise_weighted_incidence_is_identical_but_joint_state_differs(self) -> None:
        self.assertEqual(
            pairwise_intersection_counts(self.even_states, self.even),
            pairwise_intersection_counts(self.full_states, self.full),
        )
        self.assertNotEqual(
            realized_joint_tuples(self.even_states, self.even),
            realized_joint_tuples(self.full_states, self.full),
        )
        # The pairwise shadows even agree in every cell cardinality: all are 2.
        for counts in pairwise_intersection_counts(self.even_states, self.even).values():
            self.assertEqual(set(counts.values()), {2})

    def test_all_pairwise_repair_factors_match(self) -> None:
        for i in range(3):
            for j in range(3):
                if i == j:
                    continue
                self.assertEqual(
                    directed_repair_factor(
                        self.even_states, self.even[i], self.even[j]
                    ),
                    2,
                )
                self.assertEqual(
                    directed_repair_factor(
                        self.full_states, self.full[i], self.full[j]
                    ),
                    2,
                )

    def test_third_task_is_redundant_after_two_in_even_parity_system(self) -> None:
        self.assertEqual(
            conditional_repair_factor(
                self.even_states, self.even[:2], self.even[2]
            ),
            1,
        )
        self.assertEqual(
            conditional_repair_factor(
                self.full_states, self.full[:2], self.full[2]
            ),
            2,
        )

    def test_conditioning_with_more_known_precision_cannot_raise_repair(self) -> None:
        for partitions, states in (
            (self.even, self.even_states),
            (self.full, self.full_states),
        ):
            self.assertTrue(
                context_refinement_monotone(
                    states,
                    partitions[:1],
                    partitions[:2],
                    partitions[2],
                )
            )
            self.assertLessEqual(
                conditional_repair_factor(states, partitions[:2], partitions[2]),
                conditional_repair_factor(states, partitions[:1], partitions[2]),
            )

    def test_conditional_repair_spectrum_sees_higher_order_difference(self) -> None:
        self.assertNotEqual(
            conditional_repair_spectrum(
                self.even_states, self.even[:2], self.even[2]
            ),
            conditional_repair_spectrum(
                self.full_states, self.full[:2], self.full[2]
            ),
        )

    def test_joint_tuple_multiplicity_distinguishes_duplicate_vs_full_cube(self) -> None:
        even_counts = joint_tuple_multiplicities(self.even_states, self.even)
        full_counts = joint_tuple_multiplicities(self.full_states, self.full)
        self.assertEqual(set(even_counts.values()), {2})
        self.assertEqual(set(full_counts.values()), {1})


if __name__ == "__main__":
    unittest.main()
