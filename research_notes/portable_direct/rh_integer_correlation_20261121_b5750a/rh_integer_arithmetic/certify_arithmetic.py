#!/usr/bin/env python3
"""Exact rational interval tests of new divisor / sparse-endpoint identities.

All enclosures use fixed-denominator integer endpoints. No binary floating
point or unproved asymptotic remainder enters the certificates.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import comb, factorial
from pathlib import Path
import json
import time

DIGITS = 60
SCALE = 10 ** DIGITS
ZERO = (0, 0)
ONE = (SCALE, SCALE)
H = F(1, 16)
RATES = (H, 2 * H, 1 + H, 1 + 2 * H, F(1))
ANCHOR = 256
EM_ORDER = 16
LOG_TERMS = 80


def ceildiv(n, d):
    return -((-n) // d)


def interval_fraction(x):
    x = F(x)
    return x.numerator * SCALE // x.denominator, ceildiv(x.numerator * SCALE, x.denominator)


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def neg(x):
    return -x[1], -x[0]


def sub(x, y):
    return add(x, neg(y))


def scale(x, coefficient):
    coefficient = F(coefficient)
    a, b = (x if coefficient >= 0 else (x[1], x[0]))
    numerator, denominator = coefficient.numerator, coefficient.denominator
    return (a * numerator // denominator,
            ceildiv(b * numerator, denominator))


def mul(x, y):
    products = [a * b for a in x for b in y]
    return min(products) // SCALE, ceildiv(max(products), SCALE)


def absolute(x):
    if x[0] >= 0:
        return x
    if x[1] <= 0:
        return neg(x)
    return 0, max(-x[0], x[1])


def overlaps(x, y):
    return max(x[0], y[0]) <= min(x[1], y[1])


def floor_root(n, k):
    if n < 2:
        return n
    x = 1 << ((n.bit_length() + k - 1) // k)
    while True:
        nxt = ((k - 1) * x + n // (x ** (k - 1))) // k
        if nxt >= x:
            break
        x = nxt
    while (x + 1) ** k <= n:
        x += 1
    while x ** k > n:
        x -= 1
    assert x ** k <= n < (x + 1) ** k
    return x


def sieve(limit):
    # Euler's linear sieve: each composite is generated once at its least prime.
    spf = [0] * (limit + 1)
    mu = [0] * (limit + 1)
    omega = [0] * (limit + 1)
    primes = []
    mu[1] = 1
    for n in range(2, limit + 1):
        if spf[n] == 0:
            spf[n] = n
            primes.append(n)
            mu[n] = -1
            omega[n] = 1
        for p in primes:
            composite = n * p
            if composite > limit:
                break
            spf[composite] = p
            if n % p == 0:
                mu[composite] = 0
                omega[composite] = omega[n]
                break
            mu[composite] = -mu[n]
            omega[composite] = omega[n] + 1
    return spf, mu, omega


def bernoulli_numbers(limit):
    numbers = [F(1)]
    for n in range(1, limit + 1):
        numbers.append(-sum(F(comb(n + 1, k)) * numbers[k]
                            for k in range(n)) / (n + 1))
    assert numbers[1] == F(-1, 2) and numbers[2] == F(1, 6)
    return numbers


BERNOULLI = bernoulli_numbers(2 * EM_ORDER)
BERNOULLI_POLY_BOUND = sum(F(comb(2 * EM_ORDER, j)) * abs(BERNOULLI[j])
                          for j in range(2 * EM_ORDER + 1))


class Oracle:
    def __init__(self, base_limit):
        self.base_limit = max(base_limit, ANCHOR)
        self.spf, self.mu, self.omega = sieve(self.base_limit)
        self.root_cache = {1: ONE}
        self.root_calls = 0
        self.x = [ZERO] * (self.base_limit + 1)
        self.x[1] = ONE
        for n in range(2, self.base_limit + 1):
            p = self.spf[n]
            self.x[n] = mul(self.x[n // p], self.root_power(p))
        self.power_prefix = [[ZERO] * (ANCHOR + 1) for _ in RATES]
        self.mobius_prefix = [[ZERO] * (self.base_limit + 1) for _ in RATES[:4]]
        for n in range(1, self.base_limit + 1):
            powers = self.powers_at(n)
            if n <= ANCHOR:
                for j in range(len(RATES)):
                    self.power_prefix[j][n] = add(self.power_prefix[j][n - 1], powers[j])
            for j in range(4):
                self.mobius_prefix[j][n] = add(self.mobius_prefix[j][n - 1],
                                                scale(powers[j], self.mu[n]))
        self.log_cache = {1: ZERO}
        self.sum_cache = {}
        self.coefficients = []
        self.remainder_radii = []
        for j, a in enumerate(RATES):
            rising = F(1)
            coefficients = []
            for k in range(1, 2 * EM_ORDER + 1):
                rising *= a + k - 1
                if k % 2:
                    coefficients.append(BERNOULLI[k + 1] * rising / factorial(k + 1))
            self.coefficients.append(coefficients)
            multiplier = (BERNOULLI_POLY_BOUND * rising
                          / factorial(2 * EM_ORDER) / (a + 2 * EM_ORDER - 1)
                          / ANCHOR ** (2 * EM_ORDER - 1))
            upper = self.powers_at(ANCHOR)[j][1]
            self.remainder_radii.append(ceildiv(upper * multiplier.numerator,
                                               multiplier.denominator))

    def root_power(self, n):
        if n not in self.root_cache:
            q = floor_root(n * SCALE ** H.denominator, H.denominator)
            self.root_cache[n] = (SCALE * SCALE // (q + 1),
                                  ceildiv(SCALE * SCALE, q))
            self.root_calls += 1
        return self.root_cache[n]

    def powers_at(self, n):
        x = self.x[n] if n <= self.base_limit and self.x[n] != ZERO else self.root_power(n)
        xx = mul(x, x)
        return x, xx, scale(x, F(1, n)), scale(xx, F(1, n)), interval_fraction(F(1, n))

    def log_integer(self, n):
        if n in self.log_cache:
            return self.log_cache[n]

        def log_unit(z):
            z_interval = interval_fraction(z)
            square = mul(z_interval, z_interval)
            term = z_interval
            result = ZERO
            for k in range(LOG_TERMS):
                result = add(result, scale(term, F(2, 2 * k + 1)))
                term = mul(term, square)
            tail = F(2, 1) * F(1, 3) ** (2 * LOG_TERMS + 1)
            tail /= F(2 * LOG_TERMS + 1) * (1 - F(1, 9))
            return result[0], result[1] + ceildiv(tail.numerator * SCALE, tail.denominator)

        if 2 not in self.log_cache:
            self.log_cache[2] = log_unit(F(1, 3))
        exponent = n.bit_length() - 1
        unit = log_unit(F(n - 2 ** exponent, n + 2 ** exponent))
        result = add(scale(self.log_cache[2], exponent), unit)
        self.log_cache[n] = result
        return result

    def power_sum(self, j, n):
        if n <= ANCHOR:
            return self.power_prefix[j][n]
        key = (j, n)
        if key in self.sum_cache:
            return self.sum_cache[key]
        a = RATES[j]
        end = self.powers_at(n)[j]
        start = self.powers_at(ANCHOR)[j]
        if a == 1:
            integral = sub(self.log_integer(n), self.log_integer(ANCHOR))
        else:
            integral = scale(sub(scale(end, n), scale(start, ANCHOR)), 1 / (1 - a))
        result = add(self.power_prefix[j][ANCHOR], integral)
        result = add(result, scale(sub(end, start), F(1, 2)))
        for r, coefficient in enumerate(self.coefficients[j], 1):
            power = 2 * r - 1
            difference = sub(scale(start, F(1, ANCHOR ** power)),
                             scale(end, F(1, n ** power)))
            result = add(result, scale(difference, coefficient))
        radius = self.remainder_radii[j]
        result = result[0] - radius, result[1] + radius
        self.sum_cache[key] = result
        return result


def quotient_blocks(n, first=1):
    left = first
    while left <= n:
        quotient = n // left
        right = n // quotient
        yield left, right, quotient
        left = right + 1


class MobiusEndpoint:
    def __init__(self, n):
        cutoff = floor_root(n * n, 3)
        if cutoff ** 3 < n * n:
            cutoff += 1
        self.oracle = Oracle(cutoff)
        self.base = self.oracle.base_limit
        self.cache = {}
        self.block_count = 0

    def M(self, n):
        if n <= self.base:
            return tuple(row[n] for row in self.oracle.mobius_prefix)
        if n not in self.cache:
            result = [ONE] * 4
            for left, right, quotient in quotient_blocks(n, 2):
                inner = self.M(quotient)
                for j in range(4):
                    weight = sub(self.oracle.power_sum(j, right),
                                 self.oracle.power_sum(j, left - 1))
                    result[j] = sub(result[j], mul(weight, inner[j]))
                self.block_count += 1
            self.cache[n] = tuple(result)
        return self.cache[n]

    def evaluate(self, n):
        self.M(n)
        sums = [ZERO, ZERO]
        weighted = [ZERO, ZERO]
        endpoint_blocks = 0
        for left, right, quotient in quotient_blocks(n):
            hi, lo = self.M(right), self.M(left - 1)
            harmonic = self.oracle.power_sum(4, quotient)
            for j in range(2):
                sums[j] = add(sums[j], scale(sub(hi[j], lo[j]), quotient))
                weighted[j] = add(weighted[j], mul(harmonic, sub(hi[j + 2], lo[j + 2])))
            endpoint_blocks += 1
        road_smoothing = ZERO
        for j, coefficient in enumerate((2 / H, -1 / (2 * H))):
            corrected = sub(sub(scale(weighted[j], n), sums[j]), interval_fraction(n - 1))
            road_smoothing = add(road_smoothing, scale(corrected, coefficient))
        T = sub(road_smoothing, scale(self.oracle.log_integer(n), n))
        kappa1 = scale(self.oracle.log_integer(2), 2)
        green = add(T, scale(kappa1, n - 1))
        return T, green, {
            'sieve_cutoff': self.base,
            'mobius_states_above_cutoff': len(self.cache),
            'recursion_quotient_blocks': self.block_count,
            'endpoint_quotient_blocks': endpoint_blocks,
            'large_power_sum_queries': len(self.oracle.sum_cache),
            'algebraic_root_calls': self.oracle.root_calls,
            'enumerates_all_integers_through_endpoint': False,
            'M_n': [render(x) for x in self.M(n)],
            'EM_uniform_remainder_radii': [render((0, r)) for r in self.oracle.remainder_radii]
        }


def decimal(integer, places):
    unit = 10 ** (DIGITS - places)
    sign = '-' if integer < 0 else ''
    integer = abs(integer)
    return f'{sign}{integer // 10 ** DIGITS}.{integer % 10 ** DIGITS // unit:0{places}d}'


def render(x, places=26):
    unit = 10 ** (DIGITS - places)
    lo = x[0] // unit * unit
    hi = ceildiv(x[1], unit) * unit
    return {'lower': decimal(lo, places), 'upper': decimal(hi, places),
            'width_upper': str(F(x[1] - x[0], SCALE))}


def direct_check(n):
    oracle = Oracle(n)
    road = [[ONE] * (n + 1) for _ in range(2)]
    D = [ZERO] * (n + 1)
    kappa = [ZERO] * (n + 1)
    logs = [ZERO] + [oracle.log_integer(k) for k in range(1, n + 2)]
    for k in range(1, n + 1):
        second = sub(add(scale(logs[k + 1], k + 1),
                         scale(logs[k - 1], k - 1)), scale(logs[k], 2 * k))
        kappa[k] = scale(second, k)
        if k == 1:
            continue
        p = oracle.spf[k]
        quotient = k // p
        xp = oracle.x[p]
        for j, p_power in enumerate((xp, mul(xp, xp))):
            road[j][k] = (road[j][quotient] if quotient % p == 0
                          else mul(road[j][quotient], sub(ONE, p_power)))
        D[k] = scale(sub(scale(road[0][k], 4), road[1][k]), 1 / (2 * H))
    smooth = ZERO
    green = ZERO
    green_absolute = ZERO
    for k in range(2, n + 1):
        ramp = F(n, k) - 1
        smooth = add(smooth, scale(D[k], ramp))
        residual = sub(D[k], kappa[k])
        green = add(green, scale(residual, ramp))
        green_absolute = add(green_absolute, scale(absolute(residual), ramp))
    T = sub(smooth, scale(logs[n], n))
    b = [ZERO] * (n + 1)
    for d in range(1, n + 1):
        if oracle.mu[d]:
            for k in range(1, n // d + 1):
                b[d * k] = add(b[d * k], scale(kappa[k], oracle.mu[d]))
    harmonic = [ZERO] * (n + 1)
    for k in range(1, n + 1):
        harmonic[k] = add(harmonic[k - 1], interval_fraction(F(1, k)))
    atom_sum = ZERO
    atom_absolute = ZERO
    strict_signs = 0
    for d in range(1, n + 1):
        x = oracle.x[d]
        psi = scale(add(sub(interval_fraction(3), scale(x, 4)), mul(x, x)), 1 / (2 * H))
        c = sub(scale(psi, -oracle.mu[d]), b[d])
        if d >= 2:
            expected = (-1) ** (oracle.omega[d] + 1)
            assert c[0] > 0 if expected > 0 else c[1] < 0
            assert b[d][0] > 0 if expected < 0 else b[d][1] < 0
            strict_signs += 1
        q = n // d
        W = sub(scale(harmonic[q], F(n, d)), interval_fraction(q))
        atom_sum = add(atom_sum, mul(c, W))
        atom_absolute = add(atom_absolute, mul(absolute(c), W))
    assert overlaps(T, atom_sum)
    assert overlaps(green, add(T, scale(kappa[1], n - 1)))
    return T, green, {
        'all_integer_inputs': n - 1,
        'strict_background_and_residual_atom_signs': strict_signs,
        'T_direct': render(T),
        'T_divisor_atoms': render(atom_sum),
        'weighted_residual_direct': render(green),
        'weighted_residual_absolute_sum': render(green_absolute),
        'divisor_atom_absolute_sum': render(atom_absolute)
    }


def main():
    reports = []
    for n in (4096, 1000000):
        start = time.perf_counter()
        engine = MobiusEndpoint(n)
        T, green, stats = engine.evaluate(n)
        assert T[1] - T[0] < 10 ** (DIGITS - 20)
        assert green[1] - green[0] < 10 ** (DIGITS - 20)
        row = {'N': n, 'h': str(H), 'thicknesses': [str(H), str(2 * H)],
               'normalized_weights': [2, -1], 'T_equal_H_D_minus_N_log_N': render(T),
               'weighted_residual_sum_n2_toN': render(green), 'algorithm': stats}
        if n == 4096:
            direct_T, direct_green, direct_report = direct_check(n)
            assert overlaps(T, direct_T) and overlaps(green, direct_green)
            row['full_population_crosscheck'] = direct_report
        row['elapsed_seconds_diagnostic_only'] = round(time.perf_counter() - start, 3)
        reports.append(row)
        print(json.dumps({'completed_N': n, 'T': render(T),
                          'sieve_cutoff': stats['sieve_cutoff'],
                          'states': stats['mobius_states_above_cutoff'],
                          'recursion_blocks': stats['recursion_quotient_blocks'],
                          'elapsed_seconds': row['elapsed_seconds_diagnostic_only']}, ensure_ascii=False), flush=True)
    report = {
        'status': 'EXACT_INTEGER_ARITHMETIC_CERTIFICATES_PASSED',
        'precision': {'fixed_decimal_places': DIGITS, 'Euler_Maclaurin_anchor': ANCHOR,
                      'Euler_Maclaurin_order': EM_ORDER, 'atanh_log_terms': LOG_TERMS,
                      'arithmetic': 'integer endpoints and Fraction coefficients; all rounding outward'},
        'endpoints': reports,
        'scope': ['One 4096 endpoint crosschecked with all integer roads, direct residual accumulation, and divisor atoms.',
                  'The 1000000 endpoint uses a sublinear sieve cutoff and exact quotient-recursive interval certificate.',
                  'No full 1000000-point road sequence or positive-energy window is claimed certified.',
                  'Fixed h is a computational example, not an asymptotically matched RH window family.',
                  'Running time is diagnostic only; operation counts describe the reproducible resource reduction.']
    }
    Path(__file__).with_name('arithmetic_certificate_results.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(report['status'], flush=True)


if __name__ == '__main__':
    main()
