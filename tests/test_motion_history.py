import unittest

from enterprise_math.engineering_collision import Body2D
from enterprise_math.motion_history import run_open_loop_motion_program


class MotionHistoryTests(unittest.TestCase):
    def test_distinct_response_histories_can_merge_to_same_terminal_state(self):
        initial = [
            Body2D(0, -2, 0, 0),
            Body2D(1, 0, 0, 0),
        ]
        schedule = [
            {0: (1, 0), 1: (-1, 0)},
            {0: (-1, 0), 1: (0, 0)},
            {0: (1, 0), 1: (-1, 0)},
        ]
        report = run_open_loop_motion_program(initial, schedule)
        fibers = dict(report.terminal_histories)
        merged_state = (Body2D(0, -2, 0, 0), Body2D(1, -1, 0, 0))
        self.assertIn(merged_state, fibers)
        self.assertEqual(
            set(fibers[merged_state]),
            {
                (frozenset({0}), frozenset({0}), frozenset({1})),
                (frozenset({1}), frozenset({0}), frozenset({0})),
            },
        )
        self.assertGreaterEqual(dict(report.history_collision_spectrum)[2], 1)

    def test_one_tick_frontier_matches_expected_symmetric_branching(self):
        initial = [Body2D(0, -1, 0, 0), Body2D(1, 1, 0, 0)]
        schedule = [{0: (1, 0), 1: (-1, 0)}]
        report = run_open_loop_motion_program(initial, schedule)
        self.assertEqual(report.ticks, 1)
        self.assertEqual(report.history_count, 2)
        self.assertEqual(report.terminal_state_count, 2)
        self.assertEqual(dict(report.history_collision_spectrum)[1], 2)
        self.assertEqual(dict(report.history_collision_spectrum).get(2, 0), 0)

    def test_independent_program_has_one_history_and_one_terminal_state(self):
        initial = [Body2D(0, 0, 0, 0), Body2D(1, 5, 0, 0)]
        schedule = [
            {0: (1, 0), 1: (-1, 0)},
            {0: (1, 0), 1: (-1, 0)},
        ]
        report = run_open_loop_motion_program(initial, schedule)
        self.assertEqual(report.history_count, 1)
        self.assertEqual(report.terminal_state_count, 1)
        self.assertEqual(report.history_collision_spectrum, ((1, 1),))
        terminal, histories = report.terminal_histories[0]
        self.assertEqual(terminal, (Body2D(0, 2, 0, 0), Body2D(1, 3, 0, 0)))
        self.assertEqual(histories, ((frozenset({0, 1}), frozenset({0, 1})),))

    def test_input_body_order_does_not_change_frontier(self):
        initial = [Body2D(0, -2, 0, 0), Body2D(1, 0, 0, 0)]
        schedule = [
            {0: (1, 0), 1: (-1, 0)},
            {0: (-1, 0), 1: (0, 0)},
            {0: (1, 0), 1: (-1, 0)},
        ]
        self.assertEqual(
            run_open_loop_motion_program(initial, schedule),
            run_open_loop_motion_program(list(reversed(initial)), schedule),
        )

    def test_schedule_must_name_every_body_exactly_once(self):
        initial = [Body2D(0, 0, 0, 0), Body2D(1, 5, 0, 0)]
        with self.assertRaises(ValueError):
            run_open_loop_motion_program(initial, [{0: (1, 0)}])
        with self.assertRaises(ValueError):
            run_open_loop_motion_program(initial, [{0: (1, 0), 1: (0, 0), 2: (0, 0)}])


if __name__ == "__main__":
    unittest.main()
