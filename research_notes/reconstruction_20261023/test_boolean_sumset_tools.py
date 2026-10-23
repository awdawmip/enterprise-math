"""Meaningful finite checks against exhaustive independent subset enumeration."""
import itertools
import random
import unittest

from boolean_sumset_tools import (add, hard_targets, hard_targets_closed_form, layers, producer_clauses,
                                 simplex, solve_budget, sumset, support,
                                 support_obstructions)


class ExactBooleanToolsTests(unittest.TestCase):
    def test_producers_and_search_against_bruteforce(self):
        rng = random.Random(2301026)
        outcomes = set()
        for _ in range(80):
            universe = simplex(3, 3)
            rng.shuffle(universe)
            base, candidates = tuple(universe[:3]), tuple(universe[3:8])
            targets = tuple(rng.sample(simplex(6, 3), rng.randrange(9)))
            _, clauses = producer_clauses(targets, base, candidates)
            for budget in range(6):
                expected = any(set(targets) <= sumset(base + chosen)
                               for size in range(budget + 1)
                               for chosen in itertools.combinations(candidates, size))
                answer = solve_budget(clauses, budget)
                outcomes.add(answer.status)
                self.assertEqual(answer.status == 'YES', expected)
                if expected:
                    chosen = tuple(candidates[i] for i in answer.selected)
                    self.assertLessEqual(len(chosen), budget)
                    self.assertTrue(set(targets) <= sumset(base + chosen))
        self.assertEqual(outcomes, {'YES', 'NO'})

    def test_unknown_and_empty_clause_boundaries(self):
        self.assertEqual(solve_budget(((1, 2),), 1, 0).status, 'UNKNOWN')
        self.assertEqual(solve_budget(((),), 4).status, 'NO')
        self.assertEqual(solve_budget((), 0).status, 'YES')
        self.assertEqual(solve_budget(((3,),), 1).status, 'NO')

    def test_general_saturation_for_every_single_two_support_deletion(self):
        # Recheck n=7..12 without assuming one particular deleted pair.
        for n in range(7, 13):
            population = simplex(n)
            low = [p for p in population if support(p) <= 2]
            full = [p for p in population if support(p) == 4]
            full_sums = sumset(full)
            producers = {}
            for r in low:
                for x in full:
                    producers.setdefault(add(r, x), set()).add(r)
            for target in simplex(2*n):
                if support(target) != 4 or target in full_sums:
                    continue
                choices = producers.get(target, set())
                self.assertTrue(choices, (n, target))
                self.assertTrue(len(choices) >= 2 or support(next(iter(choices))) == 1,
                                (n, target, choices))

    def test_degree_six_counterexample_and_degree_eight_hard_targets(self):
        low, _, full = layers(6, (3, 3, 0, 0))
        self.assertNotIn((4, 4, 1, 3), sumset(low + full))
        hard = hard_targets(8, (4, 4, 0, 0))
        self.assertEqual(len(hard), 12)
        self.assertTrue(all(support(p) == 3 for p in hard))

    def test_closed_form_against_every_deletion_and_all_nonfull_targets(self):
        for n in range(2, 11):
            for removed in simplex(n):
                if support(removed) != 2:
                    continue
                actual = hard_targets(n, removed)
                formula = hard_targets_closed_form(n, removed)
                self.assertEqual(actual, formula, (n, removed))
                a, b = [x for x in removed if x]
                self.assertEqual(len(formula), 2*(n-2)+(a==1)+(b==1))

    def test_known_66_state_witness(self):
        low, x3, x4 = layers(8)
        q = (0, 3, 4, 47, 48, 51, 71, 73, 74)
        w = (0, 4, 7, 10, 11, 12, 14, 15, 25, 29, 31, 34)
        self.assertEqual(support_obstructions(8, (4,4,0,0), tuple(x3[i] for i in q)), ())
        actual = sumset(low + tuple(x3[i] for i in q) + tuple(x4[i] for i in w))
        self.assertEqual(actual, set(simplex(16)))
        self.assertEqual(len(actual), 969)


if __name__ == '__main__':
    unittest.main()
