from __future__ import annotations

from math import isqrt
import random

from enterprise_math.brc_energy_cross_coordinate_tail import (
    CrossEnergyDifferenceJetTailScanner,
    cross_coordinate_from_mixed,
    mixed_coordinate_from_cross,
    next_cross_coordinate,
    square_increment_cross_third_difference,
)
from enterprise_math.brc_energy_difference_jet_tail import (
    EnergyDifferenceJetTailScanner,
    square_increment_third_difference,
)


def test_cross_coordinate_is_information_equivalent_to_mixed_coordinate() -> None:
    rng = random.Random(2026090714)
    for _ in range(1000):
        mixed = rng.randrange(-(10**40), 10**40)
        q1 = rng.randrange(-(10**20), 10**20)
        q2 = rng.randrange(-2, 99)
        j1 = rng.randrange(-(10**30), 10**30)
        cross = cross_coordinate_from_mixed(mixed, q1, q2, j1)
        assert mixed_coordinate_from_cross(cross, q1, q2, j1) == mixed


def test_compact_third_difference_matches_existing_identity() -> None:
    rng = random.Random(2026090715)
    for _ in range(2000):
        q = rng.randrange(0, 10**20)
        j = rng.randrange(0, 10**30)
        s = rng.randrange(-(10**10), 10**10)
        a = rng.randrange(-2, 99)
        t = rng.randrange(-(10**15), 10**15)
        u = rng.randrange(-(10**10), 10**10)
        e = rng.randrange(-4, 5)
        w = rng.randrange(-3, 388)
        mixed = s * u
        cross = cross_coordinate_from_mixed(mixed, s, a, t)
        q_new = q + s + a + e
        j_new = j + t + u + w

        old = square_increment_third_difference(
            root=j,
            quotient=q,
            quotient_first=s,
            quotient_second=a,
            root_first=t,
            root_second=u,
            quotient_third=e,
            root_third=w,
            mixed_first_second=mixed,
        )
        compact = square_increment_cross_third_difference(
            target_root=j_new,
            target_quotient=q_new,
            quotient_third=e,
            root_third=w,
            cross_coordinate=cross,
        )
        assert compact == old


def test_cross_coordinate_recurrence_is_exact() -> None:
    rng = random.Random(2026090716)
    for _ in range(2000):
        s = rng.randrange(-(10**15), 10**15)
        a = rng.randrange(-2, 99)
        t = rng.randrange(-(10**20), 10**20)
        u = rng.randrange(-(10**15), 10**15)
        e = rng.randrange(-4, 5)
        w = rng.randrange(-3, 388)
        cross = s * u + a * (s + t)

        a_new = a + e
        s_new = s + a_new
        u_new = u + w
        t_new = t + u_new
        direct = s_new * u_new + a_new * (s_new + t_new)
        transported = next_cross_coordinate(
            cross_coordinate=cross,
            quotient_first=s,
            root_first=t,
            quotient_third=e,
            root_third=w,
            new_quotient_second=a_new,
            new_root_second=u_new,
        )
        assert transported == direct


def _assert_same_state(
    reference: EnergyDifferenceJetTailScanner,
    compact: CrossEnergyDifferenceJetTailScanner,
) -> None:
    assert (
        compact.multiplier,
        compact.root,
        compact.remainder,
        compact.last_predictor_quotient,
        compact.last_predictor_quotient_remainder,
        compact.last_square_increment,
        compact.last_quotient_third_difference,
        compact.last_root_third_difference,
        compact.last_energy_third_difference,
        compact.last_root_corrections,
    ) == (
        reference.multiplier,
        reference.root,
        reference.remainder,
        reference.last_predictor_quotient,
        reference.last_predictor_quotient_remainder,
        reference.last_square_increment,
        reference.last_quotient_third_difference,
        reference.last_root_third_difference,
        reference.last_energy_third_difference,
        reference.last_root_corrections,
    )
    root = isqrt(compact.multiplier * compact.n)
    assert compact.root == root
    assert compact.remainder == compact.multiplier * compact.n - root * root


def test_exhaustive_small_scans_match_current_energy_jet() -> None:
    for n in range(1, 300, 2):
        reference = EnergyDifferenceJetTailScanner(n)
        compact = CrossEnergyDifferenceJetTailScanner(n)
        for _ in range(120):
            reference.advance_inplace()
            compact.advance_inplace()
            _assert_same_state(reference, compact)


def test_random_large_scans_match_current_energy_jet() -> None:
    rng = random.Random(2026090717)
    for bits in (64, 128, 512, 1024, 2048, 4096, 8192):
        for _ in range(5):
            n = rng.getrandbits(bits) | (1 << (bits - 1)) | 1
            reference = EnergyDifferenceJetTailScanner(n)
            compact = CrossEnergyDifferenceJetTailScanner(n)
            for _ in range(500):
                reference.advance_inplace()
                compact.advance_inplace()
                _assert_same_state(reference, compact)


def test_seed_budgets_are_unchanged() -> None:
    scanner = CrossEnergyDifferenceJetTailScanner((1 << 1023) + 987654321)
    for _ in range(15):
        scanner.advance_inplace()
        assert scanner.last_quotient_mode == "SEED_DIVISION"
        assert scanner.last_energy_mode == "SEED_PRODUCT"
    assert scanner.seed_divisions == 15
    assert scanner.seed_square_increment_products == 15
    assert scanner.active_orbit_count == 5

    for _ in range(200):
        scanner.advance_inplace()
        assert scanner.last_quotient_mode == "JET_RECURRENCE"
        assert scanner.last_energy_mode == "CROSS_COORDINATE_RECURRENCE"
    assert scanner.seed_divisions == 15
    assert scanner.seed_square_increment_products == 15
    assert scanner.jet_steps == 200
