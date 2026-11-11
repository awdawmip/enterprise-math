#!/usr/bin/env python3
"""Finite exact regression for D25 PF W2 reflection (proof is in research_returns/...)."""
from math import comb, factorial, isqrt


def primes_below(limit):
    for p in range(5, limit):
        if all(p % j for j in range(2, isqrt(p) + 1)):
            yield p


def mul(x, y, q):
    return ((x[0] * y[0] + 2 * x[1] * y[1]) % q,
            (x[0] * y[1] + x[1] * y[0]) % q)


def eval_at_quadratic(cs, u, q):
    v = (0, 0)
    for c in reversed(cs):
        v = mul(v, u, q)
        v = ((v[0] + c) % q, v[1])
    return v


def check_prime(p):
    assert p % 3 == 1 and p >= 7
    n = (p - 1) // 3
    m = 2 * n
    q = p * p
    cs = [1]
    for k in range(m):
        cs.append(cs[-1] * (3 * k + 1) * (3 * k + 2)
                  * pow(9 * (k + 1) * (k + 1), -1, q) % q)
    # The PF operator has zero coefficients in degrees 0,..,m.
    for k in range(m):
        defect = ((k + 1) * (k + 1) * cs[k + 1]
                  - (3 * k + 1) * (3 * k + 2) * pow(9, -1, q) * cs[k]) % q
        assert defect == 0, ('PF recurrence', p, k, defect)
    assert ((3 * m + 1) * (3 * m + 2) * cs[m]) % q == 0
    # Exact polynomial identity P(1-u)=P(u) in (Z/p²)[u].
    for j in range(m + 1):
        reflected = (-1) ** j * sum(cs[k] * comb(k, j) for k in range(j, m + 1)) % q
        assert reflected == cs[j], ('reflection', p, j)
    assert sum(cs) % q == 1, ('endpoint', p)
    assert all(c % p == 0 for c in cs[n + 1:])
    inv4 = pow(4, -1, q)
    u = (2 * inv4 % q, -inv4 % q)  # (2-T)/4, T²=2
    an = eval_at_quadratic(cs[:n + 1], u, q)
    p2 = eval_at_quadratic(cs, u, q)
    assert p2[1] == 0, ('quadratic port', p, p2)
    if p % 24 in (13, 19):
        # A numerical regression of frozen supersingular input, not its proof.
        assert an[0] % p == 0 and an[1] % p == 0, (p, an)
        assert p2[0] % p == 0, (p, p2)
    return an, p2


def independently_eval_factorial(p, cutoff):
    q = p * p
    inv4 = pow(4, -1, q)
    u = (2 * inv4 % q, -inv4 % q)
    cs = [factorial(3 * k) * pow(27 ** k * factorial(k) ** 3, -1, q) % q
          for k in range(cutoff + 1)]
    return eval_at_quadratic(cs, u, q)


def main():
    tested = {}
    for p in primes_below(500):
        if p % 3 == 1:
            tested[p] = check_prime(p)
    n373 = (373 - 1) // 3
    a, t = tested[373]
    assert a == (112646, 57442)
    assert t == (8952, 0)
    assert independently_eval_factorial(373, n373) == a
    assert independently_eval_factorial(373, 2 * n373) == t
    target = [p for p in tested if p % 24 in (13, 19)]
    print('PASS: polynomial PF mod p² and reflection,', len(tested), 'primes p<500 with p≡1 (mod3)')
    print('PASS: quadratic CM port parity and supersingular residue,', len(target), 'target primes p<500')
    print('PASS: p=373 A_n/p = (302,154), P_2n/p = (24,0); independent factorial witness')


if __name__ == '__main__':
    main()
