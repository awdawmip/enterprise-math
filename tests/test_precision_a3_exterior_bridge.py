import unittest
from itertools import product

from enterprise_math.precision_a3_exterior_bridge import (
    a3_closure_defects,
    a3_closure_is_exterior_identity,
    a3_exterior_identity_holds,
    a3_exterior_quotient_codimension,
    a3_upper_relation_token,
    exterior_upper_relation_token,
    field_preserving_primitive_direction,
)
from enterprise_math.relation_lattice import same_field_shift_multiple
from enterprise_math.weighted_relation_field import weighted_relation_field


class PrecisionA3ExteriorBridgeTests(unittest.TestCase):
    def test_a3_field_is_negative_exterior_token(self):
        examples = (
            ((1, 1), (2, 5)),
            ((2, 3), (7, -4)),
            ((2, 3, 5), (11, -2, 8)),
            ((4, 6, 10, 15), (3, 9, -7, 12)),
        )
        for capacities, totals in examples:
            a3 = a3_upper_relation_token(capacities, totals)
            exterior = exterior_upper_relation_token(capacities, totals)
            self.assertEqual(a3, tuple(-value for value in exterior))
            self.assertTrue(a3_exterior_identity_holds(capacities, totals))

    def test_weighted_three_block_closure_is_exterior_wedge_identity(self):
        for capacities in ((1, 1, 1), (2, 3, 5), (4, 6, 9)):
            for totals in product(range(-2, 3), repeat=3):
                self.assertEqual(a3_closure_defects(capacities, totals), (0,))
                self.assertTrue(a3_closure_is_exterior_identity(capacities, totals))

    def test_relation_dimension_matches_rank_one_quotient_codimension(self):
        for capacities in ((1,), (1, 1), (2, 3, 5), (2, 4, 6, 8, 10)):
            self.assertEqual(a3_exterior_quotient_codimension(capacities), len(capacities) - 1)

    def test_primitive_capacity_vector_is_exterior_kernel_direction(self):
        capacities = (6, 9, 15)
        primitive = field_preserving_primitive_direction(capacities)
        self.assertEqual(primitive, (2, 3, 5))
        totals = (7, -4, 11)
        base_field = weighted_relation_field(capacities, totals)
        for steps in range(-4, 5):
            shifted = tuple(
                total + steps * direction
                for total, direction in zip(totals, primitive)
            )
            self.assertEqual(weighted_relation_field(capacities, shifted), base_field)
            self.assertEqual(same_field_shift_multiple(capacities, totals, shifted), steps)
            self.assertEqual(
                exterior_upper_relation_token(capacities, shifted),
                exterior_upper_relation_token(capacities, totals),
            )

    def test_unit_block_a3_relation_is_integer_difference(self):
        capacities = (1, 1)
        totals = (3, 8)
        self.assertEqual(a3_upper_relation_token(capacities, totals), (-5,))
        self.assertEqual(exterior_upper_relation_token(capacities, totals), (5,))


if __name__ == "__main__":
    unittest.main()
