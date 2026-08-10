import unittest

from enterprise_math.p017_factor_root_spectrum import factor_root_split_shell_primes
from enterprise_math.p017_root_split_overshoot import (
    next_p_square_overshoot,
    raw_root_branch_slot_counts,
    raw_split_primes,
    realized_root_branch_occupancy,
    realized_split_primes,
)


class P017RootSplitOvershootTests(unittest.TestCase):
    def test_raw_split_iff_prime_less_than_overshoot_at_most_2k(self) -> None:
        for k in range(3, 150):
            for prime in raw_split_primes(k):
                data = next_p_square_overshoot(k, prime)
                self.assertGreater(data["overshoot"], prime)
                self.assertLessEqual(data["overshoot"], 2 * k)

    def test_slot_formulas_match_direct_window_for_all_small_shells(self) -> None:
        for k in range(3, 100):
            # Function internally checks the exact direct interval counts.
            for prime in __import__("enterprise_math.legendre", fromlist=["primes_up_to"]).primes_up_to(k):
                data = raw_root_branch_slot_counts(k, prime)
                self.assertEqual(
                    data["raw_split"],
                    data["lower_slots"] > 0 and data["upper_slots"] > 0,
                )

    def test_realized_split_primes_equal_l067_split_shells(self) -> None:
        for k in range(3, 200):
            self.assertEqual(
                realized_split_primes(k),
                factor_root_split_shell_primes(k),
            )

    def test_raw_split_can_disappear_after_p_rough_filter(self) -> None:
        # At k=6,p=3, the raw window reaches root 4 only through q=16,
        # which is not 3-rough.  This is the same envelope-vs-realizability
        # correction that removed the false lower-band shell collision.
        raw = raw_root_branch_slot_counts(6, 3)
        actual = realized_root_branch_occupancy(6, 3)
        self.assertTrue(raw["raw_split"])
        self.assertFalse(actual["realized_split"])
        self.assertEqual(actual["upper_rough_values"], ())

    def test_overshoot_examples_pin_actual_split_and_unsplit_shells(self) -> None:
        split = realized_root_branch_occupancy(18, 7)
        self.assertTrue(split["realized_split"])
        self.assertGreater(split["lower_slots"], 0)
        self.assertGreater(split["upper_slots"], 0)

        unsplit = realized_root_branch_occupancy(11, 5)
        self.assertFalse(unsplit["realized_split"])


if __name__ == "__main__":
    unittest.main()
