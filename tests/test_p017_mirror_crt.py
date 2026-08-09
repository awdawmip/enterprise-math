import unittest

from enterprise_math.p017_mirror import (
    anchor_surviving_radius,
    mirror_transverse_supports,
)
from enterprise_math.p017_mirror_crt import (
    bounded_sign_pattern_lifts,
    exact_support_lifts,
    observed_mirror_full_core_idempotent,
    observed_mirror_idempotent,
    sign_pattern_capacity,
)


class P017MirrorCRTTests(unittest.TestCase):
    def test_observed_two_sided_support_gives_nontrivial_idempotent(self):
        saw = False
        for k in range(5, 70):
            for r in range(1, k):
                if not anchor_surviving_radius(k, r):
                    continue
                lower_support, upper_support = mirror_transverse_supports(k, r)
                if not lower_support or not upper_support:
                    continue
                data = observed_mirror_idempotent(k, r)
                modulus = data["modulus"]
                e = data["idempotent"]
                u = data["involution"]
                self.assertEqual((u * u - 1) % modulus, 0)
                self.assertEqual((e * e - e) % modulus, 0)
                self.assertNotIn(e, (0, 1))
                self.assertEqual(
                    data["lower_product"] * data["upper_product"], modulus
                )
                saw = True
        self.assertTrue(saw)

    def test_observed_radius_belongs_to_its_sign_pattern_progression(self):
        for k in range(5, 70):
            for r in range(1, k):
                if not anchor_surviving_radius(k, r):
                    continue
                lower_support, upper_support = mirror_transverse_supports(k, r)
                if not lower_support or not upper_support:
                    continue
                data = observed_mirror_idempotent(k, r)
                lifts = bounded_sign_pattern_lifts(
                    k,
                    data["support"],
                    data["idempotent"],
                    require_anchor_survival=True,
                )
                self.assertIn(r, lifts)

    def test_capacity_chain_and_d_ge_k_uniqueness(self):
        saw_large_modulus = False
        for k in range(5, 75):
            for r in range(1, k):
                if not anchor_surviving_radius(k, r):
                    continue
                lower_support, upper_support = mirror_transverse_supports(k, r)
                if not lower_support or not upper_support:
                    continue
                data = observed_mirror_idempotent(k, r)
                cap = sign_pattern_capacity(k, data["support"], data["idempotent"])
                self.assertLessEqual(cap["exact_capacity"], cap["anchor_capacity"])
                self.assertLessEqual(cap["anchor_capacity"], cap["sign_capacity"])
                self.assertIn(r, cap["exact_lifts"])
                if cap["modulus"] >= k:
                    saw_large_modulus = True
                    self.assertLessEqual(cap["sign_capacity"], 1)
        self.assertTrue(saw_large_modulus)

    def test_strict_exact_support_capacity_example(self):
        cap = sign_pattern_capacity(46, [3, 5], 6)
        self.assertEqual(cap["modulus"], 15)
        self.assertEqual(cap["anchor_lifts"], [7, 37])
        self.assertEqual(cap["exact_lifts"], [7])
        self.assertEqual(cap["anchor_capacity"], 2)
        self.assertEqual(cap["exact_capacity"], 1)

        self.assertEqual(mirror_transverse_supports(46, 7), ([5], [3]))
        self.assertEqual(mirror_transverse_supports(46, 37), ([5, 17], [3]))

    def test_k20_observed_pattern_has_unique_bounded_lift(self):
        data = observed_mirror_idempotent(20, 17)
        cap = sign_pattern_capacity(20, data["support"], data["idempotent"])
        self.assertGreaterEqual(cap["modulus"], 20)
        self.assertEqual(cap["sign_lifts"], [17])
        self.assertEqual(cap["exact_lifts"], [17])

    def test_full_core_idempotent_recovers_prime_power_cores(self):
        data = observed_mirror_full_core_idempotent(16, 7)
        self.assertEqual(data["lower_core"], 5)
        self.assertEqual(data["upper_core"], 9)
        self.assertEqual(data["lower_tail"], 53)
        self.assertEqual(data["upper_tail"], 31)
        self.assertEqual(data["modulus"], 45)
        self.assertEqual(data["squarefree_modulus"], 15)
        self.assertEqual(data["idempotent"] * data["idempotent"] % 45, data["idempotent"])
        self.assertIn(7, data["full_core_lifts"])
        self.assertLessEqual(
            data["full_core_capacity"], data["squarefree_sign_capacity"]
        )

    def test_full_core_capacity_never_exceeds_squarefree_capacity(self):
        saw = False
        saw_large_modulus = False
        for k in range(5, 100):
            for r in range(1, k):
                if not anchor_surviving_radius(k, r):
                    continue
                lower_support, upper_support = mirror_transverse_supports(k, r)
                if not lower_support or not upper_support:
                    continue
                data = observed_mirror_full_core_idempotent(k, r)
                self.assertGreaterEqual(data["modulus"], data["squarefree_modulus"])
                self.assertEqual(data["modulus"] % data["squarefree_modulus"], 0)
                self.assertTrue(
                    set(data["full_core_lifts"]).issubset(
                        data["squarefree_sign_lifts"]
                    )
                )
                self.assertLessEqual(
                    data["full_core_capacity"], data["squarefree_sign_capacity"]
                )
                if data["modulus"] >= k:
                    saw_large_modulus = True
                    self.assertLessEqual(data["full_core_capacity"], 1)
                saw = True
        self.assertTrue(saw)
        self.assertTrue(saw_large_modulus)

    def test_full_core_capacity_can_be_strictly_stronger(self):
        # k=31,r=7 gives 985=5*197 and 999=3^3*37.
        # Squarefree D=15 permits radii 7 and 22, while full S=135 permits only 7.
        data = observed_mirror_full_core_idempotent(31, 7)
        self.assertEqual(data["lower_core"], 5)
        self.assertEqual(data["upper_core"], 27)
        self.assertEqual(data["modulus"], 135)
        self.assertEqual(data["squarefree_modulus"], 15)
        self.assertEqual(data["squarefree_sign_lifts"], [7, 22])
        self.assertEqual(data["full_core_lifts"], [7])
        self.assertEqual(data["squarefree_sign_capacity"], 2)
        self.assertEqual(data["full_core_capacity"], 1)

    def test_invalid_patterns_are_rejected(self):
        with self.assertRaises(ValueError):
            sign_pattern_capacity(20, [2, 13], 1)
        with self.assertRaises(ValueError):
            sign_pattern_capacity(20, [13, 13], 1)
        with self.assertRaises(ValueError):
            sign_pattern_capacity(20, [13, 19], 0)
        with self.assertRaises(ValueError):
            exact_support_lifts(20, [13, 19], 1)


if __name__ == "__main__":
    unittest.main()
