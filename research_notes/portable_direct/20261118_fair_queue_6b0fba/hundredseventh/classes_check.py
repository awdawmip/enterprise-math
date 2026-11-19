"""Class constraints on coincidence rotations. Run with the Python standard library."""
from collections import Counter
from functools import cache
from itertools import combinations, product
from math import gcd, isqrt, lcm
from pathlib import Path
import argparse
import json


def norm(a, b):
    return a*a + a*b + 6*b*b


def norm_solutions(n):
    """All (a,b) with norm n, up to multiplication by the unit -1."""
    limit = isqrt(4*n//23)
    solutions = set()
    for b in range(-limit, limit+1):
        disc = 4*n - 23*b*b
        d = isqrt(disc)
        if d*d == disc and (d-b) % 2 == 0:
            for a in ((d-b)//2, (-d-b)//2):
                if (a, b) > (0, 0):
                    assert norm(a, b) == n
                    solutions.add((a, b))
    return sorted(solutions)


@cache
def split_class(p):
    if p == 23 or (p != 2 and pow((-23) % p, (p-1)//2, p) != 1):
        return None
    return 0 if norm_solutions(p) else 1


@cache
def factors(n):
    out = []
    p = 2
    while p*p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e:
            out.append((p, e))
        p = 3 if p == 2 else p+2
    if n != 1:
        out.append((n, 1))
    return tuple(out)


def diameter(t):
    return max((0, *t)) - min((0, *t))


@cache
def shell_histogram(k, e, c):
    hist = Counter()
    for t in product(range(-e, e+1), repeat=k):
        if diameter(t) == e:
            hist[tuple(c*x % 3 for x in t)] += 1
    assert sum(hist.values()) == (e+1)**(k+1)-2*e**(k+1)+(e-1)**(k+1)
    return hist


def add_histograms(a, b):
    out = Counter()
    for x, v in a.items():
        for y, w in b.items():
            out[tuple((i+j) % 3 for i, j in zip(x, y))] += v*w
    return out


def index_distribution(n, k):
    fac = [(split_class(p), e) for p, e in factors(n)]
    if any(c is None for c, e in fac):
        return {}
    hist = {(0,)*k: 1}
    for c, e in fac:
        hist = add_histograms(hist, shell_histogram(k, e, c))
    return hist


def geometric_index(rotations):
    # A Z-basis of the dual sum may be replaced by all these integral generators.
    den = lcm(*(n for n, a, b in rotations))
    columns = [(den, 0), (0, den)]
    for n, a, b in rotations:
        r = den//n
        columns.extend([(r*(a+b), r*6*b), (-r*b, r*a)])
    g = gcd(*(abs(x*v-y*u) for (x,y),(u,v) in combinations(columns, 2)))
    assert den*den % g == 0
    return den*den//g


def direct_census(bound, k):
    rotations = [(n,a,b) for n in range(1,bound+1) for a,b in norm_solutions(n*n)
                 if gcd(n,a,b) == 1]
    counts = Counter()
    for rows in product(rotations, repeat=k):
        m = geometric_index(rows)
        if m <= bound:
            counts[m] += 1
    for m in range(1, bound+1):
        assert counts[m] == index_distribution(m,k).get((0,)*k,0), (m,k)
    return dict(bound=bound, rotations=len(rotations), tested_tuples=len(rotations)**k,
                counts={str(m): v for m,v in sorted(counts.items())})


def local_identity(k):
    # Compute coefficients of the character identity over F_7, with 2 a cube root of 1.
    ntests = 0
    for c in product(range(3), repeat=k):
        phase = [pow(2,a,7) for a in (-sum(c), *c)]
        previous = [0, 0]
        for e in range(5):
            val = 1
            for z in phase:
                val = val*sum(pow(z,j,7) for j in range(e+1)) % 7
            expected = (val-2*previous[-1]+previous[-2]) % 7
            got = sum(pow(2,sum(a*b for a,b in zip(c,t)) % 3,7)
                      for t in product(range(-e,e+1),repeat=k) if diameter(t)==e) % 7
            assert got == expected
            previous.append(val)
            ntests += 1
    return ntests


def slow_modes(k, h):
    seen = Counter()
    for c in product(range(h),repeat=k):
        if not any(c):
            continue
        r = sum(sum(a*b for a,b in zip(c,subset)) % h == 0
                for subset in product(range(2),repeat=k)) - 1
        v = [a for a in c if a]
        pair = len(v)==2 and sum(v) % h == 0
        involution = len(set(v))==1 and 2*v[0] % h == 0
        assert r <= 2**(k-1)-1
        assert (r==2**(k-1)-1) == (len(v)==1 or pair or involution)
        seen[r] += 1
    return dict(sorted(seen.items()))


def cumulative(bound, k):
    states = Counter()
    selections = {}
    for m in range(1,bound+1):
        states.update(index_distribution(m,k))
        if m in (100, 1000, bound):
            selections[m] = dict(total=states.total(), principal=states[(0,)*k],
                                 low=min(states.get(u,0) for u in product(range(3),repeat=k)),
                                 high=max(states.values()))
    return selections


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    # theta and (1+theta) generate the ideals over 6 and 8 appearing in the argument.
    assert norm(0,1) == 6 and norm(1,1) == 8 and not norm_solutions(2)
    result = dict(discriminant=-23,
                  local_character_checks={k:local_identity(k) for k in (1,2,3,4)},
                  direct_lattice_counts={k:direct_census(b,k) for k,b in ((1,180),(2,90),(3,36))},
                  cyclic_slow_modes={f'{k},{h}':slow_modes(k,h)
                                     for k in (2,3,4) for h in (2,3,4,6)},
                  cumulative={k:cumulative(3000,k) for k in (1,2,3)})
    body = json.dumps(result,sort_keys=True,indent=2)+'\n'
    if args.output:
        args.output.write_text(body)
    else:
        print(body,end='')


if __name__=='__main__':
    main()
