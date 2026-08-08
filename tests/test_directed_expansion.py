import ast
import inspect
import itertools
import unittest

import enterprise_math.directed_expansion as directed
from enterprise_math.directed_expansion import (
    branching_collision_decomposition,
    branching_surplus,
    collision_excess,
    expansion_trajectory,
    future_section,
    local_collision_spectrum,
    section_expansion,
    successor_multiplicities,
    telescoping_expansion_check,
    union_expansion_identity,
)


class DirectedExpansionTests(unittest.TestCase):
    def setUp(self):
        self.vertices = list(range(8))
        self.edges = [
            (0, 3),
            (0, 4),
            (1, 4),
            (1, 5),
            (2, 5),
            (2, 6),
            (3, 7),
            (4, 7),
            (5, 7),
            (6, 7),
        ]

    def test_future_section_is_distinct_reachability(self):
        self.assertEqual(future_section(self.vertices, self.edges, [0, 1, 2]), frozenset((3, 4, 5, 6)))
        self.assertEqual(section_expansion(self.vertices, self.edges, [0, 1, 2]), 1)

    def test_branching_minus_collision_equals_expansion(self):
        section = [0, 1, 2]
        self.assertEqual(branching_surplus(self.vertices, self.edges, section), 3)
        self.assertEqual(collision_excess(self.vertices, self.edges, section), 2)
        self.assertEqual(
            branching_collision_decomposition(self.vertices, self.edges, section),
            {"expansion": 1, "branching_surplus": 3, "collision_excess": 2},
        )

    def test_successor_multiplicity_and_collision_spectrum(self):
        multiplicities = successor_multiplicities(self.vertices, self.edges, [0, 1, 2])
        self.assertEqual(multiplicities, {3: 1, 4: 2, 5: 2, 6: 1})
        self.assertEqual(local_collision_spectrum(self.vertices, self.edges, [0, 1, 2], 2), 2)
        self.assertEqual(local_collision_spectrum(self.vertices, self.edges, [0, 1, 2], 3), 0)

    def test_marginal_expansion_is_exact_branch_collision_balance(self):
        vertices = [0, 1, 2, 3]
        edges = [(0, 2), (0, 3), (1, 3)]
        data = branching_collision_decomposition(vertices, edges, [0, 1])
        self.assertEqual(data["branching_surplus"], 1)
        self.assertEqual(data["collision_excess"], 1)
        self.assertEqual(data["expansion"], 0)

    def test_contraction_when_collision_exceeds_branching(self):
        vertices = [0, 1, 2]
        edges = [(0, 2), (1, 2)]
        data = branching_collision_decomposition(vertices, edges, [0, 1])
        self.assertEqual(data["branching_surplus"], 0)
        self.assertEqual(data["collision_excess"], 1)
        self.assertEqual(data["expansion"], -1)

    def test_union_expansion_overlap_identity_exhaustively(self):
        vertices = list(range(5))
        possible_edges = [(source, target) for source in vertices for target in vertices]
        sampled_graphs = [
            [],
            possible_edges[::5],
            possible_edges[1::4],
            possible_edges[::3],
            possible_edges,
        ]
        nonempty_sections = [
            set(combination)
            for size in range(1, 4)
            for combination in itertools.combinations(vertices, size)
        ]
        for edges in sampled_graphs:
            for first in nonempty_sections:
                for second in nonempty_sections:
                    data = union_expansion_identity(vertices, edges, first, second)
                    self.assertEqual(
                        data["union_expansion"],
                        data["first_expansion"]
                        + data["second_expansion"]
                        + data["state_overlap"]
                        - data["future_overlap"],
                    )

    def test_trajectory_expansion_telescopes(self):
        sections, expansions = expansion_trajectory(self.vertices, self.edges, [0, 1, 2], 4)
        self.assertEqual([len(section) for section in sections], [3, 4, 1, 0])
        self.assertEqual(expansions, (1, -3, -1))
        self.assertTrue(telescoping_expansion_check(self.vertices, self.edges, [0, 1, 2], 4))
        self.assertEqual(sum(expansions), len(sections[-1]) - len(sections[0]))

    def test_reference_module_has_no_float_or_true_division(self):
        tree = ast.parse(inspect.getsource(directed))
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
