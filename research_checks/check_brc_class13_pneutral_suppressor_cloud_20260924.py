#!/usr/bin/env python3
"""Exact regression for BRC class-13 suppressor cloud theorem.

Finite computation is falsification/regression only.  The mathematical proof is
in research_notes/brc_class13_pneutral_suppressor_cloud_20260924.md.
"""
from collections import Counter
from math import factorial

BOUND = 5000

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d*d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def primes_upto(n):
    return [p for p in range(2, n+1) if is_prime(p)]

TARGETS = [p for p in primes_upto(BOUND) if p % 24 in (13, 19)]
CLASS13 = [p for p in TARGETS if p % 24 == 13]
CLASS19 = [p for p in TARGETS if p % 24 == 19]

def next_prime(n):
    x = n + 1
    while not is_prime(x):
        x += 1
    return x

def v_p(n, p):
    c = 0
    while n and n % p == 0:
        n //= p
        c += 1
    return c

def factor(n):
    out = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                n //= d
                e += 1
            out.append((d,e))
        d += 1 if d == 2 else 2
    if n > 1:
        out.append((n,1))
    return out

def order_mod(a, p):
    n = p - 1
    order = n
    for r,_ in factor(n):
        while order % r == 0 and pow(a, order//r, p) == 1:
            order //= r
    return order

def s13(p):
    assert p % 24 == 13
    o = order_mod(4, p)
    assert o % 2 == 0
    return o // 2

def c13(p):
    s = s13(p)
    return v_p(pow(4, s) + 1, p)

def factorial_v(n,p):
    ans = 0
    while n:
        n //= p
        ans += n
    return ans

def delta_single(p, j):
    h = (p-1)//2
    endpoint = int(j % h == 0)
    denom = v_p(j, p)
    if p % 24 == 13:
        s = s13(p)
        c = c13(p)
        cancel = (j % s == 0 and (j//s) % 2 == 1)
        return endpoint + denom - ((denom + c) if cancel else 0)
    return endpoint + denom

def delta(p, m):
    ans = 0
    for j,mult in m.items():
        ans += mult * delta_single(p,j)
        ans += factorial_v(mult,p)
    return ans

def dirty_class19(q):
    sq = s13(q)
    return [r for r in CLASS19 if r < q and (sq % r == 0 or sq % ((r-1)//2) == 0)]

# The exact criterion must match direct singleton defects on s_q.
criterion_failures = []
for q in CLASS13:
    if q == 13:
        continue
    sq = s13(q)
    direct = [r for r in CLASS19 if r < q and delta_single(r,sq) > 0]
    if direct != dirty_class19(q):
        criterion_failures.append((q, direct, dirty_class19(q)))
assert not criterion_failures, criterion_failures

# Sufficiency construction for every clean q<p pair under 5000.
pair_failures = []
pair_count = 0
for q in CLASS13:
    if q == 13 or dirty_class19(q):
        continue
    sq = s13(q)
    cq = c13(q)
    for p in CLASS13:
        if p <= q:
            continue
        pair_count += 1
        ell = next_prime(p)
        j = sq * ell
        cloud = Counter({j:1})
        dpj = delta_single(p,j)
        # Exact structure says dpj is either 0 or -c_p.
        if dpj < 0:
            cp = c13(p)
            assert dpj == -cp
            cloud[p**cp] += 1
        if delta(p,cloud) != 0:
            pair_failures.append(("p-neutral",p,q,delta(p,cloud),j))
        if not delta(q,cloud) < 0:
            pair_failures.append(("q-negative",p,q,delta(q,cloud),j))
        for r in CLASS19:
            if r >= p:
                break
            if delta(r,cloud) != 0:
                pair_failures.append(("class19",p,q,r,delta(r,cloud),j))
assert not pair_failures, pair_failures

# Necessity witness: for every dirty q, every tested q-cancellation multiplier
# wakes at least one fixed dirty class-19 branch. This is regression only; proof
# covers all odd multipliers.
necessity_failures = []
for q in CLASS13:
    if q == 13:
        continue
    bad = dirty_class19(q)
    if not bad:
        continue
    sq = s13(q)
    for odd in (1,3,5,7,9,11,13,17,19):
        j = sq*odd
        if not delta_single(q,j) < 0:
            # A multiplier can carry extra q-positive denominator if odd=q etc.;
            # restrict to actual negative q-cancellation samples.
            continue
        if not any(delta_single(r,j) > 0 for r in bad):
            necessity_failures.append((q,odd,j,bad))
assert not necessity_failures, necessity_failures

# Reproduce the Driver's nine class-13-only primitive-endpoint blocker cases
# (excluding base branch 13 from the blocker-class label).
class13_only = {}
for p in CLASS13:
    if p <= 13:
        continue
    h = (p-1)//2
    pos = [(q,delta_single(q,h)) for q in TARGETS if q < p and q != 13 and delta_single(q,h)>0]
    c13b = [q for q,d in pos if q%24==13]
    c19b = [q for q,d in pos if q%24==19]
    if c13b and not c19b:
        class13_only[p] = c13b

EXPECTED = {
    733:[61], 1021:[61], 1741:[61,349], 1861:[61,373],
    2029:[157], 2221:[37,61], 2749:[229], 3181:[61],
    3541:[61,709],
}
assert class13_only == EXPECTED, (class13_only, EXPECTED)

# Canonical descending construction for the seven clean cases.  It starts from
# e_h, suppresses every positive non-base class-13 branch using distinct large
# prime multipliers, and finally pays any remaining base-13 depth with clean
# e_{3 ell} ports. If a positive dirty q is encountered, the p-neutral,
# class19-neutral route is certified blocked by the theorem.
rescued = {}
blocked = {}
for p, initial in EXPECTED.items():
    h = (p-1)//2
    m = Counter({h:1})
    ell = next_prime(p)
    used = []
    obstruction = None

    while True:
        positives = [q for q in CLASS13 if 13 < q < p and delta(q,m)>0]
        if not positives:
            break
        q = max(positives)
        bad = dirty_class19(q)
        if bad:
            obstruction = (q, tuple(bad))
            break
        cq = c13(q)
        # Repeated clean singleton suppressors; distinct ell keeps factorial
        # credit absent. Recompute after every addition.
        while delta(q,m) > 0:
            sq = s13(q)
            j = sq*ell
            m[j] += 1
            used.append(("q",q,ell,j))
            if delta_single(p,j) < 0:
                cp = c13(p)
                m[p**cp] += 1
                used.append(("p_comp",p,cp,p**cp))
            ell = next_prime(ell)

    if obstruction is not None:
        blocked[p] = obstruction
        continue

    while delta(13,m)>0:
        j = 3*ell
        m[j] += 1
        used.append(("base13",13,ell,j))
        ell = next_prime(ell)

    prev = [(r,delta(r,m)) for r in TARGETS if r < p]
    if delta(p,m) != 1 or max([0]+[d for r,d in prev]) != 0:
        raise AssertionError(("rescue failed",p,delta(p,m),[(r,d) for r,d in prev if d>0],used))
    rescued[p] = used

assert sorted(rescued) == [733,1021,1741,1861,2029,3181,3541], rescued
assert blocked == {2221:(37,(19,)),2749:(229,(19,))}, blocked

print({
    "target_primes_below_5000": len(TARGETS),
    "class13_above_13": len([p for p in CLASS13 if p>13]),
    "clean_class13_q": len([q for q in CLASS13 if q>13 and not dirty_class19(q)]),
    "dirty_class13_q": len([q for q in CLASS13 if q>13 and dirty_class19(q)]),
    "clean_pair_constructions_checked": pair_count,
    "class13_only_cases": class13_only,
    "rescued_cases": sorted(rescued),
    "blocked_cases": blocked,
    "failures": 0,
})
