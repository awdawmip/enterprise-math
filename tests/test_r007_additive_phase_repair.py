from __future__ import annotations

import importlib.util
from math import gcd
from pathlib import Path
import unittest


MODULE_PATH = Path(__file__).parents[1] / "experiments" / "r007_additive_phase_repair.py"
spec = importlib.util.spec_from_file_location("r007_additive_phase_repair", MODULE_PATH)
assert spec is not None and spec.loader is not None
ap = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ap)


class TestR007AdditivePhaseRepair(unittest.TestCase):
    def test_shadow_is_principal_ideal_and_unit_orbit_with_phi_fibers(self) -> None:
        for ceiling in range(1, 31):
            for residue in range(ceiling):
                shadow = ap.divisor_shadow(residue, ceiling)
                self.assertEqual(
                    ap.principal_ideal(residue, ceiling),
                    ap.principal_ideal(shadow, ceiling),
                )
                self.assertEqual(
                    ap.unit_orbit(residue, ceiling),
                    ap.shadow_fiber(ceiling, shadow),
                )
            for shadow in ap.divisors(ceiling):
                fiber = ap.shadow_fiber(ceiling, shadow)
                self.assertEqual(len(fiber), ap.euler_phi(ceiling // shadow))
                self.assertEqual(len(fiber), ap.additive_repair_fiber_size(ceiling, shadow))

    def test_multiplication_descends_exactly(self) -> None:
        for ceiling in range(1, 31):
            for x in range(ceiling):
                for y in range(ceiling):
                    lhs = ap.divisor_shadow(x * y, ceiling)
                    rhs = ap.shadow_product(
                        ap.divisor_shadow(x, ceiling),
                        ap.divisor_shadow(y, ceiling),
                        ceiling,
                    )
                    self.assertEqual(lhs, rhs)

    def test_safe_translation_classification(self) -> None:
        for ceiling in range(1, 31):
            expected_step = ceiling // gcd(ceiling, 2)
            self.assertEqual(ap.translation_safe_step(ceiling), expected_step)
            for step in range(0, 2 * ceiling + 1):
                brute = True
                for shadow in ap.divisors(ceiling):
                    outputs = {
                        ap.divisor_shadow(r + step, ceiling)
                        for r in ap.shadow_fiber(ceiling, shadow)
                    }
                    if len(outputs) != 1:
                        brute = False
                        break
                self.assertEqual(
                    ap.translation_is_shadow_safe(ceiling, step),
                    brute,
                )
                if brute:
                    for shadow in ap.divisors(ceiling):
                        output = ap.induced_translation(ceiling, step, shadow)
                        self.assertIn(output, ap.divisors(ceiling))

    def test_exact_translation_repair_formula(self) -> None:
        for ceiling in range(1, 41):
            for step in range(1, ceiling + 1):
                self.assertEqual(
                    len(ap.moore_partition(ceiling, step)),
                    ap.translation_repair_class_count(ceiling, step),
                )

    def test_coprime_translation_forces_full_residue_phase(self) -> None:
        for ceiling in range(1, 31):
            for step in range(1, ceiling + 1):
                if gcd(step, ceiling) == 1:
                    partition = ap.moore_partition(ceiling, step)
                    self.assertEqual(len(partition), ceiling)
                    self.assertTrue(all(len(block) == 1 for block in partition))

    def test_binary_addition_descends_only_for_one_and_two(self) -> None:
        for ceiling in range(1, 20):
            brute = True
            by_shadow: dict[tuple[int, int], set[int]] = {}
            for x in range(ceiling):
                for y in range(ceiling):
                    key = (
                        ap.divisor_shadow(x, ceiling),
                        ap.divisor_shadow(y, ceiling),
                    )
                    by_shadow.setdefault(key, set()).add(
                        ap.divisor_shadow(x + y, ceiling)
                    )
            brute = all(len(outputs) == 1 for outputs in by_shadow.values())
            self.assertEqual(ap.addition_descends(ceiling), brute)


if __name__ == "__main__":
    unittest.main()
