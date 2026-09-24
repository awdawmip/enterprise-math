#!/usr/bin/env python3
"""Exact regression for the BRC three-sector backbone / compensated-star theorem.

Finite computation is falsification/regression only. The proof is in the paired note.
No network access and no probabilistic primality are used.
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


def c13(q):
    s = s13(q)
    return v_p(pow(4, s) + 1, q)


def class13(P):
    return [q for q in PRIMES if q <= P and q % 24 == 13]


def class19_below(P):
    return [r for r in PRIMES if r < P and r % 24 == 19]


def neutral19(j, P):
    return all(j % r != 0 and j % ((r - 1)//2) != 0 for r in class19_below(P))


def atom_library(P):
    clean_steps = sorted({s13(q) for q in class13(P) if neutral19(s13(q), P)})
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


def rows(P):
    return [q for q in class13(P) if q < P]


def signature(L, P):
    return tuple(-c13(q) if L % s13(q) == 0 else v_p(L, q) for q in rows(P))


def leq(u, v):
    return all(a <= b for a, b in zip(u, v))


def pure(L, P):
    return all(x <= 0 for x in signature(L, P))


def pareto_count(P, atoms):
    sigs = sorted(set(signature(L, P) for L in atoms))
    pareto = []
    for v in sigs:
        if not any(u != v and leq(u, v) for u in sigs):
            pareto.append(v)
    return len(sigs), len(pareto)


def universal_singletons(P, atoms):
    out = []
    sigmap = {L: signature(L, P) for L in atoms}
    for L in atoms:
        if all(leq(sigmap[L], sigmap[K]) for K in atoms):
            out.append(L)
    return out


def verify_star(P, A, C):
    atoms = atom_library(P)
    assert A in atoms and C in atoms
    assert A % 3 != 0 and C % 3 == 0
    assert pure(C, P)

    aA = signature(A, P)
    aC = signature(C, P)
    aAC = tuple(x + y for x, y in zip(aA, aC))

    sector3 = [L for L in atoms if L % 3 == 0]
    sector0 = [L for L in atoms if L % 3 != 0]
    assert sector3 and sector0

    assert all(leq(aC, signature(L, P)) for L in sector3)
    assert all(leq(aAC, signature(L, P)) for L in sector0)

    for L in atoms:
        witness = aC if L % 3 == 0 else aAC
        assert leq(witness, signature(L, P))

    assert universal_singletons(P, atoms) == []
    return atoms


def main():
    expected = {
        397: (23, 20, 3, 23, 175305),
        733: (79, 63, 3, 253, 10342995),
        1021: (447, 288, 5, 20999, 3270072328185),
        1117: (959, 959, 5, 1910909, 4947619432543905),
    }

    total_atom_checks = 0
    for P, (na, ns, npareto, A, C) in expected.items():
        atoms = verify_star(P, A, C)
        distinct, pareto = pareto_count(P, atoms)
        assert (len(atoms), distinct, pareto) == (na, ns, npareto)
        total_atom_checks += len(atoms)

    P = 1117
    q = 1093
    assert q in rows(P)
    assert s13(q) == 91
    assert c13(q) == 2
    assert factor(91) == {7: 1, 13: 1}
    assert neutral19(91, P)

    assert s13(13) == 3
    assert 547 in PRIMES and 547 % 24 == 19
    assert (547 - 1)//2 == 273
    assert lcm(3, 91) == 273
    assert not neutral19(273, P)

    atoms = atom_library(P)
    q1093_pure = [L for L in atoms if L % s13(q) == 0 and pure(L, P)]
    assert q1093_pure == []

    A = 1910909
    C = 4947619432543905
    qrows = rows(P)
    sigA = dict(zip(qrows, signature(A, P)))
    sigC = dict(zip(qrows, signature(C, P)))
    assert sigA[13] == 1
    assert sigA[1093] == -2
    assert sigC[13] == -1
    assert sigC[1093] == 0
    assert sigA[13] + sigC[13] == 0

    print("PASS")
    print(f"star_horizons={len(expected)}")
    print(f"total_atom_sector_checks={total_atom_checks}")
    print("p1117_q1093_pure_cover_atoms=0")
    print("p1117_compensated_debt_q13=+1-1=0")
    print("p1117_q1093_credit=-2")


if __name__ == "__main__":
    main()
