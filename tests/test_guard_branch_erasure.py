import itertools
import unittest

from enterprise_math.guard_branch_erasure import (
    rank_one_branch_erasure_report,
    rank_one_reachable_patterns,
    rank_two_branch_erasure_report,
)


def complete_effect_table(guard_count, default="same"):
    return {
        pattern: default
        for pattern in itertools.product((False, True), repeat=guard_count)
    }


class GuardBranchErasureTests(unittest.TestCase):
    def test_rank_one_sweep_matches_direct_integer_line_enumeration(self):
        steps = ((1, 1), (1, -1), (2, 3, -1), (0, 2, -3, 1))
        for step in steps:
            for base in itertools.product(range(-3, 4), repeat=len(step)):
                closed = set(rank_one_reachable_patterns(base, step))
                brute = {
                    tuple(
                        base[index] + t * step[index] >= 0
                        for index in range(len(step))
                    )
                    for t in range(-80, 81)
                }
                self.assertEqual(closed, brute, msg=(base, step))
                self.assertLessEqual(
                    len(closed), 1 + sum(delta != 0 for delta in step)
                )

    def test_rank_one_unreachable_branch_effects_create_no_obligation(self):
        base = (0, 0)
        step = (1, 1)
        effects = complete_effect_table(2, "kept")
        # Only (F,F) and (T,T) are reachable. Give the mixed patterns arbitrary
        # different effects; they must not make the quotient unsafe.
        effects[(False, True)] = "unreachable-a"
        effects[(True, False)] = "unreachable-b"
        report = rank_one_branch_erasure_report(base, step, effects)
        self.assertEqual(
            set(report.reachable_patterns),
            {(False, False), (True, True)},
        )
        self.assertTrue(report.safe_to_erase)
        self.assertEqual(report.distinct_effects, ("kept",))

    def test_rank_one_reachable_effect_difference_is_not_safe(self):
        base = (0, 0)
        step = (1, 1)
        effects = complete_effect_table(2, "same")
        effects[(True, True)] = "different"
        report = rank_one_branch_erasure_report(base, step, effects)
        self.assertFalse(report.safe_to_erase)
        self.assertEqual(set(report.distinct_effects), {"same", "different"})

    def test_rank_two_unreachable_pattern_does_not_force_precision(self):
        # scores=(s,t,s+t). Pattern (F,F,T) is impossible: s,t<0 implies s+t<0.
        generators = ((1, 0, 1), (0, 1, 1))
        base = (0, 0, 0)
        effects = complete_effect_table(3, "same")
        effects[(False, False, True)] = "unreachable-only"
        report = rank_two_branch_erasure_report(base, generators, effects)
        self.assertNotIn((False, False, True), report.reachable_patterns)
        self.assertTrue(report.safe_to_erase)
        self.assertEqual(report.distinct_effects, ("same",))

    def test_rank_two_reachable_effect_difference_is_not_safe(self):
        generators = ((1, 0, 1), (0, 1, 1))
        base = (0, 0, 0)
        effects = complete_effect_table(3, "same")
        effects[(True, False, True)] = "different"
        report = rank_two_branch_erasure_report(base, generators, effects)
        self.assertIn((True, False, True), report.reachable_patterns)
        self.assertFalse(report.safe_to_erase)
        self.assertEqual(set(report.distinct_effects), {"same", "different"})

    def test_branch_table_must_be_complete(self):
        with self.assertRaises(ValueError):
            rank_one_branch_erasure_report(
                (0, 0),
                (1, 1),
                {(False, False): "only-one"},
            )


if __name__ == "__main__":
    unittest.main()
