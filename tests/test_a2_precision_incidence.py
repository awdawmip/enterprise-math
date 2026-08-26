import unittest
from itertools import product

from enterprise_math.a2_precision_incidence import (
    active_repair_support_count,
    additive_depth_triangle,
    binary_split_identity,
    conditional_repair_factor,
    directed_repair_factor,
    directed_repair_spectrum,
    formal_joint_candidate_count,
    incidence_edges,
    multiplicative_triangle,
    pairwise_intersection_counts,
    realized_joint_class_count,
    realized_joint_tuples,
    reconstruct_repair_distribution,
    repair_size_distribution,
    same_partition,
    symmetric_repair_distance,
)


def canonical_partitions(size: int):
    labels = [0] * size

    def rec(index: int, current_max: int):
        if index == size:
            yield {state: labels[state] for state in range(size)}
            return
        for label in range(current_max + 2):
            labels[index] = label
            yield from rec(index + 1, max(current_max, label))

    labels[0] = 0
    yield from rec(1, 0)


def partitions_from_triples(triples):
    states = tuple(range(len(triples)))
    family = tuple(
        {state: triples[state][axis] for state in states}
        for axis in range(3)
    )
    return states, family


class A2PrecisionIncidenceTests(unittest.TestCase):
    def test_realized_joint_classes_are_incidence_edges_not_formal_product(self):
        states = tuple(range(4))
        first = {0: "A", 1: "A", 2: "B", 3: "B"}
        second = {0: "X", 1: "Y", 2: "Y", 3: "Z"}
        self.assertEqual(len(incidence_edges(states, first, second)), 4)
        self.assertEqual(realized_joint_class_count(states, [first, second]), 4)
        self.assertEqual(formal_joint_candidate_count(states, [first, second]), 6)

    def test_repair_factor_and_spectrum_are_exact_degree_data(self):
        states = tuple(range(6))
        known = {0: "A", 1: "A", 2: "A", 3: "B", 4: "B", 5: "B"}
        added = {0: "X", 1: "Y", 2: "Z", 3: "X", 4: "X", 5: "Y"}
        self.assertEqual(directed_repair_factor(states, known, added), 3)
        spectrum = directed_repair_spectrum(states, known, added)
        self.assertEqual(spectrum, (5, 4, 1))
        self.assertEqual(
            reconstruct_repair_distribution(spectrum),
            repair_size_distribution(states, known, added),
        )

    def test_binary_split_identity(self):
        states = (0, 1, 2, 3)
        known = {0: 0, 1: 0, 2: 1, 3: 1}
        added = {0: 0, 1: 1, 2: 0, 3: 0}
        data = binary_split_identity(states, known, added)
        self.assertEqual(data["active_support"], 1)
        self.assertEqual(active_repair_support_count(states, known, added), 1)
        self.assertEqual(data["second_repair_mass"], 1)
        self.assertEqual(data["class_count_gain"], 1)

    def test_pairwise_shadows_do_not_determine_three_task_joint_state(self):
        even = (
            (0, 0, 0), (0, 0, 0),
            (0, 1, 1), (0, 1, 1),
            (1, 0, 1), (1, 0, 1),
            (1, 1, 0), (1, 1, 0),
        )
        full = tuple(product((0, 1), repeat=3))
        even_states, even_family = partitions_from_triples(even)
        full_states, full_family = partitions_from_triples(full)
        self.assertEqual(
            pairwise_intersection_counts(even_states, even_family),
            pairwise_intersection_counts(full_states, full_family),
        )
        self.assertEqual(realized_joint_class_count(even_states, even_family), 4)
        self.assertEqual(realized_joint_class_count(full_states, full_family), 8)
        self.assertNotEqual(
            realized_joint_tuples(even_states, even_family),
            realized_joint_tuples(full_states, full_family),
        )
        self.assertEqual(
            conditional_repair_factor(even_states, even_family[:2], even_family[2]), 1
        )
        self.assertEqual(
            conditional_repair_factor(full_states, full_family[:2], full_family[2]), 2
        )

    def test_directed_and_symmetric_geometry_exhaustive_on_four_states(self):
        states = tuple(range(4))
        partitions = list(canonical_partitions(4))
        self.assertEqual(len(partitions), 15)
        for first in partitions:
            for middle in partitions:
                for last in partitions:
                    self.assertTrue(multiplicative_triangle(states, first, middle, last))
                    self.assertTrue(additive_depth_triangle(states, first, middle, last, 2))
                    self.assertLessEqual(
                        symmetric_repair_distance(states, first, last, 2),
                        symmetric_repair_distance(states, first, middle, 2)
                        + symmetric_repair_distance(states, middle, last, 2),
                    )
        for first in partitions:
            for second in partitions:
                self.assertEqual(
                    symmetric_repair_distance(states, first, second, 2) == 0,
                    same_partition(states, first, second),
                )


if __name__ == "__main__":
    unittest.main()
