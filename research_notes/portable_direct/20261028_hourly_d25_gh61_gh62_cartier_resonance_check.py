#!/usr/bin/env python3
"""GH-61/GH-62 exact finite-field checks. Standard library; no native experiment."""
from math import comb

def primes_below(limit):
    sieve = bytearray(b'\x01') * limit
    sieve[:2] = b'\x00\x00'
    for j in range(2, int(limit**0.5)+1):
        if sieve[j]:
            sieve[j*j:limit:j] = b'\x00'*len(sieve[j*j:limit:j])
    return [p for p in range(11,limit) if sieve[p] and p%8==3]

def gauss_coeffs(p):
    m=(p-3)//8
    f=[1]
    for r in range(m):
        f.append(f[-1]*(m-r)**2*pow((2*m+2+r)*(r+1),-1,p)%p)
    return m,f

def chart_data(p,m,f,a):
    fv=sum(c*pow(a,i,p) for i,c in enumerate(f))%p
    fp=sum(i*c*pow(a,i-1,p) for i,c in enumerate(f) if i)%p
    D=comb(3*m+1,m)%p
    q=pow(a,-(2*m+2),p)*pow(1-a,4*m+1,p)%p
    assert q and D
    return fv,fp,D,q

def jets(p,a,u,yp):
    A=a*(1-a)%p
    B=(5-7*a)*pow(4,-1,p)%p
    inv8=pow(8,-1,p)
    aa=[u%p,yp%p]
    for n in range(p-2):
        rhs=(n+3*inv8)**2*aa[n]-(n+1)*(n*(1-2*a)+B)*aa[n+1]
        aa.append(rhs*pow(A*(n+1)*(n+2)%p,-1,p)%p)
    C=((9*a-3)*pow(4,-1,p)*aa[p-1]+169*pow(64,-1,p)*aa[p-2])%p
    T=25*pow(64,-1,p)*aa[p-1]%p
    return C,T

def mul(a,b,p,n):
    c=[0]*n
    for i,x in enumerate(a[:n]):
        if x:
            for j,y in enumerate(b[:n-i]):
                c[i+j]=(c[i+j]+x*y)%p
    return c

def inv(a,p,n):
    s=[pow(a[0],-1,p)]
    for k in range(1,n):
        s.append(-s[0]*sum(a[j]*s[k-j] for j in range(1,min(k+1,len(a))))%p)
    return s

def power(a,e,p,n):
    out=[1]+[0]*(n-1)
    b=a[:n]
    while e:
        if e&1: out=mul(out,b,p,n)
        b=mul(b,b,p,n)
        e>>=1
    return out

def omega_coeff(p,m,f,a):
    floc=[sum(f[i]*comb(i,j)*pow(a,i-j,p) for i in range(j,len(f)))%p
          for j in range(len(f))]
    shift=0
    while shift<len(floc) and floc[shift]==0: shift+=1
    assert shift in (0,1)
    n=p+2*shift
    fi=power(inv(floc[shift:],p,n),2,p,n)
    qp=power([1-a,-1],4*m+1,p,n)
    qi=power(inv([a,1],p,n),2*m+2,p,n)
    o=mul(mul(qp,qi,p,n),fi,p,n)
    return o[p-1+2*shift], (o[2*shift-1] if shift else 0)

def main():
    total=roots=cartier=0
    for p in primes_below(2000):
        m,f=gauss_coeffs(p)
        for a in (2,9,p-1):
            fv,fp,D,q=chart_data(p,m,f,a)
            roots+=int(fv==0)
            for u,yp in ((1,0),(0,1)):
                C,T=jets(p,a,u,yp)
                W=(fv*yp-fp*u)%p
                assert C==(1-a)*D*D*fv*W*pow(q,-1,p)%p
                if fv==0:
                    assert T==(1-a)*D*D*fp*fp*u*pow(q,-1,p)%p
                total+=1
        if p in (11,19,43,59,67,83,107):
            for a in (2,9):
                C,R=omega_coeff(p,m,f,a)
                D=comb(3*m+1,m)%p
                assert C==-D*D*pow(a,-1,p)%p and R==0
                cartier+=1
    m,f=gauss_coeffs(43)
    assert chart_data(43,m,f,6)==(20,37,25,1)
    assert jets(43,6,1,0)==(3,0)
    assert jets(43,6,0,1)==(10,0)
    print('PASS_GH61_GH62',total,'basis/chart comparisons',roots,'root charts',cartier,'Laurent series')
    print('PASS_SINGLE_TERMINAL_COUNTEREXAMPLE p=43 a=6')

if __name__=='__main__':
    main()
