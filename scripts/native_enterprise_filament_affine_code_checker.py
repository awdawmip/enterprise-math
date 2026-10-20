#!/usr/bin/env python3
"""Exact checker for the curvature-flattened affine global-island code."""

from __future__ import annotations

import math
from collections import Counter

EXCEPTIONAL_K9 = {
    (11, 1): {0: 51, 1: 47, 2: 18, 3: 4, 4: 1},
    (11,-1): {0: 51, 1: 47, 2: 18, 3: 4, 4: 1},
    (13, 1): {0: 84, 1: 57, 2: 24, 3: 4},
    (13,-1): {0: 85, 1: 54, 2: 27, 3: 3},
    (23, 1): {0: 354, 1: 147, 2: 24, 3: 4},
    (23,-1): {0: 353, 1: 149, 2: 24, 3: 2, 4: 1},
    (31, 1): {0: 716, 1: 213, 2: 30, 3: 2},
    (31,-1): {0: 716, 1: 213, 2: 30, 3: 2},
    (53, 1): {0: 2366, 1: 411, 2: 30, 3: 2},
    (53,-1): {0: 2366, 1: 411, 2: 30, 3: 2},
}


def eta(j: int, chi: int, modulus: int) -> int:
    return ((3*j*j + (chi if j % 2 else 0)) * pow(2, -1, modulus)) % modulus


def word(k: int, q: int, chi: int, a: int, b: int) -> tuple[int, ...]:
    return tuple((a + b*j + eta(j, chi, q)) % q for j in range(k))


def zero_spectrum(k: int, modulus: int, chi: int) -> dict[int, int]:
    point_mult = Counter()
    for j in range(k):
        off = eta(j, chi, modulus)
        for r in range(modulus):
            c = (-3*j*r - off) % modulus
            point_mult[(r,c)] += 1
    out = Counter(point_mult.values())
    out[0] = modulus*modulus - len(point_mult)
    return dict(sorted(out.items()))


def generic_spectrum(k: int, m: int) -> dict[int, int]:
    return {
        0: m*m - k*m + math.comb(k,2),
        1: k*(m-k+1),
        2: math.comb(k,2),
    }


def distance_checks() -> None:
    q = 59
    for k in range(3,10):
        min_same = k
        for da in range(q):
            for db in range(q):
                if da == db == 0:
                    continue
                zeros = sum((da + db*j) % q == 0 for j in range(k))
                min_same = min(min_same, k-zeros)
        assert min_same == k-1

        min_cross = k
        for da in range(q):
            for db in range(q):
                zeros = sum((da + db*j + (j % 2)) % q == 0 for j in range(k))
                min_cross = min(min_cross, k-zeros)
        assert min_cross == k//2

        for chi in (1,-1):
            v = word(k,q,chi,17,23)
            for j in range(k-2):
                got = (v[j] - 2*v[j+1] + v[j+2]) % q
                expected = (3 - chi*((-1)**j)) % q
                assert got == expected


def endpoint_information_check() -> None:
    q=59
    for k in range(3,10):
        for chi in (1,-1):
            seen={}
            for a in range(q):
                for b in range(q):
                    v=word(k,q,chi,a,b)
                    key=(v[0],v[-1])
                    assert key not in seen
                    seen[key]=(a,b)
            assert len(seen)==q*q


def generic_weight_checks() -> None:
    test_primes = {3:5, 4:7, 5:7, 6:29, 7:29, 8:59, 9:59}
    for k,q in test_primes.items():
        for chi in (1,-1):
            assert zero_spectrum(k,q,chi) == generic_spectrum(k,q)


def exceptional_and_padic_checks() -> None:
    for (q,chi), expected in EXCEPTIONAL_K9.items():
        assert zero_spectrum(9,q,chi) == expected
        q2=q*q
        assert zero_spectrum(9,q2,chi) == generic_spectrum(9,q2)


def main() -> None:
    distance_checks()
    endpoint_information_check()
    generic_weight_checks()
    exceptional_and_padic_checks()
    print("FIXED_MODE_AFFINE_MDS_DISTANCE=PASS k=3..9")
    print("TWO_MODE_COSET_UNION_DISTANCE=floor(k/2)")
    print("ENDPOINT_INFORMATION_SETS=PASS k=3..9")
    print("GENERIC_WEIGHT_SPECTRA=PASS")
    print("K9_EXCEPTIONAL_Q={11,13,23,31,53}")
    print("K9_EXCEPTIONAL_CONCURRENCES_DESINGULARIZE_AT_Q_SQUARED=PASS")


if __name__ == "__main__":
    main()
