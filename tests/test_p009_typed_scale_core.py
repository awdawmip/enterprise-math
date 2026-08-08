import math
import unittest

from enterprise_math.core import collapse
from enterprise_math.typed_scale import (
    ScaleState,
    collapse_tagged,
    project_tagged,
    strict_rank_decrease,
)


class TestP009TypedScaleCore(unittest.TestCase):
    def test_projection_strictly_lowers_rank_for_proper_coarsening(self):
        for scale in range(2, 25):
            for target in range(1, scale):
                if scale % target != 0:
                    continue
                for value in range(0, 81):
                    before = ScaleState(scale, value)
                    after = project_tagged(before, target)
                    self.assertLess(after.scale, before.scale)
                    self.assertTrue(strict_rank_decrease(before, after))

    def test_collapse_strictly_lowers_rank_exactly_when_value_changes(self):
        for scale in range(1, 8):
            for exponent in range(1, 6):
                for value in range(0, 161):
                    before = ScaleState(scale, value)
                    after = collapse_tagged(before, exponent)
                    self.assertEqual(after.scale, before.scale)
                    changed = after.value != before.value
                    self.assertEqual(strict_rank_decrease(before, after), changed)
                    self.assertLessEqual(after.value, before.value)

    def test_projection_paths_to_same_target_are_identical(self):
        for value in range(0, 121):
            for d in range(1, 7):
                for a in range(1, 5):
                    for b in range(1, 5):
                        e = d * a
                        f = e * b
                        start = ScaleState(f, value)
                        via = project_tagged(project_tagged(start, e), d)
                        direct = project_tagged(start, d)
                        self.assertEqual(via, direct)

    def test_every_generated_strict_edge_lowers_one_common_rank(self):
        scales = (1, 2, 3, 4, 6, 12)
        exponents = (2, 3, 4)
        for scale in scales:
            for value in range(0, 81):
                state = ScaleState(scale, value)
                for target in scales:
                    if target >= scale or scale % target != 0:
                        continue
                    after = project_tagged(state, target)
                    self.assertTrue(strict_rank_decrease(state, after))
                for exponent in exponents:
                    after = collapse_tagged(state, exponent)
                    if after != state:
                        self.assertTrue(strict_rank_decrease(state, after))

    def test_terminal_sink_profile_is_lcm_power_profile(self):
        exponent_sets = ((2, 3), (2, 4), (3, 5), (2, 3, 4))
        for exponents in exponent_sets:
            lcm_exponent = math.lcm(*exponents)
            for value in range(0, 2001):
                fixed_by_all = all(collapse(value, p) == value for p in exponents)
                fixed_by_lcm = collapse(value, lcm_exponent) == value
                self.assertEqual(fixed_by_all, fixed_by_lcm)

    def test_mixed_collapse_projection_is_not_confluent(self):
        start = ScaleState(2, 3)
        collapse_then_project = project_tagged(collapse_tagged(start, 2), 1)
        project_then_collapse = collapse_tagged(project_tagged(start, 1), 2)
        self.assertEqual(collapse_then_project, ScaleState(1, 0))
        self.assertEqual(project_then_collapse, ScaleState(1, 1))
        self.assertNotEqual(collapse_then_project, project_then_collapse)

    def test_type_erasure_false_zero_attractor(self):
        start = ScaleState(12, 17)
        once = project_tagged(start, 6)
        same_target_again = project_tagged(once, 6)
        self.assertEqual(once, ScaleState(6, 8))
        self.assertEqual(same_target_again, once)
        self.assertEqual((17 // 2) // 2, 4)
        self.assertNotEqual(same_target_again.value, (17 // 2) // 2)

    def test_incomparable_projection_is_rejected(self):
        with self.assertRaises(ValueError):
            project_tagged(ScaleState(6, 17), 4)

    def test_invalid_tags_are_rejected(self):
        for bad_scale in (0, -1, True):
            with self.assertRaises(ValueError):
                ScaleState(bad_scale, 1)
        for bad_value in (-1, True):
            with self.assertRaises(ValueError):
                ScaleState(1, bad_value)


if __name__ == "__main__":
    unittest.main()
