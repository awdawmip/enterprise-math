import unittest

from enterprise_math.core import integer_nth_root
from enterprise_math.p017_mirror_product_bridge import (
    fixed_product_channel,
    joint_product_root,
)
from enterprise_math.p017_mirror_product_criticality import (
    power_product_candidate_window,
    unbounded_power_collision_family,
)


class P017MirrorProductCriticalityTests(unittest.TestCase):
    def test_every_valid_product_label_lies_in_universal_window(self):
        for degree in range(2, 7):
            for k in range(6, 55):
                for product in range(1, k, 2):
                    channel = fixed_product_channel(k, product)
                    for radius in channel["radii"]:
                        quotient = joint_product_root(k, radius, product)["joint_quotient"]
                        observed = integer_nth_root(quotient, degree)
                        window = power_product_candidate_window(k, observed, degree)
                        self.assertIn(product, window["odd_candidates"])

    def test_cubic_universal_window_stays_at_two_candidates_in_relevant_scale(self):
        for k in range(4, 180):
            # Every valid S<k observation has quotient > k^3 and therefore
            # cubic root >= k.  Checking the full relevant root interval avoids
            # depending on actual divisibility incidence density.
            center = k * (k + 1)
            lower_q = (center * center - (k - 1) * (k - 1)) // (k - 1)
            upper_q = center * center - 1
            first = integer_nth_root(lower_q, 3)
            last = integer_nth_root(upper_q, 3)
            for observed in range(max(k, first), last + 1):
                window = power_product_candidate_window(k, observed, 3)
                self.assertLessEqual(window["candidate_count"], 2)
                if window["candidate_count"] == 2:
                    left, right = window["odd_candidates"]
                    self.assertEqual(right - left, 2)

    def test_degree_four_and_above_have_unbounded_explicit_fibers(self):
        for degree in range(4, 8):
            previous = 0
            for scale in range(2, 11):
                data = unbounded_power_collision_family(degree, scale)
                self.assertEqual(data["common_root"], scale**3)
                self.assertEqual(data["label_count"], scale // 2)
                self.assertEqual(data["expected_label_count"], scale // 2)
                self.assertGreaterEqual(data["label_count"], previous)
                previous = data["label_count"]
                for entry in data["entries"]:
                    self.assertEqual(entry["root"], scale**3)
                    self.assertEqual(entry["product_label"] % 2, 1)
                    self.assertLess(entry["radius"], data["k"])

    def test_quartic_family_matches_visible_growth(self):
        data = unbounded_power_collision_family(4, 10)
        self.assertEqual(data["k"], 10**4)
        self.assertEqual(data["common_root"], 1000)
        self.assertEqual(data["label_count"], 5)
        self.assertEqual(
            tuple(entry["product_label"] for entry in data["entries"]),
            (9999, 9997, 9995, 9993, 9991),
        )


if __name__ == "__main__":
    unittest.main()
