import unittest

from enterprise_math.graded_precision import (
    degree_detail,
    degree_project,
    degree_recompose,
    degree_transport,
    graded_product_transport,
    graded_sum_transport,
    monomial_precision_defect,
    monomial_recovery_profile,
    multiplication_precision_carry,
    power_precision_carry,
    reconstruct_from_precision_shells_degree,
    root_collapse_is_power_carry,
    transported_precision_shell_degree,
)


class GradedPrecisionTests(unittest.TestCase):
    def test_degree_q_fiber_decomposition(self):
        for degree in range(0, 6):
            for coarse in range(1, 7):
                for ratio in range(1, 7):
                    fine = coarse * ratio
                    modulus = ratio**degree
                    for value in range(0, 100):
                        projected = degree_project(value, coarse, fine, degree)
                        detail = degree_detail(value, coarse, fine, degree)
                        self.assertLess(detail, modulus)
                        self.assertEqual(
                            degree_recompose(
                                projected, detail, coarse, fine, degree
                            ),
                            value,
                        )

    def test_graded_transport_respects_sum_and_product(self):
        for coarse in range(1, 6):
            for ratio in range(1, 6):
                fine = coarse * ratio
                for left_degree in range(0, 4):
                    for right_degree in range(0, 4):
                        for left in range(0, 12):
                            for right in range(0, 12):
                                self.assertEqual(
                                    graded_product_transport(
                                        left,
                                        right,
                                        coarse,
                                        fine,
                                        left_degree,
                                        right_degree,
                                    ),
                                    degree_transport(
                                        left * right,
                                        coarse,
                                        fine,
                                        left_degree + right_degree,
                                    ),
                                )
                                if left_degree == right_degree:
                                    self.assertEqual(
                                        graded_sum_transport(
                                            left,
                                            right,
                                            coarse,
                                            fine,
                                            left_degree,
                                        ),
                                        degree_transport(
                                            left + right,
                                            coarse,
                                            fine,
                                            left_degree,
                                        ),
                                    )

    def test_degree_q_mobius_shell_inverts(self):
        max_scale = 24
        for degree in range(0, 5):
            values = {
                d: d ** (degree + 1) + 2 * d + 3
                for d in range(1, max_scale + 1)
            }
            shells = {
                d: transported_precision_shell_degree(values, d, degree)
                for d in range(1, max_scale + 1)
            }
            for scale in range(1, max_scale + 1):
                self.assertEqual(
                    reconstruct_from_precision_shells_degree(
                        shells, scale, degree
                    ),
                    values[scale],
                )

    def test_degree_q_homogeneous_bulk_is_annihilated(self):
        for degree in range(0, 6):
            for coefficient in range(0, 8):
                values = {
                    d: coefficient * d**degree for d in range(1, 40)
                }
                self.assertEqual(
                    transported_precision_shell_degree(values, 1, degree),
                    coefficient,
                )
                for scale in range(2, 40):
                    self.assertEqual(
                        transported_precision_shell_degree(
                            values, scale, degree
                        ),
                        0,
                    )

    def test_monomial_defect_is_bounded_by_coarse_cell(self):
        exponent_sets = [[1], [2], [3], [1, 1], [2, 1], [1, 1, 1]]
        for exponents in exponent_sets:
            arity = len(exponents)
            for ratio in range(1, 6):
                coarse = 2
                fine = coarse * ratio
                for seed in range(0, 40):
                    fine_values = [
                        (seed * (i + 2) + i) % 30 for i in range(arity)
                    ]
                    data = monomial_precision_defect(
                        fine_values, exponents, coarse, fine
                    )
                    self.assertGreaterEqual(data["defect"], 0)
                    self.assertLessEqual(
                        data["defect"], data["defect_bound"]
                    )
                    degree = sum(exponents)
                    fine_monomial = 1
                    for value, exponent in zip(fine_values, exponents):
                        fine_monomial *= value**exponent
                    self.assertEqual(
                        fine_monomial,
                        ratio**degree * data["recovered"] + data["detail"],
                    )

    def test_multiplication_carry_formula_and_bound(self):
        for ratio in range(1, 10):
            coarse = 3
            fine = coarse * ratio
            for left in range(0, 50):
                for right in range(0, 50):
                    data = multiplication_precision_carry(
                        left, right, coarse, fine
                    )
                    self.assertGreaterEqual(data["carry"], 0)
                    self.assertLessEqual(
                        data["carry"], data["carry_bound"]
                    )
                    coarse_product = (
                        data["left_coarse"] * data["right_coarse"]
                    )
                    self.assertEqual(
                        left * right,
                        ratio**2 * (coarse_product + data["carry"])
                        + data["product_detail"],
                    )

    def test_power_carry_is_exact_basin_coordinate(self):
        for power in range(1, 6):
            for ratio in range(1, 8):
                coarse = 2
                fine = coarse * ratio
                for value in range(0, 80):
                    data = power_precision_carry(
                        value, power, coarse, fine
                    )
                    k = data["coarse_value"]
                    self.assertEqual(
                        data["carry_bound"],
                        (k + 1) ** power - k**power - 1,
                    )
                    self.assertGreaterEqual(data["carry"], 0)
                    self.assertLessEqual(
                        data["carry"], data["carry_bound"]
                    )

    def test_monomial_recovery_is_monotone(self):
        scale_chains = [
            [1, 2, 4, 8],
            [1, 3, 6, 30],
            [2, 6, 18, 54],
        ]
        exponent_sets = [[2], [1, 1], [2, 1], [1, 1, 1]]
        for scales in scale_chains:
            finest = scales[-1]
            for exponents in exponent_sets:
                values = [
                    finest * (i + 2) + 3 * i + 1
                    for i in range(len(exponents))
                ]
                profile = monomial_recovery_profile(
                    values, exponents, scales[0], scales
                )
                self.assertEqual(profile, sorted(profile))

    def test_stage1_collapse_defect_is_exact_power_carry(self):
        for n in range(0, 50):
            for power in range(1, 5):
                for coarse in range(1, 6):
                    for ratio in range(1, 7):
                        fine = coarse * ratio
                        data = root_collapse_is_power_carry(
                            n, power, coarse, fine
                        )
                        self.assertGreaterEqual(data["collapse_defect"], 0)
                        self.assertLessEqual(
                            data["collapse_defect"],
                            data["power_carry_bound"],
                        )

    def test_degree_matters_for_projection(self):
        # The same fine integer carries different coarse meaning depending on
        # the scale degree of the mathematical quantity.
        value = 35
        coarse = 1
        fine = 3
        self.assertEqual(degree_project(value, coarse, fine, 1), 11)
        self.assertEqual(degree_project(value, coarse, fine, 2), 3)
        self.assertEqual(degree_project(value, coarse, fine, 3), 1)


if __name__ == "__main__":
    unittest.main()
