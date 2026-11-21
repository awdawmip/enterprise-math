#!/usr/bin/env python3
"""Rationalized stable nodes, full-window bridge and genuine endpoint intervals.

Reuses the proved arithmetic method of the previous source, with a new generic
log/exp power oracle. No file in a previously published directory is modified.
All certificate operations are integer/Fraction enclosures, rounded outward.
"""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import json
import time

DIGITS = 60
SCALE = 10 ** DIGITS
ZERO = (0, 0)
ONE = (SCALE, SCALE)
Y, Z = 1024, 32768
M = 11
GRID = 2 ** 21
ANCHOR = 256
EM_ORDER = 16
LOG_TERMS = 80
EXP_TERMS = 48
QUERY_NODES = (1024, 1296, 2401, 4096, 6561, 10000, 14641, 20736, 28561, 32768)


def ceildiv(n, d):
    return -((-n) // d)


def rat(value):
    value = F(value)
    return value.numerator * SCALE // value.denominator, ceildiv(value.numerator * SCALE, value.denominator)


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def neg(x):
    return -x[1], -x[0]


def sub(x, y):
    return add(x, neg(y))


def scale(x, c):
    c = F(c)
    a, b = x if c >= 0 else (x[1], x[0])
    return a * c.numerator // c.denominator, ceildiv(b * c.numerator, c.denominator)


def mul(x, y):
    values = [a * b for a in x for b in y]
    return min(values) // SCALE, ceildiv(max(values), SCALE)


def reciprocal(x):
    assert x[0] > 0
    return SCALE * SCALE // x[1], ceildiv(SCALE * SCALE, x[0])


def divide(x, y):
    return mul(x, reciprocal(y))


def ipow(x, k):
    value = ONE
    while k:
        if k & 1:
            value = mul(value, x)
        x = mul(x, x)
        k //= 2
    return value


def floor_root(n, k):
    if n < 2:
        return n
    x = 1 << ((n.bit_length() + k - 1) // k)
    while True:
        nxt = ((k - 1) * x + n // x ** (k - 1)) // k
        if nxt >= x:
            break
        x = nxt
    while (x + 1) ** k <= n:
        x += 1
    while x ** k > n:
        x -= 1
    assert x ** k <= n < (x + 1) ** k
    return x


def isqrt_integer(n):
    q = floor_root(n * SCALE * SCALE, 2)
    return q, q + 1


def bernoulli_numbers(limit):
    values = [F(1)]
    for n in range(1, limit + 1):
        values.append(-sum(F(comb(n + 1, k)) * values[k] for k in range(n)) / (n + 1))
    return values


BERNOULLI = bernoulli_numbers(2 * EM_ORDER)
BERNOULLI_BOUND = sum(F(comb(2 * EM_ORDER, j)) * abs(BERNOULLI[j])
                      for j in range(2 * EM_ORDER + 1))


class Elementary:
    def __init__(self):
        self.logs = {1: ZERO}
        self.exp_calls = 0
        self.logs[2] = self.log_unit(rat(2))

    @staticmethod
    def log_unit(t):
        assert t[0] >= SCALE and t[1] <= 2 * SCALE
        z = divide(sub(t, ONE), add(t, ONE))
        zz = mul(z, z)
        term = z
        total = ZERO
        for k in range(LOG_TERMS):
            total = add(total, scale(term, F(2, 2 * k + 1)))
            term = mul(term, zz)
        tail = F(2) * F(1, 3) ** (2 * LOG_TERMS + 1)
        tail /= F(2 * LOG_TERMS + 1) * (1 - F(1, 9))
        return total[0], total[1] + ceildiv(SCALE * tail.numerator, tail.denominator)

    def log_integer(self, n):
        if n not in self.logs:
            e = n.bit_length() - 1
            unit = self.log_unit(rat(F(n, 2 ** e)))
            self.logs[n] = add(scale(self.logs[2], e), unit)
        return self.logs[n]

    def exp_positive(self, x):
        assert x[0] >= 0
        self.exp_calls += 1
        r = 0
        while x[1] > (SCALE // 2) * 2 ** r:
            r += 1
        small = scale(x, F(1, 2 ** r))
        term, total = ONE, ONE
        for k in range(1, EXP_TERMS + 1):
            term = scale(mul(term, small), F(1, k))
            total = add(total, term)
        # For 0 <= z <= 1/2, tail after K is bounded by
        # (1/2)^(K+1)/(K+1)! / (1 - 1/[2(K+2)]).
        tail = F(1, 2) ** (EXP_TERMS + 1) / factorial(EXP_TERMS + 1)
        tail /= 1 - F(1, 2 * (EXP_TERMS + 2))
        total = total[0], total[1] + ceildiv(tail.numerator * SCALE, tail.denominator)
        for _ in range(r):
            total = mul(total, total)
        return total

    def exp_negative(self, x):
        return reciprocal(self.exp_positive(x))

    @staticmethod
    def arctan_inverse(k, terms):
        x = F(1, k)
        total = sum((-1) ** j * x ** (2 * j + 1) / (2 * j + 1)
                    for j in range(terms))
        next_term = x ** (2 * terms + 1) / (2 * terms + 1)
        lo, hi = ((total, total + next_term) if terms % 2 == 0
                  else (total - next_term, total))
        return rat(lo)[0], rat(hi)[1]

    @classmethod
    def pi(cls):
        return sub(scale(cls.arctan_inverse(5, 80), 16),
                   scale(cls.arctan_inverse(239, 24), 4))

    @staticmethod
    def cosine(x):
        assert 0 <= x[0] <= x[1] <= 4 * SCALE
        terms = 36
        square = mul(x, x)
        term, total = ONE, ONE
        for k in range(1, terms + 1):
            term = scale(mul(term, square), F(1, (2 * k - 1) * (2 * k)))
            total = add(total, term if k % 2 == 0 else neg(term))
        tail = scale(mul(term, square), F(1, (2 * terms + 1) * (2 * terms + 2)))[1]
        return total[0] - tail, total[1] + tail


def make_nodes(elementary):
    d = M - 1
    # s = log(3+sqrt(8)); its argument divided by 4 lies in [1,2].
    unit = scale(add(rat(3), scale(isqrt_integer(2), 2)), F(1, 4))
    s = add(scale(elementary.logs[2], 2), elementary.log_unit(unit))
    e = elementary.exp_positive(scale(s, F(1, d)))
    tanh_half = divide(sub(e, ONE), add(e, ONE))
    b = scale(mul(tanh_half, tanh_half), F(1, 2))
    center = scale(add(rat(F(1, 2)), b), F(1, 2))
    radius = scale(sub(rat(F(1, 2)), b), F(1, 2))
    pi = elementary.pi()
    ideals, nodes = [], []
    for j in range(M):
        if j == 0:
            ideal = b
        elif j == d:
            ideal = rat(F(1, 2))
        else:
            cosine = elementary.cosine(scale(pi, F(j, d)))
            ideal = sub(center, mul(radius, cosine))
        numerator = ((ideal[0] + ideal[1]) * GRID + SCALE) // (2 * SCALE)
        node = F(numerator, GRID)
        error = max(abs(node - F(ideal[0], SCALE)), abs(node - F(ideal[1], SCALE)))
        assert error <= F(1, 2 * GRID)
        ideals.append(ideal)
        nodes.append(node)
    assert all(0 < nodes[j] < nodes[j + 1] for j in range(M - 1))
    assert nodes[-1] == F(1, 2)
    epsilon = F(1, 2 * GRID)
    assert epsilon <= F(1, 2 * 1024 * M * d * d)
    weights = []
    for j, a in enumerate(nodes):
        value = F(1)
        for k, other in enumerate(nodes):
            if k != j:
                value *= other / (other - a)
        weights.append(value)
    for power in range(M):
        assert sum(w * a ** power for a, w in zip(nodes, weights)) == (1 if power == 0 else 0)
    assert sum(w / a for a, w in zip(nodes, weights)) == sum(1 / a for a in nodes)
    norm = sum(abs(w) for w in weights)
    raw_norm = sum(abs(w) / a for a, w in zip(nodes, weights))
    assert norm < F(31, 10)
    product = F(1)
    for a in nodes:
        product *= a
    L = elementary.log_integer(Z)
    assert 10 * SCALE < L[0] <= L[1] < 11 * SCALE
    eta = scale(ipow(L, M + 1), product / factorial(M + 1))
    normalized_bridge = mul(mul(eta, L), isqrt_integer(Z))
    assert normalized_bridge[1] < SCALE // 2
    assert Y ** 3 == Z ** 2
    return nodes, weights, {
        'ideal_nodes': [render(x) for x in ideals],
        'grid_denominator': GRID,
        'node_grid_numerators': [int(a * GRID) for a in nodes],
        'nodes': [str(a) for a in nodes],
        'weights': [str(w) for w in weights],
        'weight_absolute_sum_exact': str(norm),
        'weight_absolute_sum': render(rat(norm)),
        'raw_R_amplification_exact': str(raw_norm),
        'raw_R_amplification': render(rat(raw_norm)),
        'unit_port_sum_inverse_nodes_exact': str(sum(1 / a for a in nodes)),
        'product_exact': str(product),
        'derivative_error_coefficient_exact': str(product / factorial(M + 1)),
        'moment_identities_checked': M,
        'pointwise_eta_uniform_n_le_Z': render(eta),
        'sup_error_div_sqrt_y_for_all_y_le_Z': render(normalized_bridge),
        'absolute_error_bound_at_Z': render(scale(mul(eta, L), Z)),
        'rounding_error_bound_exact': str(epsilon),
        'rounding_is_certified_against_ideal_Chebyshev_nodes': True,
    }


def linear_sieve(limit):
    spf = [0] * (limit + 1)
    mu = [0] * (limit + 1)
    mu[1] = 1
    primes = []
    for n in range(2, limit + 1):
        if not spf[n]:
            spf[n] = n
            primes.append(n)
            mu[n] = -1
        for p in primes:
            value = n * p
            if value > limit:
                break
            spf[value] = p
            if n % p == 0:
                mu[value] = 0
                break
            mu[value] = -mu[n]
    return spf, mu


class GenericPowerOracle:
    def __init__(self, nodes, base_limit, elementary):
        self.nodes = tuple(nodes)
        self.m = len(nodes)
        self.rates = tuple(nodes) + tuple(a + 1 for a in nodes) + (F(1),)
        self.base = max(base_limit, ANCHOR)
        self.elementary = elementary
        self.spf, self.mu = linear_sieve(self.base)
        self.power_cache = {1: (ONE,) * len(self.rates)}
        self.prime_powers = {}
        self.small_powers = [None] * (self.base + 1)
        self.small_powers[1] = (ONE,) * self.m
        for n in range(2, self.base + 1):
            p = self.spf[n]
            if p not in self.prime_powers:
                lp = elementary.log_integer(p)
                self.prime_powers[p] = tuple(elementary.exp_negative(scale(lp, a)) for a in self.nodes)
            self.small_powers[n] = tuple(mul(x, y) for x, y in
                                         zip(self.small_powers[n // p], self.prime_powers[p]))
        self.prefix = [[ZERO] * (ANCHOR + 1) for _ in self.rates]
        self.Mprefix = [[ZERO] * (self.base + 1) for _ in self.rates[:-1]]
        for n in range(1, self.base + 1):
            values = self.powers(n)
            if n <= ANCHOR:
                for j, value in enumerate(values):
                    self.prefix[j][n] = add(self.prefix[j][n - 1], value)
            for j, value in enumerate(values[:-1]):
                self.Mprefix[j][n] = add(self.Mprefix[j][n - 1], scale(value, self.mu[n]))
        self.coefficients, self.radii = [], []
        anchor_powers = self.powers(ANCHOR)
        for j, a in enumerate(self.rates):
            rising = F(1)
            coefficients = []
            for k in range(1, 2 * EM_ORDER + 1):
                rising *= a + k - 1
                if k % 2:
                    coefficients.append(BERNOULLI[k + 1] * rising / factorial(k + 1))
            self.coefficients.append(coefficients)
            coefficient = (BERNOULLI_BOUND * rising / factorial(2 * EM_ORDER)
                           / (a + 2 * EM_ORDER - 1) / ANCHOR ** (2 * EM_ORDER - 1))
            self.radii.append(ceildiv(coefficient.numerator * anchor_powers[j][1], coefficient.denominator))
        self.sum_cache = {}

    def powers(self, n):
        if n not in self.power_cache:
            if n <= self.base:
                values = self.small_powers[n]
            else:
                ln = self.elementary.log_integer(n)
                values = tuple(self.elementary.exp_negative(scale(ln, a)) for a in self.nodes)
            self.power_cache[n] = tuple(values) + tuple(scale(v, F(1, n)) for v in values) + (rat(F(1, n)),)
        return self.power_cache[n]

    def power_sum(self, j, n):
        if n <= ANCHOR:
            return self.prefix[j][n]
        key = (j, n)
        if key not in self.sum_cache:
            a = self.rates[j]
            end, start = self.powers(n)[j], self.powers(ANCHOR)[j]
            if a == 1:
                integral = sub(self.elementary.log_integer(n), self.elementary.log_integer(ANCHOR))
            else:
                integral = scale(sub(scale(end, n), scale(start, ANCHOR)), 1 / (1 - a))
            total = add(add(self.prefix[j][ANCHOR], integral), scale(sub(end, start), F(1, 2)))
            for r, coefficient in enumerate(self.coefficients[j], 1):
                power = 2 * r - 1
                difference = sub(scale(start, F(1, ANCHOR ** power)), scale(end, F(1, n ** power)))
                total = add(total, scale(difference, coefficient))
            self.sum_cache[key] = total[0] - self.radii[j], total[1] + self.radii[j]
        return self.sum_cache[key]

    def gamma(self):
        index = 2 * self.m
        value = sub(self.prefix[index][ANCHOR], self.elementary.log_integer(ANCHOR))
        value = sub(value, rat(F(1, 2 * ANCHOR)))
        for r in range(1, EM_ORDER + 1):
            value = add(value, rat(BERNOULLI[2 * r] / (2 * r * ANCHOR ** (2 * r))))
        return value[0] - self.radii[index], value[1] + self.radii[index]


def quotient_blocks(n, first=1):
    left = first
    while left <= n:
        q = n // left
        right = n // q
        yield left, right, q
        left = right + 1


class EndpointEngine:
    def __init__(self, nodes, weights, elementary):
        base = floor_root(Z * Z, 3)
        if base ** 3 < Z * Z:
            base += 1
        self.oracle = GenericPowerOracle(nodes, base, elementary)
        self.nodes, self.weights = tuple(nodes), tuple(weights)
        self.m = len(nodes)
        self.cache = {}
        self.recursion_blocks = 0
        self.endpoint_blocks = 0
        self.gamma = self.oracle.gamma()

    def mobius(self, n):
        if n <= self.oracle.base:
            return tuple(row[n] for row in self.oracle.Mprefix)
        if n not in self.cache:
            result = [ONE] * (2 * self.m)
            for left, right, q in quotient_blocks(n, 2):
                inside = self.mobius(q)
                for j in range(2 * self.m):
                    mass = sub(self.oracle.power_sum(j, right), self.oracle.power_sum(j, left - 1))
                    result[j] = sub(result[j], mul(mass, inside[j]))
                self.recursion_blocks += 1
            self.cache[n] = tuple(result)
        return self.cache[n]

    def endpoint(self, n):
        self.mobius(n)
        U, V = [ZERO] * self.m, [ZERO] * self.m
        for left, right, q in quotient_blocks(n):
            hi, lo = self.mobius(right), self.mobius(left - 1)
            harmonic = self.oracle.power_sum(2 * self.m, q)
            for j in range(self.m):
                U[j] = add(U[j], scale(sub(hi[j], lo[j]), q))
                V[j] = add(V[j], mul(harmonic, sub(hi[j + self.m], lo[j + self.m])))
            self.endpoint_blocks += 1
        A, B = ZERO, ZERO
        for j, (a, w) in enumerate(zip(self.nodes, self.weights)):
            A = add(A, scale(sub(V[j], ONE), w / a))
            B = add(B, scale(sub(U[j], ONE), w / a))
        center = sub(scale(add(ONE, self.gamma), n), scale(self.oracle.elementary.log_integer(n), n))
        value = add(sub(scale(A, n), B), center)
        assert value[1] - value[0] < 10 ** (DIGITS - 22)
        per_node = []
        for j, a in enumerate(self.nodes):
            Hj = scale(sub(sub(scale(V[j], n), U[j]), rat(n - 1)), 1 / a)
            per_node.append({'a': str(a), 'U_R_including_unit': render(U[j]),
                             'V_R_over_n_including_unit': render(V[j]),
                             'G_a': render(add(Hj, center))})
        return {'N': n, 'F': render(value), 'A_D_excluding_unit': render(A),
                'B_D_excluding_unit': render(B), 'per_thickness_ports': per_node}


def render(interval, places=28):
    unit = 10 ** (DIGITS - places)
    lo = interval[0] // unit * unit
    hi = ceildiv(interval[1], unit) * unit
    def decimal(integer):
        sign = '-' if integer < 0 else ''
        integer = abs(integer)
        return f'{sign}{integer // SCALE}.{integer % SCALE // unit:0{places}d}'
    return {'lower': decimal(lo), 'upper': decimal(hi),
            'width_upper': str(F(interval[1] - interval[0], SCALE))}


def main():
    started = time.perf_counter()
    elementary = Elementary()
    nodes, weights, certificate = make_nodes(elementary)
    print(json.dumps({'node_bridge_certified': True,
                      'node_grid_numerators': certificate['node_grid_numerators'],
                      'weight_norm': certificate['weight_absolute_sum'],
                      'eta': certificate['pointwise_eta_uniform_n_le_Z'],
                      'normalized_bridge': certificate['sup_error_div_sqrt_y_for_all_y_le_Z']}, ensure_ascii=False), flush=True)
    engine = EndpointEngine(nodes, weights, elementary)
    endpoints = []
    for n in QUERY_NODES:
        row = engine.endpoint(n)
        endpoints.append(row)
        print(json.dumps({'endpoint_N': n, 'F': row['F'],
                          'shared_M_states': len(engine.cache)}, ensure_ascii=False), flush=True)
    report = {
        'status': 'EXACT_RATIONAL_MATCHED_WINDOW_AND_ENDPOINTS_PASSED',
        'window': {'Y': Y, 'Z': Z, 'lambda': '3/2', 'theta': '1/2'},
        'm': M, 'max_thickness': '1/2', 'node_certificate': certificate,
        'gamma': render(engine.gamma, places=45), 'endpoints': endpoints,
        'precision': {'decimal_places': DIGITS, 'log_terms': LOG_TERMS, 'exp_terms': EXP_TERMS,
                      'EM_anchor': ANCHOR, 'EM_order': EM_ORDER,
                      'arithmetic': 'integer/Fraction outward enclosures; no floating input enters a certificate'},
        'counts': {'sieve_cutoff': engine.oracle.base, 'shared_M_states': len(engine.cache),
                   'recursion_quotient_blocks': engine.recursion_blocks,
                   'endpoint_quotient_blocks': engine.endpoint_blocks,
                   'cached_large_power_sums': len(engine.oracle.sum_cache),
                   'log_values': len(elementary.logs), 'exp_evaluations': elementary.exp_calls,
                   'high_degree_algebraic_roots': 0},
        'elapsed_seconds_diagnostic_only': round(time.perf_counter() - started, 3),
        'scope': ['All nodes and weights are exact rationals; their relation to ideal Chebyshev extrema is interval-certified.',
                  'The D-Lambda bound and centered bridge hold for every real 1<=y<=32768, hence the full requested window.',
                  'Every endpoint preserves all integer inputs, the original prefix history, the unit subtraction and gamma.',
                  'Endpoint intervals are passed to the separate window-energy author branch; no energy bound is asserted here.',
                  'This finite instance closes the matched-node evaluation interface; no uniform asymptotic bit-cost theorem is asserted.']
    }
    Path(__file__).with_name('rational_window_certificate.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(report['status'], flush=True)


if __name__ == '__main__':
    main()
