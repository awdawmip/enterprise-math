from enterprise_math.p022_barlow_prime_halving_flux import (
    edge_divergence_exponents,
    edge_flow_reconstructs_basis,
    flux_matches_direct_transfer,
    franel_transfer_valuation_flux,
    half_defect_flux_correction,
    half_defect_flux_matches_exact_valuation,
    half_defect_transfer_is_valuation_balanced,
    prime_halving_edge_multiplicities,
)


def test_edge_flow_reconstructs_canonical_basis_off_index_one() -> None:
    for value in range(2, 120):
        assert edge_flow_reconstructs_basis(value)

    assert prime_halving_edge_multiplicities(86) == ((3, 1), (11, 1), (43, 1))
    assert edge_divergence_exponents(86) == ((2, 1), (5, -1), (6, 1), (21, -1), (22, 1))


def test_flux_matches_direct_transfer_valuation() -> None:
    for value in (3, 5, 7, 10, 14, 22, 57, 74, 86):
        for prime in (3, 5, 7, 11, 13, 29, 173):
            assert flux_matches_direct_transfer(value, prime)

    # Psi(7)=173/14, so the 173-adic transfer valuation is exactly one.
    assert franel_transfer_valuation_flux(7, 173) == 1


def test_half_defect_flux_is_the_exact_correction() -> None:
    for prime in (23, 29, 47, 53, 71, 101, 149, 167, 173, 191, 197, 239, 269, 293):
        assert half_defect_flux_matches_exact_valuation(prime)
        assert half_defect_flux_correction(prime) == 0
        assert half_defect_transfer_is_valuation_balanced(prime)
