#!/usr/bin/env python3
"""Exact author-side D25 Gauss/Clausen spectral bridge checks.

All calculations are rational or in Z/(p**3); no floating point and no
native Enterprise Math execution/claim is implied.
"""
from fractions import Fraction as Q
from math import factorial, isqrt

L_A, L_B = Q(1, 18), Q(3, 64)
D = L_A - L_B
assert D == Q(5, 576)


def gauss_coefficients(a, b, count):
    out = [Q(1)]
    for k in range(count - 1):
        out.append(out[-1] * (Q(k) + a) * (Q(k) + b) / (k + 1)**2)
    return out


def hyper3_coefficients(lam, count):
    out = [Q(1)]
    for k in range(count - 1):
        out.append(out[-1] * (Q(k) + Q(1,2))
                   * (Q(k)**2 + Q(k) + 4*lam) / (k + 1)**3)
    return out


def exact_series_checks(count=24):
    f = gauss_coefficients(Q(1, 6), Q(1, 3), count)
    g = gauss_coefficients(Q(1, 8), Q(3, 8), count)
    ca, cb = hyper3_coefficients(L_A, count), hyper3_coefficients(L_B, count)
    for n in range(count):
        assert sum(f[k]*f[n-k] for k in range(n+1)) == ca[n]
        assert sum(g[k]*g[n-k] for k in range(n+1)) == cb[n]
        assert ca[n] * Q(1, 2**n) == Q(factorial(2*n)*factorial(3*n), 216**n*factorial(n)**5)
        assert cb[n] * Q(1, 9**n) == Q(factorial(4*n), 2304**n*factorial(n)**4)
    # W=f'g-fg'; coefficient at z^n is sum_(i+j=n+1)(i-j)f_i*g_j.
    w = [sum(Q(i-j)*f[i]*g[j] for i in range(n+2)
             for j in [n+1-i]) for n in range(count-1)]
    prod = [sum(f[i]*g[n-i] for i in range(n+1)) for n in range(count-1)]
    for n in range(count-1):
        # Exact first-order Lagrange identity:
        # z(1-z)W'+(1-3z/2)W=(L_A-L_B)fg.
        lhs = (n+1)*w[n] - (Q(n)+Q(1,2))*(w[n-1] if n else Q(0))
        assert lhs == D*prod[n]
    assert w[0] == D
    # H_B(A_N)=4 D z(theta+1/2) A_N - boundary_A z^(N+1)
    for lam, alt, cc in ((L_A,L_B,ca),(L_B,L_A,cb)):
        for k in range(1,count):
            coeff = k**3 * cc[k] - (Q(k)-Q(1,2)) * (Q(k-1)**2+Q(k-1)+4*alt)*cc[k-1]
            source = 4*(lam-alt)*(Q(k)-Q(1,2))*cc[k-1]
            assert coeff == source
    print('EXACT_RATIONAL: 24 Clausen/square coefficients per family, 23 Wronskian coefficients, spectral forcing PASS')



def aligned_wronskian_check(count=22):
    """Same observation variable: F(z), G(z)=_2F1(1/8,3/8;1;(2/9)z)."""
    cc=Q(2,9)
    fa=gauss_coefficients(Q(1,6),Q(1,3),count)
    gg=gauss_coefficients(Q(1,8),Q(3,8),count)
    gb=[gg[k]*cc**k for k in range(count)]
    fg=[sum(fa[i]*gb[n-i] for i in range(n+1)) for n in range(count)]
    ww=[sum(Q(i-j)*fa[i]*gb[j] for i in range(n+2)
            for j in [n+1-i]) for n in range(count-1)]
    for n in range(count-2):
        prev = ww[n-1] if n else Q(0)
        prev2 = ww[n-2] if n>1 else Q(0)
        # z(1-z)(1-cz) W' : z -(1+c)z^2+c z^3
        term = n*ww[n]-(1+cc)*(n-1)*prev+(cc*(n-2)*prev2 if n>=2 else 0)
        # (1-5(1+c)z/4+3cz^2/2)*W
        term += ww[n]-Q(5,4)*(1+cc)*prev+Q(3,2)*cc*prev2
        # -(1-c)z/4*(fg)'
        term -= Q(1,4)*(1-cc)*n*fg[n]
        right=(L_A-cc*L_B)*fg[n]+cc*(L_B-L_A)*(fg[n-1] if n else 0)
        assert term==right,(n,term,right)
    print('ALIGNED_WRONSKIAN: 20 exact rational coefficients at common z (216 z=1/2, 2304 (2/9)z=1/9) PASS')


def primes_below(bound):
    s = bytearray(b'\x01')*bound
    s[:2] = b'\x00\x00'
    for d in range(2,isqrt(bound-1)+1):
        if s[d]:
            s[d*d::d] = b'\x00'*len(s[d*d::d])
    return [p for p in range(5,bound) if s[p]]


