import ast
import inspect
import unittest
from math import gcd

import enterprise_math.p017_p018_cubic_pair_resolution as pair_resolution
from enterprise_math.p017_p018_cubic_pair_resolution import (
    cubic_partner_ambiguity_cutoff,
    high_small_core_forces_full_pair_resolution,
    odd_ambiguity_cell_count_bound,
    residual_pair_cubic_resolution,
)


class P017P018CubicPairResolutionTests(unittest.TestCase):
    def test_reference_cutoffs(self):
        self.assertEqual(cubic_partner_ambiguity_cutoff(64), 7)
        self.assertEqual(cubic_partner_ambiguity_cutoff(100), 8)
        self.assertEqual(cubic_partner_ambiguity_cutoff(200), 10)
        self.assertEqual(cubic_partner_ambiguity_cutoff(500), 13)
        self.assertEqual(cubic_partner_ambiguity_cutoff(631), 14)
        self.assertEqual(cubic_partner_ambiguity_cutoff(1000), 16)
        self.assertEqual(odd_ambiguity_cell_count_bound(64), 3)
        self.assertEqual(odd_ambiguity_cell_count_bound(1000), 7)

    def test_sharp_k64_prime_pair_hits_cutoff_and_horizon(self):
        data = residual_pair_cubic_resolution(64, 7, 9)
        self.assertEqual(data["ambiguity_cutoff"], 7)
        self.assertEqual(data["cubic_horizon"], 21)
        self.assertEqual(data["base_root"], 24)
        self.assertEqual(data["larger_base_root"], 21)
        self.assertTrue(data["small_core_inside_ambiguity_frontier"])
        self.assertFalse(data["larger_channel_is_high"])
        self.assertFalse(data["fully_core_pair_root_resolved"])

    def test_low_partner_channel_always_forces_small_core_under_cutoff(self):
        saw_low = False
        for k in range(16, 401):
            center = k * (k + 1)
            for d in range(3, k, 2):
                for e in range(d + 2, k + 1, 2):
                    if d * e >= k:
                        break
                    if gcd(d * e, center) != 1:
                        continue
                    data = residual_pair_cubic_resolution(k, d, e)
                    if not data["larger_channel_is_high"]:
                        saw_low = True
                        self.assertLessEqual(d, data["ambiguity_cutoff"])
                        self.assertTrue(data["small_core_inside_ambiguity_frontier"])
        self.assertTrue(saw_low)

    def test_above_cutoff_both_odd_core_channels_are_high(self):
        saw = False
        for k in range(16, 401):
            center = k * (k + 1)
            cutoff = cubic_partner_ambiguity_cutoff(k)
            for d in range(3, k, 2):
                if d <= cutoff:
                    continue
                for e in range(d + 2, k + 1, 2):
                    if d * e >= k:
                        break
                    if gcd(d * e, center) != 1:
                        continue
                    data = high_small_core_forces_full_pair_resolution(k, d, e)
                    self.assertTrue(data["fully_core_pair_root_resolved"])
                    self.assertGreater(data["base_root"], data["cubic_horizon"])
                    self.assertGreater(
                        data["larger_base_root"], data["cubic_horizon"]
                    )
                    saw = True
        self.assertTrue(saw)

    def test_inside_cutoff_does_not_force_ambiguity(self):
        # d<=D(k) is only the necessary location of ambiguity, not a claim that
        # every such pair has a low partner channel.
        data = residual_pair_cubic_resolution(100, 3, 7)
        self.assertLessEqual(data["small_core"], data["ambiguity_cutoff"])
        self.assertTrue(data["larger_channel_is_high"])
        self.assertTrue(data["fully_core_pair_root_resolved"])

    def test_known_above_cutoff_pair_is_fully_resolved(self):
        data = high_small_core_forces_full_pair_resolution(500, 17, 19)
        self.assertEqual(data["ambiguity_cutoff"], 13)
        self.assertTrue(data["fully_core_pair_root_resolved"])
        self.assertGreater(data["larger_base_root"], data["cubic_horizon"])

    def test_validation(self):
        with self.assertRaises(ValueError):
            cubic_partner_ambiguity_cutoff(1)
        with self.assertRaises(ValueError):
            residual_pair_cubic_resolution(64, 3, 5)  # 5 divides 64*65, so transversality fails.
        with self.assertRaises(ValueError):
            high_small_core_forces_full_pair_resolution(64, 7, 9)

    def test_module_has_no_float_or_true_division(self):
        tree = ast.parse(inspect.getsource(pair_resolution))
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
