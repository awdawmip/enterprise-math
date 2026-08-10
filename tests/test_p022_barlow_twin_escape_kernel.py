from enterprise_math.p022_barlow_twin_escape_kernel import (
    twin_escape_kernel_conditions,
    twin_escape_kernel_theorem,
    twin_escape_observations,
)


def test_rank_six_has_a_nontrivial_abstract_escape_kernel() -> None:
    # The endpoint depth at T-1=10 cancels the primitive source at r=6.
    # D_10 is absent because 19 is prime; the only observed interior edge is D_8.
    profile = ((6, 1), (10, 1))
    assert twin_escape_observations(6, profile) == ((8, 0), (11, 0))
    assert twin_escape_kernel_conditions(6, profile)
    assert twin_escape_kernel_theorem(6, profile)


def test_hidden_interior_mass_is_allowed_exactly_at_another_twin_center() -> None:
    # For r=21, s=30 is another twin center because 59 and 61 are prime.
    # It is an isolated vertex of the surviving defect-edge graph.
    profile = ((21, 2), (30, 3), (40, 2))
    assert twin_escape_kernel_conditions(21, profile)
    assert twin_escape_kernel_theorem(21, profile)

    # Moving the same interior mass to 29 exposes it at an existing edge.
    visible = ((21, 2), (29, 3), (40, 2))
    assert not twin_escape_kernel_conditions(21, visible)
    assert not twin_escape_kernel_theorem(21, visible)
    assert any(value for _, value in twin_escape_observations(21, visible))


def test_endpoint_prime_condition_is_part_of_the_iff() -> None:
    # r=30 is a twin center, but 4r-5=115 is composite, so the endpoint mass
    # at T-1=58 is detected by D_58 before terminal cancellation at D_59.
    profile = ((30, 1), (58, 1))
    assert not twin_escape_kernel_conditions(30, profile)
    assert not twin_escape_kernel_theorem(30, profile)
    assert (58, 1) in twin_escape_observations(30, profile)
