#!/usr/bin/env python3
"""Exact lower-prime moment obstruction on the q14 shape roster. Standard library only."""
import argparse
from collections import Counter, defaultdict
import hashlib
import json
from itertools import combinations
from math import gcd, lcm, prod
from pathlib import Path
import subprocess
import sys

PRIMES = (2, 3, 5, 7, 11, 13)
BUDGET = 2331
ORIGINAL = {
    "T6_P17_Q14_SPLIT7_7_CANONICAL_SIDE_ROSTER_20261116.json": "242e4872003368905b9355fc666c307a6182482152922b83273708b1a1d07e54",
    "T6_P17_Q14_SPLIT7_7_INDEPENDENT_REPRODUCER_20261116.py": "e40581c985c20f8a1e18be5aefca4dfee627ddc51f62b8ef49cae8560042e12b",
    "T6_P17_Q14_SPLIT7_7_EXACT_PREFLIGHT_20261116.md": "d7b3eec44f8f26fb7506dcf7a2f05cd4b083e6f84b185bbc4210e5e12e1075a9",
}


def smooth(n):
    for p in (*PRIMES, 17):
        while n % p == 0:
            n //= p
    return n == 1


def vertical_roster():
    atoms = [(q, r) for q in range(1, 8) for r in range(1, 17) if smooth(17*q+r)]
    ds = [17*(17*q+r) for q, r in atoms]
    sides = []

    def build(prefix, start, order, rest):
        if not order:
            sides.append(tuple(prefix))
            return
        for i in range(start, len(atoms)):
            q, _ = atoms[i]
            if q > order:
                break
            if ds[i]-1 <= rest:
                build(prefix+[i], i, order-q, rest-(ds[i]-1))
    build([], 0, 7, BUDGET)
    assert len(sides) == 1907 and sides == sorted(sides)
    return atoms, ds, sides


def replay(folder, atoms, sides):
    paths = [folder / n for n in ORIGINAL]
    for path in paths:
        assert hashlib.sha256(path.read_bytes()).hexdigest() == ORIGINAL[path.name]
    roster = json.loads(paths[0].read_bytes())
    assert roster['atoms'] == list(map(list, atoms))
    assert roster['roster_index_arrays'] == list(map(list, sides))

    def limits():
        import resource
        resource.setrlimit(resource.RLIMIT_AS, (1 << 30, 1 << 30))
        resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
    result = subprocess.run([sys.executable, "-B", str(paths[1]), str(paths[0])],
                            preexec_fn=limits, timeout=120, check=True, capture_output=True)
    assert json.loads(result.stdout)['status'] == 'PASS_EXACT_PREFLIGHT'


