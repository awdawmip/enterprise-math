"""R284BO: exact constant-fibre gap for three-node directed star Port.

Finite testing only, separate from the all-H algebraic proof. No third-party packages.
"""
from collections import defaultdict
from itertools import product
import json


def coefficients(c, t, frozen):
    """Return (nonconstant polynomial coefficients, constant coefficient)."""
    a, b, cc, d, e, f, g, h, i = c
    if frozen == 2:
        # Leaf swap (1 <-> 2) is an exact isomorphism of the named star observer.
        return coefficients((a, cc, b, g, i, h, d, f, e), t, 1)
    if frozen == 0:
        s, u, v = t-a, d*i-f*g, g*e-d*h
        return ((s, -s*i-cc*g, -s*e-b*d, -d, u, -g, v),
                s*(e*i-f*h)+b*u+cc*v)
    if frozen == 1:
        r = t-e
        return ((r, -r*i-f*h, -a*r-b*d, -d, d*i-f*g, -(g*r+d*h)),
                a*(r*i+f*h)+b*(d*i-f*g)-cc*(g*r+d*h))
    raise ValueError(frozen)


def determinant(c, diagonal, z):
    a = [[(diagonal[r] if r == k else 0) - c[3*r+k]
          - (z[k-1] if r == 0 and k else 0)
          for k in range(3)] for r in range(3)]
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def check_coefficient_expansion():
    checks = 0
    for H in (2, 3):
        for idx, c in enumerate(product(range(1, H+1), repeat=9)):
            if idx >= 40:
                break
            for frozen in (0, 1, 2):
                for t in (-7, 0, H*H+2):
                    sig, const = coefficients(c, t, frozen)
                    for x in ((0, 0, 0, 0), (1, 1, 1, 1), (-2, 3, 4, -5)):
                        d = [0, 0, 0]
                        d[frozen] = t
                        other = [j for j in range(3) if j != frozen]
                        d[other[0]], d[other[1]] = x[:2]
                        # frozen 2: after swapping leaves, z1<->z2
                        z = (x[3], x[2]) if frozen == 2 else (x[2], x[3])
                        actual = determinant(c, d, z)
                        if frozen == 0:
                            s, A, B, C, D, E, F = sig
                            expected = (const+s*x[0]*x[1]+A*x[0]+B*x[1]
                                        +C*x[2]*x[1]+D*x[2]+E*x[3]*x[0]+F*x[3])
                        else:
                            r, A, B, C, D, E = sig
                            expected = (const+r*x[0]*x[1]+A*x[0]+B*x[1]
                                        +C*x[2]*x[1]+D*x[2]+E*x[3])
                        assert actual == expected, (H, c, frozen, t, x, actual, expected)
                        checks += 1
    return checks


def minimum_constant_gap(H, t, frozen):
    """Full H^9 census; +infinity encoded as None when there is no constant pair."""
    buckets = defaultdict(list)
    for c in product(range(1, H+1), repeat=9):
        signature, const = coefficients(c, t, frozen)
        buckets[signature].append(const)
    gap = None
    constant_pairs = 0
    for offsets in buckets.values():
        if len(offsets) == 1:
            continue
        constant_pairs += len(offsets)*(len(offsets)-1)//2
        offsets.sort()
        for a, b in zip(offsets, offsets[1:]):
            if gap is None or b-a < gap:
                gap = b-a
    return gap, constant_pairs


def theorem_gap(H, t, frozen):
    if frozen == 0:
        return 0 if 1-H*(H-1) <= t <= H*H else None
    if t < 1-H*H:
        return 1-H*H-t
    if t <= H*H:
        return 0
    return t-H+1


def verify():
    evidence = {"schema":"R284BO_EXACT_FINITE_CHECK_V1",
                "model":"positive alphabet {1,...,H}, n=3, directed two-star, integer frozen diagonal",
                "arithmetic":"Python exact integers, no modular approximation",
                "coefficient_checks":check_coefficient_expansion(),
                "tested_dimensions":[],"result":"PASS"}
    test_sets = ((2, range(-16, 19)), (3, range(-21, 25)),
                 (4, (-24, -16, -15, -12, -11, 0, 16, 17, 25)))
    for H, ts in test_sets:
        checks = 0
        landmarks = {}
        for frozen in (0, 1, 2):
            selected = {}
            for t in ts:
                actual, count = minimum_constant_gap(H, t, frozen)
                expected = theorem_gap(H, t, frozen)
                assert actual == expected, (H, frozen, t, actual, expected)
                checks += 1
                if t in (1-H*H-1, 1-H*H, 1-H*(H-1), 0, H*H, H*H+1):
                    selected[str(t)] = {"minimum_gap":actual,"constant_pairs":count}
            landmarks[f"frozen_{frozen}"] = selected
        evidence["tested_dimensions"].append({"H":H,"matrices":H**9,
             "t_per_position":len(ts),"position_t_cases":checks,"landmarks":landmarks})
    evidence["total_position_t_cases"] = sum(x["position_t_cases"] for x in evidence["tested_dimensions"])
    return evidence


if __name__ == "__main__":
    print(json.dumps(verify(), sort_keys=True, ensure_ascii=False, indent=2))
