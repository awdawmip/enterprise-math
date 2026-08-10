import itertools
import unittest

from enterprise_math.integer_action_language_observability import (
    action_language_observation_rows,
)
from enterprise_math.integer_action_modular_closure import (
    modular_action_closure_report,
    modular_preimage_lattice_basis,
)
from enterprise_math.integer_future_modular_precision import (
    modular_smith_precision_report,
)


class IntegerActionModularClosureTests(unittest.TestCase):
    def test_modular_HNF_steps_match_literal_word_smith_kernel_on_all_small_binary_action_pairs(self):
        actions = tuple(
            (
                (entries[0], entries[1]),
                (entries[2], entries[3]),
            )
            for entries in itertools.product((0, 1), repeat=4)
        )
        observation = ((1, 0),)

        for left in actions:
            for right in actions:
                family = (left, right)
                for modulus in (2, 3):
                    report = modular_action_closure_report(
                        family,
                        observation,
                        modulus,
                    )
                    for step in report.steps:
                        literal_rows = action_language_observation_rows(
                            family,
                            observation,
                            step.horizon,
                        )
                        smith = modular_smith_precision_report(
                            literal_rows,
                            modulus,
                        )
                        self.assertEqual(
                            step.state_kernel_size,
                            smith.kernel_size,
                            (family, modulus, step.horizon),
                        )
                        self.assertEqual(
                            step.observable_phase_count,
                            smith.image_size,
                        )
                        self.assertEqual(
                            step.preimage_basis,
                            modular_preimage_lattice_basis(
                                literal_rows,
                                modulus,
                            ),
                        )

    def test_noncommutative_index_two_witness_has_mod_two_chain_four_two_one(self):
        action_a = (
            (0, 1, 0),
            (0, 0, 0),
            (0, 0, 0),
        )
        action_b = (
            (0, 0, 2),
            (0, 0, 1),
            (0, 0, 0),
        )
        report = modular_action_closure_report(
            (action_a, action_b),
            ((1, 0, 0),),
            2,
        )
        by_horizon = {step.horizon: step for step in report.steps}
        self.assertEqual(
            tuple(by_horizon[h].state_kernel_size for h in (0, 1, 2)),
            (4, 2, 1),
        )
        self.assertEqual(
            tuple(by_horizon[h].observable_phase_count for h in (0, 1, 2)),
            (2, 4, 8),
        )
        self.assertEqual(report.initial_kernel_size, 4)
        self.assertEqual(report.arithmetic_refinement_budget, 2)
        self.assertEqual(report.exact_stabilization_horizon, 2)
        self.assertTrue(report.modularly_injective)

    def test_same_integer_witness_closes_one_horizon_earlier_mod_three(self):
        action_a = (
            (0, 1, 0),
            (0, 0, 0),
            (0, 0, 0),
        )
        action_b = (
            (0, 0, 2),
            (0, 0, 1),
            (0, 0, 0),
        )
        report = modular_action_closure_report(
            (action_a, action_b),
            ((1, 0, 0),),
            3,
        )
        self.assertEqual(report.initial_kernel_size, 9)
        self.assertEqual(report.steps[1].state_kernel_size, 1)
        self.assertEqual(report.exact_stabilization_horizon, 1)
        self.assertTrue(report.modularly_injective)

    def test_prime_modulus_chain_attains_full_hidden_dimension_bound(self):
        action = (
            (0, 1, 0, 0),
            (0, 0, 1, 0),
            (0, 0, 0, 1),
            (0, 0, 0, 0),
        )
        for prime in (2, 3, 5):
            report = modular_action_closure_report(
                (action,),
                ((1, 0, 0, 0),),
                prime,
            )
            self.assertEqual(report.initial_kernel_size, prime ** 3)
            self.assertEqual(report.arithmetic_refinement_budget, 3)
            self.assertEqual(report.exact_stabilization_horizon, 3)
            self.assertEqual(
                tuple(
                    report.steps[h].state_kernel_size
                    for h in range(4)
                ),
                (prime ** 3, prime ** 2, prime, 1),
            )

    def test_zero_observation_is_stable_but_bound_is_only_an_upper_budget(self):
        actions = (
            ((1, 1), (0, 1)),
            ((0, 1), (1, 0)),
        )
        report = modular_action_closure_report(
            actions,
            ((0, 0),),
            6,
        )
        self.assertEqual(report.initial_kernel_size, 36)
        self.assertEqual(report.final_state_kernel_size, 36)
        self.assertEqual(report.final_observable_phase_count, 1)
        self.assertEqual(report.exact_stabilization_horizon, 0)
        self.assertGreater(report.arithmetic_refinement_budget, 0)

    def test_modulus_one_is_trivially_closed(self):
        report = modular_action_closure_report(
            (((2, 1), (1, 1)),),
            ((1, 0),),
            1,
        )
        self.assertEqual(report.initial_kernel_size, 1)
        self.assertEqual(report.final_observable_phase_count, 1)
        self.assertEqual(report.arithmetic_refinement_budget, 0)
        self.assertEqual(report.exact_stabilization_horizon, 0)

    def test_validation(self):
        with self.assertRaises(ValueError):
            modular_action_closure_report((), ((1,),), 2)
        with self.assertRaises(ValueError):
            modular_action_closure_report((((1,),),), ((1,),), 0)
        with self.assertRaises(ValueError):
            modular_action_closure_report((((1, 0),),), ((1,),), 2)


if __name__ == "__main__":
    unittest.main()
