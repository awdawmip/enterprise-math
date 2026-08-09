import unittest

from enterprise_math.collapse_incidence import collapse_incidence_report
from enterprise_math.common_collapse import common_collapse_multiplicity
from enterprise_math.engineering_collision import Body2D, exact_collision_pairs


class CollapseIncidenceTests(unittest.TestCase):
    def test_incidence_collision_support_matches_exact_pairs(self):
        bodies = [
            Body2D(0, -3, -1, 2),
            Body2D(1, 0, 0, 1),
            Body2D(2, 4, 0, 2),
            Body2D(3, 10, 5, 0),
            Body2D(4, 10, 5, 1),
        ]
        report = collapse_incidence_report(bodies)
        self.assertEqual(report.collision_pairs, exact_collision_pairs(bodies))
        reversed_report = collapse_incidence_report(list(reversed(bodies)))
        self.assertEqual(report, reversed_report)

    def test_pair_multiplicity_is_shared_target_count(self):
        bodies = [
            Body2D(0, 0, 0, 2),
            Body2D(1, 2, 1, 2),
            Body2D(2, -2, 0, 1),
        ]
        report = collapse_incidence_report(bodies)
        multiplicities = dict(report.pair_multiplicities)
        for left_index, left in enumerate(bodies):
            for right in bodies[left_index + 1 :]:
                expected = common_collapse_multiplicity(left, right)
                pair = (left.body_id, right.body_id)
                self.assertEqual(multiplicities.get(pair, 0), expected)

    def test_second_order_spectrum_double_counts_pair_witnesses(self):
        bodies = [
            Body2D(0, 0, 0, 1),
            Body2D(1, 1, 0, 1),
            Body2D(2, 0, 1, 1),
        ]
        report = collapse_incidence_report(bodies)
        spectrum = dict(report.overlap_spectrum)
        self.assertEqual(spectrum[2], sum(count for _pair, count in report.pair_multiplicities))
        self.assertGreater(spectrum.get(3, 0), 0)

    def test_three_bodies_on_one_target_give_binomial_spectrum(self):
        bodies = [Body2D(body_id, 7, -2, 0) for body_id in range(3)]
        report = collapse_incidence_report(bodies)
        self.assertEqual(report.emitted_memberships, 3)
        self.assertEqual(report.occupied_targets, 1)
        self.assertEqual(report.max_target_occupancy, 3)
        self.assertEqual(report.overlap_spectrum, ((2, 3), (3, 1)))
        self.assertEqual(len(report.collision_pairs), 3)

    def test_unique_ids_are_required(self):
        with self.assertRaises(ValueError):
            collapse_incidence_report([Body2D(0, 0, 0, 1), Body2D(0, 1, 1, 1)])


if __name__ == "__main__":
    unittest.main()
