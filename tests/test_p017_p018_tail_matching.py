import ast
import inspect
import unittest

import enterprise_math.p017_p018_tail_matching as tail_matching
from enterprise_math.p017_cofactor_window import square_basin_smooth_tail
from enterprise_math.p017_mirror import anchor_surviving_radius, mirror_pair
from enterprise_math.p017_p018_tail_matching import (
    residual_hard_core_tail_cycle,
    residual_hard_core_tail_partner,
)


class P017P018TailMatchingTests(unittest.TestCase):
    def _hard_core_pairs(self, k: int):
        for radius in range(1, k):
            if not anchor_surviving_radius(k, radius):
                continue
            lower, upper = mirror_pair(k, radius)
            lower_data = square_basin_smooth_tail(k, lower)
            upper_data = square_basin_smooth_tail(k, upper)
            if bool(lower_data["is_prime"]) or bool(upper_data["is_prime"]):
                continue
            a = int(lower_data["smooth_core"])
            b = int(upper_data["smooth_core"])
            if a * b >= k:
                continue
            yield (
                radius,
                int(lower_data["tail"]),
                int(upper_data["tail"]),
                a,
                b,
            )

    def test_partner_map_is_exact_fixed_point_free_involution(self):
        saw_pair = False
        for k in range(16, 350):
            for radius, lower_tail, upper_tail, lower_core, upper_core in self._hard_core_pairs(k):
                left = residual_hard_core_tail_cycle(k, lower_tail)
                right = residual_hard_core_tail_cycle(k, upper_tail)
                self.assertEqual(left["partner_tail"], upper_tail)
                self.assertEqual(right["partner_tail"], lower_tail)
                self.assertEqual(left["core"], lower_core)
                self.assertEqual(left["partner_core"], upper_core)
                self.assertEqual(left["radius"], radius)
                self.assertEqual(right["radius"], radius)
                self.assertNotEqual(lower_tail, upper_tail)
                saw_pair = True
        self.assertTrue(saw_pair)

    def test_prime_vertices_are_globally_nonreused_in_bounded_hard_core(self):
        for k in range(16, 400):
            seen: dict[int, tuple[int, int]] = {}
            for radius, lower_tail, upper_tail, _, _ in self._hard_core_pairs(k):
                for side, tail in ((-1, lower_tail), (1, upper_tail)):
                    previous = seen.setdefault(tail, (radius, side))
                    self.assertEqual(previous, (radius, side))

    def test_sharp_k64_pair_is_one_two_cycle(self):
        left = residual_hard_core_tail_partner(64, 457)
        right = residual_hard_core_tail_partner(64, 601)
        self.assertEqual(left["partner_tail"], 601)
        self.assertEqual(right["partner_tail"], 457)
        self.assertEqual(left["radius"], 47)
        self.assertEqual(right["radius"], 47)

    def test_non_residual_tail_is_rejected(self):
        with self.assertRaises(ValueError):
            residual_hard_core_tail_partner(64, 67)

    def test_matching_module_has_no_float_or_true_division(self):
        tree = ast.parse(inspect.getsource(tail_matching))
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
