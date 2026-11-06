#!/usr/bin/env python3
"""D25 source-Jacobian certificate: field-exact, author-side, not native H0/B0."""
from math import comb

def primes(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[:2] = b'\x00\x00'
    for d in range(2, int(n**0.5) + 1):
        if sieve[d]:
            sieve[d*d::d] = b'\x00' * ((n-d*d)//d+1)
    return [p for p in range(5,n+1) if sieve[p] and p%6==1]

def det3(a,p):
    a=[row[:] for row in a]
    out=1
    for k in range(3):
        t=next((r for r in range(k,3) if a[r][k]%p),None)
        if t is None: return 0
        if t!=k:
            a[t],a[k]=a[k],a[t];out=-out
        z=a[k][k]%p;out=out*z%p
        zinv=pow(z,-1,p)
        for r in range(k+1,3):
            c=a[r][k]*zinv%p
            for j in range(k,3): a[r][j]=(a[r][j]-c*a[k][j])%p
    return out%p

def samples(p, js):
    m=(p-1)//6
    s=[2*m,3*m,4*m]
    return [[sum(pow(v-r,-1,p) for r in range(j))%p for v in s] for j in js]

def interpolate_recover(p, s, y):
    gam=[y[0],(y[1]-y[0])%p,(y[2]-y[1])%p]
    q=lambda z: (s[0]-z)*(s[1]-z)*(s[2]-z)%p
    x=[]
    for v in s:
        P=0
        for r in range(3):
            numer=1;denom=1
            for t in range(3):
                if t!=r: numer=numer*(v-t)%p;denom=denom*(r-t)%p
            P=(P+q(r)*gam[r]*numer*pow(denom,-1,p))%p
        den=1
        for other in s:
            if other!=v: den=den*(other-v)%p
        x.append(P*pow(den,-1,p)%p)
    return x

def run():
    count=0
    for p in primes(3000):
        if p<13: continue
        m=(p-1)//6;s=[2*m,3*m,4*m]
        js=[1,3,4] if m==2 else ([1,2,4] if m==3 else [1,2,3])
        mat=samples(p,js)
        d=det3(mat,p)
        assert d!=0, (p,'rank failure')
        factors=[]
        for j in js:
            u=pow(-2,-j,p)
            for v in s:u=u*comb(v,j)%p
            w=(6*j+1)*u%p
            assert w != 0, (p,j,'bad weighted coordinate')
            factors.append(w)
        x=[1,2,3]
        y=[sum(mat[k][i]*x[i] for i in range(3))%p for k in range(3)]
        if m>=4:
            assert interpolate_recover(p,s,y)==x, (p,'interpolation failure')
        if p in (13,19,31,373,1009,2003):
            print('p=%d m=%d js=%s det=%d weighted_u=%s y=%s'%(p,m,js,d,factors,y))
        count+=1
    print('PASS: %d primes p=1 mod6, 13<=p<=3000; rank3, nonzero weighted coords, recovery for m>=4.'%count)
    for p in (13,19,373):
        m=(p-1)//6;a,b,c=2*m,3*m,4*m
        x=[a,-b,0]
        D=samples(p,[1,2])
        ys=[sum(row[i]*x[i] for i in range(3))%p for row in D]
        assert ys[0]==0 and ys[1]!=0
        print('one-coordinate loss p=%d: x=%s, first-two-normalized-observations=%s'%(p,x,ys))

if __name__=='__main__':run()
