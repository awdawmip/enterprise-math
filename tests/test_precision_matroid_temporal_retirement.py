import unittest

from enterprise_math.precision_matroid_temporal_retirement import (
    maximum_weight_bases,
    nested_cardinality_retirement,
)


class MatroidTemporalRetirementTests(unittest.TestCase):
    def test_cardinality_optima_can_be_nested(self):
        early = ((0, 1), (1, 0), (1, 1), (0, 1))
        late = ((0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 1, 1))
        schedule = nested_cardinality_retirement((early, late), 2)
        self.assertTrue(schedule[1].issubset(schedule[0]))
        self.assertEqual(tuple(map(len, schedule)), (2, 1))

    def test_rank_increment_equals_retirement_count(self):
        early = ((1, 0), (0, 1), (1, 1))
        late = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
        schedule = nested_cardinality_retirement((early, late), 2)
        self.assertEqual(len(schedule[0]) - len(schedule[1]), 1)

    def test_nonuniform_weighted_optima_need_not_nest(self):
        early = ((0, 1), (1, 0), (1, 1), (0, 1))
        late = ((0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 1, 1))
        weights = (3, 2, 1, 3)
        early_opt = maximum_weight_bases(early, weights, 2)
        late_opt = maximum_weight_bases(late, weights, 2)
        self.assertEqual(set(early_opt), {frozenset({0, 1}), frozenset({1, 3})})
        self.assertEqual(late_opt, (frozenset({0, 2, 3}),))
        self.assertFalse(any(B0.issubset(B1) for B0 in early_opt for B1 in late_opt))


if __name__ == "__main__":
    unittest.main()
