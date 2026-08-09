import ast
import inspect
import itertools
import unittest

import enterprise_math.operation_quotient as oq
from enterprise_math.operation_quotient import (
    class_count,
    family_descends,
    family_future_partition_sequence,
    refines,
    stable_family_partition,
    word_observation_signature,
)


class OperationQuotientTests(unittest.TestCase):
    def test_family_refinement_detects_generator_specific_difference(self):
        domain = (0, 1, 2, 3)
        operations = {
            "f": {0: 2, 1: 2, 2: 2, 3: 3},
            "g": {0: 2, 1: 3, 2: 2, 3: 3},
        }
        observation = {0: "a", 1: "a", 2: "b", 3: "c"}
        f_only = stable_family_partition(domain, {"f": operations["f"]}, observation)
        stable = stable_family_partition(domain, operations, observation)
        self.assertEqual(f_only[0], f_only[1])
        self.assertNotEqual(stable[0], stable[1])
        self.assertTrue(family_descends(domain, operations, stable))

    def test_stage_depth_equals_all_words_up_to_depth(self):
        domain = (0, 1, 2, 3)
        operations = {
            "f": {0: 1, 1: 2, 2: 2, 3: 3},
            "g": {0: 3, 1: 1, 2: 2, 3: 3},
        }
        observation = {0: "a", 1: "a", 2: "b", 3: "c"}
        stages = family_future_partition_sequence(domain, operations, observation)
        for depth, partition in enumerate(stages):
            for left in domain:
                for right in domain:
                    same_partition = partition[left] == partition[right]
                    same_words = word_observation_signature(
                        left, operations, observation, depth
                    ) == word_observation_signature(right, operations, observation, depth)
                    self.assertEqual(same_partition, same_words)

    def test_stable_partition_is_coarsest_common_compatible_refinement_exhaustive(self):
        domain = (0, 1, 2)
        all_maps = tuple(
            dict(zip(domain, values, strict=True))
            for values in itertools.product(domain, repeat=len(domain))
        )
        observations = tuple(
            dict(zip(domain, values, strict=True))
            for values in itertools.product(range(2), repeat=len(domain))
        )
        for f in all_maps:
            for g in all_maps:
                operations = {"f": f, "g": g}
                for observation in observations:
                    stable = stable_family_partition(domain, operations, observation)
                    self.assertTrue(refines(domain, stable, observation))
                    self.assertTrue(family_descends(domain, operations, stable))
                    for values in itertools.product(range(3), repeat=3):
                        candidate = dict(zip(domain, values, strict=True))
                        if refines(domain, candidate, observation) and family_descends(
                            domain, operations, candidate
                        ):
                            self.assertTrue(refines(domain, candidate, stable))

    def test_strict_rounds_have_finite_class_bound(self):
        domain = tuple(range(6))
        operations = {
            "forward": {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 5},
            "stay": {state: state for state in domain},
        }
        observation = {state: int(state == 5) for state in domain}
        stages = family_future_partition_sequence(domain, operations, observation)
        counts = [class_count(stage) for stage in stages]
        self.assertEqual(len(counts), len(set(counts)))
        self.assertLessEqual(len(stages) - 1, len(domain) - counts[0])

    def test_reference_module_has_no_float_or_true_division(self):
        tree = ast.parse(inspect.getsource(oq))
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
