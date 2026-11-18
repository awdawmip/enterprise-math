"""Two independent evaluations of the fixed-cutoff corrected carry window."""
import argparse
from fractions import Fraction
from hashlib import sha1
from importlib.util import module_from_spec, spec_from_file_location
import json
from math import fsum, lgamma, log, sqrt
from pathlib import Path
import sys
from types import ModuleType

GAMMA = 2 * log(2) - 1


def carry(n, m):
    return (2 * n) // m - 2 * (n // m)


def period(p):
    return Fraction(p // 2, p)


def prime_data(limit):
    spf = list(range(limit + 1))
    for p in range(2, int(sqrt(limit)) + 1):
        if spf[p] == p:
            for j in range(p * p, limit + 1, p):
                if spf[j] == j:
                    spf[j] = p
    primes = [p for p in range(2, limit + 1) if spf[p] == p]
    powers = [(q, p) for p in primes for q in prime_powers(p, limit)]
    return spf, primes, sorted(powers)


def prime_powers(p, limit):
    q = p
    while q <= limit:
        yield q
        q *= p


def vp_factorial(m, p):
    count = 0
    while m:
        m //= p
        count += m
    return count


def cutoff(n):
    # Exact floor(n^(3/5)) without floating point threshold decisions.
    y = 1
    while (y + 1) ** 5 <= n ** 3:
        y += 1
    return y


def frozen_modules(src):
    package = ModuleType('frozen_carry')
    package.__path__ = [str(Path(src).resolve())]
    sys.modules[package.__name__] = package
    result = []
    expected = {'brc_count_centered_carry': '42cd3b4ab4d34e96194164207a961dc6979d521e',
                'brc_large_prime_hard_core': '023dd13c0934b2bf49c1b4ab90d2b0fb992d3488'}
    for name, blob in expected.items():
        path = Path(src) / (name + '.py')
        content = path.read_bytes()
        assert sha1(b'blob ' + str(len(content)).encode() + bytes(1) + content).hexdigest() == blob
        fullname = package.__name__ + '.' + name
        spec = spec_from_file_location(fullname, path)
        mod = module_from_spec(spec)
        sys.modules[fullname] = mod
        spec.loader.exec_module(mod)
        result.append(mod)
    return result


def exact_tests(frozen):
    _, primes, _ = prime_data(512)
    checks = pairs = 0
    for p in primes:
        assert sum(carry(n, p) for n in range(p)) == p * period(p)
        assert carry(p, p) == 0
    for n in range(3, 193):
        count = sum(carry(n, m) for m in range(1, n + 1))
        alpha = Fraction(count, n)
        y = max(2, cutoff(n))
        if frozen:
            assert count == frozen[0].carry_count(n)
            assert frozen[1].large_prime_increment_certificate(n, y).verify()
        for p in primes:
            if p > n:
                break
            qs = list(prime_powers(p, n))
            q = len(qs)
            c = carry(n, p)
            tot = sum(carry(n, power) for power in qs)
            a = period(p)
            # Independent binomial/lcm valuation against original carry count.
            vp = vp_factorial(2 * n, p) - 2 * vp_factorial(n, p)
            assert tot == vp - len(list(prime_powers(p, 2 * n))) + q
            # Constant and gamma coefficients of each log(p) checked separately.
            H0, H1 = (c, -1) if p > y else (0, 0)
            B0, B1 = (a, -1) if p <= y else (0, 0)
            L0 = c - a if p <= y else 0
            P0, P1 = tot - c, -(q - 1)
            D0, D1 = -alpha * q, q
            assert H0 + B0 + L0 + P0 + D0 == tot - alpha * q
            assert H1 + B1 + P1 + D1 == 0
            pairs += 1
        checks += 1
    return {'periods_and_prime_endpoints': len(primes), 'sites': checks, 'formal_prime_log_coefficients': pairs,
            'frozen_certificates': checks if frozen else 0}


def block(N):
    y = cutoff(N)
    spf, primes, powers = prime_data(4 * N)
    low = [p for p in primes if p <= y]
    B = fsum((float(period(p)) - GAMMA) * log(p) for p in low)
    lam = [0.0] * (4 * N + 1)
    for q, p in powers:
        lam[q] = log(p)
    psi = [0.0]
    for x in lam[1:]:
        psi.append(psi[-1] + x)
    lp = {p: log(p) for p in primes}

    def radical(m):
        value = 0.0
        while m > 1:
            p = spf[m]
            if p > y:
                value += lp[p]
            while m % p == 0:
                m //= p
        return value

    def prime_endpoint(m):
        return lp[m] if m > y and spf[m] == m else 0.0

    norms = {k: [] for k in ('J', 'H', 'corrected', 'J_minus_H', 'J_minus_corrected', 'B')}
    # Independent H initialization by V17's half-residue criterion.
    increment_H = fsum((int(N % p >= (p + 1) // 2) - GAMMA) * lp[p]
                       for p in primes if y < p <= N)
    max_error = 0.0
    for n in range(N, 2 * N):
        count = sum(carry(n, m) for m in range(1, n + 1))
        alpha = count / n
        J = fsum((carry(n, q) - alpha) * lp[p] for q, p in powers if q <= n)
        J_bin = lgamma(2 * n + 1) - 2 * lgamma(n + 1) - psi[2 * n] + (1 - alpha) * psi[n]
        H = fsum((carry(n, p) - GAMMA) * lp[p] for p in primes if y < p <= n)
        small = fsum((carry(n, p) - float(period(p))) * lp[p] for p in low)
        higher = fsum((carry(n, q) - GAMMA) * lp[p] for q, p in powers if p < q <= n)
        identity = H + B + small + higher + (GAMMA - alpha) * psi[n]
        max_error = max(max_error, abs(J - J_bin), abs(H - increment_H), abs(J - identity))
        values = {'J': J, 'H': H, 'corrected': H + B, 'J_minus_H': J - H,
                  'J_minus_corrected': J - H - B, 'B': B}
        for k, v in values.items():
            norms[k].append((v / n) ** 2)
        increment_H += (radical(2 * n + 1) - prime_endpoint(2 * n + 1) - radical(n + 1)
                        + (1 - GAMMA) * prime_endpoint(n + 1))
    assert max_error < 1e-7
    return {'N': N, 'y': y, 'B_y': round(B, 9), 'energies': {k: round(fsum(v), 9) for k, v in norms.items()},
            'max_two_route_and_identity_error': max_error}


def volterra():
    count = 0
    for N in range(12, 90):
        start = (4 * N + 2) // 3
        for n in range(start, 2 * N):
            for m in range(start, n + 1):
                assert carry(n, m) == 0
                count += 1
    return count


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--v17-src', help='directory containing the two pinned public source modules')
    opt = parser.parse_args()
    f = frozen_modules(opt.v17_src) if opt.v17_src else None
    print(json.dumps({'exact': exact_tests(f), 'blocks_theta_3_over_5': [block(n) for n in (32,128,512,2048)],
                      'outer_triangle_zero_entries': volterra()}, indent=2))
