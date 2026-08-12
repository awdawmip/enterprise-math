import unittest

from enterprise_math.p017_p018_terminal_candidate_exact import (
    terminal_candidate_exact_profile,
)
from enterprise_math.p017_p018_terminal_partner_barrier import (
    terminal_residual_partner_dichotomy,
)


class P017P018TerminalPartnerBarrierTests(unittest.TestCase):
    def _routes(self, k: int) -> list[dict[str, object]]:
        profile = terminal_candidate_exact_profile(k)
        return [
            terminal_residual_partner_dichotomy(k, int(point))
            for point in profile["terminal_residual_points"]
        ]

    def test_k524287_both_terminal_residuals_route_directly_to_prime_witnesses(self):
        rows = self._routes(524_287)
        self.assertEqual(len(rows), 2)
        self.assertTrue(all(row["route"] == "PRIME_WITNESS" for row in rows))
        self.assertTrue(all(row["partner_is_prime"] for row in rows))

    def test_k8191_residuals_split_between_prime_and_high_product_routes(self):
        rows = self._routes(8_191)
        prime_rows = [row for row in rows if row["route"] == "PRIME_WITNESS"]
        high_rows = [row for row in rows if row["route"] == "HIGH_PRODUCT"]
        self.assertEqual(len(rows), 24)
        self.assertEqual(len(prime_rows), 4)
        self.assertEqual(len(high_rows), 20)
        for row in high_rows:
            self.assertGreaterEqual(
                row["pair_support_radical_product"],
                row["transverse_primorial_next"],
            )
            self.assertGreaterEqual(row["pair_complete_core_product"], 8_191)
            self.assertTrue(row["outside_residual_S_lt_k_hard_core"])

    def test_k20000_has_no_terminal_low_core_rows_to_route(self):
        profile = terminal_candidate_exact_profile(20_000)
        self.assertEqual(profile["terminal_residual_count"], 0)
        self.assertEqual(profile["terminal_residual_points"], ())


if __name__ == "__main__":
    unittest.main()
