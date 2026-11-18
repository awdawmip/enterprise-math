"""Exact radial-fibre and decorated-triple certificate for two triangular-lattice motifs."""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
import json
from math import comb
from pathlib import Path
import sys


KERNEL_SHA = "4f3e356227a1c964d33a3ddae94922463ba28097a43b8d1b8f6cd9ca5615fc9f"
U = ((0, 0), (1, 0), (0, 1))
PAIR_TARGET = {1: 12, 3: 6, 4: 9, 7: 6, 9: 3}


def square(x, y):
    return x*x + x*y + y*y


def distance(a, b):
    return square(a[0] - b[0], a[1] - b[1])


def motif(sign):
    return tuple(sorted((x + 2*sign*u, y + 2*sign*v) for (x,y), (u,v) in product(U, repeat=2)))


def triple_sides(triangle):
    return tuple(sorted(distance(a, b) for a, b in combinations(triangle, 2)))


def histogram(points):
    return Counter(distance(a, b) for a, b in combinations(points, 2))


def autocorrelation(points):
    return Counter((x-u, y-v) for (x,y), (u,v) in product(points, repeat=2))


def canonical(points):
    transforms = []
    image = points
    for _ in range(6):
        for transformed in (image, [(y, x) for x,y in image]):
            u,v = min(transformed)
            transforms.append(tuple(sorted((x-u, y-v) for x,y in transformed)))
        image = [(-y, x+y) for x,y in image]
    return min(transforms)


def typed_counts(kernel, points, arity):
    """Each ordered index path i<j[<k] names its originating subset; then project to its target."""
    unit = kernel.cwm_edge(1)
    bags = defaultdict(lambda: kernel.CWM_ZERO)
    for indices in combinations(range(len(points)), arity):
        state = kernel.CWM_ONE
        for _ in indices:
            state = kernel.cwm_propagate(state, unit)
        entries = tuple(points[i] for i in indices)
        tag = distance(*entries) if arity == 2 else triple_sides(entries)
        bags[tag] = kernel.cwm_recoalesce(bags[tag], state)
    assert all(s.count == s.total and s.dominant == 1 for s in bags.values())
    return Counter({key: s.count for key,s in bags.items()})


def anchored_fibre(a, b):
    origin, tip = (0,0), (3,0)
    box = tuple(product(range(-3,4), repeat=2))
    endpoints = [p for p in box if distance(p,origin) == 9]
    assert len(endpoints) == 6
    assert all(canonical((origin,p)) == canonical((origin,tip)) for p in endpoints)
    other = [p for p in box if distance(p,origin) in PAIR_TARGET and distance(p,tip) in PAIR_TARGET]
    assert len(other) == 14
    groups = {canonical(a): "A", canonical(b): "B"}
    assert len(groups) == 2
    accepted = []
    examined = 0
    for rest in combinations(other, 7):
        examined += 1
        candidate = (origin, tip, *rest)
        if histogram(candidate) == PAIR_TARGET:
            accepted.append(dict(points=sorted(candidate), orbit=groups[canonical(candidate)]))
    assert examined == comb(14,7) == 3432
    assert Counter(r["orbit"] for r in accepted) == {"A": 2, "B": 2}
    return dict(anchor=[origin,tip], admissible_sites=other, subsets=examined, accepted=accepted)


def local_periodic_triangles(points, period=7):
    # Unit neighbours of an anchor lie inside these nine copies since the motif diameter is 3.
    copies = {(x+period*i,y+period*j) for x,y in points for i,j in product((-1,0,1), repeat=2)}
    incidences = 0
    for p in points:
        neighbours = [q for q in copies if distance(p,q) == 1]
        incidences += sum(distance(q,r) == 1 for q,r in combinations(neighbours,2))
    assert incidences % 3 == 0
    return incidences // 3


def records(counts):
    return [dict(key=key, count=value) for key,value in sorted(counts.items()) if value]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, type=Path)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    source = args.repo / "src/enterprise_math/brc_weighted.py"
    assert sha256(source.read_bytes()).hexdigest() == KERNEL_SHA
    sys.path.insert(0, str(args.repo / "src"))
    from enterprise_math import brc_weighted as kernel

    a, b = motif(1), motif(-1)
    assert len(set(a)) == len(set(b)) == 9 and autocorrelation(a) == autocorrelation(b)
    assert typed_counts(kernel,a,2) == typed_counts(kernel,b,2) == PAIR_TARGET
    ha, hb = (typed_counts(kernel,p,3) for p in (a,b))
    for p, h in ((a,ha), (b,hb)):
        assert h == Counter(triple_sides(t) for t in combinations(p,3))
        assert sum(h.values()) == comb(9,3)
        margins = Counter()
        for key, value in h.items():
            for side in key:
                margins[side] += value
        assert margins == Counter({k:7*v for k,v in PAIR_TARGET.items()})
    diff = {k: ha[k] - hb[k] for k in set(ha) | set(hb) if ha[k] != hb[k]}
    assert diff == {(1,1,1):-1, (1,7,7):3, (3,3,3):2, (3,3,9):-3, (7,7,7):-2, (9,9,9):1}
    perimeter = Counter()
    for key,value in diff.items():
        perimeter[sum(key)] += value
    polynomial = {power:value for power,value in perimeter.items() if value}
    assert polynomial == {3:-1, 9:2, 21:-2, 27:1}
    t = Fraction(1,2)
    direct = sum(value*t**power for power,value in polynomial.items())
    assert direct == -t**3 * (1-t**6)**3 * (1+t**6)
    assert all(sum(value*power**j for power,value in polynomial.items()) == 0 for j in range(3))
    assert sum(value*power**3 for power,value in polynomial.items()) == 2592
    periodic = [local_periodic_triangles(p) for p in (a,b)]
    assert periodic == [3,4]
    fibre = anchored_fibre(a,b)
    data = dict(kernel_sha256=KERNEL_SHA, A=a, B=b, pair_counts=records(PAIR_TARGET),
                displacement_counts=records(autocorrelation(a)), triangles_A=records(ha),
                triangles_B=records(hb), signed_difference_A_minus_B=records(diff),
                gaussian_powers=records(polynomial), gaussian_at_t_half=str(direct),
                radial_fibre=fibre, period7_unit_triangles_per_cell=periodic)
    payload = json.dumps(data, ensure_ascii=True, sort_keys=True, indent=2) + "\n"
    if args.json:
        args.json.write_text(payload)
    print("anchored 3432 -> 4 -> 2 orbits; triangles 3,4; sha256", sha256(payload.encode()).hexdigest())


if __name__ == "__main__":
    main()
