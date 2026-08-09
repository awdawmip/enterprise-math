import unittest

from enterprise_math.centered_prime_radius import (
    centered_prime_pair,
    centered_prime_radius,
    centered_radius_parity,
    centered_shell_data,
    fixed_slack_centered_criterion,
    slack_centered_radius_equivalence,
)
from enterprise_math.legendre import is_prime
from enterprise_math.prime_gap_slack import factor_proof_slack


class CenteredPrimeRadiusTests(unittest.TestCase):
    def test_centered_shell_matches_symmetric_prime_pair(self):
        saw_nonempty = False
        saw_empty = False
        for center in range(5, 350):
            for radius in range(1, min(center, 14)):
                left = center - radius
                if left < 3 or not is_prime(left) or left <= radius * radius:
                    continue
                data = centered_shell_data(center, radius)
                pair = centered_prime_pair(center, radius)
                self.assertEqual(data["nonempty"], pair is not None)
                self.assertEqual(data["square_offset"], radius * radius)
                if pair is not None:
                    saw_nonempty = True
                    self.assertEqual(pair[0] + pair[1], 2 * center)
                    self.assertEqual(data["shell"], [center * center - radius * radius])
                else:
                    saw_empty = True
                    self.assertEqual(data["shell"], [])
        self.assertTrue(saw_nonempty)
        self.assertTrue(saw_empty)

    def test_actual_slack_is_minimal_centered_radius_in_range(self):
        saw = False
        for k in range(4, 900):
            slack = factor_proof_slack(k)
            radius = slack + 1
            left = k + 1 - radius
            if left < 3 or left <= radius * radius:
                continue
            data = slack_centered_radius_equivalence(k)
            self.assertTrue(data["verified"])
            self.assertEqual(data["slack"], slack)
            self.assertEqual(data["radius"], radius)
            self.assertEqual(centered_prime_radius(k + 1), radius)
            self.assertEqual(
                data["left_prime"] + data["right_prime"], 2 * (k + 1)
            )
            saw = True
        self.assertTrue(saw)

    def test_fixed_slack_criterion_uses_first_centered_pair(self):
        saw_true = False
        saw_false = False
        for k in range(4, 350):
            for slack in range(0, min(k, 10)):
                radius = slack + 1
                left = k + 1 - radius
                if left < 3 or not is_prime(left) or left <= radius * radius:
                    continue
                data = fixed_slack_centered_criterion(k, slack)
                self.assertEqual(data["criterion"], factor_proof_slack(k) == slack)
                if data["criterion"]:
                    saw_true = True
                    self.assertIsNone(data["smaller_pair_radius"])
                else:
                    saw_false = True
        self.assertTrue(saw_true)
        self.assertTrue(saw_false)

    def test_radius_parity(self):
        saw = False
        for k in range(4, 700):
            slack = factor_proof_slack(k)
            radius = slack + 1
            left = k + 1 - radius
            if left < 3 or left <= radius * radius:
                continue
            data = centered_radius_parity(k)
            self.assertTrue(data["verified"])
            self.assertEqual(data["radius"] % 2, k % 2)
            saw = True
        self.assertTrue(saw)

    def test_size_hypothesis_is_essential(self):
        # Counterexample to the over-strong global identity rho(k+1)=sigma(k)+1.
        # At k=10, sigma=3, but the first positive centered prime pair around 11
        # is 5 and 17, at radius 6 rather than radius 4.
        k = 10
        self.assertEqual(factor_proof_slack(k), 3)
        self.assertEqual(centered_prime_radius(k + 1), 6)
        self.assertNotEqual(
            centered_prime_radius(k + 1), factor_proof_slack(k) + 1
        )
        radius = factor_proof_slack(k) + 1
        left = k + 1 - radius
        self.assertLessEqual(left, radius * radius)


if __name__ == "__main__":
    unittest.main()
