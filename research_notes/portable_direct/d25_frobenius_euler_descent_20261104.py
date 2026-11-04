#!/usr/bin/env python3
"""Exact finite-field Euler/Clausen descent certificate for p = 5 (mod 8).
No network or third-party packages. All operations in F_p.
"""
from math import comb

def primes(n):
    s = bytearray(b'\x01')*(n+1)
    s[0:2] = b'\x00\x00'
    for d in range(2, int(n**.5)+1):
        if s[d]: s[d*d:n+1:d] = b'\x00'*(((n-d*d)//d)+1)
    return [i for i in range(5,n+1) if s[i] and i%8==5]

def gauss(p, a, b, end):
    out = [1]
    for k in range(1,end+1):
        num=(8*k-8+a)*(8*k-8+b)
        out.append(out[-1]*num*pow(576*k*k,-1,p)%p)
    return out

def quartic(p, end):
    out=[1]
    for k in range(1,end+1):
        out.append(out[-1]*(4*k-3)*(4*k-2)*(4*k-1)*pow(576*k*k*k,-1,p)%p)
    return out

def verify(p):
    q=(p-5)//8; L=5*q+3; t=2*q+1; N=(p+1)//2
    v=gauss(p,1,3,p-1)
    c=gauss(p,5,7,q)
    b=quartic(p,t)
    assert v[L] and b[t] and all(x==0 for x in v[L+1:])
    alpha=-pow(9,-1,p)%p
    lam=v[L]*v[L]*pow(b[t],-1,p)%p
    assert lam==alpha, ('lambda',p,lam,alpha)
    if p in (5,13,29,37,373):
        for k in range(t+1):
            original=(comb(4*k,2*k)*comb(2*k,k)**2*pow(2304,-k,p))%p
            assert original==b[k], ('original_b',p,k,original,b[k])
    gpow=[comb(N,i)*pow(alpha,i,p)%p for i in range(N+1)]
    # P = g^N C on every coefficient, not just at z=1.
    for k in range(L+1):
        val=sum(c[j]*gpow[k-j] for j in range(max(0,k-N),min(q,k)+1))%p
        assert val==v[k], ('P',p,k,val,v[k])
    # B = g*C^2: all t+1 coefficients.
    c2=[sum(c[j]*c[n-j] for j in range(max(0,n-q),min(q,n)+1))%p for n in range(2*q+1)]
    for k in range(t+1):
        val=(c2[k] if k<len(c2) else 0)+ (alpha*c2[k-1] if k else 0)
        assert val%p==b[k], ('B',p,k,val,b[k])
    S=sum(v)%p
    Y=sum((16*k+1)*v[k] for k in range(p))%p
    c0=sum(c)%p
    c1=sum(k*c[k] for k in range(1,q+1))%p
    factor=pow((1+alpha)%p,N,p)
    assert S==factor*c0%p
    assert Y==16*factor*c1%p
    assert (c0==0) != (c1==0), ('exclusive',p,c0,c1)
    selected=('C(1)' if c0==0 else "C'(1)")
    return p,q,lam,c0,c1,selected

if __name__=='__main__':
    pp=primes(2000)
    rows=[verify(p) for p in pp]
    assert len(rows)==79
    print('PASS primes=%d, full_P_coefficients=%d, full_B_coefficients=%d, source_observers=%d' % (
        len(pp),sum(5*q+4 for _,q,*_ in rows),sum(2*q+2 for _,q,*_ in rows),len(rows)))
    for x in rows:
        if x[0] in (5,13,29,37,53,61,373): print('CASE p=%d q=%d lambda=%d C1=%d Cprime1=%d zero=%s'%x)
