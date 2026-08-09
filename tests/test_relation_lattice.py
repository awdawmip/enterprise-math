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
    def test_primitive_capacity_vector_has_gcd_one(self):
        for capacities in ((2, 4), (6, 10, 14), (4, 6, 10, 14), (9, 15, 21)):
            primitive = primitive_capacity_vector(capacities)
            self.assertEqual(capacity_gcd(primitive), 1)

    def test_field_preserving_shift_keeps_weighted_field(self):
        cases = (
            ((2, 4), (3, -1)),
            ((6, 10, 14), (4, -2, 7)),
            ((4, 6, 10, 14), (1, 3, -5, 9)),
        )
        for capacities, totals in cases:
            original = weighted_relation_field(capacities, totals)
            for steps in range(-5, 6):
                shifted = field_preserving_shift(capacities, totals, steps)
                self.assertEqual(weighted_relation_field(capacities, shifted), original)

    def test_same_field_states_are_primitive_capacity_translates(self):
        capacity_sets = ((2, 4), (6, 10, 14), (4, 6, 10, 14))
        for capacities in capacity_sets:
            primitive = primitive_capacity_vector(capacities)
            for left in itertools.product(range(-2, 3), repeat=len(capacities)):
                for step in range(-2, 3):
                    right = tuple(
                        value + step * direction
                        for value, direction in zip(left, primitive)
                    )
                    self.assertEqual(
                        same_field_shift_multiple(capacities, left, right), step
                    )

    def test_relation_quantum_and_translation_period_duality(self):
        for capacities in ((1,), (2, 4), (6, 10, 14), (4, 6, 10, 14)):
            quantum, period, total = relation_precision_duality(capacities)
            self.assertEqual(quantum, relation_quantum(capacities))
            self.assertEqual(period, relation_translation_period(capacities))
            self.assertEqual(quantum * period, total)

    def test_coarsening_can_only_increase_capacity_gcd_by_divisibility(self):
        fine = (2, 3, 5, 7)
        coarse_examples = (
            (5, 12),
            (10, 7),
            (17,),
        )
        for coarse in coarse_examples:
            self.assertTrue(coarsening_quantum_divides(fine, coarse))

    def test_different_fields_do_not_have_shift_multiple(self):
        capacities = (2, 4, 6)
        self.assertIsNone(
            same_field_shift_multiple(capacities, (1, 2, 3), (1, 2, 4))
        )


if __name__ == "__main__":
    unittest.main()
