from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).parents[1] / "experiments" / "r007_operation_language_repair.py"
spec = importlib.util.spec_from_file_location("r007_operation_language_repair", MODULE_PATH)
assert spec is not None and spec.loader is not None
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class R007OperationLanguageRepairTests(unittest.TestCase):
    def test_translation_and_affine_closed_forms_match_moore_refinement(self) -> None:
        for p in (2, 3, 5):
            for beta in range(1, 5):
                modulus = p**beta
                shadow = mod.valuation_shadow_partition(p, beta)
                multipliers = mod.all_multiplier_maps(p, beta)
                for r in range(beta + 1):
                    translation = mod.translation_generator(p, beta, r)
                    translation_partition = mod.repair_partition(shadow, (translation,))
                    joint_partition = mod.repair_partition(shadow, (translation, *multipliers))
                    expected_translation = mod.canonical_partition(
                        mod.translation_only_label(n, p, beta, r)
                        for n in range(modulus)
                    )
                    expected_joint = mod.canonical_partition(
                        mod.affine_significant_label(n, p, beta, r)
                        for n in range(modulus)
                    )
                    self.assertEqual(translation_partition, expected_translation)
                    self.assertEqual(joint_partition, expected_joint)
                    self.assertEqual(len(set(joint_partition)), mod.affine_repair_count(p, beta, r))
                    self.assertEqual(len(set(translation_partition)), mod.translation_repair_count(p, beta, r))

    def test_affine_label_is_exactly_relative_significant_digit_precision(self) -> None:
        for p in (2, 3, 5):
            for beta in range(1, 5):
                modulus = p**beta
                for r in range(beta + 1):
                    left = mod.canonical_partition(
                        mod.affine_significant_label(n, p, beta, r)
                        for n in range(modulus)
                    )
                    right = mod.canonical_partition(
                        mod.significant_digit_label(n, p, beta, r)
                        for n in range(modulus)
                    )
                    self.assertEqual(left, right)

    def test_semidirect_normal_form_requires_the_correct_repair_order(self) -> None:
        for p in (2, 3, 5):
            for beta in range(1, 4):
                shadow = mod.valuation_shadow_partition(p, beta)
                multipliers = mod.all_multiplier_maps(p, beta)
                for r in range(beta + 1):
                    translation = (mod.translation_generator(p, beta, r),)
                    joint = mod.repair_partition(shadow, (*translation, *multipliers))
                    correct = mod.ordered_two_stage_repair(shadow, multipliers, translation)
                    self.assertEqual(correct, joint)

    def test_refining_for_translation_can_break_safe_multiplication(self) -> None:
        p, beta, r = 2, 3, 2
        shadow = mod.valuation_shadow_partition(p, beta)
        times_two = mod.map_tuple(8, lambda x: (2 * x) % 8)
        self.assertTrue(mod.operation_respects_partition(shadow, times_two))
        translated = mod.repair_partition(shadow, (mod.translation_generator(p, beta, r),))
        self.assertFalse(mod.operation_respects_partition(translated, times_two))
        joint = mod.repair_partition(translated, mod.all_multiplier_maps(p, beta))
        self.assertTrue(mod.operation_respects_partition(joint, times_two))

    def test_phase_tick_formulas_match_exact_state_count_differences(self) -> None:
        for p in (2, 3, 5, 7):
            for beta in range(1, 7):
                for r in range(beta):
                    self.assertEqual(
                        mod.translation_repair_count(p, beta, r + 1) - mod.translation_repair_count(p, beta, r),
                        mod.translation_phase_tick_increment(p, beta, r),
                    )
                    self.assertEqual(
                        mod.affine_repair_count(p, beta, r + 1) - mod.affine_repair_count(p, beta, r),
                        mod.affine_phase_tick_increment(p, beta, r),
                    )

    def test_multiplication_interference_cost_is_exact(self) -> None:
        for p in (2, 3, 5, 7):
            for beta in range(1, 7):
                for r in range(beta + 1):
                    self.assertEqual(
                        mod.affine_repair_count(p, beta, r) - mod.translation_repair_count(p, beta, r),
                        mod.multiplication_interference_cost(p, beta, r),
                    )

    def test_first_significant_precision_formula(self) -> None:
        for p in (2, 3, 5):
            for beta in range(1, 5):
                modulus = p**beta
                for left in range(modulus):
                    for right in range(modulus):
                        expected = None
                        for r in range(beta + 1):
                            if mod.significant_digit_label(left, p, beta, r) != mod.significant_digit_label(right, p, beta, r):
                                expected = r
                                break
                        self.assertEqual(
                            mod.first_significant_phase_precision(left, right, p, beta),
                            expected,
                        )


if __name__ == "__main__":
    unittest.main()
