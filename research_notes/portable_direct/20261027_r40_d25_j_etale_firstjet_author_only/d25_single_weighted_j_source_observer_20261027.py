#!/usr/bin/env python3
"""Exact author regression for D25 auxiliary (9+6 theta_t)j CM source observer.
Only integer/finite unramified-quadratic arithmetic. NOT native H0/B0 or a LIFT proof.
"""
import json
from math import gcd
from pathlib import Path


def primes_below(limit):
    sieve = [True] * limit
    sieve[0:2] = [False, False]
    for d in range(2, int(limit**.5) + 1):
        if sieve[d]:
            for k in range(d*d, limit, d):
                sieve[k] = False
    return [k for k, v in enumerate(sieve) if v]


class Quadratic:
    def __init__(self, modulus):
        self.n = modulus
        self.zero = (0, 0)
        self.one = (1, 0)
        self.s = (0, 1)

    def z(self, n):
        return (n % self.n, 0)

    def add(self, x, y):
        return ((x[0]+y[0]) % self.n, (x[1]+y[1]) % self.n)

    def neg(self, x):
        return (-x[0] % self.n, -x[1] % self.n)

    def sub(self, x, y):
        return self.add(x, self.neg(y))

    def mul(self, x, y):
        return ((x[0]*y[0]+2*x[1]*y[1]) % self.n,
                (x[0]*y[1]+x[1]*y[0]) % self.n)

    def inv(self, x):
        norm = (x[0]*x[0]-2*x[1]*x[1]) % self.n
        if gcd(norm, self.n) != 1:
            raise ArithmeticError(f'nonunit norm {norm} modulo {self.n}')
        z = pow(norm, -1, self.n)
        return (x[0]*z % self.n, -x[1]*z % self.n)

    def div(self, x, y):
        return self.mul(x, self.inv(y))

    def pow(self, x, e):
        out = self.one
        while e:
            if e & 1:
                out = self.mul(out, x)
            x = self.mul(x, x)
            e >>= 1
        return out

    def J(self, x):
        a = self.add(self.one, x)
        b = self.add(self.one, self.mul(self.z(9), x))
        return self.div(self.mul(self.z(27), self.mul(a, self.pow(b, 3))), x)

    def Jprime(self, x):
        x2 = self.pow(x, 2)
        a = self.add(self.one, self.mul(self.z(9), x))
        b = self.sub(self.add(self.mul(self.z(27), x2),
                              self.mul(self.z(18), x)), self.one)
        return self.div(self.mul(self.z(27), self.mul(self.pow(a, 2), b)), x2)

    def M(self, x):
        # (9+6*theta_t)J; theta_t = x(1+x)/(1-x) d/dx.
        t_factor = self.div(self.mul(x, self.add(self.one, x)),
                            self.sub(self.one, x))
        return self.add(self.mul(self.z(9), self.J(x)),
                        self.mul(self.z(6), self.mul(t_factor, self.Jprime(x))))

    def t(self, x):
        return self.div(x, self.mul(self.z(27), self.pow(self.add(self.one, x), 2)))


def check_one(p, power=4):
    ring = Quadratic(p**power)
    plus = (3 % ring.n, 2 % ring.n)
    minus = ring.inv(plus)
    assert minus == (3 % ring.n, -2 % ring.n)
    assert ring.t(plus) == ring.t(minus)
    assert ring.t(plus) == (pow(216, -1, ring.n), 0)
    expected = ring.mul(ring.z(-50388480), ring.s)
    assert ring.sub(ring.M(plus), ring.M(minus)) == expected
    assert ring.sub(ring.M(plus), ring.M(minus))[1] % p != 0
    # Deform x within the + ball. Reciprocal preserves t, lands in - ball.
    for a, b in ((0, 0), (1, 0), (0, 1), (2, 3)):
        xp = ring.add(plus, (p*a % ring.n, p*b % ring.n))
        xm = ring.inv(xp)
        assert ring.t(xp) == ring.t(xm)
        assert (xp[0] % p, xp[1] % p) == (3 % p, 2 % p)
        assert (xm[0] % p, xm[1] % p) == (3 % p, -2 % p)
        diff = ring.sub(ring.M(xp), ring.M(xm))
        assert diff[1] % p == (-50388480) % p
        assert diff[0] % p == 0
    return {'prime': p, 'modulus': ring.n, 'base_observer_difference': list(expected),
            'deformations': 4}


def main():
    target = [p for p in primes_below(5000) if p % 24 in (13, 19)]
    rows = [check_one(p) for p in target]
    assert len(rows) == 166, len(rows)
    # p=5 is an intentional exception to this exact choice of operator.
    ring5 = Quadratic(5**4)
    x = (3, 2)
    diff5 = ring5.sub(ring5.M(x), ring5.M(ring5.inv(x)))
    assert diff5[0] % 5 == diff5[1] % 5 == 0
    result = {
        'status': 'AUTHOR_EXACT_CHECK_PASS',
        'scope': 'auxiliary modular curve observer; not original H0/B0 or LIFT',
        'target_primes_below_5000': len(target),
        'deformation_checks': 4*len(target),
        'fixed_cm_difference_exact': '-50388480*s = -2^9*3^9*5*s',
        'quotient_coefficient_exact': '-12597120 = -2^7*3^9*5',
        'p5_expected_boundary': list(diff5),
        'samples': [r for r in rows if r['prime'] in (13, 19, 37, 43)],
        'admission': 'UNREVIEWED_NOT_ADMITTED',
    }
    out = Path(__file__).with_name('d25_single_weighted_j_source_observer_author_check_20261027.json')
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
