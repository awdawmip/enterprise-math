import unittest

from enterprise_math.p017_lower_band import (
    lower_band_base_root,
    lower_band_candidate_roots,
    lower_band_primes,
    lower_band_root_channels,
    lower_band_root_disjoint_bound,
    lower_band_root_overlap_bound,
)


class P017LowerBandTests(unittest.TestCase):
    def test_lower_band_definition(self):
        for k in range(2, 200):
            for p in lower_band_primes(k):
                self.assertLess(p * p, 2 * k)
                base = lower_band_base_root(k, p)
                self.assertEqual(lower_band_candidate_roots(k, p), (base, base + 1))

    def test_every_target_root_has_at_most_two_shells(self):
        saw_double = False
        for k in range(2, 600):
            data = lower_band_root_overlap_bound(k)
            self.assertLessEqual(data["max_multiplicity"], 2)
            channels = lower_band_root_channels(k)
            for primes in channels.values():
                self.assertLessEqual(len(primes), 2)
                saw_double |= len(primes) == 2
        self.assertTrue(saw_double)

    def test_three_shell_endpoint_separation_on_larger_roots(self):
        for k in (1000, 5000, 10000, 50000, 100000, 200000):
            data = lower_band_root_overlap_bound(k)
            primes = data["lower_band_primes"]
            roots = data["base_roots"]
            for i in range(len(primes) - 2):
                for j in range(i + 2, len(primes)):
                    self.assertGreaterEqual(roots[primes[i]], roots[primes[j]] + 2)
            self.assertLessEqual(data["max_multiplicity"], 2)

    def test_stable_range_candidate_pairs_are_disjoint(self):
        for k in range(15, 1000):
            data = lower_band_root_disjoint_bound(k)
            self.assertLessEqual(data["max_multiplicity"], 1)
            primes = data["lower_band_primes"]
            roots = data["base_roots"]
            for i, p in enumerate(primes):
                for q in primes[i + 1 :]:
                    self.assertGreaterEqual(roots[p], roots[q] + 2)

    def test_stable_disjointness_on_large_roots(self):
        for k in (5000, 10000, 50000, 100000, 200000):
            data = lower_band_root_disjoint_bound(k)
            self.assertLessEqual(data["max_multiplicity"], 1)

    def test_l051_sharp_double_overlap_witness(self):
        data = lower_band_root_overlap_bound(5)
        self.assertEqual(data["root_channels"][3], (2, 3))
        self.assertEqual(data["max_multiplicity"], 2)

    def test_l052_threshold_is_sharp(self):
        data = lower_band_root_overlap_bound(14)
        self.assertEqual(data["root_channels"][9], (2, 3))
        with self.assertRaises(ValueError):
            lower_band_root_disjoint_bound(14)
        self.assertEqual(lower_band_root_disjoint_bound(15)["max_multiplicity"], 1)

    def test_input_validation(self):
        with self.assertRaises(ValueError):
            lower_band_primes(0)
        with self.assertRaises(ValueError):
            lower_band_base_root(10, 5)
        with self.assertRaises(ValueError):
            lower_band_base_root(10, 4)


if __name__ == "__main__":
    unittest.main()
