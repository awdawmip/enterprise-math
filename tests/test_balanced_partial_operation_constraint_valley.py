import unittest

from enterprise_math.balanced_operation_constraint_valley import (
    balance_shape_pair,
    balanced_partition_shape,
)
from enterprise_math.balanced_partial_operation_constraint_valley import (
    augmented_partial_power_sum,
    augmented_power_sum_log_convex,
    balanced_safe_partial_count,
    most_constraining_partial_partition,
    partial_balancing_strictly_reduces_safe_count,
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


class BalancedPartialOperationConstraintValleyTests(unittest.TestCase):
    def test_augmented_power_sum_sequence_is_log_convex(self):
        checked = 0
        for state_count in range(2, 13):
            for shape in integer_partitions(state_count):
                for exponent in range(1, 8):
                    self.assertTrue(
                        augmented_power_sum_log_convex(shape, exponent)
                    )
                    checked += 1
        self.assertGreater(checked, 1000)

    def test_every_legal_balance_strictly_reduces_partial_safe_count(self):
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
                        self.assertTrue(
                            partial_balancing_strictly_reduces_safe_count(
                                shape, large_index, small_index
                            )
                        )
                        self.assertLess(
                            safe_partial_count_from_shape(balanced),
                            safe_partial_count_from_shape(shape),
                        )
                        checked += 1
        self.assertGreater(checked, 500)

    def test_balanced_shape_is_unique_partial_minimum_at_fixed_block_count(self):
        checked = 0
        for state_count in range(3, 14):
            for block_count in range(2, state_count):
                balanced = balanced_partition_shape(
                    state_count, block_count
                )
                balanced_count = balanced_safe_partial_count(
                    state_count, block_count
                )
                candidates = [
                    shape
                    for shape in integer_partitions(state_count)
                    if len(shape) == block_count
                ]
                minima = [
                    shape
                    for shape in candidates
                    if safe_partial_count_from_shape(shape) == balanced_count
                ]
                self.assertEqual(minima, [balanced])
                checked += 1
        self.assertGreater(checked, 50)

    def test_global_partial_valley_compiler_matches_all_partition_oracle(self):
        for state_count in range(3, 15):
            report = most_constraining_partial_partition(state_count)
            intermediate = [
                shape
                for shape in integer_partitions(state_count)
                if shape != (state_count,)
                and shape != (1,) * state_count
            ]
            direct_minimum = min(
                safe_partial_count_from_shape(shape)
                for shape in intermediate
            )
            direct_shapes = [
                shape
                for shape in intermediate
                if safe_partial_count_from_shape(shape) == direct_minimum
            ]
            self.assertEqual(report.safe_partial_count, direct_minimum)
            self.assertIn(report.block_shape, direct_shapes)

    def test_balanced_partial_closed_formula_matches_direct_product(self):
        for state_count in range(2, 40):
            for block_count in range(1, state_count + 1):
                shape = balanced_partition_shape(
                    state_count, block_count
                )
                self.assertEqual(
                    balanced_safe_partial_count(
                        state_count, block_count
                    ),
                    safe_partial_count_from_shape(shape),
                )

    def test_undefined_is_exact_augmented_unit_target(self):
        shapes = ((2, 1), (2, 2), (3, 2, 1), (4, 1, 1))
        for shape in shapes:
            for exponent in range(1, 6):
                self.assertEqual(
                    augmented_partial_power_sum(shape, exponent),
                    1 + sum(size**exponent for size in shape),
                )

    def test_total_and_partial_valleys_need_not_choose_same_block_count(self):
        # This test only requires one exact witness; it does not claim a fixed
        # ordering between the two valley locations.
        from enterprise_math.balanced_operation_constraint_valley import (
            most_constraining_partition,
        )

        witnesses = []
        for state_count in range(3, 40):
            total = most_constraining_partition(state_count)
            partial = most_constraining_partial_partition(state_count)
            if total.block_count != partial.block_count:
                witnesses.append(
                    (
                        state_count,
                        total.block_count,
                        partial.block_count,
                    )
                )
        self.assertTrue(witnesses)

    def test_validation(self):
        with self.assertRaises(ValueError):
            safe_partial_count_from_shape(())
        with self.assertRaises(ValueError):
            partial_balancing_strictly_reduces_safe_count((2, 2), 0, 1)
        with self.assertRaises(ValueError):
            most_constraining_partial_partition(2)
        with self.assertRaises(TypeError):
            augmented_partial_power_sum((2, 1), True)


if __name__ == "__main__":
    unittest.main()
