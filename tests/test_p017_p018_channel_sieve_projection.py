from enterprise_math.p017_p018_channel_sieve_projection import (
    mobius_channel_sieve_projection,
    ramanujan_channel_projection,
    same_size_only_future_class,
    singleton_divisor_future,
    size_only_future_signature,
    square_basin_quadratic_diagonal,
)


def test_mobius_descendant_transform_is_exact_rough_interval_count():
    for fiber_size, first_quotient, primes in (
        (10, 101, (3, 5, 7)),
        (7, 55, (3, 5)),
        (13, 211, (3, 7, 11)),
    ):
        data = mobius_channel_sieve_projection(fiber_size, first_quotient, primes)
        assert data["exact_roughness_projection"] is True
        assert data["mobius_descendant_sum"] == data["rough_progression_count"]
        assert data["rough_progression_count"] == data["consecutive_rough_interval_count"]


def test_cut_signature_is_strictly_coarser_than_full_lcm_residue_state():
    refinements = (3, 5, 7)
    a = size_only_future_signature(11, 1, refinements)
    b = size_only_future_signature(11, 19, refinements)

    assert a["cut_signature"] == b["cut_signature"] == (0, 0, 0)
    assert a["child_sizes"] == b["child_sizes"]
    assert a["lcm_modulus"] == b["lcm_modulus"] == 105
    assert a["lcm_residue_sufficient_state"] != b["lcm_residue_sufficient_state"]
    assert same_size_only_future_class(11, 1, 19, refinements) is True


def test_ramanujan_conductor_basis_reconstructs_the_same_roughness_projector():
    for fiber_size, first_quotient, primes in (
        (10, 101, (3, 5, 7)),
        (13, 211, (3, 7, 11)),
    ):
        data = ramanujan_channel_projection(fiber_size, first_quotient, primes)
        assert data["ramanujan_projection"].denominator == 1
        assert data["ramanujan_projection"].numerator == data["rough_progression_count"]
        assert data["frequency_basis_adds_no_information"] is True


def test_singleton_all_divisor_future_recovers_exact_origin():
    data = singleton_divisor_future(105)
    assert data["surviving_odd_refinements"] == (1, 3, 5, 7, 15, 21, 35, 105)
    assert data["largest_surviving_refinement"] == 105
    assert data["universal_divisor_future_recovers_origin"] is True


def test_square_basin_parent_channel_is_a_low_height_quadratic_diagonal():
    even = square_basin_quadratic_diagonal(46, (3, 5, 7, 11))
    odd = square_basin_quadratic_diagonal(45, (3, 5, 7, 11))

    assert even["fiber_size"] == 46
    assert even["first_quotient"] + 2 == 47**2
    assert even["square_offset"] == 2
    assert odd["fiber_size"] == 44
    assert odd["first_quotient"] + 3 == 46**2
    assert odd["square_offset"] == 3
    assert even["quadratic_diagonal"] is True
    assert odd["quadratic_diagonal"] is True
