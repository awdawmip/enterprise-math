from __future__ import annotations

from math import isqrt
import random

from enterprise_math.brc_energy_difference_jet_tail import (
    ENERGY_JET_TOTAL_SEED_DIVISIONS,
    ENERGY_JET_TOTAL_SEED_PRODUCTS,
    ROOT_JET_THIRD_DIFFERENCE_MAX,
    ROOT_JET_THIRD_DIFFERENCE_MIN,
    EnergyDifferenceJetTailScanner,
    root_stride_third_difference,
    root_third_difference_bound_sufficient,
    square_increment_third_difference,
)
from enterprise_math.brc_quotient_jet_tail import QuotientJetTailScanner


def _assert_last_step_exact(scanner: EnergyDifferenceJetTailScanner) -> None:
    source_m = scanner.last_source_multiplier
    step = scanner.multiplier - source_m
    quotient, quotient_remainder = divmod(
        2 * step * scanner.last_source_root,
        4 * source_m + step,
    )
    assert (
        scanner.last_predictor_quotient,
        scanner.last_predictor_quotient_remainder,
    ) == (quotient, quotient_remainder)
    assert scanner.last_square_increment == quotient * (
        2 * scanner.last_source_root + quotient
    )
    root = isqrt(scanner.multiplier * scanner.n)
    assert scanner.root == root
    assert scanner.remainder == scanner.multiplier * scanner.n - root * root
    assert scanner.last_root_corrections <= 2
    assert -4 <= scanner.last_quotient_third_difference <= 4
    assert (
        ROOT_JET_THIRD_DIFFERENCE_MIN
        <= scanner.last_root_third_difference
        <= ROOT_JET_THIRD_DIFFERENCE_MAX
    )


def test_root_third_difference_bound_and_sharp_witnesses() -> None:
    negative_n = 18432563335758795797
    negative_m = 5412521
    assert root_third_difference_bound_sufficient(negative_n, negative_m)
    assert root_stride_third_difference(negative_n, negative_m) == -3

    positive_n = 326270861943277281288965027192289443045
    positive_m = 38227135
    assert root_third_difference_bound_sufficient(positive_n, positive_m)
    assert root_stride_third_difference(positive_n, positive_m) == 387


def test_exact_square_increment_third_difference_identity() -> None:
    rng = random.Random(20260907)
    for _ in range(500):
        q0 = rng.randrange(0, 10**10)
        q1 = rng.randrange(0, 10**10)
        q2 = rng.randrange(0, 10**10)
        q3 = rng.randrange(0, 10**10)
        j0 = rng.randrange(0, 10**12)
        j1 = rng.randrange(0, 10**12)
        j2 = rng.randrange(0, 10**12)
        j3 = rng.randrange(0, 10**12)

        q_first = q2 - q1
        q_second = q2 - 2 * q1 + q0
        q_third = q3 - 3 * q2 + 3 * q1 - q0
        root_first = j2 - j1
        root_second = j2 - 2 * j1 + j0
        root_third = j3 - 3 * j2 + 3 * j1 - j0
        mixed = q_first * root_second

        energies = tuple(q * (2 * j + q) for q, j in zip(
            (q0, q1, q2, q3),
            (j0, j1, j2, j3),
        ))
        direct = energies[3] - 3 * energies[2] + 3 * energies[1] - energies[0]
        transported = square_increment_third_difference(
            root=j2,
            quotient=q2,
            quotient_first=q_first,
            quotient_second=q_second,
            root_first=root_first,
            root_second=root_second,
            quotient_third=q_third,
            root_third=root_third,
            mixed_first_second=mixed,
        )
        assert transported == direct


def test_exactly_fifteen_seed_divisions_and_products() -> None:
    scanner = EnergyDifferenceJetTailScanner((1 << 1023) + 987654321)
    for _ in range(ENERGY_JET_TOTAL_SEED_DIVISIONS):
        scanner.advance_inplace()
        assert scanner.last_quotient_mode == "SEED_DIVISION"
        assert scanner.last_energy_mode == "SEED_PRODUCT"
        _assert_last_step_exact(scanner)
    assert scanner.seed_divisions == ENERGY_JET_TOTAL_SEED_DIVISIONS
    assert (
        scanner.seed_square_increment_products
        == ENERGY_JET_TOTAL_SEED_PRODUCTS
    )
    assert scanner.active_orbit_count == 5
    assert scanner.jet_steps == 0

    for _ in range(200):
        scanner.advance_inplace()
        assert scanner.last_quotient_mode == "JET_RECURRENCE"
        assert scanner.last_energy_mode == "DIFFERENCE_JET_RECURRENCE"
        _assert_last_step_exact(scanner)
    assert scanner.seed_divisions == ENERGY_JET_TOTAL_SEED_DIVISIONS
    assert (
        scanner.seed_square_increment_products
        == ENERGY_JET_TOTAL_SEED_PRODUCTS
    )
    assert scanner.jet_steps == 200


def test_exhaustive_small_odd_scans_match_direct_oracles() -> None:
    for n in range(1, 500, 2):
        scanner = EnergyDifferenceJetTailScanner(n)
        for _ in range(200):
            scanner.advance_inplace()
            _assert_last_step_exact(scanner)


def test_random_large_scans_match_current_quotient_scanner() -> None:
    rng = random.Random(2026090713)
    for bits in (64, 128, 512, 1024, 2048, 4096, 8192):
        for _ in range(6):
            n = rng.getrandbits(bits) | (1 << (bits - 1)) | 1
            energy = EnergyDifferenceJetTailScanner(n)
            quotient = QuotientJetTailScanner(n)
            for _ in range(500):
                energy.advance_inplace()
                quotient.advance_inplace()
                assert (
                    energy.multiplier,
                    energy.root,
                    energy.remainder,
                ) == (
                    quotient.multiplier,
                    quotient.root,
                    quotient.remainder,
                )
                _assert_last_step_exact(energy)
