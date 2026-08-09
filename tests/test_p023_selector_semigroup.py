import ast
import inspect
import itertools
import unittest

import enterprise_math.p023_selector_semigroup as semigroup
from enterprise_math.operation_quotient import family_descends
from enterprise_math.p023_selector_semigroup import (
    joint_safe_partition,
    selector_word_fixed_iff_common_compatible,
    selector_word_once,
    selector_word_sequence,
    selector_word_stable_equivalence_holds,
    stable_selector_word,
)


class SafeSelectorSemigroupTests(unittest.TestCase):
    def test_five_state_one_pass_order_dependence_but_common_stable_limit(self):
        domain = (0, 1, 2, 3, 4)
        f = {0: 0, 1: 4, 2: 3, 3: 2, 4: 3}
        g = {0: 2, 1: 0, 2: 1, 3: 2, 4: 2}
        observation = {0: 0, 1: 0, 2: 0, 3: 0, 4: 1}
        fg_word = ({"f": f}, {"g": g})
        gf_word = ({"g": g}, {"f": f})

        fg_once = selector_word_once(domain, fg_word, observation)
        gf_once = selector_word_once(domain, gf_word, observation)
        self.assertNotEqual(fg_once, gf_once)
        self.assertFalse(family_descends(domain, {"f": f, "g": g}, fg_once))
        self.assertFalse(family_descends(domain, {"f": f, "g": g}, gf_once))

        fg_stable = stable_selector_word(domain, fg_word, observation)
        gf_stable = stable_selector_word(domain, gf_word, observation)
        joint = joint_safe_partition(domain, fg_word, observation)
        self.assertEqual(fg_stable, joint)
        self.assertEqual(gf_stable, joint)
        self.assertEqual(len(set(joint.values())), 5)

    def test_fixed_point_of_selector_word_is_exact_common_compatibility(self):
        domain = (0, 1, 2, 3)
        f = {0: 1, 1: 2, 2: 2, 3: 3}
        g = {0: 3, 1: 1, 2: 2, 3: 3}
        word = ({"f": f}, {"g": g})
        for labels in itertools.product(range(3), repeat=len(domain)):
            partition = dict(zip(domain, labels, strict=True))
            self.assertTrue(
                selector_word_fixed_iff_common_compatible(domain, word, partition)
            )

    def test_repeated_word_equals_joint_selector_exhaustive_three_states(self):
        domain = (0, 1, 2)
        maps = [
            dict(zip(domain, values, strict=True))
            for values in itertools.product(domain, repeat=3)
        ]
        observations = [
            dict(zip(domain, values, strict=True))
            for values in itertools.product(range(2), repeat=3)
        ]
        for f in maps:
            for g in maps:
                word = ({"f": f}, {"g": g})
                reverse = ({"g": g}, {"f": f})
                for observation in observations:
                    self.assertTrue(
                        selector_word_stable_equivalence_holds(
                            domain, word, observation
                        )
                    )
                    self.assertTrue(
                        selector_word_stable_equivalence_holds(
                            domain, reverse, observation
                        )
                    )

    def test_selector_word_terminates_with_class_bound(self):
        domain = tuple(range(7))
        f = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 6}
        g = {0: 0, 1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5}
        observation = {state: int(state == 6) for state in domain}
        stages = selector_word_sequence(domain, ({"f": f}, {"g": g}), observation)
        counts = [len(set(stage.values())) for stage in stages]
        self.assertEqual(counts, sorted(set(counts)))
        self.assertLessEqual(len(stages) - 1, len(domain) - counts[0])

    def test_reference_module_has_no_float_or_true_division(self):
        tree = ast.parse(inspect.getsource(semigroup))
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
