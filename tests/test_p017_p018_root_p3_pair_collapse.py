from enterprise_math.p017_p018_root_p3_pair_collapse import (
    root_p3_odd_candidate,
    root_p3_prime_triples_via_pairs,
)


def test_root_p3_odd_candidate_examples() -> None:
    row = root_p3_odd_candidate(203, 31, 31)
    assert row["odd_candidate"] == 43
    assert row["candidate_in_shell"]
    assert row["ordered_candidate"]
    assert row["candidate_is_prime"]
    assert row["prime_triple_gate"]
    assert row["candidate_value"] == 31 * 31 * 43

    row2 = root_p3_odd_candidate(203, 19, 41)
    assert row2["odd_candidate"] == 53
    assert row2["prime_triple_gate"]
    assert row2["candidate_value"] == 19 * 41 * 53


def test_root_p3_pair_projection_matches_direct_reconstruction() -> None:
    for k in (20, 30, 50, 100, 202, 203, 300, 500, 1000):
        data = root_p3_prime_triples_via_pairs(k)
        assert data["free_discrete_variables"] == 2
        assert data["status"] == "ROOT_P3_TWO_FREE_VARIABLES"
        for a, b, c, value, offset in data["triple_rows"]:
            assert a <= b <= c
            assert value == a * b * c == k * k + offset
            assert 1 <= offset <= 2 * k
