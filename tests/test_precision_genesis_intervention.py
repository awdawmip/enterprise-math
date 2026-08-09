import unittest
from fractions import Fraction

from enterprise_math.precision_genesis_intervention import (
    adaptive_two_step_counts,
    local_uniform_response_table,
    marginal_counts,
    master_response_seeds,
)


class PrecisionGenesisInterventionTests(unittest.TestCase):
    def test_local_rational_kernel_becomes_uniform_finite_table(self):
        table = local_uniform_response_table(
            (Fraction(1, 2), Fraction(1, 3), Fraction(1, 6))
        )
        self.assertEqual(table, (0, 0, 0, 1, 1, 2))

    def test_master_table_reproduces_every_context_marginal(self):
        kernels = (
            (Fraction(1, 2), Fraction(1, 2)),
            (Fraction(1, 3), Fraction(2, 3)),
            (Fraction(3, 4), Fraction(1, 4)),
        )
        seeds = master_response_seeds(kernels)
        self.assertEqual(len(seeds), 24)
        self.assertEqual(marginal_counts(seeds, 0), (12, 12))
        self.assertEqual(marginal_counts(seeds, 1), (8, 16))
        self.assertEqual(marginal_counts(seeds, 2), (18, 6))

    def test_adaptive_policy_is_reproduced_by_same_presampled_seed(self):
        kernels = (
            (Fraction(1, 2), Fraction(1, 2)),
            (Fraction(1, 3), Fraction(2, 3)),
            (Fraction(3, 4), Fraction(1, 4)),
        )
        seeds = master_response_seeds(kernels)
        # First use context 0.  If outcome is 0, next use context 1; if 1,
        # next use context 2.  The same seed already contains both unused
        # counterfactual responses.
        self.assertEqual(
            adaptive_two_step_counts(seeds, 0, (1, 2)),
            {(0, 0): 4, (0, 1): 8, (1, 0): 9, (1, 1): 3},
        )

    def test_invalid_rows_fail_closed(self):
        with self.assertRaises(ValueError):
            local_uniform_response_table((Fraction(1, 3), Fraction(1, 3)))
        with self.assertRaises(ValueError):
            master_response_seeds(())


if __name__ == "__main__":
    unittest.main()
