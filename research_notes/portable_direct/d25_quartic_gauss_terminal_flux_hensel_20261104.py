#!/usr/bin/env python3
"""Exact finite certificate for quartic Gauss endpoint flux and Hensel slopes.

Original coefficients: v[k]=(1/8)_k(3/8)_k / ((k!)**2 * 9**k).
No platform-native crystalline computation or mathematical admission is claimed.
"""
from math import isqrt
from fractions import Fraction


def primes(limit):
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[:2] = b'\x00\x00'
    for n in range(2, isqrt(limit) + 1):
        if sieve[n]:
            sieve[n*n:limit+1:n] = b'\x00' * ((limit - n*n)//n + 1)
    return [n for n in range(5, limit+1) if sieve[n]]


def exact_rational_coefficient(n):
    v=Fraction(1)
    for k in range(n):
        v *= Fraction((8*k+1)*(8*k+3), 576*(k+1)**2)
    return v


def check(p):
    mod = p**3
    v = 1
    S=D=D2=Yd=0
    v_end=None
    coefficients=[]
    for k in range(p):
        coefficients.append(v)
        S=(S+v)%mod
        D=(D+k*v)%mod
        D2=(D2+k*k*v)%mod
        Yd=(Yd+k*(1+16*k)*v)%mod
        if k == p-1:
            v_end=v
        else:
            v = v*(8*k+1)*(8*k+3)*pow(576*(k+1)**2,-1,mod)%mod
    Y=(S+16*D)%mod
    eps = 3 if p%8 in (1,3) else 35
    endpoint = - (8*p-7)*(8*p-5)*v_end % mod
    assert endpoint == -eps*p*p %mod, ('third-digit endpoint',p,endpoint)
    assert (576*D2-64*D2-32*D-3*S)%mod == endpoint, ('direct ODE point',p)
    assert (32*Yd-4*Y+S)%mod == endpoint, ('Y flux',p)
    if p>=11:
        coeff = (3*pow(35,-1,p))%p if p%8 in (1,3) else 1
        assert v_end == (p*p*coeff)%mod, ('Wilson terminal residue',p,v_end)
    if p in (5,7,11,13,17,19,23):
        rat=exact_rational_coefficient(p-1)
        assert v_end == rat.numerator * pow(rat.denominator,-1,mod)%mod, ('independent factorial',p)
    row = dict(p=p, eps=eps, endpoint=endpoint, terminal=v_end)
    if p%8==5:
        assert (S*Y)%p==0, ('first-digit input independently checked',p)
        assert bool(S%p) != bool(Y%p), ('exclusive first factor',p)
        if S%p == 0:
            factor='S'
            G=S
            Gprime=D
            assert Gprime%p == Y*pow(16,-1,p)%p
        else:
            factor='Y'
            G=Y
            Gprime=Yd
            assert Gprime%p == -S*pow(32,-1,p)%p
        assert Gprime%p, ('simple zero',p)
        selected_modp2 = (G%(p*p)==0)
        row.update(factor=factor,G=G,Gprime=Gprime,selected_modp2=selected_modp2)
        if selected_modp2:
            rho = - (G//(p*p)) * pow(Gprime,-1,p) %p
            xi=(1+p*p*rho)%mod
            power=1
            actual=0
            for k,vk in enumerate(coefficients):
                weight=1 if factor=='S' else (1+16*k)
                actual=(actual + weight*vk*power)%mod
                power=power*xi%mod
            assert actual==0, ('direct p3 Hensel lift',p,rho,actual)
            row.update(rho=rho,selected_quotient=G//(p*p)%p)
    return row


def main():
    rows=[check(p) for p in primes(5000)]
    subclass=[r for r in rows if r['p']%8==5]
    assert len(rows)==667 and len(subclass)==168
    assert all(r['selected_modp2'] for r in subclass), ('finite class selector',)
    assert sum(r['factor']=='S' for r in subclass)==83
    assert sum(r['factor']=='Y' for r in subclass)==85
    print('PASS all_primes=%d terminal_flux_mod_p3=%d quartic_class=%d hensel_mod_p3=%d' %
          (len(rows),len(rows),len(subclass),len(subclass)))
    for p in (5,7,11,13,19,29,37,53,373):
        row=next(r for r in rows if r['p']==p)
        print(row)


if __name__ == '__main__':
    main()
