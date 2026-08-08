import ast
import inspect
import itertools
import unittest

import enterprise_math.focusing_concentration as concentration
from enterprise_math.focusing_concentration import (
    focusing_profile,
    higher_order_concentration,
    pairwise_regime_reconstruction,
    quadratic_focusing_concentration,
)


class FocusingConcentrationTests(unittest.TestCase):
    def test_higher_order_concentration_identity_and_zero_criterion(self):
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
                    profile = focusing_profile(vertices, edges, section)
                    higher = profile["higher_order_concentration"]
                    maximum = profile["maximum_target_multiplicity"]
                    self.assertEqual(higher == 0, maximum <= 2)
                    self.assertEqual(
                        quadratic_focusing_concentration(vertices, edges, section),
                        2 * profile["collision_spectrum"][1]
                        - profile["collision_excess"]
                        if len(profile["collision_spectrum"]) >= 2
                        else 0,
                    )

    def test_same_coarse_focusing_different_spectrum_minimal_three_source_pair(self):
        vertices = [0, 1, 2, 3, 4]
        section = [0, 1, 2]

        diffuse_edges = [(0, 3), (1, 3), (0, 4), (2, 4)]
        deep_edges = [(0, 3), (1, 3), (2, 3), (0, 4)]

        diffuse = focusing_profile(vertices, diffuse_edges, section)
        deep = focusing_profile(vertices, deep_edges, section)

        for field in (
            "section_size",
            "branching_surplus",
            "collision_excess",
            "expansion",
        ):
            self.assertEqual(diffuse[field], deep[field])

        self.assertEqual(diffuse["section_size"], 3)
        self.assertEqual(diffuse["branching_surplus"], 1)
        self.assertEqual(diffuse["collision_excess"], 2)
        self.assertEqual(diffuse["expansion"], -1)

        self.assertEqual(diffuse["collision_spectrum"][:3], (4, 2, 0))
        self.assertEqual(deep["collision_spectrum"][:3], (4, 3, 1))
        self.assertEqual(diffuse["higher_order_concentration"], 0)
        self.assertEqual(deep["higher_order_concentration"], 1)
        self.assertEqual(diffuse["quadratic_focusing_concentration"], 2)
        self.assertEqual(deep["quadratic_focusing_concentration"], 4)

    def test_at_most_two_sources_coarse_data_reconstruct_multiplicity_counts(self):
        for section_size in (1, 2):
            vertices = list(range(4))
            section = list(range(section_size))
            possible_edges = [
                (source, target)
                for source in section
                for target in vertices
            ]
            for edge_mask in range(1 << len(possible_edges)):
                edges = [
                    edge
                    for index, edge in enumerate(possible_edges)
                    if edge_mask & (1 << index)
                ]
                profile = focusing_profile(vertices, edges, section)
                reconstructed = pairwise_regime_reconstruction(
                    section_size,
                    profile["branching_surplus"],
                    profile["collision_excess"],
                )
                multiplicities = {}
                for source, target in edges:
                    multiplicities[target] = multiplicities.get(target, 0) + 1
                actual_single = sum(value == 1 for value in multiplicities.values())
                actual_double = sum(value == 2 for value in multiplicities.values())
                self.assertEqual(reconstructed["single_targets"], actual_single)
                self.assertEqual(reconstructed["double_targets"], actual_double)

    def test_three_sources_are_first_possible_higher_order_regime(self):
        vertices = list(range(5))
        for section_size in (1, 2):
            section = list(range(section_size))
            possible_edges = [
                (source, target)
                for source in section
                for target in vertices
            ]
            for edge_mask in range(1 << len(possible_edges)):
                edges = [
                    edge
                    for index, edge in enumerate(possible_edges)
                    if edge_mask & (1 << index)
                ]
                self.assertEqual(
                    higher_order_concentration(vertices, edges, section),
                    0,
                )

        section = [0, 1, 2]
        edges = [(0, 3), (1, 3), (2, 3)]
        self.assertGreater(
            higher_order_concentration(vertices, edges, section),
            0,
        )

    def test_quadratic_concentration_is_sum_of_squared_excess_multiplicity(self):
        vertices = [0, 1, 2, 3, 4, 5]
        section = [0, 1, 2]
        edges = [(0, 3), (1, 3), (2, 3), (0, 4), (1, 5)]
        profile = focusing_profile(vertices, edges, section)
        self.assertEqual(profile["quadratic_focusing_concentration"], 4)
        self.assertEqual(profile["higher_order_concentration"], 1)

    def test_reference_module_has_no_float_or_true_division(self):
        tree = ast.parse(inspect.getsource(concentration))
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
