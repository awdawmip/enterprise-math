from fractions import Fraction
import unittest

from enterprise_math.euler_tetrahedral_holonomy import (
    NORMALS,
    determinant,
    dot,
    edge_spinor,
    exhaustive_certificate,
    expected_face_holonomy,
    expected_face_spinor,
    face_holonomy,
    face_spinor,
    identity_matrix,
    mat_mul,
    mat_vec,
    orientation_sign,
    quat_mul,
    quat_norm,
    quat_scale,
    scale_vec,
    shortest_rotation,
    spherical_tangent_cosine,
    tangent_vector,
    transpose,
)


class EulerTetrahedralHolonomyTests(unittest.TestCase):
    def test_regular_tetrahedral_gram_data(self) -> None:
        self.assertEqual([dot(n, n) for n in NORMALS], [3, 3, 3, 3])
        for left in range(4):
            for right in range(left + 1, 4):
                self.assertEqual(dot(NORMALS[left], NORMALS[right]), -1)
        self.assertEqual(
            tuple(sum(normal[index] for normal in NORMALS) for index in range(3)),
            (0, 0, 0),
        )

    def test_each_shortest_rotation_is_proper_and_maps_normals(self) -> None:
        for source in range(4):
            for target in range(4):
                if source == target:
                    continue
                rotation = shortest_rotation(source, target)
                self.assertEqual(mat_vec(rotation, NORMALS[source]), scale_vec(1, NORMALS[target]))
                self.assertEqual(mat_mul(transpose(rotation), rotation), identity_matrix())
                self.assertEqual(
                    mat_mul(shortest_rotation(target, source), rotation),
                    identity_matrix(),
                )
                self.assertEqual(quat_norm(edge_spinor(source, target)), 3)

    def test_every_oriented_face_loop_is_tangent_half_turn(self) -> None:
        from itertools import permutations

        for start, middle, end in permutations(range(4), 3):
            holonomy = face_holonomy(start, middle, end)
            self.assertEqual(holonomy, expected_face_holonomy(start))
            self.assertEqual(mat_vec(holonomy, NORMALS[start]), scale_vec(1, NORMALS[start]))
            for target in range(4):
                if target == start:
                    continue
                tangent = tangent_vector(start, target)
                self.assertEqual(mat_vec(holonomy, tangent), scale_vec(-1, tangent))

    def test_spin_lift_retains_orientation_sign(self) -> None:
        from itertools import permutations

        for start, middle, end in permutations(range(4), 3):
            spinor = face_spinor(start, middle, end)
            self.assertEqual(spinor, expected_face_spinor(start, middle, end))
            self.assertIn(orientation_sign(start, middle, end), (-1, 1))
            self.assertEqual(quat_mul(spinor, spinor), (-27, 0, 0, 0))
            self.assertEqual(face_spinor(start, end, middle), quat_scale(-1, spinor))
            self.assertEqual(
                face_holonomy(start, end, middle),
                face_holonomy(start, middle, end),
            )

    def test_spherical_interior_cosine_is_minus_half(self) -> None:
        from itertools import permutations

        for start, left, right in permutations(range(4), 3):
            self.assertEqual(spherical_tangent_cosine(start, left, right), Fraction(-1, 2))
            self.assertEqual(abs(determinant(NORMALS[start], NORMALS[left], NORMALS[right])), 4)

    def test_exhaustive_certificate(self) -> None:
        certificate = exhaustive_certificate()
        self.assertEqual(certificate["directed_edge_transports_checked"], 12)
        self.assertEqual(certificate["ordered_face_loops_checked"], 24)
        self.assertEqual(certificate["face_tangent_holonomy"], "minus identity")
        self.assertEqual(certificate["spherical_interior_angle_cosine"], Fraction(-1, 2))


if __name__ == "__main__":
    unittest.main()
