import itertools
import unittest

from enterprise_math.relation_lattice import (
    capacity_gcd,
    coarsening_quantum_divides,
    field_preserving_shift,
    primitive_capacity_vector,
    relation_precision_duality,
    relation_quantum,
    relation_translation_period,
    same_field_shift_multiple,
)
from enterprise_math.weighted_relation_field import weighted_relation_field


class RelationLatticeTests(unittest.TestCase):
    def test_quantum_period_duality(self):
        for capacities in (
            (1,),
            (1, 1, 1),
            (2, 2),
            (2, 3, 5),
            (4, 6, 10, 14),
        ):
            quantum, period, total = relation_precision_duality(capacities)
            self.assertEqual(quantum, capacity_gcd(capacities))
            self.assertEqual(quantum, relation_quantum(capacities))
            self.assertEqual(period, relation_translation_period(capacities))
            self.assertEqual(quantum * period, total)

    def test_primitive_capacity_vector_has_gcd_one(self):
        from math import gcd

        for capacities in ((2, 4, 6), (3, 6, 9, 12), (2, 3, 5)):
            primitive = primitive_capacity_vector(capacities)
            current = 0
            for value in primitive:
                current = gcd(current, value)
            self.assertEqual(current, 1)

    def test_field_preserving_shift_changes_total_by_exact_period(self):
        capacities = (4, 6, 10)
        totals = (3, -2, 7)
        base_field = weighted_relation_field(capacities, totals)
        period = relation_translation_period(capacities)
        for steps in range(-5, 6):
            shifted = field_preserving_shift(capacities, totals, steps)
            self.assertEqual(weighted_relation_field(capacities, shifted), base_field)
            self.assertEqual(sum(shifted) - sum(totals), steps * period)
            self.assertEqual(
                same_field_shift_multiple(capacities, totals, shifted),
                steps,
            )

    def test_equal_fields_in_bounded_search_differ_by_primitive_capacity_shift(self):
        capacities = (2, 4, 6)
        states = list(itertools.product(range(-3, 4), repeat=3))
        buckets = {}
        for state in states:
            field = weighted_relation_field(capacities, state)
            buckets.setdefault(field, []).append(state)
        for bucket in buckets.values():
            anchor = bucket[0]
            for state in bucket[1:]:
                steps = same_field_shift_multiple(capacities, anchor, state)
                self.assertIsNotNone(steps)

    def test_relation_entries_are_multiples_of_capacity_gcd(self):
        capacity_sets = ((2, 2), (4, 6, 10), (3, 6, 9, 12))
        for capacities in capacity_sets:
            quantum = relation_quantum(capacities)
            for totals in itertools.product(range(-3, 4), repeat=len(capacities)):
                field = weighted_relation_field(capacities, totals)
                for row in field:
                    for value in row:
                        self.assertEqual(value % quantum, 0)

    def test_relation_quantum_can_only_coarsen_under_partition_sums(self):
        fine = (1, 1, 1, 1, 1, 1)
        coarse_levels = (
            (2, 1, 3),
            (3, 3),
            (6,),
        )
        previous = fine
        for coarse in coarse_levels:
            self.assertTrue(coarsening_quantum_divides(previous, coarse))
            previous = coarse

        fine = (2, 4, 6, 8)
        coarse = (6, 14)
        self.assertTrue(coarsening_quantum_divides(fine, coarse))
        self.assertEqual(relation_quantum(fine), 2)
        self.assertEqual(relation_quantum(coarse), 2)


if __name__ == "__main__":
    unittest.main()
