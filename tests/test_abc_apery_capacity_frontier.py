import math
import unittest

from enterprise_math.abc_apery_capacity_frontier import (
    capacity_frontier_signature,
    exact_access_from_capacity_frontier,
    frontier_size_bound_holds,
    residue_capacity_frontier,
    residue_capacity_sequence,
)
from enterprise_math.abc_block_access_apery import exact_block_access_radius


class AbcAperyCapacityFrontierTests(unittest.TestCase):
    def test_one_six_preperiod_is_one_capacity_jump(self) -> None:
        sequence = residue_capacity_sequence((1, 6), 5)
        self.assertEqual(
            tuple(
                (point.shift, point.factorization_radius, point.capacity_threshold)
                for point in sequence
            ),
            ((0, 5, 3), (1, 2, 0)),
        )
        frontier = residue_capacity_frontier((1, 6), 5)
        self.assertEqual(frontier.target_residue, 2)
        self.assertEqual(frontier.apery_value, 5)
        self.assertEqual(
            tuple((point.shift, point.capacity_threshold) for point in frontier.points),
            ((0, 3), (1, 0)),
        )

    def test_five_two_frontier_has_three_levels(self) -> None:
        frontier = residue_capacity_frontier((5, 2), 6)
        self.assertEqual(frontier.target_residue, 1)
        self.assertEqual(frontier.apery_value, 6)
        self.assertEqual(
            tuple(
                (
                    point.shift,
                    point.factorization_radius,
                    point.capacity_threshold,
                )
                for point in frontier.points
            ),
            ((0, 3, 2), (1, 4, 1), (2, 4, 0)),
        )

    def test_stage17_exception_is_frontier_threshold_crossing(self) -> None:
        frontier = residue_capacity_frontier((2, 5, 7, 8), 6)
        self.assertEqual(
            tuple((point.shift, point.capacity_threshold) for point in frontier.points),
            ((0, 2), (1, 0)),
        )
        signature = capacity_frontier_signature((2, 5, 7, 8))
        self.assertEqual(exact_access_from_capacity_frontier(signature, 16), 2)
        self.assertEqual(exact_access_from_capacity_frontier(signature, 38), 2)
        self.assertEqual(exact_access_from_capacity_frontier(signature, 60), 3)

    def test_frontier_reconstructs_entire_access_function(self) -> None:
        rows = ((1, 6), (5, 2), (2, 5, 7, 8), (15, 10, 6), (11, 4))
        for row in rows:
            signature = capacity_frontier_signature(row)
            for target in range(0, 120):
                self.assertEqual(
                    exact_access_from_capacity_frontier(signature, target),
                    exact_block_access_radius(row, target, max_radius=120),
                )

    def test_all_small_two_variable_rows_match_direct_oracle(self) -> None:
        checked = 0
        for A in range(1, 10):
            for B in range(1, 10):
                if math.gcd(A, B) != 1:
                    continue
                signature = capacity_frontier_signature((A, B))
                for target in range(0, 50):
                    self.assertEqual(
                        exact_access_from_capacity_frontier(signature, target),
                        exact_block_access_radius((A, B), target, max_radius=80),
                    )
                    checked += 1
        self.assertGreater(checked, 2000)

    def test_frontier_cardinality_bound(self) -> None:
        for row in ((1, 6), (5, 2), (2, 5, 7, 8), (15, 10, 6), (11, 4)):
            self.assertTrue(frontier_size_bound_holds(row))


if __name__ == "__main__":
    unittest.main()
