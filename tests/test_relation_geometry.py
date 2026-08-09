import itertools
import unittest

from enterprise_math.relation_field import pair_difference_field
from enterprise_math.relation_geometry import (
    directed_weighted_cut_sum,
    maximum_directed_weighted_cut_sum,
    zero_sum_quadratic_from_unit_relation_field,
    zero_total_graph_radius_from_weighted_field,
    zero_total_l1_energy_from_weighted_field,
)
from enterprise_math.weighted_relation_field import weighted_relation_field


class RelationGeometryTests(unittest.TestCase):
    def test_maximum_cut_recovers_positive_mass_graph_radius(self):
        capacity_sets = ((1, 1), (1, 1, 1), (2, 1, 3), (2, 2, 1, 4))
        for block_sizes in capacity_sets:
            count = len(block_sizes)
            for prefix in itertools.product(range(-2, 3), repeat=count - 1):
                totals = prefix + (-sum(prefix),)
                field = weighted_relation_field(block_sizes, totals)
                expected_radius = sum(value for value in totals if value > 0)
                self.assertEqual(
                    zero_total_graph_radius_from_weighted_field(
                        block_sizes, field
                    ),
                    expected_radius,
                )
                self.assertEqual(
                    zero_total_l1_energy_from_weighted_field(
                        block_sizes, field
                    ),
                    sum(abs(value) for value in totals),
                )
                self.assertEqual(
                    maximum_directed_weighted_cut_sum(field),
                    sum(block_sizes) * expected_radius,
                )

    def test_positive_subset_is_a_maximizing_cut(self):
        block_sizes = (2, 1, 3, 2, 4)
        totals = (3, -2, 0, 4, -5)
        field = weighted_relation_field(block_sizes, totals)
        positive = tuple(index for index, total in enumerate(totals) if total > 0)
        self.assertEqual(
            directed_weighted_cut_sum(field, positive),
            maximum_directed_weighted_cut_sum(field),
        )

    def test_unit_relation_square_sum_recovers_q(self):
        for count in range(2, 7):
            for prefix in itertools.product(range(-2, 3), repeat=count - 1):
                values = prefix + (-sum(prefix),)
                field = pair_difference_field(values)
                expected_q = sum(value * value for value in values) // 2
                self.assertEqual(
                    zero_sum_quadratic_from_unit_relation_field(field),
                    expected_q,
                )


if __name__ == "__main__":
    unittest.main()
