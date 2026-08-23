from itertools import product
import unittest

from enterprise_math.idempotent_path_closure import (
    ImprovingCycleError,
    bellman_greatest_fixed_point,
    bellman_least_fixed_point,
    bellman_operator,
    capped_max_plus,
    enumerate_fixed_points,
    finite_kleene_closure,
    left_matrix_residual,
    matrix_power,
    path_value,
    right_matrix_residual,
    semiring_matvec,
    semiring_vecmat,
    validate_finite_idempotent_semiring,
)


class IdempotentPathClosureTests(unittest.TestCase):
    def test_min_plus_power_and_closure_with_witness(self):
        matrix = (
            (None, 2, 10),
            (None, None, 3),
            (None, None, None),
        )
        self.assertEqual(matrix_power(matrix, 2, "min")[0][2], 5)
        result = finite_kleene_closure(matrix, "min")
        self.assertEqual(result.closure[0][2], 5)
        witness = result.witness_path(0, 2)
        self.assertEqual(witness, (0, 1, 2))
        self.assertEqual(path_value(matrix, witness), 5)

    def test_max_plus_closure(self):
        matrix = (
            (None, 1, 2),
            (None, None, 4),
            (None, None, None),
        )
        result = finite_kleene_closure(matrix, "max")
        self.assertEqual(result.closure[0][2], 5)
        self.assertEqual(result.witness_path(0, 2), (0, 1, 2))

    def test_improving_cycles_are_explicit_obstructions(self):
        min_cycle = ((None, -2), (1, None))
        with self.assertRaises(ImprovingCycleError) as ctx:
            finite_kleene_closure(min_cycle, "min")
        self.assertEqual(ctx.exception.weight, -1)

        max_cycle = ((None, 3), (-1, None))
        with self.assertRaises(ImprovingCycleError) as ctx:
            finite_kleene_closure(max_cycle, "max")
        self.assertEqual(ctx.exception.weight, 2)

    def test_capped_max_plus_residual_galois_laws(self):
        semiring = capped_max_plus(6)
        validate_finite_idempotent_semiring(semiring)
        matrix = ((0, 1), (2, None))
        bound_right = (4, 5)
        residual = right_matrix_residual(semiring, matrix, bound_right)
        for state in product(semiring.elements, repeat=2):
            lhs = all(
                semiring.leq(value, cap)
                for value, cap in zip(
                    semiring_matvec(semiring, matrix, state), bound_right
                )
            )
            rhs = all(
                semiring.leq(value, cap)
                for value, cap in zip(state, residual)
            )
            self.assertEqual(lhs, rhs)

        bound_left = (5, 4)
        residual_left = left_matrix_residual(semiring, matrix, bound_left)
        for state in product(semiring.elements, repeat=2):
            lhs = all(
                semiring.leq(value, cap)
                for value, cap in zip(
                    semiring_vecmat(semiring, state, matrix), bound_left
                )
            )
            rhs = all(
                semiring.leq(value, cap)
                for value, cap in zip(state, residual_left)
            )
            self.assertEqual(lhs, rhs)

    def test_bellman_extremal_fixed_points(self):
        semiring = capped_max_plus(3)
        matrix = ((0, None), (None, 0))
        bias = (1, 1)
        least = bellman_least_fixed_point(semiring, matrix, bias)
        greatest = bellman_greatest_fixed_point(semiring, matrix, bias)
        fixed = enumerate_fixed_points(semiring, matrix, bias)
        self.assertEqual(least.value, (1, 1))
        self.assertEqual(greatest.value, (3, 3))
        self.assertIn(least.value, fixed)
        self.assertIn(greatest.value, fixed)
        self.assertEqual(
            bellman_operator(semiring, matrix, bias, least.value),
            least.value,
        )


if __name__ == "__main__":
    unittest.main()
