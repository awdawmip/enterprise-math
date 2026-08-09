import unittest
from heapq import heappop, heappush
from itertools import count

from enterprise_math.causal_block_future_budget import (
    budget_continuation_type,
    budget_cuts,
    budget_partition_is_nested,
    budget_remainder_intervals,
    cut_revelation_costs,
    eventual_intervals_match_gcd_scale,
    future_signature_for_remainder,
    remainder_distinguishing_cost,
    residue_minimum_costs,
    ultimate_refinement_scale,
)


def _reachable_sums(generators, costs, budget):
    serial = count()
    queue = [(0, next(serial), 0)]
    best_cost = {0: 0}
    while queue:
        current_cost, _, total = heappop(queue)
        if current_cost != best_cost[total]:
            continue
        for generator, edge_cost in zip(generators, costs):
            candidate_cost = current_cost + edge_cost
            if candidate_cost > budget:
                continue
            candidate_total = total + generator
            if candidate_cost >= best_cost.get(candidate_total, candidate_cost + 1):
                continue
            best_cost[candidate_total] = candidate_cost
            heappush(queue, (candidate_cost, next(serial), candidate_total))
    return tuple(sorted(best_cost))


class CausalBlockFutureBudgetTests(unittest.TestCase):
    def test_scale_twelve_plus_eight_reveals_nonuniform_then_uniform_partition(self):
        d = 12
        generators = (8,)
        costs = (3,)
        self.assertEqual(ultimate_refinement_scale(d, generators), 4)
        self.assertEqual(
            residue_minimum_costs(d, generators, costs),
            (0, None, None, None, 6, None, None, None, 3, None, None, None),
        )
        cut_costs = cut_revelation_costs(d, generators, costs)
        self.assertEqual(cut_costs[4], 3)
        self.assertEqual(cut_costs[8], 6)

        self.assertEqual(budget_remainder_intervals(d, generators, costs, 2), ((0, 12),))
        self.assertEqual(
            budget_remainder_intervals(d, generators, costs, 3),
            ((0, 4), (4, 12)),
        )
        self.assertEqual(
            budget_remainder_intervals(d, generators, costs, 6),
            ((0, 4), (4, 8), (8, 12)),
        )
        self.assertTrue(eventual_intervals_match_gcd_scale(d, generators, costs))

    def test_budget_interval_partition_matches_direct_future_signatures(self):
        cases = (
            (12, (8,), (3,), 0),
            (12, (8,), (3,), 3),
            (12, (8,), (3,), 6),
            (10, (4, 6), (2, 5), 9),
            (18, (6, 10), (4, 3), 15),
        )
        for d, generators, costs, budget in cases:
            reachable = _reachable_sums(generators, costs, budget)
            signatures = {
                remainder: future_signature_for_remainder(remainder, d, reachable)
                for remainder in range(d)
            }
            for left in range(d):
                for right in range(d):
                    same_signature = signatures[left] == signatures[right]
                    same_type = (
                        budget_continuation_type(left, d, generators, costs, budget)
                        == budget_continuation_type(right, d, generators, costs, budget)
                    )
                    self.assertEqual(same_signature, same_type)

    def test_remainder_distinguishing_cost_is_first_cut_between_pair(self):
        d = 12
        generators = (8,)
        costs = (3,)
        self.assertIsNone(remainder_distinguishing_cost(0, 3, d, generators, costs))
        self.assertEqual(remainder_distinguishing_cost(3, 4, d, generators, costs), 3)
        self.assertEqual(remainder_distinguishing_cost(0, 7, d, generators, costs), 3)
        self.assertEqual(remainder_distinguishing_cost(4, 8, d, generators, costs), 6)
        self.assertEqual(remainder_distinguishing_cost(0, 11, d, generators, costs), 3)

    def test_eventual_partition_is_exactly_gcd_refinement_for_multiple_languages(self):
        cases = (
            (6, (2,), (5,)),
            (6, (4, 6), (3, 7)),
            (10, (4, 6), (2, 5)),
            (12, (8, 18), (7, 2)),
            (15, (6, 10), (4, 9)),
        )
        for d, generators, costs in cases:
            self.assertTrue(eventual_intervals_match_gcd_scale(d, generators, costs))

    def test_budget_refinement_is_nested(self):
        self.assertTrue(
            budget_partition_is_nested(
                18,
                (6, 10),
                (4, 3),
                maximum_budget=30,
            )
        )

    def test_unreachable_cut_never_appears(self):
        d = 12
        generators = (8,)
        costs = (3,)
        costs_by_cut = cut_revelation_costs(d, generators, costs)
        self.assertIsNone(costs_by_cut[1])
        self.assertIsNone(costs_by_cut[2])
        self.assertEqual(budget_cuts(d, generators, costs, 100), (4, 8))


if __name__ == "__main__":
    unittest.main()
