import unittest

from enterprise_math.partial_operation_valley_asymptotic import (
    balanced_partial_probability_sandwich_holds,
    balanced_partial_safe_probability,
    partial_ideal_candidate_block_counts,
    partial_to_total_count_ratio,
    partial_to_total_shape_factor_bound_holds,
    partial_to_total_shape_factor_upper_bound,
    partial_universe_scale,
    partial_valley_lies_in_ideal_candidate_window,
    total_and_partial_balanced_shapes,
)
from enterprise_math.safe_operation_collision_moments import (
    safe_partial_probability,
    safe_total_probability,
)


def partition_from_sizes(sizes):
    result = {}
    state = 0
    for label, size in enumerate(sizes):
        for _ in range(size):
            result[state] = label
            state += 1
    return result


def integer_partitions(total, maximum=None):
    if total == 0:
        yield ()
        return
    if maximum is None or maximum > total:
        maximum = total
    for first in range(maximum, 0, -1):
        for tail in integer_partitions(total - first, first):
            yield (first,) + tail


class PartialOperationValleyAsymptoticTests(unittest.TestCase):
    def test_exact_partial_to_total_shape_factor_and_bound(self):
        checked = 0
        for state_count in range(2, 13):
            for shape in integer_partitions(state_count):
                partition = partition_from_sizes(shape)
                ratio = partial_to_total_count_ratio(partition)
                self.assertGreaterEqual(ratio, 1)
                self.assertLessEqual(
                    ratio,
                    partial_to_total_shape_factor_upper_bound(partition),
                )
                self.assertTrue(
                    partial_to_total_shape_factor_bound_holds(partition)
                )
                checked += 1
        self.assertGreater(checked, 200)

    def test_probability_identity_matches_count_ratio(self):
        shapes = (
            (4,),
            (3, 1),
            (2, 2),
            (2, 1, 1),
            (1, 1, 1, 1),
            (3, 2, 1),
        )
        for shape in shapes:
            partition = partition_from_sizes(shape)
            n = sum(shape)
            ratio = partial_to_total_count_ratio(partition)
            self.assertEqual(
                safe_partial_probability(partition),
                partial_universe_scale(n)
                * safe_total_probability(partition)
                * ratio,
            )

    def test_shape_factor_bound_is_strictly_below_three(self):
        for block_count in range(1, 30):
            partition = partition_from_sizes((1,) * block_count)
            self.assertLess(
                partial_to_total_shape_factor_upper_bound(partition),
                3,
            )

    def test_balanced_partial_probability_uses_same_ideal_surrogate_sandwich(self):
        checked = 0
        for state_count in range(3, 81):
            for block_count in range(2, state_count):
                self.assertTrue(
                    balanced_partial_probability_sandwich_holds(
                        state_count, block_count
                    )
                )
                probability = balanced_partial_safe_probability(
                    state_count, block_count
                )
                self.assertGreater(probability, 0)
                self.assertLessEqual(probability, 1)
                checked += 1
        self.assertGreater(checked, 3000)

    def test_partial_ideal_candidate_window_contains_true_partial_valley(self):
        for state_count in range(3, 121):
            self.assertTrue(
                partial_valley_lies_in_ideal_candidate_window(
                    state_count
                )
            )

    def test_total_and_partial_valleys_can_differ_finitely_but_remain_balanced(self):
        witnesses = []
        for state_count in range(3, 50):
            total_shape, partial_shape = total_and_partial_balanced_shapes(
                state_count
            )
            self.assertEqual(sum(total_shape), state_count)
            self.assertEqual(sum(partial_shape), state_count)
            self.assertLessEqual(max(total_shape) - min(total_shape), 1)
            self.assertLessEqual(max(partial_shape) - min(partial_shape), 1)
            if total_shape != partial_shape:
                witnesses.append((state_count, total_shape, partial_shape))
        self.assertTrue(witnesses)

    def test_partial_universe_scale_has_expected_endpoint_behavior(self):
        previous = None
        for state_count in range(1, 30):
            scale = partial_universe_scale(state_count)
            self.assertGreater(scale, 0)
            self.assertLess(scale, 1)
            if previous is not None:
                self.assertLess(scale, previous)
            previous = scale

    def test_validation(self):
        with self.assertRaises(ValueError):
            partial_to_total_count_ratio({})
        with self.assertRaises(ValueError):
            balanced_partial_safe_probability(2, 1)
        with self.assertRaises(ValueError):
            balanced_partial_safe_probability(5, 5)
        with self.assertRaises(TypeError):
            partial_universe_scale(True)
        with self.assertRaises(ValueError):
            partial_ideal_candidate_block_counts(2)


if __name__ == "__main__":
    unittest.main()
