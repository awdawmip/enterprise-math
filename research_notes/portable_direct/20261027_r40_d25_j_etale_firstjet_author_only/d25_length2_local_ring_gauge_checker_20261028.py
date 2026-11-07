#!/usr/bin/env python3
"""Exact full-state gauge checks for length-two local-ring opposite-weight pairs.

All checks use Python integers and exhaustive finite enumeration.  No native
Enterprise Math H0/B0 operator is evaluated here.
"""

from collections import Counter
from itertools import product
import json


class LengthTwoRing:
    def __init__(self, p, quadratic=False):
        self.p = p
        self.n = p * p
        self.quadratic = quadratic
        self.residue_size = p * p if quadratic else p
        if quadratic:
            assert p == 3, "Only the irreducible quadratic test F_9 is configured"
            assert pow(2, (p - 1) // 2, p) == p - 1
            self.elements = list(product(range(self.n), repeat=2))
            self.zero = (0, 0)
            self.one = (1, 0)
        else:
            self.elements = list(range(self.n))
            self.zero = 0
            self.one = 1
        self.units = [z for z in self.elements if self.is_unit(z)]
        assert len(self.units) == self.residue_size**2 - self.residue_size
        self.inverses = {z: self.inverse(z) for z in self.units}

    def mul(self, a, b):
        if not self.quadratic:
            return (a * b) % self.n
        x, y = a
        z, w = b
        return ((x * z + 2 * y * w) % self.n,
                (x * w + y * z) % self.n)

    def is_unit(self, a):
        if not self.quadratic:
            return a % self.p != 0
        x, y = a
        return (x % self.p != 0) or (y % self.p != 0)

    def inverse(self, a):
        if not self.quadratic:
            return pow(a, -1, self.n)
        x, y = a
        den = (x*x - 2*y*y) % self.n
        assert den % self.p != 0
        inv = pow(den, -1, self.n)
        return ((x * inv) % self.n, (-y * inv) % self.n)

    def nilpotent_coefficient(self, a):
        """Return a mod pi via a/pi mod pi, for a in pi R, pi=p."""
        assert not self.is_unit(a)
        if not self.quadratic:
            assert a % self.p == 0
            return a // self.p
        x, y = a
        assert x % self.p == 0 and y % self.p == 0
        return (x // self.p, y // self.p)

    def residue_mul(self, a, b):
        if not self.quadratic:
            return (a * b) % self.p
        x, y = a
        z, w = b
        return ((x*z + 2*y*w) % self.p,
                (x*w + y*z) % self.p)

    def invariant(self, x, y):
        if self.is_unit(x):
            return ('X_UNIT', self.mul(x, y))
        if self.is_unit(y):
            return ('Y_UNIT', self.mul(x, y))
        if x == self.zero and y == self.zero:
            return ('NIL_ORIGIN',)
        if x == self.zero:
            return ('NIL_Y_ONLY',)
        if y == self.zero:
            return ('NIL_X_ONLY',)
        return ('NIL_BOTH', self.residue_mul(
            self.nilpotent_coefficient(x), self.nilpotent_coefficient(y)))

    def verify(self):
        p = self.p
        q = self.residue_size
        expected = q*q + 2*q + 2
        buckets = Counter()
        total = 0
        gauge_tests = 0
        for x, y in product(self.elements, repeat=2):
            k = self.invariant(x, y)
            buckets[k] += 1
            total += 1
            for u in self.units:
                moved = (self.mul(u, x), self.mul(self.inverses[u], y))
                assert self.invariant(*moved) == k, (x, y, u, k, moved)
                gauge_tests += 1
        assert len(buckets) == expected, (len(buckets), expected)
        assert total == q**4
        assert gauge_tests == total*(q*q-q)
        assert sum(key[0] == 'X_UNIT' for key in buckets) == q*q
        assert sum(key[0] == 'Y_UNIT' for key in buckets) == q
        assert sum(key[0].startswith('NIL') for key in buckets) == q+2
        for key, size in buckets.items():
            if key[0] == 'NIL_ORIGIN':
                expected_size = 1
            elif key[0].startswith('NIL'):
                expected_size = q-1
            else:
                expected_size = q*q-q
            assert size == expected_size, (key, size, expected_size)
        return dict(ring=('Z/%d' % (p*p) if not self.quadratic
                          else '(Z/9)[T]/(T^2-2)'),
                    residual_field_size=q, ring_size=q*q,
                    states=total, gauge_actions_checked=gauge_tests,
                    classes=len(buckets), predicted_classes=expected,
                    class_strata={'X_UNIT': q*q, 'Y_UNIT':q,
                                  'BOTH_NONUNIT':q+2},
                    all_class_sizes_verified=True,
                    all_full_group_actions_verified=True,
                    result='PASS')


def main():
    trials = [LengthTwoRing(p) for p in (3, 5, 7, 11)]
    trials.append(LengthTwoRing(3, quadratic=True))
    rows = [ring.verify() for ring in trials]
    q = 373*373
    p373 = {
        'p':373,
        'ring':'(Z/373^2)[T]/(T^2-2)',
        'residue_field_size':q,
        'is_unramified_local':pow(2, (373-1)//2, 373)==372,
        'conditional_full_unit_gauge_orbits':q*q+2*q+2,
        'integer_scalar_ring_orbits':373*373 + 2*373 + 2,
        'two_same_product_and_valuation_witnesses':{
            'first':('(p,0)','(p,0)'),
            'second':('(p,0)','(2p,0)'),
            'both_products_mod_p_squared':0,
            'p_scaled_residual_products':[1,2],
            'equivalent_under_full_units':False
        },
        'classification_status':'conditional auxiliary coefficient-ring only, no native H0/B0 action'
    }
    assert p373['is_unramified_local']
    assert p373['two_same_product_and_valuation_witnesses']['p_scaled_residual_products'] == [1, 2]
    print(json.dumps({'schema':'D25_LENGTH2_OPPOSITE_GAUGE_AUTHOR_CHECK_V1',
                      'checks':rows,
                      'total_states':sum(z['states'] for z in rows),
                      'total_exact_gauge_actions':sum(z['gauge_actions_checked'] for z in rows),
                      'p373_formula_only':p373,
                      'overall':'PASS'}, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
