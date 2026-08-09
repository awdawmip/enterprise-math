import itertools
import unittest

from enterprise_math.relation_field import (
    block_cut_sum,
    block_imbalance_from_values,
    pair_difference_field,
    pair_dispersion_from_field,
    recover_values_from_field,
    relation_field_is_closed,
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
