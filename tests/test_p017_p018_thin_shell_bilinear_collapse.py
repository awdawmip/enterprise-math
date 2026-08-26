from fractions import Fraction

from enterprise_math.p017_p018_p3_cubic_type3_bridge import p3_cubic_type3_partition
from enterprise_math.p017_p018_thin_shell_bilinear_collapse import (
    LAST_THIN_SHELL_FAILURE,
    THIN_SHELL_BILINEAR_THRESHOLD,
    balanced_pair_third_factor,
    balanced_prime_triples_via_pairs,
    reconstruct_last_thin_shell_failure,
    square_interval_divisor_gate,
    thin_shell_bilinear_certificate,
)


def test_exact_thin_shell_bilinear_threshold() -> None:
    assert LAST_THIN_SHELL_FAILURE == 201
    assert THIN_SHELL_BILINEAR_THRESHOLD == 202
    assert reconstruct_last_thin_shell_failure() == 201

    for k in range(202, 224):
        cert = thin_shell_bilinear_certificate(k)
        assert cert["proof_mode"] == "FINITE_EXACT_THRESHOLD_WINDOW"
        assert cert["strict_margin"] > 0

    for k in (224, 512, 1000, 8191, 65536):
        cert = thin_shell_bilinear_certificate(k)
        assert cert["proof_mode"] == "RATIONAL_ANALYTIC_TAIL"
        assert cert["floor_square"] > cert["shell_width"]


def test_divisor_gate_is_exact_short_interval_remainder() -> None:
    for k in (202, 300, 1000):
        width = 2 * k
        for divisor in (width + 1, width + 7, width * 2 + 1, width * 5 + 3):
            row = square_interval_divisor_gate(k, divisor)
            upper = k * k + 2 * k
            expected = upper // divisor - (k * k) // divisor
            assert row["multiple_count"] == expected
            assert row["gate"] == (upper % divisor < width)
            assert row["reconstruction"] == Fraction(expected, 1)
            assert row["centered_remainder"] == Fraction(expected * divisor - width, divisor)


def test_balanced_pair_has_unique_floor_candidate() -> None:
    # k=203 has the explicit balanced triple 31*31*43 in the shell.
    row = balanced_pair_third_factor(203, 31, 31)
    assert row["candidate_c"] == 43
    assert row["candidate_in_shell"]
    assert row["ordered_candidate"]
    assert row["candidate_is_prime"]
    assert row["prime_triple_gate"]
    assert row["candidate_value"] == 31 * 31 * 43
    assert 203 * 203 < row["candidate_value"] <= 203 * 203 + 406


def test_pair_projection_matches_generation_2_balanced_triples() -> None:
    for k in (202, 203, 300, 500, 1000, 2000):
        direct = p3_cubic_type3_partition(k)
        projected = balanced_prime_triples_via_pairs(k)

        direct_rows = {
            (a, b, c, value, offset)
            for a, b, c, _root, value, offset in direct["cubic_low_balanced_triples"]
        }
        projected_rows = set(projected["balanced_prime_triples"])
        assert projected_rows == direct_rows
        assert projected["free_discrete_variables"] == 2
        assert projected["status"] == "THIN_SHELL_TYPE_III_TO_TYPE_II"
