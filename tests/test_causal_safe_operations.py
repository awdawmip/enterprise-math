import unittest

from enterprise_math.causal_safe_operations import (
    compose_operations,
    identity_operation,
    induced_operation,
    operation_is_safe,
    partition_refines,
    safe_composition_closure_check,
    safe_declared_operations,
)


class CausalSafeOperationsTests(unittest.TestCase):
    def test_identity_is_always_safe(self):
        states = (0, 1, 2, 3)
        quotient = {0: "a", 1: "a", 2: "b", 3: "b"}
        identity = identity_operation(states)
        self.assertTrue(operation_is_safe(quotient, identity))
        self.assertEqual(induced_operation(quotient, identity), {"a": "a", "b": "b"})

    def test_safe_operations_are_closed_under_composition(self):
        quotient = {0: "a", 1: "a", 2: "b", 3: "b"}
        first = {0: 2, 1: 3, 2: 0, 3: 1}
        second = {0: 1, 1: 0, 2: 3, 3: 2}
        self.assertTrue(operation_is_safe(quotient, first))
        self.assertTrue(operation_is_safe(quotient, second))
        self.assertTrue(safe_composition_closure_check(quotient, first, second))
        composed = compose_operations(first, second)
        self.assertTrue(operation_is_safe(quotient, composed))

    def test_unsafe_operation_is_exactly_hidden_detail_feedback(self):
        quotient = {0: "a", 1: "a", 2: "b", 3: "b"}
        unsafe = {0: 0, 1: 2, 2: 2, 3: 3}
        self.assertFalse(operation_is_safe(quotient, unsafe))
        with self.assertRaises(ValueError):
            induced_operation(quotient, unsafe)

    def test_declared_future_language_can_be_partially_preserved(self):
        quotient = {0: "a", 1: "a", 2: "b", 3: "b"}
        operations = {
            "swap-blocks": {0: 2, 1: 3, 2: 0, 3: 1},
            "within-block": {0: 1, 1: 0, 2: 3, 3: 2},
            "hidden-feedback": {0: 0, 1: 2, 2: 2, 3: 3},
        }
        self.assertEqual(
            safe_declared_operations(quotient, operations),
            ("swap-blocks", "within-block"),
        )

    def test_safe_operation_sets_are_not_monotone_under_partition_refinement(self):
        states = (0, 1, 2, 3)
        coarse = {0: "A", 1: "A", 2: "B", 3: "B"}
        finer = {0: "0", 1: "1", 2: "B", 3: "B"}
        self.assertTrue(partition_refines(finer, coarse))

        # Safe for coarse: pair 2,3 both land somewhere in coarse A, but they land
        # in distinct finer singleton classes, so it is not safe for finer.
        coarse_only = {0: 0, 1: 1, 2: 0, 3: 1}
        self.assertTrue(operation_is_safe(coarse, coarse_only))
        self.assertFalse(operation_is_safe(finer, coarse_only))

        # Safe for finer: the only nontrivial finer pair 2,3 stays together, while
        # raw 0,1 (merged only by coarse) may be sent to different coarse blocks.
        finer_only = {0: 0, 1: 2, 2: 3, 3: 3}
        self.assertTrue(operation_is_safe(finer, finer_only))
        self.assertFalse(operation_is_safe(coarse, finer_only))


if __name__ == "__main__":
    unittest.main()
