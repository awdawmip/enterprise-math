import unittest

from enterprise_math.operation_freedom_majorization import (
    maximally_imbalanced_partition_shape,
    maximum_safe_partial_count_fixed_blocks,
    maximum_safe_total_count_fixed_blocks,
    minimum_safe_partial_count_fixed_blocks,
    minimum_safe_total_count_fixed_blocks,
    operation_freedom_range,
    shape_safe_counts_lie_in_fixed_block_range,
)
from enterprise_math.balanced_operation_constraint_valley import (
    safe_total_count_from_shape,
)
from enterprise_math.balanced_partial_operation_constraint_valley import (
    safe_partial_count_from_shape,
)


def integer_partitions(total, maximum=None):
    if total == 0:
        yield ()
        return
    if maximum is None or maximum > total:
        maximum = total
    for first in range(maximum, 0, -1):
        for tail in integer_partitions(total - first, first):
            yield (first,) + tail


class OperationFreedomMajorizationTests(unittest.TestCase):
    def test_closed_maximum_formulas_match_direct_counts(self):
        for state_count in range(2, 40):
            for block_count in range(1, state_count + 1):
                shape = maximally_imbalanced_partition_shape(
                    state_count, block_count
                )
                self.assertEqual(
                    maximum_safe_total_count_fixed_blocks(
                        state_count, block_count
                    ),
                    safe_total_count_from_shape(shape),
                )
                self.assertEqual(
                    maximum_safe_partial_count_fixed_blocks(
                        state_count, block_count
                    ),
                    safe_partial_count_from_shape(shape),
                )

    def test_balanced_and_imbalanced_are_unique_fixed_block_extremes_exhaustively(self):
        checked = 0
        for state_count in range(2, 14):
            for block_count in range(1, state_count + 1):
                candidates = [
                    shape
                    for shape in integer_partitions(state_count)
                    if len(shape) == block_count
                ]
                totals = {
                    shape: safe_total_count_from_shape(shape)
                    for shape in candidates
                }
                partials = {
                    shape: safe_partial_count_from_shape(shape)
                    for shape in candidates
                }
                report = operation_freedom_range(
                    state_count, block_count
                )
                total_min_shapes = [
                    shape
                    for shape, count in totals.items()
                    if count == report.minimum_total_count
                ]
                total_max_shapes = [
                    shape
                    for shape, count in totals.items()
                    if count == report.maximum_total_count
                ]
                partial_min_shapes = [
                    shape
                    for shape, count in partials.items()
                    if count == report.minimum_partial_count
                ]
                partial_max_shapes = [
                    shape
                    for shape, count in partials.items()
                    if count == report.maximum_partial_count
                ]
                self.assertEqual(total_min_shapes, [report.balanced_shape])
                self.assertEqual(partial_min_shapes, [report.balanced_shape])
                self.assertEqual(total_max_shapes, [report.imbalanced_shape])
                self.assertEqual(partial_max_shapes, [report.imbalanced_shape])
                checked += 1
        self.assertGreater(checked, 70)

    def test_every_small_shape_lies_inside_exact_fixed_block_range(self):
        checked = 0
        for state_count in range(1, 15):
            for shape in integer_partitions(state_count):
                self.assertTrue(shape_safe_counts_lie_in_fixed_block_range(shape))
                checked += 1
        self.assertGreater(checked, 100)

    def test_same_class_count_can_hide_large_operation_freedom_difference(self):
        report = operation_freedom_range(12, 4)
        self.assertEqual(report.balanced_shape, (3, 3, 3, 3))
        self.assertEqual(report.imbalanced_shape, (9, 1, 1, 1))
        self.assertGreater(report.total_max_to_min_ratio, 1)
        self.assertGreater(report.partial_max_to_min_ratio, 1)
        self.assertGreater(report.maximum_total_count, report.minimum_total_count)
        self.assertGreater(report.maximum_partial_count, report.minimum_partial_count)

    def test_extremes_coincide_when_shape_is_forced(self):
        # b=1 and b=n each admit only one partition shape, so min=max.
        for state_count in range(1, 20):
            for block_count in (1, state_count):
                report = operation_freedom_range(
                    state_count, block_count
                )
                self.assertEqual(report.balanced_shape, report.imbalanced_shape)
                self.assertEqual(
                    report.minimum_total_count,
                    report.maximum_total_count,
                )
                self.assertEqual(
                    report.minimum_partial_count,
                    report.maximum_partial_count,
                )

    def test_fixed_block_minimum_and_maximum_helpers_are_ordered(self):
        for state_count in range(2, 60):
            for block_count in range(1, state_count + 1):
                self.assertLessEqual(
                    minimum_safe_total_count_fixed_blocks(
                        state_count, block_count
                    ),
                    maximum_safe_total_count_fixed_blocks(
                        state_count, block_count
                    ),
                )
                self.assertLessEqual(
                    minimum_safe_partial_count_fixed_blocks(
                        state_count, block_count
                    ),
                    maximum_safe_partial_count_fixed_blocks(
                        state_count, block_count
                    ),
                )

    def test_validation(self):
        with self.assertRaises(ValueError):
            maximally_imbalanced_partition_shape(3, 4)
        with self.assertRaises(TypeError):
            operation_freedom_range(True, 1)
        with self.assertRaises(ValueError):
            shape_safe_counts_lie_in_fixed_block_range(())


if __name__ == "__main__":
    unittest.main()
