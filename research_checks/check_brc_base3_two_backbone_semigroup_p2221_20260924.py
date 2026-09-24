#!/usr/bin/env python3
"""Exact p=2221 regression for the base-3 two-backbone repair theorem.

Finite computation is an exact certificate for the stated p=2221 instance.
The paired note contains the structural argument. No network or probabilistic
primality is used.
"""
from math import lcm

LIMIT = 5000
P = 2221


def sieve(n):
    a = [True] * (n + 1)
    a[0] = a[1] = False
    for k in range(2, int(n ** 0.5) + 1):
        if a[k]:
            a[k*k:n+1:k] = [False] * (((n-k*k)//k) + 1)
    return [k for k, ok in enumerate(a) if ok]


PRIMES = sieve(LIMIT)


def factor(n):
    out = {}
    x = n
    for p in PRIMES:
        if p*p > x:
            break
        if x % p == 0:
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            out[p] = e
        if x == 1:
            break
    if x > 1:
        out[x] = 1
    return out


def v_p(n, p):
    e = 0
    while n and n % p == 0:
        n //= p
        e += 1
    return e


def order_mod(a, p):
    o = p - 1
    for r, e in factor(p - 1).items():
        for _ in range(e):
            if o % r == 0 and pow(a, o // r, p) == 1:
                o //= r
            else:
                break
    return o


def s13(q):
    o = order_mod(4, q)
    assert o % 2 == 0
    return o // 2


def c13(q):
    return v_p(pow(4, s13(q)) + 1, q)


def class13_below(P):
    return [q for q in PRIMES if q < P and q % 24 == 13]


def class19_below(P):
    return [r for r in PRIMES if r < P and r % 24 == 19]


def neutral19(L, P):
    return all(L % r != 0 and L % ((r - 1)//2) != 0
               for r in class19_below(P))


def three_compatible_rows(P):
    return [q for q in class13_below(P)
            if neutral19(lcm(3, s13(q)), P)]


def atom_library(P):
    clean_steps = sorted({s13(q) for q in class13_below(P)
                          if neutral19(s13(q), P)})
    atoms = {1}
    for s in clean_steps:
        nxt = set(atoms)
        for L in atoms:
            M = lcm(L, s)
            if neutral19(M, P):
                nxt.add(M)
        atoms = nxt
    atoms.discard(1)
    return sorted(atoms)


def signature(L, P):
    return tuple(-c13(q) if L % s13(q) == 0 else v_p(L, q)
                 for q in class13_below(P))


def leq(u, v):
    return all(a <= b for a, b in zip(u, v))


def cancellation_support(L, P):
    return frozenset(q for q in three_compatible_rows(P)
                     if L % s13(q) == 0)


def canonical_lcm(S):
    L = 3
    for q in S:
        L = lcm(L, s13(q))
    return L


def pure(L, P):
    return all(not (L % q == 0 and L % s13(q) != 0)
               for q in class13_below(P))


def minimal_conflicts(U, P):
    bad = set()
    n = len(U)
    for mask in range(1, 1 << n):
        S = [U[i] for i in range(n) if mask >> i & 1]
        if not neutral19(canonical_lcm(S), P):
            bad.add(mask)
    out = []
    for mask in bad:
        mm = mask
        minimal = True
        while mm:
            bit = mm & -mm
            if (mask ^ bit) in bad:
                minimal = False
                break
            mm -= bit
        if minimal:
            out.append(tuple(U[i] for i in range(n) if mask >> i & 1))
    return sorted(out)


def main():
    U = three_compatible_rows(P)
    expected_U = [
        13, 61, 157, 349, 373, 709, 733, 853,
        877, 1021, 1069, 1213, 1741, 1789, 1861, 2029,
    ]
    assert U == expected_U

    conflicts = minimal_conflicts(U, P)
    expected_conflicts = [
        (61, 853),
        (853, 1021),
        (853, 1741),
        (853, 1861),
    ]
    assert conflicts == expected_conflicts

    # The first shared obstruction used by the theorem is the exact endpoint
    # 1065=(2131-1)/2 generated jointly by q=61 and q=853.
    assert s13(61) == 15
    assert s13(853) == 213
    assert lcm(3, s13(61), s13(853)) == 1065
    assert 2131 in class19_below(P)
    assert (2131 - 1)//2 == 1065

    A_support = frozenset(q for q in U if q != 853)
    B_support = frozenset(
        [13, 157, 349, 373, 709, 733, 853, 877,
         1069, 1213, 1789, 2029]
    )
    A = canonical_lcm(A_support)
    B = canonical_lcm(B_support)
    assert A == 13632921449642140035
    assert B == 11387499093230493441
    assert neutral19(A, P) and neutral19(B, P)
    assert cancellation_support(A, P) == A_support
    assert cancellation_support(B, P) == B_support
    assert A_support | B_support == frozenset(U)

    rows = class13_below(P)
    aA = signature(A, P)
    aB = signature(B, P)
    assert pure(A, P)
    assert not pure(B, P)
    positive_B = [(q, aB[i]) for i, q in enumerate(rows) if aB[i] > 0]
    assert positive_B == [(61, 1)]
    assert aA[rows.index(61)] == -1
    aAB = tuple(x + y for x, y in zip(aA, aB))
    assert aAB[rows.index(61)] == 0

    atoms = atom_library(P)
    V3 = [L for L in atoms if L % 3 == 0]
    assert len(V3) == 3072

    direct = compensated = 0
    for L in V3:
        aL = signature(L, P)
        supp = cancellation_support(L, P)
        if 853 not in supp:
            assert leq(aA, aL)
            direct += 1
        else:
            # The exact hyperedge (61,853) forbids simultaneous cancellation.
            assert 61 not in supp
            assert leq(aAB, aL)
            compensated += 1

    assert (direct, compensated) == (2304, 768)

    # One generator cannot dominate the whole sector: every q in U is
    # individually cancellable, so a single generator would have to cancel
    # every q in U, but no neutral V3 atom has that support.
    full = frozenset(U)
    assert not any(cancellation_support(L, P) == full for L in V3)

    print("PASS")
    print(f"p={P}")
    print(f"three_compatible_rows={len(U)}")
    print(f"minimal_conflicts={conflicts}")
    print(f"v3_atoms={len(V3)}")
    print(f"A={A}")
    print(f"B={B}")
    print(f"direct_A={direct}")
    print(f"compensated_A_plus_B={compensated}")
    print("minimum_batch_cover=2")
    print("minimum_semigroup_carrier=2")


if __name__ == "__main__":
    main()
