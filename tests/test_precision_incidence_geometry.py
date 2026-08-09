import unittest

from enterprise_math.precision_incidence_geometry import (
    additive_depth_triangle,
    common_refinement,
    directed_repair_depth,
    directed_repair_factor,
    directed_repair_spectrum,
    formal_product_candidate_count,
    incidence_edges,
    integer_symbol_depth,
    multiplicative_triangle,
    realized_product_class_count,
    refines,
    same_partition,
    symmetric_repair_distance,
    unrealized_product_tuple_defect,
)
from enterprise_math.precision_projection_spectrum import repair_spectrum


def canonical_partitions(size: int):
    """Yield restricted-growth labelings, one per set partition."""

    labels = [0] * size

    def recurse(index: int, current_max: int):
        if index == size:
            yield {state: labels[state] for state in range(size)}
            return
        for label in range(current_max + 2):
            labels[index] = label
            yield from recurse(index + 1, max(current_max, label))

    if size < 1:
        return
    labels[0] = 0
    yield from recurse(1, 0)


class PrecisionIncidenceGeometryTests(unittest.TestCase):
    def test_incidence_edges_are_exact_realized_product_classes(self) -> None:
        states = tuple(range(6))
        first = {0: "A", 1: "A", 2: "A", 3: "B", 4: "B", 5: "B"}
        second = {0: "X", 1: "Y", 2: "Y", 3: "Y", 4: "Z", 5: "Z"}
        edges = incidence_edges(states, first, second)
        self.assertEqual(
            edges,
            frozenset({("A", "X"), ("A", "Y"), ("B", "Y"), ("B", "Z")}),
        )
        self.assertEqual(realized_product_class_count(states, first, second), 4)
        self.assertEqual(formal_product_candidate_count(states, first, second), 6)
        self.assertEqual(unrealized_product_tuple_defect(states, first, second), 2)

    def test_directed_factor_is_generic_minimum_product_task_repair(self) -> None:
        states = tuple(range(6))
        known = {0: "A", 1: "A", 2: "A", 3: "B", 4: "B", 5: "B"}
        added = {0: "X", 1: "Y", 2: "Y", 3: "Y", 4: "Z", 5: "Z"}
        product = common_refinement(states, known, added)
        self.assertEqual(directed_repair_factor(states, known, added), 2)
        self.assertEqual(
            directed_repair_spectrum(states, known, added),
            repair_spectrum(states, product, known),
        )

    def test_factor_one_is_exactly_already_fine_enough(self) -> None:
        states = tuple(range(4))
        partitions = list(canonical_partitions(4))
        for known in partitions:
            for added in partitions:
                self.assertEqual(
                    directed_repair_factor(states, known, added) == 1,
                    refines(states, known, added),
                )
                self.assertEqual(
                    directed_repair_depth(states, known, added, base=2) == 0,
                    refines(states, known, added),
                )

    def test_integer_symbol_depth_is_minimum_integer_capacity_level(self) -> None:
        self.assertEqual(integer_symbol_depth(1, 2), 0)
        self.assertEqual(integer_symbol_depth(2, 2), 1)
        self.assertEqual(integer_symbol_depth(3, 2), 2)
        self.assertEqual(integer_symbol_depth(4, 2), 2)
        self.assertEqual(integer_symbol_depth(5, 2), 3)
        self.assertEqual(integer_symbol_depth(9, 3), 2)
        self.assertEqual(integer_symbol_depth(10, 3), 3)

    def test_multiplicative_triangle_exhaustive_on_four_state_partitions(self) -> None:
        states = tuple(range(4))
        partitions = list(canonical_partitions(4))
        self.assertEqual(len(partitions), 15)
        for first in partitions:
            for middle in partitions:
                for last in partitions:
                    data = multiplicative_triangle(states, first, middle, last)
                    self.assertTrue(data["holds"])
                    self.assertLessEqual(data["direct"], data["product_bound"])

    def test_directed_integer_triangle_exhaustive_on_four_state_partitions(self) -> None:
        states = tuple(range(4))
        partitions = list(canonical_partitions(4))
        for base in (2, 3):
            for first in partitions:
                for middle in partitions:
                    for last in partitions:
                        data = additive_depth_triangle(
                            states, first, middle, last, base=base
                        )
                        self.assertTrue(data["holds"])

    def test_symmetric_depth_is_metric_on_partition_relations(self) -> None:
        states = tuple(range(4))
        partitions = list(canonical_partitions(4))
        for first in partitions:
            self.assertEqual(symmetric_repair_distance(states, first, first), 0)
            for second in partitions:
                distance = symmetric_repair_distance(states, first, second)
                self.assertEqual(
                    distance == 0,
                    same_partition(states, first, second),
                )
                self.assertEqual(
                    distance,
                    symmetric_repair_distance(states, second, first),
                )
        for first in partitions:
            for middle in partitions:
                for last in partitions:
                    self.assertLessEqual(
                        symmetric_repair_distance(states, first, last),
                        symmetric_repair_distance(states, first, middle)
                        + symmetric_repair_distance(states, middle, last),
                    )

    def test_complete_incidence_graph_is_formal_independence_extreme(self) -> None:
        states = tuple(range(6))
        first = {0: "A", 1: "A", 2: "A", 3: "B", 4: "B", 5: "B"}
        second = {0: "X", 1: "Y", 2: "Z", 3: "X", 4: "Y", 5: "Z"}
        self.assertEqual(realized_product_class_count(states, first, second), 6)
        self.assertEqual(formal_product_candidate_count(states, first, second), 6)
        self.assertEqual(unrealized_product_tuple_defect(states, first, second), 0)
        self.assertEqual(directed_repair_factor(states, first, second), 3)
        self.assertEqual(directed_repair_factor(states, second, first), 2)


if __name__ == "__main__":
    unittest.main()
