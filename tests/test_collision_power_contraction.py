import itertools
import unittest

from enterprise_math.dimension_contraction import (
    balanced_power_defect,
    balanced_power_energy,
    balanced_power_residue_shell,
    min_plus_merge_power_energy,
    partition_power_energy,
)


def zero_sum_states(coordinate_count: int, bound: int):
    for prefix in itertools.product(range(-bound, bound + 1), repeat=coordinate_count - 1):
        yield prefix + (-sum(prefix),)


def merged_partition(block_sizes: tuple[int, ...], left: int, right: int) -> tuple[int, ...]:
    return tuple(
        block_sizes[index]
        for index in range(len(block_sizes))
        if index not in (left, right)
    ) + (block_sizes[left] + block_sizes[right],)


def ball_count(block_sizes: tuple[int, ...], power: int, threshold: int, bound: int = 10) -> int:
    return sum(
        partition_power_energy(block_sizes, power, state) <= threshold
        for state in zero_sum_states(len(block_sizes), bound)
    )


def cut_count(
    block_sizes: tuple[int, ...], power: int, threshold: int, receiver: int, donor: int,
    bound: int = 10,
) -> int:
    count = 0
    for state in zero_sum_states(len(block_sizes), bound):
        if partition_power_energy(block_sizes, power, state) > threshold:
            continue
        moved = list(state)
        moved[receiver] += 1
        moved[donor] -= 1
        if partition_power_energy(block_sizes, power, tuple(moved)) > threshold:
            count += 1
    return count


class CollisionPowerContractionTests(unittest.TestCase):
    def test_one_is_invariant_for_all_tested_slot_counts_and_powers(self):
        for block_size in range(1, 20):
            for power in range(1, 7):
                self.assertEqual(balanced_power_energy(block_size, power, 1), 1)
                self.assertEqual(balanced_power_energy(block_size, power, -1), 1)

    def test_power_one_is_block_insensitive(self):
        for block_size in range(1, 10):
            for total in range(-30, 31):
                self.assertEqual(balanced_power_energy(block_size, 1, total), abs(total))
                self.assertEqual(balanced_power_defect(block_size, 1, total), 0)
                self.assertEqual(balanced_power_residue_shell(block_size, 1, total), 0)

    def test_general_residue_shell_matches_scaled_power_defect(self):
        for block_size in range(1, 10):
            for power in range(2, 8):
                for total in range(-50, 51):
                    defect = balanced_power_defect(block_size, power, total)
                    shell = balanced_power_residue_shell(block_size, power, total)
                    self.assertEqual(defect, shell)
                    self.assertGreaterEqual(defect, 0)
                    self.assertEqual(
                        defect == 0,
                        abs(total) % block_size == 0,
                    )

    def test_square_layer_is_the_bounded_residue_special_case(self):
        for block_size in range(1, 20):
            for total in range(-100, 101):
                remainder = abs(total) % block_size
                self.assertEqual(
                    balanced_power_defect(block_size, 2, total),
                    remainder * (block_size - remainder),
                )

    def test_cubic_layer_keeps_same_residue_gate_but_has_lower_degree_bulk(self):
        for block_size in range(1, 10):
            for total in range(-100, 101):
                magnitude = abs(total)
                q, r = divmod(magnitude, block_size)
                expected = r * (block_size - r) * (
                    3 * block_size * q + block_size + r
                )
                self.assertEqual(
                    balanced_power_defect(block_size, 3, total),
                    expected,
                )

    def test_min_plus_dimension_addition_for_multiple_powers(self):
        for power in range(1, 6):
            for left in range(1, 5):
                for right in range(1, 5):
                    for total in range(-8, 9):
                        actual = min(
                            balanced_power_energy(left, power, split)
                            + balanced_power_energy(right, power, total - split)
                            for split in range(-20, 21)
                        )
                        self.assertEqual(
                            actual,
                            min_plus_merge_power_energy(left, right, power, total),
                        )

    def test_cut_boundary_closes_to_merged_tagged_ball_for_multiple_powers(self):
        partitions = ((1, 1, 1), (1, 1, 1, 1), (2, 1, 1), (2, 2, 1))
        for power in range(1, 5):
            for block_sizes in partitions:
                for threshold in range(0, 9):
                    for receiver in range(len(block_sizes)):
                        for donor in range(len(block_sizes)):
                            if receiver == donor:
                                continue
                            self.assertEqual(
                                cut_count(block_sizes, power, threshold, receiver, donor),
                                ball_count(
                                    merged_partition(block_sizes, receiver, donor),
                                    power,
                                    threshold,
                                ),
                                msg=(power, block_sizes, threshold, receiver, donor),
                            )


if __name__ == "__main__":
    unittest.main()
