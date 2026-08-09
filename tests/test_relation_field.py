import itertools
import unittest

from enterprise_math.relation_field import (
    anchor_chart_index,
    anchor_chart_is_legal,
    anchor_difference_coordinates,
    block_cut_sum,
    block_imbalance_from_values,
    field_from_anchor_coordinates,
    pair_difference_field,
    pair_dispersion_from_field,
    recover_values_from_anchor_coordinates,
    recover_values_from_field,
    recover_values_from_tree_flows,
    relation_field_is_closed,
    tree_flow_chart_index,
    tree_flow_coordinates,
)


class RelationFieldTests(unittest.TestCase):
    def test_difference_field_is_closed_and_recovers_values(self):
        for size in range(1, 6):
            for values in itertools.product(range(-2, 3), repeat=size):
                field = pair_difference_field(values)
                self.assertTrue(relation_field_is_closed(field))
                self.assertEqual(
                    recover_values_from_field(field, sum(values)),
                    values,
                )

    def test_anchor_coordinates_recover_state_for_every_anchor(self):
        for size in range(1, 7):
            for values in itertools.product(range(-2, 3), repeat=size):
                total = sum(values)
                for anchor in range(size):
                    coordinates = anchor_difference_coordinates(values, anchor)
                    self.assertTrue(anchor_chart_is_legal(coordinates, total))
                    self.assertEqual(
                        recover_values_from_anchor_coordinates(
                            coordinates, total, anchor
                        ),
                        values,
                    )
                    self.assertEqual(
                        field_from_anchor_coordinates(coordinates, total, anchor),
                        pair_difference_field(values),
                    )

    def test_anchor_legality_has_exact_index_n(self):
        # Modulo N, exactly N^(N-2) of N^(N-1) coordinate residues are legal.
        for slot_count in range(1, 7):
            coordinate_count = slot_count - 1
            total = 3
            legal = sum(
                anchor_chart_is_legal(coordinates, total)
                for coordinates in itertools.product(
                    range(slot_count), repeat=coordinate_count
                )
            )
            expected = 1 if slot_count == 1 else slot_count ** (slot_count - 2)
            self.assertEqual(legal, expected)
            self.assertEqual(anchor_chart_index(slot_count), slot_count)

    def test_anchor_rejects_illegal_congruence(self):
        with self.assertRaises(ValueError):
            recover_values_from_anchor_coordinates((0, 0), total=1)
        self.assertFalse(anchor_chart_is_legal((0, 0), total=1))

    def test_tree_flow_chart_is_unimodular_for_path_and_star(self):
        for size in range(1, 7):
            # Path rooted at 0: 0->1->2->... .
            path_parents = tuple(-1 if vertex == 0 else vertex - 1 for vertex in range(size))
            # Star rooted at 0.
            star_parents = tuple(-1 if vertex == 0 else 0 for vertex in range(size))
            for parents in (path_parents, star_parents):
                for values in itertools.product(range(-2, 3), repeat=size):
                    total = sum(values)
                    flows = tree_flow_coordinates(values, parents, root=0)
                    self.assertEqual(
                        recover_values_from_tree_flows(
                            flows, total, parents, root=0
                        ),
                        values,
                    )
                self.assertEqual(tree_flow_chart_index(size), 1)

    def test_arbitrary_tree_flows_are_legal_integer_states(self):
        parents = (-1, 0, 0, 1, 1, 2)
        for total in range(-3, 4):
            for flows in itertools.product(range(-2, 3), repeat=5):
                values = recover_values_from_tree_flows(
                    flows, total, parents, root=0
                )
                self.assertEqual(sum(values), total)
                self.assertEqual(
                    tree_flow_coordinates(values, parents, root=0),
                    flows,
                )

    def test_path_flow_chart_is_prefix_or_suffix_sum_basis(self):
        # With path 0->1->2->3, the non-root flows are suffix sums.
        values = (3, -2, 5, -6)
        parents = (-1, 0, 1, 2)
        self.assertEqual(tree_flow_coordinates(values, parents, 0), (-3, -1, -6))
        self.assertEqual(
            recover_values_from_tree_flows((-3, -1, -6), 0, parents, 0),
            values,
        )

    def test_every_block_imbalance_is_a_cut_sum(self):
        values = (3, -2, 5, -4, 1)
        field = pair_difference_field(values)
        indices = tuple(range(len(values)))
        for mask in range(1, (1 << len(values)) - 1):
            left = tuple(index for index in indices if mask & (1 << index))
            right = tuple(index for index in indices if not mask & (1 << index))
            self.assertEqual(
                block_cut_sum(field, left, right),
                block_imbalance_from_values(values, left, right),
            )

    def test_pair_dispersion_is_relation_field_square_sum(self):
        for size in range(2, 7):
            for prefix in itertools.product(range(-2, 3), repeat=size - 1):
                values = prefix + (-sum(prefix),)
                field = pair_difference_field(values)
                expected = sum(
                    (values[i] - values[j]) ** 2
                    for i in range(size)
                    for j in range(i + 1, size)
                )
                self.assertEqual(pair_dispersion_from_field(field), expected)
                self.assertEqual(
                    expected,
                    size * sum(value * value for value in values),
                )

    def test_zero_sum_field_alone_recovers_state(self):
        for size in range(2, 7):
            for prefix in itertools.product(range(-2, 3), repeat=size - 1):
                values = prefix + (-sum(prefix),)
                field = pair_difference_field(values)
                self.assertEqual(recover_values_from_field(field, 0), values)


if __name__ == "__main__":
    unittest.main()
