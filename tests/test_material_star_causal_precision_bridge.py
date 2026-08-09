import itertools
import unittest
from fractions import Fraction

from enterprise_math.material_star_causal_precision_bridge import (
    star_precision_causal_minimum_relation,
    star_precision_causal_report,
    star_precision_minimum_relation_is_fully_causal,
    star_q1_first_schedule_branch_certificate,
    star_q1_first_schedule_divergence_denominator,
)
from enterprise_math.material_star_local_action_language import (
    star_terminal_is_causally_reachable,
)
from enterprise_math.material_star_response_precision_phase import (
    star_minimum_response_relation_at_precision,
    star_response_refinement_phase,
    star_symmetric_minimum_numerators,
)


def independent_terminal_states(leaf_count, scaled_closing):
    start = (0,) * leaf_count
    seen = {start}
    stack = [start]
    terminal = set()
    while stack:
        state = stack.pop()
        total = sum(state)
        legal = [
            index
            for index, value in enumerate(state)
            if -scaled_closing + total + value < 0
        ]
        if not legal:
            terminal.add(state)
            continue
        for index in legal:
            updated = list(state)
            updated[index] += 1
            updated = tuple(updated)
            if updated not in seen:
                seen.add(updated)
                stack.append(updated)
    return terminal


class MaterialStarCausalPrecisionBridgeTests(unittest.TestCase):
    def test_precision_causal_minimum_filter_matches_direct_reachability(self):
        checked = 0
        for leaf_count in range(2, 7):
            for closing_quantum in range(1, 5):
                for denominator in range(1, 8):
                    scaled = closing_quantum * denominator
                    relation = star_minimum_response_relation_at_precision(
                        leaf_count, closing_quantum, denominator
                    )
                    expected = tuple(
                        vector
                        for vector in relation
                        if star_terminal_is_causally_reachable(vector, scaled)
                    )
                    self.assertEqual(
                        star_precision_causal_minimum_relation(
                            leaf_count,
                            closing_quantum,
                            denominator,
                        ),
                        expected,
                    )
                    checked += 1
        self.assertGreater(checked, 100)

    def test_full_static_minimum_causal_gate_is_exact_scaled_closing_threshold(self):
        for leaf_count in range(2, 9):
            for closing_quantum in range(1, 7):
                for denominator in range(1, 10):
                    scaled = closing_quantum * denominator
                    expected = scaled == 1 or scaled >= leaf_count + 1
                    self.assertEqual(
                        star_precision_minimum_relation_is_fully_causal(
                            leaf_count,
                            closing_quantum,
                            denominator,
                        ),
                        expected,
                    )

    def test_q1_true_refinement_first_opens_then_closes_causal_coverage_gap(self):
        for leaf_count in range(2, 10):
            self.assertTrue(
                star_precision_minimum_relation_is_fully_causal(
                    leaf_count, 1, 1
                )
            )
            for denominator in range(2, leaf_count + 1):
                self.assertFalse(
                    star_precision_minimum_relation_is_fully_causal(
                        leaf_count, 1, denominator
                    )
                )
            self.assertTrue(
                star_precision_minimum_relation_is_fully_causal(
                    leaf_count, 1, leaf_count + 1
                )
            )

    def test_q1_all_local_schedules_have_physical_total_one_through_denominator_k(self):
        for leaf_count in range(2, 7):
            for denominator in range(1, leaf_count + 1):
                terminals = independent_terminal_states(
                    leaf_count, denominator
                )
                self.assertEqual(
                    {sum(state) for state in terminals},
                    {denominator},
                )
                self.assertEqual(
                    {
                        Fraction(sum(state), denominator)
                        for state in terminals
                    },
                    {Fraction(1, 1)},
                )

    def test_first_q1_schedule_divergence_is_exactly_denominator_k_plus_one(self):
        for leaf_count in range(2, 8):
            first = star_q1_first_schedule_divergence_denominator(
                leaf_count
            )
            self.assertEqual(first, leaf_count + 1)
            for denominator in range(1, first):
                totals = {
                    sum(state)
                    for state in independent_terminal_states(
                        leaf_count, denominator
                    )
                }
                self.assertEqual(totals, {denominator})

            totals = {
                sum(state)
                for state in independent_terminal_states(
                    leaf_count, first
                )
            }
            self.assertEqual(totals, {leaf_count, leaf_count + 1})

    def test_first_schedule_branch_certificate_has_exact_two_physical_totals(self):
        for leaf_count in range(2, 10):
            certificate = star_q1_first_schedule_branch_certificate(
                leaf_count
            )
            self.assertEqual(certificate.denominator, leaf_count + 1)
            self.assertEqual(
                certificate.balanced_word,
                tuple(range(leaf_count)),
            )
            self.assertEqual(
                certificate.balanced_terminal,
                (1,) * leaf_count,
            )
            self.assertEqual(
                certificate.concentrated_word,
                (0, 0) + tuple(range(1, leaf_count)),
            )
            self.assertEqual(
                certificate.concentrated_terminal,
                (2,) + (1,) * (leaf_count - 1),
            )
            self.assertEqual(
                certificate.balanced_physical_total,
                Fraction(leaf_count, leaf_count + 1),
            )
            self.assertEqual(
                certificate.concentrated_physical_total,
                Fraction(1, 1),
            )

    def test_symmetric_minimum_appears_before_full_causal_closure(self):
        for leaf_count in range(2, 10):
            denominator = leaf_count
            phase = star_response_refinement_phase(
                leaf_count, 1, denominator
            )
            symmetric = star_symmetric_minimum_numerators(
                leaf_count, 1, denominator
            )
            self.assertEqual(phase.residue, leaf_count)
            self.assertEqual(symmetric, (1,) * leaf_count)
            self.assertTrue(
                star_terminal_is_causally_reachable(
                    symmetric, denominator
                )
            )
            self.assertFalse(
                star_precision_minimum_relation_is_fully_causal(
                    leaf_count, 1, denominator
                )
            )
            report = star_precision_causal_report(
                leaf_count, 1, denominator
            )
            self.assertTrue(report.symmetric_static_minimum_exists)
            self.assertTrue(report.symmetric_static_minimum_is_causal)
            self.assertFalse(report.full_static_minimum_relation_is_causal)
            self.assertFalse(report.sampled_policy_total_diverges)
            self.assertEqual(
                report.lowest_index_physical_total,
                Fraction(1, 1),
            )
            self.assertEqual(
                report.least_used_physical_total,
                Fraction(1, 1),
            )

    def test_unique_static_minimum_still_does_not_make_local_dynamics_unique(self):
        for leaf_count in range(2, 10):
            denominator = leaf_count + 1
            phase = star_response_refinement_phase(
                leaf_count, 1, denominator
            )
            relation = star_minimum_response_relation_at_precision(
                leaf_count, 1, denominator
            )
            self.assertEqual(phase.residue, 0)
            self.assertEqual(relation, ((1,) * leaf_count,))
            report = star_precision_causal_report(
                leaf_count, 1, denominator
            )
            self.assertTrue(report.static_minimum_unique)
            self.assertTrue(report.full_static_minimum_relation_is_causal)
            self.assertTrue(report.sampled_policy_total_diverges)
            self.assertEqual(
                report.least_used_terminal_numerator_total,
                leaf_count,
            )
            self.assertEqual(
                report.lowest_index_terminal_numerator_total,
                leaf_count + 1,
            )
            self.assertEqual(
                report.least_used_physical_total,
                Fraction(leaf_count, leaf_count + 1),
            )
            self.assertEqual(
                report.lowest_index_physical_total,
                Fraction(1, 1),
            )

    def test_reference_k3_q1_precision_sequence_separates_three_layers(self):
        reports = {
            denominator: star_precision_causal_report(
                3, 1, denominator
            )
            for denominator in (1, 2, 3, 4)
        }
        self.assertEqual(
            [reports[s].static_minimum_count for s in (1, 2, 3, 4)],
            [3, 6, 10, 1],
        )
        self.assertEqual(
            [reports[s].causal_minimum_count for s in (1, 2, 3, 4)],
            [3, 3, 7, 1],
        )
        self.assertEqual(
            [
                reports[s].full_static_minimum_relation_is_causal
                for s in (1, 2, 3, 4)
            ],
            [True, False, False, True],
        )
        self.assertEqual(
            [reports[s].sampled_policy_total_diverges for s in (1, 2, 3, 4)],
            [False, False, False, True],
        )
        self.assertTrue(reports[3].symmetric_static_minimum_exists)
        self.assertTrue(reports[3].symmetric_static_minimum_is_causal)
        self.assertTrue(reports[4].static_minimum_unique)

    def test_validation(self):
        with self.assertRaises(ValueError):
            star_precision_causal_report(1, 1, 1)
        with self.assertRaises(ValueError):
            star_precision_causal_report(3, 0, 1)
        with self.assertRaises(ValueError):
            star_precision_causal_report(3, 1, 0)


if __name__ == "__main__":
    unittest.main()
