import unittest
from itertools import product

from enterprise_math.causal_coarse_transfer_incidence import (
    coarse_state_fine_lift_count,
    coarse_transfer_witness_count,
    fiber_count,
    mean_fine_move_multiplicity_per_source_lift,
    reverse_witness_balance_identity,
    simplified_source_ratio_factors,
    total_positive_slot_incidence,
    transferred_coarse_state,
)


def _weak_compositions(total, slots):
    if slots == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in _weak_compositions(total - first, slots - 1):
            yield (first,) + rest


class CausalCoarseTransferIncidenceTests(unittest.TestCase):
    def test_fiber_count_matches_direct_weak_composition_enumeration(self):
        for capacity in range(1, 6):
            for total in range(8):
                self.assertEqual(
                    fiber_count(capacity, total),
                    len(tuple(_weak_compositions(total, capacity))),
                )

    def test_positive_slot_incidence_has_closed_form(self):
        for capacity in range(1, 6):
            for total in range(8):
                direct = sum(
                    sum(value > 0 for value in composition)
                    for composition in _weak_compositions(total, capacity)
                )
                self.assertEqual(total_positive_slot_incidence(capacity, total), direct)

    def test_coarse_transfer_witness_count_matches_direct_two_block_enumeration(self):
        for m_receiver in range(1, 4):
            for m_donor in range(1, 4):
                for c_receiver in range(4):
                    for c_donor in range(1, 5):
                        direct = 0
                        for receiver_state in _weak_compositions(c_receiver, m_receiver):
                            for donor_state in _weak_compositions(c_donor, m_donor):
                                direct += m_receiver * sum(value > 0 for value in donor_state)
                        self.assertEqual(
                            coarse_transfer_witness_count(
                                (m_receiver, m_donor),
                                (c_receiver, c_donor),
                                0,
                                1,
                            ),
                            direct,
                        )

    def test_reverse_fine_edge_incidence_is_exact_integer_balance(self):
        capacities = (2, 3, 1)
        for totals in product(range(5), repeat=3):
            for receiver in range(3):
                for donor in range(3):
                    if receiver == donor or totals[donor] == 0:
                        continue
                    self.assertTrue(
                        reverse_witness_balance_identity(
                            capacities, totals, receiver, donor
                        )
                    )

    def test_target_state_is_exact_one_unit_coarse_transfer(self):
        totals = (3, 0, 2)
        self.assertEqual(transferred_coarse_state(totals, 1, 0), (2, 1, 2))
        self.assertEqual(transferred_coarse_state(totals, 0, 2), (4, 0, 1))

    def test_average_witness_ratio_remains_exact_integer_pair(self):
        capacities = (4, 3, 2)
        totals = (5, 4, 1)
        witness, fibers = mean_fine_move_multiplicity_per_source_lift(
            capacities, totals, 0, 1
        )
        numerator, denominator = simplified_source_ratio_factors(
            capacities, totals, 0, 1
        )
        self.assertEqual(witness * denominator, fibers * numerator)

    def test_full_coarse_fiber_count_is_product_of_block_fibers(self):
        capacities = (2, 3, 1)
        totals = (4, 2, 5)
        self.assertEqual(
            coarse_state_fine_lift_count(capacities, totals),
            fiber_count(2, 4) * fiber_count(3, 2) * fiber_count(1, 5),
        )


if __name__ == "__main__":
    unittest.main()
