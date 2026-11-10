#!/usr/bin/env python3
"""Source-frozen D25 R vs third-band t: original-tagged finite witnesses.
Author-side portable only; not native Source, independent review or admission.
"""
from math import comb, factorial


def check(p):
    assert p % 24 in (13, 19)
    m = (p - 1) // 6
    q = p ** 4
    B = [1]
    for k in range(p - 1):
        B.append(B[-1] * (6*k+1) * (3*k+1) * pow(36*(k+1)**2,-1,q) % q)
    n = d = 1
    for k in range(p):
        assert B[k] == n * pow(d,-1,q) % q
        n *= (6*k+1)*(3*k+1)
        d *= 36*(k+1)**2
    g = sum(B) % q
    h = sum((12*k+1)*B[k] for k in range(p)) % q
    assert g % p == 0
    G = (g//p) % (p*p)
    assert (G*h)%p == 1
    Delta = ((G*h % (p*p) - 1)//p) % p
    tail = sum(B[2*m+1:]) % q
    assert tail % (p*p) == 0
    t = ((tail//(p*p)) * h) % p

    def C(r):
        den = 1
        for j in range(r):
            den = den * (6*j+5) * (3*j+2) % p
        return pow(2,r-1,p) * factorial(r-1)**2 * pow(18,r-1,p) * pow(den,-1,p) % p

    R = 0
    for i in range(1,m+1):
        bi = comb(m,i)*comb(2*m,i)*pow(2,-i,p)%p
        assert bi == B[i]%p
        for r in range(1,i+1):
            assert B[p-r] % (p*p) == 0
            assert B[p-r]//(p*p)%p == C(r)
            R = (R + 2*bi*(1+6*(i-r))*C(r))%p

    stream = 0; s = 0; j = 0; bi = 1; c = pow(10,-1,p)
    for i in range(1,m+1):
        bi = bi*(m-i+1)*(2*m-i+1)*pow(2*i*i,-1,p)%p
        s = (s+c)%p; j = (j+i*c)%p
        stream = (stream + 2*bi*((1+6*i)*s-6*j))%p
        if i < m:
            c = c*36*i*i*pow((6*i+5)*(3*i+2),-1,p)%p
    assert stream == R
    W = 0; a = 1; mod = p**3
    for k in range(p):
        W = (W+(6*k+1)*a)%mod
        if k < p-1:
            a = a*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3,-1,mod)%mod
    assert (g*h-W)%mod == p*p*R%mod
    assert (Delta-R)%p == ((W-p)%mod//(p*p))%p
    return (p, t, R, Delta, W)

if __name__ == '__main__':
    rows = [check(p) for p in (13,157,373)]
    assert rows == [(13,9,0,0,13),(157,0,82,82,157),(373,197,196,196,373)]
    print('PASS SOURCE-FROZEN TWO-WAY ZERO SET',rows)
