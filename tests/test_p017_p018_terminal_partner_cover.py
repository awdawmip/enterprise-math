import unittest

from enterprise_math.legendre import is_prime
from enterprise_math.p017_p018_terminal_partner_cover import (
    terminal_partner_cover_profile,
)


class P017P018TerminalPartnerCoverTests(unittest.TestCase):
    def test_k8191_reduced_residual_splits_4_plus_20(self):
        data = terminal_partner_cover_profile(8_191)
        self.assertEqual(data["terminal_residual_count"], 24)
        self.assertEqual(data["prime_partner_witness_count"], 4)
        self.assertEqual(data["high_product_pair_token_count"], 20)
        self.assertTrue(data["prime_witness_certified"])
        for row in data["rows"]:
            if row["route"] == "PRIME_PARTNER_WITNESS":
                self.assertTrue(is_prime(row["partner"]))
            else:
                self.assertTrue(row["pair_token_single_use"])
                self.assertGreaterEqual(
                    row["pair_token_product"],
                    data["next_transverse_primorial"],
                )

    def test_k524287_both_residuals_are_prime_partner_witnesses(self):
        data = terminal_partner_cover_profile(524_287)
        self.assertEqual(data["terminal_residual_count"], 2)
        self.assertEqual(data["prime_partner_witness_count"], 2)
        self.assertEqual(data["high_product_pair_token_count"], 0)
        self.assertTrue(data["prime_witness_certified"])
        self.assertTrue(all(is_prime(row["partner"]) for row in data["rows"]))

    def test_k61_is_boundary_where_high_tokens_cover_every_residual(self):
        data = terminal_partner_cover_profile(61)
        self.assertEqual(data["terminal_residual_count"], 10)
        self.assertEqual(data["prime_partner_witness_count"], 0)
        self.assertEqual(data["high_product_pair_token_count"], 10)
        self.assertFalse(data["prime_witness_certified"])
        self.assertTrue(
            all(row["route"] == "HIGH_PRODUCT_PAIR_TOKEN" for row in data["rows"])
        )


if __name__ == "__main__":
    unittest.main()
