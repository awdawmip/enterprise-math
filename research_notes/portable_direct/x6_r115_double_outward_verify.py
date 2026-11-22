"""Exact arithmetic reproducer for the R115 double-outward edge re-entry theorem.

Scope: conditional four-positive-weight six-pair BRC integer-difference observer.
Source: R90 exact unrestricted optimum; R114/R114-followup boundary atlas.
No floating-point inputs or external dependencies.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import lcm
import json
from pathlib import Path

PAIR = tuple(combinations(range(4), 2))
TEMPLATES = {
    "I": [(0, 0, 2), (0, 1, -1), (0, 1, 1)]
    + [(1, m, n) for m in (-1, 1) for n in (-3, -1, 1)]
    + [(1, 0, n) for n in (-2, 0, 2)],
    "II": [(0, 1, -1), (0, 1, 1), (0, 2, 0)]
    + [(1, m, 0) for m in (-2, 0, 2)]
    + [(1, m, n) for m in (-1, 1, 3) for n in (-1, 1)],
}

def integer_direction(tmn):
    t, m, n = tmn
    assert (m - n) % 2 == 0
    return (10*t-12*m+3*n, -5*t+7*m-2*n, t+(n-3*m)//2)

def port(a):
    return max(sum(max(v, 0) for v in a), sum(max(-v, 0) for v in a))

def weight_path(kind, eps, r):
    s = Q(1, 2) + eps/2
    if kind == "I":
        X, Y = Q(17, 4), Q(18)+r*eps
        w = (s, 1-s, X-s, Y-s)
        predicted_eta = Q(12)/(Y-eps)
    else:
        X, Y = Q(9)+r*eps, Q(8)
        w = (1-s, s, X-s, Y-s)
        predicted_eta = Q(6)/(X-eps)
    assert min(w) > 0
    return w, predicted_eta

def score(tmn, w):
    t, m, n = tmn
    z = (0, t, 3*m, t+6*n)
    return max(Q(abs(z[i]-z[j]), 1)/(w[i]+w[j]) for i, j in PAIR)

def exact_infinite_optimum(w):
    A, B, C, D = w
    s = min(A, B)
    X = C+s
    Y = D+s
    T = max(A+B, X/6, Y/12, min(X/3, Y/6))
    return 1/T

def canon(a):
    for t in a:
        if t:
            return a if t > 0 else tuple(-u for u in a)
    return a

def direct_enumeration(w, p, eta):
    """Independently scan ALL q<=p integer triples, no template restriction."""
    D = lcm(*(v.denominator for v in w))
    ws = [v.numerator*(D//v.denominator) for v in w]
    sums = [ws[i]+ws[j] for i, j in PAIR]
    threshold = Q(3, 2)*eta
    def less_than(u, v, h, bound):
        z = (0, u, v, h)
        return all(abs(z[i]-z[j])*D*bound.denominator < bound.numerator*wij
                   for (i, j), wij in zip(PAIR, sums))
    seen = set()
    total = 0
    for x in range(-p, p+1):
        for y in range(-p, p+1):
            for z in range(-p, p+1):
                if not (x or y or z):
                    continue
                a = (x, y, z)
                if port(a) > p:
                    continue
                total += 1
                u = x+3*y+6*z
                v = 3*x+12*y+30*z
                h = 7*x+39*y+126*z
                assert not less_than(u, v, h, eta), ("incorrect predicted optimum", a)
                if less_than(u, v, h, threshold):
                    seen.add(canon(a))
    return total, seen

def trial(kind, eps, r):
    w, eta = weight_path(kind, eps, r)
    assert exact_infinite_optimum(w) == eta
    target = Q(3, 2)*eta
    templates = [tmn for tmn in TEMPLATES[kind] if score(tmn, w) < target]
    qmax = 28 if kind == "I" else 38
    expected = 10 if r < 1 else 3
    assert len(templates) == expected, (kind, eps, r, templates)
    assert max(port(integer_direction(tmn)) for tmn in templates) <= qmax
    direct_count, actual = direct_enumeration(w, qmax, eta)
    expected_set = {canon(integer_direction(tmn)) for tmn in templates}
    assert actual == expected_set, (kind, r, expected_set ^ actual)
    return {
        "kind": kind, "epsilon": str(eps), "r": str(r),
        "weights": [str(v) for v in w],
        "eta": str(eta), "strict_cutoff": str(target),
        "p_min": qmax, "q_bounded_oriented_triples_checked": direct_count,
        "near_count": len(templates),
        "near_tmn": [list(tmn) for tmn in templates],
        "near_xyz": [list(integer_direction(tmn)) for tmn in templates],
        "near_max_port": max(port(integer_direction(tmn)) for tmn in templates),
        "direct_enumeration_matches": True,
    }

def main():
    rows = [trial(kind, Q(1, 100), r) for kind in ("I", "II")
            for r in (Q(1, 2), Q(1), Q(2))]
    assert [(r["kind"], r["near_count"]) for r in rows] == [
        ("I", 10), ("I", 3), ("I", 3),
        ("II", 10), ("II", 3), ("II", 3)]
    payload = {
        "schema": "X6_R115_TWO_DOUBLE_OUTWARD_REENTRY_CERTIFICATE_V1",
        "scope": "conditional 6-pair BRC; 4 positive weights; all p>=28 for I, p>=38 for II",
        "method": "Fraction exact, direct integer direction scan at p_min and analytic finite-gap bounds for arbitrary p",
        "samples": rows,
        "independent_review": False,
    }
    path = Path(__file__).with_name("x6_r115_double_outward_results.json")
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    print("PASS: exact optima, 6 rational witness sets, exhaustive integer triples at both onset ports")
    for row in rows:
        print(f'{row["kind"]} r={row["r"]}: eta={row["eta"]} near={row["near_count"]} scanned={row["q_bounded_oriented_triples_checked"]}')

if __name__ == "__main__":
    main()
