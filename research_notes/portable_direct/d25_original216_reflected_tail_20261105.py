#!/usr/bin/env python3
"""Independent exact check of reflected endpoint and constant-space tail digit.
Only original 216 Clausen coefficients. Author-side portable; not reviewed.
"""
from math import isqrt

def is_prime(p):
    return p > 1 and all(p % d for d in range(2, isqrt(p) + 1))

def verify(p):
    assert p >= 7 and p % 6 == 1 and is_prime(p)
    m, mod = (p - 1) // 6, p**3
    b = [1]
    for k in range(p - 1):
        b.append(b[-1] * (6*k + 1)*(3*k + 1)
                 * pow(36*(k+1)**2, -1, mod) % mod)
    assert b[-1] % (p*p) == 0
    c_last = (b[-1] // (p*p)) % p
    assert c_last == pow(10, -1, p), (p, c_last)

    d = pow(10, -1, p)
    A = B = tail_unit = 0
    for i in range(1, m + 1):
        if i > 1:
            r = i - 1
            d = d * (36*r*r) * pow((6*r+5)*(3*r+2), -1, p) % p
        assert b[p-i] % (p*p) == 0
        direct_unit = (b[p-i] // (p*p)) % p
        assert d == direct_unit, (p, i, d, direct_unit)
        A, B = (A+d) % p, (B+i*d) % p
        tail_unit = (tail_unit + 2*(b[i] % p)*((6*i+1)*A - 6*B)) % p

    tail_direct = 0
    for i, a in enumerate(b):
        for j in range(p-i, p):
            tail_direct = (tail_direct + (6*(i+j)+1)*a*b[j]) % mod
    assert tail_direct % (p*p) == 0
    assert tail_unit == tail_direct // (p*p) % p, (p, tail_unit, tail_direct)
    return (p,m,c_last,tail_unit,tail_direct)

if __name__ == '__main__':
    out = [verify(p) for p in range(7,374) if p%6==1 and is_prime(p)]
    for row in out:
        if row[0] in [7,13,19,37,61,373]: print(row)
    print('PASS',len(out),'primes: endpoint=1/10, reflected coefficient, fused digit=direct double sum')
