import itertools
import unittest

from enterprise_math.relation_predicate_transformer_diagnostic import (
    existential_preimage,
    predicate_transformer_preserves_all_meets,
    predicate_transformer_preserves_top,
    relation_predicate_transformer_diagnostic,
    singleton_meet_branch_witness,
)


def all_relations(states):
    pairs = tuple(itertools.product(states, repeat=2))
    return tuple(
        frozenset(pair for bit, pair in zip(mask, pairs, strict=True) if bit)
        for mask in itertools.product((0, 1), repeat=len(pairs))
    )


def direct_targets(states, relation):
    result = {state: set() for state in states}
    for source, target in relation:
        result[source].add(target)
    return result


class RelationPredicateTransformerDiagnosticTests(unittest.TestCase):
    def test_four_domain_relation_quadrants(self):
        states = (0, 1, 2)

        total_deterministic = frozenset({
            (0, 1),
            (1, 1),
            (2, 0),
        })
        report = relation_predicate_transformer_diagnostic(
            states,
            total_deterministic,
        )
        self.assertTrue(report.preserves_top)
        self.assertTrue(report.preserves_all_meets)
        self.assertTrue(report.total_deterministic)

        partial_deterministic = frozenset({
            (0, 1),
            (2, 0),
        })
        report = relation_predicate_transformer_diagnostic(
            states,
            partial_deterministic,
        )
        self.assertFalse(report.preserves_top)
        self.assertTrue(report.preserves_all_meets)
        self.assertEqual(report.undefined_sources, frozenset({1}))
        self.assertTrue(report.functional)

        total_branching = frozenset({
            (0, 1),
            (0, 2),
            (1, 1),
            (2, 2),
        })
        report = relation_predicate_transformer_diagnostic(
            states,
            total_branching,
        )
        self.assertTrue(report.preserves_top)
        self.assertFalse(report.preserves_all_meets)
        self.assertEqual(report.branching_sources, frozenset({0}))
        self.assertTrue(report.total)

        partial_branching = frozenset({
            (0, 1),
            (0, 2),
        })
        report = relation_predicate_transformer_diagnostic(
            states,
            partial_branching,
        )
        self.assertFalse(report.preserves_top)
        self.assertFalse(report.preserves_all_meets)
        self.assertEqual(report.undefined_sources, frozenset({1, 2}))
        self.assertEqual(report.branching_sources, frozenset({0}))

    def test_all_two_state_relations_match_direct_totality_and_functionality(self):
        states = (0, 1)
        for relation in all_relations(states):
            targets = direct_targets(states, relation)
            expected_total = all(targets[state] for state in states)
            expected_functional = all(len(targets[state]) <= 1 for state in states)
            report = relation_predicate_transformer_diagnostic(states, relation)
            self.assertEqual(report.preserves_top, expected_total, relation)
            self.assertEqual(
                report.preserves_all_meets,
                expected_functional,
                relation,
            )
            self.assertEqual(report.total, expected_total)
            self.assertEqual(report.functional, expected_functional)

    def test_branching_source_has_singleton_meet_counterexample(self):
        states = (0, 1, 2)
        relation = frozenset({(0, 1), (0, 2), (1, 1)})
        witness = singleton_meet_branch_witness(states, relation)
        self.assertIsNotNone(witness)
        assert witness is not None
        source, left_target, right_target = witness
        self.assertNotEqual(left_target, right_target)

        left = frozenset({left_target})
        right = frozenset({right_target})
        lhs = existential_preimage(states, relation, left & right)
        rhs = (
            existential_preimage(states, relation, left)
            & existential_preimage(states, relation, right)
        )
        self.assertNotIn(source, lhs)
        self.assertIn(source, rhs)
        self.assertFalse(predicate_transformer_preserves_all_meets(states, relation))

    def test_join_and_bottom_preservation_hold_for_branching_partial_relation(self):
        states = (0, 1, 2)
        relation = frozenset({(0, 1), (0, 2)})
        predicates = tuple(
            frozenset(subset)
            for size in range(4)
            for subset in itertools.combinations(states, size)
        )
        self.assertEqual(
            existential_preimage(states, relation, ()),
            frozenset(),
        )
        for left in predicates:
            for right in predicates:
                self.assertEqual(
                    existential_preimage(states, relation, left | right),
                    existential_preimage(states, relation, left)
                    | existential_preimage(states, relation, right),
                )

    def test_top_defect_is_exact_undefined_source_set(self):
        states = (0, 1, 2)
        relation = frozenset({(0, 1), (2, 1)})
        domain = existential_preimage(states, relation, states)
        self.assertEqual(states.__class__(states) if False else domain, frozenset({0, 2}))
        self.assertFalse(predicate_transformer_preserves_top(states, relation))
        report = relation_predicate_transformer_diagnostic(states, relation)
        self.assertEqual(frozenset(states) - domain, report.undefined_sources)

    def test_validation(self):
        with self.assertRaises(ValueError):
            existential_preimage((), frozenset(), ())
        with self.assertRaises(ValueError):
            existential_preimage((0, 1), frozenset({(0, 1)}), (2,))
        with self.assertRaises(ValueError):
            relation_predicate_transformer_diagnostic(
                (0, 1),
                frozenset({(0, 2)}),
            )


if __name__ == "__main__":
    unittest.main()
