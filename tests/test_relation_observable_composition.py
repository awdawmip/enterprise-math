import unittest

from enterprise_math.relation_observable_composition import (
    composed_signature_from_descended_transition,
    descended_relation_observation_transition,
    relation_observable_composition_report,
    relation_signature_factors_through_observation,
)
from enterprise_math.relation_observable_signature import (
    composed_relation_observation_signature_map,
)


class RelationObservableCompositionTests(unittest.TestCase):
    def test_hidden_raw_branch_can_reactivate_after_second_relation(self):
        states = frozenset(range(5))
        first = frozenset({(0, 1), (0, 2)})
        second = frozenset({(1, 3), (2, 4)})
        observation = lambda value: {
            0: "S",
            1: "M",
            2: "M",
            3: "A",
            4: "B",
        }[value]

        report = relation_observable_composition_report(
            states,
            first,
            second,
            observation,
        )
        self.assertTrue(report.first_observable_deterministic)
        self.assertTrue(report.second_observable_deterministic)
        self.assertFalse(report.second_signature_descends)
        self.assertFalse(report.composed_observable_deterministic)
        self.assertTrue(report.hidden_branch_reactivated)
        self.assertEqual(
            composed_relation_observation_signature_map(
                states,
                first,
                second,
                observation,
            )[0],
            frozenset({"A", "B"}),
        )

    def test_signature_congruence_prevents_hidden_branch_reactivation(self):
        states = frozenset(range(5))
        first = frozenset({(0, 1), (0, 2)})
        second = frozenset({(1, 3), (2, 3)})
        observation = lambda value: {
            0: "S",
            1: "M",
            2: "M",
            3: "A",
            4: "B",
        }[value]

        report = relation_observable_composition_report(
            states,
            first,
            second,
            observation,
        )
        self.assertTrue(report.first_observable_deterministic)
        self.assertTrue(report.second_observable_deterministic)
        self.assertTrue(report.second_signature_descends)
        self.assertTrue(report.sufficient_determinism_hypotheses_hold)
        self.assertTrue(report.composed_observable_deterministic)
        self.assertFalse(report.hidden_branch_reactivated)
        self.assertEqual(
            composed_signature_from_descended_transition(
                states,
                first,
                second,
                observation,
            )[0],
            frozenset({"A"}),
        )

    def test_descended_set_transition_reproduces_raw_relational_composition(self):
        states = frozenset(range(6))
        observation = lambda value: value // 2
        # Every pair in the same O-fiber has the same second-step observed target set.
        second = frozenset(
            {
                (0, 2),
                (1, 3),
                (2, 4),
                (3, 5),
                (4, 0),
                (5, 1),
            }
        )
        first = frozenset(
            {
                (0, 0),
                (0, 1),
                (1, 2),
                (1, 3),
                (2, 0),
                (2, 2),
            }
        )
        self.assertTrue(
            relation_signature_factors_through_observation(
                states,
                second,
                observation,
            )
        )
        coarse = descended_relation_observation_transition(
            states,
            second,
            observation,
        )
        self.assertEqual(coarse[0], frozenset({1}))
        self.assertEqual(coarse[1], frozenset({2}))
        self.assertEqual(coarse[2], frozenset({0}))
        self.assertEqual(
            composed_signature_from_descended_transition(
                states,
                first,
                second,
                observation,
            ),
            composed_relation_observation_signature_map(
                states,
                first,
                second,
                observation,
            ),
        )

    def test_terminal_only_composition_can_hide_intermediate_undefinedness(self):
        states = frozenset(range(4))
        first = frozenset({(0, 1), (0, 2)})
        second = frozenset({(1, 3)})
        observation = lambda value: {
            0: "S",
            1: "M",
            2: "M",
            3: "T",
        }[value]

        # Second step is deterministic at each raw source but NOT compatible
        # with the coarse intermediate observation: source 1 has target T while
        # source 2 is undefined.
        report = relation_observable_composition_report(
            states,
            first,
            second,
            observation,
        )
        self.assertTrue(report.first_observable_deterministic)
        self.assertTrue(report.second_observable_deterministic)
        self.assertFalse(report.second_signature_descends)

        # Ordinary terminal relation composition drops the dead 0->2 branch and
        # therefore happens to look deterministic at source 0.  A future language
        # observing intermediate definedness must not use this terminal-only result
        # as its full signature.
        self.assertTrue(report.composed_observable_deterministic)
        self.assertEqual(
            composed_relation_observation_signature_map(
                states,
                first,
                second,
                observation,
            )[0],
            frozenset({"T"}),
        )
        with self.assertRaises(ValueError):
            descended_relation_observation_transition(
                states,
                second,
                observation,
            )

    def test_second_relation_may_descend_as_set_valued_without_being_deterministic(self):
        states = frozenset(range(6))
        observation = lambda value: 0 if value in (0, 1) else 1 if value in (2, 3) else 2
        second = frozenset(
            {
                (0, 2),
                (0, 4),
                (1, 3),
                (1, 5),
            }
        )
        first = frozenset({(4, 0), (4, 1)})
        self.assertTrue(
            relation_signature_factors_through_observation(
                states,
                second,
                observation,
            )
        )
        coarse = descended_relation_observation_transition(
            states,
            second,
            observation,
        )
        self.assertEqual(coarse[0], frozenset({1, 2}))
        report = relation_observable_composition_report(
            states,
            first,
            second,
            observation,
        )
        self.assertTrue(report.first_observable_deterministic)
        self.assertFalse(report.second_observable_deterministic)
        self.assertTrue(report.second_signature_descends)
        self.assertFalse(report.composed_observable_deterministic)

    def test_exhaustive_two_state_sufficient_condition(self):
        states = frozenset({0, 1})
        pairs = ((0, 0), (0, 1), (1, 0), (1, 1))
        observations = (
            lambda value: value,
            lambda _: 0,
        )
        relations = tuple(
            frozenset(
                pair
                for index, pair in enumerate(pairs)
                if mask & (1 << index)
            )
            for mask in range(1 << len(pairs))
        )
        for first in relations:
            for second in relations:
                for observation in observations:
                    report = relation_observable_composition_report(
                        states,
                        first,
                        second,
                        observation,
                    )
                    if report.sufficient_determinism_hypotheses_hold:
                        self.assertTrue(report.composed_observable_deterministic)
                    if report.second_signature_descends:
                        self.assertEqual(
                            composed_signature_from_descended_transition(
                                states,
                                first,
                                second,
                                observation,
                            ),
                            composed_relation_observation_signature_map(
                                states,
                                first,
                                second,
                                observation,
                            ),
                        )

    def test_validation(self):
        with self.assertRaises(ValueError):
            relation_observable_composition_report(
                (),
                frozenset(),
                frozenset(),
                lambda value: value,
            )
        states = frozenset({0, 1})
        second = frozenset({(0, 1)})
        with self.assertRaises(ValueError):
            descended_relation_observation_transition(
                states,
                second,
                lambda _: 0,
            )


if __name__ == "__main__":
    unittest.main()
