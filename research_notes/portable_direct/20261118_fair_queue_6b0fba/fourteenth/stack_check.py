"""Reproduce the arithmetic and finite tiling checks for the cyclic coordinate audit."""
from functools import lru_cache
from itertools import combinations
from math import gcd, isqrt, lcm, prod
import json


def prime(n):
    return n >= 2 and all(n % k for k in range(2, isqrt(n) + 1))


def next_prime(n):
    candidate = n + 1
    while not prime(candidate):
        candidate += 1
    return candidate


def crt(residues, moduli):
    M = prod(moduli)
    return sum(a*(M//m)*pow(M//m, -1, m) for a, m in zip(residues, moduli)) % M


def channel_checks():
    # Restricted demonstration: p=211; one ordinary channel with three digits
    # and the two seeds. This does not instantiate the full word-rule tile.
    p = 211
    D = p**4
    seed_b = next_prime(D), next_prime(next_prime(D))
    seed_r = next_prime(2*seed_b[1]), next_prime(next_prime(2*seed_b[1]))
    ordinary_digits = (37, 41, 43)   # all exceed (5-1)*7
    channels = [(5, 7, ordinary_digits), (2, seed_b[0], (seed_r[0],)),
                (3, seed_b[1], (seed_r[1],))]
    moduli = [D]
    for a, b, digits in channels:
        for r in digits:
            v = r*pow(b, -1, a) % a
            assert r-v*b >= 0 and (r-v*b) % a == 0
        moduli.extend((prod(digits)**2, a, b))
    assert lcm(*moduli) == prod(moduli)
    q = 11
    moduli.append(q)
    assert lcm(*moduli) == prod(moduli)
    for delta in (-17, 0, 8, 123):
        inputs = [(delta-i*i) % m for i, m in enumerate(moduli)]
        x = crt(inputs, moduli)
        assert [x % m for m in moduli] == inputs
    ordinary_r = prod(ordinary_digits)
    active = (ordinary_r, 5, 7)
    seed_active = (seed_r[0], 2, seed_b[0], p*p, 3)
    for ms in (active, seed_active):
        xs = [(-i-2) % m for i,m in enumerate(ms)]
        y = crt(xs, ms)
        assert [y % m for m in ms] == xs and lcm(*ms)==prod(ms)
    for r in (2, 3, 6, 15):
        for x in range(-r, r):
            for k in range(r):
                def v(x, k, high):
                    return (x+(k-x)%r+r*high) % (r*r)
                assert {v(x,k,h) for h in range(r)}==set(range(k,r*r,r))
                assert all(v(x-3,k-3,h)==(v(x,k,h)-3)%(r*r) for h in range(r))
        assert all((r*z) % (r*r) for z in range(1,r*r,r))
    return dict(p=p, full_channels=p*p+2, full_digits=p*p*(p-1)+2,
                full_prime_support_V=p*p*(p+1)+7, reduced_moduli=moduli,
                reduced_crt_final_order=str(prod(moduli)), seed_b=list(seed_b),
                reduced_ordinary_activation_modulus=prod(active),
                reduced_seed_horizontal_index=str(prod(seed_active)*p*p))


def cover_count(masks, size):
    # Exact cover by translated tiles; different centers are counted separately,
    # including centers whose translated subsets coincide.
    through = [[m for m in masks if (m >> x) & 1] for x in range(size)]
    @lru_cache(maxsize=None)
    def extend(filled):
        if filled == (1 << size)-1:
            return 1
        point = next(x for x in range(size) if not (filled >> x) & 1)
        return sum(extend(filled | m) for m in through[point] if not (filled & m))
    return extend(0)


def arithmetic_extension(n,q,first,d,h,split=False):
    first = set(first)
    second = set(range(q)) - first
    assert {(u-v)%q for u in first for v in first} == set(range(q))
    S = {s for s in range(q) if {(s+u)%q for u in first}==first}
    def plus(x,y):
        if split:
            return (x%n+y%n)%n+n*((x//n+y//n)%q)
        return (x+y)%(n*q)
    t = d+n*h
    tile = {n*k for k in first} | {plus(t,n*k) for k in second}
    masks = [sum(1 << plus(c,z) for z in tile) for c in range(n*q)]
    found = cover_count(masks,n*q)
    g = gcd(d,n)
    length = n//g
    monodromy = (length*h if split else length*t//n)%q
    expected = (q//len(S))**g*len(S)**n if monodromy in S else 0
    assert found==expected
    return dict(n=n,q=q,d=d,h=h,split=split,stabilizer=len(S),
                cycle_defect=monodromy,center_sets=found)


def tests():
    first = {0,1,3}
    q = 7
    examples = [arithmetic_extension(7,7,first,1,h) for h in range(7)]
    examples.append(arithmetic_extension(7,7,first,1,0,True))
    all_rows = []
    for n in range(2,6):
        for d in range(1,n):
            for h in range(q):
                all_rows.append(arithmetic_extension(n,q,first,d,h))
    # Composite colour layer with a nontrivial stabilizer.
    doubled = first | {x+7 for x in first}
    for n in (2,3,4):
        for d in range(1,n):
            for h in range(14):
                all_rows.append(arithmetic_extension(n,14,doubled,d,h))
    # Least prime allowing two colour classes both with full differences.
    admissible=[]
    for m in (2,3,5,7):
        count=0
        for k in range(1,m):
            for a in combinations(range(m),k):
                b=set(range(m))-set(a)
                if all(len({(x-y)%m for x in z for y in z})==m for z in (a,b)):
                    count+=1
        admissible.append([m,count])
    assert [m for m,c in admissible if c]==[7]
    return dict(channel=channel_checks(), exact_covers_checked=len(examples)+len(all_rows),
                cyclic_49_center_counts=[row["center_sets"] for row in examples[:-1]],
                split_7_by_7=examples[-1], secondary_checks_nonzero=sum(row["center_sets"]>0 for row in all_rows),
                full_difference_bipartitions_labeled=admissible)


if __name__ == "__main__":
    print(json.dumps(tests(), indent=2))
