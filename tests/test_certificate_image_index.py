import unittest

from enterprise_math.certificate_image_index import (
    exact_certificate_image_profile,
    lattice_defect_signature,
    lattice_image_invariant,
)
from enterprise_math.relation_shared_prime_rank import derivative_coefficient_matrix


class CertificateImageIndexTests(unittest.TestCase):
    def test_maximal_minor_saturation_index(self) -> None:
        rank_one = lattice_image_invariant(((2, 4), (4, 8)))
        self.assertEqual((rank_one.rank, rank_one.saturation_index), (1, 2))

        rank_two = lattice_image_invariant(((2, 0), (0, 6)))
        self.assertEqual((rank_two.rank, rank_two.saturation_index), (2, 12))

    def test_equal_index_can_hide_different_defect_groups(self) -> None:
        cyclic_four = lattice_defect_signature(((4, 0), (0, 1)))
        klein_four = lattice_defect_signature(((2, 0), (0, 2)))
        self.assertEqual(cyclic_four.saturation_index, 4)
        self.assertEqual(klein_four.saturation_index, 4)
        self.assertEqual(cyclic_four.determinantal_divisors, (1, 4))
        self.assertEqual(klein_four.determinantal_divisors, (2, 4))
        self.assertEqual(cyclic_four.invariant_factors, (1, 4))
        self.assertEqual(klein_four.invariant_factors, (2, 2))
        self.assertNotEqual(cyclic_four.invariant_factors, klein_four.invariant_factors)

    def test_rank_one_signature_reduces_to_scalar_index(self) -> None:
        signature = lattice_defect_signature(((6,), (10,)))
        self.assertEqual(signature.rank, 1)
        self.assertEqual(signature.determinantal_divisors, (2,))
        self.assertEqual(signature.invariant_factors, (2,))
        self.assertEqual(signature.saturation_index, 2)

    def test_347_certificate_complete_precedes_relation_full_rank(self) -> None:
        _primes, matrix = derivative_coefficient_matrix((3, 4, 7))
        relation = ((1, 1, -1),)
        relation_basis = ((1, 0, 1), (0, 4, 4))
        wronskian = ((-4, 3, 0),)
        profile = exact_certificate_image_profile(
            matrix, relation, relation_basis, wronskian
        )
        self.assertEqual(profile.full_certificate_rank, 1)
        self.assertEqual(profile.intrinsic_saturation_index, 4)
        self.assertEqual(profile.first_nonzero_certificate_radius, 1)
        self.assertEqual(profile.full_certificate_rank_radius, 1)
        self.assertEqual(profile.certificate_complete_radius, 1)
        self.assertEqual(profile.relation_generator_radius, 2)
        self.assertEqual(
            tuple(
                (
                    point.radius,
                    point.certificate_rank,
                    point.index_in_full_certificate_image,
                    point.total_saturation_index,
                )
                for point in profile.points
            ),
            ((1, 1, 1, 4),),
        )

    def test_unit_1_plus_22_certificate_index_drops_two_to_one(self) -> None:
        _primes, matrix = derivative_coefficient_matrix((1, 22, 23))
        relation = ((1, 1, -1),)
        relation_basis = ((0, 1, 1),)
        wronskian = ((-22, 1, 0),)
        profile = exact_certificate_image_profile(
            matrix, relation, relation_basis, wronskian
        )
        self.assertEqual(profile.intrinsic_saturation_index, 1)
        self.assertEqual(profile.first_nonzero_certificate_radius, 2)
        self.assertEqual(profile.full_certificate_rank_radius, 2)
        self.assertEqual(profile.certificate_complete_radius, 4)
        self.assertEqual(profile.relation_generator_radius, 4)
        self.assertEqual(
            tuple(
                (
                    point.radius,
                    point.index_in_full_certificate_image,
                    point.total_saturation_index,
                )
                for point in profile.points
            ),
            ((2, 2, 2), (4, 1, 1)),
        )

    def test_redundant_zero_certificate_is_complete_at_radius_zero(self) -> None:
        _primes, matrix = derivative_coefficient_matrix((2, 3, 5))
        relation = ((1, 1, -1),)
        relation_basis = ((1, 0, 1), (0, 1, 1))
        zero = ((0, 0, 0),)
        profile = exact_certificate_image_profile(
            matrix, relation, relation_basis, zero
        )
        self.assertEqual(profile.full_certificate_rank, 0)
        self.assertEqual(profile.intrinsic_saturation_index, 1)
        self.assertEqual(profile.full_certificate_rank_radius, 0)
        self.assertEqual(profile.certificate_complete_radius, 0)
        self.assertEqual(profile.points, ())


if __name__ == "__main__":
    unittest.main()
