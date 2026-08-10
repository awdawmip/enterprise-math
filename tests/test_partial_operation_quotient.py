import itertools
import unittest

from enterprise_math.operation_quotient import (
    family_future_partition_sequence,
    stable_family_partition,
    word_observation_signature,
)
from enterprise_math.partial_operation_quotient import (
    apply_partial_word,
    partial_family_descends,
    partial_family_future_partition_sequence,
    partial_family_horizon_partition,
    partial_family_refinement_step,
    partial_operation_descends,
    partial_word_observation_signature,
    partition_refines,
    partitions_equivalent,
    stable_partial_family_is_coarsest_compatible,
    stable_partial_family_partition,
    totalize_partial_family,
)


def all_partial_operations(states):
    values = (None,) + tuple(states)
    result = []
    for targets in itertools.product(values, repeat=len(states)):
        operation = {
            state: target
            for state, target in zip(states, targets)
            if target is not None
        }
        result.append(operation)
    return tuple(result)


def all_total_operations(states):
    return tuple(
        {state: target for state, target in zip(states, targets)}
        for targets in itertools.product(states, repeat=len(states))
    )


def restricted_growth_partitions(states):
    states = tuple(states)
    if not states:
        return ()
    labels = [0] * len(states)
    result = []

    def rec(index, maximum):
        if index == len(states):
            result.append({state: labels[i] for i, state in enumerate(states)})
            return
        for label in range(maximum + 2):
            labels[index] = label
            rec(index + 1, max(maximum, label))

    labels[0] = 0
    if len(states) == 1:
        return ({states[0]: 0},)

    def rec_canonical(index, maximum):
        if index == len(states):
            result.append({state: labels[i] for i, state in enumerate(states)})
            return
        for label in range(maximum + 2):
            # Restricted-growth strings require a_i <= 1+max(previous).
            labels[index] = label
            rec_canonical(index + 1, max(maximum, label))

    result.clear()
    rec_canonical(1, 0)
    return tuple(result)


def iterate_partial_steps(states, operations, initial, depth):
    current = dict(initial)
    for _ in range(depth):
        current = partial_family_refinement_step(states, operations, current)
    return current


