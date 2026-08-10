import unittest

from enterprise_math.causal_primitive_response_cell import (
    active_primitive_constraints,
    bcc_primitive_moves,
    bcc_response_vertices,
    euclidean_voronoi_primitive_completeness_pressure_test,
    fcc_primitive_moves,
    fcc_response_vertices,
    point_satisfies_primitive_response_cell,
    response_vertex_profile,
    sc_primitive_moves,
    sc_response_vertices,
    three_dimensional_response_profiles,
)


class CausalPrimitiveResponseCellTests(unittest.TestCase):
    def test_sc_response_cell_is_cube_shadow(self):
        moves = sc_primitive_moves()
        vertices = sc_response_vertices()
        self.assertEqual(len(moves), 6)
        self.assertEqual(len(vertices), 8)
        self.assertTrue(all(point_satisfies_primitive_response_cell(v, moves) for v in vertices))
        self.assertEqual(response_vertex_profile(moves, vertices), (8, (3,) * 8))

    def test_fcc_response_cell_is_rhombic_dodecahedron_shadow(self):
        moves = fcc_primitive_moves()
        vertices = fcc_response_vertices()
        self.assertEqual(len(moves), 12)
        self.assertEqual(len(vertices), 14)
        self.assertTrue(all(point_satisfies_primitive_response_cell(v, moves) for v in vertices))
        profile = response_vertex_profile(moves, vertices)
        self.assertEqual(profile[0], 14)
        # Six axial vertices are incident to four primitive-response facets;
        # eight half-cube vertices are incident to three.
        self.assertEqual(profile[1], (3,) * 8 + (4,) * 6)

    def test_bcc_nearest_primitive_response_cell_is_octahedron(self):
        moves = bcc_primitive_moves()
        vertices = bcc_response_vertices()
        self.assertEqual(len(moves), 8)
        self.assertEqual(len(vertices), 6)
        self.assertTrue(all(point_satisfies_primitive_response_cell(v, moves) for v in vertices))
        self.assertEqual(response_vertex_profile(moves, vertices), (6, (4,) * 6))

    def test_three_dimensional_profiles_are_distinct(self):
        profiles = three_dimensional_response_profiles()
        self.assertEqual(set(profiles), {"SC", "FCC", "BCC"})
        self.assertEqual(profiles["SC"][0], 8)
        self.assertEqual(profiles["FCC"][0], 14)
        self.assertEqual(profiles["BCC"][0], 6)

    def test_external_voronoi_pressure_test_separates_bcc_primitive_incompleteness(self):
        data = euclidean_voronoi_primitive_completeness_pressure_test()
        self.assertEqual(data["SC"], (6, 6, True))
        self.assertEqual(data["FCC"], (12, 12, True))
        self.assertEqual(data["BCC"], (8, 14, False))

    def test_active_constraints_are_signed_primitive_moves(self):
        moves = fcc_primitive_moves()
        vertex = fcc_response_vertices()[0]
        active = active_primitive_constraints(vertex, moves)
        self.assertEqual(len(active), 4)
        self.assertTrue(all(move in moves for move in active))


if __name__ == "__main__":
    unittest.main()
