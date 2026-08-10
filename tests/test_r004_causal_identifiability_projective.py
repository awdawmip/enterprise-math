import unittest
from fractions import Fraction

from enterprise_math.r004_causal_identifiability_completion import (
    compile_rational_master_measure,
    direct_policy_history_law,
)
from enterprise_math.r004_causal_identifiability_projective import (
    rational_master_measure_projective_holds,
    support_master_projective_holds,
    truncate_master_measure,
)


class R004ProjectiveCompletionTests(unittest.TestCase):
    def test_support_master_families_are_projective_with_disabledness(self):
        states = (0, 1)
        relations = {
            "flip": frozenset({(0, 1), (1, 0)}),
            "stay-if-zero": frozenset({(0, 0)}),
        }
        for shallow in range(3):
            for deep in range(shallow, 3):
                self.assertTrue(
                    support_master_projective_holds(
                        states, relations, 0, shallow, deep
                    )
                )

    def test_two_action_rational_master_measures_are_exactly_projective(self):
        states = (0, 1)
        kernels = {
            "a": {
                0: {0: Fraction(1, 3), 1: Fraction(2, 3)},
                1: {0: Fraction(1, 4), 1: Fraction(3, 4)},
            },
            "b": {
                0: {0: Fraction(2, 5), 1: Fraction(3, 5)},
                1: {0: Fraction(3, 7), 1: Fraction(4, 7)},
            },
        }
        for shallow in range(3):
            for deep in range(shallow, 3):
                self.assertTrue(
                    rational_master_measure_projective_holds(
                        states, kernels, 0, shallow, deep
                    )
                )

    def test_truncation_preserves_probability_mass_exactly(self):
        states = (0, 1)
        kernels = {
            "a": {
                0: {0: Fraction(1, 2), 1: Fraction(1, 2)},
                1: {0: Fraction(1, 2), 1: Fraction(1, 2)},
            }
        }
        deep = compile_rational_master_measure(states, kernels, 0, 5)
        shallow = truncate_master_measure(deep, 2)
        self.assertEqual(sum(deep.values(), Fraction(0)), Fraction(1))
        self.assertEqual(sum(shallow.values(), Fraction(0)), Fraction(1))
        self.assertEqual(
            shallow,
            compile_rational_master_measure(states, kernels, 0, 2),
        )

    def test_fair_bit_history_requires_exponentially_many_finite_atoms(self):
        states = (0, 1)
        kernels = {
            "a": {
                0: {0: Fraction(1, 2), 1: Fraction(1, 2)},
                1: {0: Fraction(1, 2), 1: Fraction(1, 2)},
            }
        }
        policy = lambda _history: "a"
        for horizon in range(1, 7):
            law = direct_policy_history_law(
                states, kernels, 0, horizon, policy
            )
            # The initial state is fixed and the next H states are independent
            # fair bits, so there are 2^H positive histories.  A mixture of B
            # deterministic infinite masters can expose at most B histories
            # under this one-action policy; hence B >= 2^H is necessary.
            self.assertEqual(len(law), 2**horizon)
            self.assertEqual(set(law.values()), {Fraction(1, 2**horizon)})

            finite_master_measure = compile_rational_master_measure(
                states, kernels, 0, horizon
            )
            self.assertEqual(len(finite_master_measure), 2**horizon)


if __name__ == "__main__":
    unittest.main()
