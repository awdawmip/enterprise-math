from __future__ import annotations

import itertools
import sys
from fractions import Fraction
from math import gcd, lcm
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


def test_component_quotient_is_the_canonical_gcd_scale_object() -> None:
    families = [(6, 10, 15), (8, 12, 18), (6, 9, 15), (4, 6, 10), (12, 18, 30)]
    for scales in families:
        g = bridge.gcd_many(scales)
        projection = bridge.multiscale_meet_projection(scales)
        components = bridge.multiscale_overlap_components(scales)
        assert len(components) == g
        labels = []
        for component in components:
            component_labels = {projection[cell] for cell in component}
            assert len(component_labels) == 1
            labels.append(next(iter(component_labels)))
        assert sorted(labels) == list(range(g))
        for d in scales:
            expected = tuple(i // (d // g) for i in range(d))
            actual = tuple(projection[(d, i)] for i in range(d))
            assert actual == expected


def test_metric_atom_denominators_recover_lcm_join() -> None:
    values = range(2, 13)
    for size in range(1, 5):
        for scales in itertools.combinations(values, size):
            expected = lcm(*scales)
            assert bridge.metric_join_scale(scales) == expected
            assert bridge.meet_join_signature(scales) == (gcd(*scales), expected)


def test_metric_join_examples_do_not_require_uniform_atom_lengths() -> None:
    assert set(bridge.atomic_interval_lengths((6, 10, 15))) == {
        Fraction(1, 30),
        Fraction(1, 15),
    }
    assert bridge.metric_join_scale((6, 10, 15)) == 30
    assert bridge.metric_join_scale((4, 6, 10)) == 60
    assert bridge.metric_join_scale((8, 12, 18)) == 72


def test_unlabeled_overlay_retains_join_but_loses_meet_provenance() -> None:
    # The 2-grid is already contained in the 6-grid. Forgetting layer identity
    # therefore makes these states geometrically identical, even though their
    # common-scale meet differs.
    one_layer = (6,)
    two_layers = (2, 6)
    assert bridge.overlaid_grid_boundaries(one_layer) == bridge.overlaid_grid_boundaries(two_layers)
    assert bridge.atomic_interval_lengths(one_layer) == bridge.atomic_interval_lengths(two_layers)
    assert bridge.metric_join_scale(one_layer) == bridge.metric_join_scale(two_layers) == 6
    assert bridge.gcd_many(one_layer) == 6
    assert bridge.gcd_many(two_layers) == 2


def test_first_disconnect_scale_is_smallest_prime_factor() -> None:
    for n in range(2, 60):
        expected = smallest_prime_factor(n)
        assert bridge.first_disconnect_scale(n) == expected
        assert bridge.prime_by_lower_scale_connectivity(n) == (expected == n)
