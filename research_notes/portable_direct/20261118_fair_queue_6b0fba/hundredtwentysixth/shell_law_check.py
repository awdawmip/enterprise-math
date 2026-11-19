"""Recheck A3 signed coordinate moves and shell fibres. Python standard library."""
import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, permutations, product
import json
from math import gcd
from pathlib import Path
import runpy

GROUP = tuple(permutations(range(4)))
H = (1, 0, 2, 3)
G = (0, 2, 1, 3)
PIN = '28f3000ea052b78b7b7ec3ba34c3d880ed98666b61eef2888d1890cd11e61b04'


def residue(x, q):
    return tuple(t % q for t in x)


def cells(q):
    return [v + ((-sum(v)) % q,) for v in product(range(q), repeat=3)]


def fibre(r, z, q):
    faces = edges = 0
    for i, a in enumerate(z):
        rest = [b for j, b in enumerate(z) if j != i]
        for sign in (1, -1):
            if (a - sign * r) % q:
                continue
            offsets = [(r + sign * b) % q for b in rest]
            amount, rem = divmod(2 * r - sum(offsets), q)
            assert not rem and amount >= -2
            faces += (amount + 2) * (amount + 1) // 2
        if (a - r) % q:
            continue
        for j, b in enumerate(z):
            if i == j or (b + r) % q:
                continue
            c = next(z[h] for h in range(4) if h not in (i, j))
            edges += (r - c) // q + (r + c) // q + 1
    vertices = sum(all((z[i] - (r if i in plus else -r)) % q == 0
                       for i in range(4)) for plus in combinations(range(4), 2))
    return faces - edges + vertices


def mobius_divisors(n):
    terms = [(1, 1)]
    prime = 2
    while prime * prime <= n:
        if n % prime == 0:
            terms += [(prime * d, -m) for d, m in terms]
            while n % prime == 0:
                n //= prime
        prime += 1
    if n > 1:
        terms += [(n * d, -m) for d, m in terms]
    return terms


def face_count(r, z, q):
    return sum((a - s * r) % q == 0 for a in z for s in (-1, 1))


def class_terms(q, c):
    h = gcd(q, 2)
    t = gcd(q, 3) if c % gcd(q, 3) == 0 else 0
    two, four = 2 * c % q == 0, 4 * c % q == 0
    # Values are q^2 times the corresponding face-law probabilities.
    bad = 3 + t + 6 * h - 6 * four + 3 * two * (q - 2 * h)
    tr = Fraction(h + q * two, 2)
    three = Fraction(3 + t, 4)
    return {'bad': bad, 'transposition': tr, 'three_cycle': three,
            'double_transposition': h, 'four_cycle': 1,
            'quotient_square_agreement': tr + three - two}


