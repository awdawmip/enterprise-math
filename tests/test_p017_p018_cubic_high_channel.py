import ast
import inspect
import unittest
from math import gcd

import enterprise_math.p017_p018_cubic_high_channel as cubic_high
from enterprise_math.p017_p018_cubic_high_channel import (
    ABSTRACT_SMALL_K_EXCEPTIONS,
    cubic_candidate_horizon,
    cubic_to_quartic_margin,
    hard_core_cubic_routing,
    small_k_abstract_exception_frontier,
    transverse_small_endpoint_cubic_channel,
)


class P017P018CubicHighChannelTests(unittest.TestCase):
    def test_small_k_exception_frontier_is_exact_and_nontransverse(self):
        self.assertEqual(
            small_k_abstract_exception_frontier(),
            ABSTRACT_SMALL_K_EXCEPTIONS,
        )
        self.assertEqual(ABSTRACT_SMALL_K_EXCEPTIONS, ((17, 3, 5, 9, 9),))
        k, d, e, root, horizon = ABSTRACT_SMALL_K_EXCEPTIONS[0]
        self.assertEqual(root, horizon)
        self.assertNotEqual(gcd(d * e, k * (k + 1)), 1)
        self.assertEqual(gcd(d * e, k * (k + 1)), 3)

    def test_large_cubic_to_quartic_margin_is_integer_certified(self):
        for k in (64, 65, 100, 256, 631, 1000, 4096):
            data = cubic_to_quartic_margin(k)
            self.assertGreaterEqual(data["cubic_base"], 20)
            self.assertGreaterEqual(
                data["quartic_root"], data["cubic_horizon"] + 1
            )
            self.assertGreaterEqual(data["root_margin"], 1)

    def test_every_bounded_transverse_small_endpoint_is_strictly_cubic_high(self):
        saw = False
        for k in range(16, 401):
            center = k * (k + 1)
            for d in range(3, k, 2):
                for e in range(d + 2, k + 1, 2):
                    if d * e >= k:
                        break
                    if gcd(d * e, center) != 1:
                        continue
                    data = transverse_small_endpoint_cubic_channel(k, d, e)
                    self.assertGreater(data["base_root"], data["cubic_horizon"])
                    self.assertGreaterEqual(data["height_above_horizon"], 1)
                    self.assertTrue(
                        all(
                            root > data["cubic_horizon"]
                            for root in data["candidate_channel"]
                        )
                    )
                    saw = True
        self.assertTrue(saw)

    def test_cubic_high_target_identifies_odd_core_on_bounded_domain(self):
        # This is an executable regression for the P018 #195 mother theorem as
        # consumed by the bridge: an above-horizon target cannot be shared by
        # two distinct odd divisor labels.
        for k in range(16, 220):
            center = k * (k + 1)
            for d in range(3, k, 2):
                for e in range(d + 2, k + 1, 2):
                    if d * e >= k:
                        break
                    if gcd(d * e, center) != 1:
                        continue
                    data = transverse_small_endpoint_cubic_channel(k, d, e)
                    for target in data["candidate_channel"]:
                        hits = []
                        for divisor in range(3, k + 1, 2):
                            base = cubic_high.base_root_index(k, divisor)
                            if target in (base, base + 1):
                                hits.append(divisor)
                        self.assertEqual(hits, [d])

    def test_sharp_k64_hard_core_pair_has_high_small_core_route(self):
        data = hard_core_cubic_routing(64, 47)
        self.assertEqual(data["lower_core"], 9)
        self.assertEqual(data["upper_core"], 7)
        self.assertEqual(data["small_core"], 7)
        self.assertEqual(data["other_core"], 9)
        self.assertEqual(data["small_core_side"], 1)
        self.assertEqual(data["small_core_tail"], 601)
        self.assertEqual(data["small_core_actual_root"], 24)
        self.assertEqual(data["cubic_horizon"], 21)
        self.assertEqual(data["candidate_channel"], (24, 25))

    def test_other_known_residual_pairs_route_above_horizon(self):
        for k, radius in ((100, 19), (100, 71), (200, 43), (200, 181)):
            data = hard_core_cubic_routing(k, radius)
            self.assertLess(data["core_product"], k)
            self.assertGreater(data["base_root"], data["cubic_horizon"])
            self.assertIn(data["small_core_actual_root"], data["candidate_channel"])

    def test_validation(self):
        with self.assertRaises(ValueError):
            cubic_candidate_horizon(1)
        with self.assertRaises(ValueError):
            cubic_to_quartic_margin(63)
        with self.assertRaises(ValueError):
            transverse_small_endpoint_cubic_channel(64, 4, 7)
        with self.assertRaises(ValueError):
            transverse_small_endpoint_cubic_channel(17, 3, 5)
        with self.assertRaises(ValueError):
            hard_core_cubic_routing(64, 2)

    def test_module_has_no_float_or_true_division(self):
        tree = ast.parse(inspect.getsource(cubic_high))
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
