#!/usr/bin/env python3
"""D25 H40 exact arithmetic checker: two-port harmonic p^3 expansion.
No native H0/B0 execution, independent mathematical review or acceptance asserted.
"""
from fractions import Fraction
from math import comb


def primes_upto(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[0:2] = b'\x00\x00'
    for q in range(2, int(n**0.5) + 1):
        if sieve[q]:
            sieve[q*q::q] = b'\x00' * ((n-q*q)//q + 1)
    return [q for q in range(5, n+1) if sieve[q]]


def verify_one(p):
    assert p >= 5 and p % 6 in (1, 5)
    e = int(p % 6 == 5)
    m = (p - 1 - 4*e)//6
    mod = p**3
    inv2 = pow(2, -1, mod)
    inv36 = pow(36, -1, mod)
    # direct summand vs independent rational-alpha/beta base+harmony summand
    direct, base = 1, 1
    H = H2 = 0
    direct_ports = [0, 0]
    decomposed_ports = [0, 0]
    S, E, J = [0, 0], [0, 0], [0, 0]
    for k in range(m + 1):
        weights = (1, 1 - 6*e + 12*k)
        D = (H*H - H2) * inv2 % mod
        corrected = base * (1 - p*H + p*p*D) % mod
        for port in range(2):
            w = weights[port]
            direct_ports[port] = (direct_ports[port]+w*direct) % mod
            decomposed_ports[port] = (decomposed_ports[port]+w*corrected) % mod
            S[port] = (S[port]+w*base) % mod
            E[port] = (E[port]+w*base*H) % mod
            J[port] = (J[port]+w*base*D) % mod
        if k == m:
            break
        invk = pow(k+1, -1, mod)
        direct = direct * (m-k)*(2*m+e-k)*invk*invk*inv2 % mod
        a, b = 6*k+1+4*e, 3*k+1+e
        assert 0 < a < p and 0 < b < p
        ua, ub = pow(a, -1, mod), pow(b, -1, mod)
        H = (H+ua+ub) % mod
        H2 = (H2+ua*ua+ub*ub) % mod
        base = base*a*b*inv36*invk*invk % mod
    assert direct_ports == decomposed_ports, (p, direct_ports, decomposed_ports)
    for j in range(2):
        assert direct_ports[j] == (S[j]-p*E[j]+p*p*J[j]) % mod
    out = dict(p=p, e=e, m=m, A=direct_ports[0], B=direct_ports[1])
    for j, name in enumerate(('A', 'B')):
        if direct_ports[j] % (p*p) == 0:
            assert S[j] % p == 0
            carry = (S[j]//p - E[j]) % (p*p)
            assert carry % p == 0
            carry = carry//p
            out[name+'_carry'] = carry
            out[name+'_second_symmetric'] = J[j] % p
            out[name+'_third_digit'] = direct_ports[j]//(p*p)
            assert (carry+J[j]) % p == out[name+'_third_digit']
    return out


def exact_fraction_sanity():
    for p in (5, 7, 11, 13, 19, 23, 31, 41, 43):
        e = int(p % 6 == 5)
        m = (p-1-4*e)//6
        alpha, beta = Fraction(-(1+4*e), 6), Fraction(-(1+e),3)
        for k in range(m + 1):
            t = Fraction(1)
            prod = Fraction(1)
            for j in range(k):
                t *= (alpha-j)*(beta-j)/((j+1)**2*2)
                prod *= (1-Fraction(p,6*j+1+4*e))*(1-Fraction(p,3*j+1+e))
            assert t*prod == Fraction(comb(m,k)*comb(2*m+e,k), 2**k)


if __name__ == '__main__':
    exact_fraction_sanity()
    numbers = primes_upto(1000)
    assert len(numbers) == 166
    out = {p:verify_one(p) for p in numbers + [101419]}
    assert out[149]['B_carry'] == 13
    assert out[149]['B_second_symmetric'] == 5
    assert out[149]['B_third_digit'] == 18
    assert out[211]['A_carry'] == 22
    assert out[211]['A_second_symmetric'] == 152
    assert out[211]['A_third_digit'] == 174
    assert out[101419]['A_carry'] == 35425
    assert out[101419]['A_second_symmetric'] == 38207
    assert out[101419]['A_third_digit'] == 73632
    print('PASS exact rational products; 166 primes 5<=p<=1000; p=101419;')
    print('PASS both p^3 ports and three exceptional two-component third digits')
    for p in (149, 211, 101419):
        print(out[p])
