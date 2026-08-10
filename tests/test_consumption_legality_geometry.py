import itertools
import math
import unittest

from enterprise_math import consumption_legality_geometry as clg


class ConsumptionLegalityGeometryTests(unittest.TestCase):
    def test_independent_axis_decrements_generate_product_block_quotient(self):
        steps = (2, 3)
        consumptions = ((2, 0), (0, 3))
        states = list(itertools.product(range(7), range(8)))
        for left in states:
            for right in states:
                self.assertEqual(
                    clg.same_continuation_profile(left, right, consumptions),
                    clg.axis_block_quotient(left, steps)
                    == clg.axis_block_quotient(right, steps),
                )

    def test_coupled_consumption_creates_variable_dimension_wedge(self):
        consumptions = ((1, 0), (1, 1))
        states = list(itertools.product(range(7), range(9)))
        for left in states:
            for right in states:
                self.assertEqual(
                    clg.same_continuation_profile(left, right, consumptions),
                    clg.coupled_wedge_quotient(*left)
                    == clg.coupled_wedge_quotient(*right),
                )
        self.assertTrue(clg.same_continuation_profile((4, 4), (4, 8), consumptions))
        self.assertFalse(clg.same_continuation_profile((4, 2), (4, 3), consumptions))

    def test_one_dimensional_monoid_profiles_change_only_at_consumable_thresholds(self):
        consumptions = ((4,), (6,))
        profiles = [clg.feasible_operation_counts((n,), consumptions) for n in range(17)]
        for a, b in ((0, 3), (4, 5), (6, 7), (8, 9), (10, 11), (12, 13)):
            self.assertEqual(profiles[a], profiles[b])
        for threshold in (4, 6, 8, 10, 12, 14, 16):
            self.assertNotEqual(profiles[threshold - 1], profiles[threshold])

    def test_block_fiber_size_matches_bruteforce(self):
        block_sizes = (2, 1, 2)
        totals = (3, 2, 2)
        states = itertools.product(range(4), repeat=sum(block_sizes))
        count = sum(
            1 for state in states if clg.block_totals(state, block_sizes) == totals
        )
        self.assertEqual(count, clg.block_fiber_size(totals, block_sizes))
        self.assertEqual(
            count,
            math.comb(4, 1) * math.comb(2, 0) * math.comb(3, 1),
        )

    def test_visible_hidden_dimension_balance(self):
        self.assertEqual(clg.block_clock_dimension_balance((3, 2, 4)), (3, 6, 9))
        self.assertEqual(clg.block_clock_dimension_balance((9,)), (1, 8, 9))
        self.assertEqual(clg.block_clock_dimension_balance((1,) * 9), (9, 0, 9))


if __name__ == "__main__":
    unittest.main()
