from enterprise_math.p017_p018_root_p3_canonical_pair import (
    canonical_pair_recovery_profile,
    canonical_pair_triple_rows,
    canonical_odd_cofactor_candidate,
)


def test_canonical_pair_rows_use_one_single_use_token_per_triple():
    for k in (17, 31, 64, 100, 257):
        rows = canonical_pair_triple_rows(k)
        tokens = [row[3] for row in rows]
        assert len(tokens) == len(set(tokens))
        for a, b, c, token, value in rows:
            assert a < b < c or a < b <= c
            assert token == a * b > k
            assert value == token * c
            candidate = canonical_odd_cofactor_candidate(k, token)
            assert candidate["cofactor_candidate"] == c
            assert candidate["candidate_in_square_shell"] is True
            assert candidate["single_use"] is True


def test_canonical_pair_correction_recovers_prime_count():
    for k in (4, 5, 8, 17, 31, 64, 100, 257):
        data = canonical_pair_recovery_profile(k)
        assert data["exact_canonical_pair_recovery"] is True
        assert data["canonical_pair_prime_recovery"] == data["prime_count"]


def test_k1000_canonical_pair_checkpoint_has_twelve_squarefree_triples():
    data = canonical_pair_recovery_profile(1000)
    assert data["fourth_root_cutoff"] == 31
    assert data["canonical_triple_count"] == 12
    assert data["prime_count"] == 152
    assert data["canonical_pair_prime_recovery"] == 152
