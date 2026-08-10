import unittest
from itertools import combinations, product

from enterprise_math.causal_minimal_vector_geometry import (
    edge_context_two_cover,
    triangle_loop_return_counts,
)


def identity_gram(n: int):
    return tuple(tuple(1 if i == j else 0 for j in range(n)) for i in range(n))


def a_roots(rank: int):
    n = rank + 1
    roots = []
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            vector = [0] * n
            vector[i] = 1
            vector[j] = -1
            roots.append(tuple(vector))
    return tuple(roots)


def d_roots(rank: int):
    roots = []
    for i, j in combinations(range(rank), 2):
        for left in (-1, 1):
            for right in (-1, 1):
                vector = [0] * rank
                vector[i] = left
                vector[j] = right
                roots.append(tuple(vector))
    return tuple(roots)


def e8_roots_scaled():
    roots = []
    for i, j in combinations(range(8), 2):
        for left in (-2, 2):
            for right in (-2, 2):
                vector = [0] * 8
                vector[i] = left
                vector[j] = right
                roots.append(tuple(vector))
    for signs in product((-1, 1), repeat=8):
        if sum(value < 0 for value in signs) % 2 == 0:
            roots.append(tuple(signs))
    return tuple(roots)


class CausalMinimalVectorGeometryTests(unittest.TestCase):
    def test_a4_context_is_complete_two_cover_with_trivial_triangle_return(self):
        roots = a_roots(4)
        context = edge_context_two_cover(roots, identity_gram(5), roots[0])
        self.assertEqual(context.primitive_norm, 2)
        self.assertEqual(context.common_neighbor_count, 6)
        self.assertEqual(context.complementary_fiber_count, 3)
        self.assertTrue(context.complete_base)
        self.assertEqual(triangle_loop_return_counts(context), (1, 0))

    def test_d4_context_is_complete_two_cover_with_all_triangles_flipping(self):
        roots = d_roots(4)
        context = edge_context_two_cover(roots, identity_gram(4), roots[0])
        self.assertEqual(context.primitive_norm, 2)
        self.assertEqual(context.common_neighbor_count, 8)
        self.assertEqual(context.complementary_fiber_count, 4)
        self.assertTrue(context.complete_base)
        self.assertEqual(triangle_loop_return_counts(context), (0, 4))

    def test_d5_triangle_return_counts(self):
        roots = d_roots(5)
        context = edge_context_two_cover(roots, identity_gram(5), roots[0])
        self.assertEqual(context.complementary_fiber_count, 6)
        self.assertTrue(context.complete_base)
        self.assertEqual(triangle_loop_return_counts(context), (8, 12))

    def test_e8_scaled_integer_model(self):
        roots = e8_roots_scaled()
        context = edge_context_two_cover(roots, identity_gram(8), roots[0])
        self.assertEqual(len(roots), 240)
        self.assertEqual(context.primitive_norm, 8)
        self.assertEqual(context.common_neighbor_count, 56)
        self.assertEqual(context.complementary_fiber_count, 28)
        self.assertTrue(context.complete_base)
        self.assertEqual(triangle_loop_return_counts(context), (2016, 1260))


if __name__ == "__main__":
    unittest.main()
