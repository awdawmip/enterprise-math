import unittest

from enterprise_math.p017_split_repair_mass_uniformity import (
    beatty_core_index,
    dyadic_actual_split_mass,
    fixed_prime_dyadic_counts,
    split_branch_data,
)
from enterprise_math.legendre import primes_up_to


class P017SplitRepairMassUniformityTests(unittest.TestCase):
    def test_branch_slot_formulas_and_beatty_equivalence(self) -> None:
        for k in range(3, 80):
            for prime in primes_up_to(k):
                data = split_branch_data(k, prime)
                self.assertEqual(
                    data["raw_split"],
                    data["lower_slots"] > 0 and data["upper_slots"] > 0,
                )
                self.assertEqual(
                    data["upper_slots"] > 0,
                    beatty_core_index(data["multiplier"], prime) == k,
                )
                self.assertFalse(data["actual_split"] and not data["raw_split"])

    def test_fixed_prime_dyadic_counts_pin_realizability_loss(self) -> None:
        p3 = fixed_prime_dyadic_counts(100, 3)
        self.assertEqual(
            (p3["beatty_count"], p3["raw_split_count"], p3["actual_split_count"]),
            (58, 57, 57),
        )

        p13 = fixed_prime_dyadic_counts(100, 13)
        self.assertEqual(
            (p13["beatty_count"], p13["raw_split_count"], p13["actual_split_count"]),
            (27, 25, 21),
        )
        self.assertEqual(p13["realizability_failures"], 4)

    def test_dyadic_mass_is_exact_sum_of_fixed_prime_counts(self) -> None:
        data = dyadic_actual_split_mass(100, 13)
        self.assertEqual(data["total_actual_split_mass"], 246)
        self.assertEqual(
            {
                prime: row["actual_split_count"]
                for prime, row in data["by_prime"].items()
            },
            {2: 70, 3: 57, 5: 41, 7: 33, 11: 24, 13: 21},
        )

    def test_actual_splits_are_a_subset_of_raw_splits(self) -> None:
        for prime in primes_up_to(29):
            row = fixed_prime_dyadic_counts(100, prime)
            self.assertTrue(set(row["actual_splits"]).issubset(row["raw_splits"]))


if __name__ == "__main__":
    unittest.main()
