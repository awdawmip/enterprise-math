#!/usr/bin/env python3
"""Exact certificate for target-blind LCM dominance at p=397.

This is a finite exact certificate for the example in the paired research note.
The structural quotient/dominance/redundancy theorems are proved in the note.
"""

from math import lcm

P = 397
LIMIT = 5000


def sieve(n):
    a = [True] * (n + 1)
    a[0] = a[1] = False
    for k in range(2, int(n ** 0.5) + 1):
        if a[k]:
            a[k * k:n + 1:k] = [False] * (((n - k * k) // k) + 1)
    return [k for k, ok in enumerate(a) if ok]


PRIMES = sieve(LIMIT)


def factor(n):
    out = {}
    d = 2
    x = n
    while d * d <= x:
        if x % d == 0:
            e = 0
            while x % d == 0:
                x //= d
                e += 1
            out[d] = e
        d = 3 if d == 2 else d + 2
    if x > 1:
        out[x] = 1
    return out


def vp(n, p):
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
    assert q % 24 == 13
    o = order_mod(4, q)
    assert o % 2 == 0
    s = o // 2
    assert s % 2 == 1
    return s


def c13(q):
    return vp(pow(4, s13(q)) + 1, q)


def class13_le(p):
    return [q for q in PRIMES if q <= p and q % 24 == 13]


def class13_lt(p):
    return [q for q in PRIMES if q < p and q % 24 == 13]


def class19_lt(p):
    return [r for r in PRIMES if r < p and r % 24 == 19]


def neutral19(j, p):
    return all(
        j % r != 0 and j % ((r - 1) // 2) != 0
        for r in class19_lt(p)
    )


def full_atom_library(p):
    clean_steps = sorted({
        s13(q) for q in class13_le(p) if neutral19(s13(q), p)
    })
    atoms = {1}
    for s in clean_steps:
        nxt = set(atoms)
        for L in atoms:
            M = lcm(L, s)
            if neutral19(M, p):
                nxt.add(M)
        atoms = nxt
    atoms.discard(1)
    return sorted(atoms)


Q = class13_lt(P)


def earlier_support(L):
    return tuple(q for q in Q if L % s13(q) == 0)


def earlier_core(L):
    out = 1
    for q in earlier_support(L):
        out = lcm(out, s13(q))
    return out


def signature(L):
    return tuple(
        -c13(q) if L % s13(q) == 0 else vp(L, q)
        for q in Q
    )


def le_vec(a, b):
    return all(x <= y for x, y in zip(a, b))


def add_vec(*vecs):
    return tuple(sum(xs) for xs in zip(*vecs))


FULL = full_atom_library(P)
TARGET_BLIND = sorted({earlier_core(L) for L in FULL if earlier_core(L) > 1})
SIG = {L: signature(L) for L in TARGET_BLIND}

# Exact target-blind quotient.
assert len(FULL) == 23
assert len(TARGET_BLIND) == 19
for L in FULL:
    E = earlier_core(L)
    assert E == 1 or E in TARGET_BLIND
    assert L % E == 0
    assert neutral19(E, P)
    if E > 1:
        assert earlier_support(E) == earlier_support(L)
        assert le_vec(signature(E), signature(L))

# Fixed-point and same-support uniqueness.
for L in TARGET_BLIND:
    assert earlier_core(L) == L
for L in TARGET_BLIND:
    for M in TARGET_BLIND:
        if earlier_support(L) == earlier_support(M):
            assert L == M

# Pairwise dominance theorem:
# a(M) <= a(L) iff support(L) subset support(M) and all denominator
# valuations agree outside support(M).
pair_checks = 0
for L in TARGET_BLIND:
    for M in TARGET_BLIND:
        lhs = le_vec(SIG[M], SIG[L])
        AM = set(earlier_support(M))
        AL = set(earlier_support(L))
        rhs = AL <= AM and all(
            vp(M, q) == vp(L, q) for q in Q if q not in AM
        )
        assert lhs == rhs
        pair_checks += 1

UNDOMINATED = [
    L for L in TARGET_BLIND
    if not any(
        M != L and le_vec(SIG[M], SIG[L])
        for M in TARGET_BLIND
    )
]
assert UNDOMINATED == [23, 299, 175305]


def sparse(v):
    return {q: x for q, x in zip(Q, v) if x}


assert sparse(SIG[23]) == {277: -1}
assert sparse(SIG[299]) == {13: 1, 157: -1, 277: -1}
assert sparse(SIG[175305]) == {
    13: -1, 61: -1, 157: -1, 349: -1, 373: -1
}

# Pairwise antichain is not semigroup-minimal.
assert le_vec(add_vec(SIG[23], SIG[175305]), SIG[299])
assert le_vec(add_vec(SIG[299], SIG[175305]), SIG[23])

# Every target-blind atom is pairwise dominated by one undominated atom.
for L in TARGET_BLIND:
    assert any(le_vec(SIG[U], SIG[L]) for U in UNDOMINATED)

# Hence either pair below preserves every atom effect:
# if 299 was the chosen pairwise dominator, replace it by 23+175305;
# if 23 was chosen, replace it by 299+175305.
for L in TARGET_BLIND:
    assert (
        le_vec(SIG[23], SIG[L])
        or le_vec(SIG[175305], SIG[L])
        or le_vec(add_vec(SIG[23], SIG[175305]), SIG[L])
    )
    assert (
        le_vec(SIG[299], SIG[L])
        or le_vec(SIG[175305], SIG[L])
        or le_vec(add_vec(SIG[299], SIG[175305]), SIG[L])
    )

# No singleton target-blind atom can preserve both essential effects.
# Any positive multiple k*a(M) that simulates a(23) must cancel row 277.
# Any positive multiple that simulates a(175305) must cancel every negative
# row of a(175305). Multiplicity cannot create a cancellation at a zero/non-
# cancelled coordinate. Hence a singleton carrier would need the union below
# in its cancellation support. The finite target-blind library has none.
required_union = {13, 61, 157, 277, 349, 373}
assert not any(
    required_union <= set(earlier_support(M))
    for M in TARGET_BLIND
)

print({
    "target": P,
    "full_lcm_atoms": len(FULL),
    "target_blind_atoms": len(TARGET_BLIND),
    "pairwise_dominance_checks": pair_checks,
    "pairwise_undominated": UNDOMINATED,
    "pairwise_undominated_count": len(UNDOMINATED),
    "exact_two_generator_carriers": [[23, 175305], [299, 175305]],
    "minimum_generator_count_certificate": 2,
    "failures": 0,
})
