import itertools
import unittest

from enterprise_math.dimension_contraction import balanced_power_energy
from enterprise_math.weighted_relation_field import weighted_relation_field
from enterprise_math.weighted_relation_geometry import (
    minimum_cross_pair_dispersion,
    minimum_expanded_pair_dispersion,
    zero_total_square_energy_from_weighted_relations,
)


def balanced_slots(block_size: int, total: int) -> tuple[int, ...]:
    magnitude = abs(total)
    q, r = divmod(magnitude, block_size)
    sign = -1 if total < 0 else 1
    values = (q + 1,) * r + (q,) * (block_size - r)
    if sign < 0:
        values = tuple(-value for value in values)
    return values


def pair_dispersion(values: tuple[int, ...]) -> int:
    return sum(
        (values[i] - values[j]) ** 2
        for i in range(len(values))
        for j in range(i + 1, len(values))
    )


class WeightedRelationGeometryTests(unittest.TestCase):
    def test_cross_pair_formula_matches_explicit_balanced_expansion(self):
        for left_size in range(1, 5):
            for right_size in range(1, 5):
                for left_total in range(-6, 7):
                    for right_total in range(-6, 7):
                        left = balanced_slots(left_size, left_total)
                        right = balanced_slots(right_size, right_total)
                        expected = sum((x - y) ** 2 for x in left for y in right)
                        relation = right_size * left_total - left_size * right_total
                        self.assertEqual(
                            minimum_cross_pair_dispersion(
                                left_size,
                                right_size,
                                left_total,
                                right_total,
                                relation,
                            ),
                            expected,
                        )

    def test_full_pair_dispersion_matches_explicit_balanced_expansion(self):
        capacity_sets = ((1, 1), (2, 1, 3), (2, 2, 1, 3))
        for block_sizes in capacity_sets:
            for totals in itertools.product(range(-3, 4), repeat=len(block_sizes)):
                field = weighted_relation_field(block_sizes, totals)
                expanded = tuple(
                    value
                    for block_size, total in zip(block_sizes, totals)
                    for value in balanced_slots(block_size, total)
                )
                self.assertEqual(
                    minimum_expanded_pair_dispersion(
                        block_sizes, field, sum(totals)
                    ),
                    pair_dispersion(expanded),
                )

    def test_zero_total_relation_geometry_recovers_square_energy(self):
        capacity_sets = ((1, 1), (2, 1, 3), (2, 2, 1, 3))
        for block_sizes in capacity_sets:
            count = len(block_sizes)
            for prefix in itertools.product(range(-3, 4), repeat=count - 1):
                totals = prefix + (-sum(prefix),)
                field = weighted_relation_field(block_sizes, totals)
                expected = sum(
                    balanced_power_energy(block_size, 2, total)
                    for block_size, total in zip(block_sizes, totals)
                )
                self.assertEqual(
                    zero_total_square_energy_from_weighted_relations(
                        block_sizes, field
                    ),
                    expected,
                )


if __name__ == "__main__":
    unittest.main()
