import unittest

from enterprise_math.p018_root_state_carry import (
    horizon_state_carry,
    ternary_state_count_band,
    ternary_state_count_carry,
)
from enterprise_math.p018_root_state_decomposition import (
    exact_distinct_root_state_count,
    horizon_fiber_present,
)


class P018RootStateCarryTests(unittest.TestCase):
    def test_carry_reconstructs_exact_count_exhaustively(self):
        saw_zero = False
        saw_one = False
        saw_negative_raw_threshold = False
        for root_exp in range(1, 8):
            for n in range(1, 10000):
                data = horizon_state_carry(n, root_exp)
                closed = exact_distinct_root_state_count(n, root_exp)
                self.assertEqual(
                    data["distinct_root_count"], closed["distinct_root_count"]
                )
                self.assertEqual(
                    data["horizon_carry"],
                    closed["horizon_fiber_present"],
                )
                if data["horizon"]:
                    self.assertEqual(
                        data["horizon_carry"],
                        horizon_fiber_present(n, root_exp),
                    )
                    saw_zero |= not data["horizon_carry"]
                    saw_one |= bool(data["horizon_carry"])
                    saw_negative_raw_threshold |= data["raw_carry_threshold"] < 0
        self.assertTrue(saw_zero)
        self.assertTrue(saw_one)
        self.assertTrue(saw_negative_raw_threshold)

    def test_ternary_carry_reconstructs_exact_count_on_dense_grid(self):
        seen = set()
        for root_exp in range(1, 9):
            for n in range(1, 50000):
                data = ternary_state_count_carry(n, root_exp)
                closed = exact_distinct_root_state_count(n, root_exp)
                self.assertEqual(
                    data["distinct_root_count"], closed["distinct_root_count"]
                )
                self.assertIn(data["ternary_carry"], (0, 1, 2))
                self.assertLessEqual(
                    data["lower_threshold"], data["upper_threshold"]
                )
                self.assertIn(
                    data["distinct_root_count"],
                    ternary_state_count_band(n, root_exp),
                )
                q = data["horizon_quotient"]
                d = data["high_denominator_max"]
                self.assertGreaterEqual(d, max(0, q - 1))
                self.assertLessEqual(d, q + 1)
                if q > 0 and d == q - 1:
                    self.assertTrue(horizon_state_carry(n, root_exp)["horizon_carry"])
                seen.add(data["ternary_carry"])
        self.assertEqual(seen, {0, 1, 2})

    def test_ternary_carry_thresholds_are_exact_within_each_horizon_shell(self):
        for root_exp in range(1, 8):
            by_horizon: dict[int, list[tuple[int, int]]] = {}
            for n in range(1, 30000):
                data = ternary_state_count_carry(n, root_exp)
                by_horizon.setdefault(data["horizon"], []).append(
                    (n, data["ternary_carry"])
                )
            for samples in by_horizon.values():
                carries = [carry for _, carry in samples]
                self.assertEqual(carries, sorted(carries))
                for n, carry in samples:
                    data = ternary_state_count_carry(n, root_exp)
                    if carry == 0:
                        self.assertLess(n, data["lower_threshold"])
                    elif carry == 1:
                        self.assertGreaterEqual(n, data["lower_threshold"])
                        self.assertLess(n, data["upper_threshold"])
                    else:
                        self.assertGreaterEqual(n, data["upper_threshold"])

    def test_all_three_carries_have_explicit_examples(self):
        examples = {
            0: (5, 2),
            1: (18, 2),
            2: (32, 2),
        }
        for carry, (n, root_exp) in examples.items():
            data = ternary_state_count_carry(n, root_exp)
            self.assertEqual(data["ternary_carry"], carry)

        for root_exp in range(2, 10):
            n = root_exp**root_exp
            data = ternary_state_count_carry(n, root_exp)
            self.assertEqual(data["horizon"], root_exp - 1)
            self.assertEqual(data["horizon_quotient"], 0)
            self.assertEqual(data["ternary_carry"], 2)

    def test_known_missing_and_present_boundary_bits(self):
        missing = horizon_state_carry(16, 2)
        self.assertEqual(missing["horizon"], 3)
        self.assertEqual(missing["high_denominator_max"], 1)
        self.assertEqual(missing["remainder"], 0)
        self.assertEqual(missing["raw_carry_threshold"], 2)
        self.assertFalse(missing["horizon_carry"])
        self.assertEqual(missing["distinct_root_count"], 3)

        present = horizon_state_carry(18, 2)
        self.assertEqual(present["horizon"], 3)
        self.assertEqual(present["high_denominator_max"], 1)
        self.assertEqual(present["remainder"], 2)
        self.assertEqual(present["raw_carry_threshold"], 2)
        self.assertTrue(present["horizon_carry"])
        self.assertEqual(present["distinct_root_count"], 4)

    def test_effective_threshold_handles_automatic_carry(self):
        found = False
        for root_exp in range(2, 8):
            for n in range(2, 5000):
                data = horizon_state_carry(n, root_exp)
                if data["horizon"] and data["raw_carry_threshold"] <= 0:
                    self.assertEqual(data["effective_carry_threshold"], 0)
                    self.assertTrue(data["horizon_carry"])
                    found = True
                    break
            if found:
                break
        self.assertTrue(found)

    def test_large_integer_only_carry(self):
        for root_exp in (1, 2, 3, 5, 8, 12):
            binary = horizon_state_carry(10**200 + 123456789, root_exp)
            ternary = ternary_state_count_carry(10**200 + 123456789, root_exp)
            self.assertGreaterEqual(binary["remainder"], 0)
            self.assertLess(binary["remainder"], binary["next_root_power"])
            self.assertIn(binary["horizon_carry"], (False, True))
            self.assertIn(ternary["ternary_carry"], (0, 1, 2))
            self.assertEqual(
                binary["distinct_root_count"], ternary["distinct_root_count"]
            )

    def test_validation(self):
        with self.assertRaises(ValueError):
            horizon_state_carry(0, 2)
        with self.assertRaises(ValueError):
            horizon_state_carry(10, 0)
        with self.assertRaises(ValueError):
            ternary_state_count_carry(0, 2)
        with self.assertRaises(ValueError):
            ternary_state_count_carry(10, 0)


if __name__ == "__main__":
    unittest.main()
