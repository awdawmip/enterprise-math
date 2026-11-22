import ast
import inspect
import unittest

import enterprise_math.p017_p018_hard_core_cover as cover
from enterprise_math.p017_p018_hard_core_cover import (
    disjoint_small_core_channels,
    hard_core_small_endpoint,
    small_core_candidate_channel,
    small_core_channel_cover,
    small_core_cutoff,
)


class P017P018HardCoreCoverTests(unittest.TestCase):
    def test_every_odd_product_edge_meets_small_core_cover(self):
        for k in range(16, 500):
            cutoff = small_core_cutoff(k)
            for a in range(3, k, 2):
                for b in range(3, k, 2):
                    if a * b >= k:
                        break
                    data = hard_core_small_endpoint(k, a, b)
                    self.assertLessEqual(data["small_endpoint"], cutoff)

    def test_distinct_small_core_channels_are_pairwise_disjoint(self):
        for k in range(16, 500):
            cutoff = small_core_cutoff(k)
            cores = list(range(3, cutoff + 1, 2))
            for i, d in enumerate(cores):
                for e in cores[i + 1 :]:
                    data = disjoint_small_core_channels(k, d, e)
                    self.assertLess(d * e, k)
                    self.assertGreaterEqual(data["base_root_gap"], 2)
                    self.assertTrue(
                        set(data["d_channel"]).isdisjoint(data["e_channel"])
                    )

    def test_cover_cell_count_is_exact(self):
        for k in range(2, 300):
            data = small_core_channel_cover(k)
            expected = len(range(3, small_core_cutoff(k) + 1, 2))
            self.assertEqual(data["cell_count"], expected)
            self.assertEqual(len(data["channels"]), expected)

    def test_example_channels(self):
        self.assertEqual(small_core_cutoff(1000), 31)
        self.assertEqual(small_core_candidate_channel(1000, 3), (577, 578))
        self.assertEqual(small_core_candidate_channel(1000, 7), (377, 378))
        data = disjoint_small_core_channels(1000, 3, 7)
        self.assertGreaterEqual(data["base_root_gap"], 2)

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            hard_core_small_endpoint(20, 5, 5)
        with self.assertRaises(ValueError):
            small_core_candidate_channel(100, 11)
        with self.assertRaises(ValueError):
            disjoint_small_core_channels(100, 3, 11)

    def test_cover_module_has_no_float_or_true_division(self):
        tree = ast.parse(inspect.getsource(cover))
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
