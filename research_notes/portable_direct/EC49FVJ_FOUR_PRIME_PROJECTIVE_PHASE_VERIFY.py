#!/usr/bin/env python3
"""EC49FVJ: exact p=19,31 projective certificates and four-prime CRT union.

Source science: EC49FVI @ dcb080750ff13eb6fccd75b5281d47eb7afe4cb6.
Only standard-library integers and fractions; no floating-point proof steps.
"""
from collections import Counter
from fractions import Fraction
from math import gcd, lcm, prod

U = Fraction(4822040484, 8132285009)
GAMMA = Fraction(141024, 1653649)
PRIMES = (11, 17, 19, 31)


def prime_certificate(p):
    def residue(q):
        assert q.denominator % p
        return q.numerator * pow(q.denominator, -1, p) % p

    u, gamma = residue(U), residue(GAMMA)
    inv637 = pow(637, -1, p)
    c = residue(Fraction(-3, 637))  # slope of L_a
    d = u * gamma % p               # slope of L_b
    assert c != d
    rows = []
    for z in range(p):
        la = (637 - 3 * z) * inv637 % p
        lb = u * (1 + gamma * z) % p
        a = (1 - (1 - z) * la) % p
        b = (1 - (1 - z) * lb) % p
        rows.append((z, a, b, la, lb))

    singular = [r for r in rows if r[3] == r[4]]
    assert len(singular) == 1
    sz, sa, sb, sla, slb = singular[0]
    assert sa == sb and sla == slb and sa and sla
    hcoef, ncoef = (-(1 - sz) * sla) % p, sa % p
    assert hcoef != 0 and ncoef != 0

    def nonsingular_values(h, n):
        out = []
        for z, a, b, la, lb in rows:
            if z == sz:
                continue
            out.append((pow(a, h, p) * pow(la, n, p)
                        - pow(b, h, p) * pow(lb, n, p))
                       * pow((la - lb) % p, -1, p) % p)
        # Homogenized divided difference at projective infinity
        out.append((pow(c, h + n, p) - pow(d, h + n, p))
                   * pow((c - d) % p, -1, p) % p)
        return out

    patterns = {
        (h, n) for h in range(p - 1) for n in range(p - 1)
        if all(nonsingular_values(h or p - 1, n or p - 1))
    }
    # Each base (h,n) mod (p-1) has p^2 lifts modulo p(p-1).
    # Exactly p lifts lie on hcoef*h+ncoef*n=0 modulo p.
    pairs = len(patterns) * p * (p - 1)
    expected = {11: (44, 4840), 17: (96, 26112),
                19: (66, 22572), 31: (402, 373860)}
    assert (len(patterns), pairs) == expected[p]

    def valid(h, n):
        assert h > 0 and n > 0
        return ((h % (p - 1), n % (p - 1)) in patterns
                and (hcoef * h + ncoef * n) % p != 0)

    def direct(h, n):
        vals = nonsingular_values(h, n)
        vals.append(pow(sla, n - 1, p) * pow(sa, h - 1, p)
                    * (n * sa - h * (1 - sz) * sla) % p)
        return all(vals)

    # Directly check positive examples, the zero-residue representatives,
    # and shifts by the prime-local complete period.
    period = p * (p - 1)
    for h in (1, 2, 3, 7, p - 1, p, p + 1, period):
        for n in (1, 2, 4, 9, p - 1, p, p + 2, period):
            assert valid(h, n) == direct(h, n), (p, h, n)
            assert valid(h, n) == valid(h + period, n + period)

    return dict(p=p, residue_u=u, residue_gamma=gamma,
                singular=(sz, sa, sla), derivative=(hcoef, ncoef),
                patterns=patterns, class_count=pairs, modulus=period,
                valid=valid)


def main():
    certificates = {p: prime_certificate(p) for p in PRIMES}
    period = lcm(*(p - 1 for p in PRIMES))
    assert period == 720
    counts = Counter()
    for h in range(period):
        for n in range(period):
            mask = sum(1 << i for i, p in enumerate(PRIMES)
                       if (h % (p - 1), n % (p - 1))
                       in certificates[p]['patterns'])
            counts[mask] += 1
    assert sum(counts.values()) == period ** 2
    assert counts[0] == 111696

    def coverage(prime_subset):
        ans = Fraction(0)
        for mask, count in counts.items():
            active = [p for i, p in enumerate(PRIMES)
                      if p in prime_subset and mask & (1 << i)]
            if active:
                # CRT independence of four singular linear congruences.
                q = prod(active)
                ans += Fraction(count * (q - 1), q)
        return ans / (period ** 2)

    assert coverage((11, 17)) == Fraction(564, 935)
    assert coverage((11, 17, 19)) == Fraction(34931, 53295)
    union = coverage(PRIMES)
    assert union == Fraction(421142, 550715)
    total_modulus = period * prod(PRIMES)
    assert total_modulus == 79302960
    certified = union * total_modulus ** 2
    assert certified.denominator == 1
    assert certified.numerator == 4809284233966080
    assert total_modulus ** 2 == 6288959464761600

    # Verify strict novelty against the predecessor's two-prime certificates.
    assert certificates[19]['valid'](1, 30)
    assert not certificates[11]['valid'](1, 30)
    assert not certificates[17]['valid'](1, 30)
    assert certificates[31]['valid'](7, 19)
    assert not any(certificates[p]['valid'](7, 19) for p in (11, 17, 19))
    assert gcd(1, 30) == gcd(7, 19) == 1

    for p, data in certificates.items():
        print('p=', p, 'u=', data['residue_u'], 'gamma=', data['residue_gamma'],
              'singular(z,a,L)=', data['singular'],
              'derivative(h,n)=', data['derivative'],
              'base_patterns=', len(data['patterns']),
              'certified_classes=', data['class_count'],
              'of', data['modulus'] ** 2)
    print('base-period=', period, 'mask-counts=', ','.join(str(counts[i]) for i in range(16)))
    print('four-prime-union=', union, 'approx=', format(float(union), '.12f'))
    print('CRT-module=', total_modulus, 'certified=', certified.numerator,
          'of', total_modulus ** 2)
    print('novel excluded fractions: 1/31 by p19, 7/26 by p31')
    print('ALL PASS')


if __name__ == '__main__':
    main()
