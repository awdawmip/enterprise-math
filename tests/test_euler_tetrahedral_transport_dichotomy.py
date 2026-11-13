import unittest

from enterprise_math.euler_holonomy_residual_duality import (
    TORSION_RESIDUAL,
    ZERO_RESIDUAL,
)
from enterprise_math.euler_tetrahedral_transport_dichotomy import (
    EDGES,
    FACES,
    IDENTITY,
    all_permutations,
    assignment_edge_bits,
    assignment_is_equivariant,
    base_transport_candidates,
    complete_transport_certificate,
    complement_edge,
    face_transport,
    is_involution,
    permutation_sign,
    proper_half_turn_transport,
    reflection_transport,
    standard_representation_is_orthogonal,
    standard_representation_matrix,
    transport_assignment,
    verify_transport_dichotomy,
)
from enterprise_math.euler_twisted_endpoint_cohomology import determinant


class EulerTetrahedralTransportDichotomyTests(unittest.TestCase):
    def test_exactly_two_equivariant_base_transports(self) -> None:
        candidates = base_transport_candidates()
        self.assertEqual(len(candidates), 2)
        self.assertEqual(
            set(candidates),
            {
                reflection_transport((0, 1)),
                proper_half_turn_transport((0, 1)),
            },
        )

    def test_transport_assignments_are_equivariant_involutions(self) -> None:
        for kind in ("proper", "reflection"):
            self.assertTrue(assignment_is_equivariant(kind))
            for edge, transport in transport_assignment(kind).items():
                left, right = edge
                self.assertEqual(transport[left], right)
                self.assertEqual(transport[right], left)
                self.assertTrue(is_involution(transport))

    def test_proper_phase_is_exactly_flat(self) -> None:
        self.assertEqual(assignment_edge_bits("proper"), (0, 0, 0, 0, 0, 0))
        for face in FACES:
            self.assertEqual(face_transport("proper", face), IDENTITY)

    def test_reflective_phase_is_uniformly_twisted(self) -> None:
        self.assertEqual(assignment_edge_bits("reflection"), (1, 1, 1, 1, 1, 1))
        for face in FACES:
            self.assertEqual(permutation_sign(face_transport("reflection", face)), -1)

    def test_standard_three_dimensional_determinant_is_permutation_sign(self) -> None:
        for permutation in all_permutations():
            matrix = standard_representation_matrix(permutation)
            self.assertEqual(determinant(matrix), permutation_sign(permutation))
            self.assertTrue(standard_representation_is_orthogonal(permutation))

    def test_complementary_double_transposition(self) -> None:
        for edge in EDGES:
            proper = proper_half_turn_transport(edge)
            reflected = reflection_transport(edge)
            complement = reflection_transport(complement_edge(edge))
            self.assertEqual(proper, tuple(reflected[complement[index]] for index in range(4)))
            self.assertEqual(permutation_sign(proper), 1)
            self.assertEqual(permutation_sign(reflected), -1)

    def test_complete_certificate(self) -> None:
        report = verify_transport_dichotomy()
        self.assertEqual(report.candidate_count, 2)
        self.assertEqual(report.proper_residual, ZERO_RESIDUAL)
        self.assertEqual(report.reflection_residual, TORSION_RESIDUAL)
        self.assertEqual(report.permutation_representation_checks, 24)

        certificate = complete_transport_certificate()
        self.assertEqual(certificate["candidate_count"], 2)
        self.assertEqual(certificate["proper_phase"]["endpoint_residual"], {"p": 0, "q": 0, "e": 0})
        self.assertEqual(certificate["reflective_phase"]["endpoint_residual"], {"p": 0, "q": 0, "e": 1})


if __name__ == "__main__":
    unittest.main()
