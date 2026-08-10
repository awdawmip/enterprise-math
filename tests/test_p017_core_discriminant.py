import math
import unittest

from enterprise_math.p017_core_cell_lattice import exact_full_core_pair
from enterprise_math.p017_core_discriminant import (
    prime_power_collision_capacity,
    prime_power_overlap_exponent,
    signed_core_discriminant,
)


class P017CoreDiscriminantTests(unittest.TestCase):
    def test_signed_vandermonde_divisibility_on_small_domains(self) -> None:
        for k in range(5, 70):
            center = k * (k + 1)
            radii = [r for r in range(1, k) if math.gcd(r, center) == 1]
            sample = radii[: min(5, len(radii))]
            incidences = []
            for radius in sample:
                incidences.append((radius, "lower"))
                incidences.append((radius, "upper"))
            data = signed_core_discriminant(k, tuple(incidences))
            self.assertEqual(data["vandermonde"] % data["required_divisor"], 0)

    def test_arbitrary_mixed_signed_subsets(self) -> None:
        for k in range(7, 80):
            center = k * (k + 1)
            radii = [r for r in range(1, k) if math.gcd(r, center) == 1]
            if len(radii) < 3:
                continue
            incidences = (
                (radii[0], "lower"),
                (radii[1], "upper"),
                (radii[2], "lower"),
            )
            data = signed_core_discriminant(k, incidences)
            self.assertEqual(data["pair_count"], 3)
            self.assertEqual(data["vandermonde"] % data["required_divisor"], 0)

    def test_prime_power_overlap_exponent_matches_pairwise_gcd_valuation(self) -> None:
        for k in range(5, 60):
            center = k * (k + 1)
            radii = [r for r in range(1, k) if math.gcd(r, center) == 1][:4]
            cores = []
            for radius in radii:
                lower, upper = exact_full_core_pair(k, radius)
                cores.extend((lower, upper))
            cores_tuple = tuple(cores)
            for prime in (3, 5, 7):
                exponent = prime_power_overlap_exponent(cores_tuple, prime)
                product = 1
                for i, left in enumerate(cores_tuple):
                    for right in cores_tuple[i + 1 :]:
                        product *= math.gcd(left, right)
                direct = 0
                value = product
                while value % prime == 0:
                    direct += 1
                    value //= prime
                self.assertEqual(exponent, direct)

    def test_prime_power_level_capacity_reconstructs_collision_exponent(self) -> None:
        saw_reuse = False
        for k in range(8, 85):
            center = k * (k + 1)
            radii = [r for r in range(1, k) if math.gcd(r, center) == 1]
            incidences = tuple(
                item
                for radius in radii[: min(12, len(radii))]
                for item in ((radius, "lower"), (radius, "upper"))
            )
            for prime in (3, 5, 7, 11):
                if prime > k or center % prime == 0:
                    continue
                data = prime_power_collision_capacity(k, incidences, prime)
                self.assertEqual(
                    data["actual_overlap_exponent"],
                    sum(level["collisions"] for level in data["levels"]),
                )
                self.assertLessEqual(
                    data["actual_overlap_exponent"], data["universal_collision_bound"]
                )
                for level in data["levels"]:
                    self.assertLessEqual(level["multiplicity"], level["capacity"])
                    if level["power"] > k - 1:
                        self.assertLessEqual(level["multiplicity"], 1)
                    if level["multiplicity"] >= 2:
                        saw_reuse = True
        self.assertTrue(saw_reuse)

    def test_full_signed_population_obeys_prime_power_packing(self) -> None:
        for k in (20, 37, 64, 100):
            center = k * (k + 1)
            radii = [r for r in range(1, k) if math.gcd(r, center) == 1]
            incidences = tuple(
                item
                for radius in radii
                for item in ((radius, "lower"), (radius, "upper"))
            )
            for prime in (3, 5, 7, 11, 13):
                if prime > k or center % prime == 0:
                    continue
                data = prime_power_collision_capacity(k, incidences, prime)
                for level in data["levels"]:
                    expected_capacity = (k - 1) // level["power"] + 1
                    self.assertEqual(level["capacity"], expected_capacity)

    def test_same_exact_pair_discriminant_contains_fixed_cell_spacing(self) -> None:
        saw = False
        for k in range(5, 180):
            center = k * (k + 1)
            buckets = {}
            for radius in range(1, k):
                if math.gcd(radius, center) != 1:
                    continue
                buckets.setdefault(exact_full_core_pair(k, radius), []).append(radius)
            for (a, b), radii in buckets.items():
                if len(radii) < 2:
                    continue
                saw = True
                left, right = radii[0], radii[1]
                data = signed_core_discriminant(
                    k,
                    ((left, "lower"), (right, "lower"), (left, "upper"), (right, "upper")),
                )
                self.assertEqual(abs(left - right) % (2 * a * b), 0)
                self.assertEqual(data["vandermonde"] % data["required_divisor"], 0)
        self.assertTrue(saw)


if __name__ == "__main__":
    unittest.main()
