#!/usr/bin/env python3
"""GH-3: exact linear-time S-Gauss middle-port residue certificate.

This checks finite samples, not an all-prime separate-port vanishing theorem.
It never performs native Hasse / H0-B0 / Frobenius experiments.
"""
from math import isqrt


def primes_3mod8(bound):
    sieve = bytearray(b"\x01") * (bound + 1)
    sieve[:2] = b"\x00\x00"
    for d in range(2, isqrt(bound) + 1):
        if sieve[d]:
            sieve[d*d:bound+1:d] = b"\x00" * ((bound-d*d)//d + 1)
    return [p for p in range(11, bound + 1, 8) if sieve[p]]


def normalized_beta(p):
    """q_t = (u_{a+1+t}/p)/(u_{a+1}/p), 0<=t<=2a, mod p."""
    assert p > 3 and p % 8 == 3
    a = (p - 3) // 8
    n = 2 * a
    inv = [0] * (3*a + 3)
    inv[1] = 1
    for j in range(2, len(inv)):
        inv[j] = p - (p // j) * inv[p % j] % p
    inv9 = pow(9, -1, p)
    q = [1] * (n + 1)
    for t in range(n):
        unit = inv[a+t+2]
        q[t+1] = -q[t] * (n-t) * (t+1) * inv9 * unit * unit % p
    return q


def triangular_certificate(q, p):
    """Exactly compute T_p = sum_{t+u>=n}(8(t+u)+11) q_t q_u."""
    n = len(q) - 1
    tail0 = [0] * (n + 2)
    tail1 = [0] * (n + 2)
    for j in range(n, -1, -1):
        tail0[j] = (tail0[j+1] + q[j]) % p
        tail1[j] = (tail1[j+1] + j*q[j]) % p
    return sum(q[t] * ((8*t+11)*tail0[n-t] + 8*tail1[n-t])
               for t in range(n+1)) % p


def direct_source_check(p, q, fast_result):
    """Independent source-unit recurrence plus O(p^2) triangular readback."""
    a = (p - 3) // 8
    b = (3*p - 1) // 8
    h = (p - 1) // 2
    unit = 1
    val = 0
    betas = []
    for k in range(b+1):
        if k >= a+1:
            assert val == 1
            betas.append(unit)
        if k == b:
            break
        numerator = (8*k+1)*(8*k+3)
        while numerator % p == 0:
            numerator //= p
            val += 1
        unit = unit*numerator*pow(576*(k+1)**2, -1, p) % p
    assert len(betas) == 2*a+1
    assert all(betas[t] == betas[0]*q[t] % p for t in range(len(q)))
    original = sum((8*(i+j)+1)*betas[i-a-1]*betas[j-a-1]
                   for i in range(a+1,b+1) for j in range(a+1,b+1)
                   if i+j > h) % p
    assert original == fast_result * betas[0]**2 % p
    return original


def check():
    checked = primes_3mod8(100000)
    sample = {}
    for p in checked:
        q = normalized_beta(p)
        value = triangular_certificate(q, p)
        assert value == 0, (p, value)
        if p <= 2000:
            direct_source_check(p, q, value)
        if p in (11, 19, 43, 59, 67, 139, 163):
            n = len(q)-1
            zeroth = sum(q[t]*q[u] for t in range(n+1)
                         for u in range(n+1) if t+u >= n) % p
            first = sum((t+u)*q[t]*q[u] for t in range(n+1)
                        for u in range(n+1) if t+u >= n) % p
            sample[p] = (zeroth, first, value)
            assert (11*zeroth+8*first) % p == 0
    eleven_class = sum(p % 24 == 11 for p in checked)
    nineteen_class = sum(p % 24 == 19 for p in checked)
    assert (len(checked), eleven_class, nineteen_class) == (2408,1203,1205)
    assert sample[11] == (5, 0, 0)
    assert sample[19] == (13, 13, 0)
    assert sample[43] == (29, 30, 0)
    print('PASS GH3: exact prime sieve and normalized O(p) triangular residues')
    print('p<=100000, p==3(mod 8):',len(checked),
          '11-class:',eleven_class,'19-class:',nineteen_class)
    print('O(p^2) original source-unit cross-check for every p<=2000')
    for p in sample:
        print('CERT',p,'(F0,F1,T)=',sample[p])
    print('THEOREM STATUS: triangular equivalence proved; universal separate vanishing open')


if __name__ == '__main__':
    check()
