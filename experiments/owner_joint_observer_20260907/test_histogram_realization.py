"""Focused semantic checks for integer histogram realization and certificates."""
from copy import deepcopy
from fractions import Fraction
from itertools import product
import unittest

from histogram_realization import (
    AXES,
    Branch,
    WeightHistogram,
    realize_uniform_binary_histograms,
    stratify_histogram_tables,
    verify_histogram_realization,
    verify_rao_obstruction,
)
from observer_certificate import fiber_histograms


LEVELS = ((0, 1),) * 6


def uniform_tables(counts, levels=LEVELS):
    histogram = WeightHistogram.from_counts(counts)
    return {axes: {address: histogram for address in product(*(levels[i] for i in axes))}
            for axes in AXES}


class HistogramRealizationTests(unittest.TestCase):
    def test_zero_including_explicit_zero_fibers_is_realized(self):
        for tables in (uniform_tables({}), {axes: {} for axes in AXES}):
            result = realize_uniform_binary_histograms(tables, max_branches=0)
            self.assertEqual(result["status"], "REALIZED")
            self.assertEqual(result["branches"], ())
            self.assertTrue(result["verification"]["valid"])
            self.assertEqual(len(result["verification"]["checked_axis_tables"]), 20)

    def test_lambda_one_has_bound_rao_obstruction(self):
        tables = uniform_tables({1: 1})
        result = realize_uniform_binary_histograms(tables)
        self.assertEqual(result["status"], "INFEASIBLE_BY_RAO")
        self.assertTrue(verify_rao_obstruction(tables, result["certificate"]))
        self.assertFalse(verify_rao_obstruction(uniform_tables({1: 2}), result["certificate"]))
        changed = dict(result["certificate"], gram_rank=13)
        self.assertFalse(verify_rao_obstruction(tables, changed))
        for changes in ({"per_fiber_count": True}, {"branch_rows": Fraction(8)},
                        {"axis_levels": ((False, 1),) * 6}, {"weight": True}):
            self.assertFalse(verify_rao_obstruction(tables, dict(result["certificate"], **changes)))

    def test_lambda_two_three_five_construct_complete_integer_witnesses(self):
        for multiplicity in (2, 3, 5):
            with self.subTest(multiplicity=multiplicity):
                tables = uniform_tables({1: multiplicity})
                result = realize_uniform_binary_histograms(tables)
                self.assertEqual(result["status"], "REALIZED")
                self.assertEqual(len(result["branches"]), 8 * multiplicity)
                self.assertTrue(all(branch.weight == 1 for branch in result["branches"]))
                verification = verify_histogram_realization(tables, result["branches"])
                self.assertTrue(verification["valid"])
                self.assertEqual(len(verification["comparisons"]), 160)

    def test_mass_only_rational_answer_does_not_realize_histograms(self):
        tables = uniform_tables({1: 1})
        relaxation = tuple(Branch(f"relaxed:{i}", point, Fraction(1, 8))
                           for i, point in enumerate(product((0, 1), repeat=6)))
        report = verify_histogram_realization(tables, relaxation)
        self.assertFalse(report["valid"])
        self.assertTrue(report["all_mass_tables_match"])
        self.assertEqual(len(report["mismatches"]), 160)
        first = report["mismatches"][0]
        self.assertEqual(first["expected_histogram"].entries, ((Fraction(1), 1),))
        self.assertEqual(first["actual_histogram"].entries, ((Fraction(1, 8), 8),))
        self.assertEqual({row["weight"] for row in first["weight_comparisons"]}, {Fraction(1), Fraction(1, 8)})

    def test_mixed_exact_weights_are_independent_integer_layers(self):
        tables = uniform_tables({Fraction(2, 3): 3, 1: 2})
        strata = stratify_histogram_tables(tables)
        self.assertEqual(strata["weights"], (Fraction(2, 3), Fraction(1)))
        self.assertEqual(strata["branch_totals"], {Fraction(2, 3): 24, Fraction(1): 16})
        self.assertEqual(set(strata["count_layers"][Fraction(2, 3)][(0, 1, 2)].values()), {3})
        result = realize_uniform_binary_histograms(tables)
        self.assertEqual(result["status"], "REALIZED")
        self.assertEqual(len(result["branches"]), 40)
        self.assertTrue(result["verification"]["valid"])

    def test_one_bad_weight_layer_obstructs_whole_mixed_population(self):
        tables = uniform_tables({Fraction(2, 3): 1, 1: 2})
        result = realize_uniform_binary_histograms(tables)
        self.assertEqual(result["status"], "INFEASIBLE_BY_RAO")
        self.assertEqual(result["certificate"]["weight"], Fraction(2, 3))
        self.assertTrue(verify_rao_obstruction(tables, result["certificate"]))

    def test_signed_axis_affine_relabel_preserves_raw_chart(self):
        levels = ((-11, -3), (8, -2), (-5, 1), (0, 7), (9, -9), (-8, -7))
        for multiplicity in (1, 5):
            tables = uniform_tables({1: multiplicity}, levels)
            result = realize_uniform_binary_histograms(tables)
            if multiplicity == 1:
                self.assertTrue(verify_rao_obstruction(tables, result["certificate"]))
                self.assertFalse(verify_rao_obstruction(uniform_tables({1: 1}), result["certificate"]))
            else:
                self.assertTrue(result["verification"]["valid"])
                self.assertTrue(all(branch.coordinate[i] in levels[i]
                                    for branch in result["branches"] for i in range(6)))
                self.assertEqual(result["axis_levels"], tuple(tuple(sorted(values)) for values in levels))

    def test_general_realizable_input_stays_unclassified(self):
        population = (Branch("single", (-4, 2, 8, 0, 1, -5), Fraction(3, 7)),)
        tables = {axes: fiber_histograms(population, axes) for axes in AXES}
        self.assertEqual(realize_uniform_binary_histograms(tables)["status"], "UNCLASSIFIED")
        self.assertTrue(verify_histogram_realization(tables, population)["valid"])

    def test_equal_totals_do_not_imply_uniform_joint_realizability(self):
        tables = uniform_tables({1: 2})
        value = tables[(0, 1, 2)].pop((0, 0, 0))
        tables[(0, 1, 2)][(2, 0, 0)] = value
        self.assertEqual(realize_uniform_binary_histograms(tables)["status"], "UNCLASSIFIED")

    def test_missing_tables_bool_axes_and_nonraw_addresses_rejected(self):
        tables = uniform_tables({1: 2})
        missing = deepcopy(tables)
        missing.pop((0, 1, 2))
        with self.assertRaises(ValueError):
            stratify_histogram_tables(missing)
        bad_axis = deepcopy(tables)
        table = bad_axis.pop((0, 1, 2))
        bad_axis[(False, 1, 2)] = table
        with self.assertRaises(ValueError):
            stratify_histogram_tables(bad_axis)
        bad_address = deepcopy(tables)
        table = bad_address[(0, 1, 2)]
        entry = table.pop((0, 0, 0))
        table[(False, 0, 0)] = entry
        with self.assertRaises(ValueError):
            stratify_histogram_tables(bad_address)

    def test_scalar_mass_values_cannot_be_input_histograms(self):
        tables = uniform_tables({1: 2})
        tables[(0, 1, 2)][(0, 0, 0)] = Fraction(2)
        with self.assertRaises(TypeError):
            stratify_histogram_tables(tables)

    def test_per_weight_totals_must_agree_even_when_total_mass_agrees(self):
        tables = uniform_tables({1: 2})
        tables[(0, 1, 2)] = {address: WeightHistogram.from_weights([2])
                              for address in product((0, 1), repeat=3)}
        with self.assertRaisesRegex(ValueError, "exact weight"):
            stratify_histogram_tables(tables)

    def test_input_histogram_entries_are_copied(self):
        entries = [(Fraction(1), 2)]
        histogram = WeightHistogram(entries)
        tables = uniform_tables({1: 2})
        tables[(0, 1, 2)][(0, 0, 0)] = histogram
        strata = stratify_histogram_tables(tables)
        entries[0] = (Fraction(1), 9)
        self.assertEqual(strata["tables"][(0, 1, 2)][(0, 0, 0)].entries, ((Fraction(1), 2),))

    def test_mutating_inner_pair_cannot_desynchronize_histogram_and_count_layer(self):
        pair = [Fraction(1), 1]
        histogram = WeightHistogram([pair])
        tables = uniform_tables({1: 1})
        tables[(0, 1, 2)][(0, 0, 0)] = histogram
        strata = stratify_histogram_tables(tables)
        before = deepcopy(strata)
        pair[1] = 9
        self.assertEqual(strata, before)
        pair[0] = Fraction(2)
        self.assertEqual(strata, before)
        self.assertEqual(strata["tables"][(0, 1, 2)][(0, 0, 0)].entries, ((Fraction(1), 1),))
        self.assertEqual(strata["count_layers"][Fraction(1)][(0, 1, 2)][(0, 0, 0)], 1)
        self.assertEqual(strata["weights"], (Fraction(1),))

    def test_malformed_subclass_entries_are_revalidated_without_numeric_coercion(self):
        class UncheckedHistogram(WeightHistogram):
            def __post_init__(self):
                pass

        bad_entries = (
            [[True, 1]], [[1.0, 1]], [[1, 1]],
            [[Fraction(1), True]], [[Fraction(1), 1.0]],
            [[Fraction(-1), 1]], [[Fraction(1), 0]],
            [[Fraction(1), 1], [Fraction(1), 2]],
            [[Fraction(2), 1], [Fraction(1), 1]],
            [[Fraction(1)]], [[Fraction(1), 1, 2]], [1],
        )
        for entries in bad_entries:
            with self.subTest(entries=entries):
                tables = uniform_tables({1: 1})
                tables[(0, 1, 2)][(0, 0, 0)] = UncheckedHistogram(entries)
                with self.assertRaises((TypeError, ValueError)):
                    stratify_histogram_tables(tables)

    def test_missing_zero_fibers_are_checked_against_extra_branches(self):
        tables = {axes: {} for axes in AXES}
        report = verify_histogram_realization(tables, (Branch("extra", (10,) * 6),))
        self.assertFalse(report["valid"])
        self.assertEqual(len(report["mismatches"]), 20)
        self.assertTrue(all(row["expected_histogram"].is_zero for row in report["mismatches"]))

    def test_duplicate_labels_and_nonbranch_candidates_rejected(self):
        tables = {axes: {} for axes in AXES}
        branch = Branch("duplicate", (0,) * 6)
        with self.assertRaises(ValueError):
            verify_histogram_realization(tables, (branch, branch))
        with self.assertRaises(TypeError):
            verify_histogram_realization(tables, (((0,) * 6, Fraction(1)),))

    def test_materialization_budget_is_not_an_infeasibility_verdict(self):
        result = realize_uniform_binary_histograms(uniform_tables({1: 5}), max_branches=39)
        self.assertEqual(result["status"], "WITNESS_BUDGET_EXCEEDED")
        self.assertEqual(result["mathematical_status"], "UNIFORM_FAMILY_REALIZABLE")
        self.assertEqual(result["required_branches"], 40)


if __name__ == "__main__":
    unittest.main()
