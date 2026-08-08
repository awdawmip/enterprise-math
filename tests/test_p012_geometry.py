import itertools
import unittest
from math import isqrt

from enterprise_math.geometry import (
    graph_distance,
    l1_distance,
    lattice2_ball,
    lattice2_sphere,
)


class TestP012IntrinsicGeometry(unittest.TestCase):
    @staticmethod
    def cycle4():
        return {
            0: {1, 3},
            1: {0, 2},
            2: {1, 3},
            3: {0, 2},
        }

    def test_graph_distance_metric_axioms(self):
        adjacency = self.cycle4()
        vertices = tuple(adjacency)
        for u, v, w in itertools.product(vertices, repeat=3):
            duv = graph_distance(adjacency, u, v)
            dvw = graph_distance(adjacency, v, w)
            duw = graph_distance(adjacency, u, w)
            self.assertEqual(duv == 0, u == v)
            self.assertEqual(duv, graph_distance(adjacency, v, u))
            self.assertLessEqual(duw, duv + dvw)

    def test_adjacency_is_exactly_distance_one(self):
        adjacency = self.cycle4()
        for u, v in itertools.product(adjacency, repeat=2):
            if u == v:
                continue
            self.assertEqual(
                graph_distance(adjacency, u, v) == 1,
                v in adjacency[u],
            )

    def test_cycle_rotation_is_an_isometry(self):
        adjacency = self.cycle4()
        rotate = lambda vertex: (vertex + 1) % 4
        for u, v in itertools.product(adjacency, repeat=2):
            self.assertEqual(
                graph_distance(adjacency, rotate(u), rotate(v)),
                graph_distance(adjacency, u, v),
            )

    def test_l1_distance_on_standard_integer_lattice(self):
        points = tuple(itertools.product(range(-3, 4), repeat=3))
        for left in points:
            for right in points:
                expected = sum(abs(a - b) for a, b in zip(left, right, strict=True))
                self.assertEqual(l1_distance(left, right), expected)

    def test_lattice2_sphere_and_ball_counts(self):
        self.assertEqual(len(lattice2_sphere(0)), 1)
        for radius in range(1, 31):
            self.assertEqual(len(lattice2_sphere(radius)), 4 * radius)
            self.assertEqual(
                len(lattice2_ball(radius)),
                2 * radius * radius + 2 * radius + 1,
            )

    def test_squared_euclidean_distance_fails_triangle(self):
        def squared(a, b):
            return sum((x - y) ** 2 for x, y in zip(a, b, strict=True))

        a = (0,)
        b = (1,)
        c = (2,)
        self.assertGreater(squared(a, c), squared(a, b) + squared(b, c))

    def test_floor_euclidean_distance_fails_triangle_on_integer_lattice(self):
        def floor_euclidean(a, b):
            squared = sum((x - y) ** 2 for x, y in zip(a, b, strict=True))
            return isqrt(squared)

        a = (0, 0)
        b = (1, 1)
        c = (3, 3)
        self.assertEqual(floor_euclidean(a, b), 1)
        self.assertEqual(floor_euclidean(b, c), 2)
        self.assertEqual(floor_euclidean(a, c), 4)
        self.assertGreater(
            floor_euclidean(a, c),
            floor_euclidean(a, b) + floor_euclidean(b, c),
        )

    def test_unreachable_graph_distance_is_explicitly_rejected(self):
        adjacency = {0: {1}, 1: {0}, 2: set()}
        with self.assertRaises(ValueError):
            graph_distance(adjacency, 0, 2)


if __name__ == "__main__":
    unittest.main()
