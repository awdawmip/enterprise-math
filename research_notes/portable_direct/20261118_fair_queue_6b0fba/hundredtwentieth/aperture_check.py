"""Reproduce the finite prime-frequency and aperture checks, with the Python standard library."""

import json
import math
from fractions import Fraction


def primes_to(limit):
    sieve = bytearray(b"\1") * (limit + 1)
    sieve[:2] = b"\0\0"
    for prime in range(2, math.isqrt(limit) + 1):
        if sieve[prime]:
            start = prime * prime
            sieve[start::prime] = bytes((limit - start) // prime + 1)
    return [p for p, kept in enumerate(sieve) if kept]


def triangle(r, y):
    return Fraction(y - 4 * min(r, y-r), 8*y)


def smooth_integral(n, y, harmonic):
    """Full cells sum to 2 log 2 + 2 H_R - 2 H_{2R} - 1/(2R)."""
    a = n / y
    end = (n + y - 1) // y
    tail = 2 * (math.log(2) + harmonic[end] - harmonic[2*end]) - 1 / (2*end)
    if end * y == n:
        partial = 0.0
    elif a < end - 0.5:
        mid = end - 0.5
        partial = 0.5 * (2 / mid - 1 / a - 1 / end)
    else:
        partial = 0.5 * (1 / a - 1 / end)
    return n * (partial + tail)


def prime_window(n0, y):
    primes = primes_to(y)
    increments = [0.0] * n0
    initial = []
    probes = {n0, n0+1, n0+2, 2*n0-1, n0+n0//4, n0+n0//2}
    exact_positions = 0
    for p in primes:
        weight = math.log(p)
        up = (p + 1) // 2
        initial.append(weight * (int(n0 % p >= up) - (p // 2)/p))
        for n in probes:
            entry = 2*n//p - 2*(n//p)
            assert entry == int(n%p >= up)
            exact_positions += 1
        for residue, jump in ((0, -weight), (up, weight)):
            first = n0 + 1 + (residue - n0 - 1) % p
            for n in range(first, 2*n0, p):
                increments[n - n0] += jump
    current = math.fsum(initial)
    data = []
    for offset, increment in enumerate(increments):
        current += increment
        n = n0 + offset
        if n in probes:
            independent = math.fsum(math.log(p) * (2*n//p - 2*(n//p) - (p//2)/p)
                                    for p in primes)
            assert abs(current - independent) < 3e-9
        data.append(current)
    return data, exact_positions


def finite_block(n0):
    y = math.isqrt(math.isqrt(n0**3))
    values, positions = prime_window(n0, y)
    harmonic = [0.0]
    for j in range(1, 2 * ((2*n0 + y - 1)//y) + 1):
        harmonic.append(harmonic[-1] + 1/j)
    smooth_sq = prime_sq = difference_sq = triangle_sq = smooth_triangle_sq = 0.0
    for offset, residual in enumerate(values):
        n = n0 + offset
        smooth = smooth_integral(n, y, harmonic)
        predicted = -float(triangle(n % y, y)) * y**2 / n
        assert abs(smooth-predicted) < y**3 / n**2
        prime_sq += (residual/n)**2
        smooth_sq += (smooth/n)**2
        difference_sq += ((residual-smooth)/n)**2
        triangle_sq += (predicted/n)**2
        smooth_triangle_sq += ((smooth-predicted)/n)**2
    return dict(N=n0, y=y, exact_carry_probes=positions,
                prime_energy=round(prime_sq, 12), smooth_energy=round(smooth_sq, 12),
                prime_minus_smooth_energy=round(difference_sq, 12),
                triangle_energy=round(triangle_sq, 12),
                smooth_minus_triangle_energy=round(smooth_triangle_sq, 12))


def main():
    for y in range(1, 257):
        values = [triangle(r, y) for r in range(y)]
        assert sum(values)/y == Fraction(y%2, 8*y*y)
        second = Fraction(1, 192) + Fraction(1 if y%2 else 4, 96*y*y)
        assert sum(v*v for v in values)/y == second
    integral_triangle_sq = 2 * (Fraction(1, 128) - Fraction(1, 64) + Fraction(1, 96))
    assert integral_triangle_sq == Fraction(1, 192)
    x_weight = Fraction(1, 3) * (1-Fraction(1, 8))
    certificate = dict(
        discrete_triangle_grids=256,
        continuous_triangle_second_moment=str(integral_triangle_sq),
        dyadic_integral_x_to_minus_four=str(x_weight),
        critical_energy_coefficient=str(integral_triangle_sq * x_weight),
        finite_prime_and_continuous=[finite_block(2**k) for k in (8, 10, 12, 14, 16)],
    )
    print(json.dumps(certificate, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
