#!/usr/bin/env python3
"""Exact original D25 frozen R / Clausen boundary source-port alignment.

Author-side auxiliary rational arithmetic; no native H0/B0 runner.
"""
from math import comb

TARGET_PRIMES = (13, 19, 37, 43, 61, 67, 211, 373)
CONTROL_PRIMES = (7, 31, 73)


def check_prime(p: int, target: bool) -> dict:
    assert p > 3 and p % 6 == 1
    m = (p - 1) // 6
    q = p ** 3
    t = [1]
    for k in range(p - 1):
        t.append(t[-1] * (6*k + 1)*(3*k + 1) * pow(36*(k+1)**2, -1, q) % q)
    assert all((t[k] % p == 0) == (k > m) for k in range(2*m+1))
    assert all(t[k] % (p*p) == 0 for k in range(2*m+1, p))

    d = sum(t[:2*m+1]) % q
    e = sum(k*t[k] for k in range(2*m+1)) % q
    j = sum(k*t[k] for k in range(m+1)) % q
    c_raw = sum(t[2*m+1:]) % q
    assert (e-j) % p == 0
    assert c_raw % (p*p) == 0
    c = (c_raw // (p*p)) % p
    h_raw = sum(
        t[k] * sum((6*(k+i)+1) * t[i] for i in range(p-k, m+1))
        for k in range(5*m+1, p)
    ) % q
    assert h_raw % (p*p) == 0
    h = h_raw // (p*p) % p

    # Source-frozen R_p, independent of the current five-observer H definition.
    v = [0, pow(10, -1, p)]
    for a in range(1, m):
        v.append(v[-1] * 36*a*a * pow((6*a+5)*(3*a+2), -1, p) % p)
    r_source = 2 * sum(
        (t[i] % p) * sum((1+6*(i-a))*v[a] for a in range(1,i+1))
        for i in range(1,m+1)
    ) % p
    assert all(t[p-a] // (p*p) % p == v[a] for a in range(1,m+1)), p

    # Directly enumerate original signed degree-cutoff pairs i+k >= p.
    cutoff = sum(
        (6*(i+k)+1) * t[i] * t[k]
        for i in range(p) for k in range(max(0,p-i), p)
    ) % q
    assert cutoff % (p*p) == 0
    assert cutoff == 2*h_raw % q, (p, cutoff, h_raw)
    assert cutoff // (p*p) % p == r_source == 2*h % p

    # Original weighted 216 sum is independently evaluated via integer binomials.
    weighted = sum(
        (6*n+1)*comb(2*n,n)**2*comb(3*n,n)*pow(216,-n,q)
        for n in range(p)
    ) % q
    M = sum(t) % q
    N = sum(k*t[k] for k in range(p)) % q
    assert weighted == (M*(M+12*N)-cutoff) % q

    row = dict(p=p, frozen_R=r_source, boundary_h=h,
               checked_source_alignment=True, full_weighted=weighted)
    if target:
        assert p % 24 in (13,19)
        assert d % p == 0 and M % p == 0
        r = d // p % (p*p)
        e2 = e % (p*p)
        assert 12*r*e2 % p == 1
        delta = ((M // p) * ((M+12*N)%q) - 1) // p % p
        direct_obstruction = ((weighted-p)//(p*p)) % p
        four_port_delta = ((12*r*e2-1)//p + r*r + 12*e2*c) % p
        four_port_residue = (four_port_delta-r_source) % p
        assert delta == four_port_delta
        assert four_port_residue == direct_obstruction
        row.update(r=r,e=e2,c=c,delta=delta,obstruction=four_port_residue,
                   c_term=(12*e2*c)%p, signed_R_term=(-r_source)%p)
        if p == 373:
            assert (r,e2,c,h,r_source,delta,weighted) == (110805,108837,252,98,196,196,373)
            assert row['c_term'] == 197
    else:
        assert p % 24 in (1,7)
    return row


if __name__ == '__main__':
    for p in TARGET_PRIMES:
        print('TARGET', check_prime(p, True))
    for p in CONTROL_PRIMES:
        print('CONTROL', check_prime(p, False))
    print('PASS_D25_SOURCE_ALIGNED_FOUR_PORT_GAUSS_CLAUSEN')
