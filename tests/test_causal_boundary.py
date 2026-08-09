import itertools
import unittest

from enterprise_math.causal_boundary import (
    causal_boundary_complex,
    opposite_endpoint_path_has_boundary,
    path_crosses_causal_boundary,
    phase_ambiguity,
    phase_possibilities_on_fiber,
    phase_refinement_profile,
    phase_regions,
    transported_boundary_complex,
)


class CausalBoundaryTests(unittest.TestCase):
    def test_discrete_intermediate_value_property_exhaustively(self):
        for length in range(2, 8):
            path = list(range(length))
            for values in itertools.product((-1, 0, 1), repeat=length):
                if values[0] * values[-1] >= 0:
                    continue
                expansion = lambda vertex, values=values: values[vertex]
                self.assertTrue(opposite_endpoint_path_has_boundary(path, expansion))

    def test_boundary_can_be_zero_vertex_or_crossing_edge(self):
        vertices = [0, 1, 2, 3, 4]
        edges = [(0, 1), (1, 2), (2, 3), (3, 4)]
        vertex_field = {0: 1, 1: 1, 2: 0, 3: -1, 4: -1}
        vertex_boundary = causal_boundary_complex(vertices, edges, vertex_field.__getitem__)
        self.assertEqual(vertex_boundary["vertices"], (2,))
        self.assertEqual(vertex_boundary["edges"], ())
        edge_field = {0: 1, 1: 1, 2: -1, 3: -1, 4: -1}
        edge_boundary = causal_boundary_complex(vertices, edges, edge_field.__getitem__)
        self.assertEqual(edge_boundary["vertices"], ())
        self.assertEqual(edge_boundary["edges"], (frozenset((1, 2)),))

    def test_extremal_zero_without_sign_change_is_still_boundary(self):
        vertices = [0, 1, 2]
        edges = [(0, 1), (1, 2)]
        field = {0: 1, 1: 0, 2: 1}
        boundary = causal_boundary_complex(vertices, edges, field.__getitem__)
        self.assertEqual(boundary["vertices"], (1,))
        self.assertEqual(boundary["edges"], ())
        self.assertTrue(path_crosses_causal_boundary(vertices, field.__getitem__))

    def test_phase_regions_form_a_partition(self):
        vertices = list(range(9))
        field = {vertex: (vertex % 3) - 1 for vertex in vertices}
        regions = phase_regions(vertices, field.__getitem__)
        flattened = [vertex for sign in (-1, 0, 1) for vertex in regions[sign]]
        self.assertEqual(sorted(flattened), vertices)
        self.assertTrue(all(field[v] < 0 for v in regions[-1]))
        self.assertTrue(all(field[v] == 0 for v in regions[0]))
        self.assertTrue(all(field[v] > 0 for v in regions[1]))

    def test_phase_ambiguity_decreases_under_precision_refinement(self):
        states = list(range(8))
        expansion = lambda state: state - 3
        coarse = lambda state: state // 8
        medium = lambda state: state // 4
        fine = lambda state: state
        self.assertEqual(
            phase_possibilities_on_fiber(states, coarse, expansion, 3),
            frozenset((-1, 0, 1)),
        )
        self.assertEqual(phase_ambiguity(states, coarse, expansion, 3), 3)
        self.assertEqual(phase_refinement_profile(states, [coarse, medium, fine], expansion, 3), [3, 2, 1])

    def test_boundary_is_equivariant_under_graph_symmetry(self):
        vertices = [0, 1, 2, 3]
        edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
        expansion = {0: 1, 1: 0, 2: -1, 3: 0}
        rotation = {0: 1, 1: 2, 2: 3, 3: 0}
        transported = transported_boundary_complex(vertices, edges, expansion.__getitem__, rotation)
        transported_field = {rotation[vertex]: expansion[vertex] for vertex in vertices}
        recomputed = causal_boundary_complex(vertices, edges, transported_field.__getitem__)
        self.assertEqual(set(transported["vertices"]), set(recomputed["vertices"]))
        self.assertEqual(set(transported["edges"]), set(recomputed["edges"]))


if __name__ == "__main__":
    unittest.main()
