import itertools
import unittest

from enterprise_math.relation_lattice import (
    capacity_gcd,
    coarsening_quantum_divides,
    field_preserving_shift,
    lower_generation_witness,
    primitive_capacity_vector,
    relation_field_is_lower_generated,
    relation_lattice_index,
    relation_lattice_quotient_invariant_factors,
    relation_precision_duality,
    relation_quantum,
    relation_translation_period,
    same_field_shift_multiple,
)
from enterprise_math.weighted_relation_field import (
    weighted_relation_field,
    weighted_relation_field_is_closed,
)


def antisymmetric_field(size: int, upper_values: tuple[int, ...]):
    expected = size * (size - 1) // 2
    if len(upper_values) != expected:
        raise ValueError("wrong upper-triangle coordinate count")
    rows = [[0] * size for _ in range(size)]
    cursor = 0
    for i in range(size):
        for j in range(i + 1, size):
            value = upper_values[cursor]
            cursor += 1
            rows[i][j] = value
            rows[j][i] = -value
    return tuple(tuple(row) for row in rows)


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

    def test_generated_fields_are_recognized_and_have_constructive_witnesses(self):
        cases = (
            ((1,), (4,)),
            ((2, 4), (3, -1)),
            ((6, 10, 14), (4, -2, 7)),
            ((4, 6, 10, 14), (1, 3, -5, 9)),
        )
        for capacities, totals in cases:
            field = weighted_relation_field(capacities, totals)
            self.assertTrue(relation_field_is_lower_generated(capacities, field))
            witness = lower_generation_witness(capacities, field)
            self.assertEqual(weighted_relation_field(capacities, witness), field)

    def test_closed_nondivisible_field_is_in_saturated_closure_but_not_lower_generated(self):
        capacities = (2, 4)
        field = ((0, 1), (-1, 0))
        self.assertTrue(weighted_relation_field_is_closed(capacities, field))
        self.assertFalse(relation_field_is_lower_generated(capacities, field))
        with self.assertRaises(ValueError):
            lower_generation_witness(capacities, field)

    def test_lower_generation_criterion_exhaustive_small_closed_fields(self):
        capacity_sets = (
            (1, 2),
            (2, 4),
            (2, 4, 6),
            (3, 6, 9),
            (6, 10, 14),
        )
        for capacities in capacity_sets:
            edge_count = len(capacities) * (len(capacities) - 1) // 2
            quantum = relation_quantum(capacities)
            for upper_values in itertools.product(range(-3, 4), repeat=edge_count):
                field = antisymmetric_field(len(capacities), upper_values)
                if not weighted_relation_field_is_closed(capacities, field):
                    continue
                expected = all(value % quantum == 0 for row in field for value in row)
                self.assertEqual(
                    relation_field_is_lower_generated(capacities, field),
                    expected,
                )
                if expected:
                    witness = lower_generation_witness(capacities, field)
                    self.assertEqual(weighted_relation_field(capacities, witness), field)
                else:
                    with self.assertRaises(ValueError):
                        lower_generation_witness(capacities, field)

    def test_genesis_index_invariant_factors_and_index(self):
        cases = (
            ((1,), (), 1),
            ((1, 2, 3), (1, 1), 1),
            ((2, 4), (2,), 2),
            ((6, 10, 14), (2, 2), 4),
            ((9, 15, 21, 27), (3, 3, 3), 27),
        )
        for capacities, factors, index in cases:
            self.assertEqual(
                relation_lattice_quotient_invariant_factors(capacities),
                factors,
            )
            self.assertEqual(relation_lattice_index(capacities), index)


if __name__ == "__main__":
    unittest.main()
