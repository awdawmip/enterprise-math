from __future__ import annotations

import itertools
import sys
from math import gcd
from pathlib import Path

EXPERIMENTS = Path(__file__).parents[1] / "experiments"
sys.path.insert(0, str(EXPERIMENTS))

import r007_layer_deletion_capability as cap


def divisors(n: int) -> set[int]:
    return {d for d in range(1, n + 1) if n % d == 0}


def test_gamma_fixed_points_equal_exact_deletion_outputs() -> None:
    families = [
        (6, 10, 15),
        (4, 8, 16),
        (12, 18, 30),
        (6, 6, 10),
        (2, 3, 5, 7),
    ]
    for scales in families:
        for h in range(len(scales)):
            assert cap.exact_reachable_gcds_by_closure(scales, h) == cap.exact_reachable_gcds_bruteforce(scales, h)


def test_capability_ideal_is_downward_closure_of_exact_outputs() -> None:
    for scales in ((6, 10, 15), (4, 8, 16), (12, 18, 30), (2, 3, 5, 7)):
        for h in range(len(scales)):
            exact = cap.exact_reachable_gcds_by_closure(scales, h)
            downward = {
                d
                for value in exact
                for d in divisors(value)
            }
            assert set(cap.capability_ideal(scales, h)) == downward


def test_deletion_envelope_interpolates_gcd_to_lcm_by_valuation_order_statistics() -> None:
    families = ((6, 10, 15), (4, 8, 16), (12, 18, 30), (8, 12, 18, 30))
    for scales in families:
        chain = cap.envelope_chain(scales)
        assert chain[0] == cap.gcd_all(scales)
        assert chain[-1] == cap.lcm_all(scales)
        assert all(chain[i + 1] % chain[i] == 0 for i in range(len(chain) - 1))
        for h, envelope in enumerate(chain):
            for p in (2, 3, 5, 7):
                assert cap.valuation(envelope, p) == cap.valuation_order_statistic(scales, p, h)


def test_envelope_can_be_nonprincipal_and_lose_cross_prime_correlation() -> None:
    first = (6, 10, 15)
    second = (30, 2, 15)
    assert cap.envelope_chain(first) == (1, 30, 30)
    assert cap.envelope_chain(second) == (1, 30, 30)
    assert set(cap.exact_reachable_gcds_by_closure(first, 1)) == {1, 2, 3, 5}
    assert set(cap.exact_reachable_gcds_by_closure(second, 1)) == {1, 2, 15}
    assert not cap.capability_is_principal(first, 1)
    assert not cap.capability_is_principal(second, 1)


def test_principal_capability_example() -> None:
    scales = (4, 8, 16)
    assert cap.deletion_envelope(scales, 1) == 8
    assert cap.capability_is_principal(scales, 1)
    assert set(cap.capability_ideal(scales, 1)) == divisors(8)


def test_uniform_overlay_provenance_repair_distribution() -> None:
    assert cap.provenance_fiber_size(30) == 128
    assert cap.provenance_repair_distribution(30) == {
        1: 109,
        2: 5,
        3: 5,
        5: 5,
        6: 1,
        10: 1,
        15: 1,
        30: 1,
    }
    for m in range(2, 25):
        distribution = cap.provenance_repair_distribution(m)
        assert sum(distribution.values()) == cap.provenance_fiber_size(m)
        assert set(distribution) == divisors(m)
        assert all(count > 0 for count in distribution.values())


def test_small_families_against_direct_deletion_enumeration() -> None:
    values = (2, 3, 4, 5, 6)
    for scales in itertools.combinations(values, 3):
        for h in range(3):
            exact = cap.exact_reachable_gcds_bruteforce(scales, h)
            assert exact == cap.exact_reachable_gcds_by_closure(scales, h)
            envelope = 1
            for value in exact:
                envelope = envelope * value // gcd(envelope, value)
            assert envelope == cap.deletion_envelope(scales, h)
