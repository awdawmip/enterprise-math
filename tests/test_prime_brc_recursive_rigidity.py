from enterprise_math.prime_brc_recursive_rigidity import (
    quotient_support,
    quotient_support_rigidity,
    root_only_cancellation_witness,
)


def test_quotient_supports_are_injective_through_k():
    for k in range(2, 80):
        seen = {}
        for d in range(1, k + 1):
            q = quotient_support(k, d)
            assert q not in seen
            seen[q] = d
        quotient_support_rigidity(k, 1, k)


def test_root_cancellation_is_not_exact_recursive_recoalescence():
    data = root_only_cancellation_witness()
    assert data["Q_15"] == (33, 34, 35)
    assert data["Q_17"] == (29, 30, 31)
    assert data["root_multiset"] == ((5, 3),)
    assert data["signed_root_sum"] == 0
    assert not data["exact_quotient_supports_equal"]
