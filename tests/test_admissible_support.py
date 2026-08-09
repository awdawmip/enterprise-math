import unittest

from enterprise_math.admissible_support import (
    analyze_admissible_support_family,
    common_target_relation,
    converse_relation,
)
from enterprise_math.intrinsic_collapse import graph_collapse_targets
from enterprise_math.weighted_collapse import weighted_radius_relation


class AdmissibleSupportTests(unittest.TestCase):
    def test_unit_step_graph_family_is_split_complete(self):
        graph = {
            0: {1},
            1: {0, 2, 3},
            2: {1, 3},
            3: {1, 2, 4},
            4: {3},
        }
        states = frozenset(graph)
        relations = {
            radius: frozenset(
                (center, target)
                for center in graph
                for target in graph_collapse_targets(graph, center, radius)
            )
            for radius in range(7)
        }
        report = analyze_admissible_support_family(states, relations)
        self.assertTrue(report.zero_identity)
        self.assertTrue(report.monotone)
        self.assertTrue(report.subadditive)
        self.assertTrue(report.split_complete)

        for left_radius in range(4):
            for right_radius in range(4):
                collision = common_target_relation(
                    relations[left_radius], relations[right_radius]
                )
                self.assertEqual(collision, relations[left_radius + right_radius])

    def test_atomic_weighted_family_is_admissible_but_not_split_complete(self):
        graph = {
            "a": {"b": 2},
            "b": {"a": 2},
        }
        relations = {radius: weighted_radius_relation(graph, radius) for radius in range(5)}
        report = analyze_admissible_support_family(frozenset(graph), relations)
        self.assertTrue(report.zero_identity)
        self.assertTrue(report.monotone)
        self.assertTrue(report.subadditive)
        self.assertFalse(report.split_complete)
        self.assertNotEqual(
            common_target_relation(relations[1], relations[1]), relations[2]
        )

    def test_common_target_relation_is_well_defined_for_directed_support(self):
        # a and b can both reach future target z even though neither can reach
        # the other and the support relation is not symmetric.
        directed = frozenset(
            {
                ("a", "a"),
                ("b", "b"),
                ("z", "z"),
                ("a", "z"),
                ("b", "z"),
            }
        )
        collision = common_target_relation(directed, directed)
        self.assertIn(("a", "b"), collision)
        self.assertIn(("b", "a"), collision)
        self.assertNotEqual(directed, converse_relation(directed))

    def test_mixed_radius_common_target_relations_reverse_correctly(self):
        left = frozenset({("a", "z"), ("a", "u"), ("b", "u")})
        right = frozenset({("c", "z"), ("d", "u")})
        forward = common_target_relation(left, right)
        backward = common_target_relation(right, left)
        self.assertEqual(converse_relation(forward), backward)

    def test_bad_nonmonotone_family_is_detected(self):
        states = frozenset({0, 1})
        identity = frozenset({(0, 0), (1, 1)})
        relations = {
            0: identity,
            1: frozenset({(0, 0), (1, 1), (0, 1)}),
            2: identity,
        }
        report = analyze_admissible_support_family(states, relations)
        self.assertFalse(report.monotone)

    def test_bad_zero_relation_is_detected(self):
        states = frozenset({0, 1})
        report = analyze_admissible_support_family(
            states,
            {0: frozenset({(0, 0)}), 1: frozenset({(0, 0), (1, 1)})},
        )
        self.assertFalse(report.zero_identity)

    def test_external_states_are_rejected(self):
        with self.assertRaises(ValueError):
            analyze_admissible_support_family(
                frozenset({0, 1}),
                {0: frozenset({(0, 0), (1, 1), (0, 2)})},
            )


if __name__ == "__main__":
    unittest.main()
