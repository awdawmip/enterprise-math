#!/usr/bin/env python3
"""Exact author-side p-residue validation of a factorial/WZ-ready D25 inverse-moment port."""
from math import isqrt

def primes(bound):
    s=bytearray(b'\x01')*(bound+1);s[:2]=b'\x00\x00'
    for d in range(2,isqrt(bound)+1):
        if s[d]:s[d*d::d]=b'\x00'*(((bound-d*d)//d)+1)
    return [p for p in range(7,bound+1) if s[p] and p%6==1]

def test(p):
    l=(p-1)//6;m=2*l;h=3*l
    f=[1]
    for n in range(1,p):f.append(f[-1]*n%p)
    inv=lambda v:pow(v%p,-1,p)
    # a_0...a_h computed in modulus p^2 so a_{m+j}/p is exact mod p.
    q=p*p;a=1;coef=[1]
    for n in range(h):
        a=a*(2*n+1)*(3*n+1)*(3*n+2)*pow(36*(n+1)**3,-1,q)%q
        coef.append(a)
    common=f[h]*f[2*m]*f[m]%p
    inv_moment=0;fac_moment=0
    t=None
    for j in range(1,l+1):
        k=m+j
        u=(coef[k]//p)%p
        u_fac=(common*f[j-1]*inv(3*f[l-j]*f[m-j]*pow(2,k,p)*pow(f[k],3,p)))%p
        assert u==u_fac,(p,j,'coefficient',u,u_fac)
        inv_moment=(inv_moment+(1-6*k)*inv(36*k**3*u))%p
        if j==1:
            t=pow(2,m+j,p)*pow(f[m+j-1],3,p)*f[l-j]*f[m-j]*inv(f[j-1])%p
        else:
            t=(t*2*pow(m+j-1,3,p)*inv((j-1)*(l-j+1)*(m-j+1)))%p
        t_exact=pow(2,m+j,p)*pow(f[m+j-1],3,p)*f[l-j]*f[m-j]*inv(f[j-1])%p
        assert t==t_exact,(p,j,'hypergeo recurrence',t,t_exact)
        fac_moment=(fac_moment+(1-6*k)*t)%p
    fac_moment=fac_moment*inv(12*common)%p
    assert inv_moment==fac_moment,(p,inv_moment,fac_moment)
    return (p,inv_moment,fac_moment)

def main():
    pp=primes(5000)
    for p in pp:
        res=test(p)
        if p in (7,13,19,37,67,157,373):print('ANCHOR',res)
    print('PASS_D25_FACTORIAL_INVERSE_MOMENT',len(pp),'primes',sum(p%24 in (13,19) for p in pp),'frozen')

if __name__=='__main__':main()
