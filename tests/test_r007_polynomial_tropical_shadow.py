from __future__ import annotations

import importlib.util
import itertools
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).parents[1] / "experiments" / "r007_polynomial_tropical_shadow.py"
spec = importlib.util.spec_from_file_location("r007_polynomial_tropical_shadow", MODULE_PATH)
assert spec is not None and spec.loader is not None
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class R007PolynomialTropicalShadowTests(unittest.TestCase):
    def test_low_degree_initial_form_criterion_is_exact_on_small_cases(self) -> None:
        for p in (3, 5, 7):
            max_degree = min(p - 2, 3)
            for beta in range(1, 4):
                for degree in range(max_degree + 1):
                    for coefficients in itertools.product(range(-2, 3), repeat=degree + 1):
                        if coefficients[-1] == 0:
                            continue
                        self.assertEqual(
                            mod.low_degree_shadow_descent_criterion(coefficients, p, beta),
                            mod.polynomial_shadow_descends_bruteforce(coefficients, p, beta),
                        )

    def test_phase_defects_are_confined_to_newton_tie_shells(self) -> None:
        examples = ((1, 1), (1, 0, 1), (9, 3, 1), (25, 0, 5, 1), (1, -3, 0, 1))
        for p in (3, 5, 7):
            for beta in range(1, 8):
                for coefficients in examples:
                    candidates = set(mod.phase_defect_candidate_shells(coefficients, p, beta))
                    ties = set(mod.tropical_tie_shells(coefficients, p, beta))
                    self.assertLessEqual(candidates, ties)
                    self.assertTrue(mod.tie_shell_bound_holds(coefficients, p, beta))

    def test_degree_bounds_number_of_tropical_phase_frontiers(self) -> None:
        for p in (3, 5, 7):
            for beta in range(1, 12):
                for coefficients in ((1, 1), (9, 3, 1), (81, 0, 9, 0, 1), (125, 25, 5, 1)):
                    self.assertLessEqual(
                        len(mod.tropical_tie_shells(coefficients, p, beta)),
                        max(mod.polynomial_degree(coefficients), 0),
                    )

    def test_quadratic_closed_criterion_matches_bruteforce(self) -> None:
        for p in (5, 7, 11):
            for beta in range(1, 4):
                modulus = p**beta
                for c in range(-2 * modulus, 2 * modulus + 1):
                    expected = True if c == 0 else mod.quadratic_x2_plus_c_shadow_descends(c, p, beta)
                    self.assertEqual(
                        expected,
                        mod.polynomial_shadow_descends_bruteforce((c, 0, 1), p, beta),
                    )


if __name__ == "__main__":
    unittest.main()
