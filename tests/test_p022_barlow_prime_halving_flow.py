from enterprise_math.p022_barlow_prime_halving_flow import (
    flow_boundary_equals_canonical_basis,
    flow_paths_amplify_terminal_prime,
    gradient_pairing_equals_canonical,
    p157_flow_certificate,
    p369581_flow_certificate,
    prime_halving_flow,
    unit_prime_halving_flow,
)


def test_unit_prime_flows_show_recursive_path_multiplicity() -> None:
    assert unit_prime_halving_flow(17) == ((2, 3), (3, 1), (5, 1), (17, 1))
    # 1087 -> 544 = 2^5*17, so its flow contains another copy of the full
    # prime-17 ancestry in addition to five direct 2-packets.
    flow1087 = dict(unit_prime_halving_flow(1087))
    assert flow1087[1087] == 1
    assert flow1087[17] == 1
    assert flow1087[5] == 1
    assert flow1087[3] == 1
    assert flow1087[2] >= 5


def test_flow_boundary_reconstructs_canonical_integer_basis() -> None:
    for value in (2, 3, 5, 17, 31, 43, 78, 155, 184790, 369579):
        assert flow_boundary_equals_canonical_basis(value)


def test_gradient_pairing_equals_direct_beta_pairing() -> None:
    weights = {8: 1, 16: 2, 75: 1, 78: 1}
    for value in (17, 31, 43, 78, 155, 184790, 369579):
        assert gradient_pairing_equals_canonical(value, weights)


def test_p157_flow_explains_unit_support_coefficient() -> None:
    assert p157_flow_certificate() == (0, 1, 0, 1)
    assert flow_paths_amplify_terminal_prime(155, 31) == 1


def test_p369581_flow_explains_double_support_coefficient() -> None:
    assert p369581_flow_certificate() == (2, 0, -2, 2)
    assert flow_paths_amplify_terminal_prime(184790, 17) == 2


def test_m_flow_contains_two_distinct_prime17_packets() -> None:
    flow = dict(prime_halving_flow(184790))
    assert flow[17] == 2
    # The two packets are supplied by the direct factor 17 and by the factor
    # 1087 whose half 544 contains another 17.
    assert flow[1087] == 1
