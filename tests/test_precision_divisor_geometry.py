import unittest

from enterprise_math.precision_divisor_geometry import (
    coarsen_divisor_value,
    coarsen_exponent_state,
    coarsening_composes,
    divisor_coordinate_value,
    divisor_grid_distance,
    divisor_grid_edges,
    divisor_grid_profile,
    divisor_grid_states,
    equal_prime_exponent_geometry,
    isotropic_genesis_sequence,
    isotropic_profile_sequence,
)


class PrecisionDivisorGeometryTests(unittest.TestCase):
    def test_precision_one_is_one_point_zero_rank_geometry(self):
        profile = divisor_grid_profile(1)
        self.assertEqual(
            (
                profile.dimension,
                profile.prime_support,
                profile.shape,
                profile.vertex_count,
                profile.edge_count,
                profile.diameter,
                profile.uniform_exponent_level,
            ),
            (0, (), (), 1, 0, 0, 0),
        )
        self.assertEqual(divisor_grid_states(1), ((),))
        self.assertEqual(divisor_grid_edges(1), frozenset())

    def test_lambda_thirty_has_exact_binary_cube_divisor_geometry(self):
        profile = divisor_grid_profile(30)
        self.assertEqual(profile.dimension, 3)
        self.assertEqual(profile.prime_support, (2, 3, 5))
        self.assertEqual(profile.maximum_exponents, (1, 1, 1))
        self.assertEqual(profile.shape, (2, 2, 2))
        self.assertEqual(profile.vertex_count, 8)
        self.assertEqual(profile.edge_count, 12)
        self.assertEqual(profile.diameter, 3)
        self.assertEqual(profile.uniform_exponent_level, 1)
        self.assertEqual(len(divisor_grid_states(30)), 8)
        self.assertEqual(len(divisor_grid_edges(30)), 12)
        self.assertEqual(divisor_grid_distance((0, 0, 0), (1, 1, 1), 30), 3)
        self.assertEqual(divisor_coordinate_value((1, 1, 1), 30), 30)

    def test_isotropic_prime_exponent_growth_gives_cubic_grids(self):
        self.assertEqual(isotropic_genesis_sequence(30, 3), (1, 30, 900, 27000))
        profiles = isotropic_profile_sequence(30, 3)
        self.assertEqual(tuple(profile.dimension for profile in profiles), (0, 3, 3, 3))
        self.assertEqual(tuple(profile.shape for profile in profiles), ((), (2, 2, 2), (3, 3, 3), (4, 4, 4)))
        self.assertEqual(tuple(profile.vertex_count for profile in profiles), (1, 8, 27, 64))
        self.assertEqual(tuple(profile.diameter for profile in profiles), (0, 3, 6, 9))
        self.assertTrue(all(equal_prime_exponent_geometry(profile.scale) for profile in profiles))

    def test_nonuniform_exponents_are_rectangular_not_axis_symmetric(self):
        profile = divisor_grid_profile(60)
        self.assertEqual(profile.maximum_exponents, (2, 1, 1))
        self.assertEqual(profile.shape, (3, 2, 2))
        self.assertEqual(profile.vertex_count, 12)
        self.assertEqual(profile.diameter, 4)
        self.assertIsNone(profile.uniform_exponent_level)
        self.assertFalse(equal_prime_exponent_geometry(60))

    def test_gcd_coarsening_is_canonical_and_composes(self):
        # 900=2^2*3^2*5^2 -> 30=2*3*5 -> 1.
        self.assertEqual(coarsen_divisor_value(180, 900, 30), 30)
        self.assertEqual(coarsen_exponent_state((2, 2, 1), 900, 30), (1, 1, 1))
        self.assertEqual(coarsen_exponent_state((2, 2, 1), 900, 1), ())
        for state in divisor_grid_states(900):
            self.assertTrue(coarsening_composes(state, 900, 30, 1))

    def test_expansion_preserves_old_exponent_cube_as_induced_coordinate_subset(self):
        old_states = set(divisor_grid_states(30))
        new_states = set(divisor_grid_states(900))
        self.assertTrue(old_states.issubset(new_states))
        old_edges = set(divisor_grid_edges(30))
        new_edges_inside_old = {
            edge for edge in divisor_grid_edges(900) if edge.issubset(old_states)
        }
        self.assertEqual(new_edges_inside_old, old_edges)

    def test_genesis_support_must_be_squarefree(self):
        with self.assertRaises(ValueError):
            isotropic_genesis_sequence(12, 2)
        with self.assertRaises(ValueError):
            isotropic_genesis_sequence(1, 2)

    def test_invalid_coarsening_fails_closed(self):
        with self.assertRaises(ValueError):
            coarsen_divisor_value(7, 900, 30)
        with self.assertRaises(ValueError):
            coarsen_divisor_value(30, 900, 28)
        with self.assertRaises(ValueError):
            coarsening_composes((1, 1, 1), 30, 6, 5)


if __name__ == "__main__":
    unittest.main()
