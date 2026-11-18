"""Enumerate whole cyclic algebras, including nonunits and the trivial character."""
import itertools
import json
from math import gcd


def convolution(x, y, p):
    size = len(x)
    out = [0]*size
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            out[(i+j) % size] += a*b
    return tuple(z % p for z in out)


def ceiling(x, y):
    return (x+y-1)//y


def totient(d):
    return sum(gcd(d, i) == 1 for i in range(1, d+1))


def order(p, d):
    return next(i for i in range(1, d+1) if (p**i-1) % d == 0)


def formula(p, size, u, v):
    reduced = size
    while reduced % p == 0:
        reduced //= p
    h = size//reduced
    k, n = abs(u-v), min(u, v)
    ppart = 1
    while k % (ppart*p) == 0:
        ppart *= p
    count = 1
    for d in range(1, reduced+1):
        if reduced % d == 0:
            e = order(p, d)
            Q = p**e
            nonunits = Q**(h-ceiling(h,n))
            units = gcd(k,Q-1)*Q**(h-ceiling(h,ppart))
            count *= (nonunits+units)**(totient(d)//e)
    universal = n >= h and k % (h*(p**order(p,reduced)-1)) == 0
    assert universal == (count == p**size)
    return count


def audit(p, size):
    exponents = list(itertools.combinations(range(1,9),2))
    counts = dict.fromkeys(exponents, 0)
    for x in itertools.product(range(p), repeat=size):
        powers = [None, x]
        for _ in range(7):
            powers.append(convolution(powers[-1], x, p))
        for u,v in exponents:
            counts[u,v] += powers[u] == powers[v]
    assert all(formula(p, size, u, v) == count for (u,v),count in counts.items())
    return dict(p=p, width=size, ring_size=p**size, powers_checked=len(exponents),
                sample=[counts[u,v] for u,v in [(1,4),(3,6),(1,7),(2,8)]])


if __name__ == '__main__':
    rows = [audit(p,size) for p,size in [(2,3),(2,4),(2,6),(2,8),(3,3),(3,6)]]
    ell, p = 13, 5
    chi = tuple(0 if i == 0 else (1 if pow(i,6,ell)==1 else -1) for i in range(ell))
    square = convolution(chi, chi, p)
    assert square == (2,)+(4,)*12
    print(json.dumps(dict(rings=rows, gauss_square_mod5=square), indent=2))
