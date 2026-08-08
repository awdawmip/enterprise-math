import ast
import inspect
import itertools
import unittest

import enterprise_math.overlap_focusing as overlap
from enterprise_math.directed_expansion import (
    collision_excess,
    local_collision_spectrum,
    section_expansion,
)
from enterprise_math.overlap_focusing import (
    collision_from_overlap_spectrum,
    diminishing_returns_check,
    expansion_from_overlap_spectrum,
    k_way_successor_overlap,
    marginal_expansion_increment,
    overlap_spectrum,
    pair_collision_bounds,
    submodularity_defect,
)


class OverlapFocusingTests(unittest.TestCase):
    def test_overlap_spectrum_equals_p011_local_collision_spectrum(self):
        for vertex_count in range(1, 4):
            vertices = list(range(vertex_count))
            possible_edges = [
                (source, target)
                for source in vertices
                for target in vertices
            ]
            for edge_mask in range(1 << len(possible_edges)):
                edges = [
                    edge
                    for index, edge in enumerate(possible_edges)
                    if edge_mask & (1 << index)
                ]
                for section_mask in range(1, 1 << vertex_count):
                    section = [
                        vertex
                        for vertex in vertices
                        if section_mask & (1 << vertex)
                    ]
                    spectrum = overlap_spectrum(vertices, edges, section)
                    for order, value in enumerate(spectrum, start=1):
                        self.assertEqual(
                            value,
                            local_collision_spectrum(
                                vertices, edges, section, order
                            ),
                        )

    def test_collision_is_alternating_projection_of_overlap_spectrum(self):
        for vertex_count in range(1, 4):
            vertices = list(range(vertex_count))
            possible_edges = [
                (source, target)
                for source in vertices
                for target in vertices
            ]
            for edge_mask in range(1 << len(possible_edges)):
                edges = [
                    edge
                    for index, edge in enumerate(possible_edges)
                    if edge_mask & (1 << index)
                ]
                for section_mask in range(1, 1 << vertex_count):
                    section = [
                        vertex
                        for vertex in vertices
                        if section_mask & (1 << vertex)
                    ]
                    spectrum = overlap_spectrum(vertices, edges, section)
                    self.assertEqual(
                        collision_from_overlap_spectrum(spectrum),
                        collision_excess(vertices, edges, section),
                    )
                    self.assertEqual(
                        expansion_from_overlap_spectrum(vertices, edges, section),
                        section_expansion(vertices, edges, section),
                    )

    def test_pair_collision_bounds(self):
        for vertex_count in range(1, 4):
            vertices = list(range(vertex_count))
            possible_edges = [
                (source, target)
                for source in vertices
                for target in vertices
            ]
            for edge_mask in range(1 << len(possible_edges)):
                edges = [
                    edge
                    for index, edge in enumerate(possible_edges)
                    if edge_mask & (1 << index)
                ]
                for section_mask in range(1, 1 << vertex_count):
                    section = [
                        vertex
                        for vertex in vertices
                        if section_mask & (1 << vertex)
                    ]
                    data = pair_collision_bounds(vertices, edges, section)
                    self.assertLessEqual(
                        data["collision_excess"],
                        data["pair_collision_load"],
                    )
                    if data["collision_excess"] > 0:
                        self.assertLessEqual(
                            2 * data["pair_collision_load"],
                            data["maximum_target_multiplicity"]
                            * data["collision_excess"],
                        )

    def test_marginal_expansion_formula_exhaustively(self):
        for vertex_count in range(2, 5):
            vertices = list(range(vertex_count))
            possible_edges = [
                (source, target)
                for source in vertices
                for target in vertices
            ]
            sampled_edge_sets = [
                [],
                possible_edges[::2],
                possible_edges[1::2],
                possible_edges[::3],
                possible_edges,
            ]
            for edges in sampled_edge_sets:
                for section_size in range(1, vertex_count):
                    for section_tuple in itertools.combinations(
                        vertices, section_size
                    ):
                        section = set(section_tuple)
                        for added_vertex in set(vertices) - section:
                            data = marginal_expansion_increment(
                                vertices, edges, section, added_vertex
                            )
                            self.assertEqual(
                                data["marginal_expansion"],
                                data["branch_increment"]
                                - data["future_overlap_load"],
                            )

    def test_diminishing_returns_and_submodularity(self):
        vertices = list(range(5))
        possible_edges = [
            (source, target)
            for source in vertices
            for target in vertices
        ]
        sampled_edge_sets = [
            [],
            possible_edges[::2],
            possible_edges[1::3],
            possible_edges[::4],
            possible_edges,
        ]
        nonempty_sections = [
            set(combination)
            for size in range(1, 5)
            for combination in itertools.combinations(vertices, size)
        ]

        for edges in sampled_edge_sets:
            for smaller in nonempty_sections:
                for larger in nonempty_sections:
                    if not smaller.issubset(larger):
                        continue
                    for added_vertex in set(vertices) - larger:
                        self.assertTrue(
                            diminishing_returns_check(
                                vertices,
                                edges,
                                smaller,
                                larger,
                                added_vertex,
                            )
                        )

            for first in nonempty_sections:
                for second in nonempty_sections:
                    self.assertGreaterEqual(
                        submodularity_defect(
                            vertices, edges, first, second
                        ),
                        0,
                    )

    def test_explicit_three_way_overlap_corrects_pair_overcount(self):
        vertices = [0, 1, 2, 3]
        edges = [(0, 3), (1, 3), (2, 3)]
        section = [0, 1, 2]
        spectrum = overlap_spectrum(vertices, edges, section)
        self.assertEqual(spectrum, (3, 3, 1))
        self.assertEqual(collision_from_overlap_spectrum(spectrum), 2)
        self.assertEqual(collision_excess(vertices, edges, section), 2)
        self.assertEqual(
            k_way_successor_overlap(vertices, edges, section, 2), 3
        )
        self.assertEqual(
            k_way_successor_overlap(vertices, edges, section, 3), 1
        )

    def test_reference_module_has_no_float_or_true_division(self):
        tree = ast.parse(inspect.getsource(overlap))
        float_constants = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.Constant) and isinstance(node.value, float)
        ]
        true_divisions = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div)
        ]
        self.assertEqual(float_constants, [])
        self.assertEqual(true_divisions, [])


if __name__ == "__main__":
    unittest.main()
