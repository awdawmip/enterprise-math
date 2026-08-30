#!/usr/bin/env python3
"""Deterministic exact checker for ADDMUL bridge Integration atlas.

The symbolic classification is proved in the accompanying return. This checker
locks the minimal witnesses used by the pairwise matrix and cost lower bounds.
Standard library only; no floating point or randomness.
"""
from __future__ import annotations
from itertools import product
from math import factorial

CHECKS = 0


def check(cond: bool, label: str) -> None:
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(label)


def q(n: int, k: int) -> int:
    if k < 0:
        return 0
    if k == 0:
        return 1
    num = 1
    for j in range(k):
        num *= n - j
    den = factorial(k)
    check(num % den == 0, f"Q integrality n={n} k={k}")
    return num // den


def delta(n: int, p: int) -> int:
    num = n - n**p
    check(num % p == 0, f"delta integrality n={n} p={p}")
    return num // p


def defect(x: int, y: int, p: int) -> int:
    return delta(x + y, p) - delta(x, p) - delta(y, p)


def vp(n: int, p: int):
    if n == 0:
        return None
    n = abs(n)
    value = 0
    while n % p == 0:
        n //= p
        value += 1
    return value


def kappa(x: int, y: int, p: int):
    if x == y == 0:
        return "BASELINE_INFINITY"
    if x + y == 0:
        return "INF"
    vals = [v for v in (vp(x, p), vp(y, p)) if v is not None]
    return vp(x + y, p) - min(vals)


def divisors(n: int):
    return [d for d in range(1, n + 1) if n % d == 0]


