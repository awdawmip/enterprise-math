import unittest

from enterprise_math.admissible_support import (
    analyze_admissible_support_family,
    common_target_relation,
    compose_relations,
    converse_relation,
)


class AdmissibleSupportTests(unittest.TestCase):
    def test_path_ball_family_is_split_complete(self):
        states = frozenset({0, 1, 2})
        identity = frozenset((x, x) for x in states)
        radius_one = identity | frozenset(
            {(0, 1), (1, 0), (1, 2), (2, 1)}
        )
        radius_two = frozenset((x, y) for x in states for y in states)
        report = analyze_admissible_support_family(
            states, {0: identity, 1: radius_one, 2: radius_two}
        )
        self.assertTrue(report.zero_identity)
        self.assertTrue(report.monotone)
        self.assertTrue(report.subadditive)
        self.assertTrue(report.split_complete)
        self.assertEqual(compose_relations(radius_one, radius_one), radius_two)

    def test_basic_contract_does_not_imply_split_completeness(self):
        states = frozenset({0, 1, 2})
        identity = frozenset((x, x) for x in states)
        radius_two = identity | frozenset({(0, 2), (2, 0)})
        report = analyze_admissible_support_family(
            states, {0: identity, 1: identity, 2: radius_two}
        )
        self.assertTrue(report.zero_identity)
        self.assertTrue(report.monotone)
        self.assertTrue(report.subadditive)
        self.assertFalse(report.split_complete)
        self.assertEqual(compose_relations(identity, identity), identity)
        self.assertNotEqual(identity, radius_two)

    def test_common_target_relation_is_composition_with_converse(self):
        left = frozenset({("a", "x"), ("a", "y"), ("b", "z")})
        right = frozenset({("c", "y"), ("d", "z"), ("e", "q")})
        expected = frozenset({("a", "c"), ("b", "d")})
        self.assertEqual(converse_relation(right), frozenset({("y", "c"), ("z", "d"), ("q", "e")}))
        self.assertEqual(common_target_relation(left, right), expected)

    def test_invalid_family_rejected(self):
        with self.assertRaises(ValueError):
            analyze_admissible_support_family(frozenset(), {0: frozenset()})
        with self.assertRaises(ValueError):
            analyze_admissible_support_family(frozenset({0}), {1: frozenset()})
        with self.assertRaises(ValueError):
            analyze_admissible_support_family(
                frozenset({0}), {0: frozenset({(0, 1)})}
            )


if __name__ == "__main__":
    unittest.main()
