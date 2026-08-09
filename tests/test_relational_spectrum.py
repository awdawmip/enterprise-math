import itertools
import unittest

from enterprise_math.relational_spectrum import (
    function_collision_spectrum,
    function_graph_relation,
    postcompose_targets,
    relation_group_collision_spectrum,
    relation_overlap_spectrum,
)


class RelationalSpectrumTests(unittest.TestCase):
    def test_every_small_function_specializes_exactly(self):
        size = 4
        sources = tuple(range(size))
        for values in itertools.product(range(size), repeat=size):
            mapping = dict(zip(sources, values, strict=True))
            relation = function_graph_relation(mapping)
            expected = function_collision_spectrum(mapping, max_order=size)
            self.assertEqual(
                relation_overlap_spectrum(relation, max_order=size), expected
            )
            self.assertEqual(
                relation_group_collision_spectrum(
                    sources, relation, max_order=size
                ),
                expected,
            )

    def test_functional_order_one_is_domain_size(self):
        mapping = {0: "a", 1: "a", 2: "b", 3: "c", 4: "c"}
        spectrum = dict(
            relation_overlap_spectrum(function_graph_relation(mapping), max_order=5)
        )
        self.assertEqual(spectrum[1], len(mapping))
        self.assertEqual(spectrum[2], 2)

    def test_multivalued_relation_can_create_nontransitive_pair_support(self):
        relation = frozenset(
            {
                ("a", "x"),
                ("b", "x"),
                ("b", "y"),
                ("c", "y"),
            }
        )
        witness = dict(relation_overlap_spectrum(relation, max_order=3))
        groups = dict(
            relation_group_collision_spectrum(
                ("a", "b", "c"), relation, max_order=3
            )
        )
        self.assertEqual(witness, {1: 4, 2: 2, 3: 0})
        self.assertEqual(groups, {1: 3, 2: 2, 3: 0})

    def test_witness_and_group_spectra_split_on_multiple_shared_targets(self):
        relation = frozenset(
            {
                ("a", "x"),
                ("a", "y"),
                ("b", "x"),
                ("b", "y"),
            }
        )
        witness = dict(relation_overlap_spectrum(relation, max_order=2))
        groups = dict(
            relation_group_collision_spectrum(("a", "b"), relation, max_order=2)
        )
        self.assertEqual(witness, {1: 4, 2: 2})
        self.assertEqual(groups, {1: 2, 2: 1})

    def test_target_postcomposition_can_reduce_witness_count_without_losing_group(self):
        relation = frozenset(
            {
                ("a", "x"),
                ("a", "y"),
                ("b", "x"),
                ("b", "y"),
            }
        )
        merged = postcompose_targets(relation, {"x": "z", "y": "z"})
        old_witness = dict(relation_overlap_spectrum(relation, max_order=2))
        new_witness = dict(relation_overlap_spectrum(merged, max_order=2))
        old_groups = dict(
            relation_group_collision_spectrum(("a", "b"), relation, max_order=2)
        )
        new_groups = dict(
            relation_group_collision_spectrum(("a", "b"), merged, max_order=2)
        )
        self.assertGreater(old_witness[2], new_witness[2])
        self.assertEqual(old_groups[2], new_groups[2])

    def test_group_collision_spectrum_is_monotone_under_target_postcomposition(self):
        sources = (0, 1, 2)
        targets = ("x", "y")
        all_pairs = tuple(itertools.product(sources, targets))
        for mask in range(1 << len(all_pairs)):
            relation = frozenset(
                pair
                for index, pair in enumerate(all_pairs)
                if mask & (1 << index)
            )
            old = dict(
                relation_group_collision_spectrum(sources, relation, max_order=3)
            )
            for values in itertools.product((0, 1), repeat=len(targets)):
                target_map = dict(zip(targets, values, strict=True))
                updated = postcompose_targets(relation, target_map)
                new = dict(
                    relation_group_collision_spectrum(
                        sources, updated, max_order=3
                    )
                )
                for order in range(1, 4):
                    self.assertGreaterEqual(new[order], old[order])

    def test_target_postcomposition_can_create_new_collision_groups(self):
        relation = frozenset({("a", "x"), ("b", "y")})
        merged = postcompose_targets(relation, {"x": "z", "y": "z"})
        old = dict(
            relation_group_collision_spectrum(("a", "b"), relation, max_order=2)
        )
        new = dict(
            relation_group_collision_spectrum(("a", "b"), merged, max_order=2)
        )
        self.assertEqual(old[2], 0)
        self.assertEqual(new[2], 1)

    def test_one_source_can_contribute_multiple_order_one_memberships(self):
        relation = frozenset({("a", 1), ("a", 2), ("b", 2)})
        witness = dict(relation_overlap_spectrum(relation, max_order=2))
        groups = dict(
            relation_group_collision_spectrum(("a", "b"), relation, max_order=2)
        )
        self.assertEqual(witness[1], 3)
        self.assertEqual(groups[1], 2)
        self.assertEqual(witness[2], groups[2])

    def test_zero_max_order_is_empty(self):
        self.assertEqual(relation_overlap_spectrum(frozenset(), max_order=0), ())
        self.assertEqual(
            relation_group_collision_spectrum((), frozenset(), max_order=0), ()
        )


if __name__ == "__main__":
    unittest.main()
