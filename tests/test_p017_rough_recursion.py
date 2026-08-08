import unittest

from enterprise_math.factor_precision import first_factor_shell
from enterprise_math.legendre import primes_up_to
from enterprise_math.p017_cofactor_window import (
    centered_cofactor_window,
    cofactor_window_shell,
    omega_with_multiplicity,
)
from enterprise_math.p017_rough_recursion import (
    high_least_factor_band,
    p017_shell_rough_partition,
    raw_child_window,
    rough_interval_least_factor_partition,
    rough_interval_values,
    semiprime_only_band,
)


class P017RoughRecursionTests(unittest.TestCase):
    def test_generic_rough_interval_partition_is_exact(self):
        for lower in range(2, 35, 4):
            for upper in range(lower, lower + 45, 7):
                for threshold in (2, 3, 5, 7):
                    data = rough_interval_least_factor_partition(lower, upper, threshold)
                    self.assertEqual(
                        data["values"],
                        rough_interval_values(lower, upper, threshold),
                    )
                    rebuilt = list(data["primes"])
                    for ell, children in data["branches"].items():
                        rebuilt.extend(ell * child for child in children)
                    self.assertEqual(sorted(rebuilt), data["values"])

    def test_child_multiple_count_is_exact_quotient_response(self):
        saw_carry = False
        saw_no_carry = False
        for lower in range(2, 60, 5):
            for length in range(1, 35, 3):
                upper = lower + length - 1
                for prime in (2, 3, 5, 7, 11):
                    data = raw_child_window(lower, upper, prime)
                    exact = sum(1 for value in range(lower, upper + 1) if value % prime == 0)
                    self.assertEqual(data["multiple_count"], exact)
                    self.assertEqual(
                        data["multiple_count"],
                        data["transport_bulk"] + data["transport_carry"],
                    )
                    self.assertLessEqual(data["child_count"], data["ceiling_bound"])
                    saw_carry |= data["transport_carry"] == 1
                    saw_no_carry |= data["transport_carry"] == 0
        self.assertTrue(saw_carry)
        self.assertTrue(saw_no_carry)

    def test_p017_window_buchstab_partition_reconstructs_shell(self):
        for k in range(3, 55):
            for p in primes_up_to(k):
                data = p017_shell_rough_partition(k, p)
                self.assertEqual(
                    [p * q for q in data["values"]],
                    first_factor_shell(k, p),
                )
                self.assertEqual(cofactor_window_shell(k, p), first_factor_shell(k, p))

    def test_high_band_parent_length_is_at_most_p(self):
        saw = False
        for k in range(2, 90):
            for p in primes_up_to(k):
                if p * p < 2 * k:
                    continue
                data = high_least_factor_band(k, p)
                self.assertLessEqual(data["parent_length"], p)
                self.assertTrue(all(count <= 1 for count in data["branch_raw_counts"].values()))
                saw = True
        self.assertTrue(saw)

    def test_high_band_is_semiprime_or_three_prime_only(self):
        saw_semiprime = False
        saw_triple = False
        for k in range(3, 100):
            for p in primes_up_to(k):
                if p * p < 2 * k:
                    continue
                data = high_least_factor_band(k, p)
                self.assertEqual(
                    sorted(data["semiprime_states"] + data["triple_prime_states"]),
                    data["shell"],
                )
                for n in data["semiprime_states"]:
                    self.assertEqual(omega_with_multiplicity(n), 2)
                    saw_semiprime = True
                for n in data["triple_prime_states"]:
                    self.assertEqual(omega_with_multiplicity(n), 3)
                    saw_triple = True
                self.assertEqual(
                    len(data["triple_prime_states"]),
                    len(data["triple_by_second_prime"]),
                )
        self.assertTrue(saw_semiprime)
        self.assertTrue(saw_triple)

    def test_semiprime_only_root_band(self):
        saw = False
        for k in range(3, 100):
            upper = (k + 1) * (k + 1) - 1
            for p in primes_up_to(k):
                if p**3 <= upper:
                    continue
                data = semiprime_only_band(k, p)
                for n in data["shell"]:
                    self.assertEqual(omega_with_multiplicity(n), 2)
                    saw = True
        self.assertTrue(saw)

    def test_high_band_contains_exact_parent_window_geometry(self):
        for k in range(5, 70):
            for p in primes_up_to(k):
                if p * p < 2 * k:
                    continue
                expected = centered_cofactor_window(k, p)
                data = high_least_factor_band(k, p)
                self.assertEqual(data["q_min"], expected["q_min"])
                self.assertEqual(data["q_max"], expected["q_max"])
                self.assertEqual(data["raw_count"], expected["raw_count"])


if __name__ == "__main__":
    unittest.main()
