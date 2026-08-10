import unittest

from enterprise_math.precision_dependency_closure import (
    all_closed_task_sets,
    closure_exchange_holds,
    is_task_basis,
    minimal_task_bases,
    optimal_closed_context_schedule,
    task_dependency_closure,
)
from enterprise_math.precision_task_greedy import five_state_greedy_counterexample
from enterprise_math.precision_task_scheduling import optimal_order_by_symbol_depth


class PrecisionDependencyClosureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.states, self.tasks = five_state_greedy_counterexample()

    def test_closure_is_extensive_monotone_and_idempotent(self) -> None:
        names = tuple(sorted(self.tasks))
        subsets = [
            frozenset(name for index, name in enumerate(names) if mask & (1 << index))
            for mask in range(1 << len(names))
        ]
        closures = {
            subset: task_dependency_closure(self.states, self.tasks, subset)
            for subset in subsets
        }
        for subset, closure in closures.items():
            self.assertTrue(subset.issubset(closure))
            self.assertEqual(
                task_dependency_closure(self.states, self.tasks, closure),
                closure,
            )
        for left in subsets:
            for right in subsets:
                if left.issubset(right):
                    self.assertTrue(closures[left].issubset(closures[right]))

    def test_rich_task_closes_two_cheaper_tasks_for_free(self) -> None:
        self.assertEqual(
            task_dependency_closure(self.states, self.tasks, ("C",)),
            frozenset({"A", "B", "C"}),
        )
        self.assertEqual(
            task_dependency_closure(self.states, self.tasks, ("A",)),
            frozenset({"A"}),
        )
        self.assertEqual(
            task_dependency_closure(self.states, self.tasks, ("B",)),
            frozenset({"B"}),
        )

    def test_single_rich_task_is_unique_minimal_basis(self) -> None:
        self.assertTrue(is_task_basis(self.states, self.tasks, ("C",)))
        self.assertFalse(is_task_basis(self.states, self.tasks, ("A", "B")))
        self.assertEqual(minimal_task_bases(self.states, self.tasks), (frozenset({"C"}),))

    def test_dependency_closure_need_not_be_matroidal(self) -> None:
        # A is forced by C but C is not forced by A, violating closure exchange
        # with S=empty, x=A, y=C.
        self.assertFalse(
            closure_exchange_holds(
                self.states,
                self.tasks,
                (),
                "A",
                "C",
            )
        )

    def test_closed_context_dp_matches_full_subset_dp(self) -> None:
        closed = optimal_closed_context_schedule(self.states, self.tasks, base=2)
        full = optimal_order_by_symbol_depth(self.states, self.tasks, base=2)
        self.assertEqual(closed["minimum_symbol_depth"], full["minimum_symbol_depth"])
        self.assertEqual(closed["minimum_symbol_depth"], 2)
        self.assertEqual(closed["positive_cost_generators"], ("C",))
        self.assertLess(closed["all_closed_state_count"], closed["raw_subset_state_count"])

    def test_all_closed_sets_are_fixed_points(self) -> None:
        for closed in all_closed_task_sets(self.states, self.tasks):
            self.assertEqual(
                task_dependency_closure(self.states, self.tasks, closed),
                closed,
            )


if __name__ == "__main__":
    unittest.main()
