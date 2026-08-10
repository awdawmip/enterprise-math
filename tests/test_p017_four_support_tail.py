from itertools import combinations

import pytest

from enterprise_math.legendre import primes_up_to
from enterprise_math.p017_four_support_tail import (
    four_support_direct_mobius_tail,
    four_support_dual_graph,
    four_support_tail_certificate,
)


def test_known_k58_negative_witness_is_reconstructed() -> None:
    data = four_support_tail_certificate(58, [3, 5, 7, 11])
    assert data["support_product"] == 1155
    assert data["dual_threshold"] == 9
    assert data["active_vertices"] == (3, 5, 7)
    assert data["edges"] == ()
    assert data["positive_cycle_rank"] == 0
    assert data["negative_rank"] == 2
    assert data["empty_dual_correction"] == 0
    assert data["tail"] == -2
    assert data["direct_tail"] == -2


def test_empty_dual_graph_has_required_plus_one_correction() -> None:
    data = four_support_tail_certificate(271, [3, 5, 7, 13])
    assert data["support_product"] == 1365
    assert data["dual_threshold"] == 2
    assert data["active_vertices"] == ()
    assert data["edges"] == ()
    assert data["positive_cycle_rank"] == 0
    assert data["negative_rank"] == 0
    assert data["empty_dual_correction"] == 1
    assert data["tail"] == 1


def test_cycle_positive_example() -> None:
    data = four_support_tail_certificate(11, [3, 5, 7, 11])
    assert data["dual_threshold"] == 52
    assert data["active_vertices"] == (3, 5, 7, 11)
    assert data["edge_count"] == 4
    assert data["component_count"] == 1
    assert data["positive_cycle_rank"] == 1
    assert data["negative_rank"] == 0
    assert data["tail"] == 1


def test_dual_complex_is_always_a_graph() -> None:
    for k in (11, 20, 40, 80):
        primes = primes_up_to(k)
        for support in combinations(primes, 4):
            product = support[0] * support[1] * support[2] * support[3]
            if product <= 2 * k:
                continue
            data = four_support_dual_graph(k, list(support))
            u = int(data["dual_threshold"])
            for triple in combinations(support, 3):
                assert triple[0] * triple[1] * triple[2] > u


def test_graph_formula_matches_direct_mobius_tail_on_bounded_supports() -> None:
    for k in (11, 20, 40, 80):
        primes = primes_up_to(k)
        for support in combinations(primes, 4):
            product = support[0] * support[1] * support[2] * support[3]
            if product <= 2 * k:
                continue
            graph = four_support_dual_graph(k, list(support))
            direct = four_support_direct_mobius_tail(k, list(support))
            assert graph["tail"] == direct
            assert graph["tail"] == 1 - graph["vertex_count"] + graph["edge_count"]


def test_validation_rejects_wrong_supports() -> None:
    with pytest.raises(ValueError):
        four_support_dual_graph(10, [2, 3, 5])
    with pytest.raises(ValueError):
        four_support_dual_graph(10, [2, 3, 5, 5])
    with pytest.raises(ValueError):
        four_support_dual_graph(10, [2, 3, 5, 11])
    with pytest.raises(ValueError):
        four_support_dual_graph(20, [2, 3, 5, 7])
