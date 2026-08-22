from enterprise_math.prime_brc_silent_matching import (
    deterministic_silent_candidate,
    silent_matching,
    verify_all_silent_use_q_star,
)


def test_two_hit_deterministic_candidates_match_known_silent_states():
    # k=13,p=11: Q=16 even, zero-carry branch -> q_*=17 upper.
    a = deterministic_silent_candidate(13, 11)
    assert a["hit_count"] == 2
    assert a["q_star"] == 17
    assert a["side"] == 1
    assert a["q_star_is_silent"]

    # k=17,p=13: Q=23 odd, zero-carry branch -> q_*=23 lower.
    b = deterministic_silent_candidate(17, 13)
    assert b["hit_count"] == 2
    assert b["q_star"] == 23
    assert b["side"] == -1
    assert b["q_star_is_silent"]


def test_four_hit_deterministic_candidates_use_far_parity_survivor():
    # Q odd -> Q+2 survives the two-candidate silence obstruction.
    a = deterministic_silent_candidate(21, 13)
    assert a["hit_count"] == 4
    assert a["Q"] == 35
    assert a["q_star"] == 37
    assert a["side"] == 1
    assert a["q_star_is_silent"]

    # Q even -> Q-1 survives.
    b = deterministic_silent_candidate(23, 13)
    assert b["hit_count"] == 4
    assert b["Q"] == 42
    assert b["q_star"] == 41
    assert b["side"] == -1
    assert b["q_star_is_silent"]


def test_silent_core_is_bipartite_matching_dense():
    for k in range(10, 220):
        data = silent_matching(k)
        pairs = data["pairs"]
        assert len({p for p, _q, *_ in pairs}) == len(pairs)
        assert len({q for _p, q, *_ in pairs}) == len(pairs)
        assert data["matching_size"] <= data["matching_bound"]
        assert verify_all_silent_use_q_star(k)
