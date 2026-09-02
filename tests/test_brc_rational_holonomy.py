from fractions import Fraction
import unittest

from enterprise_math import (
    fundamental_cycle_holonomy,
    m_power_free_thickness,
    mod_m_holonomy_shadow,
    prime_holonomy_coordinates,
    prime_valuations,
    rational_tree_gauge_normal_form,
    squarefree_thickness,
)

Q = Fraction


class RationalHolonomyToolTest(unittest.TestCase):
    def setUp(self) -> None:
        self.edges = [
            (0, 1, Q(12, 5)),
            (2, 1, Q(7, 18)),
            (2, 3, Q(25, 14)),
            (3, 0, Q(9, 10)),
            (0, 2, Q(11, 6)),
            (1, 3, Q(5, 21)),
            (0, 1, Q(13, 8)),
        ]
        self.tree = [0, 1, 2]

    def test_prime_valuations(self) -> None:
        self.assertEqual(dict(prime_valuations(Q(12, 5))), {2: 2, 3: 1, 5: -1})
        self.assertEqual(dict(prime_valuations(Q(1, 2))), {2: -1})
        self.assertEqual(prime_valuations(1), ())

    def test_power_thickness_and_brc_root(self) -> None:
        cases = {
            Q(1, 2): (2, Q(1, 2)),
            Q(2): (2, Q(1)),
            Q(1, 8): (2, Q(1, 4)),
            Q(12, 5): (15, Q(2, 5)),
        }
        for value, (skeleton, thickness) in cases.items():
            result = squarefree_thickness(value)
            self.assertEqual((result.skeleton, result.thickness), (skeleton, thickness))
            self.assertEqual(result.reconstruct(), value)
            recovered, numerator_trace, denominator_trace = result.brc_root_materialization()
            self.assertEqual(recovered, thickness)
            self.assertTrue(numerator_trace.exact)
            self.assertTrue(denominator_trace.exact)

        cube = m_power_free_thickness(Q(72, 125), 3)
        self.assertEqual(cube.reconstruct(), Q(72, 125))
        recovered, _, _ = cube.brc_root_materialization()
        self.assertEqual(recovered, cube.thickness)

    def test_tree_gauge_normal_form(self) -> None:
        normal = rational_tree_gauge_normal_form(4, self.edges, self.tree)
        self.assertEqual(normal.vertex_scales, (Q(1), Q(5, 12), Q(35, 216), Q(49, 540)))
        self.assertTrue(all(normal.normalized_edge_weights[i] == 1 for i in self.tree))
        self.assertEqual(len(normal.fundamental_holonomies), 4)
        for index, coordinate in zip(normal.non_tree_indices, normal.fundamental_holonomies):
            self.assertEqual(
                coordinate,
                fundamental_cycle_holonomy(4, self.edges, self.tree, index),
            )

    def test_gauge_equivalent_system_has_same_coordinates(self) -> None:
        normal = rational_tree_gauge_normal_form(4, self.edges, self.tree)
        h = [Q(2, 3), Q(5, 7), Q(11, 13), Q(17, 19)]
        transformed = [
            (a, b, q * h[b] / h[a])
            for a, b, q in self.edges
        ]
        normal2 = rational_tree_gauge_normal_form(4, transformed, self.tree)
        self.assertEqual(normal2.fundamental_holonomies, normal.fundamental_holonomies)
        self.assertEqual(
            prime_holonomy_coordinates(normal2.fundamental_holonomies),
            prime_holonomy_coordinates(normal.fundamental_holonomies),
        )

    def test_mod_m_shadows(self) -> None:
        normal = rational_tree_gauge_normal_form(4, self.edges, self.tree)
        parity = mod_m_holonomy_shadow(normal.fundamental_holonomies, 2)
        mod3 = mod_m_holonomy_shadow(normal.fundamental_holonomies, 3)
        self.assertTrue(parity)
        self.assertTrue(mod3)
        self.assertTrue(all(all(value in (0, 1) for value in vector) for _, vector in parity))
        self.assertTrue(all(all(0 <= value < 3 for value in vector) for _, vector in mod3))

    def test_input_boundaries(self) -> None:
        with self.assertRaises(ValueError):
            squarefree_thickness(0)
        with self.assertRaises(ValueError):
            m_power_free_thickness(Q(1, 2), 1)
        with self.assertRaises(ValueError):
            rational_tree_gauge_normal_form(2, [(0, 0, Q(1))], [0])


if __name__ == "__main__":
    unittest.main()
