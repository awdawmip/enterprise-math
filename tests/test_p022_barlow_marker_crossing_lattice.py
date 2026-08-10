from enterprise_math.p022_barlow_marker_crossing_lattice import (
    boundary_zero_coefficients,
    crossing_lattice_certifies_nonzero,
    crossing_lattice_modulus,
    explicit_vanishing_control_marker,
    explicit_vanishing_control_midpoint_quotient,
    marker_congruence_residue,
)


def test_early_target_primes_have_zero_correction_lattice() -> None:
    for prime in (23, 29, 47, 53, 71, 101, 149, 167, 173, 191, 197, 239, 269, 293):
        assert boundary_zero_coefficients(prime) == ()
        assert crossing_lattice_modulus(prime) == 0
        assert crossing_lattice_certifies_nonzero(prime, 1)


def test_explicit_target_collision_has_even_crossing_lattice() -> None:
    assert boundary_zero_coefficients(369_581) == ((8, -2),)
    assert crossing_lattice_modulus(369_581) == 2
    assert marker_congruence_residue(369_581, 1) == (2, 1)
    assert crossing_lattice_certifies_nonzero(369_581, 1)


def test_outside_target_vanishing_example_has_no_lattice_protection() -> None:
    # p=157 is forced-midpoint and p-2=155 is composite, but p=1 mod 3.
    # The single crossing coefficient has gcd one, so the criterion is
    # correctly inconclusive; the exact recurrence/defect oracle confirms that
    # complete cancellation really happens.
    assert boundary_zero_coefficients(157) == ((16, -1),)
    assert crossing_lattice_modulus(157) == 1
    assert marker_congruence_residue(157, 1) == (1, 0)
    assert not crossing_lattice_certifies_nonzero(157, 1)
    assert explicit_vanishing_control_midpoint_quotient() == 111
    assert explicit_vanishing_control_marker() == 0


def test_lattice_certificate_is_sufficient_not_necessary() -> None:
    # If midpoint depth is divisible by the lattice modulus, the result is only
    # inconclusive; no vanishing assertion is made.
    assert not crossing_lattice_certifies_nonzero(369_581, 2)
