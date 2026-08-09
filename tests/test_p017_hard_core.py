import unittest

from enterprise_math.legendre import primes_up_to
from enterprise_math.p017_hard_core import (
    anchor_parity_full_core_capacity,
    finite_odd_wheel_admissibility,
    full_core_affine_orbit,
    generic_ternary_wheel_capacity,
    hard_core_local_sieve_signature,
    residual_generic_ternary_multi_lift_tail_gap,
    residual_hard_core_tail_gap,
    residual_multi_lift_tail_gap,
)
from enterprise_math.p017_mirror import anchor_surviving_radius, mirror_pair
from enterprise_math.p017_cofactor_window import square_basin_smooth_tail


class P017HardCoreTests(unittest.TestCase):
    def test_anchor_parity_doubles_effective_full_core_modulus(self):
        # k=28,r=23 has S_-=3, S_+=5, S=15.
        # Raw L053 lifts mod 15 are [8,23]; anchor-forced odd parity keeps only 23.
        data = anchor_parity_full_core_capacity(28, 23)
        self.assertEqual(data["modulus"], 15)
        self.assertEqual(data["raw_full_core_lifts"], [8, 23])
        self.assertEqual(data["parity_full_core_lifts"], [23])
        self.assertEqual(data["anchor_full_core_lifts"], [23])
        self.assertEqual(data["parity_modulus"], 30)
        self.assertEqual(data["parity_capacity"], 1)

    def test_2s_ge_k_forces_at_most_one_parity_lift(self):
        saw = False
        for k in range(5, 180):
            for r in range(1, k):
                if not anchor_surviving_radius(k, r):
                    continue
                lower, upper = mirror_pair(k, r)
                lower_data = square_basin_smooth_tail(k, lower)
                upper_data = square_basin_smooth_tail(k, upper)
                if bool(lower_data["is_prime"]) or bool(upper_data["is_prime"]):
                    continue
                data = anchor_parity_full_core_capacity(k, r)
                if 2 * int(data["modulus"]) >= k:
                    self.assertLessEqual(data["parity_capacity"], 1)
                    saw = True
        self.assertTrue(saw)

    def test_affine_cell_transport_and_resultant(self):
        data = full_core_affine_orbit(52, 23)
        self.assertEqual((data["lower_core"], data["upper_core"]), (3, 7))
        self.assertEqual(data["core_product"], 21)
        self.assertEqual(data["step_radius"], 42)
        self.assertEqual(data["step_lower_tail"], -14)
        self.assertEqual(data["step_upper_tail"], 6)
        self.assertEqual(data["linear_resultant"], 4 * 52 * 53)
        self.assertTrue(any(point["radius"] == 23 for point in data["orbit"]))
        for point in data["orbit"]:
            self.assertEqual(
                data["lower_core"] * point["lower_tail_form"]
                + data["upper_core"] * point["upper_tail_form"],
                2 * data["center"],
            )

    def test_local_sieve_signature_is_one_or_two(self):
        # k=52,r=23 has M=52*53 and S=3*7.
        # p=3,7 divide S; p=13 divides M; p=5,11 are generic.
        expected = {3: 1, 5: 2, 7: 1, 11: 2, 13: 1}
        for prime, forbidden_count in expected.items():
            data = hard_core_local_sieve_signature(52, 23, prime)
            self.assertEqual(data["forbidden_count"], forbidden_count)
            self.assertEqual(
                data["allowed_count"],
                prime - forbidden_count,
            )
            self.assertGreater(data["allowed_count"], 0)

    def test_dense_local_signature_matches_divisibility_formula(self):
        saw_generic = False
        saw_degenerate = False
        for k, r in ((22, 5), (28, 23), (52, 23)):
            hard = residual_hard_core_tail_gap(k, r)
            ms = hard["center"] * hard["core_product"]
            for prime in primes_up_to(k):
                if prime == 2:
                    continue
                data = hard_core_local_sieve_signature(k, r, prime)
                expected = 1 if ms % prime == 0 else 2
                self.assertEqual(data["forbidden_count"], expected)
                saw_degenerate |= expected == 1
                saw_generic |= expected == 2
        self.assertTrue(saw_generic)
        self.assertTrue(saw_degenerate)

    def test_every_finite_odd_wheel_remains_locally_admissible(self):
        data = finite_odd_wheel_admissibility(52, 23, (3, 5, 7, 11, 13))
        expected = 1
        for signature in data["local_signatures"]:
            expected *= signature["allowed_count"]
        self.assertEqual(data["allowed_class_count"], expected)
        self.assertGreater(data["allowed_class_count"], 0)
        self.assertEqual(data["wheel_modulus"], 3 * 5 * 7 * 11 * 13)

    def test_generic_mod3_collapses_lift_index_to_one_class(self):
        # k=631,r=93 has cores 7 and 5, S=35, and 3 does not divide M*S.
        # The parity cell is mod 70; mod-3 tail avoidance upgrades it to mod 210.
        data = generic_ternary_wheel_capacity(631, 93)
        self.assertEqual((data["lower_core"], data["upper_core"]), (7, 5))
        self.assertEqual(data["core_product"], 35)
        self.assertEqual(data["ternary_step_radius"], 210)
        self.assertEqual(data["ternary_capacity"], 3)
        self.assertEqual(
            [point["radius"] for point in data["ternary_safe_lifts"]],
            [93, 303, 513],
        )
        prime_points = [
            point["radius"]
            for point in data["ternary_safe_lifts"]
            if point["both_tail_forms_prime"] and point["anchor_survives"]
        ]
        self.assertEqual(prime_points, [93, 513])

    def test_known_hard_core_witnesses(self):
        data = residual_hard_core_tail_gap(22, 5)
        self.assertEqual((data["lower_core"], data["upper_core"]), (3, 7))
        self.assertEqual((data["lower_tail"], data["upper_tail"]), (167, 73))
        self.assertEqual(data["tail_gap"], 94)
        self.assertGreaterEqual(data["tail_gap"], data["parity_lower_bound"])

        data = residual_hard_core_tail_gap(28, 23)
        self.assertEqual((data["lower_core"], data["upper_core"]), (3, 5))
        self.assertEqual((data["lower_tail"], data["upper_tail"]), (263, 167))
        self.assertEqual(data["tail_gap"], 96)

    def test_dense_residual_hard_core_scan(self):
        saw = False
        saw_multi = False
        for k in range(5, 220):
            for r in range(1, k):
                if not anchor_surviving_radius(k, r):
                    continue
                lower, upper = mirror_pair(k, r)
                lower_data = square_basin_smooth_tail(k, lower)
                upper_data = square_basin_smooth_tail(k, upper)
                if bool(lower_data["is_prime"]) or bool(upper_data["is_prime"]):
                    continue
                a = int(lower_data["smooth_core"])
                b = int(upper_data["smooth_core"])
                if a * b >= k:
                    continue
                data = residual_hard_core_tail_gap(k, r)
                self.assertLess(data["core_product"], k)
                self.assertGreater(data["lower_tail"], k)
                self.assertGreater(data["upper_tail"], k)
                self.assertGreater(data["tail_gap"], k + 5)
                self.assertGreaterEqual(data["tail_gap"], data["parity_lower_bound"])
                self.assertEqual(data["tail_gap"] % 2, 0)
                saw = True

                if 2 * a * b < k:
                    multi = residual_multi_lift_tail_gap(k, r)
                    self.assertGreater(multi["tail_gap"], 3 * k + 9)
                    self.assertGreaterEqual(
                        multi["tail_gap"], multi["multi_lift_parity_lower_bound"]
                    )
                    saw_multi = True
        self.assertTrue(saw)
        self.assertTrue(saw_multi)

    def test_multi_lift_witness(self):
        data = residual_multi_lift_tail_gap(52, 23)
        self.assertEqual((data["lower_core"], data["upper_core"]), (3, 7))
        self.assertEqual(data["core_product"], 21)
        self.assertLess(2 * data["core_product"], 52)
        self.assertEqual((data["lower_tail"], data["upper_tail"]), (911, 397))
        self.assertEqual(data["tail_gap"], 514)
        self.assertGreater(data["tail_gap"], 3 * 52 + 9)

    def test_generic_ternary_multi_lift_gap(self):
        for r in (93, 513):
            data = residual_generic_ternary_multi_lift_tail_gap(631, r)
            self.assertEqual(data["core_product"], 35)
            self.assertLess(6 * data["core_product"], 631)
            self.assertGreater(data["tail_gap"], 11 * 631 + 25)
            self.assertGreaterEqual(
                data["tail_gap"], data["generic_ternary_parity_lower_bound"]
            )

    def test_rejects_nonhard_cases(self):
        with self.assertRaises(ValueError):
            residual_hard_core_tail_gap(31, 7)  # full-core product 135 >= 31
        with self.assertRaises(ValueError):
            residual_hard_core_tail_gap(10, 2)  # not anchor-surviving
        with self.assertRaises(ValueError):
            residual_multi_lift_tail_gap(28, 23)  # 2*15 >= 28
        with self.assertRaises(ValueError):
            generic_ternary_wheel_capacity(52, 23)  # 3 divides S=21
        with self.assertRaises(ValueError):
            residual_generic_ternary_multi_lift_tail_gap(52, 23)


if __name__ == "__main__":
    unittest.main()