def limiting(q, r, key, primitive):
    terms = mobius_divisors(gcd(q, r)) if primitive else [(1, 1)]
    n = sum(mu * class_terms(q // d, r // d)[key] for d, mu in terms)
    den = sum(mu * (q // d) ** 2 for d, mu in terms)
    return Fraction(n, den)


def run(source):
    assert sha256(source.read_bytes()).hexdigest() == PIN
    native = runpy.run_path(str(source))
    move, action, shell = (native[k] for k in ('prefix_move','r_act','shell'))
    counts = Counter()
    examples = []
    double = (1, 0, 3, 2)
    three = (1, 2, 0, 3)
    four = (1, 2, 3, 0)
    grids = {q: cells(q) for q in range(2, 11)}
    bad = {q: {z for z in grid if len({residue(action(g,z),q) for g in GROUP}) < 24}
           for q, grid in grids.items()}
    agree = {q: {z for z in grid if residue(action(G,z),q) in (z,residue(action(H,z),q))}
             for q, grid in grids.items()}
    for q, grid in grids.items():
        def events(z):
            yield 'bad', z in bad[q]
            yield 'quotient_square_agreement', z in agree[q]
            for key, g in [('transposition', G), ('double_transposition', double),
                           ('three_cycle', three), ('four_cycle', four)]:
                yield key, residue(action(g,z),q) == z
        for c in range(q):
            for prim in [False, True]:
                terms = Counter()
                tot = 0
                for z in grid:
                    if prim and gcd(*z, gcd(q, c)) > 1:
                        continue
                    w = face_count(c, z, q)
                    tot += w
                    for name, yes in events(z):
                        terms[name] += w * yes
                for name in class_terms(q, c):
                    assert Fraction(terms[name], tot) == limiting(q, c, name, prim)
                    counts['face_probability_checks'] += 1
    for r in range(1, 15):
        points = tuple(shell(r))
        primitive_points = [x for x in points if gcd(*x) == 1]
        for q, grid in grids.items():
            raw = Counter(residue(x,q) for x in points)
            raw_prim = Counter(residue(x,q) for x in primitive_points)
            divisors = mobius_divisors(r)
            mobius_fibres = Counter()
            for d, mu in divisors:
                for y in grid:
                    mobius_fibres[tuple(d*a % q for a in y)] += mu*fibre(r//d,y,q)
            assert mobius_fibres == raw_prim
            counts['primitive_mobius_fibres'] += len(grid)
            for z in grid:
                value = fibre(r,z,q)
                assert raw[z] == value
                counts['integer_fibres'] += 1
                assert fibre(r+2*q,z,q)-2*fibre(r+q,z,q)+value == 4*face_count(r,z,q)
                counts['second_differences'] += 1
                if 2*r % q == 0:
                    c = r % q
                    assert value == (2*r//q)**2*z.count(c) + 2*(z.count(c)==4)
                    if r > 1:
                        den = 4*sum(mu*(q//d)**2 for d,mu in mobius_divisors(gcd(q,r)))
                        wanted = z.count(c)*len(primitive_points) if gcd(gcd(q,r),*z)==1 else 0
                        assert raw_prim[z]*den == wanted
                        counts['exact_resonant_primitive_fibres'] += 1
            if q == 2 and r > 1:
                stabs = {z:frozenset(g for g in GROUP if residue(action(g,z),2)==z)
                         for z in raw_prim}
                states = {frozenset(GROUP): 1}
                for t in range(1,7):
                    update = Counter()
                    for old, multiplicity in states.items():
                        for z, weight in raw_prim.items():
                            update[old & stabs[z]] += multiplicity*weight
                    states = update
                    failure = Fraction(sum(v for s,v in states.items() if len(s)>1),len(primitive_points)**t)
                    expected = (3*Fraction(1,2)**t - 2*Fraction(1,4)**t if r%2
                                else 3*Fraction(1,3)**t)
                    assert failure == expected
                    counts['independent_repetitions'] += 1
            # Same input on the common shell of the two actual scale paths.
            for n, depth in [(r,1),(r+1,2)]:
                def native_agree(x):
                    upper = move(n+1,depth,G,x)
                    lower = move(n,depth,G,x)
                    return residue(lower,q) in (residue(upper,q),residue(action(H,upper),q))
                assert sum(map(native_agree,points)) == sum(raw[z] for z in agree[q])
                counts['paired_native_marker_checks'] += len(points)
            if (q,r) in [(5,4),(5,5),(5,10),(7,7),(7,14),(8,8),(9,9)]:
                def summary(tab):
                    den = sum(tab.values())
                    return {'points':den,'not_free':sum(tab[z] for z in bad[q]),
                            'square_agreements':sum(tab[z] for z in agree[q])}
                examples.append({'q':q,'r':r,'ordinary':summary(raw),'primitive':summary(raw_prim),
                           'phase_limits_ordinary':{name:str(limiting(q,r,name,False))
                               for name in ('bad','quotient_square_agreement')},
                           'phase_limits_primitive':{name:str(limiting(q,r,name,True))
                               for name in ('bad','quotient_square_agreement')}})
    return {'source_sha256':PIN,'verified':counts,'examples':examples}


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo',type=Path,default=Path('.'),help='checkout of enterprise-math')
    args = ap.parse_args()
    print(json.dumps(run(args.repo/'scripts/check_a3_recursive_shell_alignment_tomography.py'),
                     ensure_ascii=False, indent=2, sort_keys=True))
