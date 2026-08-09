import unittest

from enterprise_math.p017_mirror import (
    anchor_surviving_radius,
    mirror_transverse_supports,
)
from enterprise_math.p017_mirror_crt import (
    bounded_sign_pattern_lifts,
    exact_support_lifts,
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

    def test_invalid_patterns_are_rejected(self):
        # 2 is an anchor prime for every k>=2 and cannot enter transverse D.
        with self.assertRaises(ValueError):
            sign_pattern_capacity(20, [2, 13], 1)
        with self.assertRaises(ValueError):
            sign_pattern_capacity(20, [13, 13], 1)
        # e=0 or 1 is trivial and does not encode two nonempty sides.
        with self.assertRaises(ValueError):
            sign_pattern_capacity(20, [13, 19], 0)
        with self.assertRaises(ValueError):
            exact_support_lifts(20, [13, 19], 1)


if __name__ == "__main__":
    unittest.main()
