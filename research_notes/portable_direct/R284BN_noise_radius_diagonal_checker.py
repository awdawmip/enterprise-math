"""R284BN: all-radius frozen-diagonal classification for the 3x3 binary star-Port.

Standard library only; exhaustive, exact integer/rational arithmetic. 512 matrices,
130816 unordered pairs for each of three frozen diagonals. No random search.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
import hashlib
import json

CANDIDATES = tuple(product((1, 2), repeat=9))
CORNERS = tuple(product((0, 1), repeat=4))


def determinant(c, diagonal, star):
    a = [[(diagonal[i] if i == k else 0) - c[3*i+k] -
          (star[k-1] if i == 0 and k else 0)
          for k in range(3)] for i in range(3)]
    return (a[0][0]*(a[1][1]*a[2][2] - a[1][2]*a[2][1])
            - a[0][1]*(a[1][0]*a[2][2] - a[1][1]*a[2][0])
            + a[0][2]*(a[1][0]*a[2][1] - a[1][1]*a[2][0]))


def signatures(frozen, t):
    others = [i for i in range(3) if i != frozen]
    result = []
    for c in CANDIDATES:
        current = []
        for x0, x1, z1, z2 in CORNERS:
            d = [0, 0, 0]
            d[frozen] = t
            d[others[0]], d[others[1]] = x0, x1
            current.append(determinant(c, d, (z1, z2)))
        result.append(tuple(current))
    return result


def classify(frozen):
    zero, one = signatures(frozen, 0), signatures(frozen, 1)
    universal = Counter()   # Q(t,x) = a + b*t for all x, for all t
    isolated = Counter()    # Q(t,x) = c for all x only at this integer t
    witness = {}
    for i, k in combinations(range(len(CANDIDATES)), 2):
        u = [zero[i][h] - zero[k][h] for h in range(16)]
        v = [one[i][h] - one[k][h] - u[h] for h in range(16)]
        ux = [w - u[0] for w in u]
        vx = [w - v[0] for w in v]
        pivot = next((h for h in range(1, 16) if vx[h]), None)
        if pivot is None:
            if any(ux):
                continue
            key = (u[0], v[0])
            universal[key] += 1
            witness.setdefault(("universal", key), (i, k))
        else:
            t = Fraction(-ux[pivot], vx[pivot])
            if t.denominator == 1 and all(ux[h]+t*vx[h] == 0 for h in range(1,16)):
                ti = int(t)
                c = u[0] + ti * v[0]
                key = (ti, c)
                isolated[key] += 1
                witness.setdefault(("isolated", key), (i, k))
    return universal, isolated, witness


def forbidden(universal, isolated, m):
    # For real circular error radius rho, m=floor(2*rho), an integer >=0.
    out = {t for (t, c) in isolated if abs(c) <= m}
    for (a, b) in universal:
        if b == 0:
            if abs(a) <= m:
                return None  # Every frozen t is obstructed.
        else:
            lo = (-m-a) // b if b > 0 else None
            if b < 0:
                raise AssertionError("Unexpected negative universal slope")
            # These ranges are finite and only grow linearly in the test m.
            lo = -((m+a)//b)
            hi = (m-a)//b
            out.update(range(lo, hi+1))
    return out


def prove():
    output = {"schema":"R284BN_ALL_NOISE_RADIUS_FROZEN_DIAGONAL_CERTIFICATE_V1",
              "population":"{1,2}^{3x3}","population_size":512,
              "unordered_pairs_per_index":130816,
              "real_error_radius":"rho >= 0; circular metric mod freely chosen prime",
              "m":"floor(2*rho)","indices":[]}
    for j in range(3):
        u, isolated, witness = classify(j)
        if j == 0:
            assert not u
            assert isolated == Counter({(-1,0):18,(0,0):36,(1,0):98,
                                       (2,0):98,(3,0):36,(4,0):18})
        else:
            assert u == Counter({(-3,2):16,(-2,2):32,(-1,1):16,(-1,2):16,
                                 (0,1):48,(0,2):48,(1,1):32,(2,1):16,
                                 (2,2):16,(3,1):16})
            assert len(isolated) == 68 and sum(isolated.values()) == 1824
            assert set(t for t,c in isolated) == set(range(-1,5))
            assert all((t,0) in isolated for t in range(-1,5))
        for m in range(0,31):
            direct = forbidden(u, isolated, m)
            expected = (set(range(-1,5)) if j==0 else
                        set(range(-m-3,max(4,m+1)+1)))
            assert direct == expected, (j,m,direct^expected)
        witnesses = {}
        if j == 0:
            choices = [("isolated",(t,0)) for t in range(-1,5)]
        else:
            choices = [("universal",(a,1)) for a in range(-1,4)] + [
                ("isolated",(t,0)) for t in (2,3,4)]
        for kind, key in choices:
            i,k = witness[(kind,key)]
            witnesses[f"{kind}:{key[0]},{key[1]}"] = [
                "".join(map(str,CANDIDATES[i])), "".join(map(str,CANDIDATES[k]))]
        output["indices"].append({
            "frozen_index":j,
            "universal_pairs":sum(u.values()),
            "universal_forms":[{"a":a,"b":b,"pair_count":count}
                               for (a,b),count in sorted(u.items())],
            "isolated_pairs":sum(isolated.values()),
            "isolated_integer_t":sorted({t for t,c in isolated}),
            "isolated_c_minmax":[min(c for t,c in isolated), max(c for t,c in isolated)],
            "isolated_distinct_t_c":len(isolated),
            "all_radius_bad_t":"[-1,4]" if j == 0 else "[-m-3, max(4,m+1)]",
            "witnesses":witnesses,
        })
    return output


if __name__ == "__main__":
    print(json.dumps(prove(),ensure_ascii=False,sort_keys=True,indent=2))
