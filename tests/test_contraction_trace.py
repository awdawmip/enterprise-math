import math
import unittest

from enterprise_math.contraction_trace import (
    balanced_minimizer_count,
    directed_boundary_split,
    fiber_excess_energy,
    fiber_witness_interval,
    fiber_witness_multiplicity,
    oriented_contraction_history_count,
    two_block_argmin_profile,
    unoriented_partition_chain_count,
)
from enterprise_math.dimension_contraction import balanced_power_energy


class ContractionTraceTests(unittest.TestCase):
    def test_argmin_profile_is_exact_and_multiplicity_preserving(self):
        for power in range(1, 5):
            for left_size in range(1, 5):
                for right_size in range(1, 5):
                    for total in range(-10, 11):
                        profile = two_block_argmin_profile(
                            left_size, right_size, power, total
                        )
                        minimum = balanced_power_energy(
                            left_size + right_size, power, total
                        )
                        for left_total, _ in profile:
                            self.assertEqual(
                                balanced_power_energy(left_size, power, left_total)
                                + balanced_power_energy(
                                    right_size, power, total - left_total
                                ),
                                minimum,
                            )
                        self.assertEqual(
                            sum(multiplicity for _, multiplicity in profile),
                            balanced_minimizer_count(
                                left_size + right_size, power, total
                            ),
                        )

    def test_fiber_sublevel_set_is_exact_integer_interval(self):
        for power in range(1, 5):
            for left_size in range(1, 4):
                for right_size in range(1, 4):
                    for total in range(-6, 7):
                        for slack in range(0, 12):
                            left, right = fiber_witness_interval(
                                left_size, right_size, power, total, slack
                            )
                            actual = [
                                split
                                for split in range(left - 4, right + 5)
                                if fiber_excess_energy(
                                    left_size,
                                    right_size,
                                    power,
                                    total,
                                    split,
                                )
                                <= slack
                            ]
                            self.assertEqual(actual, list(range(left, right + 1)))
                            self.assertEqual(
                                fiber_witness_multiplicity(
                                    left_size,
                                    right_size,
                                    power,
                                    total,
                                    slack,
                                ),
                                len(actual),
                            )

    def test_directed_boundary_is_right_endpoint(self):
        for power in range(1, 5):
            for receiver_size, donor_size in ((1, 1), (2, 1), (2, 3)):
                for total in range(-5, 6):
                    for slack in range(0, 10):
                        left, right = fiber_witness_interval(
                            receiver_size, donor_size, power, total, slack
                        )
                        receiver_total, donor_total = directed_boundary_split(
                            receiver_size, donor_size, power, total, slack
                        )
                        self.assertEqual(receiver_total, right)
                        self.assertEqual(donor_total, total - right)
                        self.assertLessEqual(
                            fiber_excess_energy(
                                receiver_size,
                                donor_size,
                                power,
                                total,
                                right,
                            ),
                            slack,
                        )
                        self.assertGreater(
                            fiber_excess_energy(
                                receiver_size,
                                donor_size,
                                power,
                                total,
                                right + 1,
                            ),
                            slack,
                        )
                        self.assertLessEqual(left, right)

    def test_partition_chain_counts(self):
        for slot_count in range(1, 9):
            expected_unoriented = 1
            expected_oriented = 1
            for block_count in range(2, slot_count + 1):
                expected_unoriented *= math.comb(block_count, 2)
                expected_oriented *= block_count * (block_count - 1)
            self.assertEqual(
                unoriented_partition_chain_count(slot_count), expected_unoriented
            )
            self.assertEqual(
                oriented_contraction_history_count(slot_count), expected_oriented
            )
            self.assertEqual(
                oriented_contraction_history_count(slot_count),
                (2 ** (slot_count - 1))
                * unoriented_partition_chain_count(slot_count),
            )


if __name__ == "__main__":
    unittest.main()
