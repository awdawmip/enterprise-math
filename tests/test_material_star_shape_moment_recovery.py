import itertools
import unittest

from enterprise_math.material_star_shape_moment_recovery import (
    adaptive_moment_shape_signature,
    adaptive_shape_power_sums,
    elementary_symmetric_from_power_sums,
    fixed_shell_adaptive_moment_signature,
    monic_polynomial_from_power_sums,
    recover_shape_from_adaptive_power_sums,
)
from enterprise_math.material_star_shape_observables import (
    finite_difference_shape_alias,
    response_shape_histogram,
    response_shape_power_signature,
)


def partitions(total, maximum=None):
    if total == 0:
        yield ()
        return
    upper = total if maximum is None else min(total, maximum)
    for first in range(upper, 0, -1):
        for tail in partitions(total - first, first):
            yield (first,) + tail


class MaterialStarShapeMomentRecoveryTests(unittest.TestCase):
    def test_newton_reconstruction_recovers_every_partition_through_total_fifteen(self):
        checked = 0
        for total in range(1, 16):
            for shape in partitions(total):
                powers = adaptive_shape_power_sums(shape)
                self.assertEqual(
                    recover_shape_from_adaptive_power_sums(powers),
                    shape,
                )
                checked += 1
        self.assertGreater(checked, 600)

    def test_adaptive_signature_has_no_collisions_on_bounded_partition_space(self):
        for total in range(1, 18):
            signatures = {}
            for shape in partitions(total):
                signature = adaptive_moment_shape_signature(shape)
                key = (signature.active_count, signature.power_sums)
                self.assertNotIn(key, signatures)
                signatures[key] = shape
                self.assertEqual(
                    signature.exact_histogram,
                    response_shape_histogram(shape),
                )

    def test_shell_local_signature_can_drop_known_total_moment(self):
        for total in range(1, 18):
            signatures = {}
            for shape in partitions(total):
                signature = fixed_shell_adaptive_moment_signature(shape, total)
                self.assertNotIn(signature, signatures)
                signatures[signature] = shape

    def test_finite_difference_aliases_need_more_than_the_fixed_low_order_signature(self):
        for degree in range(1, 7):
            alias = finite_difference_shape_alias(degree)
            self.assertEqual(
                response_shape_power_signature(alias.left_shape, degree),
                response_shape_power_signature(alias.right_shape, degree),
            )
            left_exact = adaptive_moment_shape_signature(alias.left_shape)
            right_exact = adaptive_moment_shape_signature(alias.right_shape)
            self.assertNotEqual(
                (left_exact.active_count, left_exact.power_sums),
                (right_exact.active_count, right_exact.power_sums),
            )

    def test_newton_coefficients_match_direct_elementary_symmetric_values(self):
        shapes = (
            (4, 3, 1),
            (5, 4, 2, 2, 2),
            (7, 7, 4, 2, 2, 1),
            (3, 3, 3),
        )
        for shape in shapes:
            powers = adaptive_shape_power_sums(shape)
            elementary = elementary_symmetric_from_power_sums(powers)
            direct = [1]
            for degree in range(1, len(shape) + 1):
                total = 0
                for indices in itertools.combinations(range(len(shape)), degree):
                    product = 1
                    for index in indices:
                        product *= shape[index]
                    total += product
                direct.append(total)
            self.assertEqual(elementary, tuple(direct))

    def test_monic_polynomial_has_every_shape_part_with_correct_multiplicity(self):
        shape = (5, 5, 3, 2, 2)
        coefficients = monic_polynomial_from_power_sums(
            adaptive_shape_power_sums(shape)
        )

        def evaluate(value):
            result = 0
            for coefficient in coefficients:
                result = result * value + coefficient
            return result

        for root in set(shape):
            self.assertEqual(evaluate(root), 0)
        self.assertNotEqual(evaluate(1), 0)
        self.assertEqual(recover_shape_from_adaptive_power_sums(
            adaptive_shape_power_sums(shape)
        ), shape)

    def test_single_part_shell_signature_needs_no_extra_power_moments(self):
        self.assertEqual(fixed_shell_adaptive_moment_signature((9,), 9), (1, ()))
        self.assertEqual(recover_shape_from_adaptive_power_sums((9,)), (9,))

    def test_invalid_moment_and_shell_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            adaptive_shape_power_sums(())
        with self.assertRaises(ValueError):
            adaptive_shape_power_sums((1, 2))
        with self.assertRaises(ValueError):
            elementary_symmetric_from_power_sums(())
        with self.assertRaises(ValueError):
            elementary_symmetric_from_power_sums((2, 1))
        with self.assertRaises(ValueError):
            recover_shape_from_adaptive_power_sums((2, 1))
        with self.assertRaises(ValueError):
            fixed_shell_adaptive_moment_signature((2, 1), 4)
        with self.assertRaises(ValueError):
            fixed_shell_adaptive_moment_signature((2, 1), 0)


if __name__ == "__main__":
    unittest.main()
