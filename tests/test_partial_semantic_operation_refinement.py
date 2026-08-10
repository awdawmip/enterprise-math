import unittest

from enterprise_math.partial_semantic_operation_refinement import (
    coarsest_partial_operation_safe_refinement,
    observable_undefined_totalization_matches,
    partial_operation_refinement_step,
    partial_operation_safe_on_partition,
    partial_partition_is_safe_for_all,
    total_specialization_matches,
    verify_partial_coarsest_against_candidate,
)
from enterprise_math.semantic_precision_preorder import (
    normalize_partition,
    partition_refines,
)


def all_set_partitions(values):
    values = tuple(values)

    def rec(index, blocks):
        if index == len(values):
            yield normalize_partition(tuple(frozenset(block) for block in blocks))
            return
        value = values[index]
        for block_index in range(len(blocks)):
            next_blocks = [set(block) for block in blocks]
            next_blocks[block_index].add(value)
            yield from rec(index + 1, next_blocks)
        yield from rec(index + 1, [*blocks, {value}])

    seen = set()
    for partition in rec(0, []):
        if partition not in seen:
            seen.add(partition)
            yield partition


class PartialSemanticOperationRefinementTests(unittest.TestCase):
    def test_mixed_definedness_splits_even_when_defined_target_is_in_same_block(self):
        initial = ({0, 1}, {2})
        operation = {0: 2}
        self.assertFalse(partial_operation_safe_on_partition(initial, operation))
        first = partial_operation_refinement_step(initial, {"u": operation})
        self.assertEqual(
            set(first),
            {frozenset({0}), frozenset({1}), frozenset({2})},
        )

    def test_domain_split_can_trigger_later_target_split(self):
        initial = ({0, 1}, {2, 3})
        operations = {
            "u": {
                0: 2,
                1: 3,
                2: 0,
                # 3 is undefined.
            }
        }
        first = partial_operation_refinement_step(initial, operations)
        self.assertEqual(
            set(first),
            {frozenset({0, 1}), frozenset({2}), frozenset({3})},
        )
        second = partial_operation_refinement_step(first, operations)
        self.assertEqual(
            set(second),
            {frozenset({0}), frozenset({1}), frozenset({2}), frozenset({3})},
        )

        report = coarsest_partial_operation_safe_refinement(initial, operations)
        self.assertEqual(report.strict_refinement_steps, 2)
        self.assertEqual(report.final_partition, second)
        self.assertTrue(partial_partition_is_safe_for_all(report.final_partition, operations))

    def test_exhaustive_four_state_coarsest_property_for_domain_target_cascade(self):
        states = (0, 1, 2, 3)
        initial = normalize_partition(({0, 1}, {2, 3}))
        operations = {
            "u": {
                0: 2,
                1: 3,
                2: 0,
            }
        }
        report = coarsest_partial_operation_safe_refinement(initial, operations)
        safe_candidates = 0
        for candidate in all_set_partitions(states):
            if not partition_refines(candidate, initial):
                continue
            if not partial_partition_is_safe_for_all(candidate, operations):
                continue
            safe_candidates += 1
            self.assertTrue(
                verify_partial_coarsest_against_candidate(
                    report,
                    candidate,
                    operations,
                )
            )
        self.assertGreater(safe_candidates, 0)

    def test_total_specialization_agrees_with_total_operation_compiler(self):
        partition = ({0, 1}, {2, 3})
        operations = {
            "a": {0: 2, 1: 3, 2: 0, 3: 3},
            "b": {0: 0, 1: 0, 2: 2, 3: 2},
        }
        self.assertTrue(total_specialization_matches(partition, operations))

    def test_observable_undefined_totalization_matches_partial_compiler(self):
        cases = (
            (
                ({0, 1}, {2, 3}),
                {"u": {0: 2, 1: 3, 2: 0}},
            ),
            (
                ({0, 1, 2}, {3}),
                {
                    "u": {0: 1, 1: 2},
                    "v": {0: 3, 2: 3, 3: 0},
                },
            ),
            (
                ({0, 1, 2},),
                {"u": {}},
            ),
        )
        for partition, operations in cases:
            self.assertTrue(
                observable_undefined_totalization_matches(
                    partition,
                    operations,
                )
            )

    def test_all_undefined_operation_is_safe_without_refinement(self):
        initial = ({0, 1}, {2, 3})
        operations = {"never": {}}
        report = coarsest_partial_operation_safe_refinement(initial, operations)
        self.assertEqual(report.final_partition, normalize_partition(initial))
        self.assertEqual(report.strict_refinement_steps, 0)

    def test_multiple_partial_operations_use_joint_definedness_target_signature(self):
        initial = ({0, 1, 2}, {3, 4})
        operations = {
            "u": {0: 3, 1: 4, 3: 0},
            "v": {0: 1, 2: 1, 4: 2},
        }
        report = coarsest_partial_operation_safe_refinement(initial, operations)
        self.assertTrue(partial_partition_is_safe_for_all(report.final_partition, operations))
        self.assertTrue(partition_refines(report.final_partition, initial))
        self.assertLessEqual(
            report.strict_refinement_steps,
            5 - len(normalize_partition(initial)),
        )

    def test_definedness_must_match_before_target_equivalence_matters(self):
        partition = ({0, 1}, {2, 3})
        # Only 0 is defined, even though its target lies in a coarse block that
        # could otherwise absorb a target difference.
        self.assertFalse(
            partial_operation_safe_on_partition(
                partition,
                {0: 2},
            )
        )

    def test_validation(self):
        with self.assertRaises(ValueError):
            coarsest_partial_operation_safe_refinement(
                ({0, 1},),
                {"bad": {2: 0}},
            )
        with self.assertRaises(ValueError):
            coarsest_partial_operation_safe_refinement(
                ({0, 1},),
                {"bad": {0: 2}},
            )
        with self.assertRaises(ValueError):
            total_specialization_matches(
                ({0, 1},),
                {"partial": {0: 1}},
            )


if __name__ == "__main__":
    unittest.main()
