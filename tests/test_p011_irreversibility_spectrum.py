import itertools
import unittest
from collections import Counter
from math import comb


class TestP011IrreversibilitySpectrum(unittest.TestCase):
    @staticmethod
    def all_maps(size):
        for values in itertools.product(range(size), repeat=size):
            yield values

    @staticmethod
    def compose(first, second):
        return tuple(second[first[x]] for x in range(len(first)))

    @staticmethod
    def fiber_counts(mapping):
        return Counter(mapping)

    @classmethod
    def collision_count(cls, mapping, k):
        return sum(comb(size, k) for size in cls.fiber_counts(mapping).values())

    @classmethod
    def collision_spectrum(cls, mapping):
        size = len(mapping)
        return tuple(cls.collision_count(mapping, k) for k in range(1, size + 1))

    @classmethod
    def reconstructed_fiber_size_multiplicities(cls, mapping):
        size = len(mapping)
        spectrum = (0,) + cls.collision_spectrum(mapping)
        reconstructed = {}
        for r in range(1, size + 1):
            reconstructed[r] = sum(
                ((-1) ** (k - r)) * comb(k, r) * spectrum[k]
                for k in range(r, size + 1)
            )
        return reconstructed

    @classmethod
    def actual_fiber_size_multiplicities(cls, mapping):
        sizes = Counter(cls.fiber_counts(mapping).values())
        return {r: sizes.get(r, 0) for r in range(1, len(mapping) + 1)}

    @classmethod
    def fiber_functional(cls, mapping, phi):
        return sum(phi(size) for size in cls.fiber_counts(mapping).values())

    def test_collision_spectrum_is_monotone_under_postcomposition(self):
        size = 3
        for current in self.all_maps(size):
            old = self.collision_spectrum(current)
            for next_map in self.all_maps(size):
                updated = self.compose(current, next_map)
                new = self.collision_spectrum(updated)
                self.assertEqual(old[0], size)
                self.assertEqual(new[0], size)
                for k in range(1, size):
                    self.assertGreaterEqual(new[k], old[k])

    def test_pair_count_is_strict_exactly_on_reachable_merge(self):
        size = 3
        for current in self.all_maps(size):
            reachable = set(current)
            for next_map in self.all_maps(size):
                updated = self.compose(current, next_map)
                strict_pairs = self.collision_count(updated, 2) > self.collision_count(current, 2)
                reachable_merge = len({next_map[y] for y in reachable}) < len(reachable)
                self.assertEqual(strict_pairs, reachable_merge)

    def test_binomial_inversion_recovers_fiber_size_distribution(self):
        size = 5
        for mapping in self.all_maps(size):
            self.assertEqual(
                self.reconstructed_fiber_size_multiplicities(mapping),
                self.actual_fiber_size_multiplicities(mapping),
            )

    def test_standard_superadditive_functionals_are_monotone(self):
        size = 3
        functions = (
            lambda n: n - 1,
            lambda n: n * n,
            lambda n: comb(n, 2),
            lambda n: comb(n, 3),
        )
        for current in self.all_maps(size):
            for next_map in self.all_maps(size):
                updated = self.compose(current, next_map)
                for phi in functions:
                    self.assertGreaterEqual(
                        self.fiber_functional(updated, phi),
                        self.fiber_functional(current, phi),
                    )

    def test_pair_increment_equals_new_cross_pairs(self):
        current = (0, 0, 1, 1, 1, 2)
        next_map = (0, 0, 1, 3, 4, 5)
        updated = self.compose(current, next_map)

        old_pair_count = self.collision_count(current, 2)
        new_pair_count = self.collision_count(updated, 2)

        # The next map merges the old fibers of sizes 2 and 3.
        self.assertEqual(new_pair_count - old_pair_count, 2 * 3)


if __name__ == "__main__":
    unittest.main()
