import itertools
import unittest

from enterprise_math.dimension_contraction import (
    balanced_energy_increment,
    balanced_square_energy,
    min_plus_merge_energy,
    minimum_pair_collisions,
    partition_fiber_energy,
    transfer_energy_increment,
)


class DimensionContractionTests(unittest.TestCase):
    def test_one_is_dimension_invariant(self):
        for block_size in range(1, 20):
            self.assertEqual(balanced_square_energy(block_size, 1), 1)
            self.assertEqual(balanced_square_energy(block_size, -1), 1)

    def test_balanced_square_energy_matches_exhaustive_fiber_minimum(self):
        for block_size in range(1, 6):
            for total in range(-8, 9):
                bound = abs(total) + 3
                actual = min(
                    sum(x * x for x in coordinates)
                    for coordinates in itertools.product(range(-bound, bound + 1), repeat=block_size)
                    if sum(coordinates) == total
                )
                self.assertEqual(actual, balanced_square_energy(block_size, total))

    def test_min_plus_dimension_addition(self):
        for left in range(1, 6):
            for right in range(1, 6):
                for total in range(-10, 11):
                    actual = min(
                        balanced_square_energy(left, split)
                        + balanced_square_energy(right, total - split)
                        for split in range(-20, 21)
                    )
                    self.assertEqual(actual, min_plus_merge_energy(left, right, total))

    def test_square_energy_is_units_plus_twice_minimum_pair_collisions(self):
        for block_size in range(1, 10):
            for units in range(0, 40):
                self.assertEqual(
                    balanced_square_energy(block_size, units),
                    units + 2 * minimum_pair_collisions(block_size, units),
                )

    def test_increment_closed_form(self):
        for block_size in range(1, 10):
            for total in range(-30, 31):
                self.assertEqual(
                    balanced_square_energy(block_size, total + 1)
                    - balanced_square_energy(block_size, total),
                    balanced_energy_increment(block_size, total),
                )

    def test_partition_energy_matches_full_fiber_minimum(self):
        block_sizes = (2, 1, 2)
        totals = (1, -2, 1)
        expected = partition_fiber_energy(block_sizes, totals)
        candidates = []
        for a0 in range(-3, 4):
            for a1 in range(-3, 4):
                if a0 + a1 != totals[0]:
                    continue
                for c0 in range(-3, 4):
                    for c1 in range(-3, 4):
                        if c0 + c1 != totals[2]:
                            continue
                        candidates.append(a0*a0 + a1*a1 + totals[1]**2 + c0*c0 + c1*c1)
        self.assertEqual(expected, min(candidates))

    def test_transfer_increment_matches_recomputed_partition_energy(self):
        cases = [
            ((1, 1, 1, 1), (2, -1, -1, 0), 0, 1),
            ((2, 1, 1), (1, -2, 1), 0, 1),
            ((3, 2), (4, -4), 1, 0),
        ]
        for sizes, totals, receiver, donor in cases:
            moved = list(totals)
            moved[receiver] += 1
            moved[donor] -= 1
            self.assertEqual(
                transfer_energy_increment(sizes, totals, receiver, donor),
                partition_fiber_energy(sizes, tuple(moved))
                - partition_fiber_energy(sizes, totals),
            )


if __name__ == "__main__":
    unittest.main()
