import unittest

from enterprise_math.contraction_atlas import (
    chart_index_identity,
    chart_index_product,
    chart_matrix,
    imbalance_tags,
    internal_block_sizes,
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

    def test_chart_determinant_equals_internal_size_product(self):
        for leaf_count in range(1, 7):
            labels = tuple(range(leaf_count))
            for tree in ordered_binary_trees(labels):
                determinant, product = chart_index_identity(tree)
                self.assertEqual(determinant, product, msg=tree)

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
