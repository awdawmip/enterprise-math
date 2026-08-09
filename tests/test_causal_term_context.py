import unittest
from itertools import product

from enterprise_math.causal_operation_language import (
    class_count,
    partition_refines,
)
from enterprise_math.causal_term_context import (
    elementary_context_generators,
    induced_operation_tables,
    minimum_term_context_partition,
    operations_respect_partition,
    term_operation_coupling_defect,
)


def _set_partitions(items):
    if not items:
        yield []
        return
    first, *rest = items
    for partition in _set_partitions(rest):
        yield [[first]] + [block[:] for block in partition]
        for index in range(len(partition)):
            copy = [block[:] for block in partition]
            copy[index].append(first)
            yield copy


def _partition_map(states, blocks):
    result = {}
    for class_id, block in enumerate(blocks):
        for state in block:
            result[state] = class_id
    return result


def _refines_observation(partition, observation, states):
    return all(
        partition[a] != partition[b] or observation[a] == observation[b]
        for a in states
        for b in states
    )


def _direct_operation_congruence(states, partition, arity, table):
    raw_inputs = tuple(product(states, repeat=arity))
    for left in raw_inputs:
        for right in raw_inputs:
            if all(partition[a] == partition[b] for a, b in zip(left, right)):
                if partition[table[left]] != partition[table[right]]:
                    return False
    return True


class CausalTermContextTests(unittest.TestCase):
    def test_ternary_operation_can_force_hidden_state_distinction(self):
        states = (0, 1, 2, 3)
        observation = {0: 0, 1: 0, 2: 0, 3: 1}
        table = {args: 0 for args in product(states, repeat=3)}
        table[(2, 0, 0)] = 3
        operations = {"omega": (3, table)}

        partition = minimum_term_context_partition(states, observation, operations)
        self.assertNotEqual(partition[0], partition[2])
        self.assertTrue(operations_respect_partition(states, partition, operations))
        self.assertTrue(_direct_operation_congruence(states, partition, 3, table))

    def test_elementary_contexts_are_enough_for_binary_congruence(self):
        states = (0, 1, 2, 3)
        observation = {state: state % 2 for state in states}
        add_mod_four = {
            args: (args[0] + args[1]) % 4
            for args in product(states, repeat=2)
        }
        operations = {"add": (2, add_mod_four)}
        partition = minimum_term_context_partition(states, observation, operations)
        self.assertEqual(class_count(partition), 2)
        self.assertTrue(_direct_operation_congruence(states, partition, 2, add_mod_four))
        quotient = induced_operation_tables(states, partition, operations)
        self.assertEqual(quotient["add"][0], 2)
        self.assertEqual(len(quotient["add"][1]), 4)

    def test_minimum_term_partition_is_coarsest_congruence_refining_observation(self):
        states = (0, 1, 2, 3)
        observation = {0: 0, 1: 0, 2: 0, 3: 1}
        table = {args: 0 for args in product(states, repeat=2)}
        table[(2, 0)] = 3
        operations = {"star": (2, table)}
        minimum = minimum_term_context_partition(states, observation, operations)

        found_safe = 0
        for blocks in _set_partitions(list(states)):
            candidate = _partition_map(states, blocks)
            if not _refines_observation(candidate, observation, states):
                continue
            if not _direct_operation_congruence(states, candidate, 2, table):
                continue
            found_safe += 1
            self.assertTrue(partition_refines(candidate, minimum))
        self.assertGreater(found_safe, 0)

    def test_unary_operations_are_exact_special_case_of_term_contexts(self):
        states = (0, 1, 2, 3)
        observation = {0: 0, 1: 0, 2: 0, 3: 1}
        g = {0: 0, 1: 0, 2: 1, 3: 0}
        h = {0: 0, 1: 3, 2: 0, 3: 0}
        left_ops = {"g": (1, {(state,): g[state] for state in states})}
        right_ops = {"h": (1, {(state,): h[state] for state in states})}
        extra, lost = term_operation_coupling_defect(
            states,
            observation,
            left_ops,
            right_ops,
            maximum_order=4,
        )
        self.assertEqual(extra, 1)
        self.assertEqual(lost, (0, 1, 0, 0))

    def test_nullary_constants_need_no_one_hole_context(self):
        states = (0, 1)
        observation = {0: 0, 1: 0}
        operations = {"zero": (0, {(): 0})}
        generators = elementary_context_generators(states, operations)
        self.assertEqual(generators, {})
        partition = minimum_term_context_partition(states, observation, operations)
        self.assertEqual(class_count(partition), 1)


if __name__ == "__main__":
    unittest.main()
