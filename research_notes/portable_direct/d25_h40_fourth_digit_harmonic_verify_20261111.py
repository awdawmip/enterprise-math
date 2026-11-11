#!/usr/bin/env python3
"""Exact fourth-digit D25 two-port certificate (author-side, no native experiment)."""
import json
from math import isqrt


def primes(n):
    s = bytearray(b'\x01') * (n + 1)
    s[:2] = b'\x00\x00'
    for d in range(2, isqrt(n) + 1):
        if s[d]:
            s[d*d:n+1:d] = b'\x00' * ((n-d*d)//d+1)
    return [p for p in range(5, n+1) if s[p]]


def check_prime(p):
    assert p >= 5 and all(p % q for q in range(2, isqrt(p)+1))
    eps = 0 if p % 6 == 1 else 1
    assert p % 6 in (1,5)
    m = (p-1-4*eps)//6
    M = p**4
    inv = [0] * p
    inv[1] = 1
    for a in range(2,p):
        inv[a] = (- (M//a) * inv[M%a]) % M
    i2, i6, i36 = pow(2,-1,M), pow(6,-1,M), pow(36,-1,M)
    original, alpha = 1, 1
    h1 = h2 = h3 = 0
    direct = [0,0]
    S,E,J,L = [0,0],[0,0],[0,0],[0,0]
    for k in range(m+1):
        e2 = (h1*h1-h2)*i2 % M
        e3 = (h1**3-3*h1*h2+2*h3)*i6 % M
        for z,rho in enumerate((1, 1-6*eps+12*k)):
            direct[z] = (direct[z]+rho*original) % M
            t = rho*alpha % M
            S[z] = (S[z]+t) % M
            E[z] = (E[z]+t*h1) % M
            J[z] = (J[z]+t*e2) % M
            L[z] = (L[z]+t*e3) % M
        if k==m: break
        z=inv[k+1]**2 % M
        original=original*(m-k)*(2*m+eps-k)*i2*z % M
        alpha=alpha*(-1-4*eps-6*k)*(-1-eps-3*k)*i36*z % M
        u,v=inv[6*k+1+4*eps], inv[3*k+1+eps]
        h1=(h1+u+v)%M
        h2=(h2+u*u+v*v)%M
        h3=(h3+u*u*u+v*v*v)%M
    result = {'p':p,'epsilon':eps,'m':m,'ports':{}}
    for z,name in enumerate(('A','B')):
        assert (S[z]-p*E[z]+p*p*J[z]-p**3*L[z])%M==direct[z]
        row={'value_mod_p4':direct[z]}
        if direct[z]%(p*p)==0:
            assert S[z]%p==0
            y=(S[z]//p-E[z]) % (p**3)
            assert y%p==0
            C=(y//p)%(p*p)
            j=J[z]%(p*p)
            ell=L[z]%p
            assert (C+j-p*ell)%(p*p)==direct[z]//(p*p)
            c1,c0=divmod(C,p)
            j1,j0=divmod(j,p)
            carry=(c0+j0)//p
            d2=(c0+j0)%p
            d3=(c1+j1+carry-ell)%p
            assert d2==direct[z]//p**2%p
            assert d3==direct[z]//p**3%p
            row.update(dict(c0=c0,j0=j0,d2=d2,c1=c1,j1=j1,
                            addition_carry=carry,l0=ell,d3=d3))
        result['ports'][name]=row
    return result


def main():
    tests=primes(1000)+[101419]
    assert len(tests)==167
    results=[check_prime(p) for p in tests]
    select=[r for r in results if r['p'] in (149,211,101419)]
    for r in select:
        port='B' if r['p']==149 else 'A'
        assert r['ports'][port]['d2']=={149:18,211:174,101419:73632}[r['p']]
        assert r['ports'][port]['d3']=={149:84,211:137,101419:69065}[r['p']]
    print(json.dumps({'verified_primes':len(tests),'mismatches':0,
                      'anomalies':select},indent=2))


if __name__=='__main__':
    main()
