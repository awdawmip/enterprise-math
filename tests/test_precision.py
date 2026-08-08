import unittest

from enterprise_math.precision import (
    addition_carry,
    coarse_order_status,
    collapse_refinement_defect,
    collapse_recovery_profile,
    precision_chain_decomposition,
    precision_detail,
    project_precision,
    projected_refined_collapse,
    reconstruct_from_precision_shells,
    recompose_precision,
    root_precision_detail,
    scale_collapse_state,
    scale_root_state,
    subtraction_borrow,
    transported_precision_shell,
)


class PrecisionCalculusTests(unittest.TestCase):
    def test_precision_fiber_decomposition_is_unique(self):
        for fine in range(1, 25):
            for coarse in range(1, fine + 1):
                if fine % coarse:
                    continue
                ratio = fine // coarse
                for value in range(0, 100):
                    coarse_value = project_precision(value, coarse, fine)
                    detail = precision_detail(value, coarse, fine)
                    self.assertLess(detail, ratio)
                    self.assertEqual(
                        recompose_precision(coarse_value, detail, coarse, fine),
                        value,
                    )

    def test_nested_detail_composition(self):
        for high in range(1, 31):
            for middle in range(1, high + 1):
                if high % middle:
                    continue
                for low in range(1, middle + 1):
                    if middle % low:
                        continue
                    s = high // middle
                    for value in range(0, 120):
                        middle_value = project_precision(value, middle, high)
                        low_middle = precision_detail(middle_value, low, middle)
                        middle_high = precision_detail(value, middle, high)
                        direct = precision_detail(value, low, high)
                        self.assertEqual(direct, s * low_middle + middle_high)

    def test_coarse_order_is_a_permanent_certificate(self):
        for fine in range(1, 20):
            for coarse in range(1, fine + 1):
                if fine % coarse:
                    continue
                for left in range(0, 45):
                    for right in range(0, 45):
                        status = coarse_order_status(left, right, coarse, fine)
                        if status < 0:
                            self.assertLess(left, right)
                        elif status > 0:
                            self.assertGreater(left, right)
                        else:
                            self.assertEqual(
                                project_precision(left, coarse, fine),
                                project_precision(right, coarse, fine),
                            )

    def test_equal_coarse_fiber_reduces_order_to_detail(self):
        for ratio in range(1, 12):
            coarse = 3
            fine = coarse * ratio
            for block in range(0, 8):
                for left_detail in range(ratio):
                    for right_detail in range(ratio):
                        left = ratio * block + left_detail
                        right = ratio * block + right_detail
                        self.assertEqual(left < right, left_detail < right_detail)
                        self.assertEqual(left == right, left_detail == right_detail)

    def test_addition_carry_is_binary_and_exact(self):
        for ratio in range(1, 12):
            coarse = 2
            fine = coarse * ratio
            for left in range(0, 50):
                for right in range(0, 50):
                    coarse_sum, carry, detail = addition_carry(
                        left, right, coarse, fine
                    )
                    self.assertIn(carry, (0, 1))
                    self.assertEqual(
                        project_precision(left + right, coarse, fine), coarse_sum
                    )
                    self.assertEqual(
                        precision_detail(left + right, coarse, fine), detail
                    )

    def test_subtraction_borrow_is_binary_and_exact(self):
        for ratio in range(1, 12):
            coarse = 2
            fine = coarse * ratio
            for left in range(0, 50):
                for right in range(0, left + 1):
                    coarse_difference, borrow, detail = subtraction_borrow(
                        left, right, coarse, fine
                    )
                    self.assertIn(borrow, (0, 1))
                    self.assertEqual(
                        project_precision(left - right, coarse, fine),
                        coarse_difference,
                    )
                    self.assertEqual(
                        precision_detail(left - right, coarse, fine), detail
                    )

    def test_precision_chain_telescopes(self):
        chains = [
            [1],
            [1, 2, 4, 8, 16],
            [1, 3, 6, 30],
            [2, 6, 18, 90],
            [5, 10, 20, 100],
        ]
        for scales in chains:
            finest = scales[-1]
            for value in range(0, 200):
                base, details = precision_chain_decomposition(value, scales)
                rebuilt = base * (finest // scales[0])
                for i, detail in enumerate(details, start=1):
                    rebuilt += (finest // scales[i]) * detail
                self.assertEqual(rebuilt, value)

    def test_transported_mobius_shell_inverts_exactly(self):
        max_scale = 30
        values = {d: d * d + 3 * d + 1 for d in range(1, max_scale + 1)}
        shells = {
            d: transported_precision_shell(values, d)
            for d in range(1, max_scale + 1)
        }
        for scale in range(1, max_scale + 1):
            self.assertEqual(
                reconstruct_from_precision_shells(shells, scale),
                values[scale],
            )

    def test_scale_linear_bulk_is_annihilated(self):
        for coefficient in range(0, 10):
            values = {d: coefficient * d for d in range(1, 50)}
            self.assertEqual(transported_precision_shell(values, 1), coefficient)
            for scale in range(2, 50):
                self.assertEqual(transported_precision_shell(values, scale), 0)

    def test_root_precision_detail_and_projection_compatibility(self):
        for n in range(0, 50):
            for power in range(1, 5):
                for coarse in range(1, 8):
                    for ratio in range(1, 8):
                        fine = coarse * ratio
                        coarse_root = scale_root_state(n, power, coarse)
                        fine_root = scale_root_state(n, power, fine)
                        detail = root_precision_detail(n, power, coarse, fine)
                        self.assertEqual(fine_root, ratio * coarse_root + detail)
                        self.assertLess(detail, ratio)
                        self.assertEqual(fine_root // ratio, coarse_root)

    def test_root_precision_shell_removes_coarse_bulk(self):
        n = 2
        power = 2
        max_scale = 36
        root_values = {
            d: scale_root_state(n, power, d) for d in range(1, max_scale + 1)
        }
        coarse_root = root_values[1]
        detail_values = {d: root_values[d] - d * coarse_root for d in root_values}
        for scale in range(2, max_scale + 1):
            self.assertEqual(
                transported_precision_shell(root_values, scale),
                transported_precision_shell(detail_values, scale),
            )

    def test_precision_shells_need_not_be_nonnegative(self):
        root_values = {d: scale_root_state(2, 2, d) for d in range(1, 13)}
        self.assertEqual(transported_precision_shell(root_values, 12), -3)

    def test_local_root_detail_need_not_grow_with_refinement(self):
        scales = [1, 2, 4, 8, 16]
        local_details = [
            root_precision_detail(2, 2, low, high)
            for low, high in zip(scales, scales[1:])
        ]
        self.assertEqual(local_details, [0, 1, 1, 0])

    def test_fine_collapse_does_not_commute_with_coarse_collapse(self):
        self.assertEqual(scale_collapse_state(3, 2, 1), 1)
        self.assertEqual(projected_refined_collapse(3, 2, 1, 10), 2)
        self.assertEqual(collapse_refinement_defect(3, 2, 1, 10), 1)

    def test_collapse_refinement_defect_is_a_coarse_basin_coordinate(self):
        for n in range(0, 40):
            for power in range(1, 5):
                for coarse in range(1, 7):
                    k = scale_root_state(n, power, coarse)
                    gap = (k + 1) ** power - k**power
                    for ratio in range(1, 7):
                        fine = coarse * ratio
                        defect = collapse_refinement_defect(
                            n, power, coarse, fine
                        )
                        self.assertGreaterEqual(defect, 0)
                        self.assertLess(defect, gap)

    def test_collapse_recovery_is_monotone_under_refinement(self):
        chains = [
            [1, 2, 4, 8, 16],
            [2, 6, 18, 54],
            [3, 6, 30, 60],
        ]
        for n in range(0, 40):
            for power in range(1, 5):
                for chain in chains:
                    profile = collapse_recovery_profile(
                        n, power, chain[0], chain
                    )
                    self.assertEqual(profile, sorted(profile))
                    coarse_collapse = scale_collapse_state(
                        n, power, chain[0]
                    )
                    self.assertEqual(profile[0], coarse_collapse)
                    self.assertLessEqual(profile[-1], n * chain[0] ** power)
                    increments = [
                        later - earlier
                        for earlier, later in zip(profile, profile[1:])
                    ]
                    self.assertTrue(all(increment >= 0 for increment in increments))
                    self.assertEqual(
                        sum(increments), profile[-1] - profile[0]
                    )


if __name__ == "__main__":
    unittest.main()
