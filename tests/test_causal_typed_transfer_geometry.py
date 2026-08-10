import unittest

from enterprise_math.causal_typed_transfer_geometry import (
    charge_class_direction_counts,
    charge_classes,
    charge_preserving_transfer_edges,
    full_anonymous_single_charge_geometry,
    primitive_transfer_preserves_charges,
    typed_a_component_ranks,
    typed_relation_rank,
    typed_relation_rank_closed_form,
)


class CausalTypedTransferGeometryTests(unittest.TestCase):
    def test_one_common_charge_recovers_full_complete_transfer_component(self):
        charges = full_anonymous_single_charge_geometry(5)
        self.assertEqual(charge_classes(charges), ((0, 1, 2, 3, 4),))
        self.assertEqual(len(charge_preserving_transfer_edges(charges)), 10)
        self.assertEqual(typed_relation_rank(charges), 4)
        self.assertEqual(typed_a_component_ranks(charges), (4,))
        self.assertEqual(charge_class_direction_counts(charges), (20,))

    def test_distinct_charge_species_split_primitive_geometry_into_complete_components(self):
        charges = ((1, 0), (1, 0), (0, 1), (1, 0), (0, 1), (2, 2))
        self.assertEqual(charge_classes(charges), ((0, 1, 3), (2, 4), (5,)))
        self.assertEqual(
            charge_preserving_transfer_edges(charges),
            ((0, 1), (0, 3), (1, 3), (2, 4)),
        )
        self.assertEqual(typed_a_component_ranks(charges), (2, 1, 0))
        self.assertEqual(typed_relation_rank(charges), 3)
        self.assertEqual(typed_relation_rank_closed_form(charges), 3)
        self.assertEqual(charge_class_direction_counts(charges), (6, 2, 0))

    def test_charge_preservation_is_exactly_equality_of_slot_charge_labels(self):
        charges = ((1, 2), (1, 2), (2, 1), (1, 2))
        for receiver in range(4):
            for donor in range(4):
                if receiver == donor:
                    continue
                self.assertEqual(
                    primitive_transfer_preserves_charges(charges, receiver, donor),
                    charges[receiver] == charges[donor],
                )

    def test_every_new_charge_class_removes_one_relation_rank_from_fixed_slot_count(self):
        cases = (
            (((0,), (0,), (0,), (0,)), 3),
            (((0,), (0,), (1,), (1,)), 2),
            (((0,), (1,), (2,), (3,)), 0),
        )
        for charges, expected_rank in cases:
            self.assertEqual(typed_relation_rank(charges), expected_rank)
            self.assertEqual(expected_rank, len(charges) - len(charge_classes(charges)))


if __name__ == "__main__":
    unittest.main()
