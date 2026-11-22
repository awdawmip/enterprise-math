#!/usr/bin/env python3
"""Exact finite-field dual-number witnesses for order-43 first jets of frozen R5.
No floating point; cone formula preserves the three overlapping failure events.
Only m=37..43 is asserted as a characteristic-zero nonvanishing theorem.
"""
from itertools import permutations, product

SUPPORTS = (
    (214, 215, 216, 217, 218),
    (214, 216, 217, 218, 219, 220, 221),
    (215, 216, 217, 218, 219, 220, 221),
)
PRIMES_AND_ROOTS = ((1033, 995), (1291, 341), (1549, 104), (1721, 1393))
MAX_M = 43


def check(p, z):
    assert z != 1 and pow(z, 43, p) == 1
    assert all(p % x for x in range(2, int(p**0.5) + 1))
    zero, one = (0, 0), (1, 0)

    def add(x, y):
        return ((x[0] + y[0]) % p, (x[1] + y[1]) % p)

    def neg(x):
        return (-x[0] % p, -x[1] % p)

    def sub(x, y):
        return add(x, neg(y))

    def mul(x, y):
        return (x[0] * y[0] % p, (x[0] * y[1] + x[1] * y[0]) % p)

    def inv(x):
        u = pow(x[0], -1, p)
        return (u, -x[1] * u * u % p)

    def qpow(exponent):
        v = pow(z, exponent % 43, p)
        return (v, exponent * v % p)

    def dprod(prices):
        result = one
        for price in prices:
            result = mul(result, sub(one, qpow(price)))
        return result

    def inv_t_factor(seq, c, power):
        out = seq.copy()
        for k in range(power, MAX_M):
            out[k] = add(out[k], mul(c, out[k - power]))
        return out

    def single_block(prices):
        # [t^(m-1)] D_S(q)/((1-t)*prod_(a in S)(1-q^a*t))
        seq = [zero] * MAX_M
        seq[0] = dprod(prices)
        seq = inv_t_factor(seq, one, 1)
        for price in prices:
            seq = inv_t_factor(seq, qpow(price), 1)
        return seq

    def three_event_union():
        # Exact six-cone decomposition of min(s0,s1,s2) with strict tie-breaks.
        total = [zero] * MAX_M
        for r in (219, 220, 221):
            beta = one
            for other in (219, 220, 221):
                if other != r:
                    beta = mul(beta, inv(sub(one, qpow(other - r))))
            for a, b, c in permutations((214, 215, r)):
                delta1, delta2 = int(a > b), int(b > c)
                coefficient = beta
                # Cancel the (1-q^a) cone denominator algebraically,
                # before specializing q to the order-43 root (215 is 43*5).
                for price in range(214, 222):
                    if price != a:
                        coefficient = mul(coefficient, sub(one, qpow(price)))
                if delta1:
                    coefficient = mul(coefficient, qpow(a))
                if delta2:
                    coefficient = mul(coefficient, qpow(a + b))
                seq = [zero] * MAX_M
                seq[delta2] = coefficient
                seq = inv_t_factor(seq, one, 1)
                for price in (216, 217, 218):
                    seq = inv_t_factor(seq, qpow(price), 1)
                seq = inv_t_factor(seq, qpow(a + b), 1)
                seq = inv_t_factor(seq, qpow(a + b + c), 2)
                total = [add(x, y) for x, y in zip(total, seq)]
        return total

    def direct_three_event_union(m):
        # Independent literal joint-event inclusion/exclusion check for m<=3.
        result = zero
        for mask in range(1, 8):
            selected = tuple(i for i in range(3) if mask & (1 << i))
            union = sorted(set().union(*(SUPPORTS[i] for i in selected)))
            h = zero
            for multiplicities in product(range(m), repeat=len(union)):
                if all(sum(n for price, n in zip(union, multiplicities)
                           if price in SUPPORTS[i]) < m for i in selected):
                    h = add(h, qpow(sum(price * n for price, n
                                         in zip(union, multiplicities))))
            term = mul(h, dprod(union))
            result = add(result, term if len(selected) % 2 else neg(term))
        return result

    a = three_event_union()
    b = single_block(range(223, 291))
    c = single_block(range(296, 313))
    for m in (1, 2, 3):
        assert a[m - 1] == direct_three_event_union(m), (p, m, 'overlap')
    out = []
    for m in range(37, 44):
        x, y, w = a[m - 1], b[m - 1], c[m - 1]
        # R=1-(1-A)(1-B)(1-C) for fixed m, not a t-convolution.
        r = sub(one, mul(mul(sub(one, x), sub(one, y)), sub(one, w)))
        assert r[0] == 0 and r[1] != 0, (p, m, r)
        assert y[0] == 0 and w[0] == 0
        out.append((m, r[0], r[1]))
    assert c[36][1] == (-43 * 301) % p  # analytic S4 plateau check
    return out


def main():
    print('prime,primitive_root,m,R_at_root,Euler_first_jet')
    for p, z in PRIMES_AND_ROOTS:
        for m, value, jet in check(p, z):
            print(f'{p},{z},{m},{value},{jet}')
    print('ALL CHECKS PASS: 28/28 first jets nonzero; literal overlap m=1,2,3 checked at four primes')


if __name__ == '__main__':
    main()
