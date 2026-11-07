#!/usr/bin/env python3
"""Exact modular verification of the D25 three-stratum p^3 Gauss coefficients and four-port readouts."""
from math import comb

def primes(limit):
    a=bytearray(b'\x01')*(limit+1);a[:2]=b'\x00\x00'
    for d in range(2,int(limit**0.5)+1):
        if a[d]:a[d*d::d]=b'\x00'*((limit-d*d)//d+1)
    return [p for p in range(5,limit+1) if a[p]]

def formulas(p,u,v,c1_num,c2_num,den):
    M=p**3;inv=lambda x:pow(x,-1,M)
    c1,c2=c1_num*inv(den)%M,c2_num*inv(den)%M
    fac=[1]*p;h=[0]*p;h2=[0]*p
    for n in range(1,p):
        fac[n]=fac[n-1]*n%M
        h[n]=(h[n-1]+inv(n))%M
        h2[n]=(h2[n-1]+inv(n)**2)%M
    actual=1;digits=[];coeffs=[]
    for n in range(p):
        if n<=u:
            base=comb(u,n)*comb(v,n)%M
            L=(c1*(h[u]-h[u-n])+c2*(h[v]-h[v-n]))%M
            T=(c1*c1*(h2[u]-h2[u-n])+c2*c2*(h2[v]-h2[v-n]))%M
            expected=base*(1-p*L+p*p*((L*L-T)*inv(2)%M))%M;grade=0
        elif n<=v:
            base=((-1)**(u+n)*c1*fac[u]*fac[n-u-1]*fac[v]
                  *inv(fac[v-n])*inv(fac[n])**2)%M
            S=(c1*(h[n-u-1]-h[u])-c2*(h[v]-h[v-n]))%M
            expected=p*base*(1+p*S)%M;grade=1
        else:
            base=((-1)**(u+v)*c1*c2*fac[u]*fac[v]
                  *fac[n-u-1]*fac[n-v-1]*inv(fac[n])**2)%M
            expected=p*p*base%M;grade=2
        assert expected==actual,(p,u,v,n,grade,expected,actual)
        digits.append(grade);coeffs.append(expected)
        if n<p-1:
            actual=(actual*(n-u+c1*p)*(n-v+c2*p)*inv(n+1)**2)%M
    return digits,coeffs

def original_weighted(p,which):
    M=p**3
    if which=='A':
        return sum((6*n+1)*comb(2*n,n)**2*comb(3*n,n)
                   *pow(pow(216,n,M),-1,M) for n in range(p))%M
    return sum((8*n+1)*comb(2*n,n)**2*comb(4*n,2*n)
               *pow(pow(2304,n,M),-1,M) for n in range(p))%M

def conv(a,b,M):
    return [sum(a[j]*b[n-j] for j in range(n+1))%M for n in range(len(a))]

def ev(A,p,base,weight,euler=False):
    M=p**3
    if euler:A=[(x-(A[i-1] if i else 0))%M for i,x in enumerate(A)]
    return sum((1+weight*n)*x*pow(base,n,M) for n,x in enumerate(A))%M

def gauss_ports(p,u,v,c1num,c2num,den):
    M=p**3; inv=lambda n:pow(n,-1,M)
    c1=c1num*inv(den)%M;c2=c2num*inv(den)%M
    f=[1]*p;H=[0]*p;H2=[0]*p
    for n in range(1,p):
        f[n]=f[n-1]*n%M
        H[n]=(H[n-1]+inv(n))%M
        H2[n]=(H2[n-1]+inv(n)**2)%M
    F0=[0]*p;F1=[0]*p;F2=[0]*p
    for n in range(p):
        if n<=u:
            base=comb(u,n)*comb(v,n)%M
            L=(c1*(H[u]-H[u-n])+c2*(H[v]-H[v-n]))%M
            T=(c1*c1*(H2[u]-H2[u-n])+c2*c2*(H2[v]-H2[v-n]))%M
            F0[n]=base;F1[n]=-base*L%M;F2[n]=base*(L*L-T)*inv(2)%M
        elif n<=v:
            base=((-1)**(u+n)*c1*f[u]*f[n-u-1]*f[v]*inv(f[v-n])*inv(f[n])**2)%M
            S=(c1*(H[n-u-1]-H[u])-c2*(H[v]-H[v-n]))%M
            F1[n]=base;F2[n]=base*S%M
        else:
            F2[n]=((-1)**(u+v)*c1*c2*f[u]*f[v]*f[n-u-1]*f[n-v-1]*inv(f[n])**2)%M
    return F0,F1,F2

def port_samples(p,which):
    M=p**3
    if which=='A':
        m=(p-1)//6;ports=gauss_ports(p,m,2*m,1,2,6)
        base=pow(2,-1,M);weight=6;euler=False
    else:
        k=(p-3)//8 if p%8==3 else (p-5)//8
        ports=gauss_ports(p,k,3*k+1,1,3,8)
        base=pow(9,-1,M);weight=8;euler=p%8==5
    a,b,c=ports
    terms=[conv(a,a,M),[(2*x)%M for x in conv(a,b,M)],
           conv(b,b,M),[(2*x)%M for x in conv(a,c,M)]]
    vals=[ev(term,p,base,weight,euler) for term in terms]
    W=(vals[0]+p*vals[1]+p*p*(vals[2]+vals[3]))%M
    assert W==original_weighted(p,which),(p,which,W,original_weighted(p,which))
    return (vals[0]%M,vals[1]%p**2,vals[2]%p,vals[3]%p),W

if __name__=='__main__':
    ps=primes(401); ca=cb=0
    for p in ps:
        if p%6==1:
            m=(p-1)//6
            digits,coeffs=formulas(p,m,2*m,1,2,6)
            assert digits.count(0)==m+1 and digits.count(1)==m and digits.count(2)==p-2*m-1
            gauss_ports(p,m,2*m,1,2,6)
            port_samples(p,'A')
            ca+=1
        if p%8 in (3,5):
            k=(p-3)//8 if p%8==3 else (p-5)//8
            digits,coeffs=formulas(p,k,3*k+1,1,3,8)
            assert digits.count(0)==k+1 and digits.count(1)==2*k+1 and digits.count(2)==p-3*k-2
            port_samples(p,'B')
            cb+=1
    assert (ca,cb)==(37,41)
    print('PASS p^3 Gauss coefficients and direct original binomial readouts',ca,cb)
    for p in (13,19,43,67,373):
        a,wa=port_samples(p,'A');b,vb=port_samples(p,'B')
        assert wa==vb==p,(p,wa,vb)
        print('four-port',p,'A',a,'B',b)
    a,_=port_samples(373,'A');b,_=port_samples(373,'B')
    assert a==(25720961,64951,198,189)
    assert b==(16706670,63754,188,267)
    assert a[0]-b[0]+373*(a[1]-b[1])+373**2*((a[2]-b[2])+(a[3]-b[3]))==0
    print('PASS exact 373 four-port cancellation')