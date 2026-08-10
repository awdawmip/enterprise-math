import unittest

from enterprise_math.balanced_operation_constraint_valley import (
    balance_shape_pair,
    balanced_partition_shape,
    balanced_safe_total_count,
    balancing_strictly_reduces_safe_total_count,
    most_constraining_partition,
    power_sum_log_convex,
    safe_total_count_from_shape,
    shape_power_sum,
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


class BalancedOperationConstraintValleyTests(unittest.TestCase):
    def test_power_sum_sequence_is_log_convex_on_all_small_shapes(self):
        checked = 0
        for state_count in range(2, 13):
            for shape in integer_partitions(state_count):
                for exponent in range(1, 8):
                    self.assertTrue(power_sum_log_convex(shape, exponent))
                    checked += 1
        self.assertGreater(checked, 1000)

    def test_every_legal_robin_hood_balance_strictly_reduces_safe_count(self):
        checked = 0
        for state_count in range(3, 13):
            for shape in integer_partitions(state_count):
                for large_index, large in enumerate(shape):
                    for small_index, small in enumerate(shape):
                        if large_index == small_index or large < small + 2:
                            continue
                        balanced = balance_shape_pair(
                            shape, large_index, small_index
                        )
                        self.assertEqual(sum(balanced), state_count)
                        self.assertEqual(len(balanced), len(shape))
                        self.assertTrue(
                            balancing_strictly_reduces_safe_total_count(
                                shape, large_index, small_index
                            )
                        )
                        self.assertLess(
                            safe_total_count_from_shape(balanced),
                            safe_total_count_from_shape(shape),
                        )
                        checked += 1
        self.assertGreater(checked, 500)

    def test_balanced_shape_is_unique_fixed_block_count_minimum_exhaustively(self):
        checked = 0
        for state_count in range(3, 14):
            for block_count in range(2, state_count):
                balanced = balanced_partition_shape(
                    state_count, block_count
                )
                balanced_count = balanced_safe_total_count(
                    state_count, block_count
                )
                same_block_count = [
                    shape
                    for shape in integer_partitions(state_count)
                    if len(shape) == block_count
                ]
                minima = [
                    shape
                    for shape in same_block_count
                    if safe_total_count_from_shape(shape) == balanced_count
                ]
                self.assertEqual(minima, [balanced])
                self.assertEqual(
                    balanced_count,
                    min(
                        safe_total_count_from_shape(shape)
                        for shape in same_block_count
                    ),
                )
                checked += 1
        self.assertGreater(checked, 50)

    def test_global_one_dimensional_valley_matches_all_partition_oracle(self):
        for state_count in range(3, 15):
            report = most_constraining_partition(state_count)
            intermediate = [
                shape
                for shape in integer_partitions(state_count)
                if shape != (state_count,)
                and shape != (1,) * state_count
            ]
            direct_minimum = min(
                safe_total_count_from_shape(shape)
                for shape in intermediate
            )
            direct_shapes = [
                shape
                for shape in intermediate
                if safe_total_count_from_shape(shape) == direct_minimum
            ]
            self.assertEqual(report.safe_total_count, direct_minimum)
            self.assertIn(report.block_shape, direct_shapes)
            self.assertEqual(
                report.block_shape,
                balanced_partition_shape(
                    state_count, report.block_count
                ),
            )

    def test_reference_global_valley_shapes(self):
        expected = {
            3: (2, 1),
            4: (2, 2),
            5: (2, 2, 1),
            6: (2, 2, 2),
            7: (3, 2, 2),
            8: (2, 2, 2, 2),
            9: (3, 2, 2, 2),
            10: (2, 2, 2, 2, 2),
            11: (3, 2, 2, 2, 2),
            12: (3, 3, 3, 3),
        }
        for state_count, shape in expected.items():
            self.assertEqual(
                most_constraining_partition(state_count).block_shape,
                shape,
            )

    def test_balanced_closed_formula_matches_direct_power_sum_product(self):
        for state_count in range(2, 40):
            for block_count in range(1, state_count + 1):
                shape = balanced_partition_shape(
                    state_count, block_count
                )
                self.assertEqual(
                    balanced_safe_total_count(
                        state_count, block_count
                    ),
                    safe_total_count_from_shape(shape),
                )

    def test_discrete_convex_target_power_sum_reduction(self):
        # This locks the first half of the balancing proof independently of the
        # full safe-operation product.
        for a in range(3, 10):
            for b in range(1, a - 1):
                if a < b + 2:
                    continue
                old = (a, b, 2)
                new = tuple(sorted((a - 1, b + 1, 2), reverse=True))
                self.assertEqual(shape_power_sum(old, 1), shape_power_sum(new, 1))
                for exponent in range(2, 8):
                    self.assertLess(
                        shape_power_sum(new, exponent),
                        shape_power_sum(old, exponent),
                    )

    def test_validation(self):
        with self.assertRaises(ValueError):
            safe_total_count_from_shape(())
        with self.assertRaises(ValueError):
            balance_shape_pair((2, 2), 0, 1)
        with self.assertRaises(ValueError):
            balance_shape_pair((3, 1), 0, 0)
        with self.assertRaises(ValueError):
            balanced_partition_shape(3, 4)
        with self.assertRaises(ValueError):
            most_constraining_partition(2)
        with self.assertRaises(TypeError):
            shape_power_sum((2, 1), True)


if __name__ == "__main__":
    unittest.main()
