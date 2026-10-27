#!/usr/bin/env python3
"""Exact finite-field author certificate: Clausen Gauss-port high-tail bridge.

Original two labelled factorial/Gauss carriers; no native H0/B0 or Frobenius run.
No optional dependencies, floating point, random seeds, or external network.
"""
from math import isqrt


def primes_below(bound):
    return [p for p in range(7, bound) if p % 6 == 1 and
            all(p % d for d in range(2, isqrt(p) + 1))]


def gauss_units(p):
    """Return (valuation, unit mod p) of t_k for 0<=k<p.

    t_(k+1)/t_k = (6k+1)(3k+1) / [36(k+1)^2].
    """
    val = [0] * p
    unit = [1] * p
    for k in range(p - 1):
        num = (6 * k + 1) * (3 * k + 1)
        e = 0
        while num % p == 0:
            num //= p
            e += 1
        val[k + 1] = val[k] + e
        unit[k + 1] = (unit[k] * num *
                       pow(36 * (k + 1) ** 2, -1, p)) % p
    return val, unit


def factorial_units(p):
    """p-adic factorial unit and valuation up to 3(p-1), modulo p."""
    nmax = 3 * (p - 1)
    units = [1] * (nmax + 1)
    valuations = [0] * (nmax + 1)
    for n in range(1, nmax + 1):
        x = n
        extra = 0
        while x % p == 0:
            x //= p
            extra += 1
        units[n] = units[n - 1] * x % p
        valuations[n] = valuations[n - 1] + extra
    return units, valuations


def original_w_normalized(n, p, units, valuations):
    """Exact v_p(w_n), and w_n/p^v mod p from original factorials."""
    e = valuations[2 * n] + valuations[3 * n] - 5 * valuations[n]
    denom = units[n] ** 5 * pow(216, n, p)
    u = ((6 * n + 1) * units[2 * n] * units[3 * n] *
         pow(denom, -1, p)) % p
    return e, u


def reflected_r23_u(p, m, factmod):
    total = 0
    for j in range(2 * m, 3 * m):
        # Actual R23 reflected W/p^2 coefficient A_j; factorial denominators <p.
        num = (6 * j + 5) * pow(216, j, p) * pow(factmod[j], 5, p)
        den = factmod[2 * j + 1] * factmod[3 * j - 6 * m + 1]
        total = (total + num * pow(den, -1, p)) % p
    return total


def verify(p):
    m = (p - 1) // 6
    vals, t = gauss_units(p)
    assert all(vals[k] == (0 if k <= m else 1 if k <= 2 * m else 2)
               for k in range(p))
    fact, fval = factorial_units(p)
    g_mm = g_lh = g_lh_low = upper_count = internal_count = 0
    # Low+high pairs at n<=3m are the distinct half-side counterpart.
    for n in range(2 * m + 1, 3 * m + 1):
        lh = sum(t[j] * t[n - j] for j in range(m + 1)
                 if 2 * m < n - j < p) % p
        g_lh_low = (g_lh_low + 2 * (6 * n + 1) * lh) % p
    for n in range(3 * m + 1, p):
        # Ordered middle-middle and low-high Gauss-pair contributions.
        mm = sum(t[i] * t[n - i] for i in range(m + 1, 2 * m + 1)
                 if m < n - i <= 2 * m) % p
        lh = sum(t[j] * t[n - j] for j in range(m + 1)
                 if 2 * m < n - j < p) % p
        observed = (6 * n + 1) * (mm + 2 * lh) % p
        v, w_unit = original_w_normalized(n, p, fact, fval)
        if n <= 4 * m:
            assert v == 2 and observed == w_unit, (p, n, v)
            g_mm = (g_mm + (6 * n + 1) * mm) % p
            g_lh = (g_lh + 2 * (6 * n + 1) * lh) % p
            internal_count += 1
        else:
            # Strong coefficient gap; normalized low-high convolution = 0.
            assert v == 3 and mm == 0 and lh == 0 and observed == 0, (p, n)
            assert t[n] == (-sum(t[j] * t[n - j]
                                  for j in range(1, m + 1))) % p
            upper_count += 1
    r23_u = reflected_r23_u(p, m, fact)
    assert (g_mm + g_lh) % p == r23_u, (p, g_mm, g_lh, r23_u)
    # All-prime cutoff-sensitive high-low identity, in the other Gauss chart.
    aa = sum(t[:m + 1]) % p
    jj = sum(j * t[j] for j in range(m + 1)) % p
    cc = sum(t[2 * m + 1:]) % p
    c1 = sum(k * t[k] for k in range(2 * m + 1, p)) % p
    hh = sum(t[k] * t[j] * (6 * (k + j) + 1)
             for k in range(2 * m + 1, p)
             for j in range(m + 1) if k + j >= p) % p
    full_lh = (2 * (aa * cc + 6 * (jj * cc + aa * c1) - hh)) % p
    assert (g_lh_low + g_lh) % p == full_lh, (p, g_lh_low, g_lh, full_lh)
    if p % 24 in (13, 19):
        assert aa == 0, (p, aa)
        assert full_lh == (12 * jj * cc - 2 * hh) % p
    assert upper_count == 2 * m and internal_count == m
    return (g_mm, g_lh, r23_u, internal_count, upper_count,
            g_lh_low, aa, jj, cc, hh, full_lh)


def main():
    ps = primes_below(1000)
    assert len(ps) == 80, len(ps)
    special = {7, 13, 19, 139, 181, 199, 277, 373}
    rows = {}
    internal_total = upper_total = 0
    for p in ps:
        row = verify(p)
        internal_total += row[3]
        upper_total += row[4]
        if p in special:
            rows[p] = row
    assert special == set(rows)
    print(f"PASS primes={len(ps)} paired-internal-ranks={internal_total} "
          f"high-degree-gap-ranks={upper_total}")
    for p in sorted(rows):
        g_mm, g_lh, u, inside, gap, g_low, aa, jj, cc, hh, full_lh = rows[p]
        print(f"p={p}: G_MM={g_mm} G_LH={g_lh} R23_U={u} "
              f"HL_low={g_low} HL_full={full_lh} "
              f"A={aa} J={jj} C={cc} H={hh} "
              f"internal={inside} gap={gap}")


if __name__ == "__main__":
    main()
