import itertools
import unittest

from enterprise_math.relation_lattice import (
    field_preserving_shift,
    primitive_capacity_vector,
    relation_translation_period,
)
from enterprise_math.relation_zero_total_orbit import (
    relation_field_total_residue_is_well_defined,
    relation_fields_share_zero_total_orbit,
    relation_zero_total_orbit_residue,
    zero_total_relation_orbit_witness,
)
from enterprise_math.weighted_relation_field import weighted_relation_field


class RelationZeroTotalOrbitTests(unittest.TestCase):
    def test_constructed_witness_is_exact_on_bounded_state_families(self):
        capacity_families = (
            (1, 1),
            (2, 3),
            (2, 4),
            (2, 3, 5),
            (2, 4, 6),
            (3, 5, 7),
            (2, 3, 4, 5),
        )
        for capacities in capacity_families:
            period = relation_translation_period(capacities)
            states = tuple(itertools.product(range(-1, 2), repeat=len(capacities)))
            for left in states:
                for right in states:
                    expected = (sum(right) - sum(left)) % period == 0
                    self.assertEqual(
                        relation_fields_share_zero_total_orbit(
                            capacities, left, right
                        ),
                        expected,
                    )
                    witness = zero_total_relation_orbit_witness(
                        capacities, left, right
                    )
                    self.assertEqual(witness.same_orbit, expected)
                    if expected:
                        self.assertIsNotNone(witness.zero_total_update)
                        self.assertIsNotNone(witness.shifted_left)
                        self.assertEqual(sum(witness.zero_total_update), 0)
                        self.assertEqual(
                            weighted_relation_field(
                                capacities, witness.shifted_left
                            ),
                            weighted_relation_field(capacities, right),
                        )
                    else:
                        self.assertIsNone(witness.zero_total_update)
                        self.assertIsNone(witness.shifted_left)

    def test_zero_total_updates_preserve_the_orbit_residue(self):
        capacities = (6, 10, 14, 22)
        base = (5, -3, 8, 1)
        updates = (
            (1, -1, 0, 0),
            (3, 2, -7, 2),
            (-5, 4, 3, -2),
        )
        base_residue = relation_zero_total_orbit_residue(capacities, base)
        for update in updates:
            self.assertEqual(sum(update), 0)
            changed = tuple(value + delta for value, delta in zip(base, update))
            self.assertEqual(
                relation_zero_total_orbit_residue(capacities, changed),
                base_residue,
            )
            self.assertTrue(
                relation_fields_share_zero_total_orbit(
                    capacities, base, changed
                )
            )

    def test_primitive_field_preserving_shift_changes_total_by_tau_but_not_residue(self):
        capacities = (6, 10, 14, 22)
        totals = (5, -3, 8, 1)
        period = relation_translation_period(capacities)
        for steps in range(-4, 5):
            shifted = field_preserving_shift(capacities, totals, steps)
            self.assertEqual(
                sum(shifted) - sum(totals),
                steps * period,
            )
            self.assertEqual(
                weighted_relation_field(capacities, shifted),
                weighted_relation_field(capacities, totals),
            )
            self.assertTrue(
                relation_field_total_residue_is_well_defined(
                    capacities, totals, shifted
                )
            )

    def test_every_mod_tau_residue_is_realized_by_a_legal_relation_state(self):
        for capacities in (
            (1, 1),
            (2, 3),
            (6, 10, 14),
            (4, 8, 12, 20),
        ):
            period = relation_translation_period(capacities)
            residues = set()
            for residue in range(period):
                state = (residue,) + (0,) * (len(capacities) - 1)
                residues.add(relation_zero_total_orbit_residue(capacities, state))
            self.assertEqual(residues, set(range(period)))

    def test_different_residues_cannot_be_connected_by_zero_total_update_even_if_fields_shift(self):
        capacities = (2, 3, 5)
        period = relation_translation_period(capacities)
        self.assertGreater(period, 1)
        left = (0, 0, 0)
        right = (1, 0, 0)
        self.assertNotEqual(
            relation_zero_total_orbit_residue(capacities, left),
            relation_zero_total_orbit_residue(capacities, right),
        )
        witness = zero_total_relation_orbit_witness(capacities, left, right)
        self.assertFalse(witness.same_orbit)
        self.assertIsNone(witness.zero_total_update)

    def test_same_residue_can_connect_different_relation_fields_by_explicit_zero_total_update(self):
        capacities = (2, 3, 5)
        left = (0, 0, 0)
        # Grand total difference is zero, but the relation field changes.
        right = (2, -1, -1)
        self.assertNotEqual(
            weighted_relation_field(capacities, left),
            weighted_relation_field(capacities, right),
        )
        witness = zero_total_relation_orbit_witness(capacities, left, right)
        self.assertTrue(witness.same_orbit)
        self.assertEqual(witness.kernel_shift_steps, 0)
        self.assertEqual(witness.zero_total_update, right)
        self.assertEqual(witness.shifted_left, right)

    def test_nonzero_total_difference_multiple_of_tau_uses_kernel_shift_plus_zero_total_update(self):
        capacities = (6, 10, 14)
        primitive = primitive_capacity_vector(capacities)
        period = relation_translation_period(capacities)
        left = (3, -2, 5)
        zero_total = (4, -7, 3)
        self.assertEqual(sum(zero_total), 0)
        steps = 2
        right = tuple(
            value + update + steps * primitive_value
            for value, update, primitive_value in zip(
                left, zero_total, primitive
            )
        )
        self.assertEqual(sum(right) - sum(left), steps * period)
        witness = zero_total_relation_orbit_witness(capacities, left, right)
        self.assertTrue(witness.same_orbit)
        self.assertEqual(witness.kernel_shift_steps, steps)
        self.assertEqual(witness.zero_total_update, zero_total)
        self.assertEqual(
            weighted_relation_field(capacities, witness.shifted_left),
            weighted_relation_field(capacities, right),
        )

    def test_single_vertex_relation_space_has_one_orbit_class(self):
        capacities = (9,)
        self.assertEqual(relation_translation_period(capacities), 1)
        for left in range(-5, 6):
            for right in range(-5, 6):
                witness = zero_total_relation_orbit_witness(
                    capacities, (left,), (right,)
                )
                self.assertTrue(witness.same_orbit)
                self.assertEqual(witness.zero_total_update, (0,))
                self.assertEqual(
                    weighted_relation_field(capacities, witness.shifted_left),
                    weighted_relation_field(capacities, (right,)),
                )

    def test_invalid_state_shapes_are_rejected(self):
        with self.assertRaises(ValueError):
            relation_zero_total_orbit_residue((), ())
        with self.assertRaises(ValueError):
            relation_zero_total_orbit_residue((1, 2), (0,))
        with self.assertRaises(ValueError):
            relation_fields_share_zero_total_orbit((1, 2), (0, 0), (0, True))
        with self.assertRaises(ValueError):
            relation_field_total_residue_is_well_defined(
                (1, 2), (0, 0), (1, 0)
            )


if __name__ == "__main__":
    unittest.main()
