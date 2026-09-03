import unittest

from enterprise_math.euler_c12_root_torsor import (
    EDGES,
    FACES,
    all_edge_bits,
    all_holonomy_codes,
    all_vertex_bits,
    coboundary,
    complete_certificate,
    crt6,
    crt6_inverse,
    crt12,
    crt12_inverse,
    edge_transport_is_consistent,
    face_holonomies,
    gauge_equivalent,
    global_root_assignments,
    holonomy_code,
    is_flat,
    neg_mod,
    projective_half_turn_endpoint,
    quarter_turn_roots,
    reconstruct_vertex_signs,
    reduce12_to6,
    root_cover_kernel,
    root_state,
    transport_root,
    triangle_transport,
    verify_root_cover,
    verify_tetrahedral_flatness,
    vertex_flip,
)


class EulerC12RootTorsorTests(unittest.TestCase):
    def test_crt_decompositions_and_compatibility(self) -> None:
        for value in range(6):
            self.assertEqual(crt6_inverse(crt6(value)), value)
        for value in range(12):
            self.assertEqual(crt12_inverse(crt12(value)), value)
            a, b4 = crt12(value)
            self.assertEqual(crt6(reduce12_to6(value)), (a, b4 % 2))

    def test_root_cover_is_exact_and_non_split(self) -> None:
        verify_root_cover()
        self.assertEqual(root_cover_kernel(), (0, 6))
        generator_lifts = [value for value in range(12) if value % 6 == 1]
        self.assertEqual(generator_lifts, [1, 7])
        self.assertTrue(all((6 * value) % 12 == 6 for value in generator_lifts))

    def test_quarter_turn_is_a_free_c2_torsor(self) -> None:
        self.assertEqual(quarter_turn_roots(), (3, 9))
        for bit, root in enumerate(quarter_turn_roots()):
            self.assertEqual(root_state(bit), root)
            self.assertEqual((2 * root) % 12, 6)
            self.assertEqual(root % 6, 3)
            self.assertNotEqual(neg_mod(root, 12), root)
            self.assertIn(neg_mod(root, 12), quarter_turn_roots())
            self.assertEqual(transport_root(1, root), neg_mod(root, 12))
            self.assertEqual(transport_root(0, root), root)

    def test_flat_is_exactly_globalizable(self) -> None:
        image = {coboundary(vertices) for vertices in all_vertex_bits()}
        flat = {edges for edges in all_edge_bits() if is_flat(edges)}
        self.assertEqual(image, flat)
        self.assertEqual(len(flat), 8)

        for edges in flat:
            first, second = global_root_assignments(edges)
            self.assertEqual(second, vertex_flip(first))
            self.assertEqual(coboundary(first), edges)
            self.assertEqual(coboundary(second), edges)
            self.assertEqual(reconstruct_vertex_signs(edges, root_at_a=0), first)
            self.assertEqual(reconstruct_vertex_signs(edges, root_at_a=1), second)

    def test_face_holonomy_has_three_independent_bits(self) -> None:
        states = tuple(all_edge_bits())
        fibers = {
            code: {edges for edges in states if holonomy_code(edges) == code}
            for code in all_holonomy_codes()
        }
        self.assertEqual(len(fibers), 8)
        self.assertTrue(all(len(fiber) == 8 for fiber in fibers.values()))

        for edges in states:
            h0, h1, h2, h3 = face_holonomies(edges)
            self.assertEqual(h3, h0 ^ h1 ^ h2)

    def test_holonomy_code_is_complete_gauge_invariant(self) -> None:
        states = tuple(all_edge_bits())
        for left in states:
            for right in states:
                self.assertEqual(
                    gauge_equivalent(left, right),
                    holonomy_code(left) == holonomy_code(right),
                )

    def test_triangle_transport_detects_exact_face_holonomy(self) -> None:
        for edges in all_edge_bits():
            for face, holonomy in zip(FACES, face_holonomies(edges)):
                for root in quarter_turn_roots():
                    expected = root if holonomy == 0 else neg_mod(root, 12)
                    self.assertEqual(triangle_transport(edges, face, root), expected)

    def test_projective_endpoint_is_chirality_independent(self) -> None:
        self.assertEqual(
            {projective_half_turn_endpoint(root) for root in quarter_turn_roots()},
            {6},
        )

    def test_vertex_root_transport_is_consistent(self) -> None:
        for vertices in all_vertex_bits():
            self.assertTrue(edge_transport_is_consistent(vertices))

    def test_complete_exhaustive_certificate(self) -> None:
        report = verify_tetrahedral_flatness()
        self.assertEqual(report.edge_systems, 64)
        self.assertEqual(report.flat_edge_systems, 8)
        self.assertEqual(report.gauge_orbits, 8)
        self.assertEqual(report.systems_per_holonomy_code, 8)
        self.assertEqual(report.global_lifts_per_flat_system, 2)
        self.assertEqual(report.independent_face_bits, 3)
        self.assertEqual(report.projective_endpoint, 6)

        certificate = complete_certificate()
        self.assertEqual(
            certificate["tetrahedral_flatness"]["independent_face_bits"],
            3,
        )
        self.assertEqual(tuple(certificate["root_cover"]["quarter_turn_roots"]), (3, 9))


if __name__ == "__main__":
    unittest.main()
