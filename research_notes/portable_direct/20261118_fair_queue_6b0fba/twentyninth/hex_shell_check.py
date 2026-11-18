"""Primitive hexagon shell counts and Euler factors. Python 3, standard library."""
from array import array
from fractions import Fraction
from math import gcd
import json


def arithmetic(limit):
    """Linear sieve for g=mu*chi_{-3}, tracking the local factor at p exactly."""
    least = array("I", [0]) * (limit + 1)
    phi = array("I", [0]) * (limit + 1)
    g = array("i", [0]) * (limit + 1)
    mu = array("b", [0]) * (limit + 1)
    primes = []
    g[1] = phi[1] = mu[1] = 1
    for n in range(2, limit + 1):
        if least[n] == 0:
            least[n] = n
            primes.append(n)
        p = least[n]
        m = n // p
        if m % p:
            phi[n] = phi[m] * (p - 1)
            mu[n] = -mu[m]
            g[n] = g[m] * (-1 if p == 3 else -2 if p % 3 == 2 else 0)
        else:
            phi[n] = phi[m] * p
            g[n] = -g[m] if p % 3 == 2 else 0
        for q in primes:
            if q > p or q * n > limit:
                break
            least[q * n] = q
    return phi, g, mu, primes


def geometry(phi, g, limit):
    shells = [0] * (limit + 1)
    for q in range(-limit, limit + 1):
        for r in range(-limit, limit + 1):
            h = max(abs(2 * q + r), abs(q + 2 * r), abs(q - r))
            if 1 <= h <= limit and gcd(q, r) == 1:
                shells[h] += 1
    assert all(shells[n] == 2 * (phi[n] - g[n]) for n in range(1, limit + 1))
    return shells[1:13]


def divisor_audit(mu, g, limit):
    via_convolution = [0] * (limit + 1)
    for d in range(1, limit + 1):
        if mu[d]:
            for k in range(1, limit // d + 1):
                via_convolution[d * k] += mu[d] * (0, 1, -1)[k % 3]
    assert list(g[1:limit + 1]) == via_convolution[1:]


def check_euler_factors():
    for p in (2, 3, 7, 11, 13):
        x = Fraction(1, p ** 2)
        chi = (0, 1, -1)[p % 3]
        if p == 3:
            a, b, magnitude = 1 + x, 1 - x, 1 + x
        elif chi == 1:
            a = b = magnitude = 1
        else:
            a, b, magnitude = 1 / (1 - x), 1 / (1 + x), (1 + x) / (1 - x)
        zeta_over_L = (1 - chi * x) / (1 - x)
        tail = 1 / (1 - x * x) if chi == -1 else 1
        assert a * a == zeta_over_L * tail * ((1 + x)**2 * (1 - x) if p == 3 else 1)
        assert b * b == tail / zeta_over_L * ((1 - x) if p == 3 else 1)
        assert magnitude == zeta_over_L * (1 - x * x if p == 3 else 1)


def main():
    limit = 2_000_000
    phi, g, mu, primes = arithmetic(limit)
    first = geometry(phi, g, 256)
    divisor_audit(mu, g, 32_768)
    check_euler_factors()
    excess = deficit = absolute_sum = signed_sum = 0
    rows = []
    for n in range(1, limit + 1):
        excess += g[n] < 0
        deficit += g[n] > 0
        absolute_sum += 2 * abs(g[n])
        signed_sum -= 2 * g[n]
        if n in (100, 1000, 10_000, 100_000, 1_000_000, limit):
            rows.append({"X": n, "v_above_2phi": excess, "v_below_2phi": deficit,
                         "v_equal_2phi": n - excess - deficit,
                         "sum_abs_discrepancy": absolute_sum, "sum_discrepancy": signed_sum})
    fermat = [2 ** (2 ** j) + 1 for j in range(6)]
    assert fermat[-1] == 641 * 6_700_417
    small_factors = fermat[:-1] + [641, 6_700_417, 31, 43]
    assert all(all(n % p for p in primes if p * p <= n) for n in small_factors)
    assert all((pow(4, t, divisor) - 1) % divisor == 0
               for t, divisor in [(3, 9), (5, 31), (7, 43), (32, 6_700_417)])
    dyadic_discrepancies = []
    for j in range(6):
        factors = fermat[:j + 1] if j < 5 else fermat[:5] + [641, 6_700_417]
        val = 1
        for p in factors:
            val *= (0, 1, -1)[p % 3] - 1
        assert -2 * val == ((-1) ** j * 2 ** (j + 1) if j < 5 else 0)
        dyadic_discrepancies.append(-2 * val)
    period = 3 * 5 * 7 * 32
    covered = sum(any(t % d == 0 for d in (3, 5, 7, 32)) for t in range(1, period + 1))
    assert Fraction(covered, period) == Fraction(39, 70)
    # For the Euler constant, use a rational bound exp(t)<=1/(1-t) for 0<=t<1.
    cutoff = 100_000
    partial = Fraction(1)
    for p in primes:
        if p > cutoff:
            break
        if p % 3 == 2:
            partial *= Fraction(p * p, p * p - 1)
    log_tail = (Fraction(1, cutoff) + Fraction(1, cutoff + 1)) / 2
    lower, upper = partial, partial / (1 - log_tail)
    scale = 10 ** 8
    # Outward-rounded exact rational interval.
    enclosure = [lower.numerator * scale // lower.denominator,
                 -((-upper.numerator * scale) // upper.denominator)]
    print(json.dumps({"shell_geometry_through": 256, "v_1_to_12": first,
                      "dirichlet_convolution_checked_through": 32_768,
                      "prime_product_cutoff": cutoff, "P2_interval_in_units_1e-8": enclosure,
                      "frozen_dyadic_discrepancies_j_0_to_5": dyadic_discrepancies,
                      "forced_equal_exponent_density": str(Fraction(covered, period)),
                      "counts": rows}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
