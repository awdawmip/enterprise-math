import ast
import inspect
import itertools
import unittest

import enterprise_math.p023_safe_precision_interior as safe
from enterprise_math.operation_quotient import family_descends, refines, stable_family_partition
from enterprise_math.p023_safe_precision_interior import (
    idempotent_safe_repair,
    partition_relation,
    relation_compatible,
    safe_partition_selector,
    safe_relation_selector,
    safe_relation_step,
    sequential_single_operation_pass,
)


class SafePrecisionInteriorTests(unittest.TestCase):
    def test_relation_selector_matches_existing_partition_selector(self):
        domain = (0, 1, 2, 3)
        operations = {
            "f": {0: 1, 1: 2, 2: 2, 3: 3},
            "g": {0: 3, 1: 1, 2: 2, 3: 3},
        }
        observation = {0: "a", 1: "a", 2: "b", 3: "c"}
        relation = safe_relation_selector(domain, operations, partition_relation(domain, observation))
        selected = safe_partition_selector(domain, operations, observation)
        self.assertEqual(relation, partition_relation(domain, selected))
        self.assertTrue(relation_compatible(domain, operations, relation))

    def test_relation_step_is_reductive_and_fixed_exactly_at_compatibility(self):
        domain = (0, 1, 2, 3)
        operations = {"f": {0: 1, 1: 2, 2: 2, 3: 3}}
        observation = {0: 0, 1: 0, 2: 1, 3: 1}
        relation = partition_relation(domain, observation)
        step = safe_relation_step(domain, operations, relation)
        self.assertTrue(step.issubset(relation))
        stable = safe_relation_selector(domain, operations, relation)
        self.assertEqual(safe_relation_step(domain, operations, stable), stable)
        self.assertTrue(relation_compatible(domain, operations, stable))

    def test_selector_is_monotone_in_initial_precision(self):
        domain = (0, 1, 2, 3)
        operations = {"f": {0: 1, 1: 2, 2: 3, 3: 3}}
        coarse = {0: 0, 1: 0, 2: 0, 3: 1}
        fine = {0: 0, 1: 1, 2: 2, 3: 3}
        coarse_safe = safe_relation_selector(domain, operations, partition_relation(domain, coarse))
        fine_safe = safe_relation_selector(domain, operations, partition_relation(domain, fine))
        self.assertTrue(fine_safe.issubset(coarse_safe))

    def test_more_operations_can_only_require_finer_safe_precision(self):
        domain = (0, 1, 2, 3)
        f = {0: 1, 1: 2, 2: 2, 3: 3}
        g = {0: 3, 1: 1, 2: 2, 3: 3}
        observation = {0: 0, 1: 0, 2: 1, 3: 1}
        f_safe = safe_relation_selector(domain, {"f": f}, partition_relation(domain, observation))
        fg_safe = safe_relation_selector(domain, {"f": f, "g": g}, partition_relation(domain, observation))
        self.assertTrue(fg_safe.issubset(f_safe))

    def test_idempotent_operation_closes_after_one_repair(self):
        domain = (0, 1, 2, 3, 4)
        operation = {0: 0, 1: 0, 2: 2, 3: 2, 4: 4}
        observation = {0: 0, 1: 0, 2: 0, 3: 0, 4: 1}
        repaired = idempotent_safe_repair(domain, operation, observation)
        stable = stable_family_partition(domain, {"T": operation}, observation)
        self.assertEqual(
            partition_relation(domain, repaired),
            partition_relation(domain, stable),
        )
        self.assertTrue(family_descends(domain, {"T": operation}, repaired))

    def test_idempotent_one_step_theorem_exhaustive_on_three_states(self):
        domain = (0, 1, 2)
        all_maps = [
            dict(zip(domain, values, strict=True))
            for values in itertools.product(domain, repeat=3)
        ]
        idempotents = [
            operation
            for operation in all_maps
            if all(operation[operation[x]] == operation[x] for x in domain)
        ]
        observations = [
            dict(zip(domain, values, strict=True))
            for values in itertools.product(range(2), repeat=3)
        ]
        for operation in idempotents:
            for observation in observations:
                repaired = idempotent_safe_repair(domain, operation, observation)
                self.assertTrue(refines(domain, repaired, observation))
                self.assertTrue(family_descends(domain, {"T": operation}, repaired))

    def test_one_sequential_pass_of_single_selectors_can_fail_both_orders(self):
        domain = (0, 1, 2, 3, 4)
        f = {0: 0, 1: 4, 2: 3, 3: 2, 4: 3}
        g = {0: 2, 1: 0, 2: 1, 3: 2, 4: 2}
        observation = {0: 0, 1: 0, 2: 0, 3: 0, 4: 1}
        joint = stable_family_partition(domain, {"f": f, "g": g}, observation)
        fg = sequential_single_operation_pass(domain, (f, g), observation)
        gf = sequential_single_operation_pass(domain, (g, f), observation)
        self.assertEqual(len(set(joint.values())), 5)
        self.assertFalse(family_descends(domain, {"f": f, "g": g}, fg))
        self.assertFalse(family_descends(domain, {"f": f, "g": g}, gf))
        self.assertNotEqual(partition_relation(domain, fg), partition_relation(domain, joint))
        self.assertNotEqual(partition_relation(domain, gf), partition_relation(domain, joint))

    def test_reference_module_has_no_float_or_true_division(self):
        tree = ast.parse(inspect.getsource(safe))
        floats = [
            node for node in ast.walk(tree)
            if isinstance(node, ast.Constant) and isinstance(node.value, float)
        ]
        divisions = [
            node for node in ast.walk(tree)
            if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div)
        ]
        self.assertEqual(floats, [])
        self.assertEqual(divisions, [])


if __name__ == "__main__":
    unittest.main()
