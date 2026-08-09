from itertools import product

import pytest

from enterprise_math.p022_symmetry_quotient_repair import (
    barlow_orbit_edge_multiplicity,
    barlow_quotient_path_lift_count,
    equitable_transition_multiplicities,
    non_equitable_counterexample,
    quotient_path_lift_count,
)
from enterprise_math.p022_barlow_two_sided_repair import (
    two_sided_microscopic_fiber_size,
    unordered_absolute_pair_history,
)


def _words(length: int):
    return tuple(tuple(word) for word in product((-1, 1), repeat=length))


def test_barlow_orbit_edge_weights_are_exactly_one_two_or_four() -> None:
    reachable = {(0, 0)}
    for _ in range(6):
        nxt = set()
        for state in reachable:
            a, b = state
            for sa in (-1, 1):
                for sb in (-1, 1):
                    nxt.add(tuple(sorted((abs(a + sa), abs(b + sb)))))
        for left in reachable:
            a, b = left
            successors = {
                tuple(sorted((abs(a + sa), abs(b + sb))))
                for sa in (-1, 1)
                for sb in (-1, 1)
            }
            for right in successors:
                assert barlow_orbit_edge_multiplicity(left, right) in (1, 2, 4)
        reachable = nxt


def test_barlow_path_lift_product_matches_direct_microscopic_fibers() -> None:
    for length in range(0, 7):
        fibers = {}
        words = _words(length)
        for left in words:
            for right in words:
                history = unordered_absolute_pair_history(left, right)
                fibers.setdefault(history, 0)
                fibers[history] += 1
        for history, direct in fibers.items():
            assert barlow_quotient_path_lift_count(history) == direct
            assert barlow_quotient_path_lift_count(
                history
            ) == two_sided_microscopic_fiber_size(history)


def test_generic_equitable_path_lift_formula_matches_direct_path_enumeration() -> None:
    # Two vertices per orbit; every A vertex has two B continuations and every
    # B vertex has one C continuation.
    adjacency = {
        "a1": ("b1", "b2"),
        "a2": ("b1", "b2"),
        "b1": ("c1",),
        "b2": ("c2",),
        "c1": (),
        "c2": (),
    }
    block_of = {
        "a1": "A",
        "a2": "A",
        "b1": "B",
        "b2": "B",
        "c1": "C",
        "c2": "C",
    }
    multiplicities = equitable_transition_multiplicities(adjacency, block_of)
    assert multiplicities[("A", "B")] == 2
    assert multiplicities[("B", "C")] == 1
    assert quotient_path_lift_count(("A", "B", "C"), multiplicities) == 2

    # Fixed microscopic start a1 has exactly two A-B-C lifts.
    direct = 0
    for middle in adjacency["a1"]:
        for terminal in adjacency[middle]:
            if block_of[middle] == "B" and block_of[terminal] == "C":
                direct += 1
    assert direct == 2


def test_non_equitable_partition_has_no_representative_independent_edge_weight() -> None:
    adjacency, block_of = non_equitable_counterexample()
    with pytest.raises(ValueError, match="not equitable"):
        equitable_transition_multiplicities(adjacency, block_of)
