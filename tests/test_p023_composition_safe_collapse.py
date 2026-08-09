import ast
import inspect
import itertools
import unittest

import enterprise_math.composition_safe_collapse as safe
from enterprise_math.composition_safe_collapse import (
    canonical_class_ids,
    class_count,
    coarsest_one_step_repair,
    descends_through,
    fiber_constancy_witness,
    future_partition_sequence,
    future_signature,
    induced_map,
    one_step_transition_refinement,
    refines,
    stable_future_partition,
    transition_compatible,
)


class CompositionSafeCollapseTests(unittest.TestCase):
    def test_factorization_iff_fiber_constancy(self):
        domain = (0, 1, 2, 3)
        coarse = {0: "a", 1: "a", 2: "b", 3: "b"}
        good = {0: 5, 1: 5, 2: 7, 3: 7}
        bad = {0: 5, 1: 6, 2: 7, 3: 7}
        self.assertTrue(descends_through(domain, coarse, good))
        self.assertEqual(induced_map(domain, coarse, good), {"a": 5, "b": 7})
        self.assertFalse(descends_through(domain, coarse, bad))
        self.assertEqual(fiber_constancy_witness(domain, coarse, bad), (0, 1))
        with self.assertRaises(ValueError):
            induced_map(domain, coarse, bad)

    def test_one_step_repair_is_safe_and_refines_original(self):
        domain = (0, 1, 2, 3)
        coarse = {0: 0, 1: 0, 2: 1, 3: 1}
        observed = {0: "x", 1: "y", 2: "z", 3: "z"}
        repaired = coarsest_one_step_repair(domain, coarse, observed)
        self.assertTrue(refines(domain, repaired, coarse))
        self.assertTrue(descends_through(domain, repaired, observed))
        self.assertEqual(class_count(repaired), 3)

    def test_one_step_repair_is_coarsest_among_safe_refinements_bounded(self):
        domain = (0, 1, 2, 3)
        coarse = {0: 0, 1: 0, 2: 1, 3: 1}
        observed = {0: "x", 1: "y", 2: "z", 3: "z"}
        repaired = coarsest_one_step_repair(domain, coarse, observed)
        # Exhaust all partitions represented by labels in 0..3. Any candidate
        # that refines coarse and makes observed descend must refine repaired.
        for values in itertools.product(range(4), repeat=4):
            candidate = dict(zip(domain, values, strict=True))
            if refines(domain, candidate, coarse) and descends_through(
                domain, candidate, observed
            ):
                self.assertTrue(refines(domain, candidate, repaired))

    def test_future_refinement_separates_delayed_observation_difference(self):
        # 0 and 1 look equal now, and after one step, but differ after two steps.
        domain = (0, 1, 2, 3, 4, 5)
        transition = {0: 2, 1: 3, 2: 4, 3: 5, 4: 4, 5: 5}
        observation = {0: 0, 1: 0, 2: 0, 3: 0, 4: 1, 5: 2}
        stages = future_partition_sequence(domain, transition, observation)
        self.assertEqual(stages[0][0], stages[0][1])
        self.assertEqual(stages[1][0], stages[1][1])
        self.assertNotEqual(stages[2][0], stages[2][1])
        self.assertEqual(future_signature(0, transition, observation, 2), (0, 0, 1))
        self.assertEqual(future_signature(1, transition, observation, 2), (0, 0, 2))

    def test_stage_t_equals_depth_t_future_observation_equivalence(self):
        domain = (0, 1, 2, 3, 4)
        transition = {0: 1, 1: 2, 2: 2, 3: 4, 4: 4}
        observation = {0: "a", 1: "a", 2: "b", 3: "a", 4: "c"}
        stages = future_partition_sequence(domain, transition, observation)
        for depth, partition in enumerate(stages):
            for left in domain:
                for right in domain:
                    same_partition = partition[left] == partition[right]
                    same_signature = future_signature(
                        left, transition, observation, depth
                    ) == future_signature(right, transition, observation, depth)
                    self.assertEqual(same_partition, same_signature)

    def test_stable_partition_is_transition_compatible(self):
        domain = (0, 1, 2, 3, 4, 5)
        transition = {0: 2, 1: 3, 2: 4, 3: 5, 4: 4, 5: 5}
        observation = {0: 0, 1: 0, 2: 0, 3: 0, 4: 1, 5: 2}
        stable = stable_future_partition(domain, transition, observation)
        self.assertTrue(refines(domain, stable, observation))
        self.assertTrue(transition_compatible(domain, transition, stable))
        induced = induced_map(
            domain,
            stable,
            {state: stable[transition[state]] for state in domain},
        )
        self.assertTrue(induced)

    def test_stable_partition_is_coarsest_compatible_refinement_bounded(self):
        domain = (0, 1, 2, 3)
        transition = {0: 1, 1: 2, 2: 2, 3: 3}
        observation = {0: 0, 1: 0, 2: 1, 3: 1}
        stable = stable_future_partition(domain, transition, observation)
        for values in itertools.product(range(4), repeat=4):
            candidate = canonical_class_ids(domain, dict(zip(domain, values, strict=True)))
            if refines(domain, candidate, observation) and transition_compatible(
                domain, transition, candidate
            ):
                self.assertTrue(refines(domain, candidate, stable))

    def test_each_strict_round_increases_class_count_and_finite_bound(self):
        domain = tuple(range(7))
        transition = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 6}
        observation = {state: int(state == 6) for state in domain}
        stages = future_partition_sequence(domain, transition, observation)
        counts = [class_count(stage) for stage in stages]
        self.assertEqual(counts, sorted(counts))
        self.assertEqual(len(counts), len(set(counts)))
        self.assertLessEqual(len(stages) - 1, len(domain) - counts[0])
        self.assertTrue(transition_compatible(domain, transition, stages[-1]))

    def test_one_step_refinement_never_merges(self):
        domain = (0, 1, 2, 3)
        transition = {0: 1, 1: 1, 2: 3, 3: 3}
        partition = {0: 0, 1: 0, 2: 1, 3: 1}
        refined = one_step_transition_refinement(domain, transition, partition)
        self.assertTrue(refines(domain, refined, partition))

    def test_reference_module_has_no_float_or_true_division(self):
        tree = ast.parse(inspect.getsource(safe))
        floats = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.Constant) and isinstance(node.value, float)
        ]
        divisions = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div)
        ]
        self.assertEqual(floats, [])
        self.assertEqual(divisions, [])


if __name__ == "__main__":
    unittest.main()
