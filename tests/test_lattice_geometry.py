import ast
import inspect
import itertools
import unittest

import enterprise_math.lattice_geometry as lattice_geometry
from enterprise_math.lattice_geometry import (
    a_ball_collapse,
    a_ball_count,
    a_collapsed_radial_distance,
    a_coordinator_shell_count,
    a_first_precision_shell_count,
    a_graph_distance,
    a_precision_distance_ball_count,
    a_precision_distance_shell_count,
    a_quadratic_separation,
    a_quadratic_shell_count,
    a_quadratic_shell_counts,
    a_triangle_carry,
)


def a_points(p: int, bound: int):
    for prefix in itertools.product(range(-bound, bound + 1), repeat=p):
        yield prefix + (-sum(prefix),)


def unit_relation_signature(p: int):
    zero = (0,) * (p + 1)
    shell = [
        v
        for v in a_points(p, 2)
        if v != zero and a_collapsed_radial_distance(zero, v) == 1
    ]
    shell_set = set(shell)
    signature: dict[int, set[int]] = {}
    for v in shell:
        q = a_quadratic_separation(zero, v)
        common = sum(
            1
            for w in shell
            if tuple(w[i] - v[i] for i in range(p + 1)) in shell_set
        )
        signature.setdefault(q, set()).add(common)
    return signature


