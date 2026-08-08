import itertools
import unittest

from enterprise_math.dimension_contraction import partition_fiber_energy


def zero_sum_states(coordinate_count: int, bound: int):
    for prefix in itertools.product(range(-bound, bound + 1), repeat=coordinate_count - 1):
        yield prefix + (-sum(prefix),)


def tagged_ball_count(block_sizes: tuple[int, ...], threshold: int, bound: int = 12) -> int:
    return sum(
        1
        for state in zero_sum_states(len(block_sizes), bound)
        if partition_fiber_energy(block_sizes, state) <= threshold
    )


def directed_cut_count(
    block_sizes: tuple[int, ...], threshold: int, receiver: int, donor: int, bound: int = 12
) -> int:
    count = 0
    for state in zero_sum_states(len(block_sizes), bound):
        if partition_fiber_energy(block_sizes, state) > threshold:
            continue
        moved = list(state)
        moved[receiver] += 1
        moved[donor] -= 1
        if partition_fiber_energy(block_sizes, tuple(moved)) > threshold:
            count += 1
    return count


def merged_partition(block_sizes: tuple[int, ...], left: int, right: int) -> tuple[int, ...]:
    merged = block_sizes[left] + block_sizes[right]
    return tuple(
        block_sizes[index]
        for index in range(len(block_sizes))
        if index not in (left, right)
    ) + (merged,)


class DimensionContractionBoundaryTests(unittest.TestCase):
    def test_directed_radial_cut_equals_merged_tagged_ball(self):
        partitions = (
            (1, 1, 1),
            (1, 1, 1, 1),
            (2, 1, 1),
            (2, 2, 1),
            (3, 1, 2),
        )
        for block_sizes in partitions:
            for threshold in range(0, 10):
                for receiver in range(len(block_sizes)):
                    for donor in range(len(block_sizes)):
                        if receiver == donor:
                            continue
                        actual = directed_cut_count(
                            block_sizes, threshold, receiver, donor
                        )
                        expected = tagged_ball_count(
                            merged_partition(block_sizes, receiver, donor), threshold
                        )
                        self.assertEqual(
                            actual,
                            expected,
                            msg=(block_sizes, threshold, receiver, donor),
                        )


if __name__ == "__main__":
    unittest.main()
