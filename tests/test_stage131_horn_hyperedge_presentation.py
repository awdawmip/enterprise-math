import unittest

from enterprise_math.stage131_horn_hyperedge_presentation import (
    HornRule,
    add_derived_horn_macros,
    and_tree_full_closure_rounds_closed,
    and_tree_macro_premise_literals_closed,
    and_tree_macro_rule_count_closed,
    and_tree_root_round_closed,
    and_tree_span_macros,
    and_tree_span_presentation_report,
    balanced_binary_and_tree,
    conjunction_projection_false_positive_witness,
    derived_macros_preserve_closure_exhaustive,
    horn_closure,
    horn_derivation_rounds,
    horn_full_closure_rounds,
    horn_target_round,
    naive_unary_projection,
    premise_literal_storage,
    rule_is_semantically_derived,
    rule_literal_storage,
    synchronous_horn_closure_sequence,
    unary_graph_closure,
)


class Stage131HornHyperedgePresentationTests(unittest.TestCase):
    def test_conjunctive_rule_cannot_be_projected_to_unary_graph_edges(self):
        rules, exact_from_a, projected_from_a = conjunction_projection_false_positive_witness()
        self.assertNotIn("c", exact_from_a)
        self.assertIn("c", projected_from_a)
        self.assertEqual(
            naive_unary_projection(rules),
            frozenset({("a", "c"), ("b", "c")}),
        )

    def test_horn_round_is_min_over_rules_of_one_plus_max_premise_round(self):
        rules = (
            HornRule(frozenset({"a"}), "p"),
            HornRule(frozenset({"b"}), "q"),
            HornRule(frozenset({"p", "q"}), "z"),
        )
        rounds = horn_derivation_rounds(rules, {"a", "b"})
        self.assertEqual(rounds["a"], 0)
        self.assertEqual(rounds["b"], 0)
        self.assertEqual(rounds["p"], 1)
        self.assertEqual(rounds["q"], 1)
        self.assertEqual(rounds["z"], 2)

        macro = HornRule(frozenset({"a", "b"}), "z")
        self.assertTrue(rule_is_semantically_derived(rules, macro))
        extended = add_derived_horn_macros(rules, (macro,))
        self.assertEqual(horn_target_round(extended, {"a", "b"}, "z"), 1)
        self.assertEqual(horn_closure(rules, {"a", "b"}), horn_closure(extended, {"a", "b"}))

    def test_derived_macro_preserves_closure_for_every_seed_subset(self):
        rules = (
            HornRule(frozenset({"a"}), "p"),
            HornRule(frozenset({"b"}), "q"),
            HornRule(frozenset({"p", "q"}), "z"),
        )
        macro = HornRule(frozenset({"a", "b"}), "z")
        self.assertTrue(derived_macros_preserve_closure_exhaustive(rules, (macro,)))

    def test_balanced_and_tree_local_basis_depth_equals_height(self):
        for height in range(1, 8):
            tree = balanced_binary_and_tree(height)
            self.assertEqual(len(tree.leaves), 1 << height)
            self.assertEqual(len(tree.local_rules), (1 << height) - 1)
            self.assertEqual(premise_literal_storage(tree.local_rules), 2 * ((1 << height) - 1))
            self.assertEqual(rule_literal_storage(tree.local_rules), 3 * ((1 << height) - 1))
            self.assertEqual(horn_target_round(tree.local_rules, tree.leaves, tree.root), height)
            self.assertEqual(horn_full_closure_rounds(tree.local_rules, tree.leaves), height)

    def test_span_macro_count_and_premise_literal_closed_forms(self):
        for height in range(1, 8):
            tree = balanced_binary_and_tree(height)
            for span in range(1, height + 1):
                macros = and_tree_span_macros(tree, span)
                self.assertEqual(
                    len(macros),
                    and_tree_macro_rule_count_closed(height, span),
                )
                self.assertEqual(
                    premise_literal_storage(macros),
                    and_tree_macro_premise_literals_closed(height, span),
                )
                self.assertTrue(
                    all(len(rule.premises) == (1 << span) for rule in macros)
                )

    def test_span_macro_root_and_full_closure_depth_formulas(self):
        for height in range(1, 8):
            for span in range(1, height + 1):
                report = and_tree_span_presentation_report(height, span)
                self.assertEqual(
                    report.root_round,
                    and_tree_root_round_closed(height, span),
                )
                self.assertEqual(
                    report.full_closure_rounds,
                    and_tree_full_closure_rounds_closed(height, span),
                )

    def test_giant_root_macro_is_one_round_readout_but_not_one_round_full_state(self):
        height = 8
        report = and_tree_span_presentation_report(height, height)
        self.assertEqual(report.macro_rule_count, 1)
        self.assertEqual(report.macro_premise_literals, 1 << height)
        self.assertEqual(report.root_round, 1)
        self.assertEqual(report.full_closure_rounds, height - 1)
        self.assertEqual(report.base_rule_count, (1 << height) - 1)

    def test_intermediate_span_trades_macro_count_width_and_depth(self):
        height = 8
        reports = {
            span: and_tree_span_presentation_report(height, span)
            for span in (1, 2, 4, 8)
        }
        # Span1 duplicates the local one-level update pattern and does not reduce depth.
        self.assertEqual(reports[1].full_closure_rounds, 8)
        # Wider macros lower root/full depth but use exponentially wider premises.
        self.assertLess(reports[2].root_round, reports[1].root_round)
        self.assertLess(reports[4].root_round, reports[2].root_round)
        self.assertEqual(reports[8].root_round, 1)
        self.assertGreater(1 << 8, 1 << 4)
        self.assertLess(reports[8].macro_rule_count, reports[4].macro_rule_count)

    def test_synchronous_sequence_matches_reported_full_rounds(self):
        tree = balanced_binary_and_tree(5)
        macros = and_tree_span_macros(tree, 2)
        extended = add_derived_horn_macros(tree.local_rules, macros)
        stages = synchronous_horn_closure_sequence(extended, tree.leaves)
        self.assertEqual(len(stages) - 1, and_tree_full_closure_rounds_closed(5, 2))
        self.assertIn(tree.root, stages[-1])

    def test_validation(self):
        with self.assertRaises(ValueError):
            HornRule(frozenset(), "x")
        with self.assertRaises(ValueError):
            balanced_binary_and_tree(0)
        with self.assertRaises(ValueError):
            and_tree_span_presentation_report(4, 5)


if __name__ == "__main__":
    unittest.main()
