import unittest

from enterprise_math.brc_critical_orbits import (
    CriticalOrbitPrefix,
    critical_euler_coefficients,
    critical_orbit_prefix,
    critical_primitive_orbit_counts,
    critical_word_counts,
    critical_zeta_coefficients,
)


class CriticalOrbitFoundationTests(unittest.TestCase):
    def test_unit_three_cycle(self):
        k = ((0, 1, 0), (0, 0, 1), (1, 0, 0))
        total, closed = critical_word_counts(k, 8)
        primitive = critical_primitive_orbit_counts(k, 8)
        self.assertTrue(all(total[n] == 3 for n in range(1, 9)))
        self.assertEqual(closed[3], 3)
        self.assertEqual(primitive[3], 1)
        self.assertEqual(sum(primitive[1:]), 1)

    def test_binary_one_state_necklaces(self):
        k = ((2,),)
        primitive = critical_primitive_orbit_counts(k, 6)
        self.assertEqual(primitive, (0, 2, 1, 2, 3, 6, 9))
        total, closed = critical_word_counts(k, 6)
        self.assertEqual(total, (1, 2, 4, 8, 16, 32, 64))
        self.assertEqual(closed, total)

    def test_branching_and_local_tie_can_share_orbit_inventory(self):
        local_tie = ((2,),)
        branching = ((1, 1), (1, 1))
        self.assertEqual(
            critical_primitive_orbit_counts(branching, 8),
            critical_primitive_orbit_counts(local_tie, 8),
        )

    def test_euler_matches_determinant_zeta(self):
        matrices = (
            ((1, 1), (1, 0)),
            ((1, 1), (1, 1)),
            ((0, 2), (1, 0)),
            ((1, 0), (0, 3)),
        )
        for matrix in matrices:
            self.assertEqual(
                critical_euler_coefficients(matrix, 10),
                critical_zeta_coefficients(matrix, 10),
            )

    def test_verified_prefix(self):
        prefix = critical_orbit_prefix(((1, 1), (1, 0)), 8)
        self.assertIsInstance(prefix, CriticalOrbitPrefix)
        self.assertTrue(prefix.verify())
        self.assertEqual(prefix.upto, 8)
        self.assertEqual(prefix.zeta_coefficients, critical_zeta_coefficients(prefix.critical_matrix, 8))

    def test_typed_guards(self):
        with self.assertRaises(TypeError):
            critical_word_counts(((True,),), 3)
        with self.assertRaises(ValueError):
            critical_word_counts(((-1,),), 3)
        with self.assertRaises(ValueError):
            critical_word_counts(((1,),), 0)
        with self.assertRaises(ValueError):
            critical_word_counts(((1, 0),), 3)


if __name__ == "__main__":
    unittest.main()
