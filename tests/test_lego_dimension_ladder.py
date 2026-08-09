import unittest

from enterprise_math.lego_dimension_ladder import (
    adjacent_lower,
    allocation_row,
    dimension_ladder_identity,
    prefix_accumulate,
)


class LegoDimensionLadderTests(unittest.TestCase):
    def test_prefix_and_adjacent_difference_are_exact_inverses(self):
        examples = (
            (1,),
            (1, 2, 3, 4),
            (2, -1, 5, 0, 7),
        )
        for values in examples:
            self.assertEqual(adjacent_lower(prefix_accumulate(values)), values)

    def test_allocation_dimension_raises_by_prefix_accumulation(self):
        # H1 = 1,1,1,... ; H2 = 1,2,3,... ; H3 = 1,3,6,10,...
        self.assertEqual(allocation_row(1, 5), (1, 1, 1, 1, 1, 1))
        self.assertEqual(allocation_row(2, 5), (1, 2, 3, 4, 5, 6))
        self.assertEqual(allocation_row(3, 5), (1, 3, 6, 10, 15, 21))
        self.assertEqual(prefix_accumulate(allocation_row(1, 5)), allocation_row(2, 5))
        self.assertEqual(prefix_accumulate(allocation_row(2, 5)), allocation_row(3, 5))

    def test_allocation_dimension_lowers_by_exact_integer_difference(self):
        self.assertEqual(adjacent_lower(allocation_row(4, 7)), allocation_row(3, 7))
        self.assertEqual(adjacent_lower(allocation_row(3, 7)), allocation_row(2, 7))
        self.assertEqual(adjacent_lower(allocation_row(2, 7)), allocation_row(1, 7))

    def test_ladder_identity_many_small_dimensions(self):
        for capacity in range(1, 9):
            for maximum_total in range(0, 12):
                self.assertTrue(dimension_ladder_identity(capacity, maximum_total))

    def test_one_value_does_not_change_when_dimension_rises(self):
        # A single unit stays a single unit; only its placement multiplicity grows.
        for capacity in range(1, 8):
            row = allocation_row(capacity, 1)
            self.assertEqual(row[0], 1)
            self.assertEqual(row[1], capacity)


if __name__ == "__main__":
    unittest.main()
