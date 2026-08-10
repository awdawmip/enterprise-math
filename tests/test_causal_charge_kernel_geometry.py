import unittest
from itertools import product

from enterprise_math.causal_charge_kernel_geometry import (
    a_kernel_basis,
    a_relation_rank,
    classify_total_conservation,
    d_kernel_basis,
    d_primitive_pair_moves,
    d_relation_rank,
    in_a_kernel,
    in_d_kernel,
    in_scaled_e8_charge_kernel,
    scaled_e8_charge_constraints,
    scaled_e8_relation_rank,
)
from enterprise_math.causal_primitive_link_profile import (
    a_roots,
    d_roots,
    e6_scaled_roots,
    e7_scaled_roots,
    e8_scaled_roots,
)


def _bareiss_det(matrix):
    values = [list(row) for row in matrix]
    n = len(values)
    if n == 0:
        return 1
    sign = 1
    previous = 1
    for pivot_index in range(n - 1):
        if values[pivot_index][pivot_index] == 0:
            swap = next(
                (row for row in range(pivot_index + 1, n) if values[row][pivot_index] != 0),
                None,
            )
            if swap is None:
                return 0
            values[pivot_index], values[swap] = values[swap], values[pivot_index]
            sign *= -1
        pivot = values[pivot_index][pivot_index]
        for row in range(pivot_index + 1, n):
            for column in range(pivot_index + 1, n):
                numerator = values[row][column] * pivot - values[row][pivot_index] * values[pivot_index][column]
                if numerator % previous != 0:
                    raise AssertionError("Bareiss division must be exact")
                values[row][column] = numerator // previous
        previous = pivot
    return sign * values[-1][-1]


class CausalChargeKernelGeometryTests(unittest.TestCase):
    def test_a_is_exact_total_charge_kernel_and_loses_one_free_rank(self):
        for p in range(1, 7):
            roots = a_roots(p)
            self.assertTrue(all(in_a_kernel(root) for root in roots))
            self.assertEqual(a_relation_rank(p + 1), p)
            self.assertEqual(len(a_kernel_basis(p + 1)), p)
            self.assertTrue(all(classify_total_conservation(root) == (0, 0) for root in roots))

    def test_d_is_parity_kernel_and_keeps_full_integer_rank(self):
        for rank in range(3, 8):
            roots = d_roots(rank)
            self.assertEqual(set(roots), set(d_primitive_pair_moves(rank)))
            self.assertTrue(all(in_d_kernel(root) for root in roots))
            self.assertTrue(any(not in_a_kernel(root) for root in roots))
            self.assertEqual(d_relation_rank(rank), rank)
            basis = d_kernel_basis(rank)
            self.assertEqual(len(basis), rank)
            matrix = tuple(tuple(basis[column][row] for column in range(rank)) for row in range(rank))
            self.assertEqual(abs(_bareiss_det(matrix)), 2)
            self.assertEqual(
                {classify_total_conservation(root)[0] for root in roots},
                {-2, 0, 2},
            )
            self.assertEqual(
                {classify_total_conservation(root)[1] for root in roots},
                {0},
            )

    def test_scaled_e8_is_full_rank_but_has_stronger_finite_charge_code(self):
        roots = e8_scaled_roots()
        self.assertEqual(len(roots), 240)
        self.assertTrue(all(in_scaled_e8_charge_kernel(root) for root in roots))
        self.assertEqual(scaled_e8_relation_rank(), 8)
        self.assertEqual(
            {scaled_e8_charge_constraints(root) for root in roots},
            {(True, True)},
        )
        # The defining congruence classes have index 256 in Z^8: among 4^8
        # residue words mod 4, exactly 256 satisfy same-parity + total mod 4=0.
        valid = 0
        for vector in product(range(4), repeat=8):
            if in_scaled_e8_charge_kernel(vector):
                valid += 1
        self.assertEqual(valid, 256)
        self.assertEqual(4 ** 8 // valid, 256)

    def test_e7_and_e6_add_exact_linear_charge_constraints_to_e8_code(self):
        ones = (1,) * 8
        selector = (1, 1, 1, 1, 1, 1, -3, -3)
        e7 = e7_scaled_roots()
        e6 = e6_scaled_roots()
        self.assertTrue(all(in_scaled_e8_charge_kernel(root) for root in e7))
        self.assertTrue(all(sum(a * b for a, b in zip(root, ones)) == 0 for root in e7))
        self.assertTrue(all(in_scaled_e8_charge_kernel(root) for root in e6))
        self.assertTrue(all(sum(a * b for a, b in zip(root, ones)) == 0 for root in e6))
        self.assertTrue(all(sum(a * b for a, b in zip(root, selector)) == 0 for root in e6))

    def test_modular_charge_restricts_index_without_reducing_rational_rank(self):
        for rank in range(2, 7):
            basis = d_kernel_basis(rank)
            matrix = tuple(tuple(basis[column][row] for column in range(rank)) for row in range(rank))
            self.assertNotEqual(_bareiss_det(matrix), 0)
            self.assertEqual(d_relation_rank(rank), rank)


if __name__ == "__main__":
    unittest.main()
