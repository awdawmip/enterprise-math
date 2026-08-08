import ast
import inspect
import unittest

import enterprise_math.directional_focusing as directional
from enterprise_math.directional_focusing import (
    causal_phase_role,
    causal_role_channels,
    collision_rate_anisotropy_numerator,
    direction_resolution_no_go,
    directional_channel_data,
    incidence_orbits,
    orbit_causal_phase_role,
    pair_collision_channel_decomposition,
    phase_marked_direction_roles,
    section_stabilizer_automorphisms,
)


class DirectionalFocusingTests(unittest.TestCase):
    def test_section_stabilizer_orbits_separate_private_and_common_future_channels(self):
        vertices = ["a", "b", "x", "y", "z"]
        edges = [("a", "x"), ("b", "y"), ("a", "z"), ("b", "z")]
        section = ["a", "b"]
        automorphisms = section_stabilizer_automorphisms(vertices, edges, section)
        channels = incidence_orbits(vertices, edges, section, automorphisms)
        channel_sets = {frozenset(channel) for channel in channels}
        self.assertEqual(
            channel_sets,
            {
                frozenset({("a", "x"), ("b", "y")}),
                frozenset({("a", "z"), ("b", "z")}),
            },
        )
        data = sorted(
            (directional_channel_data(channel) for channel in channels),
            key=lambda item: int(item["collision_excess"]),
        )
        self.assertEqual([item["collision_excess"] for item in data], [0, 1])
        self.assertEqual(collision_rate_anisotropy_numerator(channels), 4)
        self.assertFalse(direction_resolution_no_go(channels))

    def test_edge_transitive_unmarked_structure_has_one_direction_orbit(self):
        vertices = ["a", "b", "x", "y"]
        edges = [("a", "x"), ("b", "y")]
        channels = incidence_orbits(vertices, edges, ["a", "b"])
        self.assertEqual(len(channels), 1)
        self.assertTrue(direction_resolution_no_go(channels))
        self.assertEqual(collision_rate_anisotropy_numerator(channels), 0)

    def test_causal_phase_marks_can_refine_an_unmarked_transitive_orbit(self):
        vertices = ["a", "b", "x", "y"]
        edges = [("a", "x"), ("b", "y")]
        section = ["a", "b"]
        unmarked = incidence_orbits(vertices, edges, section)
        marks = {"a": 0, "b": 0, "x": 1, "y": -1}
        marked = incidence_orbits(vertices, edges, section, marks=marks)
        self.assertEqual(len(unmarked), 1)
        self.assertEqual(len(marked), 2)
        self.assertEqual(
            {frozenset(channel) for channel in marked},
            {frozenset({("a", "x")}), frozenset({("b", "y")})},
        )

    def test_phase_roles_are_coordinate_free_transition_labels(self):
        marks = {"a": 0, "b": 1, "x": -1, "y": 1}
        self.assertEqual(causal_phase_role(("a", "x"), marks), (0, -1))
        self.assertEqual(causal_phase_role(("b", "y"), marks), (1, 1))

    def test_causal_role_channels_group_exact_phase_transitions(self):
        vertices = ["a", "b", "x", "y", "z"]
        edges = [("a", "x"), ("a", "y"), ("b", "y"), ("b", "z")]
        marks = {"a": 0, "b": 0, "x": -1, "y": 0, "z": 1}
        channels = causal_role_channels(vertices, edges, ["a", "b"], marks)
        self.assertEqual(
            channels,
            {
                (0, -1): (("a", "x"),),
                (0, 0): (("a", "y"), ("b", "y")),
                (0, 1): (("b", "z"),),
            },
        )

    def test_marked_direction_orbit_cannot_mix_causal_roles(self):
        vertices = ["a", "b", "x", "y"]
        edges = [("a", "x"), ("b", "y")]
        marks = {"a": 0, "b": 0, "x": 1, "y": -1}
        resolved = phase_marked_direction_roles(vertices, edges, ["a", "b"], marks)
        self.assertEqual({item["role"] for item in resolved}, {(0, 1), (0, -1)})
        for item in resolved:
            self.assertEqual(orbit_causal_phase_role(item["orbit"], marks), item["role"])

    def test_same_causal_role_may_still_contain_multiple_direction_orbits(self):
        vertices = ["a", "b", "x", "y", "z"]
        edges = [("a", "x"), ("b", "y"), ("a", "z"), ("b", "z")]
        marks = {vertex: 0 for vertex in vertices}
        resolved = phase_marked_direction_roles(vertices, edges, ["a", "b"], marks)
        self.assertEqual({item["role"] for item in resolved}, {(0, 0)})
        self.assertEqual(len(resolved), 2)

    def test_pair_collision_splits_into_internal_and_cross_channel_terms(self):
        first = [("a", "x"), ("b", "z")]
        second = [("a", "z"), ("b", "x")]
        data = pair_collision_channel_decomposition([first, second])
        self.assertEqual(data["total_j2"], 2)
        self.assertEqual(data["internal_j2"], (0, 0))
        self.assertEqual(sum(data["cross_j2"].values()), 2)

    def test_fraction_free_anisotropy_zero_iff_channel_collision_rates_match(self):
        equal_rate = [
            [(0, "x"), (1, "x")],
            [(2, "y"), (3, "y")],
        ]
        unequal_rate = [
            [(0, "x"), (1, "x")],
            [(2, "y"), (3, "z")],
        ]
        self.assertEqual(collision_rate_anisotropy_numerator(equal_rate), 0)
        self.assertGreater(collision_rate_anisotropy_numerator(unequal_rate), 0)

    def test_supplied_non_automorphism_is_rejected(self):
        vertices = [0, 1, 2]
        edges = [(0, 2), (1, 2)]
        bad = {0: 2, 1: 1, 2: 0}
        with self.assertRaises(ValueError):
            incidence_orbits(vertices, edges, [0, 1], [bad])

    def test_marks_must_cover_every_vertex(self):
        vertices = [0, 1, 2]
        edges = [(0, 2), (1, 2)]
        with self.assertRaises(ValueError):
            incidence_orbits(vertices, edges, [0, 1], marks={0: 0, 1: 0})

    def test_phase_marks_are_typed(self):
        vertices = [0, 1]
        edges = [(0, 1)]
        with self.assertRaises(ValueError):
            causal_role_channels(vertices, edges, [0], {0: 0, 1: 2})

    def test_reference_module_has_no_float_or_true_division(self):
        tree = ast.parse(inspect.getsource(directional))
        floats = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.Constant) and isinstance(node.value, float)
        ]
        divisions = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div)
        ]
        self.assertEqual(floats, [])
        self.assertEqual(divisions, [])


if __name__ == "__main__":
    unittest.main()
