from enterprise_math.p017_p018_root_p3_core_tail_dichotomy import root_p3_core_tail_partition
from enterprise_math.p017_p018_root_p3_pair_collapse import root_p3_prime_triples_via_pairs


def test_root_p3_triples_are_exactly_fully_k_smooth_rough_states() -> None:
    for k in (20, 30, 50, 100, 202, 203, 300, 500, 1000):
        data = root_p3_core_tail_partition(k)
        assert data["rough_count"] == (
            data["prime_count"]
            + data["semiprime_tail_count"]
            + data["fully_smooth_triple_count"]
        )
        assert data["p3_only_equals_root_rough_intersect_k_smooth"]
        assert data["status"] == "ROOT_P3_CORE_TAIL_DICHOTOMY"

        for p, q, value, offset in data["semiprime_tail_rows"]:
            assert data["p3_cutoff"] < p <= k < q
            assert value == p * q == k * k + offset

        for a, b, c, value, offset in data["fully_smooth_triple_rows"]:
            assert data["p3_cutoff"] < a <= b <= c <= k
            assert a * b > k
            assert value == a * b * c == k * k + offset


def test_fully_smooth_core_triples_match_pair_projection() -> None:
    for k in (20, 100, 202, 203, 300, 500):
        core = root_p3_core_tail_partition(k)
        pair = root_p3_prime_triples_via_pairs(k)
        assert set(core["fully_smooth_triple_rows"]) == set(pair["triple_rows"])
