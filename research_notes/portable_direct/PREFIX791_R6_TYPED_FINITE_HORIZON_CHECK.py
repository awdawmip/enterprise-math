#!/usr/bin/env python3
"""PREFIX-791 exact finite-horizon typed continuation regression.

Scientific scope: finite typed labelled integer-weight multigraphs with
nonnegative integer terminal multiplicities. Uses standard-library integers.
No native X6 admission or physical event is inferred.
"""
from collections import defaultdict
from itertools import product
from random import Random
import json

ALPHABET = ("port-a", "port-b")
MODULI = (2, 3, 5, 6, 7)


def project(hist, modulus):
    out = defaultdict(int)
    for w, count in hist.items():
        out[w % modulus] += count
    return {w: c for w, c in out.items() if c}


def initial(terminal):
    return [{0: c} if c else {} for c in terminal]


def prepend(graph, vector, label, modulus=None):
    n = len(graph)
    out = []
    for s in range(n):
        accum = defaultdict(int)
        for a, t, w in graph[s]:
            if a == label:
                for tail_w, c in vector[t].items():
                    total = w + tail_w
                    if modulus is not None:
                        total %= modulus
                    accum[total] += c
        out.append(dict(accum))
    return out


def all_word_vectors(graph, terminal, depth, modulus=None):
    level = {(): initial(terminal)}
    result = dict(level)
    for _ in range(depth):
        next_level = {}
        for word, vec in level.items():
            for label in ALPHABET:
                next_level[(label,) + word] = prepend(graph, vec, label, modulus)
        result.update(next_level)
        level = next_level
    return result


def signatures_agree(vectors, i, j, depth):
    return all(vec[i] == vec[j] for word, vec in vectors.items() if len(word) <= depth)


def one_case(graph, terminal, stats):
    n = len(graph)
    horizon = n - 1
    probe_depth = n + 2
    exact = all_word_vectors(graph, terminal, probe_depth)
    mods = {m: all_word_vectors(graph, terminal, probe_depth, m) for m in MODULI}
    for m, mv in mods.items():
        for word, values in exact.items():
            for s, hist in enumerate(values):
                assert project(hist, m) == mv[word][s]
                stats["projection_checks"] += 1
    for i in range(n):
        for j in range(i + 1, n):
            if signatures_agree(exact, i, j, horizon):
                assert signatures_agree(exact, i, j, probe_depth)
                stats["integer_horizon_matches"] += 1
            for m, mv in mods.items():
                if signatures_agree(mv, i, j, horizon):
                    assert signatures_agree(mv, i, j, probe_depth)
                    stats["residue_horizon_matches"] += 1
            stats["pair_tests"] += 1
    stats["cases"] += 1


def run():
    stats = {"cases": 0, "projection_checks": 0, "pair_tests": 0,
             "integer_horizon_matches": 0, "residue_horizon_matches": 0}
    # Exhaustive binary two-state one-label edge patterns, including dead states.
    for mask in range(16):
        for terminal in product((0, 1), repeat=2):
            graph = [[("port-a", j, 0) for j in range(2) if mask & (1 << (2*i+j))]
                     for i in range(2)]
            one_case(graph, terminal, stats)
    rng = Random(79120261115)
    for _ in range(512):
        n = rng.randrange(2, 6)
        graph = [[] for _ in range(n)]
        for s in range(n):
            for a in ALPHABET:
                for _ in range(rng.randrange(3)):
                    graph[s].append((a, rng.randrange(n), rng.randrange(-3, 4)))
        terminal = [rng.randrange(3) for _ in range(n)]
        one_case(graph, terminal, stats)
    # Exact witness for current-readout equality, future Port inequality.
    witness = [[("port-a", 0, 0)], []]
    vv = all_word_vectors(witness, [1, 1], 1)
    assert vv[()][0] == vv[()][1] == {0: 1}
    assert vv[("port-a",)][0] == {0: 1}
    assert vv[("port-a",)][1] == {}
    stats["witness"] = {"states": 2, "depth_zero_equal": True,
        "port_a_length_one_counts": [vv[("port-a",)][0], vv[("port-a",)][1]]}
    stats["source_pin"] = "awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d"
    stats["method"] = "EXACT_INTEGER_LAURENT_HISTOGRAM_DYNAMIC_PROGRAMMING"
    stats["scope"] = "external finite typed multigraph, nonnegative integer terminal counts, signed integer weights, finite alphabet; random checks are regressions, universal theorem is algebraic"
    stats["theorem"] = "n-1 word depth sufficient for all finite words for exact integer or exact residue-weight histograms, by field linear span and m-th root decomposition"
    print(json.dumps(stats, indent=2, sort_keys=True))
    print("ALL_CHECKS_PASS PREFIX791 FINITE_HORIZON_TYPED_RESIDUAL")


if __name__ == "__main__":
    run()
