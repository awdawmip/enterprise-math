import itertools
import unittest

from enterprise_math.relation_path_count_branching_diagnostic import (
    BRANCHING,
    DETERMINISTIC,
    UNDEFINED,
    relation_source_count_diagnostics,
    relation_source_outdegrees,
    source_relation_class_from_count,
)
from enterprise_math.relation_predicate_transformer_diagnostic import (
    relation_predicate_transformer_diagnostic,
)


def all_relations(states):
    pairs = tuple(itertools.product(states, repeat=2))
    return tuple(
        frozenset(pair for bit, pair in zip(mask, pairs, strict=True) if bit)
        for mask in itertools.product((0, 1), repeat=len(pairs))
    )


class RelationPathCountBranchingDiagnosticTests(unittest.TestCase):
    def test_zero_one_many_successors_give_three_exact_classes(self):
        states = (0, 1, 2)
        relation = frozenset({
            (1, 0),
            (2, 0),
            (2, 1),
        })
        diagnostics = {
            item.source: item
            for item in relation_source_count_diagnostics(states, relation)
        }
        self.assertEqual(diagnostics[0].successor_count, 0)
        self.assertEqual(diagnostics[0].raw_class, UNDEFINED)
        self.assertFalse(diagnostics[0].boolean_defined)

        self.assertEqual(diagnostics[1].successor_count, 1)
        self.assertEqual(diagnostics[1].raw_class, DETERMINISTIC)
        self.assertTrue(diagnostics[1].boolean_defined)

        self.assertEqual(diagnostics[2].successor_count, 2)
        self.assertEqual(diagnostics[2].raw_class, BRANCHING)
        self.assertTrue(diagnostics[2].boolean_defined)

    def test_boolean_definedness_is_exact_positivity_quotient_of_outdegree(self):
        states = (0, 1)
        for relation in all_relations(states):
            diagnostics = relation_source_count_diagnostics(states, relation)
            predicate = relation_predicate_transformer_diagnostic(states, relation)
            undefined = predicate.undefined_sources
            branching = predicate.branching_sources
            for item in diagnostics:
                self.assertEqual(
                    item.boolean_defined,
                    item.source not in undefined,
                )
                self.assertEqual(
                    item.raw_class == BRANCHING,
                    item.source in branching,
                )
                self.assertEqual(
                    item.raw_class == DETERMINISTIC,
                    item.source not in undefined and item.source not in branching,
                )

    def test_outdegree_vector_is_raw_branch_multiplicity(self):
        states = ("a", "b", "c")
        relation = frozenset({
            ("a", "a"),
            ("a", "b"),
            ("a", "c"),
            ("b", "c"),
        })
        self.assertEqual(
            relation_source_outdegrees(states, relation),
            (("a", 3), ("b", 1), ("c", 0)),
        )

    def test_validation(self):
        with self.assertRaises(ValueError):
            relation_source_outdegrees((), frozenset())
        with self.assertRaises(ValueError):
            relation_source_outdegrees((0, 0), frozenset())
        with self.assertRaises(ValueError):
            relation_source_outdegrees((0, 1), frozenset({(0, 2)}))
        with self.assertRaises(ValueError):
            source_relation_class_from_count(-1)
        with self.assertRaises(ValueError):
            source_relation_class_from_count(False)


if __name__ == "__main__":
    unittest.main()
