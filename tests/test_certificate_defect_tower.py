import unittest

from enterprise_math.certificate_defect_tower import exact_certificate_defect_tower
from enterprise_math.relation_shared_prime_rank import derivative_coefficient_matrix


class CertificateDefectTowerTests(unittest.TestCase):
    def test_3_plus_7_multi_certificate_tower_changes_2_4_to_2_2(self) -> None:
        _primes, matrix = derivative_coefficient_matrix((3, 7, 10))
        relation = ((1, 1, -1),)
        relation_basis = ((1, 0, 1), (0, 1, 1))
        certificates = ((2, 0, 0), (0, 2, 0))
        tower = exact_certificate_defect_tower(
            matrix, relation, relation_basis, certificates
        )
        self.assertEqual(tower.full_certificate_rank, 2)
        self.assertEqual(tower.terminal_signature.invariant_factors, (2, 2))
        self.assertEqual(tower.terminal_signature.saturation_index, 4)
        self.assertEqual(tower.full_rank_radius, 1)
        self.assertEqual(tower.certificate_complete_radius, 2)
        self.assertEqual(tower.relation_generator_radius, 2)
        self.assertEqual(
            tuple(
                (
                    point.radius,
                    point.invariant_factors,
                    point.total_saturation_index,
                    point.access_image_index,
                    point.terminal,
                )
                for point in tower.points
            ),
            (
                (1, (2, 4), 8, 2, False),
                (2, (2, 2), 4, 1, True),
            ),
        )

    def test_3_plus_4_scalar_certificate_tower_stabilizes_early(self) -> None:
        _primes, matrix = derivative_coefficient_matrix((3, 4, 7))
        relation = ((1, 1, -1),)
        relation_basis = ((1, 0, 1), (0, 4, 4))
        wronskian = ((-4, 3, 0),)
        tower = exact_certificate_defect_tower(
            matrix, relation, relation_basis, wronskian
        )
        self.assertEqual(tower.terminal_signature.invariant_factors, (4,))
        self.assertEqual(tower.full_rank_radius, 1)
        self.assertEqual(tower.certificate_complete_radius, 1)
        self.assertEqual(tower.relation_generator_radius, 2)
        self.assertEqual(
            tuple((p.radius, p.invariant_factors, p.terminal) for p in tower.points),
            ((1, (4,), True),),
        )

    def test_1_plus_22_scalar_tower_is_pure_access_defect(self) -> None:
        _primes, matrix = derivative_coefficient_matrix((1, 22, 23))
        relation = ((1, 1, -1),)
        relation_basis = ((0, 1, 1),)
        wronskian = ((-22, 1, 0),)
        tower = exact_certificate_defect_tower(
            matrix, relation, relation_basis, wronskian
        )
        self.assertEqual(tower.terminal_signature.invariant_factors, (1,))
        self.assertEqual(
            tuple((p.radius, p.invariant_factors, p.access_image_index) for p in tower.points),
            ((2, (2,), 2), (4, (1,), 1)),
        )


if __name__ == "__main__":
    unittest.main()
