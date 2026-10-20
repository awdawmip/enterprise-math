from enterprise_math.p022_barlow_hahn_centered_transfer import (
    admissible_p022_boundary,
    centered_terminal_vector,
    centered_transfer_matches_hahn,
    hahn_diagonal_residue,
    transfer_product_determinant,
    zero_forced_local_ratios,
)


def test_fixed_transfer_matches_hahn_known_boundaries():
    for n in (1, 2, 3, 4, 5, 7, 8, 9, 25):
        assert centered_transfer_matches_hahn(n)


def test_known_unrestricted_hahn_zero_is_seen_by_transfer():
    n = 25
    prime = 6 * n - 1
    assert prime == 149
    assert hahn_diagonal_residue(n) == 0
    assert centered_terminal_vector(n)[0] == 0
    assert transfer_product_determinant(n) != 0


def test_admissible_small_boundaries_have_no_regression_zero():
    seen = 0
    for n in range(3, 501, 3):
        if not admissible_p022_boundary(n):
            continue
        seen += 1
        assert centered_transfer_matches_hahn(n)
        assert hahn_diagonal_residue(n) != 0
        assert transfer_product_determinant(n) != 0
    assert seen == 13


def test_zero_local_ratios_are_universal():
    for n in (3, 15, 18, 45):
        prime = 6 * n - 1
        back, cross, forward = zero_forced_local_ratios(n)
        assert back == 4 * pow(3, -1, prime) % prime
        assert cross == -3 * pow(8, -1, prime) % prime
        assert forward == 3 * pow(2, -1, prime) % prime
