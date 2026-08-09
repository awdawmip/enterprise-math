import unittest
from itertools import product

from enterprise_math.contextual_closure import (
    FiniteOperation,
    candidate_refines_contextual_closure,
    contextual_closure_partition,
    first_stable_context_depth,
    floor_quotient_addition_separator,
    minimal_uniform_detail_size,
    partition_is_signature_congruence,
    partition_meet,
    quotient_operation_tables,
)
from enterprise_math.predictive_closure import (
    candidate_is_observation_respecting,
    observation_partition,
    partition_refines,
)


def all_partitions(states):
    states = tuple(states)
    if not states:
        yield frozenset()
        return

    def rec(index, blocks):
        if index == len(states):
            yield frozenset(frozenset(block) for block in blocks)
            return
        state = states[index]
        for slot in range(len(blocks)):
            new_blocks = [set(block) for block in blocks]
            new_blocks[slot].add(state)
            yield from rec(index + 1, new_blocks)
        yield from rec(index + 1, blocks + [{state}])

    yield from rec(1, [{states[0]}])


class ContextualClosureTests(unittest.TestCase):
    def test_already_congruent_parity_quotient_needs_no_refinement(self) -> None:
        states = tuple(range(6))
        add = FiniteOperation("add", 2, lambda args: (args[0] + args[1]) % 6)
        neg = FiniteOperation("neg", 1, lambda args: (-args[0]) % 6)
        observation = lambda x: x % 2
        depth, closure = first_stable_context_depth(states, (add, neg), observation)
        self.assertEqual(depth, 0)
        self.assertEqual(closure, observation_partition(states, observation))
        self.assertTrue(
            partition_is_signature_congruence(states, (add, neg), closure)
        )

        tables = quotient_operation_tables(states, (add, neg), closure)
        even = next(block for block in closure if 0 in block)
        odd = next(block for block in closure if 1 in block)
        self.assertEqual(tables["add"][(odd, odd)], even)
        self.assertEqual(tables["add"][(odd, even)], odd)
        self.assertEqual(tables["neg"][(odd,)], odd)

    def test_noncongruent_binary_quotient_refines_to_equality(self) -> None:
        states = tuple(range(4))
        add = FiniteOperation("add", 2, lambda args: (args[0] + args[1]) % 4)
        observation = lambda x: x // 2
        depth, closure = first_stable_context_depth(states, (add,), observation)
        self.assertGreater(depth, 0)
        self.assertEqual(len(closure), 4)
        self.assertEqual(minimal_uniform_detail_size(states, (add,), observation), 2)

    def test_ternary_operation_is_handled_without_binary_reduction(self) -> None:
        states = (0, 1, 2)
        operation = FiniteOperation(
            "ternary", 3, lambda args: (args[0] + args[1] + args[2]) % 3
        )
        observation = lambda x: 0 if x < 2 else 1
        closure = contextual_closure_partition(states, (operation,), observation)
        self.assertEqual(len(closure), 3)
        self.assertTrue(
            partition_is_signature_congruence(states, (operation,), closure)
        )

    def test_binary_context_bound_can_be_tight(self) -> None:
        states = (0, 1, 2, 3)
        table = (
            0, 0, 0, 0,
            0, 0, 0, 0,
            0, 0, 0, 0,
            0, 0, 3, 1,
        )
        operation = FiniteOperation(
            "mu", 2, lambda args: table[4 * args[0] + args[1]]
        )
        labels = (0, 1, 0, 0)
        observation = lambda x: labels[x]
        initial = observation_partition(states, observation)
        depth, closure = first_stable_context_depth(states, (operation,), observation)
        self.assertEqual(depth, len(states) - len(initial))
        self.assertEqual(len(closure), len(states))

    def test_exhaustive_two_state_binary_signatures_obey_bound_and_congruence(self) -> None:
        states = (0, 1)
        for values in product(states, repeat=4):
            operation = FiniteOperation(
                "mu", 2, lambda args, values=values: values[2 * args[0] + args[1]]
            )
            for labels in product((0, 1), repeat=2):
                observation = lambda x, labels=labels: labels[x]
                initial = observation_partition(states, observation)
                depth, closure = first_stable_context_depth(
                    states, (operation,), observation
                )
                self.assertLessEqual(depth, len(states) - len(initial))
                self.assertTrue(partition_refines(closure, initial))
                self.assertTrue(
                    partition_is_signature_congruence(states, (operation,), closure)
                )

    def test_contextual_closure_is_maximal_among_candidate_congruences(self) -> None:
        states = (0, 1, 2, 3)
        operation = FiniteOperation(
            "mu", 2, lambda args: (2 * args[0] + args[1]) % 4
        )
        observation = lambda x: x // 2
        closure = contextual_closure_partition(states, (operation,), observation)
        checked = 0
        for candidate in all_partitions(states):
            if not candidate_is_observation_respecting(candidate, observation):
                continue
            if not partition_is_signature_congruence(states, (operation,), candidate):
                continue
            checked += 1
            self.assertTrue(
                candidate_refines_contextual_closure(
                    states, (operation,), observation, candidate
                )
            )
            self.assertTrue(partition_refines(candidate, closure))
        self.assertGreater(checked, 0)

    def test_more_operations_can_only_force_more_detail(self) -> None:
        states = (0, 1, 2, 3)
        observation = lambda x: 0 if x < 3 else 1
        f = FiniteOperation("f", 1, lambda args: (0, 0, 1, 0)[args[0]])
        g = FiniteOperation("g", 1, lambda args: (0, 3, 0, 0)[args[0]])
        f_closure = contextual_closure_partition(states, (f,), observation)
        g_closure = contextual_closure_partition(states, (g,), observation)
        joint = contextual_closure_partition(states, (f, g), observation)
        self.assertTrue(partition_refines(joint, f_closure))
        self.assertTrue(partition_refines(joint, g_closure))

    def test_mixed_contexts_can_refine_beyond_intersection_of_separate_closures(self) -> None:
        states = (0, 1, 2, 3)
        observation = lambda x: 0 if x < 3 else 1
        f = FiniteOperation("f", 1, lambda args: (0, 0, 1, 0)[args[0]])
        g = FiniteOperation("g", 1, lambda args: (0, 3, 0, 0)[args[0]])
        f_closure = contextual_closure_partition(states, (f,), observation)
        g_closure = contextual_closure_partition(states, (g,), observation)
        separate_meet = partition_meet(states, (f_closure, g_closure))
        joint = contextual_closure_partition(states, (f, g), observation)

        self.assertNotEqual(joint, separate_meet)
        separate_blocks = {state: block for block in separate_meet for state in block}
        joint_blocks = {state: block for block in joint for state in block}
        self.assertEqual(separate_blocks[0], separate_blocks[2])
        self.assertNotEqual(joint_blocks[0], joint_blocks[2])
        self.assertNotEqual(
            observation(g.apply((f.apply((0,)),))),
            observation(g.apply((f.apply((2,)),))),
        )

    def test_contextual_closure_preserves_meet_of_observations(self) -> None:
        states = (0, 1, 2, 3)
        operation = FiniteOperation("step", 1, lambda args: (1, 2, 3, 3)[args[0]])
        first = lambda x: x // 2
        second = lambda x: x % 2
        combined = lambda x: (first(x), second(x))
        left = contextual_closure_partition(states, (operation,), combined)
        right = partition_meet(
            states,
            (
                contextual_closure_partition(states, (operation,), first),
                contextual_closure_partition(states, (operation,), second),
            ),
        )
        self.assertEqual(left, right)

    def test_floor_quotient_addition_forces_residue_distinction(self) -> None:
        for radix in range(2, 20):
            for quotient in range(5):
                fiber = tuple(range(quotient * radix, (quotient + 1) * radix))
                for index, x in enumerate(fiber):
                    for y in fiber[index + 1 :]:
                        shift = floor_quotient_addition_separator(radix, x, y)
                        self.assertEqual((x + shift) // radix, quotient)
                        self.assertEqual((y + shift) // radix, quotient + 1)

    def test_empty_operation_signature_keeps_static_observation(self) -> None:
        states = (0, 1, 2, 3)
        observation = lambda x: x % 2
        depth, closure = first_stable_context_depth(states, (), observation)
        self.assertEqual(depth, 0)
        self.assertEqual(closure, observation_partition(states, observation))


if __name__ == "__main__":
    unittest.main()
