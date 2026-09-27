"""Simultaneous degree-three floor moments from actual BRC integer traces.

Signed Python integers encode (sign, magnitude). Only signs, finite indices,
zero tests and metadata are host wiring; magnitude arithmetic is delegated
to the existing typed full-adder composition. No modular order is inferred.
"""
from pathlib import Path
from copy import deepcopy
import hashlib
import sys

ROOT = Path(__file__).resolve().parent
LAZY = ROOT.parents[1] / 'sep26-shor-general/optimization/lazy_modular'
sys.path.insert(0, str(LAZY))
from lazy_modular import Arithmetic, source_binding

DEGREES = tuple((p, e) for e in range(4) for p in range(4-e))
BINOMIAL = ((1,), (1, 1), (1, 2, 1), (1, 3, 3, 1))


def require(test, message):
    if not test:
        raise ValueError(message)


class TypedFloorMoments:
    def __init__(self):
        self.arithmetic = Arithmetic()
        self.signed_operations = []
        self.cache, self.nodes, self.weight_queries = {}, [], []
        self.stats = {'moment_requests': 0, 'cache_hits': 0,
                      'max_recursion_depth': 0, 'max_observed_integer_bits': 0}
        self._source = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()

    def _check(self):
        require(hashlib.sha256(Path(__file__).read_bytes()).hexdigest() == self._source,
                'floor-moment source changed')

    def _record(self, kind, inputs, result, start):
        values = (*inputs, *(result if isinstance(result, tuple) else (result,)))
        self.stats['max_observed_integer_bits'] = max(
            self.stats['max_observed_integer_bits'], *(abs(x).bit_length() for x in values))
        self.signed_operations.append({'operation': kind, 'inputs': inputs,
            'result': result, 'typed_operation_indices': list(range(start, len(self.arithmetic.operations)))})
        return result

    def add(self, x, y):
        start = len(self.arithmetic.operations)
        if (x < 0) == (y < 0):
            magnitude, _ = self.arithmetic.add(abs(x), abs(y))
            answer = -magnitude if x < 0 else magnitude
        else:
            relation, magnitude, _ = self.arithmetic.compare(abs(x), abs(y))
            if relation < 0:
                _, magnitude, _ = self.arithmetic.compare(abs(y), abs(x))
                answer = -magnitude if y < 0 else magnitude
            else:
                answer = -magnitude if x < 0 else magnitude
        return self._record('signed_add', (x, y), answer, start)

    def sub(self, x, y):
        return self.add(x, -y)

    def mul(self, x, y):
        start = len(self.arithmetic.operations)
        magnitude, _ = self.arithmetic.multiply(abs(x), abs(y))
        answer = -magnitude if (x < 0) != (y < 0) else magnitude
        return self._record('signed_multiply', (x, y), answer, start)

    def floor_div(self, x, m):
        require(type(m) is int and m > 0, 'positive integer floor modulus required')
        start = len(self.arithmetic.operations)
        quotient, remainder, _ = self.arithmetic.divide(abs(x), m)
        if x < 0:
            if remainder:
                quotient, _ = self.arithmetic.add(quotient, 1)
                _, remainder, _ = self.arithmetic.compare(m, remainder)
            quotient = -quotient
        return self._record('signed_euclidean_division', (x, m), (quotient, remainder), start)

    def exact_div(self, x, m):
        quotient, remainder = self.floor_div(x, m)
        require(remainder == 0, 'fixed polynomial denominator is not exact')
        return quotient

    def total(self, terms):
        value = 0
        for term in terms:
            value = self.add(value, term)
        return value

    def small_power(self, value, exponent):
        require(type(exponent) is int and 0 <= exponent <= 3, 'fixed exponent 0..3 required')
        answer = 1
        for _ in range(exponent):
            answer = self.mul(answer, value)
        return answer

    def power_sums(self, n):
        if not n:
            return (0, 0, 0, 0)
        less = self.sub(n, 1)
        p1 = self.exact_div(self.mul(n, less), 2)
        p2 = self.exact_div(self.mul(self.mul(n, less), self.sub(self.mul(2, n), 1)), 6)
        p3 = self.mul(p1, p1)
        return (n, p1, p2, p3)

    def moments(self, n, m, a, b, _depth=0):
        self._check()
        require(all(type(x) is int for x in (n, m, a, b)) and n >= 0 and m >= 1,
                'integer n>=0, m>=1 and signed a,b required')
        self.stats['moment_requests'] += 1
        self.stats['max_recursion_depth'] = max(self.stats['max_recursion_depth'], _depth)
        key = n, m, a, b
        if key in self.cache:
            self.stats['cache_hits'] += 1
            return dict(self.cache[key])
        start = len(self.signed_operations)
        powers = self.power_sums(n)
        output = {(p, e): powers[p] if e == 0 else 0 for p, e in DEGREES}
        branch, child = 'empty', None
        if n:
            A, a0 = self.floor_div(a, m)
            B, b0 = self.floor_div(b, m)
            if A or B:
                branch, child = 'normalize_signed_coefficients', (n, m, a0, b0)
                g = self.moments(*child, _depth=_depth+1)
                for p, e in DEGREES:
                    if not e:
                        continue
                    terms = []
                    for k in range(e+1):
                        for l in range(e-k+1):
                            coefficient = self.mul(BINOMIAL[e][k], BINOMIAL[e-k][l])
                            coefficient = self.mul(coefficient, self.small_power(A, l))
                            coefficient = self.mul(coefficient, self.small_power(B, e-k-l))
                            terms.append(self.mul(coefficient, g[p+l, k]))
                    output[p, e] = self.total(terms)
            elif not a:
                branch = 'normalized_constant_zero'
            else:
                Y, _ = self.floor_div(self.add(self.mul(a, self.sub(n, 1)), b), m)
                if not Y:
                    branch = 'normalized_zero_height'
                else:
                    offset = self.sub(self.add(self.sub(m, b), a), 1)
                    branch, child = 'transpose_lattice', (Y, a, m, offset)
                    g = self.moments(*child, _depth=_depth+1)
                    y2, y3 = self.mul(Y, Y), self.small_power(Y, 3)
                    output[0, 1] = self.sub(self.mul(n, Y), g[0, 1])
                    output[1, 1] = self.sub(self.mul(powers[1], Y),
                        self.exact_div(self.sub(g[0, 2], g[0, 1]), 2))
                    output[2, 1] = self.sub(self.mul(powers[2], Y), self.exact_div(
                        self.total((self.mul(2, g[0, 3]), -self.mul(3, g[0, 2]), g[0, 1])), 6))
                    output[0, 2] = self.sub(self.mul(n, y2),
                        self.add(self.mul(2, g[1, 1]), g[0, 1]))
                    output[1, 2] = self.sub(self.mul(powers[1], y2), self.exact_div(
                        self.total((self.mul(2, g[1, 2]), g[0, 2], -self.mul(2, g[1, 1]), -g[0, 1])), 2))
                    output[0, 3] = self.sub(self.mul(n, y3),
                        self.total((self.mul(3, g[2, 1]), self.mul(3, g[1, 1]), g[0, 1])))
        self.cache[key] = dict(output)
        self.nodes.append({'parameters': key, 'branch': branch, 'child': child,
            'signed_operations_start': start, 'signed_operations_stop': len(self.signed_operations),
            'moments': {f'{p},{e}': output[p, e] for p, e in DEGREES}})
        return dict(output)

    def interval_count(self, V, R, x):
        require(type(V) is int and V >= 1 and type(R) is int and R >= 1,
                'positive integer interval and counting modulus required')
        v, u = self.floor_div(V, R)
        _, rho = self.floor_div(x, R)
        first, second = self.sub(u, rho), self.sub(u, self.sub(R, rho))
        return self.total((self.mul(R, self.mul(v, v)), self.mul(2, self.mul(v, u)),
                           first if first > 0 else 0, second if second > 0 else 0))

    def weighted_affine_count(self, H, V, R, a, b):
        """sum_j (H-j) Count(V,R,(aj+b) mod R), without enumerating j."""
        v, u = self.floor_div(V, R)
        powers = self.power_sums(H)
        weight_sum = self.sub(self.mul(H, H), powers[1])
        base = self.add(self.mul(R, self.mul(v, v)), self.mul(2, self.mul(v, u)))
        if not u:
            return self.mul(weight_sum, base)
        moment_sets = [self.moments(H, R, a, offset)
                       for offset in (b, self.sub(b, u), self.add(b, u))]

        def weighted(f, e):
            return self.sub(self.mul(H, f[0, e]), f[1, e])

        def weighted_x(f):
            j_part = self.sub(self.mul(H, f[1, 1]), f[2, 1])
            return self.add(self.mul(a, j_part), self.mul(b, weighted(f, 1)))

        f, fm, fp = moment_sets
        w1, wm1, wp1 = (weighted(x, 1) for x in moment_sets)
        w2, wm2, wp2 = (weighted(x, 2) for x in moment_sets)
        wx, wxm, wxp = (weighted_x(x) for x in moment_sets)
        twice_first = self.total((self.mul(self.mul(2, u), self.sub(w1, wm1)),
            -self.mul(2, self.sub(wx, wxm)),
            self.mul(R, self.sub(self.add(w2, w1), self.add(wm2, wm1)))))
        twice_second = self.total((self.mul(2, self.sub(wxp, wx)),
            self.mul(self.mul(2, self.sub(u, R)), self.sub(wp1, w1)),
            -self.mul(R, self.sub(self.sub(wp2, wp1), self.sub(w2, w1)))))
        return self.add(self.mul(weight_sum, base),
                        self.exact_div(self.add(twice_first, twice_second), 2))

    def window_weight(self, H, V, P, R, r, d):
        """Integer pair count only; R is NOT certified as any modular order here."""
        self._check()
        require(all(type(x) is int for x in (H, V, P, R, r, d)), 'strict integer inputs required')
        require(H >= 1 and V >= 1 and P >= 1 and R >= 1 and 0 <= r < R and -P < d < P,
                'positive sizes, canonical target and bounded displacement required')
        start = len(self.signed_operations)
        t, S = self.sub(r, self.mul(V, d)), self.mul(V, P)
        plus = self.weighted_affine_count(H, V, R, S, t)
        minus = self.weighted_affine_count(H, V, R, -S, t)
        center = self.mul(H, self.interval_count(V, R, t))
        answer = self.sub(self.add(plus, minus), center)
        require(answer >= 0, 'count became negative')
        self.weight_queries.append({'inputs': {'H': H, 'V': V, 'P': P, 'R': R, 'r': r, 'd': d},
            't': t, 'S': S, 'positive_slope_sum': plus, 'negative_slope_sum': minus,
            'double_counted_center': center, 'value': answer,
            'signed_operations_start': start, 'signed_operations_stop': len(self.signed_operations)})
        return answer

    def evidence(self):
        self._check()
        return deepcopy({'schema': 'BRC_DEGREE_THREE_FLOOR_MOMENTS_V1',
            'source_sha256': self._source, 'native_source': source_binding(),
            'arithmetic_operations': self.arithmetic.operations,
            'arithmetic_stats': self.arithmetic.stats,
            'signed_operations': self.signed_operations, 'moment_nodes': self.nodes,
            'window_weight_queries': self.weight_queries, 'stats': self.stats,
            'scope': 'integer counting only; no modular-order certification or phase propagation',
            'host_wiring': 'sign/magnitude encoding, fixed-degree indices, zero tests, cache routing, bit-length metadata'} )
