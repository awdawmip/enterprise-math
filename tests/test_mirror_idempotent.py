import unittest

from enterprise_math.mirror import anchor_pair_survival, mirror_support_separation
from enterprise_math.mirror_idempotent import (
    bounded_idempotent_lifts,
    bounded_lift_capacity,
    mirror_idempotent,
    mirror_pairwise_coprime,
)


class MirrorIdempotentTests(unittest.TestCase):
    def test_surviving_mirror_triple_is_pairwise_coprime(self):
        for k in range(3, 100):
            for r in range(1, k):
                if not anchor_pair_survival(k, r)["survives"]:
                    continue
                data = mirror_pairwise_coprime(k, r)
                self.assertEqual(data["center_radius_gcd"], 1)
                self.assertEqual(data["lower_center_gcd"], 1)
                self.assertEqual(data["upper_center_gcd"], 1)
                self.assertEqual(data["lower_upper_gcd"], 1)

    def test_idempotent_recovers_two_sided_support_partition(self):
        saw = False
        for k in range(3, 100):
            for r in range(1, k):
                if not anchor_pair_survival(k, r)["survives"]:
                    continue
                supports = mirror_support_separation(k, r)
                if not supports["lower_support"] or not supports["upper_support"]:
                    continue
                data = mirror_idempotent(k, r)
                modulus = data["modulus"]
                e = data["idempotent"]
                u = data["involution"]
                self.assertEqual((e * e - e) % modulus, 0)
                self.assertEqual((u * u - 1) % modulus, 0)
                self.assertNotIn(e, (0, 1))
                self.assertEqual(
                    data["lower_product"] * data["upper_product"], modulus
                )
                saw = True
        self.assertTrue(saw)

    def test_original_radius_is_a_bounded_idempotent_lift(self):
        data = mirror_idempotent(20, 17)
        lifts = bounded_idempotent_lifts(
            20, data["support"], data["idempotent"], True
        )
        self.assertEqual(lifts, [17])
        capacity = bounded_lift_capacity(
            20, data["support"], data["idempotent"]
        )
        self.assertEqual(capacity["surviving_capacity"], 1)
        self.assertEqual(capacity["unfiltered_capacity"], 1)
        self.assertGreater(capacity["modulus"], 19)

    def test_every_observed_partition_contains_its_radius_among_lifts(self):
        saw_multiple_capacity = False
        for k in range(5, 80):
            for r in range(1, k):
                if not anchor_pair_survival(k, r)["survives"]:
                    continue
                supports = mirror_support_separation(k, r)
                if not supports["lower_support"] or not supports["upper_support"]:
                    continue
                data = mirror_idempotent(k, r)
                lifts = bounded_idempotent_lifts(
                    k, data["support"], data["idempotent"], True
                )
                self.assertIn(r, lifts)
                capacity = bounded_lift_capacity(
                    k, data["support"], data["idempotent"]
                )
                self.assertEqual(capacity["surviving_capacity"], len(lifts))
                self.assertLessEqual(
                    capacity["surviving_capacity"],
                    capacity["unfiltered_capacity"],
                )
                if capacity["unfiltered_capacity"] > 1:
                    saw_multiple_capacity = True
        self.assertTrue(saw_multiple_capacity)


if __name__ == "__main__":
    unittest.main()
