#!/usr/bin/env python3
"""Exact checks for graph-coupled R5 optimum repair libraries.
Python 3.8+ standard library. Integer enumeration only.
"""
from itertools import combinations
import json
from pathlib import Path

PIN = "435e77af0d180eac32bd1f9c4c464bc4010b7551"
GAPS = (3, 2, 2, 3, 2, 1)
DL, DR = (0, 1, 3, 5), (0, 2, 4, 6)
HARD, LEFT, RIGHT = (1, 3, 4, 6), (1, 2, 3, 5), (1, 2, 4, 6)


def delta(a, b):
    return len(set(a) - set(b))


def optimum(mask):
    gaps = list(GAPS)
    if mask & 1:
        gaps[0] -= 1
    if mask & 2:
        gaps[3] -= 1
    points = [0]
    for gap in gaps:
        points.append(points[-1] + gap)
    best, family = None, []
    for centers in combinations(range(7), 4):
        distances = [min(abs(points[i] - points[j]) for j in centers)
                     for i in range(7)]
        if max(distances) > 2:
            continue
        val = sum(distances)
        if best is None or val < best:
            best, family = val, [centers]
        elif val == best:
            family.append(centers)
    return best, family


def neighbors(h, words, ell):
    return [h ^ (1 << i) for i in range(ell)
            if (h ^ (1 << i)) in words]


def optimal_library(words, ell):
    """Canonical min-size construction: parity + two cores on isolated words."""
    W = set(words)
    lib = []
    for h in sorted(W):
        if not neighbors(h, W, ell):
            lib.extend(((DL, h), (DR, h)))
        else:
            lib.append((DL if h.bit_count() % 2 == 0 else DR, h))
    return lib


def covers(family, words, lib, radius):
    return all(any(delta(c, d) + (h ^ j).bit_count() <= radius
                   for d, j in lib)
               for c in family for h in words)


def graph_stats(words, ell):
    W = set(words)
    iso = sum(not neighbors(h, W, ell) for h in W)
    return len(W), iso, len(W) + iso


def no_adjacent_ones(ell):
    return [h for h in range(1 << ell) if h & (h >> 1) == 0]


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def main():
    opts = [optimum(mask) for mask in range(4)]
    assert [v for v, _ in opts] == [5] * 4
    assert [len(f) for _, f in opts] == [5, 12, 9, 17]
    G0, Ga, Gb, Gab = [f for _, f in opts]
    assert [delta(HARD, d) for d in G0] == [3, 2, 3, 3, 2]
    for new in (Ga, Gab):
        assert all(c in new for c in (HARD, LEFT, RIGHT))
        assert [d for d in G0 if delta(HARD, d) <= 2] == [DL, DR]
        assert (delta(LEFT, DL), delta(LEFT, DR)) == (1, 3)
        assert (delta(RIGHT, DL), delta(RIGHT, DR)) == (3, 1)
        assert all(delta(c, d) >= 1
                   for c in (LEFT, RIGHT) for d in G0)
        assert not any(all(delta(c, d) <= 2 for c in (HARD, LEFT, RIGHT))
                       for d in G0)
        assert all(delta(c, DL) <= 1 or delta(c, DR) <= 1
                   or (delta(c, DL) == 2 and delta(c, DR) == 2)
                   for c in new)
    b_left, b_right = (0, 1, 3, 6), (0, 1, 4, 6)
    assert [d for d in G0 if delta(b_left, d) <= 1] == [DL]
    assert [d for d in G0 if delta(b_right, d) <= 1] == [DR]
    assert all(min(delta(c, DL), delta(c, DR)) <= 1 for c in Gb)

    exhaustive = []
    for ell in range(4):
        all_words = list(range(1 << ell))
        subset_masks = [1] if ell == 0 else range(1, 1 << (1 << ell))
        checks, with_isolates = 0, 0
        minimum, maximum = 10 ** 9, 0
        for subset in subset_masks:
            X = [h for h in all_words if (subset >> h) & 1]
            count, isolated, predicted = graph_stats(X, ell)
            L = optimal_library(X, ell)
            assert len(L) == predicted
            assert covers(Ga, X, L, 2)
            assert covers(Gab, X, L, 2)
            B = [(DL, h) for h in X] + [(DR, h) for h in X]
            assert len(B) == 2 * count and covers(Gb, X, B, 1)
            checks += 1
            with_isolates += bool(isolated)
            minimum = min(minimum, predicted)
            maximum = max(maximum, predicted)
        exhaustive.append({"ell": ell, "nonempty_languages": checks,
                           "languages_with_isolates": with_isolates,
                           "min_kappa_a_ab": minimum,
                           "max_kappa_a_ab": maximum})

    fibonacci_rows = []
    for ell in range(1, 16):
        X = no_adjacent_ones(ell)
        count, isolated, predicted = graph_stats(X, ell)
        assert count == fibonacci(ell + 2)
        assert isolated == 0 and predicted == count
        fibonacci_rows.append({"ell": ell, "suffixes": count,
                               "kappa_a_ab": predicted,
                               "kappa_b": 2 * count})
    for ell in range(1, 9):
        X = no_adjacent_ones(ell)
        assert covers(Ga, X, optimal_library(X, ell), 2)
        assert covers(Gab, X, optimal_library(X, ell), 2)

    assert graph_stats([0, 7], 3) == (2, 2, 4)
    assert covers(Ga, [0, 7], optimal_library([0, 7], 3), 2)
    assert covers(Gab, [0, 7], optimal_library([0, 7], 3), 2)

    result = {
        "status": "PASS_R5_GRAPH_COUPLED_SUFFIX_EXACT_ADVICE",
        "frozen_science_pin": PIN,
        "model": "one-dimensional indexed-center covering with extra shared suffix-compatibility X",
        "exact_theorem": "kappa_a(X,2)=kappa_ab(X,2)=|X|+isolates(X); kappa_b(X,1)=2|X|; kappa_0(X,0)=5|X|",
        "all_lengths_proof_depends_on": "inherited optimizer-product lemma + exhaustively checked 7-event core certificate",
        "finite_coverage": "all 274 nonempty X at ell=0..3, Fibonacci ell=1..15, direct repair coverage Fibonacci ell=1..8",
        "core_optimum_costs": [v for v, _ in opts],
        "core_family_sizes": [len(f) for _, f in opts],
        "exhaustive_languages": exhaustive,
        "fibonacci_languages": fibonacci_rows,
        "isolated_example": {"ell": 3, "X": ["000", "111"], "kappa_a_ab": 4},
    }
    out = Path(__file__).with_name("EXACT_GRAPH_COUPLED_SUFFIX_EVIDENCE.json")
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2,
                              sort_keys=True) + "\n", encoding="utf-8")
    print(result["status"])
    print("checked X counts:", [(x["ell"], x["nonempty_languages"])
                                for x in exhaustive])
    print("Fibonacci sample:", [(x["ell"], x["suffixes"])
                               for x in fibonacci_rows[:9]])
    print("result:", out)


if __name__ == "__main__":
    main()
