"""Recompute the three h=3 probes, using exact arithmetic and no external packages."""
from fractions import Fraction as Q
from itertools import product
import json

PROBES = ((1, 4, 1, 3), (2, 1, 4, 2), (3, 1, 4, 1))


def transfer(edges):
    matrix = [(1, 0, 0, 1)] + [(0, 0, 0, 0)] * 3
    for resistor in edges:
        upper = [(a+resistor*c, b+resistor*d, c, d) for a, b, c, d in matrix]
        matrix = [(a, b, c+(upper[i-1][0] if i else 0),
                   d+(upper[i-1][1] if i else 0))
                  for i, (a, b, c, d) in enumerate(upper)]
    return matrix


def numerator(edges):
    one, two, three = [a+d for a, b, c, d in transfer(edges)[1:]]
    assert one == len(edges)*sum(edges)
    return two**2 - 2*one*three


def resistance_beta(edges):
    n, total = len(edges), sum(edges)
    positions = [sum(edges[:i]) for i in range(n)]
    table = []
    for x in positions:
        arcs = [abs(x-y) for y in positions]
        table.append([Q(a*(total-a), total) for a in arcs])
    rows = [sum(row) for row in table]
    return Q(2, n**4*total**2) * (
        n**2*sum(a*a for row in table for a in row)
        - 2*n*sum(x*x for x in rows) + sum(rows)**2)


def parameters(edges):
    x, y, z = (sum(edges[:i]) for i in (1, 2, 3))
    return sum(edges), Q(x+y+z, 3), Q(z-x, 2), Q(x+z-2*y, 6)


def micro(r, m, s, d):
    points = (0, m-s+d, m-2*d, m+s+d, r)
    return tuple(v-u for u, v in zip(points, points[1:]))


def scalar_coordinates(r, m, s, d):
    h, z, w = 2*m-r, s*d, d*d
    m0 = (450*r*r*m*m + 2394*r*r*m + 15949*r*r - 900*r*m**3 -
          2394*r*m*m - 23226*r*m + 29636*r + 450*m**4 + 23226*m*m + 83720)
    d0 = 3*h*(-90*r*m-361*r+90*m*m+1212)
    summed = (m0 + 512*s**4 - 512*(r+9)*s**3 + 3072*s*s*w
              + 32*(15*r*r-30*r*m+135*r+30*m*m+1487)*s*s
              - 3584*(r+9)*s*w + 640*h*(r+9)*z
              + 8*(r+9)*(-50*r*m-133*r+50*m*m-180)*s + 4608*w*w
              + 96*(18*r*r-30*r*m+189*r+30*m*m+1730)*w)
    diff = d0 + 288*h*s*s + 384*(r+9)*z + 120*h*(r+9)*s + 864*h*w
    return 160*(r+9)*(-3*r+6*m+5), summed, diff


def interval_certificate():
    r = Q(1, 100)
    s, w = r/2, r*r/36
    ms = -12960 + 2048*s**3 + 6144*s*w + 64*(45*r*r+135*r+1487)*s
    mz = 640*r*(9+r)
    mw = (3072*s*s+3584*(9+r)*s+9216*w
          +96*(48*r*r+189*r+1730))
    ds = (576*s + 120*(9+r))*r
    dw = 864*r
    assert ms < -12000 and mz < 58 and mw < 167000
    assert ds < 11 and dw < 9
    s_margin = 12000-Q(2, 9)*r*167000
    assert s_margin > 11000 and (58 + Q(2, 3)*167000)/s_margin < 10
    assert 11+2*r < 12 and Q(120, 3450) < 1
    return {"r_upper": str(r), "M_s_upper": str(ms), "abs_M_z_upper": str(mz),
            "abs_M_w_upper": str(mw), "abs_D_s_upper": str(ds),
            "abs_D_w_upper": str(dw), "D_z_lower": 3456,
            "contraction_upper": str(Q(120, 3450))}


def main():
    states = independent = 0
    for increments in product(range(5), repeat=4):
        if sum(increments) > 4:
            continue
        edges = tuple(1+i for i in increments)
        values = []
        for probe in PROBES:
            ring = edges + probe
            exact = numerator(ring)
            assert Q(8*exact,(8*sum(ring))**4) == resistance_beta(ring)
            values.append(exact)
            independent += 1
        f1, f2, f3 = values
        assert (f1-f2, f1+f3, f1-f3) == scalar_coordinates(*parameters(edges))
        states += 1
    assert (states, independent) == (70, 210)

    mirror_checks = 0
    for b in ((1,), (3, 2), (1, 7, 2), *PROBES, (8, 2, 3, 11, 1)):
        n, v, total = 4+len(b), len(b), sum(b)
        u = transfer(b)[1][0]
        for r, m, s in ((12, 5, 2), (9, 4, 1), (1, Q(1, 2), Q(1, 10))):
            d = s*Q(1, 6)
            delta = numerator(micro(r, m, s, d)+b)-numerator(micro(r, m, s, -d)+b)
            predicted = 16*n*(r+total)*s*d*((v+1)*(2*m-r)+2*u-(v-1)*total)
            assert delta == predicted
            mirror_checks += 1

    # Re-use exactly the unrounded beta readings after multiplying all probe
    # resistances by K. The three differences should identify every grid point.
    keys = set()
    for internal in product(range(1, 13), repeat=4):
        if sum(internal) != 12:
            continue
        edges = tuple(Q(x, 12) for x in internal)
        scaled = [tuple(100*x for x in p) for p in PROBES]
        reads = tuple(numerator(edges+p) for p in scaled)
        assert reads not in keys
        keys.add(reads)
    sample = tuple(Q(i, 10) for i in range(1, 5))
    k = 100
    native = [resistance_beta(sample+tuple(k*x for x in p)) for p in PROBES]
    r,m,s,d = parameters(tuple(x/k for x in sample))
    vals = [x*(8*(r+9))**4/8 for x in native]
    assert (vals[0]-vals[1],vals[0]+vals[2],vals[0]-vals[2]) == scalar_coordinates(r,m,s,d)
    recovered_m = ((vals[0]-vals[1])/(160*(r+9))+3*r-5)/6
    assert recovered_m == m
    return {"probe_words": PROBES, "unisolvent_grid_sum_of_increments_at_most": 4,
            "interpolation_nodes": states, "effective_resistance_comparisons": independent,
            "different_positive_compositions_of_12": len(keys),
            "universal_reflection_identity_checks": mirror_checks,
            "uniform_rectangle_certificate": interval_certificate(),
            "one_original_scale_ring_experiment": {
                "K": k, "hidden_edges": list(map(str,sample)), "beta2": list(map(str,native)),
                "normalized_r_m_s_d": list(map(str,(r,m,s,d))),
                "normalized_m_from_first_two": str(recovered_m)}}


if __name__ == "__main__":
    print(json.dumps(main(), ensure_ascii=False, indent=2))
