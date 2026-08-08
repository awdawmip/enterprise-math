import unittest

from enterprise_math.precision_proof import (
    FALSE,
    TRUE,
    UNRESOLVED,
    equality_threshold_certificate,
    homogeneous_operation_defect,
    homogeneous_operation_recovery_profile,
    monotone_cell_bounds,
    monotone_threshold_certificate,
    order_cell_certificate,
    precision_cell,
    precision_cell_nesting,
    strict_less_threshold_certificate,
    threshold_certificate_profile,
    zero_defect_certificate,
)


def sum_operation(values):
    return sum(values)


def square_operation(values):
    return values[0] ** 2


def quadratic_form(values):
    x, y = values
    return x * x + x * y + y * y


def product_operation(values):
    result = 1
    for value in values:
        result *= value
    return result


class PrecisionProofTests(unittest.TestCase):
    def test_precision_cells_contain_state(self):
        for fine in range(1, 30):
            for coarse in range(1, fine + 1):
                if fine % coarse:
                    continue
                for value in range(0, 100):
                    cell = precision_cell(value, coarse, fine)
                    self.assertLessEqual(cell["lower"], value)
                    self.assertLessEqual(value, cell["upper"])
                    self.assertEqual(
                        cell["upper"] - cell["lower"] + 1,
                        fine // coarse,
                    )

    def test_refinement_cells_are_nested(self):
        for fine in range(1, 31):
            for middle in range(1, fine + 1):
                if fine % middle:
                    continue
                for coarse in range(1, middle + 1):
                    if middle % coarse:
                        continue
                    for value in range(0, 90):
                        data = precision_cell_nesting(
                            value, coarse, middle, fine
                        )
                        self.assertLessEqual(
                            data["coarse"]["lower"],
                            data["refined"]["lower"],
                        )
                        self.assertLessEqual(
                            data["refined"]["upper"],
                            data["coarse"]["upper"],
                        )

    def test_monotone_cell_bounds_enclose_operation(self):
        operations = [sum_operation, square_operation, quadratic_form, product_operation]
        sample_vectors = [[7], [11], [7, 13], [3, 5, 7]]
        for operation, values in zip(operations, sample_vectors):
            for coarse, fine in [(1, 10), (2, 10), (5, 20), (3, 30)]:
                data = monotone_cell_bounds(operation, values, coarse, fine)
                self.assertLessEqual(data["image_lower"], data["actual"])
                self.assertLessEqual(data["actual"], data["image_upper"])

    def test_threshold_certificate_trichotomy(self):
        self.assertEqual(strict_less_threshold_certificate(3, 7, 8), TRUE)
        self.assertEqual(strict_less_threshold_certificate(8, 12, 8), FALSE)
        self.assertEqual(
            strict_less_threshold_certificate(3, 9, 8), UNRESOLVED
        )
        self.assertEqual(equality_threshold_certificate(5, 5, 5), TRUE)
        self.assertEqual(equality_threshold_certificate(6, 8, 5), FALSE)
        self.assertEqual(equality_threshold_certificate(4, 7, 5), UNRESOLVED)

    def test_coarse_threshold_certificate_is_sound(self):
        for value in range(0, 80):
            for threshold in range(0, 80):
                for coarse, fine in [(1, 10), (2, 10), (5, 20)]:
                    data = monotone_threshold_certificate(
                        square_operation, [value], coarse, fine, threshold
                    )
                    cell = precision_cell(value, coarse, fine)
                    truths = [x * x < threshold for x in range(cell["lower"], cell["upper"] + 1)]
                    if data["certificate"] == TRUE:
                        self.assertTrue(all(truths))
                    elif data["certificate"] == FALSE:
                        self.assertFalse(any(truths))

    def test_certificate_persists_under_refinement(self):
        scales = [1, 2, 4, 8, 16]
        for value in range(0, 100):
            finest_value = value
            for threshold in range(0, 140):
                statuses = threshold_certificate_profile(
                    square_operation, [finest_value], threshold, scales
                )
                decided = None
                for status in statuses:
                    if decided is not None:
                        self.assertEqual(status, decided)
                    elif status != UNRESOLVED:
                        decided = status

    def test_order_certificate_recovers_stage1_order_rule(self):
        for ratio in range(1, 12):
            coarse = 1
            fine = ratio
            for left in range(0, 50):
                for right in range(0, 50):
                    status = order_cell_certificate(left, right, coarse, fine)
                    left_block = left // ratio
                    right_block = right // ratio
                    if left_block < right_block:
                        self.assertEqual(status, TRUE)
                        self.assertLess(left, right)
                    elif left_block > right_block:
                        self.assertEqual(status, FALSE)
                        self.assertGreater(left, right)
                    else:
                        if ratio > 1:
                            self.assertEqual(status, UNRESOLVED)

    def test_homogeneous_operation_defect_for_quadratic_form(self):
        for ratio in range(1, 8):
            coarse = 2
            fine = coarse * ratio
            for x in range(0, 40):
                for y in range(0, 40):
                    data = homogeneous_operation_defect(
                        quadratic_form, [x, y], coarse, fine, 2
                    )
                    self.assertGreaterEqual(data["defect"], 0)
                    self.assertLessEqual(
                        data["defect"], data["defect_bound"]
                    )
                    self.assertEqual(
                        quadratic_form([x, y]),
                        ratio**2 * data["recovered"] + data["output_detail"],
                    )

    def test_zero_defect_certificate_is_exact(self):
        for ratio in range(1, 10):
            coarse = 1
            fine = ratio
            for x in range(0, 50):
                for y in range(0, 50):
                    no_crossing = zero_defect_certificate(
                        quadratic_form, [x, y], coarse, fine, 2
                    )
                    data = homogeneous_operation_defect(
                        quadratic_form, [x, y], coarse, fine, 2
                    )
                    self.assertEqual(no_crossing, data["defect"] == 0)

    def test_homogeneous_operation_recovery_is_monotone(self):
        chains = [[1, 2, 4, 8], [1, 3, 6, 30], [2, 6, 18, 54]]
        operations = [(square_operation, 2, 1), (quadratic_form, 2, 2), (product_operation, 3, 3)]
        for scales in chains:
            finest = scales[-1]
            for operation, degree, arity in operations:
                values = [finest * (i + 2) + 7 * i + 1 for i in range(arity)]
                profile = homogeneous_operation_recovery_profile(
                    operation, values, degree, scales[0], scales
                )
                self.assertEqual(profile, sorted(profile))

    def test_nonhomogeneous_map_is_rejected_by_defect_contract_when_detected(self):
        def shifted_square(values):
            return values[0] ** 2 + 1

        with self.assertRaises(ValueError):
            homogeneous_operation_defect(
                shifted_square, [19], 1, 10, 2
            )


if __name__ == "__main__":
    unittest.main()