def valuation(n, p):
    assert n
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def local_rows(points, vert, p):
    """Integer rows and moduli for evaluations on scaled reciprocal coordinates."""
    pool = dict.fromkeys(points, 1)
    values = [1]*len(vert)
    rows = []
    pivots = []
    for degree in range(min(7, len(points))):
        pivot = min(pool, key=lambda x: valuation(pool[x], p))
        modulus = p**valuation(pool[pivot], p)
        # Divide a common factor out of this particular congruence only.
        common = gcd(modulus, *values)
        reduced = modulus // common
        if reduced > 1:
            rows.append((tuple((a//common) % reduced for a in values), reduced, degree))
        pivots.append(pivot)
        del pool[pivot]
        for x in pool:
            pool[x] *= x-pivot
        values = [a*(x-pivot) for a, x in zip(values, vert)]
    return rows, pivots


def rational_rows(points, vert):
    values = [prod(x-y for y in points) for x in vert]
    return [(tuple(a*x**k for a, x in zip(values, vert)), 0, len(points)+k)
            for k in range(max(0, 7-len(points)))]


def row_classes(rows, active, sides):
    labels = {}
    result = {}
    for i in active:
        s = sides[i]
        key = tuple(sum(values[a] for a in s) % m if m else sum(values[a] for a in s)
                    for values, m, _ in rows)
        result[i] = labels.setdefault(key, len(labels))
    return result


def consistency_test():
    # Exhaustive minors on small samples check p-ordering with a different,
    # determinant-based test for the local column lattice.
    from itertools import permutations
    def det(rows):
        return sum((-1)**sum(c[i] > c[j] for i,j in combinations(range(len(c)),2))
                   *prod(rows[i][j] for i,j in enumerate(c))
                   for c in permutations(range(len(rows))))
    count = 0
    for p in (2, 3, 5):
        for nodes in [(0, 2, 4, 6), (1, 4, 7, 10), (0, 3, 6, 10)]:
            cols = [tuple(x**j for j in range(4)) for x in nodes]
            index_v = valuation(det(cols), p)
            for a in range(8):
                for b in range(a, 8):
                    v = [a**j-b**j for j in range(4)]
                    tests, _ = local_rows(nodes, (a, b), p)
                    via_newton = all((row[0]-row[1]) % m == 0 for row,m,_ in tests)
                    via_determinants = all((n:=det([*subset, v])) == 0 or valuation(n,p)>=index_v
                                           for subset in combinations(cols,3))
                    assert via_newton == via_determinants
                    count += 1
    return count


def sharp_witness():
    p = 11

    def coordinate(d):
        v = valuation(d, p)
        assert v <= 2
        return (p**(2-v) * pow(d//(p**v), -1, p)) % p

    def polynomial(d):
        x = coordinate(d)
        return x*prod(j*x-1 for j in range(1,6)) % p

    assert all(polynomial(d)==0 for d in range(2,726))
    pair = [2057, 2142]
    assert [polynomial(d) for d in pair] == [9,0]
    allowed = [2]+[121*j for j in range(1,7)]
    residues = [coordinate(d) for d in allowed]
    determinant = prod(b-a for a,b in combinations(residues, 2)) % p
    assert determinant
    return {'vertical_denominators':pair, 'current_M':276, 'necessary_new_mass':725,
            'least_M_in_11_adic_unbounded_linear_relaxation':726,
            'polynomial_values_mod_11':[9,0], 'lower_pivot_denominators':allowed,
            'residues_mod_11':residues, 'vandermonde_det_mod_11':determinant}


def main():
    arg = argparse.ArgumentParser()
    arg.add_argument('--frozen-dir', type=Path, help="directory with the three immutable source files")
    args = arg.parse_args()
    atoms, den, sides = vertical_roster()
    if args.frozen_dir:
        replay(args.frozen_dir, atoms, sides)
    side_limit = [1+BUDGET-sum(den[a]-1 for a in s) for s in sides]
    bound = max(side_limit)
    future = [d for d in range(2,bound+1) if smooth(d)]
    scale = lcm(*den, *future)
    vert = [scale//a for a in den]
    masks = [sum(1 << a for a in set(s)) for s in sides]
    groups = defaultdict(list)
    for i, m in enumerate(side_limit):
        groups[m].append(i)
    bits_hist = Counter()
    limit_hist = []
    examples = {}
    first_survivor = None
    labels = ('rational', *map(str, PRIMES))
    active = []
    for limit, new in sorted(groups.items()):
        active.extend(new)
        points = [scale//d for d in future if d <= limit]
        all_rows = [rational_rows(points, vert)]
        all_rows.extend(local_rows(points, vert, p)[0] for p in PRIMES)
        classes = [row_classes(rows, active, sides) for rows in all_rows]
        tested = cut = 0
        for i in new:
            for j in active:
                if side_limit[j] == limit and j >= i or masks[i] & masks[j]:
                    continue
                tested += 1
                bits = sum(1 << k for k,c in enumerate(classes) if c[i] != c[j])
                bits_hist[bits] += 1
                if not bits and first_survivor is None:
                    first_survivor = {"M":limit, "denominators_plus":[den[a] for a in sides[i]],
                                      "denominators_minus":[den[a] for a in sides[j]]}
                if bits:
                    cut += 1
                    name = labels[(bits & -bits).bit_length()-1]
                    score = (len(sides[i])+len(sides[j]), limit, min(i,j), max(i,j))
                    if name not in examples or score < examples[name][0]:
                        rowset = all_rows[labels.index(name)]
                        for values,m,degree in rowset:
                            delta = sum(values[a] for a in sides[i])-sum(values[a] for a in sides[j])
                            if (delta % m if m else delta):
                                examples[name] = (score, {'denominators_plus':[den[a] for a in sides[i]],
                                    'denominators_minus':[den[a] for a in sides[j]], 'max_denominator':limit,
                                    'separating_degree':degree, 'reduced_modulus':m,
                                    'difference_after_reduction':delta % m if m else delta})
                                break
        limit_hist.append([limit, tested, cut])
    total = sum(bits_hist.values())
    assert total == 809566
    hits = {n:sum(v for k,v in bits_hist.items() if k & (1<<i)) for i,n in enumerate(labels)}
    unique = {n:bits_hist[1<<i] for i,n in enumerate(labels)}
    result = {'side_rosters': len(sides), 'named_atoms':len(atoms), 'disjoint_unordered_pairs':total,
              'max_future_denominator_range':[min(side_limit),max(side_limit)], 'reciprocal_scale':scale,
              'local_primes':PRIMES,'rejected_by_union':total-bits_hist[0],
              'pass_necessary_test':bits_hist[0], 'rejections_by_test_overlapping':hits,
              'rejections_only_by_this_test':unique,
              'max_denominator_counts_columns':['M','pairs','rejected'],
              'max_denominator_counts':limit_hist,'examples':{k:v for k,(_,v) in sorted(examples.items())},
              'first_relaxed_survivor':first_survivor, 'sharp_local_witness':sharp_witness(),
              'determinant_cross_checks':consistency_test()}
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