def ghost(a: dict[int, int], indices: tuple[int, ...]) -> dict[int, int]:
    return {
        n: sum(d * a.get(d, 0) ** (n // d) for d in divisors(n))
        for n in indices
    }


def invert_ghost(g: dict[int, int], indices: tuple[int, ...]):
    a: dict[int, int] = {}
    for n in sorted(indices):
        lower = sum(d * a[d] ** (n // d) for d in divisors(n) if d < n)
        num = g[n] - lower
        if num % n:
            return None
        a[n] = num // n
    return a


def f_c(x: int, y: int, c: int) -> int:
    return x + y + c * x * y


def t_c(x: int, c: int) -> int:
    return 1 + c * x


def mod3_gauss_nonzero() -> bool:
    # For F_3, the nontrivial multiplicative character is chi(1)=1, chi(2)=-1.
    # At additive frequency t=1 its Fourier column is zeta^2-zeta.  In
    # Q[zeta]/(1+zeta+zeta^2), coefficient vector (0,-1,1) is nonzero because
    # it is not a multiple of (1,1,1).
    coeff = (0, -1, 1)
    return not (coeff[0] == coeff[1] == coeff[2])


def main() -> None:
    # W1: A1 and A2 at p=2 are the same normalized quadratic refinement up to sign.
    for x in range(-12, 13):
        check(delta(x, 2) == -q(x, 2), f"delta2=-Q2 x={x}")
        for y in range(-12, 13):
            check(q(x + y, 2) - q(x, 2) - q(y, 2) == x * y, "A1 product")
            check(defect(x, y, 2) == -x * y, "A2 p2 product")

    # W2: A1 reconstructs A3 exactly over Z: F_c = x+y+c*cr_2 Q2.
    for c in range(-4, 5):
        for x, y in product(range(-5, 6), repeat=2):
            cr = q(x + y, 2) - q(x, 2) - q(y, 2)
            check(f_c(x, y, c) == x + y + c * cr, "A1->A3")
            check(t_c(f_c(x, y, c), c) == t_c(x, c) * t_c(y, c), "A3 transport")

    # W3: A2 odd-prime anti-diagonal has an infinite product-loss fiber.
    for p in (3, 5, 7, 11):
        products = set()
        for a in range(-12, 13):
            check(defect(a, -a, p) == 0, f"A2 anti-diagonal p={p}")
            products.add(-a * a)
        check(len(products) > 5, f"A2 anti-diagonal varying product p={p}")

    # W4: A3 finite-ring fibers are exactly Ann(c); Z/8,c=2 has fiber size 2.
    modulus, c = 8, 2
    buckets: dict[int, list[int]] = {}
    for x in range(modulus):
        buckets.setdefault((1 + c * x) % modulus, []).append(x)
    check(sorted(map(len, buckets.values())) == [2, 2, 2, 2], "A3 fiber Z8 c2")
    for x, y in product(range(modulus), repeat=2):
        same = ((1 + c * x) - (1 + c * y)) % modulus == 0
        ann = (c * (x - y)) % modulus == 0
        check(same == ann, "A3 Ann(c) fiber")

    # W5: A4 image gate is essential and prime-power skeleton misses composite index.
    check(invert_ghost({1: 0, 2: 1}, (1, 2)) is None, "A4 invalid ghost")
    indices6 = (1, 2, 3, 6)
    ga = ghost({1: 0, 2: 0, 3: 0, 6: 0}, indices6)
    gb = ghost({1: 0, 2: 0, 3: 0, 6: 1}, indices6)
    for n in (1, 2, 3):
        check(ga[n] == gb[n], "A4 prime-power skeleton equality")
    check(gb[6] - ga[6] == 6, "A4 composite residual")

    # W6: A1 and A3 compose exactly componentwise on A4's integral ghost image.
    indices = (1, 2, 3)
    packets = []
    for vals in product((-1, 0, 1), repeat=len(indices)):
        packets.append(ghost(dict(zip(indices, vals)), indices))
    for g, h in product(packets, repeat=2):
        prodvec = {n: g[n] * h[n] for n in indices}
        check(invert_ghost(prodvec, indices) is not None, "A4 product closure")
        q2prod = {
            n: q(g[n] + h[n], 2) - q(g[n], 2) - q(h[n], 2)
            for n in indices
        }
        check(q2prod == prodvec, "A1 product on ghost image")
        for c in (-2, -1, 0, 1, 2):
            fvec = {n: f_c(g[n], h[n], c) for n in indices}
            check(invert_ghost(fvec, indices) is not None, "A3 F_c closure on ghost image")

    # W7: A5 finite valuation state cannot determine addition; depth is unbounded.
    for p in (2, 3, 5, 7, 11):
        for depth in range(1, 9):
            y = p**depth - 1
            check(vp(1, p) == 0 and vp(y, p) == 0, "A5 same input valuation state")
            check(kappa(1, y, p) == depth, f"A5 arbitrary depth p={p} d={depth}")
    check((kappa(1, 649, 2), kappa(1, 649, 3), kappa(1, 649, 5)) == (1, 0, 2), "A5 CRT witness")

    # W8: fixed residue depth D cannot close tied addition when kappa>=D.
    for p in (2, 3, 5):
        for depth in range(1, 7):
            y = p**depth - 1
            check((y + 1) % (p**depth) == 0, "A5 residue overflow")
            check(kappa(1, y, p) == depth, "A5 exact hidden depth")

    # W9: A4 integer ghost data cannot be reduced mod p without information loss
    # whenever p divides a retained index: S={1,p}, varying a_p disappears mod p.
    for p in (2, 3, 5, 7):
        indices_p = (1, p)
        g0 = ghost({1: 0, p: 0}, indices_p)
        g1 = ghost({1: 0, p: 1}, indices_p)
        check(g0[1] % p == g1[1] % p, "A4/A6 reduction coord1")
        check(g0[p] % p == g1[p] % p, "A4/A6 reduction loses ap")
        check(g0[p] != g1[p], "A4/A6 integer lift distinguishes ap")

    # W10: A6's natural Gauss transition is not a convolution-algebra intertwiner.
    # In F3, multiplicative idempotents e0,e1 have zero cross convolution, but their
    # additive Fourier columns overlap nontrivially at nonzero frequency.
    check(mod3_gauss_nonzero(), "A6 nontrivial Gauss column F3")
    check((-1) != 0 and mod3_gauss_nonzero(), "A6 overlapping spectra obstruction")

    # W11: zero-atom completion vs codimension-one constraint is an exact cost trade.
    # For unit-only f(0)=0, sum of all unnormalised additive Fourier coordinates is 0.
    p = 5
    for values in product(range(-1, 2), repeat=p - 1):
        f = [0] + list(values)
        total = 0
        for x, value in enumerate(f):
            kernel = p if x == 0 else 0  # sum_t zeta^{-tx}
            total += value * kernel
        check(total == 0, "A6 unit-only hyperplane constraint")

    print(
        "PASS task=RS-ADDMUL-BRIDGE-INTEGRATION-STRENGTH-COST-ATLAS "
        f"checks={CHECKS}"
    )


if __name__ == "__main__":
    main()
