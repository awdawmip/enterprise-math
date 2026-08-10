from enterprise_math.p022_barlow_defect_kernel_functional import (
    additive_A_depth,
    defect_kernel_factorization_theorem,
    defect_kernel_residuals,
    twin_source_signed_prime_weights,
)


def test_any_additive_prime_weight_functional_lies_in_the_defect_kernel() -> None:
    weights = ((2, 1), (3, -2), (5, 3), (7, -1), (11, 2), (13, -3))
    depths = (0,) + tuple(additive_A_depth(n, weights) for n in range(1, 9))
    assert defect_kernel_factorization_theorem(8, depths)
    assert all(value == 0 for _, value in defect_kernel_residuals(8, depths))


def test_mutating_one_composite_coordinate_breaks_factorization() -> None:
    weights = ((2, 1), (3, -2), (5, 3), (7, -1), (11, 2), (13, -3))
    depths = [0] + [additive_A_depth(n, weights) for n in range(1, 9)]
    depths[5] += 1  # 2*5-1=9 is composite, so this is a constrained coordinate.
    assert not defect_kernel_factorization_theorem(8, tuple(depths))
    assert (5, 1) in defect_kernel_residuals(8, tuple(depths))


def test_primitive_twin_source_forces_signed_neighbor_prime_weights() -> None:
    assert twin_source_signed_prime_weights(6, 1) == (1, -1)
    assert twin_source_signed_prime_weights(21, 3) == (3, -3)
