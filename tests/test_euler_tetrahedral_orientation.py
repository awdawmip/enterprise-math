import unittest

from enterprise_math.euler_tetrahedral_orientation import (
    IDENTITY3,
    TETRAHEDRAL_NORMALS,
    compose_symmetries,
    covariance_certificate,
    cross,
    cross_square_certificate,
    determinant,
    dot,
    even_transports,
    graph_cycle_holonomies,
    graph_sign_class_count,
    incidence_ray,
    mat_mul,
    negate,
    odd_transports,
    orientation_local_system_certificate,
    permutation_sign,
    shared_line_axes,
    stabilizer,
    tetrahedral_symmetries,
    transpose,
    triangle_loop_holonomies,
    vertex_gauge,
)


class EulerTetrahedralOrientationTests(unittest.TestCase):
    def test_regular_tetrahedral_gram_data(self) -> None:
        self.assertEqual(
            tuple(map(sum, zip(*TETRAHEDRAL_NORMALS))),
            (0, 0, 0),
        )
        for left in range(4):
            for right in range(4):
                self.assertEqual(
                    dot(TETRAHEDRAL_NORMALS[left], TETRAHEDRAL_NORMALS[right]),
                    3 if left == right else -1,
                )

    def test_six_shared_line_families(self) -> None:
        axes = shared_line_axes()
        self.assertEqual(len(axes), 6)
        self.assertEqual(len(set(axes.values())), 6)
        self.assertEqual(
            set(axes.values()),
            {
                (1, 1, 0),
                (1, -1, 0),
                (1, 0, 1),
                (1, 0, -1),
                (0, 1, 1),
                (0, 1, -1),
            },
        )

    def test_incidence_rays_reverse_across_a_shared_line(self) -> None:
        for source in range(4):
            for target in range(4):
                if source == target:
                    continue
                self.assertEqual(
                    incidence_ray(target, source),
                    negate(incidence_ray(source, target)),
                )

    def test_full_tetrahedral_group_and_orientation_character(self) -> None:
        symmetries = tetrahedral_symmetries()
        self.assertEqual(len(symmetries), 24)
        self.assertEqual(sum(item.orientation_preserving for item in symmetries), 12)
        self.assertEqual(sum(not item.orientation_preserving for item in symmetries), 12)
        self.assertEqual(len({item.permutation for item in symmetries}), 24)
        for item in symmetries:
            self.assertEqual(item.determinant, determinant(item.matrix))
            self.assertEqual(item.determinant, permutation_sign(item.permutation))
            self.assertEqual(mat_mul(item.matrix, transpose(item.matrix)), IDENTITY3)

    def test_cross_square_and_twisted_covariance(self) -> None:
        for normal in TETRAHEDRAL_NORMALS:
            left, right = cross_square_certificate(normal)
            self.assertEqual(left, right)
        for symmetry in tetrahedral_symmetries():
            for normal_index in range(4):
                left, right = covariance_certificate(symmetry, normal_index)
                self.assertEqual(left, right)

    def test_transport_counts_and_stabilizers(self) -> None:
        for source in range(4):
            self.assertEqual(len(stabilizer(source)), 3)
            for target in range(4):
                self.assertEqual(len(even_transports(source, target)), 3)
                self.assertEqual(len(odd_transports(source, target)), 3)

    def test_even_triangle_transport_has_flat_chirality(self) -> None:
        for triangle in ((0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)):
            profile = triangle_loop_holonomies(*triangle)
            self.assertEqual(sum(profile.values()), 27)
            self.assertEqual(len(profile), 3)
            self.assertEqual(sorted(profile.values()), [9, 9, 9])
            self.assertEqual(set(profile), {item.matrix for item in stabilizer(triangle[0])})

    def test_explicit_compositions_remain_in_the_group(self) -> None:
        symmetries = tetrahedral_symmetries()
        known = {item.matrix for item in symmetries}
        for first in symmetries:
            for second in symmetries:
                result = compose_symmetries(first, second)
                self.assertIn(result.matrix, known)
                self.assertEqual(
                    result.determinant,
                    first.determinant * second.determinant,
                )

    def test_abstract_graph_sign_space_has_eight_classes(self) -> None:
        self.assertEqual(graph_sign_class_count(), 8)
        for bits in (
            (0, 0, 0, 0, 0, 0),
            (1, 0, 1, 1, 0, 1),
            (1, 1, 1, 1, 1, 1),
        ):
            invariant = graph_cycle_holonomies(bits)
            for gauge in (
                (0, 0, 0, 0),
                (1, 0, 0, 0),
                (1, 1, 0, 1),
                (1, 1, 1, 1),
            ):
                self.assertEqual(
                    graph_cycle_holonomies(vertex_gauge(bits, gauge)),
                    invariant,
                )

    def test_complete_certificate(self) -> None:
        certificate = orientation_local_system_certificate()
        self.assertEqual(certificate["status"], "PASS")
        self.assertEqual(certificate["symmetry_count"], 24)
        self.assertEqual(certificate["orientation_preserving_count"], 12)
        self.assertEqual(certificate["orientation_reversing_count"], 12)
        self.assertEqual(certificate["abstract_graph_sign_class_count"], 8)
        self.assertEqual(certificate["ambient_oriented_transport_class"], (0, 0, 0))
        self.assertEqual(certificate["triangle_chirality_holonomy"], 0)


if __name__ == "__main__":
    unittest.main()
