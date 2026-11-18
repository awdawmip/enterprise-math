#!/usr/bin/env python3
"""Exact, finite, source-line faithful check for an X6 triad midpoint helper.

Source line focus: experiments/x6_triadic_atomic_scatter_v1_20260906/
check_triadic_atomic_scatter.py:54-57 (Git blob d5f6dfcfd0dedbe46feae3bc1b227185af417c2f).
Native BRC formulas mirror pinned signed_brc.py blob
300a96e3dc24bf6fff73743037a0347a8bc83176.
The tested current source's 160 triad cases are only unit vectors at ZERO.
"""
from itertools import combinations, product
from math import factorial
import json

N = 6
ZERO = (0,) * N

def add(a, b): return tuple(x + y for x, y in zip(a, b))
def sub(a, b): return tuple(x - y for x, y in zip(a, b))
def l1(a): return sum(abs(x) for x in a)
def unit(i, s=1): return tuple(s if j == i else 0 for j in range(N))
def step(a, i, s):
    b = list(a); b[i] += s; return tuple(b)

def shortest_event_count(z): return l1(z)
def shortest_path_multiplicity(z):
    n = l1(z)
    ans = factorial(n)
    for v in z: ans //= factorial(abs(v))
    return ans

def midpoint_options_source(a, b):
    # Exact executable contents of source lines 54-57, with brc methods inlined.
    if shortest_event_count(sub(b, a)) != 2:
        raise ValueError("outside checked native two-step domain")
    if shortest_path_multiplicity(sub(b, a)) != 2:
        raise ValueError("outside checked native two-path domain")
    return (ZERO, add(a, b))

def true_shortest_midpoints(a, b):
    d = sub(b, a)
    assert shortest_event_count(d) == 2
    assert shortest_path_multiplicity(d) == 2
    idx = [j for j, v in enumerate(d) if v]
    return frozenset(step(a, i, d[i]) for i in idx)

def require(x, message):
    if not x: raise RuntimeError(message)

# Exact original caller at lines 63-70: starts are mapped by a signed triad rotation.
def q_triad(T):
    i, j, k = T
    g = list(range(1, N + 1))
    g[i] = -(j + 1); g[j] = -(k + 1); g[k] = -(i + 1)
    return tuple(g)

def act(g, z):
    out = [0] * N
    for i, c in enumerate(z):
        if c:
            y = g[i]
            out[abs(y) - 1] += (1 if y > 0 else -1) * c
    return tuple(out)

caller_pairs = 0
for T in combinations(range(N), 3):
    g = q_triad(T)
    for signs in product((-1, 1), repeat=3):
        starts = [unit(i, s) for i, s in zip(T, signs)]
        targets = [act(g, a) for a in starts]
        for a, b in zip(starts, targets):
            require(frozenset(midpoint_options_source(a, b)) ==
                    true_shortest_midpoints(a, b), "original caller mismatch")
            caller_pairs += 1
require(caller_pairs == 480, "triad caller case count")

# Independently enumerate all legal two-axis two-step inputs in a bounded chart.
cases = equal = unequal = theorem_errors = 0
witness = None
for a in product((-1, 0, 1), repeat=N):
    for i, j in combinations(range(N), 2):
        for si, sj in product((-1, 1), repeat=2):
            b = step(step(a, i, si), j, sj)
            require(shortest_event_count(sub(b, a)) == 2 and
                    shortest_path_multiplicity(sub(b, a)) == 2,
                    "invalid generated precondition")
            actual = frozenset(midpoint_options_source(a, b))
            truth = true_shortest_midpoints(a, b)
            correct = actual == truth
            expected = (l1(a) == 1 and l1(b) == 1)
            if correct != expected: theorem_errors += 1
            cases += 1
            if correct: equal += 1
            else:
                unequal += 1
                if witness is None and a == (1, 0, 1, 0, 0, 0) and b == (0, 1, 1, 0, 0, 0):
                    witness = {"a": a, "b": b,
                               "native_shortest_length": 2,
                               "native_shortest_brc": 2,
                               "original": sorted(actual),
                               "correct": sorted(truth)}
require(theorem_errors == 0, "iff theorem counterexample")
require(cases == 43740 and equal == 120 and unequal == 43620, "census mismatch")
require(witness is not None, "missing explicit off-anchor witness")
print(json.dumps({
    "schema": "EM_X6_UNIT126_TRANSLATION_MIDPOINT_EXACT_CENSUS_V1",
    "source_code_blob_sha1": "d5f6dfcfd0dedbe46feae3bc1b227185af417c2f",
    "native_brc_blob_sha1": "300a96e3dc24bf6fff73743037a0347a8bc83176",
    "scope": "all six-component a in {-1,0,1}^6; 15 named axis pairs; 4 signed displacements per pair",
    "tested_source_triad_pairs": caller_pairs,
    "all_valid_two_step_pairs": cases,
    "original_midpoints_correct": equal,
    "original_midpoints_wrong": unequal,
    "exact_iff_violations": theorem_errors,
    "counterexample": witness,
    "full_source_import_executed": False,
    "original_R063_benchmark_executed": False,
    "status": "AUTHOR_EXACT_FINITE_CHECK_UNREVIEWED"
}, sort_keys=True, separators=(',', ':')))
