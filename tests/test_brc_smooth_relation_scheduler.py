from __future__ import annotations

import unittest

from enterprise_math.brc_multiplier_factor_scan import admissible_root_state_sequence
from enterprise_math.brc_smooth_relation_scheduler import minimum_gap_relation_points


class BRCSmoothRelationSchedulerTests(unittest.TestCase):
    def test_minimum_gap_stream_is_sorted_and_exact(self) -> None:
        n = 14111
        states = admissible_root_state_sequence(n)
        points = tuple(minimum_gap_relation_points(states, 500))
        gaps = tuple(point.gap for point in points)
        self.assertEqual(gaps, tuple(sorted(gaps)))
        for point in points:
            self.assertEqual(
                point.x * point.x - point.gap,
                point.state.multiplier * n,
            )

    def test_scheduler_matches_bruteforce_prefix_of_union(self) -> None:
        n = 18721
        states = admissible_root_state_sequence(n)
        expected = []
        # 40 vertical points per strip are ample for the first 300 union values
        # in this small deterministic regression.
        for state in states:
            target = state.multiplier * n
            root = state.root if state.remainder == 0 else state.root + 1
            for t in range(40):
                x = root + t
                expected.append((x * x - target, state.multiplier, t, x))
        expected.sort()
        observed = tuple(minimum_gap_relation_points(states, 300))
        self.assertEqual(
            tuple((p.gap, p.state.multiplier, p.vertical_offset, p.x) for p in observed),
            tuple(expected[:300]),
        )

    def test_every_strip_starts_with_its_ceiling_gap(self) -> None:
        n = 24961
        states = admissible_root_state_sequence(n)
        points = tuple(minimum_gap_relation_points(states, len(states)))
        # The first len(states) global points need not contain every strip, but
        # every emitted offset-zero point is the exact ceiling gap of that strip.
        for point in points:
            if point.vertical_offset == 0:
                expected_x = point.state.root if point.state.remainder == 0 else point.state.root + 1
                self.assertEqual(point.x, expected_x)


if __name__ == "__main__":
    unittest.main()
