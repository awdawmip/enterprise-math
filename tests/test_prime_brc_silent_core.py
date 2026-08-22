from enterprise_math.prime_brc_silent_core import (
    polarity_signature,
    polarity_silent,
    silent_core_capacity,
    silent_core_classification,
    silent_fixed_p_certificate,
)


def test_minimal_anchor_silent_witness_and_prime_alias():
    # k=8 lies below the k>=10 classification threshold but gives a clean
    # no-resurrection witness: 65=5*13 and prime 67 both have empty proper-
    # divisor polarity signatures in the same square basin.
    assert polarity_signature(8, 65) == ()
    assert polarity_signature(8, 67) == ()
    assert polarity_silent(8, 65)


def test_silent_core_examples_classify_as_high_semiprimes():
    examples = [
        (13, 5, 1, 11, 17),
        (14, 11, 1, 13, 17),
        (15, 7, 1, 13, 19),
        (17, 7, -1, 13, 23),
        (24, 11, -1, 19, 31),
    ]
    for k, radius, side, p, q in examples:
        data = silent_core_classification(k, radius, side)
        assert data["least_prime"] == p
        assert data["cofactor_prime"] == q
        assert data["omega"] == 2


def test_fixed_p_silent_capacity_is_at_most_one_dense():
    for k in range(10, 350):
        for p in range(k // 2 + 1, k + 1):
            # The certificate itself validates primality/transversality/chi=0.
            try:
                data = silent_fixed_p_certificate(k, p)
            except ValueError:
                continue
            assert data["capacity"] <= 1
            assert data["hit_count"] in (2, 4)


def test_global_silent_capacity_bound_dense():
    for k in range(10, 180):
        data = silent_core_capacity(k)
        assert data["silent_count"] <= data["prime_branch_count"]
