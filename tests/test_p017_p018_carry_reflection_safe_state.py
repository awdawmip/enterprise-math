from enterprise_math.p017_p018_carry_reflection_safe_state import (
    carry_only_insufficiency_witness,
    reflection_safe_signature,
)


def test_reflection_factors_through_carry_plus_ternary_defect_state():
    for primes in ((3,), (3, 5), (3, 5, 7)):
        primorial = 1
        for prime in primes:
            primorial *= prime
        for K in range(2 * primorial):
            data = reflection_safe_signature(K, primes)
            assert data["reflection_future_safe"] is True
            assert data["reflection_defect_invariant"] is True
            assert data["induced_reflection_is_involution"] is True


def test_current_carry_alone_is_not_a_reflection_safe_quotient():
    data = carry_only_insufficiency_witness()
    assert data["shared_current_carry"] == 1
    assert data["first_reflected_carry"] == 0
    assert data["second_reflected_carry"] == -1
    assert data["carry_alone_future_safe"] is False
    assert data["carry_plus_ternary_defect_future_safe"] is True
