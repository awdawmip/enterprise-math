"""Exact Stage46 X6 single-Link absorbing-mask certificate (PREFIX-1002)."""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb
import json
from pathlib import Path

D = tuple(range(1, 7)) + tuple(range(-1, -7, -1))
O = (0,) * 6
E = (1, 0, 0, 0, 0, 0)


def shift(x, j):
    y = list(x)
    y[abs(j)-1] += 1 if j > 0 else -1
    return tuple(y)


def blocked(x, j):
    return (x == O and j == 1) or (x == E and j == -1)


def next_states(states, gate):
    y = defaultdict(int)
    for (x, h), a in states.items():
        for j in D:
            if gate and blocked(x, j):
                continue
            y[(shift(x, j), -j)] += a * (1 - 6 * int(h == j))
    return {s: a for s, a in y.items() if a}


def enumerate_words(n, gate):
    y = defaultdict(int)
    for word in product(D, repeat=n):
        x, h, a = O, -1, 1
        for j in word:
            if gate and blocked(x, j):
                break
            a *= 1 - 6 * int(h == j)
            x, h = shift(x, j), -j
        else:
            y[(x, h)] += a
    return {s: a for s, a in y.items() if a}


def A(m):
    a = [1] * (m+1)
    for _ in range(5):
        a = [sum(comb(k, j)**2 * a[k-j] for j in range(k+1))
             for k in range(m+1)]
    return a[m]


def score(s, n, grade):
    return Fraction(sum(a*a for (x, h), a in s.items()
                        if grade is None or sum(x) == grade), 36**n)


def check():
    full = gated = {(O, -1): 1}
    rows = []
    for n in range(1, 7):
        full, gated = next_states(full, False), next_states(gated, True)
        if n <= 3:
            assert full == enumerate_words(n, False)
            assert gated == enumerate_words(n, True)
        original = Fraction(6*A(n-1), 36**n)
        masked = Fraction(5 if n == 1 else 4*A(n-1)+6*A(n-2), 36**n)
        assert score(full, n, n) == original
        assert score(gated, n, n) == masked
        rows.append({"n": n, "full_outer": str(original),
                     "masked_outer": str(masked),
                     "masked_first_interior": str(score(gated, n, n-2)),
                     "masked_total": str(score(gated, n, None)),
                     "outer_ratio": str(masked/original)})
    ratios = {}
    for n in (10, 40, 100, 300):
        r = Fraction(2, 3) + Fraction(A(n-2), A(n-1))
        ratios[str(n)] = f"{float(r):.12f}"
        assert r > Fraction(25, 36)
    return {"schema": "PREFIX1002_X6_LINK_MASK_EXACT_V1",
            "initial_neighbour_port": "-e1",
            "closed_directed_arcs": ["0 -> e1", "e1 -> 0"],
            "local_kernel": "(1-6*[h=j])/6; no degree renormalization",
            "all_length_outer_n_ge_2": "[4*A6(n-1)+6*A6(n-2)]/36^n",
            "outer_n_1": "5/36", "asymptotic_ratio": "25/36",
            "verified_by_exact_DP_n": [1, 2, 3, 4, 5, 6],
            "independent_word_enumeration_n": [1, 2, 3],
            "rows": rows, "ratio_decimals": ratios,
            "review": "AUTHOR_CHECKED_NOT_INDEPENDENTLY_REVIEWED"}


if __name__ == "__main__":
    output = check()
    Path(__file__).with_name("PREFIX1002_R6_CERTIFICATE.json").write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, ensure_ascii=False))
