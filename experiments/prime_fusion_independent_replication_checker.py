#!/usr/bin/env python3
"""
Prime Fusion blind independent replication checker.

Authored independently from:
  - research_tasks/PRIME_FUSION_INDEPENDENT_REPLICATION_20260823.md
  - research_inputs/PRIME_FUSION_BLIND_INDEPENDENT_REPLICATION_PACKET_20260823.md
  - definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md

Exact integer arithmetic only. No source-run checker inspected or copied.
"""

from math import gcd, isqrt
from collections import defaultdict

BOX_IDENTITY = 300
BOX_CARRIER = 180
BOX_PRIME = 350
BOX_ADJ = 350
MOD_PRIME_MAX = 199
SCALAR_COLLISION_BOX = 80
MODULI_2D = (6, 30, 210, 385)


def A(a, b):
    return a*a + b*b


def B(a, b):
    return a*a - a*b + b*b


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
    return [p for p in range(2, n + 1) if is_prime(p)]


def legendre(x, p):
    assert p > 2 and is_prime(p)
    x %= p
    if x == 0:
        return 0
    z = pow(x, (p - 1)//2, p)
    return 1 if z == 1 else -1


def expected_projective_A_roots(p):
    if p == 2:
        return 1
    return 2 if p % 4 == 1 else 0


def expected_projective_B_roots(p):
    if p == 3:
        return 1
    if p == 2:
        return 0
    return 2 if p % 3 == 1 else 0


def recover_unordered(x, y):
    d2 = 2*y - x
    s2 = 3*x - 2*y
    if d2 < 0 or s2 < 0:
        return None
    d = isqrt(d2)
    s = isqrt(s2)
    if d*d != d2 or s*s != s2:
        return None
    if (s + d) % 2:
        return None
    lo = (s - d)//2
    hi = (s + d)//2
    if lo < 0:
        return None
    if A(lo, hi) != x or B(lo, hi) != y:
        return None
    return (lo, hi)


def carrier_mark(a, b):
    assert a > 0 and b > 0 and gcd(a, b) == 1
    x, y = A(a, b), B(a, b)
    n = x*y
    assert gcd(b, n) == 1
    r = (a * pow(b, -1, n)) % n
    return n, r


def test_identities_and_recovery():
    for a in range(0, BOX_IDENTITY + 1):
        for b in range(0, BOX_IDENTITY + 1):
            if a == b == 0:
                continue
            x, y = A(a, b), B(a, b)
            assert x - y == a*b
            assert 2*y - x == (a-b)*(a-b)
            assert 3*x - 2*y == (a+b)*(a+b)
            g = gcd(a, b)
            assert gcd(x, y) == g*g
            rec = recover_unordered(x, y)
            assert rec == tuple(sorted((a, b)))
    print(f"PASS identities/recovery/gcd: 0<=a,b<={BOX_IDENTITY}, excluding (0,0)")


def test_marked_carrier():
    count = 0
    for a in range(1, BOX_CARRIER + 1):
        for b in range(1, BOX_CARRIER + 1):
            if gcd(a, b) != 1:
                continue
            x, y = A(a, b), B(a, b)
            n, r = carrier_mark(a, b)
            f = r*r + 1
            h = r*r - r + 1
            assert gcd(f, h) == 1
            assert gcd(n, f) == x
            assert gcd(n, h) == y
            lo, hi = recover_unordered(x, y)
            candidates = {(lo, hi), (hi, lo)}
            matches = []
            for u, v in candidates:
                if gcd(v, n) == 1 and (u * pow(v, -1, n)) % n == r:
                    matches.append((u, v))
            assert (a, b) in matches
            if a != b:
                assert len(matches) == 1
                assert (r * r) % n != 1
            count += 1
    print(f"PASS marked carrier reconstruction: {count} primitive positive cells in box 1..{BOX_CARRIER}")


def test_scalar_collision():
    by_n = defaultdict(list)
    collision = None
    for a in range(1, SCALAR_COLLISION_BOX + 1):
        for b in range(a, SCALAR_COLLISION_BOX + 1):
            if gcd(a, b) != 1:
                continue
            x, y = A(a, b), B(a, b)
            n = x*y
            by_n[n].append((a, b, x, y))
    for n in sorted(by_n):
        vals = by_n[n]
        uniq = {(a, b) for a, b, _, _ in vals}
        if len(uniq) > 1:
            collision = (n, vals)
            break
    assert collision is not None
    n, vals = collision
    expected = {(14, 43, 2045, 1443), (31, 38, 2405, 1227)}
    assert expected.issubset(set(vals))
    print(f"PASS scalarization collision search: box<= {SCALAR_COLLISION_BOX}; N={n}; cells={vals}")


def test_modular_directions_and_slices():
    for p in primes_upto(MOD_PRIME_MAX):
        nonzero = [(a, b) for a in range(p) for b in range(p) if not (a == 0 and b == 0)]
        za = [(a, b) for a, b in nonzero if A(a, b) % p == 0]
        zb = [(a, b) for a, b in nonzero if B(a, b) % p == 0]
        assert not (set(za) & set(zb))
        na = expected_projective_A_roots(p)
        nb = expected_projective_B_roots(p)
        assert len(za) == na*(p-1)
        assert len(zb) == nb*(p-1)

        surv = sum(1 for a in range(p) for b in range(p)
                   if A(a, b) % p != 0 and B(a, b) % p != 0)
        expected_surv = (p-1)*(p+1-na-nb)
        assert surv == expected_surv

        for k in range(p):
            ra = sum(1 for t in range(p) if A(t+k, t) % p == 0)
            rb = sum(1 for t in range(p) if B(t+k, t) % p == 0)
            if p == 2:
                exp_a = 2 if k == 0 else 0
                exp_b = 1 if k == 0 else 0
            else:
                exp_a = 1 if k == 0 else na
                exp_b = 1 if k == 0 else nb
            assert ra == exp_a
            assert rb == exp_b

    print(f"PASS modular direction/root/survivor classifications: every prime <= {MOD_PRIME_MAX}")


def test_channel_divisor_congruence_witnesses():
    for p in primes_upto(MOD_PRIME_MAX):
        if p == 2 or (p > 2 and p % 4 == 1):
            found = False
            for r in range(p):
                if (r*r + 1) % p == 0:
                    assert A(r, 1) % p == 0
                    found = True
                    break
            if p == 2:
                assert A(1, 1) % 2 == 0
                found = True
            assert found
        if p == 3 or (p > 3 and p % 3 == 1):
            found = False
            for r in range(p):
                if (r*r - r + 1) % p == 0:
                    assert B(r, 1) % p == 0
                    found = True
                    break
            assert found
    print(f"PASS allowed prime-divisor classes have primitive witnesses through p<={MOD_PRIME_MAX}")


def simultaneous_prime(a, b):
    return is_prime(A(a, b)) and is_prime(B(a, b))


def test_simultaneous_prime_relations():
    count = 0
    for a in range(1, BOX_PRIME + 1):
        for b in range(1, BOX_PRIME + 1):
            if not simultaneous_prime(a, b):
                continue
            p, q = A(a, b), B(a, b)
            assert gcd(a, b) == 1
            if p > 2 and q > 3:
                assert p % 4 == 1
                assert q % 6 == 1
                assert (p % 8, q % 12) in {(1, 1), (5, 7)}
                assert (a-b) % p != 0
                assert (a+b) % p != 0
                assert (a-b) % q != 0
                assert (a+b) % q != 0
                assert legendre(2*q, p) == 1
                assert legendre(-2*q, p) == 1
                assert legendre(-p, q) == 1
                assert legendre(3*p, q) == 1
                common = legendre(q, p)
                assert common == legendre(p, q)
                assert common == legendre(2, p)
                assert common == legendre(-1, q)
                assert common == legendre(3, q)
                count += 1
    print(f"PASS simultaneous-prime congruence/reciprocity: {count} cells in box 1..{BOX_PRIME}")


NEIGHBOR_STEPS = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1))


