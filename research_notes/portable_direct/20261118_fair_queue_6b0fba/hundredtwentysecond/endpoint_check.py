"""Recompute finite-ring endpoint and sampling identities with Python's standard library."""
import itertools
import json
import math
import random
from collections import Counter
from fractions import Fraction


def identity(d):
    return tuple(tuple(int(i == j) for j in range(d)) for i in range(d))


def mul(a, b, n):
    return tuple(tuple(sum(x*y for x, y in zip(row, col)) % n for col in zip(*b)) for row in a)


def combine(a, x, b, y, n):
    return tuple(tuple((x*v + y*w) % n for v, w in zip(row, col)) for row, col in zip(a, b))


def bezout(a, b):
    u, v, x, y = 1, 0, 0, 1
    while b:
        q = a // b
        a, b, u, x, v, y = b, a % b, x, u-q*x, y, v-q*y
    return a, u, v


def read_ports(n, offsets, weights, ports):
    I = identity(len(ports[0]))
    total, g = combine(I, 0, I, 0, n), n
    for offset, weight, observed in zip(offsets, weights, ports):
        new_g, u, v = bezout(g, weight)
        total = combine(total, u, combine(observed, 1, I, -offset, n), v, n)
        g = new_g
    assert all(x % g == 0 for row in total for x in row)
    m = n // g
    return m, tuple(tuple(x//g % m for x in row) for row in total)


def charpoly(a, n):
    # Integer Faddeev--LeVerrier on integer lifts; all divisions are exact in Z.
    d = len(a)
    b = identity(d)
    coeff = [1]
    for k in range(1, d+1):
        prod = [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]
        c, rem = divmod(-sum(prod[i][i] for i in range(d)), k)
        assert rem == 0
        coeff.append(c)
        for i in range(d):
            prod[i][i] += c
        b = prod
    return tuple(x % n for x in coeff)


def decode(n, m, b):
    d = len(b)
    c = charpoly(b, m)
    groups = []
    for r in range(d+1):
        target = [(-1)**j*math.comb(r, j) if j <= r else 0 for j in range(d+1)]
        h = math.gcd(m, *(x-y for x, y in zip(c, target)))
        groups.append(math.gcd(n, pow(h, n.bit_length(), n)))
    dark = n // math.prod(groups)
    assert math.gcd(math.prod(groups), dark) == 1
    return groups, dark


def rank_mod(a, p):
    b = [list(row) for row in a]
    r = 0
    for j in range(len(b)):
        i = next((k for k in range(r, len(b)) if b[k][j] % p), None)
        if i is None:
            continue
        b[i], b[r] = b[r], b[i]
        z = pow(b[r][j], -1, p)
        for k in range(r+1, len(b)):
            v = b[k][j]*z % p
            b[k] = [(c-v*t) % p for c, t in zip(b[k], b[r])]
        r += 1
    return r


def matrix(flat, d):
    return tuple(tuple(flat[i:i+d]) for i in range(0, len(flat), d))


def idempotents(d, n):
    for v in itertools.product(range(n), repeat=d*d):
        a = matrix(v, d)
        if mul(a, a, n) == a:
            yield a


def weights(d, p, e):
    out = []
    for r in range(d+1):
        binom = math.prod(p**(d-i)-1 for i in range(r)) // math.prod(p**(r-i)-1 for i in range(r))
        out.append(binom*p**((2*e-1)*r*(d-r)))
    return out


def newton(a, n):
    b2 = mul(a, a, n)
    return combine(b2, 3, mul(b2, a, n), -2, n)


def inv2(a, n):
    (x,y),(z,w) = a
    u = pow(x*w-y*z, -1, n)
    return ((u*w % n, -u*y % n), (-u*z % n, u*x % n))


def visible_orbits(n, m):
    d = 2
    I = identity(d)
    lifts = {}
    for b in idempotents(d, n):
        key = combine(b, 1, I, 0, m)
        lifts.setdefault(key, set()).add(b)
    total = 0
    for key, targets in lifts.items():
        start = key
        for _ in range(n.bit_length().bit_length()):
            start = newton(start, n)
        assert start in targets
        hits = Counter()
        for v in itertools.product(range(n//m), repeat=4):
            s = combine(I, 1, matrix(v, d), m, n)
            hits[mul(mul(s, start, n), inv2(s, n), n)] += 1
        assert set(hits) == targets and len(set(hits.values())) == 1
        total += sum(hits.values())
    return {'N':n,'M':m,'endpoints':len(lifts),'targets':sum(map(len,lifts.values())),'conjugations':total}


def crt(residues, mods):
    n = math.prod(mods)
    return sum(v*(n//q)*pow(n//q, -1, q) for v, q in zip(residues, mods)) % n


def endpoint_trials():
    primes = (2,3,5,7)
    powers = (16,27,25,7)
    n = math.prod(powers)
    d = 6
    I = identity(d)
    rng = random.Random(20261119)
    ms = (1,2,18,35,150,420,2100,n)
    assert all(n % m == 0 for m in ms)
    trials = 0
    example = None
    for ranks in itertools.chain([(0,2,4,6),(4,0,3,6)], (tuple(rng.randrange(d+1) for _ in primes) for _ in range(66))):
        diag = [crt([int(i < r) for r in ranks], powers) for i in range(d)]
        b = tuple(tuple(diag[i] if i == j else 0 for j in range(d)) for i in range(d))
        for _ in range(12):
            i,j = rng.sample(range(d),2)
            u = rng.randrange(n)
            E = tuple(tuple(int((ii,jj) == (i,j)) for jj in range(d)) for ii in range(d))
            s, si = combine(I,1,E,u,n), combine(I,1,E,-u,n)
            b = mul(mul(s, b, n), si, n)
        assert mul(b,b,n) == b
        for m in ms:
            g = n//m
            G, L = (2*g,3*g), (19,-8)
            ports = [combine(I,l,b,w,n) for l,w in zip(L,G)]
            recovered, b0 = read_ports(n,L,G,ports)
            assert recovered == m and b0 == combine(b,1,I,0,m)
            groups, dark = decode(n,m,b0)
            independent = [math.prod(q for p,q in zip(primes,powers) if m % p == 0 and rank_mod(b,p)==r) for r in range(d+1)]
            assert groups == independent
            if ranks == (0,2,4,6) and m == 18:
                example = {'N':n,'M':m,'rank_factors':groups,'blind_factor':dark,'trace_mod_2':sum(b[i][i] for i in range(d)) % 2}
            trials += 1
    return {'checks':trials,'example':example}


def sampling_report():
    out = []
    for d,p,e,q,f in [(1,2,3,3,2),(2,2,2,3,1),(3,2,1,3,1),(4,5,2,7,1),(5,101,1,103,1),(6,101,1,103,1)]:
        a,b = weights(d,p,e), weights(d,q,f)
        denom = sum(a)*sum(b)
        split = Fraction(denom-sum(x*y for x,y in zip(a,b)),denom)
        m = d//2
        distance = 1-Fraction((1+d%2)*a[m]*b[m],denom)
        if d%2:
            assert split >= Fraction(1,2)
        assert distance >= split
        out.append({'d':d,'prime_powers':[p**e,q**f],'unequal_rank_probability':str(split),'central_sampler_TV':str(distance)})
    return out


def main():
    local = []
    for d,p,e in [(2,2,1),(2,2,2),(2,2,3),(2,3,1),(2,3,2),(2,5,1),(3,2,1),(3,3,1),(4,2,1)]:
        counts = Counter(rank_mod(b,p) for b in idempotents(d,p**e))
        expected = weights(d,p,e)
        assert [counts[r] for r in range(d+1)] == expected
        local.append({'d':d,'p':p,'e':e,'ranks':expected})
    composite = {}
    for n,powers in [(6,[(2,2),(3,3)]),(12,[(2,4),(3,3)])]:
        real = Counter(tuple(rank_mod(b,p) for p,q in powers) for b in idempotents(2,n))
        w = [weights(2,p,1 if q==p else 2) for p,q in powers]
        assert all(real[r,s] == w[0][r]*w[1][s] for r,s in itertools.product(range(3), repeat=2))
        composite[n] = {'matrices':sum(real.values()),'unequal_rank_matrices':sum(v for (r,s),v in real.items() if r!=s)}
    print(json.dumps({'integer_endpoint':endpoint_trials(),'all_visible_fibers':[visible_orbits(4,2),visible_orbits(8,2),visible_orbits(12,6)],'local_exhaustive':local,'composite_exhaustive':composite,'sampling':sampling_report()},indent=2,sort_keys=True))


if __name__=='__main__':
    main()
