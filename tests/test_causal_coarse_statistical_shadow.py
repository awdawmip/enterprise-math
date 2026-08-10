import unittest
from itertools import product

from enterprise_math.causal_coarse_statistical_shadow import (
    averaged_rate_closed_form_identity,
    averaged_rate_detailed_balance_identity,
    averaged_transfer_rate_pair,
    coarse_totals_with_grand_total,
    grouped_fiber_decomposition_identity,
    reduced_uniform_probability_pair,
    total_fine_occupancy_count,
    uniform_fine_state_probability_pair,
)


class CausalCoarseStatisticalShadowTests(unittest.TestCase):
    def test_grouped_macro_multiplicities_reconstruct_full_fine_fiber(self):
        capacities_cases = ((1, 1), (2, 1), (2, 3), (1, 2, 3), (3, 2, 2, 1))
        for capacities in capacities_cases:
            for grand_total in range(8):
                self.assertTrue(grouped_fiber_decomposition_identity(capacities, grand_total))
                states = coarse_totals_with_grand_total(len(capacities), grand_total)
                self.assertTrue(all(sum(state) == grand_total for state in states))

    def test_uniform_fine_probability_pair_is_exact_integer_ratio_only(self):
        capacities = (2, 3)
        totals = (4, 2)
        numerator, denominator = uniform_fine_state_probability_pair(capacities, totals)
        self.assertGreater(numerator, 0)
        self.assertEqual(denominator, total_fine_occupancy_count(capacities, 6))
        reduced_num, reduced_den = reduced_uniform_probability_pair(capacities, totals)
        self.assertEqual(numerator * reduced_den, denominator * reduced_num)

    def test_average_rate_closed_form_matches_witness_incidence_ratio(self):
        capacities = (2, 3, 4)
        for totals in product(range(5), repeat=3):
            for receiver in range(3):
                for donor in range(3):
                    if receiver == donor:
                        continue
                    self.assertTrue(
                        averaged_rate_closed_form_identity(
                            capacities, totals, receiver, donor
                        )
                    )

    def test_optional_averaged_rate_shadow_obeys_exact_macro_detailed_balance(self):
        capacities = (2, 3, 1)
        for totals in product(range(5), repeat=3):
            for receiver in range(3):
                for donor in range(3):
                    if receiver == donor or totals[donor] == 0:
                        continue
                    self.assertTrue(
                        averaged_rate_detailed_balance_identity(
                            capacities, totals, receiver, donor
                        )
                    )

    def test_receiver_total_does_not_enter_average_endpoint_count_but_donor_total_does(self):
        capacities = (4, 3)
        rates = {
            totals: averaged_transfer_rate_pair(capacities, totals, 0, 1)
            for totals in ((0, 2), (5, 2), (9, 2))
        }
        self.assertEqual(len(set(rates.values())), 1)
        donor_rates = [
            averaged_transfer_rate_pair(capacities, (5, donor), 0, 1)
            for donor in (1, 2, 3, 4)
        ]
        self.assertGreater(len(set(donor_rates)), 1)


if __name__ == "__main__":
    unittest.main()
