import unittest

from enterprise_math.legendre import is_prime
from enterprise_math.prime_gap_slack import (
    bounded_gap_to_slack_constant,
    factor_proof_slack,
    near_diagonal_shell_data,
    prime_pair_to_slack_bound,
    sigma_one_cousin_equivalence,
    sigma_zero_twin_equivalence,
    slack_implies_fixed_gap,
)


class PrimeGapSlackTests(unittest.TestCase):
    def test_slack_zero_exactly_matches_twin_primes(self):
        for k in range(3, 700):
            self.assertTrue(sigma_zero_twin_equivalence(k))

    def test_slack_one_exactly_matches_gap_four_prime_pairs(self):
        for k in range(4, 700):
            self.assertTrue(sigma_one_cousin_equivalence(k))

    def test_near_diagonal_shell_is_singleton_exactly_at_prime_pair(self):
        saw_nonempty = False
        saw_empty = False
        for k in range(4, 350):
            for slack in range(0, min(k, 12)):
                p = k - slack
                if p < 3 or not is_prime(p) or p <= (slack + 1) ** 2:
                    continue
                data = near_diagonal_shell_data(k, slack)
                q = p + 2 * (slack + 1)
                self.assertEqual(data["nonempty"], is_prime(q))
                self.assertEqual(data["gap"], 2 * (slack + 1))
                if data["nonempty"]:
                    saw_nonempty = True
                    self.assertEqual(data["shell"], [p * q])
                else:
                    saw_empty = True
                    self.assertEqual(data["shell"], [])
        self.assertTrue(saw_nonempty)
        self.assertTrue(saw_empty)

    def test_actual_small_slack_forces_corresponding_fixed_gap(self):
        saw = False
        for k in range(5, 700):
            slack = factor_proof_slack(k)
            p = k - slack
            if p < 3 or p <= (slack + 1) ** 2:
                continue
            data = slack_implies_fixed_gap(k)
            self.assertTrue(data["verified"])
            self.assertEqual(data["gap"], 2 * (slack + 1))
            self.assertTrue(is_prime(data["p"]))
            self.assertTrue(is_prime(data["q"]))
            saw = True
        self.assertTrue(saw)

    def test_fixed_prime_pairs_create_bounded_slack(self):
        saw = False
        for p in range(3, 500):
            if not is_prime(p):
                continue
            for half_gap in range(1, 11):
                q = p + 2 * half_gap
                if not is_prime(q) or p <= half_gap**2:
                    continue
                data = prime_pair_to_slack_bound(p, half_gap)
                self.assertLessEqual(data["actual_slack"], half_gap - 1)
                self.assertEqual(data["gap"], 2 * half_gap)
                saw = True
        self.assertTrue(saw)

    def test_polymath_246_arithmetic_conversion_is_122(self):
        self.assertEqual(bounded_gap_to_slack_constant(246), 122)
        self.assertEqual(bounded_gap_to_slack_constant(247), 122)


if __name__ == "__main__":
    unittest.main()
