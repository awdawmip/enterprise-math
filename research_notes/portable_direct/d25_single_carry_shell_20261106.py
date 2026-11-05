#!/usr/bin/env python3
"""D25 single-carry shell: exact independent finite-field checks; portable, not native CM."""
from math import isqrt

def primes_to(n):
    s=bytearray([1])*(n+1);s[:2]=bytes((0,0))
    for k in range(2,isqrt(n)+1):
        if s[k]: s[k*k:n+1:k]=b'\\0'*((n-k*k)//k+1)
    return [i for i in range(n+1) if s[i]]

def values(q):
    eps=1 if q%6==1 else -1
    m=(q-eps)//6
    delta=(1-eps)//2
    a,b,c=(2*m-delta,3*m-delta,4*m-delta)
    assert 0<=a<b<c<q
    inv=[0]*q
    for j in range(1,q):inv[j]=pow(j,-1,q)
    fac=[1]*q; ifac=[1]*q
    for j in range(1,q):fac[j]=fac[j-1]*j%q
    ifac[-1]=pow(fac[-1],-1,q)
    for j in range(q-1,0,-1):ifac[j-1]=ifac[j]*j%q
    def C(n,k):
        return fac[n]*ifac[k]%q*ifac[n-k]%q if 0<=k<=n else 0
    H=[0]*q
    for j in range(1,q):H[j]=(H[j-1]+inv[j])%q
    v=pow(-2,-1,q)
    vpow=1
    Z=L=Shead=Stail=0
    for j in range(b+1):
        if j<=a:
            uj=vpow*C(a,j)*C(b,j)*C(c,j)%q
            hj=H[a]-H[a-j]+H[b]-H[b-j]+H[c]-H[c-j]+3*H[j]
            ej=uj*hj%q
            Z=(Z+uj)%q;L=(L+(6*j+1)*uj)%q
            Shead=(Shead+(6*j+1)*ej)%q
        else:
            slope=(-1 if (j-a-1)%2 else 1)*fac[a]*fac[j-a-1]%q*ifac[j]%q
            ej=vpow*slope*C(b,j)*C(c,j)%q
            Stail=(Stail+(6*j+1)*ej)%q
        vpow=vpow*v%q
    u,e=1,0; zr=lr=sr=0
    for j in range(q):
        zr=(zr+u)%q;lr=(lr+(6*j+1)*u)%q;sr=(sr+(6*j+1)*e)%q
        if j==q-1: break
        ts=[a-j,b-j,c-j]
        P=ts[0]*ts[1]*ts[2]%q
        Q=(ts[0]*ts[1]+ts[0]*ts[2]+ts[1]*ts[2])%q
        cf=v*P*pow(inv[j+1],3,q)%q
        df=v*(Q+3*P*inv[j+1])*pow(inv[j+1],3,q)%q
        u,e=cf*u%q,(cf*e+df*u)%q
    assert (Z,L,(Shead+Stail)%q)==(zr,lr,sr), (q,Z,L,Shead,Stail,zr,lr,sr)
    assert L==0,(q,L)
    return (q,eps,m,a,b,c,Z,Shead,Stail,sr)

if __name__=='__main__':
    ps=[p for p in primes_to(3000) if p>=5]
    rs=[values(q) for q in ps]
    assert len(rs)==428
    assert sum(r[8]!=0 for r in rs)==427
    print('PASS',len(rs),'primes 5<=q<=3000')
    print('q eps m a b c Z S_regular S_singlecarry S_total')
    for r in rs:
        if r[0] in (5,7,11,13,19,31,373,1009,2003):print(*r)
