import unittest
from itertools import product

from enterprise_math.clearance_precision import (
    ACTIVE_COUNT,
    ACTIVE_SET,
    FULL_VECTOR,
    SCALAR_DEPTH,
    active_axis_count_multiplicity,
    clearance_behavior_signature,
    clearance_precision_class_counts,
    clearance_shell_multiplicity,
)


class ClearancePrecisionTests(unittest.TestCase):
    def test_shell_and_active_axis_formulas_match_direct_enumeration(self):
        for dimension in range(1, 5):
            for factor in range(2, 7):
                shell_total = 0
                for depth in range(1, factor):
                    q = factor - depth
                    shell = [
                        vector
                        for vector in product(range(factor), repeat=dimension)
                        if max(vector) == q
                    ]
                    self.assertEqual(
                        clearance_shell_multiplicity(dimension, factor, depth),
                        len(shell),
                    )
                    shell_total += len(shell)
                    for active_count in range(1, dimension + 1):
                        direct = sum(
                            sum(value == q for value in vector) == active_count
                            for vector in shell
                        )
                        self.assertEqual(
                            active_axis_count_multiplicity(
                                dimension, factor, depth, active_count
                            ),
                            direct,
                        )
                self.assertEqual(shell_total, factor**dimension - 1)

    def test_exact_class_counts_match_direct_signatures(self):
        modes = (
            (SCALAR_DEPTH, "scalar_depth_classes"),
            (ACTIVE_COUNT, "active_count_classes"),
            (ACTIVE_SET, "active_set_classes"),
            (FULL_VECTOR, "full_vector_classes"),
        )
        for dimension in range(1, 5):
            for factor in range(1, 7):
                vectors = [
                    vector
                    for vector in product(range(factor), repeat=dimension)
                    if any(vector)
                ]
                counts = clearance_precision_class_counts(dimension, factor)
                self.assertEqual(counts.coarse_only_states, len(vectors))
                for mode, field in modes:
                    signatures = {
                        clearance_behavior_signature(vector, factor, mode)
                        for vector in vectors
                    }
                    self.assertEqual(len(signatures), getattr(counts, field))

    def test_information_hierarchy_refines_monotonically(self):
        for dimension in range(1, 6):
            for factor in range(1, 8):
                counts = clearance_precision_class_counts(dimension, factor)
                self.assertLessEqual(counts.scalar_depth_classes, counts.active_count_classes)
                self.assertLessEqual(counts.active_count_classes, counts.active_set_classes)
                self.assertLessEqual(counts.active_set_classes, counts.full_vector_classes)

    def test_direction_witness_can_be_hidden_by_scalar_depth(self):
        factor = 4
        x_only = (2, 0)
        tie = (2, 2)
        self.assertEqual(
            clearance_behavior_signature(x_only, factor, SCALAR_DEPTH),
            clearance_behavior_signature(tie, factor, SCALAR_DEPTH),
        )
        self.assertNotEqual(
            clearance_behavior_signature(x_only, factor, ACTIVE_COUNT),
            clearance_behavior_signature(tie, factor, ACTIVE_COUNT),
        )

    def test_active_count_can_hide_which_direction_is_available(self):
        factor = 5
        x_only = (3, 1)
        y_only = (1, 3)
        self.assertEqual(
            clearance_behavior_signature(x_only, factor, ACTIVE_COUNT),
            clearance_behavior_signature(y_only, factor, ACTIVE_COUNT),
        )
        self.assertNotEqual(
            clearance_behavior_signature(x_only, factor, ACTIVE_SET),
            clearance_behavior_signature(y_only, factor, ACTIVE_SET),
        )

    def test_active_set_can_hide_nonmaximal_clearance(self):
        factor = 6
        first = (4, 0)
        second = (4, 3)
        self.assertEqual(
            clearance_behavior_signature(first, factor, ACTIVE_SET),
            clearance_behavior_signature(second, factor, ACTIVE_SET),
        )
        self.assertNotEqual(
            clearance_behavior_signature(first, factor, FULL_VECTOR),
            clearance_behavior_signature(second, factor, FULL_VECTOR),
        )

    def test_invalid_states_are_rejected(self):
        with self.assertRaises(ValueError):
            clearance_behavior_signature((), 3, SCALAR_DEPTH)
        with self.assertRaises(ValueError):
            clearance_behavior_signature((0, 0), 3, SCALAR_DEPTH)
        with self.assertRaises(ValueError):
            clearance_behavior_signature((3, 0), 3, SCALAR_DEPTH)
        with self.assertRaises(ValueError):
            clearance_behavior_signature((1, 0), 3, "UNKNOWN")


if __name__ == "__main__":
    unittest.main()
