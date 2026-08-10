from __future__ import annotations

import itertools
import sys
from math import gcd
from pathlib import Path

EXPERIMENTS = Path(__file__).parents[1] / "experiments"
sys.path.insert(0, str(EXPERIMENTS))

import r007_overlap_prime_bridge as bridge
import r007_residue_extension_csp as base


def smallest_prime_factor(n: int) -> int:
    for d in range(2, n + 1):
        if n % d == 0:
            return d
    raise AssertionError


def test_pressure_kernel_compiles_hull_and_is_idempotent() -> None:
    for r in range(2, 6):
        kernel = bridge.naturality_kernel(r)
        assert bridge.kernel_is_idempotent(kernel)
        for f in itertools.product(range(r), repeat=r):
            assert bridge.hull_from_kernel(f, kernel) == base.natural_hull(f, r)


def test_prime_scale_still_has_nondivisor_global_constraints() -> None:
    f = (0, 0, 0, 1, 2)
    assert base.path_nonexpansive(f)
    assert base.internally_coherent(f, 5)
    assert not base.globally_extendable(f, 5)
    assert base.natural_hull(f, 5) == (0, 0, 1, 1, 2)


def test_uniform_leaf_pruning_and_euclidean_gap_recursion() -> None:
    for d in range(2, 15):
        for e in range(d + 1, 30):
            if gcd(d, e) != 1:
                continue
            q, s, residual = bridge.uniform_leaf_pruning_signature(d, e)
            assert e == q * d + s
            assert residual == bridge.fine_side_leaf_multiplicities(d, d + s)
            a, t, epsilon = bridge.euclidean_gap_recursion(d, s)
            assert d == a * s + t
            assert set(epsilon) <= {0, 1}
            assert sum(epsilon) == t


def test_multiscale_nerve_has_gcd_components_and_expected_f_vector() -> None:
    families = [(6, 10, 15), (4, 6, 10), (6, 9, 15), (2, 3, 5), (8, 12, 18)]
    for scales in families:
        g = bridge.gcd_many(scales)
        assert bridge.multiscale_overlap_component_count(scales) == g
        assert bridge.multiscale_nerve_euler_characteristic(scales) == g
    assert bridge.multiscale_simplex_counts((6, 10, 15)) == (31, 52, 22)
    assert [
        base.overlap_component_count(a, b)
        for a, b in ((6, 10), (6, 15), (10, 15))
    ] == [2, 3, 5]
    assert bridge.multiscale_overlap_component_count((6, 10, 15)) == 1


def test_first_disconnect_scale_is_smallest_prime_factor() -> None:
    for n in range(2, 60):
        expected = smallest_prime_factor(n)
        assert bridge.first_disconnect_scale(n) == expected
        assert bridge.prime_by_lower_scale_connectivity(n) == (expected == n)
