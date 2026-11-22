"""Exact certificate for X6 R112; standard-library rational arithmetic only."""
from fractions import Fraction as Q
from itertools import product
import json

CASES = [
    {"w": (60, 1, 10, 46), "E": Q(1, 11), "outer": Q(9, 61), "p": 51,
     "inside_max": Q(7, 53), "out_count": 2},
    {"w": (6, 47, 45, 2), "E": Q(6, 49), "outer": Q(9, 47), "p": 92,
     "inside_max": Q(3, 17), "out_count": 2},
]
EPS = Q(1, 25)


def moments(a):
    x, y, z = a
    return (x+3*y+6*z, 3*x+12*y+30*z, 7*x+39*y+126*z)


def port(a):
    return max(sum(max(t, 0) for t in a), sum(max(-t, 0) for t in a))


def denominators(w):
    A, B, C, D = w
    return (A+B, A+C, A+D, B+C, B+D, C+D)


def score_moments(uvw, w):
    u, v, h = uvw
    values = (u, v, h, v-u, h-u, h-v)
    return max(Q(abs(x), d) for x, d in zip(values, denominators(w)))


def oriented(a):
    return tuple(-t for t in a) if a < tuple(-t for t in a) else a


def orbit(a):
    r = tuple(t % 3 for t in a)
    return min(r, tuple((-t) % 3 for t in r))


def exact_carrier(w, radius):
    """All ±a with F_w(a)<=radius, via complete integer moment box."""
    d = denominators(w)
    bounds = tuple((radius * d[i]).numerator // (radius * d[i]).denominator for i in range(3))
    U, V, H = bounds
    rows = {}
    for u, v, h in product(range(-U, U+1), range(-V, V+1), range(-H, H+1)):
        if v % 3 or (h-u) % 6 or (h-u-6*v) % 12:
            continue
        uvw = (u, v, h)
        f = score_moments(uvw, w)
        if f > radius:
            continue
        a = ((h+19*u-8*v)//2, (-h-14*u+7*v)//3, (h+11*u-6*v)//12)
        if moments(a) != uvw:
            raise AssertionError("inverse congruence mismatch")
        if a == (0, 0, 0):
            continue
        rows[oriented(a)] = (f, port(a), orbit(a))
    return bounds, rows


def frac(f):
    return str(f)


def certify(case):
    w = case['w']
    radius = case['outer']
    eta = case['E']
    p0 = case['p']
    bounds, rows = exact_carrier(w, radius)
    assert len(rows) == 14
    assert min(f for f, q, r in rows.values()) == eta
    assert eta < Q(3, 2)*eta < radius
    near = {a: (f, q, r) for a, (f, q, r) in rows.items() if f < Q(3, 2)*eta}
    outer = {a: (f, q, r) for a, (f, q, r) in rows.items() if f >= Q(3, 2)*eta}
    assert len(near) == 12 and len(outer) == case['out_count']
    assert max(q for f, q, r in near.values()) == p0
    assert max(f for f, q, r in near.values()) == case['inside_max']
    assert min(f for f, q, r in outer.values()) == radius
    witness = [a for a,(f,q,r) in near.items() if f == eta and q <= p0]
    assert witness
    residues = set(r for f,q,r in near.values())
    all_orbits = {orbit(a) for a in product(range(3),repeat=3) if a != (0,0,0)}
    assert len(residues) == 12 and all_orbits - residues == {(0,1,2)}
    d_min = min(denominators(w))
    t = 2 * EPS / d_min
    K = (1+t)/(1-t)
    inside_ratio = max(f / eta for f,q,r in near.values())
    outside_ratio = radius / eta
    assert inside_ratio * K < Q(3, 2)
    assert outside_ratio / K > Q(3, 2)
    def row_entry(a, val):
        f,q,r = val
        return {"a": list(a), "q": q, "score": frac(f), "mod3_orbit":list(r)}
    return {
        "weights":list(w), "min_pair_denominator":d_min,
        "minimizer_score_all_ports_ge_p0":frac(eta), "port_at_least":p0,
        "complete_carrier_cutoff":frac(radius), "moment_box_bounds":list(bounds),
        "complete_carrier_unoriented_count":len(rows),
        "strict_near_count_for_all_ports_ge_p0":len(near),
        "near_max_score":frac(max(f for f,q,r in near.values())),
        "outside_min_score":frac(radius), "excluded_mod3_sign_orbit":[0,1,2],
        "perturbation_sup_abs_radius":frac(EPS),
        "score_ratio_in_at_base":frac(inside_ratio),
        "score_ratio_out_at_base_lower_bound":frac(outside_ratio),
        "multiplicative_relative_ratio_bound":frac(K),
        "strict_in_margin_verified":bool(inside_ratio*K<Q(3,2)),
        "strict_out_margin_verified":bool(outside_ratio/K>Q(3,2)),
        "near_directions": [row_entry(a,near[a]) for a in sorted(near,key=lambda a:near[a][1])],
        "excluded_at_cutoff": [row_entry(a,outer[a]) for a in sorted(outer,key=lambda a:outer[a][1])],
    }


def main():
    res = {"schema":"X6_R112_DUAL_OPEN_TWELVE_CHAMBERS_V1",
           "scientific_status":"AUTHOR_EXACT_RATIONAL_CERTIFICATE_NOT_INDEPENDENTLY_REVIEWED",
           "method":"six-pair exact rational norm; complete inverse-moment lattice carrier",
           "cases":[certify(x) for x in CASES]}
    print(json.dumps(res, ensure_ascii=False, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()
