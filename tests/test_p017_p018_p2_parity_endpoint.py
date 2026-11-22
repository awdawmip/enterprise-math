from enterprise_math.p017_p018_p2_parity_endpoint import p2_parity_endpoint


def test_p2_mobius_endpoint_reconstructs_prime_and_semiprime_counts() -> None:
    for k in (3, 4, 5, 10, 17, 31, 100, 203, 500, 1000):
        data = p2_parity_endpoint(k)
        assert data["prime_from_mobius"] == data["prime_count"]
        assert data["semiprime_from_mobius"] == data["semiprime_count"]
        assert data["rough_count"] == data["prime_count"] + data["semiprime_count"]
        assert data["high_prime_incidence"] == data["semiprime_count"]
        assert data["legendre_failure_equivalent"]
        assert data["status"] == "P2_PARITY_ENDPOINT"


def test_p2_rough_composites_are_squarefree_one_low_one_high_semiprimes() -> None:
    for k in (17, 100, 203, 500):
        data = p2_parity_endpoint(k)
        z2 = data["p2_cutoff"]
        for p, q, value, offset in data["semiprime_rows"]:
            assert z2 < p <= k < q
            assert p != q
            assert value == p * q == k * k + offset
            assert 1 <= offset <= 2 * k
