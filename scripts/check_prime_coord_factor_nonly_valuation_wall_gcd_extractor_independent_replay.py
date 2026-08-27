#!/usr/bin/env python3
"""Independent exact checker for the PCF4R N-only valuation-wall extractor.

Constructor-side code receives only N and public integer indices.
Hidden primes are used only by bounded regression oracles.
"""

from math import comb, gcd, isqrt


def a_direct(n: int) -> int:
    return comb(2 * n, n) ** 2 * comb(3 * n, n)


def a_next(n: int, a_n: int) -> int:
    """Exact recurrence A_n -> A_{n+1}; never uses modular division."""
    num = 6 * (2 * n + 1) * (3 * n + 1) * (3 * n + 2) * a_n
    den = (n + 1) ** 3
    assert num % den == 0
    return num // den


def split_nonly(N: int):
    """Split a promised distinct odd semiprime N=pq with 3<p<q.

    The function receives N only. It uses exact integer recurrence, public
    dyadic indices, gcd, isqrt, and the two public fallback indices.
    """
    if N <= 1 or gcd(N, 6) != 1:
        raise ValueError("domain requires N coprime to 6")

    M = isqrt(N)
    t = M // 3
    fallback_targets = (t, t + 1)
    fallback = {}

    A = 1
    dyadic = 1
    synchronized = False
    dyadic_trace = []

    for n in range(1, M + 1):
        A = a_next(n - 1, A)

        if n == t or n == t + 1:
            fallback[n] = gcd(A, N)

        if synchronized:
            if t in fallback and t + 1 in fallback:
                for u in fallback_targets:
                    g = fallback[u]
                    if 1 < g < N:
                        return g, {
                            "mode": "fallback",
                            "seed": u,
                            "last_n": n,
                            "M": M,
                            "t": t,
                            "dyadic_trace": tuple(dyadic_trace),
                            "fallback": dict(fallback),
                        }
                raise AssertionError(("two-seed fallback failed", N, fallback))
            continue

        if n == dyadic:
            g = gcd(A, N)
            dyadic_trace.append((n, g))
            if g == 1:
                dyadic *= 2
            elif g < N:
                return g, {
                    "mode": "dyadic",
                    "seed": n,
                    "last_n": n,
                    "M": M,
                    "t": t,
                    "dyadic_trace": tuple(dyadic_trace),
                    "fallback": dict(fallback),
                }
            else:
                synchronized = True
                if t in fallback and t + 1 in fallback:
                    for u in fallback_targets:
                        h = fallback[u]
                        if 1 < h < N:
                            return h, {
                                "mode": "fallback",
                                "seed": u,
                                "last_n": n,
                                "M": M,
                                "t": t,
                                "dyadic_trace": tuple(dyadic_trace),
                                "fallback": dict(fallback),
                            }
                    raise AssertionError(("two-seed fallback failed", N, fallback))

    raise AssertionError(("public stopping cap exhausted", N, M))


def vp_fact(n: int, p: int) -> int:
    out = 0
    while n:
        n //= p
        out += n
    return out


def vp_a(n: int, p: int) -> int:
    return vp_fact(2 * n, p) + vp_fact(3 * n, p) - 5 * vp_fact(n, p)


def primes_below(limit: int):
    """Test-oracle sieve only; split_nonly never calls this."""
    flag = [True] * limit
    if limit:
        flag[0] = False
    if limit > 1:
        flag[1] = False
    for d in range(2, isqrt(limit - 1) + 1):
        if flag[d]:
            for k in range(d * d, limit, d):
                flag[k] = False
    return [n for n, ok in enumerate(flag) if ok]


def first_dyadic_wall(p: int) -> int:
    """Proof-side oracle helper; not used by split_nonly."""
    s = 1
    while 3 * s < p:
        s *= 2
    return s


def main() -> None:
    A = 1
    recurrence_checks = 0
    for n in range(0, 301):
        assert A == a_direct(n)
        recurrence_checks += 1
        A = a_next(n, A)

    primes = [p for p in primes_below(1000) if p > 3]
    valuation_checks = 0
    for r in primes:
        for s in range(r):
            got = vp_a(s, r)
            want = (2 * s) // r + (3 * s) // r
            assert got == want, (r, s, got, want)
            assert (got > 0) == (3 * s >= r)
            valuation_checks += 1

    semiprimes = 0
    dyadic_returns = 0
    fallback_returns = 0
    synchronization_checks = 0
    max_last_n = 0

    for i, p in enumerate(primes):
        for q in primes[i + 1 :]:
            N = p * q

            s = first_dyadic_wall(p)
            assert s < p < q
            assert 3 * s >= p
            assert 3 * (s // 2) < p
            g_wall = gcd(a_direct(s), N)
            want_wall = N if 3 * s >= q else p
            assert g_wall == want_wall
            if g_wall == N:
                assert q < 2 * p
                synchronization_checks += 1

            factor, info = split_nonly(N)
            assert factor in (p, q)
            assert 1 < factor < N
            assert N % factor == 0
            assert info["last_n"] <= isqrt(N)

            semiprimes += 1
            max_last_n = max(max_last_n, info["last_n"])
            if info["mode"] == "dyadic":
                dyadic_returns += 1
            elif info["mode"] == "fallback":
                fallback_returns += 1
                assert info["dyadic_trace"][-1][1] == N
                assert q < 2 * p
            else:
                raise AssertionError(info)

    assert semiprimes > 0
    assert dyadic_returns + fallback_returns == semiprimes
    assert fallback_returns == synchronization_checks

    print("PCF4R independent checker: PASS")
    print(f"recurrence_crosschecks={recurrence_checks}")
    print(f"valuation_checks={valuation_checks}")
    print(f"semiprime_regressions={semiprimes}")
    print(f"dyadic_returns={dyadic_returns}")
    print(f"fallback_returns={fallback_returns}")
    print(f"synchronization_checks={synchronization_checks}")
    print(f"max_last_n={max_last_n}")
    print("constructor_hidden_factor_inputs=0")


if __name__ == "__main__":
    main()
