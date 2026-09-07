"""Owner's independent finite checks of the new path and arithmetic consumers.

Uses an unsigned carry matrix plus signed inclusion-exclusion, independently of
the production active-axis/BRC transfer. Path checks target observer contracts.
This is a research audit, not a canonical registration or a general proof.
"""
from collections import Counter
from dataclasses import replace
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from math import comb
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / "src"),
               str(ROOT / "experiments/owner_path_monitor_20260907")]
from enterprise_math.brc_histogram import WeightHistogram
from owner_arithmetic_20260907 import signed_valuation_spectrum
from path_monitor import (ALPHABET, HIT, START, MONITOR_STATES, Edge, Node,
                          NativeGraph, port_excursion_series, compose_port_series,
                          verify_port_series)
from examples import blind_pair, branching_hidden_cycle_graph


def word_hit(initial, suffix):
    if initial == HIT:
        return True
    word = tuple(suffix) if initial == START else (initial,) + tuple(suffix)
    return any(a == -b for a, b in zip(word, word[1:]))


def path_checks():
    # Myhill-Nerode lower bound checked from words, with no monitor transitions.
    suffixes = [()] + [(step,) for step in ALPHABET]
    pair_count = 0
    for left, right in combinations(MONITOR_STATES, 2):
        assert any(word_hit(left, word) != word_hit(right, word) for word in suffixes)
        pair_count += 1

    graph = NativeGraph(
        (Node("P", (0,) * 6), Node("A", (1, 0, 0, 0, 0, 0))),
        (Edge("a", "P", "A", 1, Fraction(1)),
         Edge("b", "P", "A", 1, Fraction(1, 2)),
         Edge("c", "P", "A", 1, Fraction(1, 2)),
         Edge("return", "A", "P", -1, Fraction(1))),
    )
    walks = compose_port_series(port_excursion_series(graph, ("P",), 4))
    assert verify_port_series(graph, ("P",), 4, walks)["status"] == "VERIFIED"
    key = ("P", "P", 2, START, HIT)
    original = walks.coefficients[key]
    forged = WeightHistogram.from_weights([1, Fraction(3, 4), Fraction(1, 4)])
    cwm = lambda h: (h.count, h.total_mass, h.dominant_mass)
    assert cwm(original) == cwm(forged) and original != forged
    changed = dict(walks.coefficients)
    changed[key] = forged
    assert verify_port_series(graph, ("P",), 4, replace(walks, coefficients=changed))["status"] == "REJECTED"

    # Relabel the six signed axes and change the raw anchor. This is an input
    # transformation, not a claim that any new physical rotation law holds.
    transformed_cases = 0
    graphs = (*blind_pair(), branching_hidden_cycle_graph())
    for source_graph in graphs:
        expected = compose_port_series(port_excursion_series(source_graph, ("P",), 6))
        for shift in (0, 1, 3, 5):
            def step_map(step):
                if step in (START, HIT):
                    return step
                old = abs(step) - 1
                return (1 if step > 0 else -1) * (-1 if old % 2 else 1) * ((old + shift) % 6 + 1)

            def coordinate_map(coordinate):
                result = [10 + i for i in range(6)]
                for old, value in enumerate(coordinate):
                    result[(old + shift) % 6] += (-1 if old % 2 else 1) * value
                return tuple(result)

            transformed = NativeGraph(
                tuple(Node(node.label, coordinate_map(node.coordinate)) for node in source_graph.nodes),
                tuple(Edge(edge.label, edge.source, edge.target, step_map(edge.step), edge.weight)
                      for edge in source_graph.edges),
            )
            got = compose_port_series(port_excursion_series(transformed, ("P",), 6))
            mapped = {(s, t, length, step_map(initial), step_map(final)): histogram
                      for (s, t, length, initial, final), histogram in expected.coefficients.items()}
            assert got.coefficients == mapped
            assert verify_port_series(transformed, ("P",), 6, got)["status"] == "VERIFIED"
            assert verify_port_series(transformed, ("P",), 6, expected)["status"] == "REJECTED"
            transformed_cases += 1
    return {"pairwise_suffix_separations": pair_count,
            "same_CWM_different_histogram_forgery": "REJECTED",
            "signed_frame_and_anchor_cases": transformed_cases}


def bounded_digit_count(width, total, prime):
    """Count labeled bounded compositions by stars-and-bars inclusion-exclusion."""
    if width == 0:
        return int(total == 0)
    if total < 0:
        return 0
    return sum((-1)**j * comb(width, j) * comb(total - prime*j + width - 1, width - 1)
               for j in range(min(width, total // prime) + 1))


def unsigned_spectrum(radius, prime, width):
    if width == 0:
        return {0: 1} if radius == 0 else {}
    digits = []
    remaining = radius
    while remaining:
        remaining, digit = divmod(remaining, prime)
        digits.append(digit)
    states = {(0, 0): 1}
    for digit in digits or [0]:
        following = Counter()
        for (carry, exponent), count in states.items():
            for outgoing in range(width):
                ways = bounded_digit_count(width, digit + prime*outgoing - carry, prime)
                if ways:
                    assert ways > 0
                    following[outgoing, exponent + outgoing] += count * ways
        states = following
    return {exponent: count for (carry, exponent), count in states.items() if carry == 0}


def arithmetic_checks():
    cases = []
    for radius in (0, 4, 11, 31, 64, 257, 1000001):
        for prime in (2, 3, 7):
            lifted = Counter()
            for width in range(7):
                coefficient = comb(6, width) * (-1)**(6-width) * 2**width
                for exponent, count in unsigned_spectrum(radius, prime, width).items():
                    lifted[exponent] += coefficient * count
            independent = {e: count for e, count in lifted.items() if count}
            assert all(count > 0 for count in independent.values())
            actual = signed_valuation_spectrum(radius, prime).valuation_counts()
            assert actual == independent
            cases.append({"N": radius, "p": prime, "bins": len(actual)})
    # With N<p no numerator factorial contains p. Check the upper default p.
    count = sum(2**r * comb(6, r) * comb(29, r-1) for r in range(1, 7))
    assert signed_valuation_spectrum(30, 31).valuation_counts() == {0: count}
    return {"independent_unsigned_matrix_lifting_cases": cases,
            "N_less_than_p_boundary": "PASS",
            "independence": "No active-axis state, BRC multiplication, or digit coefficient convolution in oracle"}


def main():
    paths = ["experiments/owner_path_monitor_20260907/path_monitor.py",
             "experiments/owner_path_monitor_20260907/test_path_monitor.py",
             "research_notes/owner_arithmetic_20260907.py",
             "research_notes/OWNER_ARITHMETIC_FRONTIER_20260907.md"]
    before = {path: sha256((ROOT / path).read_bytes()).hexdigest() for path in paths}
    output = {"status": "PASS", "path": path_checks(), "arithmetic": arithmetic_checks(),
              "source_sha256": before,
              "scope": "independent finite implementation checks; general proofs audited separately"}
    assert before == {path: sha256((ROOT / path).read_bytes()).hexdigest() for path in paths}
    destination = Path(__file__).with_suffix(".json")
    destination.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(output, ensure_ascii=False))


if __name__ == "__main__":
    main()
