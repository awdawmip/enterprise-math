from enterprise_math.p017_p018_root_p3_pair_collapse import root_p3_odd_candidate
from enterprise_math.p017_p018_signed_bilinear_gate import signed_odd_divisor_gate


def test_signed_gate_is_exact_mod_2d_residue_count() -> None:
    for k, divisor in ((20, 25), (100, 187), (203, 19 * 41), (203, 31 * 31), (500, 29 * 37)):
        row = signed_odd_divisor_gate(k, divisor)
        assert row["signed_modulus"] == 2 * divisor
        assert row["signed_residue"] == divisor
        assert all(n % (2 * divisor) == divisor for n in row["states"])
        assert all(q % 2 == 1 for q in row["odd_quotients"])
        if divisor > k:
            assert row["count"] in (0, 1)
            assert row["single_use_in_shell"]


def test_root_p3_odd_candidate_gate_equals_signed_divisor_gate() -> None:
    for k, a, b in ((203, 19, 41), (203, 31, 31), (300, 19, 47), (500, 29, 37)):
        projection = root_p3_odd_candidate(k, a, b)
        signed = signed_odd_divisor_gate(k, a * b)
        assert bool(projection["candidate_in_shell"]) == (signed["count"] == 1)
        if signed["count"] == 1:
            assert signed["odd_quotients"] == (projection["odd_candidate"],)
