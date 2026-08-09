import unittest

from enterprise_math.p017_smooth_core import (
    square_basin_smooth_core,
    square_basin_smooth_core_profile,
)


class P017SmoothCoreTests(unittest.TestCase):
    def test_every_basin_tail_is_unit_or_one_large_prime(self):
        saw_unit_tail = False
        saw_large_prime_tail = False
        saw_composite_prime_tail = False
        for k in range(2, 120):
            for n in range(k * k + 1, (k + 1) * (k + 1)):
                data = square_basin_smooth_core(k, n)
                tail = data["large_tail"]
                core = data["smooth_core"]
                self.assertEqual(core * tail, n)
                if tail == 1:
                    saw_unit_tail = True
                else:
                    saw_large_prime_tail = True
                    self.assertGreater(tail, k)
                    self.assertLessEqual(core, k)
                if not data["state_is_prime"] and tail > 1:
                    saw_composite_prime_tail = True
                    self.assertGreater(core, 1)
        self.assertTrue(saw_unit_tail)
        self.assertTrue(saw_large_prime_tail)
        self.assertTrue(saw_composite_prime_tail)

    def test_prime_iff_full_smooth_core_is_one(self):
        for k in range(2, 100):
            for n in range(k * k + 1, (k + 1) * (k + 1)):
                data = square_basin_smooth_core(k, n)
                self.assertEqual(data["state_is_prime"], data["smooth_core"] == 1)

    def test_prime_power_multiplicity_is_preserved(self):
        # 279=3^2*31 lies in the k=16 basin and keeps the full 3^2 core.
        data = square_basin_smooth_core(16, 279)
        self.assertEqual(data["smooth_core"], 9)
        self.assertEqual(data["large_tail"], 31)
        self.assertEqual(data["smooth_prime_powers"], ((3, 2),))

        # 265=5*53 gives the opposite mirror side of the same useful witness.
        other = square_basin_smooth_core(16, 265)
        self.assertEqual(other["smooth_core"], 5)
        self.assertEqual(other["large_tail"], 53)

    def test_complete_profile_partitions_each_basin(self):
        for k in (2, 3, 5, 10, 16, 25, 50, 100):
            data = square_basin_smooth_core_profile(k)
            self.assertEqual(len(data["states"]), 2 * k)
            self.assertEqual(
                len(data["primes"]) + len(data["composites"]), 2 * k
            )
            self.assertTrue(
                set(data["fully_k_smooth_composites"]).issubset(data["composites"])
            )
            self.assertTrue(
                set(data["prime_tail_composites"]).issubset(data["composites"])
            )

    def test_input_validation(self):
        with self.assertRaises(ValueError):
            square_basin_smooth_core(0, 2)
        with self.assertRaises(ValueError):
            square_basin_smooth_core(5, 25)
        with self.assertRaises(ValueError):
            square_basin_smooth_core(5, 36)


if __name__ == "__main__":
    unittest.main()
