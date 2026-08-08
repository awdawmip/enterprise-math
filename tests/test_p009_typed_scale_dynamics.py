import unittest

from enterprise_math.typed_scale import (
    ScaleState,
    collapse_tagged,
    is_strict_rank_decrease,
    project_tagged,
)


class TestP009TypedScaleDynamics(unittest.TestCase):
    def test_every_strict_projection_decreases_scale_rank(self):
        scales = (1, 2, 3, 4, 6, 12)
        for scale in scales:
            for value in range(0, 121):
                state = ScaleState(scale, value)
                for target in scales:
                    if target >= scale or scale % target != 0:
                        continue
                    projected = project_tagged(state, target)
                    self.assertTrue(is_strict_rank_decrease(state, projected))

    def test_every_strict_collapse_decreases_value_rank(self):
        for scale in (1, 2, 3, 6):
            for value in range(0, 121):
                state = ScaleState(scale, value)
                for exponent in (2, 3, 4, 5):
                    collapsed = collapse_tagged(state, exponent)
                    if collapsed != state:
                        self.assertEqual(collapsed.scale, state.scale)
                        self.assertLess(collapsed.value, state.value)
                        self.assertTrue(is_strict_rank_decrease(state, collapsed))

    def test_projection_composition_to_same_target_is_path_independent(self):
        for value in range(0, 241):
            start = ScaleState(12, value)
            via_six = project_tagged(project_tagged(start, 6), 1)
            via_four = project_tagged(project_tagged(start, 4), 1)
            via_three = project_tagged(project_tagged(start, 3), 1)
            direct = project_tagged(start, 1)
            self.assertEqual(via_six, direct)
            self.assertEqual(via_four, direct)
            self.assertEqual(via_three, direct)

    def test_no_strict_edge_can_return_to_same_rank(self):
        scales = (1, 2, 3, 4, 6, 12)
        states = [ScaleState(scale, value) for scale in scales for value in range(0, 31)]
        for state in states:
            strict_successors = []
            for target in scales:
                if target < state.scale and state.scale % target == 0:
                    strict_successors.append(project_tagged(state, target))
            for exponent in (2, 3, 4):
                collapsed = collapse_tagged(state, exponent)
                if collapsed != state:
                    strict_successors.append(collapsed)
            for successor in strict_successors:
                self.assertTrue(is_strict_rank_decrease(state, successor))
                self.assertNotEqual(successor, state)

    def test_type_erasure_would_create_spurious_repeated_projection(self):
        start = ScaleState(100, 141)
        once = project_tagged(start, 10)
        self.assertEqual(once, ScaleState(10, 14))

        # The original typed arrow 100 -> 10 is no longer applicable.
        with self.assertRaises(ValueError):
            project_tagged(once, 100)

        # A further projection must name a genuinely new target scale, e.g. 10 -> 1.
        twice = project_tagged(once, 1)
        self.assertEqual(twice, ScaleState(1, 1))

    def test_invalid_projection_between_incomparable_scales_is_rejected(self):
        with self.assertRaises(ValueError):
            project_tagged(ScaleState(6, 20), 4)


if __name__ == "__main__":
    unittest.main()
