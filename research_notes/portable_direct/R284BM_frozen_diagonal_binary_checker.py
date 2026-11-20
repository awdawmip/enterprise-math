"""R284BM: exhaustive 3x3 binary frozen-diagonal classification and modular certificates.
Python >=3.9, standard library only. All work is exact integer/fraction arithmetic.
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
from math import isqrt
import json

CANDIDATES = list(product((1, 2), repeat=9))
MODULUS = 13604881
DELTA = 3
FIXTURES = (
    (0, 5, (5, 6533875, 4219379), (912295, 3441724), 644,
     "b1919f8cf74c3b6a8f3477e1776752b0e4f4b70986f8c424e593b97cc87b3868"),
    (1, 8, (2134880, 8, 7707204), (8299942, 5571858), 7,
     "5836687c68b8434cce8d8aa2458a2cb0604c699d3dd39151eb5e3b4d9c8c5c1e"),
    (2, 8, (7506413, 9793806, 8), (7755770, 3250345), 7,
     "61492b0d7ff2692094671ac1f9a7c2c3a786297c885ef4a310db2644ddf7991b"),
)


def det3(a):
    x, y, z = a
    return (x[0] * (y[1]*z[2]-y[2]*z[1])
            - x[1] * (y[0]*z[2]-y[2]*z[0])
            + x[2] * (y[0]*z[1]-y[1]*z[0]))


def det3_perm(a):
    return (a[0][0]*a[1][1]*a[2][2]
            + a[0][1]*a[1][2]*a[2][0]
            + a[0][2]*a[1][0]*a[2][1]
            - a[0][2]*a[1][1]*a[2][0]
            - a[0][1]*a[1][0]*a[2][2]
            - a[0][0]*a[1][2]*a[2][1])


def matrix(c, d, z):
    return [[(d[i] if i == k else 0) - c[3*i+k]
             - (z[k-1] if i == 0 and k != 0 else 0)
             for k in range(3)] for i in range(3)]


def signature_at(c, frozen, t):
    free = [k for k in range(3) if k != frozen]
    out = []
    for a, b, z1, z2 in product((0, 1), repeat=4):
        d = [0, 0, 0]
        d[frozen] = t
        d[free[0]], d[free[1]] = a, b
        out.append(det3(matrix(c, d, (z1, z2))))
    return tuple(out)


def exceptional_integers():
    results = []
    for j in range(3):
        s0 = [signature_at(c, j, 0) for c in CANDIDATES]
        s1 = [signature_at(c, j, 1) for c in CANDIDATES]
        bad, universal_forms = set(), Counter()
        universal_pairs = isolated_pairs = 0
        for ai, bi in combinations(range(len(CANDIDATES)), 2):
            u = [s0[ai][k] - s0[bi][k] for k in range(16)]
            v = [s1[ai][k] - s1[bi][k] - u[k] for k in range(16)]
            ux = [w-u[0] for w in u]
            vx = [w-v[0] for w in v]
            pivot = next((k for k in range(16) if vx[k]), None)
            if pivot is None:
                if any(ux):
                    continue  # Never constant in the four free controls.
                universal_pairs += 1
                universal_forms[(u[0], v[0])] += 1
                if v[0] == 0:
                    assert abs(u[0]) > 2*DELTA, "Would obstruct every integer t"
                    continue
                # Enumerate all integers solving |u0+t*v0|<=2*DELTA.
                for cval in range(-2*DELTA, 2*DELTA+1):
                    numer = cval-u[0]
                    if numer % v[0] == 0:
                        bad.add(numer//v[0])
            else:
                t = Fraction(-ux[pivot], vx[pivot])
                if all(ux[k]+t*vx[k] == 0 for k in range(16)):
                    cval = u[0]+t*v[0]
                    if t.denominator == 1 and abs(cval) <= 2*DELTA:
                        bad.add(int(t))
                        isolated_pairs += 1
        expected = list(range(-1, 5)) if j == 0 else list(range(-9, 8))
        assert sorted(bad) == expected, (j, sorted(bad))
        assert universal_pairs == (0 if j == 0 else 256)
        results.append({"frozen_diagonal_index": j,
                        "bad_integer_values": sorted(bad),
                        "universal_constant_difference_pairs": universal_pairs,
                        "isolated_obstruction_pairs": isolated_pairs,
                        "universal_affine_forms": [
                            {"a": a, "b": b, "count": n}
                            for (a, b), n in sorted(universal_forms.items())]})
    return results


def prime_by_trial(n):
    return n > 1 and all(n % k for k in range(2, isqrt(n)+1))


def certify_fixtures():
    assert prime_by_trial(MODULUS)
    results = []
    for j, t, d, z, expected_gap, expected_hash in FIXTURES:
        assert d[j] == t
        residues = []
        for c in CANDIDATES:
            a = matrix(c, d, z)
            assert det3(a) == det3_perm(a)
            residues.append(det3(a) % MODULUS)
        sorted_r = sorted(residues)
        gaps = [sorted_r[k+1]-sorted_r[k] for k in range(511)]
        gaps.append(MODULUS+sorted_r[0]-sorted_r[-1])
        gap = min(gaps)
        digest = sha256(",".join(map(str, residues)).encode("ascii")).hexdigest()
        assert len(set(residues)) == 512
        assert gap == expected_gap and digest == expected_hash
        decoded = {}
        for i, r in enumerate(residues):
            for e in range(-DELTA, DELTA+1):
                v = (r+e) % MODULUS
                assert v not in decoded or decoded[v] == i
                decoded[v] = i
        assert len(decoded) == 512*(2*DELTA+1)
        results.append({"frozen_diagonal_index": j, "frozen_value": t,
                        "diagonal": list(d), "star_z": list(z),
                        "minimum_circular_gap": gap,
                        "distinct_centers": len(set(residues)),
                        "decoded_noisy_residues": len(decoded),
                        "lex_residues_sha256": digest})
    return results


if __name__ == "__main__":
    result = {"schema": "R284BM_EXACT_FROZEN_DIAGONAL_CERTIFICATE_V1",
              "matrix_population": "{1,2}^{3x3}", "candidate_count": len(CANDIDATES),
              "unordered_candidate_pairs": 512*511//2,
              "integer_noise_radius": DELTA,
              "minimum_required_circular_gap": 2*DELTA+1,
              "modulus": MODULUS,
              "exceptional_integer_classification": exceptional_integers(),
              "certified_fixtures": certify_fixtures(),
              "independent_review": "NOT_REVIEWED"}
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
