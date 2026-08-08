import itertools
import unittest
from collections import Counter
from math import comb


class TestP011CollisionPolynomial(unittest.TestCase):
    @staticmethod
    def polynomial(mapping):
        degree = len(mapping)
        coefficients = [0] * (degree + 1)
        for size in Counter(mapping).values():
            for k in range(1, size + 1):
                coefficients[k] += comb(size, k)
        return tuple(coefficients)

    @staticmethod
    def compose(first, second):
        return tuple(second[first[x]] for x in range(len(first)))

    @staticmethod
    def pair_merge_increment(a, b):
        degree = a + b
        result = [0] * (degree + 1)
        for i in range(1, a + 1):
            for j in range(1, b + 1):
                result[i + j] += comb(a, i) * comb(b, j)
        return tuple(result)

    def test_two_fiber_factorization_coefficients(self):
        for a in range(1, 8):
            for b in range(1, 8):
                direct = tuple(
                    (comb(a + b, k) if k <= a + b else 0)
                    - (comb(a, k) if k <= a else 0)
                    - (comb(b, k) if k <= b else 0)
                    for k in range(a + b + 1)
                )
                self.assertEqual(direct, self.pair_merge_increment(a, b))

    def test_polynomial_is_coefficientwise_monotone_under_postcomposition(self):
        size = 3
        all_maps = tuple(itertools.product(range(size), repeat=size))
        for current in all_maps:
            old = self.polynomial(current)
            for next_map in all_maps:
                updated = self.compose(current, next_map)
                new = self.polynomial(updated)
                self.assertTrue(all(a <= b for a, b in zip(old, new, strict=True)))

    def test_polynomial_equality_exactly_when_no_reachable_merge(self):
        size = 3
        all_maps = tuple(itertools.product(range(size), repeat=size))
        for current in all_maps:
            reachable = set(current)
            old = self.polynomial(current)
            for next_map in all_maps:
                updated = self.compose(current, next_map)
                no_merge = len({next_map[y] for y in reachable}) == len(reachable)
                self.assertEqual(self.polynomial(updated) == old, no_merge)

    def test_t_equals_one_strict_increment(self):
        def value_at_one(mapping):
            return sum((1 << size) - 1 for size in Counter(mapping).values())

        current = (0, 0, 1, 1, 1)
        next_map = (0, 0, 2, 3, 4)
        updated = self.compose(current, next_map)
        self.assertEqual(value_at_one(updated) - value_at_one(current), (2**2 - 1) * (2**3 - 1))


if __name__ == "__main__":
    unittest.main()
