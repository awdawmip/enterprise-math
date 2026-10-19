from fractions import Fraction
from itertools import permutations
import unittest

from enterprise_math.euler_fcc_tetrahedral_transport import (
    IDENTITY,
    NORMALS,
    chiral_skew,
    determinant,
    face_half_turn,
    is_orthogonal,
    mapply,
    matrix_pow,
    mirror_face_holonomy,
    mirror_transport,
    mmul,
    mneg,
    proper_face_holonomy,
    proper_transport,
    shared_axis,
    spherical_cosine_certificate,
    tangent_witnesses,
    verify_all,
    vneg,
)


class EulerFccTetrahedralTransportTests(unittest.TestCase):
    def test_all_ordered_overlap_pairs(self) -> None:
        for i in range(4):
            for j in range(4):
                if i == j:
                    continue
                axis = shared_axis(i, j)
                proper = proper_transport(i, j)
                mirror = mirror_transport(i, j)

                self.assertTrue(is_orthogonal(proper))
                self.assertEqual(determinant(proper), 1)
                self.assertEqual(mapply(proper, NORMALS[i]), NORMALS[j])
                self.assertEqual(mapply(proper, axis), axis)
                self.assertEqual(mmul(proper_transport(j, i), proper), IDENTITY)

                self.assertTrue(is_orthogonal(mirror))
                self.assertEqual(determinant(mirror), -1)
                self.assertEqual(mapply(mirror, NORMALS[i]), NORMALS[j])
                self.assertEqual(mapply(mirror, axis), axis)
                self.assertEqual(matrix_pow(mirror, 2), IDENTITY)

    def test_proper_transport_preserves_chiral_complex_structure(self) -> None:
        for i in range(4):
            for j in range(4):
                if i == j:
                    continue
                left = mmul(
                    proper_transport(i, j),
                    mmul(chiral_skew(i), proper_transport(j, i)),
                )
                self.assertEqual(left, chiral_skew(j))

    def test_mirror_transport_reverses_chiral_complex_structure(self) -> None:
        for i in range(4):
            for j in range(4):
                if i == j:
                    continue
                bridge = mirror_transport(i, j)
                left = mmul(bridge, mmul(chiral_skew(i), bridge))
                self.assertEqual(left, mneg(chiral_skew(j)))

    def test_every_proper_face_loop_is_the_based_half_turn(self) -> None:
        for i, j, k in permutations(range(4), 3):
            holonomy = proper_face_holonomy(i, j, k)
            self.assertEqual(holonomy, face_half_turn(i))
            self.assertEqual(matrix_pow(holonomy, 2), IDENTITY)
            self.assertEqual(determinant(holonomy), 1)
            self.assertEqual(mapply(holonomy, NORMALS[i]), NORMALS[i])
            for tangent in tangent_witnesses(i):
                self.assertEqual(mapply(holonomy, tangent), vneg(tangent))

    def test_face_orientation_changes_lift_not_endpoint(self) -> None:
        for i, j, k in permutations(range(4), 3):
            self.assertEqual(
                proper_face_holonomy(i, j, k),
                proper_face_holonomy(i, k, j),
            )

    def test_every_mirror_face_loop_is_improper(self) -> None:
        for i, j, k in permutations(range(4), 3):
            holonomy = mirror_face_holonomy(i, j, k)
            self.assertTrue(is_orthogonal(holonomy))
            self.assertEqual(determinant(holonomy), -1)
            self.assertEqual(mapply(holonomy, NORMALS[i]), NORMALS[i])

    def test_base_face_exact_matrix(self) -> None:
        expected = (
            (Fraction(-1, 3), Fraction(2, 3), Fraction(2, 3)),
            (Fraction(2, 3), Fraction(-1, 3), Fraction(2, 3)),
            (Fraction(2, 3), Fraction(2, 3), Fraction(-1, 3)),
        )
        self.assertEqual(proper_face_holonomy(0, 1, 2), expected)

    def test_spherical_cosine_certificate(self) -> None:
        certificate = spherical_cosine_certificate()
        self.assertEqual(certificate["side_cosine"], Fraction(-1, 3))
        self.assertEqual(certificate["side_sine_squared"], Fraction(8, 9))
        self.assertEqual(certificate["vertex_cosine"], Fraction(-1, 2))

    def test_complete_certificate(self) -> None:
        result = verify_all()
        self.assertTrue(result.all_checks_passed)
        self.assertEqual(result.pair_count, 12)
        self.assertEqual(result.oriented_face_count, 24)
        self.assertEqual(result.proper_triangle_tangent_sign, -1)


if __name__ == "__main__":
    unittest.main()
