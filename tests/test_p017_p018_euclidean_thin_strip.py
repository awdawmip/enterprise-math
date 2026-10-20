from enterprise_math.p017_p018_euclidean_thin_strip import (
    euclidean_divisor_channel,
    euclidean_normalized_reciprocity_phase,
    euclidean_thin_strip_chart,
    reciprocity_integer,
)


def test_euclidean_chart_exactly_straightens_the_physical_thin_strip():
    for k in (8, 17, 46):
        for n in range(1, min(k + 3, 20)):
            data = euclidean_thin_strip_chart(k, n)
            M = data["center"]
            Q = data["quotient_Q"]
            t = data["remainder_t"]
            assert M == n * Q + t
            for row in data["rows"]:
                assert row["m"] == Q + row["j"]
                assert row["radius"] == n * row["j"] - t
                assert -k < row["radius"] < k
                assert row["opposite_state"] == n * (Q - row["j"]) + 2 * t


def test_divisor_channel_is_exact_residue_in_the_j_coordinate():
    k = 46
    for n in (5, 7, 11, 13):
        chart = euclidean_thin_strip_chart(k, n)
        for d in (3, 5, 7, 11, 13, 17):
            if d % 2 == 0 or __import__("math").gcd(n, d) != 1:
                continue
            for row in chart["rows"]:
                data = euclidean_divisor_channel(k, n, int(row["j"]), d)
                assert data["divisor_channel_identity"] is True
                assert data["direct_divisibility"] == data["channel_selected"]


def test_additive_reciprocity_difference_is_integral():
    for m, d in ((5, 7), (11, 35), (37, 43), (199, 35)):
        assert isinstance(reciprocity_integer(m, d), int)


def test_large_center_disappears_into_nested_euclidean_remainders():
    for center, m, d, h in (
        (46 * 47, 11, 35, 1),
        (46 * 47, 199, 35, 3),
        (8191 * 8192, 127, 105, 7),
    ):
        data = euclidean_normalized_reciprocity_phase(center, m, d, h)
        assert data["euclidean_phase_identity"] is True
        assert 0 <= data["remainder_u"] < m
        assert 0 <= data["nested_remainder_v"] < d
        assert 0 <= data["remainder_mod_md"] < m * d
        assert data["remainder_mod_md"] == center % (m * d)
        assert data["phase_difference_integer"] == int(
            data["reciprocal_phase"] - data["euclidean_normalized_phase"]
        )
