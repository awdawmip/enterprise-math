import unittest
from fractions import Fraction

from enterprise_math.safe_operation_collision_moments import (
    collision_power_sum,
    equal_block_total_safe_count,
    equal_block_total_safe_probability,
    most_constraining_equal_block_partition,
    partial_operation_constraint_deficit,
    safe_partial_probability,
    safe_partial_probability_from_block_factors,
    safe_total_probability,
    safe_total_probability_from_collision_moments,
    total_operation_constraint_deficit,
)


def partition_from_sizes(sizes):
    result = {}
    state = 0
    for label, size in enumerate(sizes):
        for _ in range(size):
            result[state] = label
            state += 1
    return result


class SafeOperationCollisionMomentTests(unittest.TestCase):
    def test_total_probability_is_product_of_collision_moments(self):
        shapes = (
            (4,),
            (3, 1),
            (2, 2),
            (2, 1, 1),
            (1, 1, 1, 1),
            (3, 2, 1),
            (2, 2, 2),
        )
        for shape in shapes:
            partition = partition_from_sizes(shape)
            self.assertEqual(
                safe_total_probability(partition),
                safe_total_probability_from_collision_moments(partition),
            )

    def test_partial_probability_is_product_of_source_block_factors(self):
        shapes = (
            (4,),
            (3, 1),
            (2, 2),
            (2, 1, 1),
            (1, 1, 1, 1),
            (3, 2, 1),
            (2, 2, 2),
        )
        for shape in shapes:
            partition = partition_from_sizes(shape)
            self.assertEqual(
                safe_partial_probability(partition),
                safe_partial_probability_from_block_factors(partition),
            )

    def test_collision_power_sum_matches_direct_block_mass_powers(self):
        partition = partition_from_sizes((3, 2, 1))
        self.assertEqual(collision_power_sum(partition, 1), Fraction(1, 1))
        self.assertEqual(
            collision_power_sum(partition, 2),
            Fraction(3**2 + 2**2 + 1, 6**2),
        )
        self.assertEqual(
            collision_power_sum(partition, 3),
            Fraction(3**3 + 2**3 + 1, 6**3),
        )

    def test_total_operation_probability_reconnects_exactly_at_both_extremes(self):
        for n in range(2, 9):
            indiscrete = partition_from_sizes((n,))
            discrete = partition_from_sizes((1,) * n)
            self.assertEqual(safe_total_probability(indiscrete), 1)
            self.assertEqual(safe_total_probability(discrete), 1)
            self.assertEqual(total_operation_constraint_deficit(indiscrete), 0)
            self.assertEqual(total_operation_constraint_deficit(discrete), 0)

    def test_genuine_intermediate_partitions_have_positive_total_constraint_deficit(self):
        shapes = (
            (2, 1),
            (2, 2),
            (3, 1),
            (2, 1, 1),
            (3, 2),
            (2, 2, 1),
            (4, 1, 1),
            (3, 3),
        )
        for shape in shapes:
            partition = partition_from_sizes(shape)
            self.assertGreater(total_operation_constraint_deficit(partition), 0)
            self.assertLess(safe_total_probability(partition), 1)

    def test_partial_operation_probability_has_only_discrete_full_freedom(self):
        for n in range(2, 8):
            indiscrete = partition_from_sizes((n,))
            discrete = partition_from_sizes((1,) * n)
            self.assertLess(safe_partial_probability(indiscrete), 1)
            self.assertGreater(partial_operation_constraint_deficit(indiscrete), 0)
            self.assertEqual(safe_partial_probability(discrete), 1)
            self.assertEqual(partial_operation_constraint_deficit(discrete), 0)

    def test_equal_block_probability_has_closed_form(self):
        for n, block_size in (
            (4, 2),
            (6, 2),
            (6, 3),
            (12, 3),
            (16, 4),
            (30, 5),
        ):
            block_count = n // block_size
            partition = partition_from_sizes((block_size,) * block_count)
            expected = Fraction(1, block_count ** (n - block_count))
            self.assertEqual(
                equal_block_total_safe_probability(n, block_size),
                expected,
            )
            self.assertEqual(
                safe_total_probability(partition),
                expected,
            )
            self.assertEqual(
                equal_block_total_safe_count(n, block_size),
                expected * n**n,
            )

    def test_exact_equal_block_valley_moves_to_larger_block_size(self):
        # These state counts have enough divisors to expose the slow migration
        # predicted by the continuous m*=W(e*n) calibration, without evaluating
        # Lambert W numerically in the executable theorem layer.
        expected = {
            4: 2,
            12: 3,
            48: 4,
            180: 5,
            720: 6,
        }
        for n, block_size in expected.items():
            report = most_constraining_equal_block_partition(n)
            self.assertEqual(report.block_size, block_size)
            self.assertEqual(report.block_count, n // block_size)
            self.assertEqual(
                report.safe_total_count,
                equal_block_total_safe_count(n, block_size),
            )
            self.assertEqual(
                report.safe_probability,
                equal_block_total_safe_probability(n, block_size),
            )

    def test_four_state_constraint_valley_matches_safe_spectrum(self):
        indiscrete = partition_from_sizes((4,))
        middle = partition_from_sizes((2, 2))
        discrete = partition_from_sizes((1, 1, 1, 1))
        self.assertEqual(safe_total_probability(indiscrete), Fraction(1, 1))
        self.assertEqual(safe_total_probability(middle), Fraction(1, 4))
        self.assertEqual(safe_total_probability(discrete), Fraction(1, 1))
        self.assertEqual(
            total_operation_constraint_deficit(middle),
            Fraction(3, 4),
        )

    def test_validation(self):
        with self.assertRaises(ValueError):
            collision_power_sum({}, 2)
        with self.assertRaises(ValueError):
            collision_power_sum({0: 0}, 0)
        with self.assertRaises(TypeError):
            collision_power_sum({0: 0}, True)
        with self.assertRaises(ValueError):
            equal_block_total_safe_count(6, 4)
        with self.assertRaises(ValueError):
            most_constraining_equal_block_partition(7)
        with self.assertRaises(TypeError):
            equal_block_total_safe_count(True, 1)


if __name__ == "__main__":
    unittest.main()
