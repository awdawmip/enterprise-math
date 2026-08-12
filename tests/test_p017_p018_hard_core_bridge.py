import ast
import inspect
import unittest

import enterprise_math.p017_p018_hard_core_bridge as bridge
from enterprise_math.legendre import is_prime
from enterprise_math.p017_p018_hard_core_bridge import (
    RISK_K_MAX,
    SMALL_ACTUAL_GAP_ROWS,
    SMALL_GAP_COMPOSITE_WITNESSES,
    enumerate_small_actual_gap_rows,
    finite_base_gap_reduction,
    finite_base_risk_triples,
    prime_tail_root_gap_certificate,
)


class P017P018HardCoreBridgeTests(unittest.TestCase):
    def test_analytic_finite_reduction_has_exact_small_risk_frontier(self):
        rows = finite_base_risk_triples()
        self.assertEqual(len(rows), 58)
        self.assertEqual(max(row[0] for row in rows), 198)
        self.assertEqual(RISK_K_MAX, 284)
        for k, d, e, j_d, j_e in rows:
            data = finite_base_gap_reduction(k, d, e)
            self.assertEqual(data["j_d"], j_d)
            self.assertEqual(data["j_e"], j_e)
            self.assertLessEqual(j_d - j_e, 3)
            self.assertLessEqual(d, 15)
            self.assertLessEqual(e, 21)
            self.assertLessEqual(k, RISK_K_MAX)

    def test_exact_small_actual_gap_rows_are_complete(self):
        self.assertEqual(enumerate_small_actual_gap_rows(), SMALL_ACTUAL_GAP_ROWS)
        self.assertEqual(len(SMALL_ACTUAL_GAP_ROWS), 13)
        self.assertTrue(all(row[7] - row[8] == 2 for row in SMALL_ACTUAL_GAP_ROWS))

    def test_every_small_actual_gap_row_has_explicit_composite_tail(self):
        self.assertEqual(
            len(SMALL_ACTUAL_GAP_ROWS), len(SMALL_GAP_COMPOSITE_WITNESSES)
        )
        for row, (side, factor) in zip(
            SMALL_ACTUAL_GAP_ROWS, SMALL_GAP_COMPOSITE_WITNESSES, strict=True
        ):
            target = row[5] if side == "d" else row[6]
            self.assertGreater(target, factor)
            self.assertEqual(target % factor, 0)
            self.assertFalse(is_prime(target))
            self.assertFalse(is_prime(row[5]) and is_prime(row[6]))

    def test_prime_tail_certificate_covers_entire_counterexample_box(self):
        saw_prime_pair = False
        for k, d, e, _, _ in finite_base_risk_triples():
            center = k * (k + 1)
            for orientation in (-1, 1):
                for radius in range(1, k):
                    d_num = center + orientation * radius
                    e_num = center - orientation * radius
                    if d_num % d or e_num % e:
                        continue
                    q_d = d_num // d
                    q_e = e_num // e
                    if q_d <= k or q_e <= k:
                        continue
                    if not is_prime(q_d) or not is_prime(q_e):
                        continue
                    data = prime_tail_root_gap_certificate(
                        k, d, e, radius, orientation
                    )
                    self.assertGreaterEqual(data["root_gap"], 3)
                    saw_prime_pair = True
        self.assertTrue(saw_prime_pair)

    def test_sharp_gap_three_witness(self):
        data = prime_tail_root_gap_certificate(64, 7, 9, 47, 1)
        self.assertEqual(data["q_d"], 601)
        self.assertEqual(data["q_e"], 457)
        self.assertEqual((data["root_d"], data["root_e"]), (24, 21))
        self.assertEqual(data["root_gap"], 3)

    def test_known_k22_hard_core_witness_has_gap_four(self):
        data = prime_tail_root_gap_certificate(22, 3, 7, 5, -1)
        self.assertEqual(data["q_d"], 167)
        self.assertEqual(data["q_e"], 73)
        self.assertEqual(data["root_gap"], 4)

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            finite_base_gap_reduction(16, 3, 7)
        with self.assertRaises(ValueError):
            prime_tail_root_gap_certificate(64, 7, 9, 47, 0)
        with self.assertRaises(ValueError):
            prime_tail_root_gap_certificate(16, 3, 5, 7, 1)

    def test_bridge_module_has_no_float_or_true_division(self):
        tree = ast.parse(inspect.getsource(bridge))
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
