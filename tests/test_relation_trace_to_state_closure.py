import itertools
import unittest

from enterprise_math.relation_branching_semiring import (
    boolean_semiring,
    natural_semiring,
)
from enterprise_math.relation_branching_vs_trace_cutoff import (
    semiring_terminal_trace_partition,
)
from enterprise_math.relation_semiring_stable_refinement import (
    coarsest_shared_semiring_refinement,
)
from enterprise_math.relation_support_stable_refinement import (
    normalize_partition,
    partition_from_observation,
    partition_refines,
)
from enterprise_math.relation_trace_to_state_closure import (
    continuation_debt_report,
    exact_count_trace_to_state_report,
    partition_between,
    stable_closure_absorbs_intermediate_partition,
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


def support_choice_timing_fixture():
    states = ("p", "q", "r", "s", "t", "z")
    relations = {
        "a": frozenset({("p", "r"), ("q", "s"), ("q", "t")}),
        "b": frozenset({("r", "z"), ("s", "z")}),
        "c": frozenset({("r", "z"), ("t", "z")}),
    }
    return states, relations, lambda _state: "visible"


def count_correlation_fixture():
    states = ("p", "q", "r1", "r2", "s", "t", "z1", "z2")
    relations = {
        "a": frozenset(
            {
                ("p", "r1"),
                ("p", "r2"),
                ("q", "s"),
                ("q", "t"),
            }
        ),
        "b": frozenset(
            {
                ("r1", "z1"),
                ("r2", "z1"),
                ("s", "z1"),
                ("s", "z2"),
            }
        ),
        "c": frozenset(
            {
                ("r1", "z1"),
                ("r2", "z1"),
                ("t", "z1"),
                ("t", "z2"),
            }
        ),
    }
    return states, relations, lambda _state: "visible"


class RelationTraceToStateClosureTests(unittest.TestCase):
    def test_boolean_choice_timing_trace_has_one_block_of_continuation_debt(self):
        states, relations, observation = support_choice_timing_fixture()
        initial = partition_from_observation(states, observation)
        trace = semiring_terminal_trace_partition(
            states,
            relations,
            observation,
            3,
            boolean_semiring(),
        )
        self.assertIn(frozenset({"p", "q"}), trace)
        report = continuation_debt_report(
            initial,
            trace,
            relations,
            boolean_semiring(),
        )
        self.assertTrue(report.has_continuation_debt)
        self.assertEqual(report.extra_state_blocks, 1)
        self.assertEqual(report.strict_repair_rounds, 1)
        self.assertIn(frozenset({"p"}), report.executable_state_partition)
        self.assertIn(frozenset({"q"}), report.executable_state_partition)

    def test_exact_count_correlation_trace_has_one_block_of_continuation_debt(self):
        states, relations, observation = count_correlation_fixture()
        report = exact_count_trace_to_state_report(
            states,
            relations,
            observation,
        )
        self.assertIn(frozenset({"p", "q"}), report.answer_partition)
        self.assertTrue(report.has_continuation_debt)
        self.assertEqual(report.extra_state_blocks, 1)
        self.assertEqual(report.strict_repair_rounds, 1)
        self.assertIn(frozenset({"p"}), report.executable_state_partition)
        self.assertIn(frozenset({"q"}), report.executable_state_partition)

    def test_no_debt_when_answer_is_already_the_stable_state(self):
        states = (0, 1, 2)
        relations = {
            "a": frozenset({(0, 1), (1, 2), (2, 2)}),
        }
        observation = lambda state: state
        initial = partition_from_observation(states, observation)
        report = continuation_debt_report(
            initial,
            initial,
            relations,
            natural_semiring(),
        )
        self.assertFalse(report.has_continuation_debt)
        self.assertEqual(report.strict_repair_rounds, 0)

    def test_interval_absorption_holds_for_every_intermediate_four_state_partition(self):
        states = (0, 1, 2, 3)
        relations = {
            "a": frozenset({(0, 2), (1, 3), (2, 0), (3, 3)}),
        }
        initial = partition_from_observation(states, lambda _state: 0)
        final = coarsest_shared_semiring_refinement(
            initial,
            relations,
            (natural_semiring(),),
        ).final_partition
        checked = 0
        for candidate in all_set_partitions(states):
            if not partition_between(final, candidate, initial):
                continue
            checked += 1
            self.assertTrue(
                stable_closure_absorbs_intermediate_partition(
                    initial,
                    candidate,
                    relations,
                    natural_semiring(),
                )
            )
        self.assertGreater(checked, 0)

    def test_answer_partition_must_lie_between_initial_and_stable_state(self):
        states = (0, 1, 2)
        relations = {
            "a": frozenset({(0, 2), (1, 2)}),
        }
        initial = partition_from_observation(states, lambda _state: 0)
        # A partition that splits a stable-equivalent pair is too fine to be an
        # answer lying between the initial observation and the coarsest state.
        bad_answer = normalize_partition(({0}, {1}, {2}))
        with self.assertRaises(ValueError):
            continuation_debt_report(
                initial,
                bad_answer,
                relations,
                natural_semiring(),
            )

    def test_partition_between_orientation(self):
        fine = normalize_partition(({0}, {1}, {2}, {3}))
        middle = normalize_partition(({0, 1}, {2}, {3}))
        coarse = normalize_partition(({0, 1, 2, 3},))
        self.assertTrue(partition_between(fine, middle, coarse))
        self.assertFalse(partition_between(middle, fine, coarse))


if __name__ == "__main__":
    unittest.main()
