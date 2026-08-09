import itertools
import unittest

from enterprise_math.contraction_atlas import (
    chart_index_identity,
    chart_index_product,
    chart_matrix,
    imbalance_tags,
    internal_block_sizes,
    recover_leaf_totals_from_split_flows,
    split_flow_coordinates,
    split_flow_transform_determinant,
    split_flows_to_preorder_imbalances,
)


def ordered_binary_trees(labels: tuple[int, ...]):
    if len(labels) == 1:
        yield labels[0]
        return
    for split in range(1, len(labels)):
        for left in ordered_binary_trees(labels[:split]):
            for right in ordered_binary_trees(labels[split:]):
                yield (left, right)


class ContractionAtlasTests(unittest.TestCase):
    def test_known_four_slot_chart_indices(self):
        chain = (((0, 1), 2), 3)
        balanced = ((0, 1), (2, 3))
        self.assertEqual(internal_block_sizes(chain), (2, 3, 4))
        self.assertEqual(internal_block_sizes(balanced), (2, 2, 4))
        self.assertEqual(chart_index_product(chain), 24)
        self.assertEqual(chart_index_product(balanced), 16)
        self.assertEqual(chart_index_identity(chain), (24, 24))
        self.assertEqual(chart_index_identity(balanced), (16, 16))
        self.assertEqual(split_flow_transform_determinant(chain), 24)
        self.assertEqual(split_flow_transform_determinant(balanced), 16)

    def test_chart_determinant_equals_internal_size_product(self):
        for leaf_count in range(1, 7):
            labels = tuple(range(leaf_count))
            for tree in ordered_binary_trees(labels):
                determinant, product = chart_index_identity(tree)
                self.assertEqual(determinant, product, msg=tree)
                self.assertEqual(
                    split_flow_transform_determinant(tree),
                    product,
                    msg=tree,
                )

    def test_split_flow_chart_accepts_arbitrary_integer_coordinates(self):
        trees = (
            (((0, 1), 2), 3),
            ((0, 1), (2, 3)),
            (0, (1, (2, 3))),
        )
        for tree in trees:
            for root_total in range(-3, 4):
                for flows in itertools.product(range(-2, 3), repeat=3):
                    leaves = recover_leaf_totals_from_split_flows(
                        tree, root_total, flows
                    )
                    self.assertEqual(sum(leaves.values()), root_total)
                    self.assertEqual(split_flow_coordinates(tree, leaves), flows)

    def test_split_flow_to_imbalance_tags_matches_leaf_state(self):
        tree = ((0, 1), (2, 3))
        for root_total in range(-3, 4):
            for flows in itertools.product(range(-2, 3), repeat=3):
                leaves = recover_leaf_totals_from_split_flows(
                    tree, root_total, flows
                )
                preorder_tags = split_flows_to_preorder_imbalances(
                    tree, root_total, flows
                )
                left_total = leaves[0] + leaves[1]
                right_total = leaves[2] + leaves[3]
                expected = (
                    2 * left_total - 2 * right_total,
                    leaves[0] - leaves[1],
                    leaves[2] - leaves[3],
                )
                self.assertEqual(preorder_tags, expected)

    def test_chart_matrix_maps_zero_sum_basis_to_tags(self):
        tree = ((0, 1), (2, 3))
        matrix = chart_matrix(tree)
        leaves = (0, 1, 2, 3)
        dependent = leaves[-1]
        for column, leaf in enumerate(leaves[:-1]):
            state = {label: 0 for label in leaves}
            state[leaf] = 1
            state[dependent] = -1
            expected = imbalance_tags(tree, state)
            actual = tuple(row[column] for row in matrix)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
