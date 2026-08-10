import itertools
import unittest

from enterprise_math.relation_boolean_future_semimodule import (
    boolean_join_closure,
    boolean_join_irreducibles,
    boolean_row_action,
    boolean_semimodule_closure_step,
    relation_boolean_future_semimodule_report,
    relation_boolean_matrix,
)
from enterprise_math.relation_future_powerset import (
    relation_family_future_partition,
)


def all_relations(states):
    pairs = tuple(itertools.product(states, repeat=2))
    return tuple(
        frozenset(pair for bit, pair in zip(mask, pairs, strict=True) if bit)
        for mask in itertools.product((0, 1), repeat=len(pairs))
    )


class RelationBooleanFutureSemimoduleTests(unittest.TestCase):
    def test_boolean_matrix_matches_direct_relation_preimage_on_rows(self):
        states = (0, 1, 2)
        relation = frozenset({(0, 1), (0, 2), (2, 1)})
        matrix = relation_boolean_matrix(states, relation)
        # Target predicate {1}: sources with an R-successor in {1} are {0,2}.
        self.assertEqual(
            boolean_row_action((0, 1, 0), matrix),
            (1, 0, 1),
        )
        # Target predicate {1,2}: only source 0 or 2 has a successor there.
        self.assertEqual(
            boolean_row_action((0, 1, 1), matrix),
            (1, 0, 1),
        )

    def test_join_irreducibles_are_the_unique_needed_generators_on_examples(self):
        closure = boolean_join_closure(((1, 1, 0), (0, 1, 1)))
        self.assertEqual(
            closure,
            frozenset({
                (0, 0, 0),
                (1, 1, 0),
                (0, 1, 1),
                (1, 1, 1),
            }),
        )
        self.assertEqual(
            boolean_join_irreducibles(closure),
            ((0, 1, 1), (1, 1, 0)),
        )

        chain = frozenset({
            (0, 0, 0),
            (1, 0, 0),
            (1, 1, 0),
            (1, 1, 1),
        })
        self.assertEqual(
            boolean_join_irreducibles(chain),
            ((1, 0, 0), (1, 1, 0), (1, 1, 1)),
        )

    def test_semimodule_partition_matches_literal_word_partition_for_all_two_state_relation_pairs(self):
        states = (0, 1)
        relations = all_relations(states)
        observations = (
            lambda _: 0,
            lambda state: state,
        )

        for left in relations:
            for right in relations:
                family = {"L": left, "R": right}
                for observation in observations:
                    report = relation_boolean_future_semimodule_report(
                        states,
                        family,
                        observation,
                    )
                    steps = {step.horizon: step for step in report.steps}
                    for horizon in range(4):
                        literal = relation_family_future_partition(
                            states,
                            family,
                            observation,
                            horizon,
                        )
                        semimodule = (
                            steps[horizon].state_partition
                            if horizon in steps
                            else report.steps[-1].state_partition
                        )
                        self.assertEqual(
                            semimodule,
                            literal,
                            (left, right, horizon),
                        )

    def test_state_partition_can_finish_before_boolean_support_module_closes(self):
        states = (0, 1, 2)
        relations = {
            "R": frozenset({(2, 0), (1, 1)}),
        }
        observation = lambda state: 0 if state in (0, 1) else 1
        report = relation_boolean_future_semimodule_report(
            states,
            relations,
            observation,
        )
        self.assertEqual(report.exact_stabilization_horizon, 2)

        horizon_one = report.steps[1]
        horizon_two = report.steps[2]
        discrete = frozenset({
            frozenset({0}),
            frozenset({1}),
            frozenset({2}),
        })
        self.assertEqual(horizon_one.state_partition, discrete)
        self.assertEqual(horizon_two.state_partition, discrete)
        self.assertNotEqual(horizon_one.semimodule, horizon_two.semimodule)
        self.assertEqual(len(horizon_one.semimodule), 5)
        self.assertEqual(len(horizon_two.semimodule), 6)
        # The new horizon-two predicate is {state 1}; it adds Boolean support
        # reconstruction power without adding another raw-state distinction.
        self.assertNotIn((0, 1, 0), horizon_one.semimodule)
        self.assertIn((0, 1, 0), horizon_two.semimodule)
        self.assertEqual(report.steps[2].semimodule, report.steps[3].semimodule)

    def test_one_equal_semimodule_step_is_a_permanent_stop_certificate(self):
        states = (0, 1, 2)
        relations = {
            "A": frozenset({(0, 1), (1, 2), (2, 2)}),
            "I": frozenset({(0, 0), (1, 1), (2, 2)}),
        }
        report = relation_boolean_future_semimodule_report(
            states,
            relations,
            lambda state: state,
        )
        # Identity observation already distinguishes every raw state, so the
        # Boolean row semimodule is the full Boolean algebra at horizon zero.
        self.assertEqual(report.exact_stabilization_horizon, 0)
        self.assertEqual(len(report.final_semimodule), 8)
        self.assertEqual(report.final_semimodule, report.steps[1].semimodule)

    def test_constant_observation_can_generate_future_definedness_precision(self):
        states = (0, 1, 2)
        relations = {
            "D": frozenset({(2, 1), (1, 0)}),
        }
        report = relation_boolean_future_semimodule_report(
            states,
            relations,
            lambda _: 0,
        )
        # Present observation is constant, but repeated relation definedness
        # separates the countdown depths.
        self.assertEqual(
            report.steps[0].state_partition,
            frozenset({frozenset({0, 1, 2})}),
        )
        self.assertEqual(
            report.final_join_irreducibles,
            ((0, 0, 1), (0, 1, 1), (1, 1, 1)),
        )
        self.assertEqual(
            report.steps[-1].state_partition,
            frozenset({frozenset({0}), frozenset({1}), frozenset({2})}),
        )

    def test_semimodule_step_uses_join_basis_without_losing_full_closure(self):
        semimodule = boolean_join_closure(((1, 1, 0), (0, 1, 1)))
        action = (
            (1, 0, 0),
            (0, 0, 1),
            (0, 1, 0),
        )
        next_semimodule = boolean_semimodule_closure_step(
            semimodule,
            (action,),
        )
        # Repeating after closure cannot shrink it.
        self.assertTrue(semimodule.issubset(next_semimodule))

    def test_validation(self):
        with self.assertRaises(ValueError):
            relation_boolean_matrix((), frozenset())
        with self.assertRaises(ValueError):
            boolean_join_closure(())
        with self.assertRaises(ValueError):
            boolean_join_irreducibles(((1, 0),))
        with self.assertRaises(ValueError):
            boolean_row_action((1, 0), ((1,),))


if __name__ == "__main__":
    unittest.main()
