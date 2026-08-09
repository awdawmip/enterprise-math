import unittest

from enterprise_math.collapse_incidence import (
    collapse_incidence_report,
    insertion_spectrum_delta,
    overlap_spectrum_from_occupancies,
)
from enterprise_math.common_collapse import (
    common_collapse_multiplicity,
    iter_terminal_collapse_targets,
)
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

    def test_pascal_insertion_delta_matches_full_spectrum_recomputation(self):
        occupancies = {(0, 0): 3, (1, 0): 1, (2, 0): 0}
        targets = ((0, 0), (1, 0), (2, 0))
        old = dict(overlap_spectrum_from_occupancies(occupancies, max_order=4))
        delta = dict(insertion_spectrum_delta(occupancies, targets, max_order=4))
        updated = dict(occupancies)
        for target in targets:
            updated[target] = updated.get(target, 0) + 1
        new = dict(overlap_spectrum_from_occupancies(updated, max_order=4))
        for order in range(2, 5):
            self.assertEqual(new[order] - old[order], delta[order])
        self.assertEqual(delta, {2: 4, 3: 3, 4: 1})

    def test_incremental_spectrum_tracks_actual_body_insertions(self):
        bodies = [
            Body2D(0, 0, 0, 1),
            Body2D(1, 1, 0, 1),
            Body2D(2, 0, 1, 1),
            Body2D(3, 3, 0, 2),
        ]
        occupancies = {}
        spectrum = {}
        for index, body in enumerate(bodies):
            targets = tuple(iter_terminal_collapse_targets(body))
            future_max = max(
                (occupancies.get(target, 0) + 1 for target in targets), default=0
            )
            max_order = max(2, future_max)
            delta = dict(
                insertion_spectrum_delta(
                    occupancies, targets, max_order=max_order
                )
            )
            for order, increment in delta.items():
                spectrum[order] = spectrum.get(order, 0) + increment
            for target in targets:
                occupancies[target] = occupancies.get(target, 0) + 1

            recomputed = dict(
                overlap_spectrum_from_occupancies(
                    occupancies,
                    max_order=max(2, max(occupancies.values(), default=0)),
                )
            )
            for order, value in recomputed.items():
                self.assertEqual(spectrum.get(order, 0), value)
            report = collapse_incidence_report(bodies[: index + 1])
            self.assertEqual(dict(report.overlap_spectrum), {
                order: value for order, value in spectrum.items() if value or order <= report.max_target_occupancy
            })

    def test_duplicate_targets_in_one_insertion_are_rejected(self):
        with self.assertRaises(ValueError):
            insertion_spectrum_delta({(0, 0): 1}, ((0, 0), (0, 0)))

    def test_unique_ids_are_required(self):
        with self.assertRaises(ValueError):
            collapse_incidence_report([Body2D(0, 0, 0, 1), Body2D(0, 1, 1, 1)])


if __name__ == "__main__":
    unittest.main()
