#!/usr/bin/env python3
"""Exact regression for the BRC base-3 universal-backbone criterion.

Finite computation is falsification/regression only. The theorem is proved in
the paired note. No network access or probabilistic primality is used.
"""
from math import lcm

LIMIT = 5000


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
    s = o // 2
    assert s % 2 == 1
    return s


def class13_below(P):
    return [q for q in PRIMES if q < P and q % 24 == 13]


def class19_below(P):
    return [r for r in PRIMES if r < P and r % 24 == 19]


def neutral19(j, P):
    return all(j % r != 0 and j % ((r - 1)//2) != 0
               for r in class19_below(P))


def three_compatible_rows(P):
    return [q for q in class13_below(P)
            if neutral19(lcm(3, s13(q)), P)]


def backbone_core(P):
    C = 1
    for q in three_compatible_rows(P):
        C = lcm(C, s13(q))
    return C


def pure_core(C, P):
    for q in class13_below(P):
        if C % s13(q) != 0 and C % q == 0:
            return False
    return True


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


def c13(q):
    return v_p(pow(4, s13(q)) + 1, q)


def signature(L, P):
    return tuple(-c13(q) if L % s13(q) == 0 else v_p(L, q)
                 for q in class13_below(P))


def leq(u, v):
    return all(a <= b for a, b in zip(u, v))


def main():
    expected = {
        397: 175305,
        733: 10342995,
        1021: 3270072328185,
        1117: 4947619432543905,
    }
    v3_checks = 0
    for P, expected_C in expected.items():
        C = backbone_core(P)
        assert C == expected_C
        assert neutral19(C, P)
        assert pure_core(C, P)
        atoms = atom_library(P)
        v3 = [L for L in atoms if L % 3 == 0]
        assert C in atoms
        aC = signature(C, P)
        assert all(leq(aC, signature(L, P)) for L in v3)
        v3_checks += len(v3)

    P = 2221
    assert s13(61) == 15
    assert s13(853) == 213
    assert neutral19(15, P)
    assert neutral19(213, P)

    r = 2131
    assert r in PRIMES and r % 24 == 19 and r < P
    h = (r - 1)//2
    assert h == 1065
    assert lcm(15, 213) == 1065

    U3 = three_compatible_rows(P)
    assert 61 in U3 and 853 in U3
    C = backbone_core(P)
    assert C % 1065 == 0
    assert not neutral19(C, P)

    prior = [p for p in PRIMES if 13 < p <= P and p % 24 == 13]
    failures = []
    for p in prior:
        Cp = backbone_core(p)
        if not (neutral19(Cp, p) and pure_core(Cp, p)):
            failures.append(p)
    assert failures == [2221]

    print("PASS")
    print(f"moderate_v3_atom_checks={v3_checks}")
    print(f"three_compatible_rows_p2221={len(U3)}")
    print("p2221_forbidden_class19_prime=2131")
    print("p2221_forbidden_endpoint=1065")
    print("p2221_shared_pair=s61=15,s853=213")
    print("regression_failures_through_2221=[2221]")


if __name__ == "__main__":
    main()
