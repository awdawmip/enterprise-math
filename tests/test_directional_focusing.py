import ast
import inspect
import unittest

import enterprise_math.directional_focusing as directional
from enterprise_math.directional_focusing import (
    collision_rate_anisotropy_numerator,
    direction_resolution_no_go,
    directional_channel_data,
    incidence_orbits,
    pair_collision_channel_decomposition,
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
