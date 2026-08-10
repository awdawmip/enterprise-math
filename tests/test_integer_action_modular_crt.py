import itertools
import unittest

from enterprise_math.integer_action_modular_crt import (
    modular_action_crt_report,
    modular_smith_crt_report,
    prime_power_factorization,
)
from enterprise_math.integer_action_modular_closure import (
    modular_action_closure_report,
)


class IntegerActionModularCRTTests(unittest.TestCase):
    def test_prime_power_factorization(self):
        self.assertEqual(prime_power_factorization(1), ())
        self.assertEqual(
            tuple((factor.prime, factor.exponent, factor.modulus) for factor in prime_power_factorization(360)),
            ((2, 3, 8), (3, 2, 9), (5, 1, 5)),
        )
        self.assertEqual(
            tuple(factor.modulus for factor in prime_power_factorization(2 * 3 * 5 * 7)),
            (2, 3, 5, 7),
        )

    def test_static_smith_kernel_and_image_counts_factor_over_CRT(self):
        matrices = (
            ((2, 0), (0, 3)),
            ((1, 1), (1, -1)),
            ((4, 2),),
            ((1, 0, 0),),
        )
        for matrix in matrices:
            for modulus in (1, 6, 12, 18, 20, 45, 72):
                report = modular_smith_crt_report(matrix, modulus)
                self.assertEqual(
                    report.product_kernel_size,
                    report.composite.kernel_size,
                )
                self.assertEqual(
                    report.product_image_size,
                    report.composite.image_size,
                )

    def test_parallel_prime_refinement_can_beat_composite_Omega_budget(self):
        # Initial observation sees e1 only.  One nilpotent action exposes e2 at
        # horizon one.  Mod 2 and mod 3 each spend one hidden-residue factor in
        # parallel; mod 6 therefore closes in one step although Omega(6)=2.
        action = (
            (0, 1),
            (0, 0),
        )
        report = modular_action_crt_report(
            (action,),
            ((1, 0),),
            6,
        )
        self.assertEqual(report.composite.initial_kernel_size, 6)
        self.assertEqual(report.composite.arithmetic_refinement_budget, 2)
        self.assertEqual(report.component_refinement_budgets, (1, 1))
        self.assertEqual(report.component_stabilization_horizons, (1, 1))
        self.assertEqual(report.parallel_budget_bound, 1)
        self.assertEqual(report.crt_stabilization_horizon, 1)
        self.assertTrue(report.composite_horizon_matches_CRT_max)

    def test_composite_horizon_is_exact_max_of_slow_and_fast_prime_power_components(self):
        # The coefficient 2 hides e3 one extra horizon in the 2-adic component,
        # while it is invertible mod 3 and therefore immediately useful there.
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
        report = modular_action_crt_report(
            (action_a, action_b),
            ((1, 0, 0),),
            12,
        )
        factors = tuple(factor.modulus for factor in report.factors)
        horizons = dict(zip(factors, report.component_stabilization_horizons, strict=True))
        self.assertEqual(horizons[4], 2)
        self.assertEqual(horizons[3], 1)
        self.assertEqual(report.crt_stabilization_horizon, 2)
        self.assertEqual(report.composite.exact_stabilization_horizon, 2)
        self.assertTrue(report.composite.modularly_injective)

    def test_composite_action_closure_matches_CRT_on_small_binary_action_pairs(self):
        actions = tuple(
            (
                (entries[0], entries[1]),
                (entries[2], entries[3]),
            )
            for entries in itertools.product((0, 1), repeat=4)
        )
        observation = ((1, 0),)
        # Sample all individual binary actions and a deterministic subset of
        # pairs; this is enough to pressure-test horizon and count factorization
        # without turning the regression itself into a word-explosion benchmark.
        families = [(action,) for action in actions]
        families.extend(
            (actions[left], actions[right])
            for left in range(0, len(actions), 3)
            for right in range(0, len(actions), 5)
        )
        for family in families:
            for modulus in (6, 12, 18):
                report = modular_action_crt_report(
                    family,
                    observation,
                    modulus,
                )
                direct = modular_action_closure_report(
                    family,
                    observation,
                    modulus,
                )
                self.assertEqual(
                    report.crt_stabilization_horizon,
                    direct.exact_stabilization_horizon,
                    (family, modulus),
                )
                self.assertEqual(
                    report.composite.final_state_kernel_size,
                    direct.final_state_kernel_size,
                )
                self.assertEqual(
                    report.composite.final_observable_phase_count,
                    direct.final_observable_phase_count,
                )
                self.assertTrue(report.composite_horizon_matches_CRT_max)

    def test_modulus_one_has_empty_CRT_factor_family_and_trivial_horizon(self):
        report = modular_action_crt_report(
            (((1, 1), (0, 1)),),
            ((1, 0),),
            1,
        )
        self.assertEqual(report.factors, ())
        self.assertEqual(report.components, ())
        self.assertEqual(report.crt_stabilization_horizon, 0)
        self.assertEqual(report.parallel_budget_bound, 0)
        self.assertEqual(report.composite.final_state_kernel_size, 1)

    def test_validation(self):
        with self.assertRaises(ValueError):
            prime_power_factorization(0)
        with self.assertRaises(TypeError):
            prime_power_factorization(False)


if __name__ == "__main__":
    unittest.main()
