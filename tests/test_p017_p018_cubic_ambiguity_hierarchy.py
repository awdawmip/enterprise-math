import ast
import inspect
import unittest
from math import gcd

import enterprise_math.p017_p018_cubic_ambiguity_hierarchy as hierarchy
from enterprise_math.p017_p018_cubic_ambiguity_hierarchy import (
    hierarchy_summary,
    low_partner_ambiguity_hierarchy,
    low_partner_core_floor,
    parity_multilift_small_core_cutoff,
    ternary_multilift_small_core_cutoff,
)
from enterprise_math.p017_p018_cubic_pair_resolution import residual_pair_cubic_resolution


class P017P018CubicAmbiguityHierarchyTests(unittest.TestCase):
    def test_reference_hierarchy_values(self):
        self.assertEqual(
            hierarchy_summary(64),
            {
                "k": 64,
                "partner_ambiguity_cutoff": 7,
                "low_partner_core_floor": 9,
                "parity_multilift_cutoff": 3,
                "ternary_multilift_cutoff": 1,
            },
        )
        self.assertEqual(hierarchy_summary(631)["low_partner_core_floor"], 46)
        self.assertEqual(hierarchy_summary(631)["partner_ambiguity_cutoff"], 14)
        self.assertEqual(hierarchy_summary(631)["parity_multilift_cutoff"], 6)
        self.assertEqual(hierarchy_summary(631)["ternary_multilift_cutoff"], 2)
        self.assertEqual(hierarchy_summary(1000)["low_partner_core_floor"], 63)
        self.assertEqual(hierarchy_summary(1000)["partner_ambiguity_cutoff"], 16)
        self.assertEqual(hierarchy_summary(1000)["parity_multilift_cutoff"], 7)
        self.assertEqual(hierarchy_summary(1000)["ternary_multilift_cutoff"], 2)

    def test_k64_sharp_pair_is_ambiguous_but_parity_singleton(self):
        data = low_partner_ambiguity_hierarchy(64, 7, 9)
        self.assertEqual(data["larger_base_root"], data["cubic_horizon"])
        self.assertEqual(data["low_partner_core_floor"], 9)
        self.assertFalse(data["parity_cell_can_have_multiple_lifts"])
        self.assertTrue(data["ternary_exception"])

    def test_low_partner_pairs_obey_all_exact_cutoffs_on_bounded_domain(self):
        saw_parity_repeat = False
        saw_generic = False
        for k in range(16, 401):
            center = k * (k + 1)
            for d in range(3, k, 2):
                for e in range(d + 2, k + 1, 2):
                    if d * e >= k:
                        break
                    if gcd(d * e, center) != 1:
                        continue
                    base = residual_pair_cubic_resolution(k, d, e)
                    if base["larger_channel_is_high"]:
                        continue
                    data = low_partner_ambiguity_hierarchy(k, d, e)
                    self.assertGreaterEqual(e, data["low_partner_core_floor"])
                    self.assertLessEqual(d, data["ambiguity_cutoff"])
                    if data["parity_cell_can_have_multiple_lifts"]:
                        saw_parity_repeat = True
                        self.assertLessEqual(d, data["parity_multilift_cutoff"])
                    if data["generic_mod3_cell"]:
                        saw_generic = True
                    if data["generic_mod3_cell_can_have_multiple_prime_lifts"]:
                        self.assertLessEqual(d, data["ternary_multilift_cutoff"])
        self.assertTrue(saw_parity_repeat)
        self.assertTrue(saw_generic)

    def test_generic_ternary_cutoff_has_exact_arithmetic_boundary(self):
        # First compact witness found by the exact integer search: L=223 and
        # 6*5*223=6690=k-1.  Thus E6=5 is attained rather than being a loose
        # asymptotic cutoff.
        data = low_partner_ambiguity_hierarchy(6691, 5, 223)
        self.assertEqual(data["low_partner_core_floor"], 223)
        self.assertEqual(data["ternary_multilift_cutoff"], 5)
        self.assertTrue(data["generic_mod3_cell"])
        self.assertTrue(data["generic_mod3_cell_can_have_multiple_prime_lifts"])
        self.assertEqual(6 * 5 * 223, 6690)

    def test_above_parity_cutoff_low_partner_cells_are_single_lift_cells(self):
        for k in range(16, 300):
            center = k * (k + 1)
            e2 = parity_multilift_small_core_cutoff(k)
            for d in range(max(3, e2 + 1), k, 2):
                for e in range(d + 2, k + 1, 2):
                    if d * e >= k:
                        break
                    if gcd(d * e, center) != 1:
                        continue
                    base = residual_pair_cubic_resolution(k, d, e)
                    if base["larger_channel_is_high"]:
                        continue
                    data = low_partner_ambiguity_hierarchy(k, d, e)
                    self.assertFalse(data["parity_cell_can_have_multiple_lifts"])
                    self.assertGreaterEqual(2 * d * e, k)

    def test_validation(self):
        with self.assertRaises(ValueError):
            low_partner_core_floor(1)
        with self.assertRaises(ValueError):
            hierarchy_summary(15)
        with self.assertRaises(ValueError):
            low_partner_ambiguity_hierarchy(100, 3, 7)  # partner channel is already cubic-high

    def test_module_has_no_float_or_true_division(self):
        tree = ast.parse(inspect.getsource(hierarchy))
        floats = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.Constant) and isinstance(node.value, float)
        ]
        divisions = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div)
        ]
        self.assertEqual(floats, [])
        self.assertEqual(divisions, [])


if __name__ == "__main__":
    unittest.main()
