from __future__ import annotations

import importlib.util
import itertools
from math import gcd
from pathlib import Path


MODULE_PATH = Path(__file__).parents[1] / "experiments" / "r007_residue_extension_csp.py"
spec = importlib.util.spec_from_file_location("r007_residue_extension_csp", MODULE_PATH)
assert spec is not None and spec.loader is not None
csp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(csp)


def test_overlap_graph_recovers_gcd_and_component_profile() -> None:
    for d in range(1, 20):
        for e in range(1, 20):
            g = gcd(d, e)
            assert csp.overlap_component_count(d, e) == g
            assert csp.overlap_edge_count(d, e) == d + e - g
            profile = (d // g, e // g, d // g + e // g - 1)
            assert csp.overlap_component_profiles(d, e) == [profile] * g


def test_coprime_overlap_graph_is_caterpillar() -> None:
    for d in range(1, 15):
        for e in range(1, 15):
            if gcd(d, e) == 1:
                assert csp.coprime_overlap_is_caterpillar(d, e)


def test_overlap_relation_is_minmax_closed() -> None:
    for d in range(1, 10):
        for e in range(1, 10):
            assert csp.overlap_relation_minmax_closed(d, e)


def test_pair_compatibility_is_colored_overlap_graph_endomorphism() -> None:
    identity3 = (0, 1, 2)
    identity2 = (0, 1)
    assert csp.pair_compatible(identity3, 3, identity2, 2)
    bad3 = (0, 2, 2)
    assert not csp.pair_compatible(bad3, 3, identity2, 2)


def test_farey_bridge_dominance_small_levels() -> None:
    for n in range(2, 9):
        assert csp.bridge_dominance_holds(n)


def test_prime_internal_freedom_small_scales() -> None:
    for r in (2, 3, 5):
        assert all(csp.internally_coherent(f, r) for f in itertools.product(range(r), repeat=r))
    for r, d in ((4, 2), (6, 2), (8, 2)):
        block = r // d
        witness = [0] * r
        witness[1] = block
        assert not csp.internally_coherent(witness, r)


def test_prime_power_internal_count_formula() -> None:
    assert csp.prime_power_internal_count(2, 1) == 4
    assert csp.prime_power_internal_count(2, 2) == 64
    assert csp.prime_power_internal_count(2, 3) == 16384
    assert csp.prime_power_internal_count(3, 1) == 27


def test_p_adic_valuation_is_component_saturation_depth() -> None:
    for n in range(2, 50):
        for p in (2, 3, 5, 7):
            valuation = csp.p_adic_valuation(n, p)
            for k in range(0, 6):
                assert csp.prime_power_component_signature(n, p, k) == p ** min(valuation, k)


def test_arc_consistency_is_exact_and_cutoff_is_r() -> None:
    expected = {2: 4, 3: 17, 4: 40, 5: 195, 6: 182}
    for r, count in expected.items():
        survivors = csp.finite_prefix_image(r, r)
        assert len(survivors) == count
        assert all(csp.globally_extendable(f, r) for f in survivors)


def test_every_compatible_prefix_constructively_extends() -> None:
    for r in range(2, 7):
        for f in csp.finite_prefix_image(r, r):
            family = csp.finite_prefix_completion(f, r, r)
            assert family is not None
            extended = csp.extend_family_through(family, r + 3)
            assert csp.family_compatible(extended)
            assert extended[r] == f
