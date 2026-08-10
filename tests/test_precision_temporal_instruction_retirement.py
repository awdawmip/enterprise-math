import unittest

from enterprise_math.precision_temporal_instruction_retirement import (
    cut_clutter_weakens,
    minimum_transversals,
    optimal_nested_schedule,
)


class TemporalInstructionRetirementTests(unittest.TestCase):
    def test_anticipatory_redundancy_can_win(self):
        early = (("a",), ("b",))
        late = (("a", "c"), ("b", "c"))
        cost, schedule = optimal_nested_schedule(("a", "b", "c"), (early, late, late))
        self.assertEqual(cost, 5)
        self.assertEqual(schedule[0], frozenset({"a", "b", "c"}))
        self.assertEqual(schedule[1], frozenset({"c"}))
        self.assertEqual(schedule[2], frozenset({"c"}))

    def test_single_late_stage_ties_myopic_schedule(self):
        early = (("a",), ("b",))
        late = (("a", "c"), ("b", "c"))
        cost, _ = optimal_nested_schedule(("a", "b", "c"), (early, late))
        self.assertEqual(cost, 4)

    def test_local_optima_need_not_nest(self):
        early = (("a",), ("b",))
        late = (("a", "c"), ("b", "c"))
        self.assertEqual(minimum_transversals(("a", "b", "c"), early), (frozenset({"a", "b"}),))
        self.assertEqual(minimum_transversals(("a", "b", "c"), late), (frozenset({"c"}),))

    def test_cut_weakening_direction(self):
        early = (("a",), ("b",))
        late = (("a", "c"), ("b", "c"))
        self.assertTrue(cut_clutter_weakens(early, late))
        self.assertFalse(cut_clutter_weakens(late, early))

    def test_more_future_cannot_need_fewer_generators(self):
        early = (("a",), ("b",), ("c",))
        late = (("a", "b"), ("b", "c"))
        self.assertLessEqual(
            len(minimum_transversals(("a", "b", "c"), late)[0]),
            len(minimum_transversals(("a", "b", "c"), early)[0]),
        )


if __name__ == "__main__":
    unittest.main()
