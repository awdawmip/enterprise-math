import unittest

from enterprise_math.factor_precision import first_factor_shell, square_basin
from enterprise_math.legendre import is_prime, primes_up_to
from enterprise_math.p017_cofactor_window import (
    centered_cofactor_window,
    cofactor_square_offsets,
    cofactor_window_shell,
    cofactor_window_survivors,
    is_p_rough,
    near_diagonal_prime_degeneracy,
    omega_with_multiplicity,
    root_depth_shell_bound,
    square_basin_smooth_tail,
)


class P017CofactorWindowTests(unittest.TestCase):
    def test_exact_window_reconstructs_every_bounded_first_factor_shell(self):
        for k in range(2, 85):
            for p in primes_up_to(k):
                self.assertEqual(cofactor_window_shell(k, p), first_factor_shell(k, p))

    def test_every_shell_cofactor_lies_in_window_and_is_p_rough(self):
        for k in range(2, 70):
            for p in primes_up_to(k):
                data = centered_cofactor_window(k, p)
                for n in first_factor_shell(k, p):
                    q = n // p
                    self.assertLessEqual(data["q_min"], q)
                    self.assertLessEqual(q, data["q_max"])
                    self.assertTrue(is_p_rough(q, p))
                    offsets = cofactor_square_offsets(k, p, q)
                    self.assertGreater(offsets["lower_offset"], 0)
                    self.assertGreater(offsets["upper_offset"], 0)

    def test_raw_width_is_bulk_plus_single_boundary_carry(self):
        saw_carry = False
        saw_no_carry = False
        for k in range(2, 120):
            for p in primes_up_to(k):
                data = centered_cofactor_window(k, p)
                self.assertEqual(
                    data["raw_count"],
                    2 + data["transport_bulk"] + data["transport_carry"],
                )
                self.assertIn(data["transport_carry"], (0, 1))
                saw_carry |= data["transport_carry"] == 1
                saw_no_carry |= data["transport_carry"] == 0
        self.assertTrue(saw_carry)
        self.assertTrue(saw_no_carry)

    def test_two_or_three_candidate_regime(self):
        saw_two = False
        saw_three = False
        for k in range(3, 180):
            for p in primes_up_to(k):
                data = centered_cofactor_window(k, p)
                r = data["radius"]
                if p > 2 * (r - 1):
                    self.assertIn(data["raw_count"], (2, 3))
                    saw_two |= data["raw_count"] == 2
                    saw_three |= data["raw_count"] == 3
        self.assertTrue(saw_two)
        self.assertTrue(saw_three)

    def test_near_diagonal_prime_pair_is_only_a_degenerate_case(self):
        saw_nonempty = False
        saw_empty = False
        for k in range(4, 500):
            for p in primes_up_to(k):
                r = k + 1 - p
                if p >= 3 and p > r * r:
                    data = near_diagonal_prime_degeneracy(k, p)
                    expected_q = k + 1 + r
                    self.assertEqual(data["raw_count"], 2)
                    self.assertEqual(data["symmetric_q"], expected_q)
                    self.assertEqual(bool(data["shell"]), is_prime(expected_q))
                    saw_nonempty |= bool(data["shell"])
                    saw_empty |= not data["shell"]
        self.assertTrue(saw_nonempty)
        self.assertTrue(saw_empty)

    def test_k10_boundary_case_is_three_candidate_window(self):
        data = centered_cofactor_window(10, 7)
        self.assertEqual((data["q_min"], data["q_max"]), (15, 17))
        self.assertEqual(data["raw_count"], 3)
        self.assertEqual(cofactor_window_survivors(10, 7), [17])
        self.assertEqual(cofactor_window_shell(10, 7), [119])

    def test_root_depth_bound(self):
        saw_nontrivial = False
        for k in range(3, 100):
            for p in primes_up_to(k):
                for m in range(1, 5):
                    data = root_depth_shell_bound(k, p, m)
                    if data["condition"] and data["observed_max_omega"]:
                        self.assertLessEqual(data["observed_max_omega"], m)
                        saw_nontrivial = True
        self.assertTrue(saw_nontrivial)

    def test_omega_examples(self):
        self.assertEqual(omega_with_multiplicity(2), 1)
        self.assertEqual(omega_with_multiplicity(12), 3)
        self.assertEqual(omega_with_multiplicity(72), 5)
        self.assertEqual(omega_with_multiplicity(97), 1)

    def test_square_basin_smooth_tail_dichotomy(self):
        saw_tail_one = False
        saw_large_prime_tail = False
        for k in range(2, 70):
            for n in square_basin(k):
                data = square_basin_smooth_tail(k, n)
                tail = data["tail"]
                if tail == 1:
                    saw_tail_one = True
                else:
                    saw_large_prime_tail = True
                    self.assertGreater(tail, k)
                    self.assertTrue(is_prime(tail))
                self.assertEqual(data["smooth_core"] == 1, is_prime(n))
        self.assertTrue(saw_tail_one)
        self.assertTrue(saw_large_prime_tail)


if __name__ == "__main__":
    unittest.main()