class LatticeGeometryTests(unittest.TestCase):
    def test_low_dimensional_coordinator_shells(self):
        self.assertEqual(
            [a_coordinator_shell_count(2, r) for r in range(6)],
            [1, 6, 12, 18, 24, 30],
        )
        self.assertEqual(
            [a_coordinator_shell_count(3, r) for r in range(6)],
            [1, 12, 42, 92, 162, 252],
        )

    def test_low_dimensional_graph_balls(self):
        self.assertEqual([a_ball_count(1, r) for r in range(5)], [1, 3, 5, 7, 9])
        self.assertEqual([a_ball_count(2, r) for r in range(5)], [1, 7, 19, 37, 61])
        self.assertEqual([a_ball_count(3, r) for r in range(4)], [1, 13, 55, 147])

    def test_graph_distance_is_half_l1_on_a_lattice(self):
        for p in range(1, 5):
            points = list(a_points(p, 2))[:30]
            for x in points:
                for y in points:
                    delta = [a - b for a, b in zip(x, y)]
                    self.assertEqual(2 * a_graph_distance(x, y), sum(abs(v) for v in delta))

    def test_quadratic_separation_is_integral_and_roots_have_unit_separation(self):
        for p in range(1, 6):
            zero = (0,) * (p + 1)
            for i in range(p + 1):
                for j in range(p + 1):
                    if i == j:
                        continue
                    root = tuple(
                        1 if k == i else -1 if k == j else 0
                        for k in range(p + 1)
                    )
                    self.assertEqual(a_quadratic_separation(zero, root), 1)
                    self.assertEqual(a_collapsed_radial_distance(zero, root), 1)

    def test_first_precision_shell_counts(self):
        self.assertEqual(
            [a_first_precision_shell_count(p) for p in range(1, 6)],
            [2, 12, 42, 110, 260],
        )
        for p in range(1, 5):
            zero = (0,) * (p + 1)
            actual = sum(
                1
                for v in a_points(p, 3)
                if v != zero and a_collapsed_radial_distance(zero, v) == 1
            )
            self.assertEqual(actual, a_first_precision_shell_count(p))

    def test_unit_distance_collapse_does_not_imply_relation_homogeneity(self):
        self.assertEqual(unit_relation_signature(3), {1: {24}, 2: {20}, 3: {14}})
        signature_p5 = unit_relation_signature(5)
        self.assertEqual(signature_p5[1], {132})
        self.assertEqual(signature_p5[2], {94})
        self.assertEqual(signature_p5[3], {54, 58})

    def test_finite_quadratic_shell_kernel(self):
        self.assertEqual(a_quadratic_shell_counts(1, 10), (1, 2, 0, 0, 2, 0, 0, 0, 0, 2, 0))
        self.assertEqual(a_quadratic_shell_counts(2, 10), (1, 6, 0, 6, 6, 0, 0, 12, 0, 6, 0))
        self.assertEqual(a_quadratic_shell_counts(3, 10), (1, 12, 6, 24, 12, 24, 8, 48, 6, 36, 24))
        for p in range(1, 5):
            for q in range(0, 8):
                zero = (0,) * (p + 1)
                actual = sum(
                    1
                    for v in a_points(p, 4)
                    if a_quadratic_separation(zero, v) == q
                )
                self.assertEqual(actual, a_quadratic_shell_count(p, q))

    def test_precision_distance_shells_are_root_basins_of_q(self):
        expected = {
            1: [1, 2, 2, 2, 2],
            2: [1, 12, 18, 24, 30],
            3: [1, 42, 98, 228, 314],
            4: [1, 110, 550, 1430, 3130],
        }
        for p, shells in expected.items():
            self.assertEqual(
                [a_precision_distance_shell_count(p, d) for d in range(5)],
                shells,
            )
            running = 0
            for d, shell in enumerate(shells):
                running += shell
                self.assertEqual(a_precision_distance_ball_count(p, d), running)
        for p in range(1, 6):
            self.assertEqual(a_precision_distance_shell_count(p, 0), 1)
            self.assertEqual(
                a_precision_distance_shell_count(p, 1),
                a_first_precision_shell_count(p),
            )

    def test_graph_and_radial_distance_integer_bounds(self):
        for p in range(1, 5):
            points = list(a_points(p, 2))[:30]
            for x in points:
                for y in points:
                    graph = a_graph_distance(x, y)
                    q = a_quadratic_separation(x, y)
                    radial = a_collapsed_radial_distance(x, y)
                    self.assertLessEqual(graph, q)
                    self.assertLessEqual(q, graph * graph if graph else 0)
                    self.assertLessEqual(radial, graph)
                    self.assertLessEqual(lattice_geometry.integer_nth_root(graph, 2), radial)

    def test_collapsed_radial_distance_has_additive_one_triangle_bound(self):
        for p in range(1, 4):
            points = list(a_points(p, 2))[:20]
            for x in points:
                for y in points:
                    for z in points:
                        self.assertLessEqual(
                            a_collapsed_radial_distance(x, z),
                            a_collapsed_radial_distance(x, y)
                            + a_collapsed_radial_distance(y, z)
                            + 1,
                        )
                        self.assertIn(a_triangle_carry(x, y, z), (0, 1))

    def test_triangle_carry_bound_is_sharp(self):
        a = (-2, 0, 2)
        b = (-1, 1, 0)
        c = (0, 2, -2)
        self.assertEqual(a_collapsed_radial_distance(a, b), 1)
        self.assertEqual(a_collapsed_radial_distance(b, c), 1)
        self.assertEqual(a_collapsed_radial_distance(a, c), 3)
        self.assertEqual(a_triangle_carry(a, b, c), 1)

    def test_ball_collapse_is_reductive_monotone_and_idempotent(self):
        for p in range(1, 5):
            last = -1
            for n in range(0, 300):
                current = a_ball_collapse(n, p)
                self.assertLessEqual(current, n)
                self.assertGreaterEqual(current, last)
                self.assertEqual(a_ball_collapse(current, p), current)
                last = current

    def test_reference_module_has_no_float_or_true_division(self):
        tree = ast.parse(inspect.getsource(lattice_geometry))
        float_constants = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.Constant) and isinstance(node.value, float)
        ]
        true_divisions = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div)
        ]
        self.assertEqual(float_constants, [])
        self.assertEqual(true_divisions, [])


if __name__ == "__main__":
    unittest.main()
