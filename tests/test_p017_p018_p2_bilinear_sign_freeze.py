from enterprise_math.p017_p018_p2_bilinear_sign_freeze import (
    p2_nontrivial_factorization_sign_freeze,
)


def test_p2_nontrivial_factorizations_have_frozen_positive_state_mobius() -> None:
    for k in (3, 4, 5, 10, 17, 31, 100, 203, 500, 1000):
        data = p2_nontrivial_factorization_sign_freeze(k)
        assert data["ordered_nontrivial_factorization_count"] == 2 * data["semiprime_count"]
        assert data["all_state_mobius_signs_positive"]
        assert data["prime_states_have_no_nontrivial_factorization"]
        assert data["status"] == "P2_BILINEAR_MOBIUS_SIGN_FREEZE"

        for m, n, value, offset in data["ordered_nontrivial_factorization_rows"]:
            assert m > 1 and n > 1 and m != n
            assert value == m * n == k * k + offset
            assert 1 <= offset <= 2 * k
