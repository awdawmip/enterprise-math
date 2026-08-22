from enterprise_math.prime_brc_outer_switch import (
    odd_hit_bit,
    odd_unique_hit_candidate,
    outer_switch_from_triprime,
    scaled_future_divisor_bit,
    triprime_from_outer_modulus,
)


def test_odd_unique_hit_threshold_k():
    # k=51, D=93=3*31 has two raw hits 2697,2790 but only one odd hit.
    data = odd_unique_hit_candidate(51, 93)
    assert data["exists"] is True
    assert data["quotient"] == 29
    assert data["state"] == 2697
    assert odd_hit_bit(51, 93) == 1


def test_scaled_future_is_exact_divisor_signature():
    # n=2697=3*29*31, D=3*31=93, residual q=29.
    assert scaled_future_divisor_bit(51, 93, 1) == 1
    assert scaled_future_divisor_bit(51, 93, 29) == 1
    assert scaled_future_divisor_bit(51, 93, 3) == 0
    assert scaled_future_divisor_bit(51, 93, 5) == 0


def test_outer_switch_squarefree_triprime():
    data = outer_switch_from_triprime(51, 2697)
    assert (data["p_min"], data["p_mid"], data["p_max"]) == (3, 29, 31)
    assert data["outer_modulus"] == 93
    assert triprime_from_outer_modulus(51, 93)["n"] == 2697


def test_outer_switch_repeated_triprime():
    # 1083=3*19^2, outer D=57 and middle q=19.
    data = outer_switch_from_triprime(32, 1083)
    assert (data["p_min"], data["p_mid"], data["p_max"]) == (3, 19, 19)
    assert data["outer_modulus"] == 57
    assert triprime_from_outer_modulus(32, 57)["n"] == 1083


def test_non_straddling_p2_modulus_is_not_outer_triprime_key():
    # D can have an odd hit without its decoded quotient lying between D's factors.
    assert triprime_from_outer_modulus(20, 33) is None
