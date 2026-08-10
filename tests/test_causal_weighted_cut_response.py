import unittest
from fractions import Fraction
from itertools import combinations, product

from enterprise_math.causal_weighted_cut_response import (
    all_weighted_cut_responses,
    centered_capacity_cut_response,
    maximum_absolute_weighted_cut_response,
    weighted_cut_closed_form,
    weighted_cut_identity,
    weighted_cut_relation_sum,
    weighted_relation_matrix,
    zero_total_cut_response_is_subset_total,
)


class CausalWeightedCutResponseTests(unittest.TestCase):
    def test_weighted_cut_sum_has_fraction_free_closed_form(self):
        cases = (
            ((1, 1, 1, 1), (2, -1, 0, -1)),
            ((2, 1, 3), (5, -2, 4)),
            ((4, 2, 5, 1), (7, -3, 6, 2)),
        )
        for capacities, totals in cases:
            for size in range(1, len(capacities)):
                for subset in combinations(range(len(capacities)), size):
                    self.assertTrue(weighted_cut_identity(capacities, totals, subset))
                    self.assertEqual(
                        weighted_cut_relation_sum(capacities, totals, subset),
                        weighted_cut_closed_form(capacities, totals, subset),
                    )

    def test_zero_total_weighted_cut_response_forgets_capacity_in_value_but_not_probe_structure(self):
        capacities = (3, 1, 4, 2)
        totals = (5, -2, -1, -2)
        self.assertEqual(sum(totals), 0)
        for size in range(1, len(capacities)):
            for subset in combinations(range(len(capacities)), size):
                self.assertTrue(zero_total_cut_response_is_subset_total(capacities, totals, subset))
                self.assertEqual(
                    centered_capacity_cut_response(capacities, totals, subset),
                    Fraction(sum(totals[index] for index in subset)),
                )

    def test_unit_capacities_recover_complete_slot_cut_probes(self):
        capacities = (1, 1, 1, 1)
        for totals in product(range(-2, 3), repeat=4):
            if sum(totals) != 0:
                continue
            responses = all_weighted_cut_responses(capacities, totals)
            expected = {
                subset: Fraction(sum(totals[index] for index in subset))
                for size in range(1, 4)
                for subset in combinations(range(4), size)
            }
            self.assertEqual(responses, expected)
            self.assertEqual(
                maximum_absolute_weighted_cut_response(capacities, totals),
                max(abs(value) for value in expected.values()),
            )

    def test_relation_matrix_is_antisymmetric_and_generates_every_cut_response(self):
        capacities = (2, 3, 1)
        totals = (4, -5, 1)
        matrix = weighted_relation_matrix(capacities, totals)
        for i in range(3):
            self.assertEqual(matrix[i][i], 0)
            for j in range(3):
                self.assertEqual(matrix[i][j], -matrix[j][i])
        for subset in ((0,), (1,), (2,), (0, 1), (0, 2), (1, 2)):
            self.assertTrue(weighted_cut_identity(capacities, totals, subset))

    def test_complement_cut_has_opposite_response(self):
        capacities = (2, 1, 3, 4)
        totals = (5, -2, 1, -4)
        all_indices = set(range(4))
        for size in range(1, 4):
            for subset in combinations(range(4), size):
                complement = tuple(sorted(all_indices - set(subset)))
                self.assertEqual(
                    centered_capacity_cut_response(capacities, totals, subset),
                    -centered_capacity_cut_response(capacities, totals, complement),
                )


if __name__ == "__main__":
    unittest.main()
