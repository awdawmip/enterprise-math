import unittest

from enterprise_math.abc_small_derivative_block import (
    capacity_pressure,
    compressed_escape_count,
    minimum_escape_radius_by_counts,
    normalized_block_capacity,
    rational_small_derivative_bound_holds,
    witness_capacity_slack,
)


class AbcSmallDerivativeBlockTests(unittest.TestCase):
    def test_exact_integer_block_capacities(self) -> None:
        self.assertEqual(normalized_block_capacity(1), 0)
        self.assertEqual(normalized_block_capacity(22), 13)
        self.assertEqual(normalized_block_capacity(242), 15)
        self.assertEqual(normalized_block_capacity(243), 5)
        self.assertEqual(normalized_block_capacity(512), 9)

    def test_1_plus_242_capacity_lower_bound_and_zero_floor_slack(self) -> None:
        pressure = capacity_pressure(1, 242, 243)
        self.assertEqual(pressure.pair_capacity_ab, 15)
        self.assertEqual(pressure.multiplicity_residual_c, 81)
        self.assertEqual(pressure.mu_capacity_lower_bound, 6)
        self.assertEqual(pressure.mu, 27)
        self.assertEqual(pressure.exact_c_upper_capacity, 1215)
        self.assertEqual(witness_capacity_slack(1, 242, 243, 27, 5), 0)

    def test_capacity_slack_distinguishes_nonextremal_floor_access(self) -> None:
        self.assertEqual(witness_capacity_slack(1, 22, 23, 5, 1), 64)
        self.assertEqual(witness_capacity_slack(5, 7, 12, 2, 2), 20)

    def test_compressed_escape_count_recovers_mu(self) -> None:
        before = compressed_escape_count(1, 8, 9, 1)
        self.assertEqual(before.additive_state_count, 1)
        self.assertEqual(before.nondegenerate_state_count, 0)
        self.assertFalse(before.escaped)

        at = compressed_escape_count(1, 8, 9, 2)
        self.assertGreater(at.nondegenerate_state_count, 0)
        self.assertTrue(at.escaped)
        self.assertEqual(minimum_escape_radius_by_counts(1, 8, 9), 2)
        self.assertEqual(minimum_escape_radius_by_counts(2, 3, 5), 1)

    def test_rational_small_derivative_threshold_uses_only_integer_powers(self) -> None:
        self.assertFalse(rational_small_derivative_bound_holds(1, 242, 243, 1, 2))
        self.assertTrue(rational_small_derivative_bound_holds(1, 242, 243, 2, 3))
        self.assertTrue(rational_small_derivative_bound_holds(2, 3, 5, 1, 2))


if __name__ == "__main__":
    unittest.main()
