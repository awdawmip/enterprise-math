import itertools
import unittest

from enterprise_math.profinite_ghost_cylinder_compactness import (
    ghost_finite_cylinder_intersection,
    modulus_family_lcm,
)


class ProfiniteGhostCylinderCompactnessTests(unittest.TestCase):
    def test_lcm_controls_finite_cylinder_intersection(self):
        families = (
            (2, 3),
            (4, 6),
            (8, 9, 25),
            (5, 7, 11, 13),
            (16, 27, 49, 121),
        )
        for family in families:
            report = ghost_finite_cylinder_intersection(family)
            self.assertEqual(report.lcm_modulus, modulus_family_lcm(family))
            self.assertTrue(report.solves_every_cylinder)
            self.assertEqual(report.polynomial_value % report.lcm_modulus, 0)

    def test_every_small_triple_has_one_common_lcm_root(self):
        candidates = tuple(range(1, 13))
        for family in itertools.combinations(candidates, 3):
            report = ghost_finite_cylinder_intersection(family)
            self.assertTrue(report.solves_every_cylinder)

    def test_repeated_and_nested_moduli_do_not_change_the_lcm_cylinder(self):
        first = ghost_finite_cylinder_intersection((4, 6))
        second = ghost_finite_cylinder_intersection((2, 3, 4, 6, 12, 12))
        self.assertEqual(first.lcm_modulus, 12)
        self.assertEqual(second.lcm_modulus, 12)
        self.assertTrue(first.solves_every_cylinder)
        self.assertTrue(second.solves_every_cylinder)

    def test_validation(self):
        with self.assertRaises(ValueError):
            modulus_family_lcm(())
        with self.assertRaises(ValueError):
            ghost_finite_cylinder_intersection((0, 2))
        with self.assertRaises(TypeError):
            ghost_finite_cylinder_intersection((True, 2))


if __name__ == "__main__":
    unittest.main()
