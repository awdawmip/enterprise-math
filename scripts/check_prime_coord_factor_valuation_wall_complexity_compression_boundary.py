#!/usr/bin/env python3
"""Exact bounded regression for PCF5 valuation-wall complexity compression.

The checker validates the block-factorial identity used by the proof, not the
asymptotic cost of this small Python reference implementation.  Polynomial
construction/evaluation below is deliberately elementary so the residue checks
are independent of any fast-polynomial library.
"""

from math import comb, gcd, isqrt


def primes_upto(n: int) -> list[int]:
    out: list[int] = []
    for x in range(2, n + 1):
        if all(x % d for d in range(2, isqrt(x) + 1)):
            out.append(x)
    return out


def poly_mul_linear(coeffs: list[int], a: int, mod: int) -> list[int]:
    """Return coeffs * (X+a) modulo mod, coefficients low-to-high."""
    out = [0] * (len(coeffs) + 1)
    for i, c in enumerate(coeffs):
        out[i] = (out[i] + c * a) % mod
        out[i + 1] = (out[i + 1] + c) % mod
    return out


def poly_eval(coeffs: list[int], x: int, mod: int) -> int:
    value = 0
    for c in reversed(coeffs):
        value = (value * x + c) % mod
    return value


def block_factorial_mod(k: int, mod: int) -> int:
    """Strassen-style block identity for k! mod mod.

    Let m=ceil(sqrt(k)) and Q(X)=prod_{j=1}^m (X+j).  Then
    prod_i Q(im), followed by the <m leftover factors, is exactly k!.
    The production proof replaces these elementary polynomial operations by
    product-tree / multipoint algorithms over Z/mod Z.
    """
    if k <= 1:
        return 1 % mod
    m = isqrt(k)
    if m * m < k:
        m += 1
    q = [1]
    for j in range(1, m + 1):
        q = poly_mul_linear(q, j, mod)
    blocks = k // m
    acc = 1 % mod
    for i in range(blocks):
        acc = (acc * poly_eval(q, i * m, mod)) % mod
    for r in range(blocks * m + 1, k + 1):
        acc = (acc * r) % mod
    return acc


def direct_factorial_mod(k: int, mod: int) -> int:
    acc = 1 % mod
    for j in range(1, k + 1):
        acc = (acc * j) % mod
    return acc


def block_A_mod(s: int, n: int, stats: dict[str, int] | None = None) -> tuple[str, int]:
    fs = block_factorial_mod(s, n)
    d = gcd(fs, n)
    if d != 1:
        if stats is not None:
            stats["den_nonunit"] += 1
        return "factor", d
    inv = pow(fs, -1, n)
    value = block_factorial_mod(2 * s, n) * block_factorial_mod(3 * s, n) % n
    value = value * pow(inv, 5, n) % n
    return "residue", value


def direct_A_mod(s: int, n: int) -> int:
    return (comb(2 * s, s) ** 2 * comb(3 * s, s)) % n


def splitter(n: int, stats: dict[str, int]) -> tuple[int, str]:
    s = 1
    while True:
        kind, value = block_A_mod(s, n, stats)
        stats["evaluator_calls"] += 1
        g = value if kind == "factor" else gcd(value, n)
        if 1 < g < n:
            return g, "DYADIC"
        if g == n:
            t = isqrt(n) // 3
            for u, mode in ((t, "FALLBACK_T"), (t + 1, "FALLBACK_T1")):
                kind, value = block_A_mod(u, n, stats)
                stats["evaluator_calls"] += 1
                gg = value if kind == "factor" else gcd(value, n)
                if 1 < gg < n:
                    return gg, mode
            raise AssertionError(("fallback failure", n, s, t))
        s *= 2


def main() -> None:
    ps = [p for p in primes_upto(199) if p > 3]
    pairs = [(p, q) for i, p in enumerate(ps) for q in ps[i + 1 :]]

    factorial_checks = 0
    for p, q in pairs[:12]:
        n = p * q
        for k in range(121):
            assert block_factorial_mod(k, n) == direct_factorial_mod(k, n)
            factorial_checks += 1

    a_checks = 0
    for p, q in pairs[::11]:
        n = p * q
        samples = sorted(
            set((0, 1, max(0, p // 3 - 1), p // 3, (p + 2) // 3, min(p - 1, p // 2), p - 1))
        )
        for s in samples:
            if 0 <= s < p:
                kind, value = block_A_mod(s, n)
                assert kind == "residue"
                assert value == direct_A_mod(s, n)
                a_checks += 1

    wall_checks = 0
    for p in ps:
        for s in range(p):
            assert (direct_A_mod(s, p) == 0) == (3 * s > p)
            wall_checks += 1

    stats = {"den_nonunit": 0, "evaluator_calls": 0}
    modes: dict[str, int] = {}
    splitter_checks = 0
    for p, q in pairs:
        n = p * q
        factor, mode = splitter(n, stats)
        assert 1 < factor < n
        assert n % factor == 0
        assert factor in (p, q)
        modes[mode] = modes.get(mode, 0) + 1
        splitter_checks += 1

    assert stats["den_nonunit"] == 0
    print(
        "PASS "
        f"factorial_checks={factorial_checks} "
        f"A_checks={a_checks} "
        f"wall_checks={wall_checks} "
        f"splitter_checks={splitter_checks} "
        f"evaluator_calls={stats['evaluator_calls']} "
        f"denominator_nonunit_events={stats['den_nonunit']} "
        f"modes={modes}"
    )


if __name__ == "__main__":
    main()
