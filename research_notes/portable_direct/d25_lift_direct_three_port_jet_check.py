#!/usr/bin/env python3
"""Author exact p-adic LIFT observer test; original recurrence versus three root-factor jet ports.

python d25_lift_direct_three_port_jet_check.py [max_p=2000]
This is not a Source-native benchmark, admission or theorem proof.
"""
from __future__ import annotations
import sys

def primes_up_to(limit: int) -> list[int]:
    flags = bytearray(b'\x01') * (limit + 1)
    flags[:2] = b'\x00\x00'
    for d in range(2, int(limit ** 0.5) + 1):
        if flags[d]:
            flags[d*d::d] = b'\x00' * ((limit - d*d)//d+1)
    return [p for p in range(2, limit + 1) if flags[p] and p % 24 in (13, 19)]

def inverse(a: int, mod: int) -> int:
    return pow(a % mod, -1, mod)

def certificate(p: int) -> dict[str, int]:
    assert p > 3 and p % 24 in (13, 19)
    m = (p-1)//6
    mod = p**3
    p2 = p*p
    inv2, inv3, inv6 = (inverse(v,mod) for v in (2,3,6))
    inv36, inv9 = inverse(36,mod), inverse(9,mod)

    # Original frozen B ratio, including the p-valuation of every term.
    exact_b = 1
    source_g = source_h = source_low = source_mid = source_high = 0
    valuations = [0,0,0]
    for k in range(p):
        source_g = (source_g + exact_b) % mod
        source_h = (source_h + (12*k+1)*exact_b) % mod
        if k <= m:
            source_low = (source_low + exact_b)%mod
            assert exact_b%p != 0
            valuations[0] += 1
        elif k <= 2*m:
            source_mid = (source_mid + exact_b)%mod
            assert exact_b%p == 0 and exact_b%p2 != 0
            valuations[1] += 1
        else:
            source_high = (source_high + exact_b)%mod
            assert exact_b%p2 == 0
            valuations[2] += 1
        if k+1 < p:
            exact_b = (exact_b*(6*k+1)*(3*k+1)*inverse(36*(k+1)**2,mod))%mod
    assert valuations == [m+1,m,4*m]
    assert source_g%p == 0
    source_G = source_g//p
    assert (source_G*source_h-1)%p == 0, ('UR', p)
    source_delta = ((source_G*source_h-1)%p2)//p

    # 0..m: base terminating polynomial plus 1st and 2nd parameter jets.
    b = 1
    D = E = 0
    L0 = L1 = L2 = H0 = H1 = 0
    for k in range(m+1):
        w = 12*k+1
        L0 = (L0 + b)%mod
        L1 = (L1 + b*D)%mod
        L2 = (L2 + b*((D*D-E)%mod)*inv2)%mod
        H0 = (H0+w*b)%mod
        H1 = (H1+w*b*D)%mod
        if k == m:
            break
        d1 = inverse(k-m,mod)
        d2 = inverse(k-2*m,mod)
        D = (D + inv6*d1 + inv3*d2)%mod
        E = (E + inv36*d1*d1 + inv9*d2*d2)%mod
        b = (b*(k-m)*(k-2*m)*inverse(2*(k+1)**2,mod))%mod
    assert L0%p == 0, ('CM0', p)
    L0_over_p = (L0//p)%p2

    # m+1..2m: one exact zero factor, one derivative jet.
    u = (b*(-m)*inverse(12*(m+1)**2,mod))%mod
    P = (D-inverse(3*m,mod))%mod
    M1 = M2 = J1 = 0
    for k in range(m+1,2*m+1):
        M1 = (M1 + u)%mod
        M2 = (M2 + u*P)%mod
        J1 = (J1 + (12*k+1)*u)%mod
        if k == 2*m:
            break
        d1, d2 = inverse(k-m,mod), inverse(k-2*m,mod)
        P = (P+inv6*d1+inv3*d2)%mod
        u = (u*(k-m)*(k-2*m)*inverse(2*(k+1)**2,mod))%mod

    # 2m+1..p-1: two exact zero factors, zeroth jet only.
    v = (u*m*inverse(6*(2*m+1)**2,mod))%mod
    V2 = 0
    for k in range(2*m+1,p):
        V2 = (V2 + v)%mod
        if k+1 == p:
            break
        v = (v*(k-m)*(k-2*m)*inverse(2*(k+1)**2,mod))%mod

    gamma0 = (L0_over_p+L1+M1)%p2
    gamma1 = (L2+M2+V2)%p2
    Hjet1 = (H1+J1)%p2
    predicted_G = (gamma0 + p*gamma1)%p2
    predicted_h = (H0+p*Hjet1)%p2
    assert predicted_G == source_G%p2
    assert predicted_h == source_h%p2
    assert (gamma0*H0-1)%p == 0

    delta_components = (
        (((gamma0*H0-1)%p2)//p)%p,
        ((L2+M2)*H0)%p,
        (V2*H0)%p,
        (gamma0*Hjet1)%p,
    )
    delta_pred = sum(delta_components)%p
    assert source_delta == delta_pred
    assert source_low == (L0+p*L1+p*p*L2)%mod
    assert source_mid == (p*M1+p*p*M2)%mod
    assert source_high == (p*p*V2)%mod
    return {
        'p':p,'m':m,'G_mod_p2':source_G%p2,'h_mod_p2':source_h%p2,
        'Delta_p':delta_pred,'base_digit':delta_components[0],
        'low_mid_second_jet':delta_components[1],
        'upper_double_zero':delta_components[2],
        'h_first_jet':delta_components[3],
    }

def main(max_p: int) -> None:
    ps = primes_up_to(max_p)
    upper_nonzero = 0
    for p in ps:
        r = certificate(p)
        if r['upper_double_zero']:
            upper_nonzero += 1
        if p in (13,19,37,43,67,139,211,499,997):
            print(r)
    print(f'PASS {len(ps)}/{len(ps)} target primes <= {max_p}; nonzero upper port {upper_nonzero}; exact original B and three-port jet agree at required precision.')

if __name__ == '__main__':
    main(int(sys.argv[1]) if len(sys.argv)>1 else 2000)
