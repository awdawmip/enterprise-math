from __future__ import annotations

import math
import unittest
from fractions import Fraction

from enterprise_math.brc_count_centered_carry import (
    GammaAffine,
    carry_bit,
    carry_count,
    centered_geometry_ratio,
    count_centered_coefficient,
    count_centered_holonomy,
    direct_gamma_centered_prime_error_form,
    divisor_summatory,
    factor_positive_integer,
    hard_prime_skeleton_thickness,
    mobius,
    mobius_divisor_deconvolution_form,
    old_population_valuations,
    prime_power_branch_weight,
    selected_old_valuations,
    valuation_product,
)


class BRCCountCenteredCarryTests(unittest.TestCase):
    def test_carry_count_and_zero_sum_centering(self) -> None:
        for n in range(1, 129):
            direct = sum(carry_bit(n, m) for m in range(1, n + 1))
            self.assertEqual(carry_count(n), direct)
            self.assertEqual(
                carry_count(n),
                divisor_summatory(2 * n) - 2 * divisor_summatory(n) - n,
            )
            self.assertEqual(
                sum((count_centered_coefficient(n, m) for m in range(1, n + 1)), Fraction(0)),
                0,
            )

    def test_prime_power_branch_weights_and_population_product(self) -> None:
        self.assertEqual(prime_power_branch_weight(1), 1)
        self.assertEqual(prime_power_branch_weight(8), 2)
        self.assertEqual(prime_power_branch_weight(27), 3)
        self.assertEqual(prime_power_branch_weight(12), 1)

        for n in range(1, 97):
            lcm_value = 1
            for m in range(1, n + 1):
                lcm_value = math.lcm(lcm_value, m)
            self.assertEqual(valuation_product(old_population_valuations(n)), lcm_value)

    def test_selected_product_matches_kummer_binomial_ratio(self) -> None:
        for n in range(1, 97):
            lcm_n = 1
            lcm_2n = 1
            for m in range(1, 2 * n + 1):
                lcm_2n = math.lcm(lcm_2n, m)
                if m <= n:
                    lcm_n = math.lcm(lcm_n, m)
            outer = lcm_2n // lcm_n
            expected = math.comb(2 * n, n) // outer
            self.assertEqual(valuation_product(selected_old_valuations(n)), expected)

    def test_count_centered_holonomy_exact_and_gauge_invariant(self) -> None:
        for n in range(1, 97):
            state = count_centered_holonomy(n)
            self.assertTrue(state.verify())
            self.assertEqual(
                state.omega,
                state.selected_product**n / state.population_product**state.selected_count,
            )

            pop = dict(state.population_valuations)
            sel = dict(state.selected_valuations)
            gauge = {2: 3, 3: -2, 5: 1}
            shifted_pop = {p: pop.get(p, 0) + n * 0 for p in pop}
            all_primes = set(pop) | set(sel) | set(gauge)
            shifted_population = {
                p: pop.get(p, 0) + n * gauge.get(p, 0) for p in all_primes
            }
            shifted_selected = {
                p: sel.get(p, 0) + state.selected_count * gauge.get(p, 0)
                for p in all_primes
            }
            shifted_h = {
                p: n * shifted_selected[p] - state.selected_count * shifted_population[p]
                for p in all_primes
            }
            self.assertEqual(
                tuple(sorted((p, e) for p, e in shifted_h.items() if e)),
                state.holonomy_valuations,
            )
            self.assertEqual(shifted_pop, pop)

    def test_symbolic_gamma_geometry(self) -> None:
        for n in range(1, 80):
            value = centered_geometry_ratio(n)
            self.assertEqual(value, GammaAffine(carry_count(n), -n))
        self.assertEqual(centered_geometry_ratio(7, 3), GammaAffine(0, -2))

    def test_mobius_log_deconvolution_identity(self) -> None:
        for n in range(1, 81):
            direct = direct_gamma_centered_prime_error_form(n)
            deconvolved = mobius_divisor_deconvolution_form(n)
            self.assertTrue(direct.equivalent(deconvolved), msg=f"n={n}")

    def test_hard_prime_skeleton_thickness(self) -> None:
        for n in range(2, 129):
            state = hard_prime_skeleton_thickness(n)
            self.assertTrue(state.verify())
            remainder = (-state.selected_count) % n
            self.assertEqual(
                state.skeleton_valuations,
                tuple((p, remainder) for p in state.hard_primes if remainder),
            )
            for p in state.hard_primes:
                exponent = n * carry_bit(n, p) - state.selected_count
                quotient, residue = divmod(exponent, n)
                self.assertEqual(residue, remainder)
                self.assertEqual(dict(state.thickness_valuations).get(p, 0), quotient)
            if 0 < state.selected_count < n:
                self.assertEqual(
                    state.thickness_valuations,
                    tuple((p, -1) for p in state.unselected_hard_primes),
                )

    def test_factor_and_mobius_reference_values(self) -> None:
        self.assertEqual(factor_positive_integer(1), ())
        self.assertEqual(factor_positive_integer(72), ((2, 3), (3, 2)))
        self.assertEqual(mobius(1), 1)
        self.assertEqual(mobius(6), 1)
        self.assertEqual(mobius(30), -1)
        self.assertEqual(mobius(12), 0)


class BRCReciprocalShellTests(unittest.TestCase):
    def test_shells_cover_each_d_once_and_geometry_is_exact(self) -> None:
        from enterprise_math.brc_count_centered_carry import reciprocal_shells

        for n in range(2, 129):
            shells = reciprocal_shells(n)
            covered: list[int] = []
            for shell in shells:
                self.assertTrue(shell.nonempty)
                for d in range(shell.lower_d, shell.upper_d + 1):
                    covered.append(d)
                    self.assertEqual(n // d, shell.quotient)
                    self.assertEqual(shell.geometry(d), centered_geometry_ratio(n, d))
            self.assertEqual(covered, list(range(2, n + 1)))

    def test_shell_jump_is_tau_minus_one(self) -> None:
        from enterprise_math.brc_count_centered_carry import reciprocal_quotient_shell

        n = 100
        shell = reciprocal_quotient_shell(n, 2)
        self.assertEqual((shell.lower_d, shell.midpoint_upper_d, shell.upper_d), (34, 40, 50))
        self.assertEqual(shell.jump, 1)  # tau(5)-1
        self.assertEqual(shell.geometry(40), GammaAffine(1, -2))
        self.assertEqual(shell.geometry(41), GammaAffine(0, -2))

    def test_shell_deconvolution_matches_direct_form(self) -> None:
        from enterprise_math.brc_count_centered_carry import mobius_shell_deconvolution_form

        for n in range(1, 81):
            direct = direct_gamma_centered_prime_error_form(n)
            shell = mobius_shell_deconvolution_form(n)
            self.assertTrue(direct.equivalent(shell), msg=f"n={n}")


if __name__ == "__main__":
    unittest.main()
