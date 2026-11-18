"""Budgeted quadratic Lucas and wheel branches from the frozen manuscript."""
from collections import Counter
from math import gcd, isqrt


class Exhausted(Exception):
    pass


class Work:
    def __init__(self, limit):
        self.limit = limit
        self.left = limit
        self.counts = Counter()
        self.pending = None
        self.degenerate = 0

    def pay(self, label):
        if self.left == 0:
            self.pending = label
            raise Exhausted
        self.left -= 1
        self.counts[label] += 1


def prime_powers(bound, pay):
    for p in range(2, bound + 1):
        pay('prime_candidate')
        for divisor in range(2, isqrt(p) + 1):
            pay('prime_trial')
            if p % divisor == 0:
                break
        else:
            power = p
            while True:
                pay('power_trial')
                if power > bound // p:
                    break
                power *= p
            yield power


def lucas(trace, exponent, n, pay):
    a, b = 2 % n, trace % n
    for bit in range(exponent.bit_length() - 1, -1, -1):
        pay('lucas_cross')
        middle = (a * b - trace) % n
        pay('lucas_square')
        if (exponent >> bit) & 1:
            a, b = middle, (b * b - 2) % n
        else:
            a, b = (a * a - 2) % n, middle
    return a


def wheel_primes(d, pay):
    x, divisor = d, 2
    while True:
        pay('D_trial')
        if divisor * divisor > x:
            break
        if x % divisor == 0:
            yield divisor
            while True:
                pay('D_strip')
                x //= divisor
                if x % divisor:
                    break
        divisor += 1
    if x > 1:
        yield x


def screen(n, bound=50, d=210, limit=10000, route='both'):
    params = dict(N=n, B1=bound, D=d, limit=limit, route=route)
    if (any(type(x) is not int for x in (n, bound, d, limit))
            or n < 2 or bound < 2 or d < 2 or limit < 0
            or route not in ('lucas', 'wheel', 'both')):
        return dict(params=params, status='INVALID_INPUT', used=0, work={})
    w = Work(limit)

    def end(status, factor=None):
        return dict(params=params, status=status, factor=factor, used=limit-w.left,
                    remaining=w.left, pending=w.pending, work=dict(w.counts),
                    degenerate_gcd=w.degenerate)

    def check(g):
        if not 1 < g < n:
            return None
        w.pay('factor_validation')
        if n % g:
            return None
        return end('FACTOR_FOUND', g)

    def from_gcd(x):
        w.pay('candidate_gcd')
        g = gcd(x, n)
        if g == n:
            w.degenerate += 1
        return check(g)

    try:
        w.pay('even_trial')
        if n % 2 == 0:
            return check(2) or end('NO_HIT_IN_DECLARED_SEARCH')
        if route in ('lucas', 'both'):
            trace = 3 % n
            for power in prime_powers(bound, w.pay):
                trace = lucas(trace, power, n, w.pay)
                hit = from_gcd(trace - 2)
                if hit:
                    return hit
        if route in ('wheel', 'both'):
            for p in wheel_primes(d, w.pay):
                w.pay('wheel_prime_trial')
                if n % p == 0:
                    hit = check(p)
                    if hit:
                        return hit
            w.pay('square_test')
            r = isqrt(n)
            if r*r == n:
                hit = check(r)
                if hit:
                    return hit
            for x in range(r, r+d+1):
                w.pay('fermat_candidate')
                diff = x*x - n
                if diff >= 0:
                    y = isqrt(diff)
                    if y*y == diff:
                        hit = from_gcd(x-y)
                        if hit:
                            return hit
            lower = (r//d)*d
            product = 1
            for lo, hi in ((1, lower), (lower+1, lower+d)):
                for x in range(lo, hi+1):
                    w.pay('wheel_filter_gcd')
                    if gcd(x, d) == 1:
                        w.pay('wheel_modmul')
                        product = product*x % n
                hit = from_gcd(product)
                if hit:
                    return hit
        return end('NO_HIT_IN_DECLARED_SEARCH')
    except Exhausted:
        return end('BUDGET_EXHAUSTED')