def test_adjacency():
    nodes = {(a, b) for a in range(1, BOX_ADJ + 1) for b in range(1, BOX_ADJ + 1)
             if simultaneous_prime(a, b)}
    adj = {v: [] for v in nodes}
    for a, b in nodes:
        for da, db in NEIGHBOR_STEPS:
            w = (a + da, b + db)
            if w in nodes:
                adj[(a, b)].append(w)
                assert (da, db) in {(1, 1), (-1, -1)}
        assert len(adj[(a, b)]) <= 1

    seen = set()
    max_comp = 0
    for v in nodes:
        if v in seen:
            continue
        stack = [v]
        seen.add(v)
        size = 0
        while stack:
            z = stack.pop()
            size += 1
            for w in adj[z]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        max_comp = max(max_comp, size)
    assert max_comp <= 2

    b3 = [(a, b) for a in range(1, 20) for b in range(1, 20)
          if B(a, b) == 3 and simultaneous_prime(a, b)]
    assert set(b3) == {(1, 2), (2, 1)}
    assert (2, 3) in nodes and (3, 2) in nodes
    print(f"PASS sector-local adjacency: {len(nodes)} nodes, max component={max_comp}, box 1..{BOX_ADJ}; B=3 exceptions={b3}")


def prime_factors_squarefree(m):
    ps = []
    d = 2
    n = m
    while d*d <= n:
        if n % d == 0:
            ps.append(d)
            n //= d
            assert n % d != 0, f"{m} not squarefree"
        d += 1
    if n > 1:
        ps.append(n)
    return ps


