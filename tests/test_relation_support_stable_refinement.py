import unittest

from enterprise_math.relation_boolean_future_semimodule import (
    relation_boolean_future_semimodule_report,
)
from enterprise_math.relation_support_stable_refinement import (
    coarsest_relation_support_stable_refinement,
    normalize_partition,
    partition_from_observation,
    partition_refines,
    relation_family_support_stable_on_partition,
    relation_support_refinement_step,
    relation_support_stable_refines_terminal_trace_partition,
    support_stability_is_strictly_finer_than_terminal_trace,
    verify_relation_support_coarsest_against_candidate,
)


def all_set_partitions(values):
    values = tuple(values)

    def rec(index, blocks):
        if index == len(values):
            yield normalize_partition(tuple(frozenset(block) for block in blocks))
            return
        value = values[index]
        for block_index in range(len(blocks)):
            nxt = [set(block) for block in blocks]
            nxt[block_index].add(value)
            yield from rec(index + 1, nxt)
        yield from rec(index + 1, [*blocks, {value}])

    seen = set()
    for partition in rec(0, []):
        if partition not in seen:
            seen.add(partition)
            yield partition


def branch_correlation_fixture():
    states = ("x", "y", "u1", "u2", "v1", "v2", 0, 1)
    relations = {
        "a": frozenset(
            {
                ("x", "u1"),
                ("x", "u2"),
                ("y", "v1"),
                ("y", "v2"),
            }
        ),
        "b": frozenset(
            {
                ("u1", 0),
                ("u2", 1),
                ("v1", 0),
                ("v2", 1),
            }
        ),
        "c": frozenset(
            {
                ("u1", 0),
                ("u2", 1),
                ("v1", 1),
                ("v2", 0),
            }
        ),
    }
    observation = {
        "x": "source",
        "y": "source",
        "u1": "middle",
        "u2": "middle",
        "v1": "middle",
        "v2": "middle",
        0: "zero",
        1: "one",
    }
    return states, relations, lambda state: observation[state]


class RelationSupportStableRefinementTests(unittest.TestCase):
    def test_empty_successor_support_preserves_partial_definedness(self):
        initial = ({0, 1}, {2})
        relations = {"u": frozenset({(0, 2)})}
        first = relation_support_refinement_step(initial, relations)
        self.assertEqual(
            set(first),
            {frozenset({0}), frozenset({1}), frozenset({2})},
        )

    def test_partial_domain_target_cascade_is_recovered_as_zero_or_singleton_support(self):
        initial = ({0, 1}, {2, 3})
        relations = {
            "u": frozenset(
                {
                    (0, 2),
                    (1, 3),
                    (2, 0),
                    # 3 has empty successor support.
                }
            )
        }
        first = relation_support_refinement_step(initial, relations)
        self.assertEqual(
            set(first),
            {frozenset({0, 1}), frozenset({2}), frozenset({3})},
        )
        second = relation_support_refinement_step(first, relations)
        self.assertEqual(
            set(second),
            {frozenset({0}), frozenset({1}), frozenset({2}), frozenset({3})},
        )
        report = coarsest_relation_support_stable_refinement(initial, relations)
        self.assertEqual(report.strict_refinement_steps, 2)
        self.assertEqual(report.final_partition, second)

    def test_bounded_exhaustive_coarsest_property(self):
        states = (0, 1, 2, 3)
        initial = normalize_partition(({0, 1}, {2, 3}))
        relations = {
            "u": frozenset({(0, 2), (1, 3), (2, 0)})
        }
        report = coarsest_relation_support_stable_refinement(initial, relations)
        stable_candidates = 0
        for candidate in all_set_partitions(states):
            if not partition_refines(candidate, initial):
                continue
            if not relation_family_support_stable_on_partition(candidate, relations):
                continue
            stable_candidates += 1
            self.assertTrue(
                verify_relation_support_coarsest_against_candidate(
                    report,
                    candidate,
                    relations,
                )
            )
        self.assertGreater(stable_candidates, 0)

    def test_multivalued_branch_correlation_splits_middle_states_then_sources(self):
        states, relations, observation = branch_correlation_fixture()
        initial = partition_from_observation(states, observation)
        report = coarsest_relation_support_stable_refinement(initial, relations)

        by_step = report.steps
        self.assertEqual(report.strict_refinement_steps, 2)

        # First split exposes the four distinct joint (b,c) behaviours of the
        # middle states, while x/y still have the same a-target observation block.
        self.assertIn(frozenset({"x", "y"}), by_step[1])
        for middle in ("u1", "u2", "v1", "v2"):
            self.assertIn(frozenset({middle}), by_step[1])

        # Second split sees that relation a reaches different sets of those
        # behavioural quotient classes from x and y.
        self.assertIn(frozenset({"x"}), report.final_partition)
        self.assertIn(frozenset({"y"}), report.final_partition)

    def test_terminal_observed_support_trace_keeps_x_and_y_equivalent_forever(self):
        states, relations, observation = branch_correlation_fixture()
        trace = relation_boolean_future_semimodule_report(
            states,
            relations,
            observation,
        )
        final_partition = set(trace.steps[-1].state_partition)
        self.assertIn(frozenset({"x", "y"}), final_partition)
        self.assertTrue(
            relation_support_stable_refines_terminal_trace_partition(
                states,
                relations,
                observation,
            )
        )
        self.assertTrue(
            support_stability_is_strictly_finer_than_terminal_trace(
                states,
                relations,
                observation,
            )
        )

    def test_terminal_trace_and_relation_stability_can_coincide_for_deterministic_family(self):
        states = (0, 1, 2)
        relations = {
            "u": frozenset({(0, 1), (1, 2), (2, 2)})
        }
        observation = lambda state: int(state == 2)
        initial = partition_from_observation(states, observation)
        stable = coarsest_relation_support_stable_refinement(initial, relations)
        trace = relation_boolean_future_semimodule_report(states, relations, observation)
        trace_partition = normalize_partition(tuple(trace.steps[-1].state_partition))
        self.assertEqual(stable.final_partition, trace_partition)

    def test_validation(self):
        with self.assertRaises(ValueError):
            coarsest_relation_support_stable_refinement(
                ({0, 1},),
                {},
            )
        with self.assertRaises(ValueError):
            coarsest_relation_support_stable_refinement(
                ({0, 1},),
                {"bad": frozenset({(0, 2)})},
            )
        with self.assertRaises(TypeError):
            coarsest_relation_support_stable_refinement(
                ({0, 1},),
                {"bad": {(0, 1)}},
            )


if __name__ == "__main__":
    unittest.main()
