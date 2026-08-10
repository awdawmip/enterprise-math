from __future__ import annotations

import importlib.util
from itertools import combinations
from math import gcd, lcm
from pathlib import Path
import unittest


MODULE_PATH = Path(__file__).parents[1] / "experiments" / "r007_divisor_action_calculus.py"
spec = importlib.util.spec_from_file_location("r007_divisor_action_calculus", MODULE_PATH)
assert spec is not None and spec.loader is not None
calc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(calc)


class R007DivisorActionCalculusTests(unittest.TestCase):
    def test_future_envelope_is_exact_signature_quotient(self) -> None:
        probe_families = [
            (),
            (2,),
            (3,),
            (2, 3),
            (4, 6),
            (5, 7, 9),
        ]
        for G in range(1, 50):
            divisors = calc.positive_divisors(G)
            for probes in probe_families + [(G,)]:
                C = calc.future_probe_envelope(G, probes)
                self.assertEqual(G % C, 0)
                for x in divisors:
                    for y in divisors:
                        same_signature = (
                            calc.future_signature(x, G, probes)
                            == calc.future_signature(y, G, probes)
                        )
                        same_projection = gcd(x, C) == gcd(y, C)
                        self.assertEqual(same_signature, same_projection)

    def test_fixed_mask_basis_generates_all_actions_with_exact_depth(self) -> None:
        for G in range(1, 100):
            basis = calc.fixed_mask_action_basis(G)
            self.assertEqual(len(basis), calc.big_omega(G))

            closure = {G}
            changed = True
            while changed:
                changed = False
                for state in tuple(closure):
                    for mask in basis:
                        child = gcd(state, mask)
                        if child not in closure:
                            closure.add(child)
                            changed = True
            self.assertEqual(closure, set(calc.positive_divisors(G)))

            for target in calc.positive_divisors(G):
                result = G
                program = calc.compile_fixed_mask_action(G, target)
                for mask in program:
                    result = gcd(result, mask)
                self.assertEqual(result, target)
                self.assertEqual(
                    len(program),
                    calc.little_omega(G // target),
                )

    def test_exact_action_depth_spectrum(self) -> None:
        for G in range(1, 150):
            measured = calc.action_depth_spectrum(G)
            formula = calc.action_depth_spectrum_formula(G)
            self.assertEqual(
                tuple(measured.get(depth, 0) for depth in range(len(formula))),
                formula,
            )
            self.assertEqual(sum(formula), calc.divisor_count(G))

    def test_future_language_expansion_splits_only_saturated_coordinates(self) -> None:
        for G in range(1, 70):
            divisors = calc.positive_divisors(G)
            for coarse in divisors:
                for fine in divisors:
                    if fine % coarse:
                        continue
                    for observed in calc.positive_divisors(coarse):
                        old_fiber = [
                            state
                            for state in divisors
                            if gcd(state, coarse) == observed
                        ]
                        refined = {gcd(state, fine) for state in old_fiber}
                        self.assertEqual(
                            len(refined),
                            calc.refinement_split_count(
                                G, coarse, fine, observed
                            ),
                        )

    def test_extremal_witness_cover_preserves_gcd_and_lcm(self) -> None:
        families = [
            (6, 10, 15),
            (12, 18, 30, 42),
            (8, 12, 18, 27),
            (14, 21, 35, 70),
            (16, 24, 36, 54, 81),
        ]
        for values in families:
            full_gcd = values[0]
            full_lcm = 1
            for value in values[1:]:
                full_gcd = gcd(full_gcd, value)
            for value in values:
                full_lcm = lcm(full_lcm, value)

            for size in range(1, len(values) + 1):
                for indices in combinations(range(len(values)), size):
                    subset = [values[index] for index in indices]
                    subset_gcd = subset[0]
                    subset_lcm = 1
                    for value in subset[1:]:
                        subset_gcd = gcd(subset_gcd, value)
                    for value in subset:
                        subset_lcm = lcm(subset_lcm, value)

                    self.assertEqual(
                        subset_gcd == full_gcd,
                        calc.witness_cover_preserves(
                            values, indices, mode="gcd"
                        ),
                    )
                    self.assertEqual(
                        subset_lcm == full_lcm,
                        calc.witness_cover_preserves(
                            values, indices, mode="lcm"
                        ),
                    )

    def test_squarefree_balanced_compiler_interpolates_endpoints(self) -> None:
        for prime_count in range(1, 10):
            self.assertEqual(
                calc.balanced_squarefree_compiler_storage(prime_count, 1),
                2**prime_count - 1,
            )
            self.assertEqual(
                calc.balanced_squarefree_compiler_storage(
                    prime_count, prime_count
                ),
                prime_count,
            )


if __name__ == "__main__":
    unittest.main()
