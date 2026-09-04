import unittest

from enterprise_math.euler_holonomy_residual_duality import (
    TORSION_RESIDUAL,
    ZERO_RESIDUAL,
)
from enterprise_math.euler_twisted_endpoint_cohomology import (
    FLAT_EDGE_BITS,
    ORDINARY_INCIDENCE,
    UNIFORM_TWISTED_INCIDENCE,
    UNIFORM_TWIST_EDGE_BITS,
    ZERO_TOTAL_TWISTED_MATRIX,
    complete_twisted_cohomology_certificate,
    determinantal_divisors,
    edge_total,
    equivariant_root_kernel_images,
    face_holonomies,
    matrix_vector,
    mod_two_matrix,
    neutralize_twisted_representative,
    smith_invariant_factors,
    symmetric_connection_classes,
    twisted_coboundary,
    unique_nonzero_equivariant_root_kernel_image,
    vector_add,
    verify_twisted_endpoint_cohomology,
    vertex_total,
)


class EulerTwistedEndpointCohomologyTests(unittest.TestCase):
    def test_smith_data(self) -> None:
        self.assertEqual(determinantal_divisors(ORDINARY_INCIDENCE), (1, 1, 1))
        self.assertEqual(smith_invariant_factors(ORDINARY_INCIDENCE), (1, 1, 1))
        self.assertEqual(determinantal_divisors(UNIFORM_TWISTED_INCIDENCE), (1, 1, 1, 2))
        self.assertEqual(smith_invariant_factors(UNIFORM_TWISTED_INCIDENCE), (1, 1, 1, 2))
        self.assertEqual(determinantal_divisors(ZERO_TOTAL_TWISTED_MATRIX), (1, 1, 2))
        self.assertEqual(smith_invariant_factors(ZERO_TOTAL_TWISTED_MATRIX), (1, 1, 2))

    def test_characteristic_two_identifies_the_incidence_maps(self) -> None:
        self.assertNotEqual(ORDINARY_INCIDENCE, UNIFORM_TWISTED_INCIDENCE)
        self.assertEqual(mod_two_matrix(ORDINARY_INCIDENCE), mod_two_matrix(UNIFORM_TWISTED_INCIDENCE))

    def test_uniform_twist_is_the_symmetric_nonflat_phase(self) -> None:
        self.assertEqual(face_holonomies(FLAT_EDGE_BITS), (0, 0, 0, 0))
        self.assertEqual(face_holonomies(UNIFORM_TWIST_EDGE_BITS), (1, 1, 1, 1))
        self.assertEqual(symmetric_connection_classes(), (ZERO_RESIDUAL, TORSION_RESIDUAL))

    def test_twisted_total_identity(self) -> None:
        for vertices in (
            (0, 0, 0, 0),
            (1, 0, 0, 0),
            (1, -2, 3, 4),
            (-5, 7, -11, 13),
        ):
            image = twisted_coboundary(vertices)
            self.assertEqual(edge_total(image), 3 * vertex_total(vertices))

    def test_total_mod_three_neutralization(self) -> None:
        samples = (
            (0, 0, 0, 0, 0, 0),
            (1, 1, 1, 0, 0, 0),
            (2, -1, 0, 1, 2, -1),
            (-3, 4, 2, -1, 1, 0),
        )
        for edges in samples:
            if sum(edges) % 3:
                continue
            shift, neutral = neutralize_twisted_representative(edges)
            self.assertEqual(sum(neutral), 0)
            self.assertEqual(vector_add(neutral, twisted_coboundary(shift)), edges)

    def test_unique_nonzero_symmetric_kernel_bridge(self) -> None:
        self.assertEqual(equivariant_root_kernel_images(), (ZERO_RESIDUAL, TORSION_RESIDUAL))
        self.assertEqual(unique_nonzero_equivariant_root_kernel_image(), TORSION_RESIDUAL)

    def test_bounded_exhaustive_certificate(self) -> None:
        report = verify_twisted_endpoint_cohomology(bound=2)
        self.assertEqual(report.ordinary_free_rank, 3)
        self.assertEqual(report.twisted_free_rank, 2)
        self.assertEqual(report.twisted_torsion, (2,))
        self.assertEqual(report.neutral_free_rank, 2)
        self.assertEqual(report.neutral_torsion, (2,))
        self.assertEqual(report.symmetric_gauge_classes, (ZERO_RESIDUAL, TORSION_RESIDUAL))
        self.assertEqual(report.unique_nonzero_kernel_image, TORSION_RESIDUAL)
        self.assertEqual(report.zero_total_injection_cases_checked, 5**4)
        self.assertGreater(report.neutralization_cases_checked, 0)

        certificate = complete_twisted_cohomology_certificate(bound=2)
        self.assertEqual(certificate["ordinary_graph_cohomology"]["abstract_group"], "Z^3")
        self.assertEqual(
            certificate["uniformly_twisted_graph_cohomology"]["abstract_group"],
            "Z^2 + Z/2",
        )
        self.assertEqual(certificate["zero_total_precision_sector"]["index_in_full_twisted_cohomology"], 3)
        self.assertFalse(certificate["zero_total_precision_sector"]["extension_split"])
        self.assertEqual(
            certificate["unique_nonzero_equivariant_root_kernel_image"],
            {"p": 0, "q": 0, "e": 1},
        )


if __name__ == "__main__":
    unittest.main()