def local_survivor_count(p):
    na = expected_projective_A_roots(p)
    nb = expected_projective_B_roots(p)
    return (p-1)*(p+1-na-nb)


def survivor(a, b, m):
    return gcd(A(a, b)*B(a, b), m) == 1


def test_finite_dimensional_reduction():
    for m in MODULI_2D:
        ps = prime_factors_squarefree(m)
        global_count = sum(1 for a in range(m) for b in range(m) if survivor(a, b, m))
        slice_counts = [sum(1 for t in range(m) if survivor(t+k, t, m)) for k in range(m)]
        assert sum(slice_counts) == global_count
        crt_count = 1
        for p in ps:
            crt_count *= local_survivor_count(p)
        assert global_count == crt_count
    print(f"PASS finite dimensional-reduction mean identity + squarefree CRT counts: M={MODULI_2D}")


def test_negative_cases():
    assert gcd(2, 2) == 2 and gcd(A(2, 2), B(2, 2)) == 4
    for n in range(1, 100):
        assert A(n, 0) == B(n, 0) == n*n
        assert not (is_prime(A(n, 0)) and is_prime(B(n, 0)))
        assert A(0, n) == B(0, n) == n*n
        assert not (is_prime(A(0, n)) and is_prime(B(0, n)))
    a, b = 2, 5
    assert (A(a, b), B(a, b)) == (A(b, a), B(b, a))
    n, r = carrier_mark(a, b)
    n2, r2 = carrier_mark(b, a)
    assert n == n2
    assert r2 == pow(r, -1, n)
    assert r != r2
    assert simultaneous_prime(1, 2) and simultaneous_prime(2, 3)
    assert (2, 3) == (1 + 1, 2 + 1)
    assert A(1, 1) == 2 and B(1, 1) == 1
    assert B(1, 2) == 3 and A(1, 2) == 5
    print("PASS mandatory negative/degeneracy tests")


def main():
    test_identities_and_recovery()
    test_marked_carrier()
    test_scalar_collision()
    test_modular_directions_and_slices()
    test_channel_divisor_congruence_witnesses()
    test_simultaneous_prime_relations()
    test_adjacency()
    test_finite_dimensional_reduction()
    test_negative_cases()
    print("ALL CHECKS PASS")


if __name__ == "__main__":
    main()
