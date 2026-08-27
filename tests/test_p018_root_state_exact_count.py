import unittest

from enterprise_math.p018_root_state_decomposition import (
    exact_distinct_root_state_count,
    horizon_fiber_present,
    naive_positive_quotient_root_states,
    quotient_root_state_decomposition,
    state_coalescence_horizon,
)
from enterprise_math.p018_power_coalescence import exact_root_fiber_capacity


class P018RootStateExactCountTests(unittest.TestCase):
    def test_closed_count_matches_naive_exhaustively(self):
        saw_missing_horizon = False
        saw_present_horizon = False
        for root_exp in range(1, 7):
            for n in range(1, 5000):
                closed = exact_distinct_root_state_count(n, root_exp)
                naive = naive_positive_quotient_root_states(n, root_exp)
                self.assertEqual(closed["distinct_root_count"], len(naive))
                h = closed["horizon"]
                d = closed["high_denominator_max"]
                if h == 0:
                    self.assertEqual(len(naive), d)
                    continue
                self.assertIn(len(naive), (d + h - 1, d + h))
                if closed["horizon_fiber_present"]:
                    self.assertEqual(len(naive), d + h)
                    saw_present_horizon = True
                else:
                    self.assertEqual(len(naive), d + h - 1)
                    saw_missing_horizon = True
        self.assertTrue(saw_present_horizon)
        self.assertTrue(saw_missing_horizon)

    def test_every_low_root_below_horizon_is_forced_nonempty(self):
        for root_exp in range(1, 7):
            for n in range(1, 10000):
                h = state_coalescence_horizon(n, root_exp)
                for target in range(1, h):
                    self.assertGreater(
                        exact_root_fiber_capacity(n, root_exp, target), 0
                    )

    def test_minimal_missing_horizon_example(self):
        # r=2,n=16: H=3. Roots 1,2 are forced; root 3 is absent because
        # floor(16/9)=floor(16/16)=1. The high singleton branch contributes 4.
        closed = exact_distinct_root_state_count(16, 2)
        self.assertEqual(closed["horizon"], 3)
        self.assertEqual(closed["high_denominator_max"], 1)
        self.assertFalse(closed["horizon_fiber_present"])
        self.assertFalse(horizon_fiber_present(16, 2))
        data = quotient_root_state_decomposition(16, 2)
        self.assertEqual(data["low_roots"], (1, 2))
        self.assertEqual(data["high_roots"], (4,))
        self.assertEqual(data["distinct_root_count"], 3)
        self.assertEqual(data["distinct_roots"], (1, 2, 4))

    def test_r1_recovers_exact_classical_floor_quotient_counts(self):
        expected = {
            1: 1,
            2: 2,
            5: 3,
            10: 5,
            25: 9,
            26: 9,
            100: 19,
        }
        for n, count in expected.items():
            closed = exact_distinct_root_state_count(n, 1)
            self.assertEqual(closed["distinct_root_count"], count)

    def test_large_closed_count_uses_no_denominator_scan(self):
        for root_exp in (1, 2, 3, 5, 8):
            closed = exact_distinct_root_state_count(10**100, root_exp)
            h = closed["horizon"]
            d = closed["high_denominator_max"]
            self.assertIn(
                closed["distinct_root_count"],
                (d + h - 1, d + h) if h else (d,),
            )
            self.assertLess(closed["distinct_root_count"], 10**51)


if __name__ == "__main__":
    unittest.main()
