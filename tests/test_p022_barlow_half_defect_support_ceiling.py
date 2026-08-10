from enterprise_math.p022_barlow_half_defect_support_ceiling import (
    central_binomial_basis_support_ceiling,
    half_defect_low_support_ceiling,
    half_defect_support_respects_ceiling,
    largest_odd_prime_factor,
    rank_ceiling_is_automatic_safe,
    support_ceiling_profile,
)


def test_prime_factor_support_ceiling_examples() -> None:
    assert largest_odd_prime_factor(1) == 1
    assert largest_odd_prime_factor(16) == 1
    assert largest_odd_prime_factor(57) == 19
    assert largest_odd_prime_factor(86) == 43

    assert central_binomial_basis_support_ceiling(16) == 1
    assert central_binomial_basis_support_ceiling(57) == 10
    assert central_binomial_basis_support_ceiling(86) == 22


def test_half_defect_support_is_below_ceiling_plus_safe_neighbor() -> None:
    for prime in (23, 29, 47, 53, 71, 101, 149, 167, 173, 191, 197, 269, 293):
        assert half_defect_support_respects_ceiling(prime)


def test_rank_ceiling_certifies_many_nonprimitive_cases() -> None:
    # p=149 is nonprimitive at the midpoint: Z_p={50,74,98}.
    # The canonical A-support ceiling is only 19, so avoidance is automatic.
    assert support_ceiling_profile(149) == (74, 50, 19, True)
    assert rank_ceiling_is_automatic_safe(149)

    # p=239 is also nonprimitive, but r_p=94 lies above its sparse-tree ceiling.
    midpoint, rank, ceiling, safe = support_ceiling_profile(239)
    assert (midpoint, rank) == (119, 94)
    assert rank > ceiling
    assert safe


def test_rank_ceiling_is_only_sufficient_not_necessary() -> None:
    # p=173 has a very early zero at F_4, below the ceiling 22.  The rank test
    # therefore cannot decide support avoidance even though the actual support
    # tree is safe (handled by the stronger exact support oracle elsewhere).
    assert half_defect_low_support_ceiling(173) == 22
    midpoint, rank, ceiling, safe = support_ceiling_profile(173)
    assert (midpoint, rank, ceiling, safe) == (86, 4, 22, False)
