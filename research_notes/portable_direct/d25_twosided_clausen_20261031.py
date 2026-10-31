#!/usr/bin/env python3
"""D25 author-side exact arithmetic: two-sided finite Clausen square-cutoff identity.

Requires only Python standard library. This is a finite regression, not a
universal proof or a native same-original-class H0/B0 execution.
"""
from math import comb


def primes_upto(n):
    flags = bytearray(b'\x01') * (n + 1)
    flags[:2] = b'\x00\x00'
    for i in range(2, int(n ** .5) + 1):
        if flags[i]:
            flags[i*i:n+1:i] = b'\x00' * ((n-i*i)//i + 1)
    return [i for i in range(5, n + 1) if flags[i]]


def port_value(p):
    m = p**4
    # Rational coefficients in Z_(p). All denominators are p-units for k < p.
    alpha, beta, aa, bb = [1], [1], [1], [1]
    for k in range(p-1):
        inv2 = pow((k+1)**2, -1, m)
        inv3 = pow((k+1)**3, -1, m)
        alpha.append(alpha[-1] * (6*k+1)*(3*k+1)*pow(36, -1, m)*inv2 % m)
        beta.append(beta[-1] * (8*k+1)*(8*k+3)*pow(576, -1, m)*inv2 % m)
        aa.append(aa[-1] * (2*k+1)*(3*k+1)*(3*k+2)*pow(36,-1,m)*inv3 % m)
        bb.append(bb[-1] * (4*k+1)*(2*k+1)*(4*k+3)*pow(288,-1,m)*inv3 % m)
    # One-sided suffix sums preserve the triangular i+j>=p boundary and weights.
    sa, ia, sb, ib = [[0]*(p+1) for _ in range(4)]
    for j in range(p-1,-1,-1):
        sa[j]=(sa[j+1]+alpha[j])%m
        ia[j]=(ia[j+1]+j*alpha[j])%m
        sb[j]=(sb[j+1]+beta[j])%m
        ib[j]=(ib[j+1]+j*beta[j])%m
    ta=sum(alpha[i]*((6*i+1)*sa[p-i]+6*ia[p-i]) for i in range(1,p))%m
    tb=sum(beta[i]*((8*i+1)*sb[p-i]+8*ib[p-i]) for i in range(1,p))%m
    ga=sum(alpha)%m
    ha=sum((12*i+1)*alpha[i] for i in range(p))%m
    gb=sum(beta)%m
    hb=sum((16*i+1)*beta[i] for i in range(p))%m
    A=sum((6*i+1)*aa[i] for i in range(p))%m
    B=sum((8*i+1)*bb[i] for i in range(p))%m
    assert (ga*ha-ta-A)%m==0
    assert (gb*hb-tb-B)%m==0
    assert (A-2*B+p)%m==0 if p%24 in (13,19) else True  # finite conjecture test
    assert ta%p**2 == 0 if p%6==1 else True
    assert tb%p**2 == 0 if p%24 ==19 else True
    # Independent integer-binomial input for representative cases.
    if p in (13,19,37,43,67,373):
        x=sum((6*k+1)*comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,m)
              for k in range(p)) % m
        y=sum((8*k+1)*comb(4*k,2*k)*comb(2*k,k)**2*pow(2304,-k,m)
              for k in range(p)) % m
        assert x==A and y==B
    return dict(p=p, A=A,B=B, GaHa=ga*ha%m,GbHb=gb*hb%m,TA=ta,TB=tb,
                TA_p2=ta%p**2, TB_p2=tb%p**2,
                GB_p2=gb%p**2)


def main():
    arr=[port_value(p) for p in primes_upto(1200) if p%24 in (13,19)]
    assert len(arr)==sum(1 for p in primes_upto(1200) if p%24 in (13,19))
    for x in arr:
        p=x['p']
        if p%24 == 13:
            # The tail has a unit-valued individual source, not a global p^2 bound.
            low=(5*p-1)//8
            assert 2*low>=p and (16*low+1)%p !=0
        else:
            # Both coefficient valuations <=1 force i+j<p; hence tail v_p>=2.
            hi=(3*p-1)//8
            assert 2*hi<p
    print('PASS two-sided exact Clausen mod p^4, class-wise tail bounds,',len(arr),'target primes <=1200')
    for x in arr:
        if x['p'] in (13,19,37,43,67,373):
            print(x)

if __name__=='__main__':
    main()
