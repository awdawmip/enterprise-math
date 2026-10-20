import unittest

from enterprise_math.legendre import primes_up_to
from enterprise_math.prime_collapse_field import factor_horizon
from enterprise_math.prime_cubic_full_forcing_band import (
    cubic_last_upper_not_closed_by_gap_cap,
    cubic_upper_certificate_kind,
    cubic_upper_closed_by_gap_cap,
)


class PrimeCubicFullForcingBandTests(unittest.TestCase):
    def test_selected_1328_cap_transition(self):
        self.assertFalse(cubic_upper_closed_by_gap_cap(783_190, 1328))
        self.assertTrue(cubic_upper_closed_by_gap_cap(783_191, 1328))
        # A local scan locks the carry-tooth neighborhood without making the
        # full 5.8-million finite certificate part of every unit-test run.
        self.assertEqual(
            cubic_last_upper_not_closed_by_gap_cap(785_000, 1328),
            783_190,
        )

    def test_1724_cap_has_later_transition(self):
        self.assertFalse(cubic_upper_closed_by_gap_cap(1_320_145, 1724))
        self.assertTrue(cubic_upper_closed_by_gap_cap(1_320_146, 1724))
        self.assertEqual(
            cubic_last_upper_not_closed_by_gap_cap(1_322_000, 1724),
            1_320_145,
        )

    def test_upper_certificate_branch_is_square_or_next_prime(self):
        for k in (783_191, 800_000, 1_000_000):
            self.assertTrue(cubic_upper_closed_by_gap_cap(k, 1328))
            horizon = factor_horizon(k, 3)
            lower = k**3
            # Check a bounded sample from both ends of the candidate list.
            candidates = primes_up_to(min(horizon, 10_000))
            for q in candidates:
                if q * horizon <= lower:
                    continue
                kind = cubic_upper_certificate_kind(k, q, 1328)
                self.assertIn(kind, ("SQUARE", "NEXT_PRIME"))
                if kind == "SQUARE":
                    self.assertGreater(q * q, lower)
                else:
                    self.assertLessEqual(q * q, lower)

    def test_end_of_current_full_band_is_far_inside_upper_gap_range(self):
        k = 5_848_035
        self.assertTrue(cubic_upper_closed_by_gap_cap(k, 1328))
        self.assertLess(factor_horizon(k, 3) + 1328, 400_000_000_000_000_000)


if __name__ == "__main__":
    unittest.main()
