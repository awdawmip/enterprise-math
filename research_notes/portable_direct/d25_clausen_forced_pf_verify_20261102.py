#!/usr/bin/env python3
"""Exact author-side test of finite Clausen defect's forced Picard--Fuchs jet recurrence.
No native H0/B0 experiment, Source checkpoint, or mathematical admission.
"""
from math import comb, isqrt

def primes_1_mod_6(bound):
    sieve = bytearray(b'\x01') * (bound + 1)
    sieve[:2] = b'\x00\x00'
    for d in range(2, isqrt(bound) + 1):
        if sieve[d]:
            sieve[d*d::d] = b'\x00' * (((bound - d*d) // d) + 1)
    return [p for p in range(7, bound + 1) if sieve[p] and p % 6 == 1]

def poly_mul(a, b, p):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] = (c[i+j] + x*y) % p
    return c

def verify(p, max_n=5):
    assert p > 3 and p % 6 == 1
    r = (p-1) // 6
    mod = p**3
    inv18 = pow(18, -1, mod)
    inv2 = pow(2, -1, mod)
    h, a, two = [1]*p, [1]*p, [1]*p
    for k in range(1, p):
        ik = pow(k, -1, mod)
        two[k] = two[k-1]*inv2 % mod
        h[k] = h[k-1]*(6*k-5)*(3*k-2)*inv18*ik*ik % mod
        a[k] = a[k-1]*(2*k-1)*(3*k-2)*(3*k-1)*inv18*ik*ik*ik % mod
    degree = max_n + 3
    hg = [sum(pow(k,d,mod)*h[k]*two[k] for k in range(p))%mod for d in range(degree+1)]
    ff = [sum(pow(k,d,mod)*a[k]*two[k] for k in range(p))%mod for d in range(degree+1)]
    D = []
    for d in range(degree+1):
        diff = (sum(comb(d,j)*hg[j]*hg[d-j] for j in range(d+1))-ff[d])%mod
        assert diff % (p*p) == 0, (p, d, 'not integral')
        D.append(diff//(p*p))
    Pj = []
    for d in range(max_n+2):
        Pj.append(sum(pow(k,d,p)*comb(r,k)*comb(2*r,k)*pow(2,-k,p) for k in range(r+1)) % p)
    inv2p, inv6p, inv18p = (pow(t,-1,p) for t in (2,6,18))
    Q = [pow(9,-1,p), 13*inv18p%p, 3*inv2p%p, 1]
    pow_shift = [1]
    for n in range(max_n+1):
        if n: pow_shift = poly_mul(pow_shift, [1,1], p)
        q = poly_mul(pow_shift, Q, p)
        lhs = (D[n+3]-inv2p*sum(q[k]*D[k] for k in range(len(q)))) % p
        rhs = (-inv6p*Pj[n+1]) % p
        assert lhs == rhs, (p,n,lhs,rhs)
    assert (18*D[3]-27*D[2]-13*D[1]-2*D[0]+6*Pj[1])%p == 0
    assert (18*D[4]-45*D[3]-40*D[2]-15*D[1]-2*D[0]+6*Pj[2])%p == 0
    assert (36*D[4]-108*D[3]-53*D[2]-17*D[1]-2*D[0]+2*pow(3,-1,p)*Pj[0])%p == 0
    if p%24 in (13,19):
        assert Pj[0] == 0, (p,'CM root not in finite sample')
        assert (36*D[4]-108*D[3]-53*D[2]-17*D[1]-2*D[0])%p == 0
    return D, Pj

def verify_polynomial_coefficients(p):
    """Independent coefficient-by-coefficient forced ODE check, small prime sample."""
    r=(p-1)//6; mod=p**3
    h=[1]*p
    for k in range(1,p):
        h[k]=h[k-1]*(6*k-5)*(3*k-2)*pow(18*k*k,-1,mod)%mod
    conv=[0]*(2*p-1)
    for i in range(p):
        for j in range(p):
            conv[i+j]=(conv[i+j]+h[i]*h[j])%mod
    E=[0]*(2*p)
    for n in range(p,2*p-1):
        assert conv[n]%(p*p)==0
        E[n]=conv[n]//(p*p)
    q=lambda k:(k+pow(2,-1,p))*(k+pow(3,-1,p))*(k+2*pow(3,-1,p))%p
    for n in range(2*p):
        lhs=(n**3*E[n]-q(n-1)*E[n-1])%p
        j=n-p
        rhs=(-pow(3,-1,p)*j*comb(r,j)*comb(2*r,j))%p if 0<=j<=r else 0
        assert lhs==rhs,(p,n,lhs,rhs)
    return True

def main():
    ps = primes_1_mod_6(3000)
    for p in ps:
        verify(p)
    for p in ps:
        if p<=103:verify_polynomial_coefficients(p)
    print('PASS: coefficientwise forced ODE checked for all p=1mod6 primes <=103')
    print('PASS:',len(ps),'primes 7<=p<=3000, p=1 mod6; n=0..5 forced PF recurrence; direct Clausen derivatives modulo p^3 versus independent binomial CM jets')
    for p in [7,13,19,31,37,43,61,373,1171]:
        D,Pj = verify(p)
        print('CERT',p,'D0..D5=',D[:6],'P0,P1,P2=',Pj[:3], 'CM=',p%24 in (13,19))
    print('STATUS=AUTHOR-DERIVED / EXACT-TESTED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING')
if __name__=='__main__': main()
