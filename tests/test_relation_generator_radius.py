import unittest

from enterprise_math.relation_generator_radius import (
    basis_coordinates,
    coordinate_subgroup_index,
    exact_relation_generator_radius,
    relation_generation_layer,
)
from enterprise_math.relation_shared_prime_rank import derivative_coefficient_matrix


class RelationGeneratorRadiusTests(unittest.TestCase):
    def test_rank_one_shared_prime_relation_starts_at_radius_two(self) -> None:
        _primes, matrix = derivative_coefficient_matrix((2, 4, 6))
        relation = ((4, 1, -2),)
        basis = ((2, 8, 8),)
        result = exact_relation_generator_radius(matrix, relation, basis)
        self.assertEqual(result.first_nonzero_radius, 2)
        self.assertEqual(result.generator_radius, 2)
        self.assertEqual(result.direct_basis_upper_bound, 2)
        self.assertEqual(result.layer_at_generator_radius.subgroup_index, 1)

    def test_abc_rank_two_relation_group_is_generated_at_radius_one(self) -> None:
        _primes, matrix = derivative_coefficient_matrix((2, 3, 5))
        relation = ((1, 1, -1),)
        basis = ((1, 0, 1), (0, 1, 1))
        layer = relation_generation_layer(matrix, relation, basis, 1)
        self.assertEqual(layer.coordinate_rank, 2)
        self.assertEqual(layer.subgroup_index, 1)
        self.assertTrue(layer.complete)

        result = exact_relation_generator_radius(matrix, relation, basis)
        self.assertEqual(result.first_nonzero_radius, 1)
        self.assertEqual(result.generator_radius, 1)
        self.assertEqual(result.direct_basis_upper_bound, 1)

    def test_generation_can_precede_direct_access_to_a_chosen_basis(self) -> None:
        matrix = ((1, 0), (0, 1))
        relation = ()
        # Unimodular but deliberately long basis of Z^2.
        basis = ((10, 1), (11, 1))
        self.assertEqual(basis_coordinates(basis, (1, 0)), (-1, 1))
        self.assertEqual(basis_coordinates(basis, (0, 1)), (11, -10))

        result = exact_relation_generator_radius(matrix, relation, basis)
        self.assertEqual(result.first_nonzero_radius, 1)
        self.assertEqual(result.generator_radius, 1)
        self.assertEqual(result.direct_basis_upper_bound, 11)
        self.assertLess(result.generator_radius, result.direct_basis_upper_bound)

    def test_maximal_minor_gcd_is_exact_subgroup_index(self) -> None:
        self.assertEqual(coordinate_subgroup_index(((2, 0), (0, 3)), 2), 6)
        self.assertEqual(
            coordinate_subgroup_index(((2, 0), (0, 3), (1, 1)), 2),
            1,
        )
        self.assertIsNone(coordinate_subgroup_index(((2, 0), (4, 0)), 2))
        self.assertEqual(coordinate_subgroup_index(((2,), (3,)), 1), 1)
        self.assertEqual(coordinate_subgroup_index(((4,), (6,)), 1), 2)

    def test_rank_two_layer_can_have_full_rank_but_nontrivial_index(self) -> None:
        matrix = ((2, 0), (0, 3))
        relation = ()
        # The relation lattice is 2Z x 3Z, so use its true basis.
        basis = ((2, 0), (0, 3))
        layer = relation_generation_layer(matrix, relation, basis, 1)
        self.assertEqual(layer.coordinate_rank, 2)
        self.assertEqual(layer.subgroup_index, 1)
        self.assertTrue(layer.complete)

    def test_value_outside_declared_integer_lattice_is_rejected(self) -> None:
        basis = ((2, 0), (0, 3))
        with self.assertRaises(ValueError):
            basis_coordinates(basis, (1, 0))


if __name__ == "__main__":
    unittest.main()