class PartialOperationQuotientTests(unittest.TestCase):
    def test_domain_membership_is_part_of_quotient_behavior(self):
        states = (0, 1)
        operation = {0: 0}
        coarse = {0: "same", 1: "same"}

        self.assertFalse(partial_operation_descends(states, operation, coarse))
        stable = stable_partial_family_partition(
            states, {"a": operation}, coarse
        )
        self.assertNotEqual(stable[0], stable[1])
        self.assertTrue(
            partial_operation_descends(states, operation, stable)
        )

    def test_disabled_action_is_not_silently_identity(self):
        states = (0, 1)
        operations = {"a": {0: 1}}
        observation = {0: "O", 1: "O"}

        sig0 = partial_word_observation_signature(
            0, operations, observation, 1
        )
        sig1 = partial_word_observation_signature(
            1, operations, observation, 1
        )
        self.assertNotEqual(sig0, sig1)
        self.assertEqual(sig0, ((True, "O"), (True, "O")))
        self.assertEqual(sig1, ((True, "O"), (False, None)))

    def test_apply_partial_word_returns_first_disabled_prefix(self):
        operations = {
            "a": {0: 1, 1: 2},
            "b": {2: 0},
        }
        defined = apply_partial_word(0, operations, ("a", "a", "b"))
        self.assertTrue(defined.defined)
        self.assertEqual(defined.state, 0)
        self.assertEqual(defined.defined_prefix_length, 3)

        blocked = apply_partial_word(0, operations, ("a", "b", "a"))
        self.assertFalse(blocked.defined)
        self.assertIsNone(blocked.state)
        self.assertEqual(blocked.defined_prefix_length, 1)

    def test_refinement_depth_equals_legality_sensitive_word_signature_exhaustive(self):
        states = (0, 1)
        partials = all_partial_operations(states)
        observations = (
            {0: 0, 1: 0},
            {0: 0, 1: 1},
        )
        checked = 0
        for left in partials:
            for right in partials:
                operations = {"a": left, "b": right}
                for observation in observations:
                    for depth in range(4):
                        iterative = iterate_partial_steps(
                            states, operations, observation, depth
                        )
                        words = partial_family_horizon_partition(
                            states, operations, observation, depth
                        )
                        self.assertTrue(
                            partitions_equivalent(states, iterative, words)
                        )
                        checked += 1
        self.assertGreater(checked, 600)

    def test_stable_partition_is_compatible_and_finite(self):
        states = (0, 1, 2)
        initial = {0: 0, 1: 0, 2: 0}
        checked = 0
        for operation in all_partial_operations(states):
            operations = {"a": operation}
            stages = partial_family_future_partition_sequence(
                states, operations, initial
            )
            stable = stages[-1]
            self.assertLessEqual(len(stages), len(states))
            self.assertTrue(partial_family_descends(states, operations, stable))
            self.assertTrue(partition_refines(states, stable, initial))
            for earlier, later in zip(stages, stages[1:]):
                self.assertTrue(partition_refines(states, later, earlier))
            checked += 1
        self.assertEqual(checked, 64)

    def test_stable_partition_is_coarsest_compatible_refinement_bruteforce(self):
        states = (0, 1, 2)
        all_partitions = restricted_growth_partitions(states)
        self.assertEqual(len(all_partitions), 5)
        initial_partitions = (
            {0: 0, 1: 0, 2: 0},
            {0: 0, 1: 0, 2: 1},
        )
        checked = 0
        for operation in all_partial_operations(states):
            operations = {"a": operation}
            for initial in initial_partitions:
                stable = stable_partial_family_partition(
                    states, operations, initial
                )
                for candidate in all_partitions:
                    implication = stable_partial_family_is_coarsest_compatible(
                        states,
                        operations,
                        initial,
                        candidate,
                    )
                    self.assertTrue(implication)
                    if (
                        partition_refines(states, candidate, initial)
                        and partial_family_descends(
                            states, operations, candidate
                        )
                    ):
                        self.assertTrue(
                            partition_refines(states, candidate, stable)
                        )
                    checked += 1
        self.assertGreater(checked, 500)

    def test_total_operation_family_reduces_to_existing_p023_quotient(self):
        states = (0, 1)
        observations = (
            {0: 0, 1: 0},
            {0: 0, 1: 1},
        )
        totals = all_total_operations(states)
        checked = 0
        for left in totals:
            for right in totals:
                operations = {"a": left, "b": right}
                for observation in observations:
                    partial_stages = partial_family_future_partition_sequence(
                        states, operations, observation
                    )
                    total_stages = family_future_partition_sequence(
                        states, operations, observation
                    )
                    self.assertEqual(len(partial_stages), len(total_stages))
                    for partial_stage, total_stage in zip(
                        partial_stages, total_stages
                    ):
                        self.assertTrue(
                            partitions_equivalent(
                                states, partial_stage, total_stage
                            )
                        )
                    self.assertTrue(
                        partitions_equivalent(
                            states,
                            stable_partial_family_partition(
                                states, operations, observation
                            ),
                            stable_family_partition(
                                states, operations, observation
                            ),
                        )
                    )
                    checked += 1
        self.assertGreater(checked, 30)

    def test_observable_totalization_matches_every_partial_horizon_exhaustive(self):
        states = (0, 1)
        observation = {0: "same", 1: "same"}
        partials = all_partial_operations(states)
        checked = 0
        for left in partials:
            for right in partials:
                operations = {"a": left, "b": right}
                augmented, total_ops, total_observation = totalize_partial_family(
                    states,
                    operations,
                    observation,
                    undefined_state="BOTTOM",
                    undefined_observation="UNDEFINED",
                )
                self.assertEqual(augmented[-1], "BOTTOM")
                for depth in range(4):
                    partial_horizon = partial_family_horizon_partition(
                        states, operations, observation, depth
                    )
                    total_signatures = {
                        state: word_observation_signature(
                            state, total_ops, total_observation, depth
                        )
                        for state in states
                    }
                    self.assertTrue(
                        partitions_equivalent(
                            states, partial_horizon, total_signatures
                        )
                    )
                    checked += 1
        self.assertGreater(checked, 300)

    def test_absorbing_undefined_totalization_matches_partial_quotient(self):
        states = (0, 1)
        observation = {0: "same", 1: "same"}
        partials = all_partial_operations(states)
        checked = 0
        for left in partials:
            for right in partials:
                operations = {"a": left, "b": right}
                partial_stable = stable_partial_family_partition(
                    states, operations, observation
                )
                augmented, total_ops, total_observation = totalize_partial_family(
                    states,
                    operations,
                    observation,
                    undefined_state="BOTTOM",
                    undefined_observation="UNDEFINED",
                )
                total_stable = stable_family_partition(
                    augmented, total_ops, total_observation
                )
                restricted = {state: total_stable[state] for state in states}
                self.assertTrue(
                    partitions_equivalent(
                        states, partial_stable, restricted
                    )
                )
                checked += 1
        self.assertEqual(checked, 81)

    def test_totalization_requires_distinguished_undefined_observation(self):
        # If an implementation totalizes a disabled action to a sink but then
        # gives that sink the same observation as ordinary states, one-step
        # behavior can be spuriously merged.  The genuine partial quotient does
        # not permit that collapse.
        states = (0, 1)
        operations = {"a": {0: 0}}
        observation = {0: "same", 1: "same"}
        partial = stable_partial_family_partition(
            states, operations, observation
        )
        self.assertNotEqual(partial[0], partial[1])

        sink = 2
        total_ops = {"a": {0: 0, 1: sink, sink: sink}}
        bad_observation = {0: "same", 1: "same", sink: "same"}
        bad_total = stable_family_partition(
            (0, 1, sink), total_ops, bad_observation
        )
        self.assertEqual(bad_total[0], bad_total[1])

    def test_prefix_legality_is_recovered_because_prefixes_are_words(self):
        states = (0, 1, 2)
        operations = {
            "a": {0: 1, 1: 2},
            "b": {1: 1, 2: 2},
        }
        observation = {0: "O", 1: "O", 2: "O"}
        sig0 = partial_word_observation_signature(
            0, operations, observation, 2
        )
        sig1 = partial_word_observation_signature(
            1, operations, observation, 2
        )
        self.assertNotEqual(sig0, sig1)
        horizon = partial_family_horizon_partition(
            states, operations, observation, 2
        )
        self.assertNotEqual(horizon[0], horizon[1])

    def test_operation_domain_can_be_empty(self):
        states = (0, 1)
        operations = {"never": {}}
        observation = {0: 0, 1: 0}
        stable = stable_partial_family_partition(
            states, operations, observation
        )
        self.assertEqual(stable[0], stable[1])
        self.assertTrue(partial_family_descends(states, operations, stable))

    def test_validation(self):
        with self.assertRaises(ValueError):
            stable_partial_family_partition((), {"a": {}}, {})
        with self.assertRaises(ValueError):
            stable_partial_family_partition(
                (0, 1), {}, {0: 0, 1: 0}
            )
        with self.assertRaises(ValueError):
            stable_partial_family_partition(
                (0, 1), {"a": {2: 0}}, {0: 0, 1: 0}
            )
        with self.assertRaises(ValueError):
            stable_partial_family_partition(
                (0, 1), {"a": {0: 2}}, {0: 0, 1: 0}
            )
        with self.assertRaises(ValueError):
            stable_partial_family_partition(
                (0, 1), {"a": {0: 0}}, {0: 0}
            )
        with self.assertRaises(ValueError):
            partial_word_observation_signature(
                0, {"a": {0: 0}}, {0: 0}, -1
            )
        with self.assertRaises(ValueError):
            apply_partial_word(0, {"a": {0: 0}}, ("b",))
        with self.assertRaises(ValueError):
            totalize_partial_family(
                (0, 1),
                {"a": {0: 1}},
                {0: "same", 1: "same"},
                undefined_state=1,
                undefined_observation="UNDEFINED",
            )
        with self.assertRaises(ValueError):
            totalize_partial_family(
                (0, 1),
                {"a": {0: 1}},
                {0: "same", 1: "same"},
                undefined_state="BOTTOM",
                undefined_observation="same",
            )


if __name__ == "__main__":
    unittest.main()
