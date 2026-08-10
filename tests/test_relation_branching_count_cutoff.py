import itertools
import unittest

from enterprise_math.relation_branching_count_cutoff import (
    count_branching_cutoff_report,
    exact_count_and_modular_sequences_agree_above_outdegree,
    minimal_exact_modulus_for_count_branching,
    modulus_reflects_all_block_counts,
    relation_max_outdegree,
    universal_exact_count_branching_modulus,
    worst_case_modulus_collision_fixture,
)


def all_two_state_relations():
    states = (0, 1)
    pairs = tuple(itertools.product(states, repeat=2))
    return tuple(
        frozenset(pair for pair, keep in zip(pairs, mask, strict=True) if keep)
        for mask in itertools.product((0, 1), repeat=4)
    )


class RelationBranchingCountCutoffTests(unittest.TestCase):
    def test_universal_cutoff_formula(self):
        self.assertEqual(universal_exact_count_branching_modulus(0), 2)
        self.assertEqual(universal_exact_count_branching_modulus(1), 2)
        self.assertEqual(universal_exact_count_branching_modulus(2), 3)
        self.assertEqual(universal_exact_count_branching_modulus(7), 8)
        for delta in range(10):
            cutoff = universal_exact_count_branching_modulus(delta)
            self.assertTrue(cutoff > delta)
            self.assertTrue(modulus_reflects_all_block_counts(delta, cutoff))

    def test_all_two_state_relation_pairs_match_exact_N_at_theorem_cutoff(self):
        states = (0, 1)
        relations = all_two_state_relations()
        observations = (
            lambda _state: 0,
            lambda state: state,
        )
        for first in relations:
            for second in relations:
                family = {"a": first, "b": second}
                delta = relation_max_outdegree(states, family)
                modulus = universal_exact_count_branching_modulus(delta)
                for observation in observations:
                    self.assertTrue(
                        exact_count_and_modular_sequences_agree_above_outdegree(
                            states,
                            family,
                            observation,
                            modulus,
                        )
                    )
                    report = count_branching_cutoff_report(
                        states,
                        family,
                        observation,
                        modulus,
                    )
                    self.assertTrue(report.theorem_guaranteed)
                    self.assertTrue(report.complete_sequences_equal)

    def test_sharp_zero_vs_M_successor_collision_for_every_small_modulus(self):
        for modulus in range(2, 8):
            states, relations, observation = worst_case_modulus_collision_fixture(modulus)
            self.assertEqual(relation_max_outdegree(states, relations), modulus)
            report = count_branching_cutoff_report(
                states,
                relations,
                observation,
                modulus,
            )
            self.assertFalse(report.theorem_guaranteed)
            self.assertNotEqual(report.exact_steps, report.modular_steps)
            self.assertNotEqual(report.exact_steps[-1], report.modular_steps[-1])

            safe = count_branching_cutoff_report(
                states,
                relations,
                observation,
                modulus + 1,
            )
            self.assertTrue(safe.theorem_guaranteed)
            self.assertTrue(safe.complete_sequences_equal)

    def test_worst_case_sharpness_inside_a_larger_outdegree_budget(self):
        # Any M<=Delta can fail somewhere in the class of worlds with outdegree
        # at most Delta.  The isolated source w raises the world's actual Delta
        # without changing the x/y count collision at M.
        for delta in range(3, 8):
            for modulus in range(2, delta + 1):
                states, relations, observation = worst_case_modulus_collision_fixture(
                    modulus,
                    max_outdegree=delta,
                )
                self.assertEqual(relation_max_outdegree(states, relations), delta)
                report = count_branching_cutoff_report(
                    states,
                    relations,
                    observation,
                    modulus,
                )
                self.assertFalse(report.complete_sequences_equal)

    def test_specific_relation_can_need_less_than_the_universal_cutoff(self):
        states = (0, 1, 2)
        relations = {
            "a": frozenset({(0, 1), (0, 2)}),
        }
        # Delta=2, so the universal theorem says mod3.  Identity observation is
        # already discrete, so every modulus gives the same state partition.
        observation = lambda state: state
        self.assertEqual(relation_max_outdegree(states, relations), 2)
        self.assertEqual(universal_exact_count_branching_modulus(2), 3)
        self.assertEqual(
            minimal_exact_modulus_for_count_branching(
                states,
                relations,
                observation,
            ),
            2,
        )

    def test_minimal_modulus_search_is_finite_and_never_exceeds_Delta_plus_one(self):
        states = (0, 1)
        relations = all_two_state_relations()
        for relation in relations:
            family = {"a": relation}
            delta = relation_max_outdegree(states, family)
            cutoff = universal_exact_count_branching_modulus(delta)
            minimum = minimal_exact_modulus_for_count_branching(
                states,
                family,
                lambda _state: 0,
            )
            self.assertGreaterEqual(minimum, 2)
            self.assertLessEqual(minimum, cutoff)

    def test_validation(self):
        with self.assertRaises(ValueError):
            universal_exact_count_branching_modulus(-1)
        with self.assertRaises(TypeError):
            universal_exact_count_branching_modulus(False)
        with self.assertRaises(ValueError):
            modulus_reflects_all_block_counts(2, 1)
        with self.assertRaises(ValueError):
            worst_case_modulus_collision_fixture(3, max_outdegree=2)
        with self.assertRaises(ValueError):
            exact_count_and_modular_sequences_agree_above_outdegree(
                (0, 1),
                {"a": frozenset({(0, 0), (0, 1)})},
                lambda _state: 0,
                2,
            )


if __name__ == "__main__":
    unittest.main()
