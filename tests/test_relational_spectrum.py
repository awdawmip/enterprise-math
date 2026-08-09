import unittest

from enterprise_math.relational_spectrum import (
    function_collision_spectrum,
    function_graph_relation,
    postcompose_targets,
    relation_group_collision_spectrum,
    relation_overlap_spectrum,
    relation_source_supports,
    relation_target_occupancies,
)


class RelationalSpectrumTests(unittest.TestCase):
    def test_function_graph_degenerates_exactly_to_p011_fiber_formula(self):
        mapping = {0: "a", 1: "a", 2: "b", 3: "a", 4: "c"}
        relation = function_graph_relation(mapping)
        sources = tuple(mapping)
        witness = relation_overlap_spectrum(relation, max_order=5)
        groups = relation_group_collision_spectrum(sources, relation, max_order=5)
        direct = function_collision_spectrum(mapping, max_order=5)
        self.assertEqual(witness, direct)
        self.assertEqual(groups, direct)

    def test_multivalued_relation_splits_witness_and_group_spectra(self):
        sources = ("a", "b", "c")
        relation = frozenset(
            {
                ("a", "x"),
                ("b", "x"),
                ("a", "y"),
                ("b", "y"),
                ("c", "z"),
            }
        )
        witness = dict(relation_overlap_spectrum(relation, max_order=3))
        groups = dict(relation_group_collision_spectrum(sources, relation, max_order=3))
        self.assertEqual(witness[2], 2)
        self.assertEqual(groups[2], 1)
        self.assertGreater(witness[2], groups[2])

    def test_group_spectrum_cannot_decrease_under_deterministic_postcomposition(self):
        sources = (0, 1, 2)
        relation = frozenset(
            {
                (0, "a"),
                (1, "a"),
                (1, "b"),
                (2, "b"),
            }
        )
        before = dict(relation_group_collision_spectrum(sources, relation, max_order=3))
        after_relation = postcompose_targets(relation, {"a": "q", "b": "q"})
        after = dict(relation_group_collision_spectrum(sources, after_relation, max_order=3))
        for order in before:
            self.assertGreaterEqual(after[order], before[order])

    def test_witness_spectrum_can_decrease_when_targets_merge(self):
        relation = frozenset(
            {
                (0, "a"),
                (1, "a"),
                (0, "b"),
                (1, "b"),
            }
        )
        before = dict(relation_overlap_spectrum(relation, max_order=2))
        merged = postcompose_targets(relation, {"a": "q", "b": "q"})
        after = dict(relation_overlap_spectrum(merged, max_order=2))
        self.assertEqual(before[2], 2)
        self.assertEqual(after[2], 1)

    def test_support_and_occupancy_helpers(self):
        relation = frozenset({("a", 1), ("a", 2), ("b", 2)})
        self.assertEqual(relation_target_occupancies(relation), {1: 1, 2: 2})
        supports = relation_source_supports(("a", "b", "c"), relation)
        self.assertEqual(supports["a"], frozenset({1, 2}))
        self.assertEqual(supports["b"], frozenset({2}))
        self.assertEqual(supports["c"], frozenset())

    def test_undeclared_source_rejected(self):
        with self.assertRaises(ValueError):
            relation_source_supports(("a",), frozenset({("b", 1)}))


if __name__ == "__main__":
    unittest.main()
