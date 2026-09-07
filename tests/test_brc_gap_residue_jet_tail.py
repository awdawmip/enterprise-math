from __future__ import annotations

from math import isqrt
import random

from enterprise_math.brc_gap_residue_jet_tail import (
    INITIAL_FULL_WIDTH_REDUCTIONS,
    ROOT_RESIDUE_TOTAL_SEED_REDUCTIONS,
    GapResidueJetTailScanner,
    RootResidueDifferenceOrbit,
    transported_cascade_modulus,
)
from enterprise_math.brc_square_gap_cascade import (
    passes_square_residue_cascade,
)


def _exact_gap(root: int, remainder: int) -> int:
    return 0 if remainder == 0 else 2 * root + 1 - remainder


def _assert_last_source_exact(scanner: GapResidueJetTailScanner) -> None:
    multiplier = scanner.last_source_multiplier
    target = multiplier * scanner.n
    root = isqrt(target)
    remainder = target - root * root
    gap = _exact_gap(root, remainder)

    assert (scanner.last_source_root, scanner.last_source_remainder) == (
        root,
        remainder,
    )
    assert scanner.last_root_residue == root % scanner.modulus
    assert scanner.last_completion_gap_residue == gap % scanner.modulus
    assert scanner.last_cascade_passed == passes_square_residue_cascade(
        gap,
        "BALANCED",
    )
    if scanner.last_cascade_passed:
        gap_root = isqrt(gap)
        assert scanner.last_exact_square == (gap_root * gap_root == gap)


def _assert_last_source_exact_without_square(
    scanner: GapResidueJetTailScanner,
) -> None:
    multiplier = scanner.last_source_multiplier
    target = multiplier * scanner.n
    root = isqrt(target)
    remainder = target - root * root
    gap = _exact_gap(root, remainder)
    assert scanner.last_root_residue == root % scanner.modulus
    assert scanner.last_completion_gap_residue == gap % scanner.modulus
    assert scanner.last_cascade_passed == passes_square_residue_cascade(
        gap,
        "BALANCED",
    )


def test_registered_product_moduli() -> None:
    assert transported_cascade_modulus("PRIMARY") == 4032
    assert transported_cascade_modulus("COMPACT") == 49_008_960
    assert transported_cascade_modulus("FULL") == 621_090_550_080


def test_root_residue_difference_orbit_is_exact() -> None:
    modulus = 49_008_960
    roots = (10**60 + 17, 10**60 + 123_456, 10**60 + 654_321)
    orbit = RootResidueDifferenceOrbit.seed(
        modulus,
        (
            (101, roots[0] % modulus),
            (109, roots[1] % modulus),
            (117, roots[2] % modulus),
        ),
    )
    next_root = 10**60 + 2_345_678
    third = next_root - 3 * roots[2] + 3 * roots[1] - roots[0]
    assert orbit.advance(125, third) == next_root % modulus


def test_exact_seed_budget_then_no_new_root_reductions() -> None:
    scanner = GapResidueJetTailScanner((1 << 1023) + 987_654_321)
    assert scanner.initial_full_width_reductions == INITIAL_FULL_WIDTH_REDUCTIONS

    for _ in range(ROOT_RESIDUE_TOTAL_SEED_REDUCTIONS):
        scanner.advance_filter_inplace()
        assert scanner.last_root_residue_mode == "SEED_ROOT_MOD"
        _assert_last_source_exact(scanner)

    assert scanner.root_seed_mod_reductions == ROOT_RESIDUE_TOTAL_SEED_REDUCTIONS
    assert scanner.active_root_residue_orbit_count == 5
    assert scanner.root_residue_jet_steps == 0

    for _ in range(300):
        scanner.advance_filter_inplace()
        assert scanner.last_root_residue_mode == "ROOT_RESIDUE_JET"
        _assert_last_source_exact(scanner)

    assert scanner.root_seed_mod_reductions == ROOT_RESIDUE_TOTAL_SEED_REDUCTIONS
    assert scanner.root_residue_jet_steps == 300


def test_exhaustive_small_odd_scans_match_native_cascade() -> None:
    for n in range(1, 500, 2):
        scanner = GapResidueJetTailScanner(n)
        for _ in range(200):
            scanner.advance_filter_inplace()
            _assert_last_source_exact(scanner)


def test_random_large_scans_match_native_cascade_for_all_profiles() -> None:
    rng = random.Random(2026090714)
    for profile in ("PRIMARY", "COMPACT", "FULL"):
        for bits in (64, 128, 512, 1024, 2048, 4096, 8192):
            for _ in range(4):
                n = rng.getrandbits(bits) | (1 << (bits - 1)) | 1
                scanner = GapResidueJetTailScanner(
                    n,
                    transported_profile=profile,
                )
                for _ in range(400):
                    scanner.advance_filter_inplace()
                    _assert_last_source_exact(scanner)


def test_primary_rejection_can_defer_exact_gap_materialization() -> None:
    scanner = GapResidueJetTailScanner((1 << 511) + 123_456_789)
    found = False
    for _ in range(500):
        scanner.advance_filter_inplace(check_exact_square=False)
        if not scanner.last_transported_stages_passed:
            assert scanner.last_exact_gap is None
            found = True
            break
    assert found


def test_full_profile_has_no_post_seed_native_big_modulo() -> None:
    scanner = GapResidueJetTailScanner(
        (1 << 2047) + 333_777,
        transported_profile="FULL",
    )
    for _ in range(500):
        scanner.advance_filter_inplace(check_exact_square=False)
        _assert_last_source_exact_without_square(scanner)
    assert scanner.native_big_mod_reductions == 0
    assert scanner.root_seed_mod_reductions == ROOT_RESIDUE_TOTAL_SEED_REDUCTIONS
