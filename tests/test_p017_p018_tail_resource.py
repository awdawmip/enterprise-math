import ast
import inspect
import unittest

import enterprise_math.p017_p018_tail_resource as tail_resource
from enterprise_math.legendre import is_prime
from enterprise_math.p017_p018_tail_resource import (
    odd_core_candidate_from_large_tail,
    recover_hard_core_state_from_prime_tail,
    recover_odd_core_state,
)


class P017P018TailResourceTests(unittest.TestCase):
    def test_odd_core_recovery_on_all_bounded_valid_states(self):
        for k in range(3, 250):
            for core in range(3, k + 1, 2):
                q_min = (k * k) // core + 1
                q_max = (k * (k + 2)) // core
                for tail in range(max(k + 1, q_min), q_max + 1):
                    state = core * tail
                    if not (k * k < state < (k + 1) ** 2):
                        continue
                    self.assertEqual(
                        odd_core_candidate_from_large_tail(k, tail), core
                    )
                    data = recover_odd_core_state(k, tail)
                    self.assertTrue(data["exists"])
                    self.assertEqual(data["core"], core)
                    self.assertEqual(data["state"], state)

    def test_tail_resource_is_unique_across_odd_cores(self):
        for k in range(3, 300):
            seen: dict[int, tuple[int, int]] = {}
            for core in range(3, k + 1, 2):
                q_min = (k * k) // core + 1
                q_max = (k * (k + 2)) // core
                for tail in range(max(k + 1, q_min), q_max + 1):
                    state = core * tail
                    if not (k * k < state < (k + 1) ** 2):
                        continue
                    previous = seen.setdefault(tail, (core, state))
                    self.assertEqual(previous, (core, state))

    def test_known_prime_tail_states_recover_exactly(self):
        data = recover_hard_core_state_from_prime_tail(64, 601)
        self.assertEqual(data["core"], 7)
        self.assertEqual(data["state"], 4207)
        self.assertEqual(data["radius"], 47)
        self.assertEqual(data["side"], 1)

        data = recover_hard_core_state_from_prime_tail(64, 457)
        self.assertEqual(data["core"], 9)
        self.assertEqual(data["state"], 4113)
        self.assertEqual(data["radius"], 47)
        self.assertEqual(data["side"], -1)

    def test_prime_tail_recovery_requires_actual_hard_core_candidate(self):
        self.assertTrue(is_prime(83))
        with self.assertRaises(ValueError):
            recover_hard_core_state_from_prime_tail(64, 83)
        with self.assertRaises(ValueError):
            recover_hard_core_state_from_prime_tail(64, 600)

    def test_validation(self):
        with self.assertRaises(ValueError):
            odd_core_candidate_from_large_tail(10, 10)
        with self.assertRaises(ValueError):
            recover_odd_core_state(1, 3)

    def test_module_has_no_float_or_true_division(self):
        tree = ast.parse(inspect.getsource(tail_resource))
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
