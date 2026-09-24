#!/usr/bin/env python3
"""Exact certificate for a strict singleton-vs-LCM repair gap.

This checker verifies one finite symbolic witness. It is a certificate/regression
for the theorem note, not a substitute for its structural proof.
"""

P = 3181
D = 37
Q1 = 2221
Q2 = 3109
L = 555
SINGLE_Q2 = 111


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def factor(n):
    out = {}
    d = 2
    while d * d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                n //= d
                e += 1
            out[d] = e
        d += 1 if d == 2 else 2
    if n > 1:
        out[n] = 1
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
    o = order_mod(4, q)
    assert q % 24 == 13 and o % 2 == 0
    return o // 2


def c13(q):
    s = s13(q)
    e = 0
    x = pow(4, s) + 1
    while x % q == 0:
        x //= q
        e += 1
    return e


def delta13_odd(j, q):
    s = s13(q)
    if j % s == 0 and (j // s) % 2 == 1:
        return -c13(q)
    return vp(j, q)


def delta19_odd(j, r):
    return int(j % ((r - 1) // 2) == 0) + vp(j, r)


assert all(is_prime(x) for x in (P, D, Q1, Q2))
assert all(x % 24 == 13 for x in (P, D, Q1, Q2))
assert factor(L) == {3: 1, 5: 1, 37: 1}
assert factor(SINGLE_Q2) == {3: 1, 37: 1}

orders = {q: order_mod(4, q) for q in (13, 61, D, Q1, Q2, P)}
steps = {q: s13(q) for q in orders}
depths = {q: c13(q) for q in (D, Q1, Q2, P)}
assert orders[D] == 18 and steps[D] == 9
assert orders[Q1] == 1110 and steps[Q1] == 555 and depths[Q1] == 1
assert orders[Q2] == 222 and steps[Q2] == 111 and depths[Q2] == 1
assert orders[P] == 530 and steps[P] == 265 and depths[P] == 1
assert L % steps[Q1] == 0 and (L // steps[Q1]) % 2 == 1
assert L % steps[Q2] == 0 and (L // steps[Q2]) % 2 == 1
assert SINGLE_Q2 % steps[Q2] == 0
assert L % steps[P] != 0 and L % P != 0

# Exact class-19 neutrality below P.
class19 = [r for r in range(2, P) if is_prime(r) and r % 24 == 19]
assert all(delta19_odd(L, r) == 0 for r in class19)
assert all(delta19_odd(SINGLE_Q2, r) == 0 for r in class19)

# Exact class-13 signatures below/at P.
class13 = [q for q in range(2, P + 1) if is_prime(q) and q % 24 == 13]
sigL = {q: delta13_odd(L, q) for q in class13}
sig111 = {q: delta13_odd(SINGLE_Q2, q) for q in class13}
positive_L = {q: v for q, v in sigL.items() if v > 0}
negative_L = {q: v for q, v in sigL.items() if v < 0}
assert positive_L == {37: 1}
assert negative_L == {13: -1, 61: -1, 2221: -1, 3109: -1}
assert sigL[P] == 0
assert sig111[D] == 1 and sig111[Q2] == -1 and sig111[Q1] == 0

# Residual state b: two clean demands, one unit of dirty slack, all other
# earlier class-13 rows nonpositive. Use zero for all unspecified rows.
b = {q: 0 for q in class13 if q < P}
b[Q1] = 1
b[Q2] = 1
b[D] = -1

# Descending singleton policy: q2 first uses 111, q1 then uses 555.
single_final = {q: b[q] + sig111[q] + sigL[q] for q in b}
assert single_final[Q2] <= 0 and single_final[Q1] <= 0
assert single_final[D] == 1

# One shared LCM atom L=555 closes both clean rows and spends dirty slack once.
shared_final = {q: b[q] + sigL[q] for q in b}
assert shared_final[Q1] == 0
assert shared_final[Q2] == 0
assert shared_final[D] == 0
assert all(v <= 0 for v in shared_final.values())
assert sigL[P] == 0
assert all(delta19_odd(L, r) == 0 for r in class19)

print({
    "target": P,
    "dirty_row": D,
    "clean_rows": [Q1, Q2],
    "steps": {Q1: steps[Q1], Q2: steps[Q2], P: steps[P]},
    "shared_lcm_core": L,
    "shared_signature_nonzero": {q: v for q, v in sigL.items() if v},
    "singleton_dirty_final": single_final[D],
    "shared_dirty_final": shared_final[D],
    "earlier_class19_positive": 0,
    "failures": 0,
})
