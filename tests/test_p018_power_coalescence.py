import unittest

from enterprise_math.p018_power_coalescence import (
    coalescence_phase,
    coalescence_root_constant,
    coarse_sublinear_descent_threshold,
    cross_root_coalescence_horizon,
    cross_root_divisor_collision,
    power_basin_cross_root,
    same_exponent_coalescence_horizon,
    sharp_adjacent_collision_family,
    verify_coarse_sublinear_descent,
)


class P018PowerCoalescenceTests(unittest.TestCase):
    def test_root_order_constants_are_sharp_candidates(self):
        self.assertEqual(
            [coalescence_root_constant(r) for r in range(1, 7)],
            [1, 2, 3, 4, 5, 6],
        )

    def test_exhaustive_small_cross_root_collisions(self):
        saw = False
        phases = set()
        for source_exp in range(1, 5):
            for root_exp in range(1, 6):
                phases.add(coalescence_phase(source_exp, root_exp))
                for k in range(1, 7):
                    start = k**source_exp
                    stop = (k + 1) ** source_exp
                    for n in range(start, stop):
                        divisors = range(2, min(n + 1, 18))
                        roots = {
                            d: power_basin_cross_root(
                                k, n, source_exp, root_exp, d
                            )
                            for d in divisors
                        }
                        for d in divisors:
                            for e in range(d + 1, min(n + 1, 18)):
                                if roots[d] != roots[e]:
                                    continue
                                data = cross_root_divisor_collision(
                                    k, n, source_exp, root_exp, d, e
                                )
                                self.assertTrue(data["coalesces"])
                                t = data["common_root"]
                                self.assertEqual(
                                    data["root_order_constant"], root_exp
                                )
                                self.assertLess(
                                    t + 1,
                                    root_exp * (d + 1),
                                )
                                self.assertLess(
                                    t ** (root_exp + 1),
                                    root_exp * (k + 1) ** source_exp,
                                )
                                self.assertLessEqual(
                                    t, data["coalescence_horizon"]
                                )
                                saw = True
        self.assertTrue(saw)
        self.assertEqual(
            phases,
            {"sublinear", "linear-boundary", "superlinear-bound"},
        )

    def test_square_collision_is_exact_general_specialization(self):
        # The p=r=2 theorem now reproduces the sharp square constant 2 rather
        # than the earlier coarse binomial constant 3.
        data = cross_root_divisor_collision(97, 9464, 2, 2, 13, 14)
        self.assertTrue(data["coalesces"])
        self.assertEqual(data["common_root"], 26)
        self.assertEqual(data["root_order_constant"], 2)
        self.assertLess(26**3, 2 * 98**2)
        self.assertLessEqual(26, same_exponent_coalescence_horizon(97, 2))

    def test_explicit_sharp_family_for_many_cross_exponents(self):
        for source_exp in range(1, 6):
            for root_exp in range(1, 7):
                previous_ratio = -1.0
                for m in (2, 3, 5, 10, 30, 100):
                    witness = sharp_adjacent_collision_family(
                        source_exp, root_exp, m
                    )
                    data = cross_root_divisor_collision(
                        witness["k"],
                        witness["n"],
                        source_exp,
                        root_exp,
                        witness["left"],
                        witness["right"],
                    )
                    self.assertTrue(data["coalesces"])
                    self.assertEqual(
                        data["common_root"], witness["common_root"]
                    )
                    ratio = (
                        witness["sharp_ratio_numerator"]
                        / witness["sharp_ratio_denominator"]
                    )
                    self.assertGreater(ratio, previous_ratio)
                    self.assertLess(ratio, 1.0)
                    previous_ratio = ratio
                self.assertGreater(previous_ratio, 0.98)

    def test_same_exponent_family_is_always_sublinear(self):
        for exponent in range(1, 8):
            self.assertEqual(coalescence_phase(exponent, exponent), "sublinear")
            threshold = coarse_sublinear_descent_threshold(exponent, exponent)
            for k in (threshold, threshold + 1, 2 * threshold + 3):
                data = verify_coarse_sublinear_descent(k, exponent, exponent)
                self.assertLess(data["horizon"], k)
                self.assertEqual(data["phase"], "sublinear")

    def test_cross_exponent_phase_boundary(self):
        self.assertEqual(coalescence_phase(4, 4), "sublinear")
        self.assertEqual(coalescence_phase(4, 3), "linear-boundary")
        self.assertEqual(coalescence_phase(4, 2), "superlinear-bound")
        self.assertEqual(coalescence_phase(2, 5), "sublinear")

    def test_coarse_threshold_is_sufficient_on_grid(self):
        for source_exp in range(1, 5):
            for root_exp in range(1, 6):
                if root_exp + 1 <= source_exp:
                    continue
                threshold = coarse_sublinear_descent_threshold(
                    source_exp, root_exp
                )
                for k in range(threshold, threshold + 25):
                    data = verify_coarse_sublinear_descent(
                        k, source_exp, root_exp
                    )
                    self.assertLess(data["horizon"], k)

    def test_horizon_argument_is_exact_integer_ceiling(self):
        for source_exp, root_exp, k in (
            (1, 1, 20),
            (2, 2, 97),
            (3, 3, 50),
            (2, 4, 30),
            (4, 5, 300),
        ):
            horizon = cross_root_coalescence_horizon(k, source_exp, root_exp)
            argument = root_exp * (k + 1) ** source_exp - 1
            self.assertLessEqual(horizon ** (root_exp + 1), argument)
            self.assertGreater((horizon + 1) ** (root_exp + 1), argument)

    def test_validation(self):
        with self.assertRaises(ValueError):
            coalescence_root_constant(0)
        with self.assertRaises(ValueError):
            cross_root_coalescence_horizon(0, 2, 2)
        with self.assertRaises(ValueError):
            power_basin_cross_root(3, 8, 2, 2, 2)
        with self.assertRaises(ValueError):
            cross_root_divisor_collision(3, 9, 2, 2, 3, 3)
        with self.assertRaises(ValueError):
            sharp_adjacent_collision_family(2, 2, 1)
        with self.assertRaises(ValueError):
            coarse_sublinear_descent_threshold(4, 3)


if __name__ == "__main__":
    unittest.main()
