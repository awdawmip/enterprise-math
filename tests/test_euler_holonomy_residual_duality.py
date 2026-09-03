import unittest

from enterprise_math.euler_c12_root_torsor import (
    all_edge_bits,
    gauge_equivalent,
)
from enterprise_math.euler_holonomy_residual_duality import (
    EDGE_PAIRS,
    TORSION_RESIDUAL,
    ZERO_RESIDUAL,
    AffineResidual,
    all_face_flip_code,
    all_face_flip_edge_witness,
    all_permutations,
    all_residuals,
    complete_duality_certificate,
    edge_to_residual,
    holonomy_to_residual,
    invariant_residuals,
    opposite_edge,
    opposite_face_values,
    permute_edge_bits,
    permute_residual,
    permute_vertex_values,
    residual_support_edge,
    residual_to_holonomy,
    values_to_residual,
    verify_holonomy_residual_duality,
)


class EulerHolonomyResidualDualityTests(unittest.TestCase):
    def test_coordinate_maps_are_mutual_inverses(self) -> None:
        for residual in all_residuals():
            self.assertEqual(
                holonomy_to_residual(residual_to_holonomy(residual)),
                residual,
            )
        for a in (0, 1):
            for b in (0, 1):
                for c in (0, 1):
                    code = (a, b, c)
                    self.assertEqual(
                        residual_to_holonomy(holonomy_to_residual(code)),
                        code,
                    )

    def test_even_values_are_exact_affine_values(self) -> None:
        for residual in all_residuals():
            self.assertEqual(values_to_residual(residual.values), residual)
            self.assertEqual(sum(residual.values) % 2, 0)

    def test_edge_residual_is_complete_gauge_invariant(self) -> None:
        edge_states = tuple(all_edge_bits())
        for left in edge_states:
            for right in edge_states:
                self.assertEqual(
                    gauge_equivalent(left, right),
                    edge_to_residual(left) == edge_to_residual(right),
                )

    def test_opposite_face_map_is_s4_equivariant(self) -> None:
        for edges in all_edge_bits():
            for permutation in all_permutations():
                pushed = permute_edge_bits(edges, permutation)
                self.assertEqual(
                    opposite_face_values(pushed),
                    permute_vertex_values(opposite_face_values(edges), permutation),
                )
                self.assertEqual(
                    edge_to_residual(pushed),
                    permute_residual(edge_to_residual(edges), permutation),
                )

    def test_unique_invariant_line(self) -> None:
        self.assertEqual(invariant_residuals(), (ZERO_RESIDUAL, TORSION_RESIDUAL))
        self.assertEqual(holonomy_to_residual(all_face_flip_code()), TORSION_RESIDUAL)
        self.assertEqual(edge_to_residual(all_face_flip_edge_witness()), TORSION_RESIDUAL)

    def test_six_nonconstant_states_are_the_six_edges(self) -> None:
        nonconstant = tuple(residual for residual in all_residuals() if not residual.is_constant)
        supports = {residual_support_edge(residual) for residual in nonconstant}
        self.assertEqual(supports, set(EDGE_PAIRS))
        for residual in nonconstant:
            self.assertEqual(
                residual_support_edge(residual.complement()),
                opposite_edge(residual_support_edge(residual)),
            )

    def test_orbit_representatives(self) -> None:
        permutations_all = tuple(all_permutations())
        edge_state = AffineResidual(1, 0, 0)
        orbit = {permute_residual(edge_state, permutation) for permutation in permutations_all}
        self.assertEqual(len(orbit), 6)
        self.assertNotIn(ZERO_RESIDUAL, orbit)
        self.assertNotIn(TORSION_RESIDUAL, orbit)

    def test_complete_exhaustive_certificate(self) -> None:
        report = verify_holonomy_residual_duality()
        self.assertEqual(report.edge_cochains, 64)
        self.assertEqual(report.gauge_classes, 8)
        self.assertEqual(report.residual_states, 8)
        self.assertEqual(report.invariant_states, (ZERO_RESIDUAL, TORSION_RESIDUAL))
        self.assertEqual(report.nonconstant_edge_states, 6)
        self.assertEqual(report.permutations_checked, 24)
        self.assertEqual(report.equivariance_pairs_checked, 64 * 24)

        certificate = complete_duality_certificate()
        self.assertEqual(certificate["orbit_decomposition"], [1, 1, 6])
        self.assertEqual(certificate["all_face_flip_maps_to"], {"p": 0, "q": 0, "e": 1})


if __name__ == "__main__":
    unittest.main()