def modular_check(p):
    mod = p**3
    half = pow(2,-1,mod)
    a_inv = pow(9,-1,mod)
    b_inv = pow(16,-1,mod)
    # c_n for both original full 3F2 series, n <= p-1.
    ca = cb = 1
    for n in range(p-1):
        denom_inv = pow(n+1,-3,mod)
        na = (n+half)*((n*n+n)+2*a_inv)%mod
        nb = (n+half)*((n*n+n)+3*b_inv)%mod
        next_a = ca*na*denom_inv%mod
        next_b = cb*nb*denom_inv%mod
        # Compare the source-labelled cross-operator forcing at z^(n+1).
        # H_B A coefficient - 4(L_A-L_B)(n+1/2)c_n must vanish.
        delta = 5*pow(144,-1,mod)%mod
        hb_a = (n+1)**3*next_a - (n+half)*(n*n+n+3*b_inv)*ca
        ha_b = (n+1)**3*next_b - (n+half)*(n*n+n+2*a_inv)*cb
        assert (hb_a-delta*(n+half)*ca)%mod == 0, (p,n,'A')
        assert (ha_b+delta*(n+half)*cb)%mod == 0, (p,n,'B')
        ca,cb=next_a,next_b
    # Truncation boundary for the operator at n=p-1 is a p^3 multiple.
    assert ca==0 and cb==0, (p,ca,cb)
    return ca,cb



def gauss_mod_coefficients(p, a_num, a_den, b_num, b_den):
    """Native labelled Gauss coefficients for indices 0..p-1, mod p**3."""
    mod=p**3
    inv_denom=pow(a_den*b_den,-1,mod)
    coeffs=[1]
    for n in range(p-1):
        weight=((a_den*n+a_num)*(b_den*n+b_num)*inv_denom)%mod
        coeffs.append(coeffs[-1]*weight*pow(n+1,-2,mod)%mod)
    return coeffs


def valuation_mod_p3(x,p):
    if x%p: return 0
    if x%(p*p):return 1
    if x%(p*p*p):return 2
    return 3


def exact_carry_ports_check(p):
    """Check sharp port valuation thresholds with actual p^3 coefficients."""
    if p%6!=1:
        return
    aa=gauss_mod_coefficients(p,1,6,1,3)
    m=(p-1)//6
    va=[0 if k<=m else 1 if k<=2*m else 2 for k in range(p)]
    assert all(valuation_mod_p3(a,p)==v for a,v in zip(aa,va))
    assert valuation_mod_p3(aa[1]*aa[p-1]%(p**3),p)==2
    # Only p=13 or 19 mod 24 are targeted by the mother objective.
    if p%24 not in (13,19):return
    bb=gauss_mod_coefficients(p,1,8,3,8)
    if p%24==19:
        q=(p-3)//8
        first,second=q,(3*p-1)//8
        vb=[0 if k<=first else 1 if k<=second else 2 for k in range(p)]
        assert all(valuation_mod_p3(a,p)==v for a,v in zip(bb,vb))
        assert valuation_mod_p3(bb[1]*bb[p-1]%(p**3),p)==2
        assert 2*second<p
    else:
        first,second=(5*p-1)//8,(7*p-3)//8
        vb=[0 if k<=first else 1 if k<=second else 2 for k in range(p)]
        assert all(valuation_mod_p3(a,p)==v for a,v in zip(bb,vb))
        mid=(p+1)//2
        assert mid<=first and bb[mid]%p!=0
        # A witness PORT, not a universal noncancellation claim for its aggregate.
        assert valuation_mod_p3(bb[mid]*bb[mid]%(p**3),p)==0
    if p in (13,19,37,43,109,373):
        n=p+1; c=sum(bb[i]*bb[n-i] for i in range(2,p)
                         if 0<=n-i<p)%(p**3)
        print('LABELLED_CARRY',p,'class_mod24',p%24,
              'min_B_port_valuation',0 if p%24==13 else 2,
              'actual_B_carry_coefficient_at_z^(p+1)_mod_p',c%p)

def main():
    exact_series_checks()
    aligned_wronskian_check()
    pp=primes_below(1000)
    for p in pp:modular_check(p)
    print(f'MODULAR: {len(pp)}/{len(pp)} primes 5<=p<1000, both p^3 spectral identities and vanishing top boundaries PASS')
    for p in pp: exact_carry_ports_check(p)
    print('BRC_PORTS: sharp 216 and 2304 carry valuations on all p=1 mod6 below 1000, target classes checked PASS')
    print('MATHEMATICAL_STATUS: exact rational derivation / finite independent checks; author-side, unreviewed, not admitted')

if __name__ == '__main__': main()
