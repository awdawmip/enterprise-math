import unittest

from enterprise_math.relation_shared_prime_rank import shared_prime_relation_system
from enterprise_math.shared_prime_certificate_rank import (
    build_shared_prime_certificate_rank_gain,
    shared_prime_certificate_rank_gain,
)


class SharedPrimeCertificateRankTests(unittest.TestCase):
    def test_pairwise_coprime_abc_recovers_stage27_gain(self) -> None:
        system = shared_prime_relation_system((2, 3, 5), ((1, 1, -1),))
        result = shared_prime_certificate_rank_gain(system, ((-3, 2, 0),))
        self.assertEqual(result.derivative_rank, 3)
        self.assertEqual(result.relation_derivative_rank, 1)
        self.assertEqual(result.compressed_rank, 2)
        self.assertEqual(result.rank_gain, 1)
        self.assertEqual(result.residual_kernel_rank, 1)

    def test_shared_prime_246_has_only_one_available_certificate_dimension(self) -> None:
        system = shared_prime_relation_system((2, 4, 6), ((1, 1, -1),))
        self.assertEqual(system.compressed_rank, 1)

        first_value = shared_prime_certificate_rank_gain(system, ((1, 0, 0),))
        self.assertEqual(first_value.certificate_derivative_rows, ((1, 0),))
        self.assertEqual(first_value.rank_gain, 1)
        self.assertTrue(first_value.compressed_state_complete)

        many = shared_prime_certificate_rank_gain(
            system,
            (
                (1, 0, 0),
                (0, 1, 0),
                (0, 0, 1),
                (3, -2, 5),
            ),
        )
        self.assertEqual(many.rank_gain, 1)
        self.assertTrue(many.compressed_state_complete)

    def test_declared_relation_row_remains_redundant_after_shared_map(self) -> None:
        relation = (1, 1, -1)
        result = build_shared_prime_certificate_rank_gain(
            (2, 4, 6),
            (relation,),
            (relation, tuple(5 * value for value in relation)),
        )
        self.assertEqual(result.rank_gain, 0)
        self.assertTrue(result.relation_redundant)
        self.assertEqual(result.residual_kernel_rank, 1)

    def test_shared_prime_coupling_reduces_identity_certificate_gain(self) -> None:
        # With no declared relation, naive block counting would see two block
        # coordinates.  Both actually depend on the same prime coordinate x_2.
        result = build_shared_prime_certificate_rank_gain(
            (4, 8),
            (),
            ((1, 0), (0, 1)),
        )
        self.assertEqual(result.derivative_rank, 1)
        self.assertEqual(result.compressed_rank, 1)
        self.assertEqual(result.certificate_row_count, 2)
        self.assertEqual(result.rank_gain, 1)
        self.assertTrue(result.compressed_state_complete)

    def test_zero_on_image_certificate_adds_no_precision(self) -> None:
        system = shared_prime_relation_system((4, 8), ())
        # t_8 - 3 t_4 vanishes on im(B) because derivative rows are (4) and (12).
        result = shared_prime_certificate_rank_gain(system, ((-3, 1),))
        self.assertEqual(result.certificate_derivative_rows, ((0,),))
        self.assertEqual(result.rank_gain, 0)
        self.assertTrue(result.relation_redundant)


if __name__ == "__main__":
    unittest.main()
