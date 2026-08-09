import unittest

from enterprise_math.admissible_support import analyze_admissible_support_family
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
