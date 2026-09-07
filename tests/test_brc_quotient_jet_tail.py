from __future__ import annotations

from math import isqrt
import random

from enterprise_math.brc_quotient_jet_tail import (
    QUOTIENT_JET_MAX_ABS_CORRECTION,
    QUOTIENT_JET_SECOND_DIFFERENCE_MAX,
    QUOTIENT_JET_SECOND_DIFFERENCE_MIN,
    QuotientJetTailScanner,
    outgoing_sparse_step,
    quotient_jet_bound_sufficient,
    quotient_jet_tail_threshold,
)
from enterprise_math.brc_linear_deep_tail import (
    common_mod8_linear_tail_sufficient,
    odd_n_multiplier_is_representative,
)


def _assert_last_step_exact(scanner: QuotientJetTailScanner) -> None:
    source_m = scanner.last_source_multiplier
    h = scanner.multiplier - source_m
    direct_q, direct_rho = divmod(
        2 * h * scanner.last_source_root,
        4 * source_m + h,
    )
    assert (
        scanner.last_predictor_quotient,
        scanner.last_predictor_quotient_remainder,
    ) == (direct_q, direct_rho)
    direct_root = isqrt(scanner.multiplier * scanner.n)
    assert scanner.root == direct_root
    assert scanner.remainder == (
        scanner.multiplier * scanner.n - direct_root * direct_root
    )
    assert scanner.last_root_corrections <= 2
    assert (
        abs(scanner.last_quotient_correction)
        <= QUOTIENT_JET_MAX_ABS_CORRECTION
    )


def test_outgoing_sparse_step_pattern() -> None:
    expected = {0: 1, 1: 2, 3: 2, 5: 2, 7: 1}
    for m in range(1, 1000):
        if odd_n_multiplier_is_representative(m):
            assert outgoing_sparse_step(m) == expected[m % 8]


def test_uniform_tail_threshold_certifies_both_steps() -> None:
    for n in (1, 3, 17, 10**30 + 57, (1 << 2047) + 987654321):
        start = quotient_jet_tail_threshold(n)
        assert odd_n_multiplier_is_representative(start)
        assert common_mod8_linear_tail_sufficient(n, start)
        assert quotient_jet_bound_sufficient(n, start, 1)
        assert quotient_jet_bound_sufficient(n, start, 2)


def test_exactly_fifteen_seed_divisions_then_only_jet_steps() -> None:
    n = (1 << 521) + 987654321
    scanner = QuotientJetTailScanner(n)
    modes = []
    for _ in range(15):
        scanner.advance_inplace()
        modes.append(scanner.last_quotient_mode)
        _assert_last_step_exact(scanner)
    assert modes == ["SEED_DIVISION"] * 15
    assert scanner.seed_divisions == 15
    assert scanner.jet_steps == 0

    for _ in range(200):
        scanner.advance_inplace()
        assert scanner.last_quotient_mode == "JET_RECURRENCE"
        _assert_last_step_exact(scanner)
    assert scanner.seed_divisions == 15
    assert scanner.jet_steps == 200


def test_step_record_and_allocation_free_hot_path_agree() -> None:
    n = (1 << 1023) + 42424243
    left = QuotientJetTailScanner(n)
    right = QuotientJetTailScanner(n)
    for _ in range(100):
        record = left.step()
        right.advance_inplace()
        assert (
            record.target_multiplier,
            record.target_root,
            record.target_remainder,
        ) == (right.multiplier, right.root, right.remainder)
        assert record.predictor_quotient == right.last_predictor_quotient
        assert record.predictor_quotient_remainder == (
            right.last_predictor_quotient_remainder
        )
        assert record.quotient_mode == right.last_quotient_mode
        assert record.quotient_correction == right.last_quotient_correction
        assert record.root_corrections == right.last_root_corrections


def test_exhaustive_small_odd_scans_match_direct_oracles() -> None:
    for n in range(1, 500, 2):
        scanner = QuotientJetTailScanner(n)
        for _ in range(200):
            scanner.advance_inplace()
            _assert_last_step_exact(scanner)
            for second in scanner.quotient_second_differences:
                assert (
                    QUOTIENT_JET_SECOND_DIFFERENCE_MIN
                    <= second
                    <= QUOTIENT_JET_SECOND_DIFFERENCE_MAX
                )


def test_random_large_scans_match_direct_oracles() -> None:
    rng = random.Random(20260907)
    for bits in (64, 128, 512, 1024, 2048, 4096, 8192):
        for _ in range(6):
            n = rng.getrandbits(bits) | (1 << (bits - 1)) | 1
            scanner = QuotientJetTailScanner(n)
            for _ in range(500):
                scanner.advance_inplace()
                _assert_last_step_exact(scanner)


def test_bound_four_is_attained_in_finite_regression_witness() -> None:
    # A deterministic witness found by the finite stress harness. It prevents
    # silently tightening the proved [-4,4] interval to a false smaller range.
    n = 16056244865410046723
    scanner = QuotientJetTailScanner(n)
    seen = False
    for _ in range(64):
        scanner.advance_inplace()
        if scanner.last_source_multiplier == 5359:
            assert scanner.last_quotient_correction == -4
            seen = True
            break
    assert seen
