import unittest

from enterprise_math.core import integer_nth_root
from enterprise_math.p018_power_coalescence import (
    coalescence_multiplicity_cap,
    coalescence_phase,
    coalescence_root_constant,
    coarse_sublinear_descent_threshold,
    cross_root_coalescence_horizon,
    cross_root_divisor_collision,
    exact_root_fiber_capacity,
    observed_root_divisor_multiplicity,
    power_basin_cross_root,
    same_exponent_coalescence_horizon,
    sharp_adjacent_collision_family,
    sharp_consecutive_collision_block,
    total_divisor_root_fiber,
    verify_coarse_sublinear_descent,
)


class P018PowerCoalescenceTests(unittest.TestCase):
    def test_root_order_constants_are_sharp_candidates(self):
        self.assertEqual(
            [coalescence_root_constant(r) for r in range(1, 7)],
            [1, 2, 3, 4, 5, 6],
        )

    def test_exact_total_divisor_root_fibers(self):
        for root_exp in range(1, 6):
            for n in range(1, 180):
                max_root = integer_nth_root(n, root_exp) + 2
                for target in range(1, max_root + 1):
                    data = total_divisor_root_fiber(n, root_exp, target)
                    labels = data["positive_divisor_labels"]
                    expected = tuple(
                        d
                        for d in range(1, n + 2)
                        if integer_nth_root(n // d, root_exp) == target
                    )
                    self.assertEqual(labels, expected)
                    self.assertEqual(
                        data["positive_capacity"],
                        exact_root_fiber_capacity(n, root_exp, target),
                    )
                    self.assertEqual(
                        data["positive_capacity"],
                        data["upper_inclusive"] - data["lower_exclusive"],
                    )

    def test_exhaustive_small_cross_root_collisions(self):
        saw = False
        saw_gap = False
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
                                gap = e - d
                                self.assertEqual(
                                    data["root_order_constant"], root_exp
                                )
                                self.assertLess(
                                    gap * (t + 1),
                                    root_exp * e,
                                )
                                if t > 0:
                                    self.assertLess(
                                        gap * t ** (root_exp + 1),
                                        root_exp * (k + 1) ** source_exp,
                                    )
                                saw_gap |= gap > 1
                                saw = True
        self.assertTrue(saw)
        self.assertTrue(saw_gap)
        self.assertEqual(
            phases,
            {"sublinear", "linear-boundary", "superlinear-bound"},
        )

    def test_square_collision_is_exact_general_specialization(self):
        data = cross_root_divisor_collision(97, 9464, 2, 2, 13, 14)
        self.assertTrue(data["coalesces"])
        self.assertEqual(data["common_root"], 26)
        self.assertEqual(data["root_order_constant"], 2)
        self.assertEqual(data["divisor_gap"], 1)
        self.assertLess(26**3, 2 * 98**2)
        self.assertLessEqual(26, same_exponent_coalescence_horizon(97, 2))

    def test_explicit_sharp_adjacent_family_for_many_cross_exponents(self):
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

    def test_sharp_consecutive_blocks_realize_all_multiplicity_scales(self):
        for source_exp in (1, 2, 3, 5):
            for root_exp in (1, 2, 3, 5):
                for gap in (1, 2, 3, 5, 8):
                    previous_ratio = -1.0
                    for parameter in (2, 5, 20, 100):
                        block = sharp_consecutive_collision_block(
                            source_exp, root_exp, gap, parameter
                        )
                        self.assertEqual(block["multiplicity"], gap + 1)
                        self.assertEqual(
                            block["divisor_hits"],
                            tuple(range(block["left"], block["right"] + 1)),
                        )
                        exact = total_divisor_root_fiber(
                            block["n"], root_exp, block["common_root"]
                        )
                        self.assertTrue(
                            set(block["divisor_hits"]).issubset(
                                exact["positive_divisor_labels"]
                            )
                        )
                        self.assertLessEqual(
                            block["multiplicity"], block["multiplicity_cap"]
                        )
                        ratio = (
                            block["weighted_ratio_numerator"]
                            / block["weighted_ratio_denominator"]
                        )
                        self.assertGreater(ratio, previous_ratio)
                        self.assertLess(ratio, 1.0)
                        previous_ratio = ratio
                    self.assertGreater(previous_ratio, 0.98)

    def test_multiplicity_cap_matches_direct_enumeration(self):
        saw_multiple = False
        for source_exp in (1, 2, 3):
            for root_exp in (1, 2, 3, 4):
                for k in range(2, 10):
                    for n in range(k**source_exp, (k + 1) ** source_exp):
                        max_divisor = min(max(3, 2 * (k + 1) ** source_exp), 120)
                        root_groups: dict[int, list[int]] = {}
                        for divisor in range(2, max_divisor + 1):
                            root = power_basin_cross_root(
                                k, n, source_exp, root_exp, divisor
                            )
                            if root <= 0:
                                continue
                            root_groups.setdefault(root, []).append(divisor)
                        for target, hits in root_groups.items():
                            audited = observed_root_divisor_multiplicity(
                                k,
                                n,
                                source_exp,
                                root_exp,
                                target,
                                max_divisor,
                            )
                            cap = coalescence_multiplicity_cap(
                                k, source_exp, root_exp, target
                            )
                            self.assertIsNotNone(cap)
                            self.assertEqual(audited["divisor_hits"], tuple(hits))
                            self.assertLessEqual(len(hits), cap)
                            saw_multiple |= len(hits) >= 2
        self.assertTrue(saw_multiple)

    def test_multiplicity_cap_is_hierarchical(self):
        for k in (10, 30, 100, 1000):
            for source_exp in (1, 2, 3):
                for root_exp in (1, 2, 4):
                    previous = None
                    horizon = cross_root_coalescence_horizon(
                        k, source_exp, root_exp
                    )
                    for target in range(1, max(2, 2 * horizon + 4)):
                        cap = coalescence_multiplicity_cap(
                            k, source_exp, root_exp, target
                        )
                        self.assertIsNotNone(cap)
                        if previous is not None:
                            self.assertLessEqual(cap, previous)
                        previous = cap
                        if target > horizon:
                            self.assertEqual(cap, 1)

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

    def test_zero_root_has_no_finite_cap_from_this_law(self):
        self.assertIsNone(coalescence_multiplicity_cap(10, 2, 2, 0))

    def test_validation(self):
        with self.assertRaises(ValueError):
            coalescence_root_constant(0)
        with self.assertRaises(ValueError):
            total_divisor_root_fiber(10, 0, 1)
        with self.assertRaises(ValueError):
            total_divisor_root_fiber(10, 2, 0)
        with self.assertRaises(ValueError):
            cross_root_coalescence_horizon(0, 2, 2)
        with self.assertRaises(ValueError):
            power_basin_cross_root(3, 8, 2, 2, 2)
        with self.assertRaises(ValueError):
            cross_root_divisor_collision(3, 9, 2, 2, 3, 3)
        with self.assertRaises(ValueError):
            sharp_adjacent_collision_family(2, 2, 1)
        with self.assertRaises(ValueError):
            sharp_consecutive_collision_block(2, 2, 0, 3)
        with self.assertRaises(ValueError):
            coarse_sublinear_descent_threshold(4, 3)


if __name__ == "__main__":
    unittest.main()
