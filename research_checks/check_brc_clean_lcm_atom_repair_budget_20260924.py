#!/usr/bin/env python3
"""
Exact regression for the BRC clean-step finite LCM-atom repair theorem.

This is falsification/regression only. The proof is in the paired research note.
No network access and no probabilistic primality are used.
"""
from math import lcm
import random

LIMIT = 3000


def sieve(n):
    a = [True] * (n + 1)
    a[0] = a[1] = False
    for k in range(2, int(n ** 0.5) + 1):
        if a[k]:
            a[k*k:n+1:k] = [False] * (((n - k*k)//k) + 1)
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


def delta13_singleton(j, q):
    # j is odd. The class-13 endpoint h_q=(q-1)/2 is even, so it is absent.
    s = s13(q)
    if j % s == 0:
        return -c13(q)
    return v_p(j, q)


def canonical_core(j, P):
    L = 1
    for q in class13(P):
        s = s13(q)
        if j % s == 0:
            L = lcm(L, s)
    return L


def fresh_prime_over(P, avoid):
    for ell in PRIMES:
        if ell > P and ell not in avoid:
            return ell
    raise RuntimeError("LIMIT too small for fresh-prime test")


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


def main():
    # Exact exhaustive canonicalization on one nontrivial horizon.
    P = 397
    qrows = class13(P)
    exhaustive = 0
    for j in range(1, 200000, 2):
        if not neutral19(j, P):
            continue
        L = canonical_core(j, P)
        exhaustive += 1
        assert j % L == 0
        assert neutral19(L, P)
        A_j = tuple(q for q in qrows if j % s13(q) == 0)
        A_L = tuple(q for q in qrows if L % s13(q) == 0)
        assert A_j == A_L
        for q in qrows:
            assert delta13_singleton(L, q) <= delta13_singleton(j, q)

    # Deterministic randomized stress on larger horizons, using exact integers.
    rng = random.Random(20260924)
    random_cases = 0
    atom_budget_checks = 0
    for P in (157, 277, 397, 733, 1021):
        qrows = class13(P)
        clean = [q for q in qrows if neutral19(s13(q), P)]
        for _ in range(600):
            chosen = [q for q in clean if rng.random() < 0.25]
            if not chosen:
                chosen = [rng.choice(clean)]
            j = 1
            for q in chosen:
                j = lcm(j, s13(q))
            for a in (3, 5, 7, 11, 13, 17, 23, 29, 31, 37, 41, 47, 53):
                if rng.random() < 0.08:
                    j *= a ** rng.randint(1, 2)
            if not neutral19(j, P):
                continue

            L = canonical_core(j, P)
            random_cases += 1
            assert j % L == 0 and neutral19(L, P)
            for q in qrows:
                assert delta13_singleton(L, q) <= delta13_singleton(j, q)

            # A fresh-prime lift has exactly the core signature on every q<=P.
            ell = fresh_prime_over(P, set(factor(L)))
            lift = L * ell
            assert neutral19(lift, P)
            for q in qrows:
                assert delta13_singleton(lift, q) == delta13_singleton(L, q)

            # A target-cancelling core has an exact target-only p-adic compensator.
            if P % 24 == 13 and P in PRIMES and L % s13(P) == 0:
                cp = c13(P)
                ell2 = fresh_prime_over(P, set(factor(L)) | {ell})
                comp = (P ** cp) * ell2
                assert delta13_singleton(comp, P) == cp
                for q in qrows:
                    if q < P:
                        assert delta13_singleton(comp, q) == 0
                assert neutral19(comp, P)
                assert delta13_singleton(lift, P) + delta13_singleton(comp, P) == 0

            # Exact atom budget coordinates.
            for q in qrows:
                a = delta13_singleton(L, q)
                if L % s13(q) == 0:
                    assert a == -c13(q)
                else:
                    assert a == v_p(L, q) >= 0
                if not neutral19(s13(q), P):
                    assert L % s13(q) != 0
                    assert a == v_p(L, q) >= 0
                atom_budget_checks += 1

    # Enumerate the full finite atom library for a small horizon and verify the
    # exact shared-support budget identities for random integer combinations.
    P = 397
    qrows = class13(P)
    atoms = atom_library(P)
    assert atoms
    for L in atoms:
        assert neutral19(L, P)
        assert canonical_core(L, P) == L
    rng2 = random.Random(39720260924)
    budget_vectors = 0
    for _ in range(500):
        x = {L: rng2.randrange(0, 4) for L in atoms}
        for q in qrows:
            direct = sum(delta13_singleton(L, q) * n for L, n in x.items())
            Nq = sum(n for L, n in x.items() if L % s13(q) == 0)
            Dq = sum(v_p(L, q) * n for L, n in x.items() if L % s13(q) != 0)
            assert direct == -c13(q) * Nq + Dq
            if not neutral19(s13(q), P):
                assert Nq == 0
                assert direct == Dq >= 0
            budget_vectors += 1

    print("PASS")
    print(f"exhaustive_neutral_ports={exhaustive}")
    print(f"random_neutral_ports={random_cases}")
    print(f"atom_budget_coordinate_checks={atom_budget_checks}")
    print(f"atom_library_P397={len(atoms)}")
    print(f"shared_budget_vector_checks={budget_vectors}")


if __name__ == "__main__":
    main()
