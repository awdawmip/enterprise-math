import unittest

from enterprise_math.relation_generation_profile import (
    exact_relation_generation_profile,
    finite_index_drop_count_bound,
)
from enterprise_math.relation_shared_prime_rank import derivative_coefficient_matrix


class RelationGenerationProfileTests(unittest.TestCase):
    def test_unit_1_plus_22_equals_23_full_rank_precedes_index_one(self) -> None:
        _primes, matrix = derivative_coefficient_matrix((1, 22, 23))
        relation = ((1, 1, -1),)
        basis = ((0, 1, 1),)
        profile = exact_relation_generation_profile(matrix, relation, basis)
        self.assertEqual(profile.relation_rank, 1)
        self.assertEqual(profile.first_nonzero_radius, 2)
        self.assertEqual(profile.full_rank_radius, 2)
        self.assertEqual(profile.generator_radius, 4)
        self.assertEqual(profile.direct_basis_upper_bound, 5)
        self.assertEqual(
            tuple((p.radius, p.coordinate_rank, p.subgroup_index) for p in profile.points),
            ((2, 1, 2), (4, 1, 1)),
        )
        self.assertEqual(finite_index_drop_count_bound(profile), 2)

    def test_unit_189_profile_collapses_in_one_step(self) -> None:
        _primes, matrix = derivative_coefficient_matrix((1, 8, 9))
        relation = ((1, 1, -1),)
        basis = ((0, 12, 12),)
        profile = exact_relation_generation_profile(matrix, relation, basis)
        self.assertEqual(
            (
                profile.first_nonzero_radius,
                profile.full_rank_radius,
                profile.generator_radius,
            ),
            (2, 2, 2),
        )
        self.assertEqual(
            tuple((p.radius, p.coordinate_rank, p.subgroup_index) for p in profile.points),
            ((2, 1, 1),),
        )

    def test_rank_two_abc_profile_is_complete_at_radius_one(self) -> None:
        _primes, matrix = derivative_coefficient_matrix((2, 3, 5))
        relation = ((1, 1, -1),)
        basis = ((1, 0, 1), (0, 1, 1))
        profile = exact_relation_generation_profile(matrix, relation, basis)
        self.assertEqual(profile.relation_rank, 2)
        self.assertEqual(
            (
                profile.first_nonzero_radius,
                profile.full_rank_radius,
                profile.generator_radius,
            ),
            (1, 1, 1),
        )
        self.assertEqual(profile.points[0].subgroup_index, 1)

    def test_long_basis_does_not_change_profile_endpoint(self) -> None:
        matrix = ((1, 0), (0, 1))
        basis = ((10, 1), (11, 1))
        profile = exact_relation_generation_profile(matrix, (), basis)
        self.assertEqual(profile.first_nonzero_radius, 1)
        self.assertEqual(profile.full_rank_radius, 1)
        self.assertEqual(profile.generator_radius, 1)
        self.assertEqual(profile.direct_basis_upper_bound, 11)
        self.assertEqual(profile.points[0].subgroup_index, 1)

    def test_shared_prime_rank_one_profile(self) -> None:
        _primes, matrix = derivative_coefficient_matrix((2, 4, 6))
        relation = ((4, 1, -2),)
        basis = ((2, 8, 8),)
        profile = exact_relation_generation_profile(matrix, relation, basis)
        self.assertEqual(
            (
                profile.first_nonzero_radius,
                profile.full_rank_radius,
                profile.generator_radius,
            ),
            (2, 2, 2),
        )
        self.assertEqual(profile.points[0].subgroup_index, 1)


if __name__ == "__main__":
    unittest.main()
