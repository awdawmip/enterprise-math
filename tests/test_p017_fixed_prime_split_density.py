import unittest

from enterprise_math.p017_fixed_prime_split_density import (
    actual_fixed_prime_split,
    fixed_prime_split_count,
    integer_beatty_core,
    split_failure_localization,
)
from enterprise_math.p017_root_split_overshoot import raw_root_branch_slot_counts


class P017FixedPrimeSplitDensityTests(unittest.TestCase):
    def test_beatty_core_is_exactly_the_raw_upper_boundary_condition(self) -> None:
        for prime in (2, 3, 5, 7, 11):
            for k in range(max(3, prime), 250):
                raw = raw_root_branch_slot_counts(k, prime)
                self.assertEqual(
                    integer_beatty_core(k, prime),
                    int(raw["overshoot"]) <= 2 * k,
                )

    def test_actual_failures_inside_beatty_core_are_primorial_localized(self) -> None:
        for prime in (2, 3, 5, 7, 11):
            for k in range(max(3, prime), 300):
                data = split_failure_localization(k, prime)
                self.assertTrue(data["failure_localized"])

    def test_fixed_prime_split_counts_pin_density_regression(self) -> None:
        # Finite audits only; the density theorem is proved by Beatty density plus
        # equidistribution and the shrinking boundary-layer argument.
        expected = {2: 3532, 3: 2875, 5: 2217, 7: 1870, 11: 1485}
        for prime, count in expected.items():
            self.assertEqual(fixed_prime_split_count(prime, 5000), count)

    def test_p2_actual_split_equals_raw_split(self) -> None:
        for k in range(3, 500):
            raw = bool(raw_root_branch_slot_counts(k, 2)["raw_split"])
            self.assertEqual(actual_fixed_prime_split(k, 2), raw)


if __name__ == "__main__":
    unittest.main()
