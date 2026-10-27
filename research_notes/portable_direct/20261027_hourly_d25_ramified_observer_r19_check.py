#!/usr/bin/env python3
"""R19 exact author check, original p19 four-face algebraic observer obstruction."""
from fractions import Fraction
from math import comb, factorial
P=19; M=3; L,N=-5,5; Z0=13

def source():
    f=[Fraction(1)]
    for r in range(P-1):
        f.append(f[-1]*Fraction((6*r+1)*(3*r+1),18*(r+1)**2))
    beta={r:f[r]/P**2 for r in range(7,P)}
    theta=Fraction(-P,6); Z={}; E={}
    for n in range(L,N+1):
        pairs=[(j,j+n) for j in range(1,7) if 1<=j+n<=6]
        Z[n]=sum(((j+ell-P)*f[j]*beta[P-ell] for j,ell in pairs),Fraction())
        if n>=0:
            E[n]=(2*(M+theta)**2*beta[P-n-1]-
                  (6*M*M-8*M*theta+2*theta**2)*f[6-n]*beta[12])
        else:
            E[n]=((20*M*M-14*M*theta+2*theta**2)*f[-n]*beta[P-1]+
                  (2*M*theta-2*theta**2)*f[6]*beta[P-(7+n)])
    assert all(E[n]==(P-n)*Z[n]-(P-n-Fraction(1,2))*Z.get(n+1,Fraction()) for n in Z)
    assert Z[L]==-4*M*f[6]*beta[P-1]
    return Z,E

def residue(a,mod):
    assert a.denominator%P
    return (a.numerator*pow(a.denominator,-1,mod))%mod

def valuation(a):
    if not a:return 999
    def v(n):
        r=0
        while n%P==0:r+=1;n//=P
        return r
    return v(abs(a.numerator))-v(a.denominator)

def choose_integer(n,k):
    a=1
    for i in range(k):a*=n-i
    return a//factorial(k)

def run():
    Z,E=source()
    T=[Z[i-5] for i in range(11)]
    c=[sum((comb(i,k)*Z0**(i-k)*T[i] for i in range(k,11)),Fraction()) for k in range(11)]
    q=[residue(a,361) for a in c]
    assert q==[247,304,342,122,82,193,85,232,36,241,44]
    assert [valuation(c[i]) for i in range(4)]==[1,1,1,0]
    assert residue(c[0]/P,P)==13 and residue(c[3],P)==8
    assert (-13*pow(8,-1,P))%P==15
    assert all(pow(u,3,P)!=15 for u in range(1,P))
    def jets(low,high):
        return [residue(sum((choose_integer(n,k)*Fraction(Z0)**(n-k)*E[n]
                              for n in range(low,high+1)),Fraction()),P)
                for k in range(3)]
    negative=jets(L,-1);positive=jets(0,N)
    assert negative==[8,4,3] and positive==[11,15,9]
    assert [(a+b)%P for a,b in zip(negative,positive)]==[0,0,12]
    coefficient=-(1-pow(Z0,-1,P))*pow(Z0,-4,P)*3*8%P
    assert coefficient==12
    def ports(z):
        z=Fraction(z)
        O=sum((z**n*Z[n] for n in Z),Fraction())
        J=sum((n*z**n*Z[n] for n in Z),Fraction())
        Gm=sum((z**n*E[n] for n in range(L,0)),Fraction())
        Gp=sum((z**n*E[n] for n in range(0,N+1)),Fraction())
        boundary=(P-L+Fraction(1,2))*z**(L-1)*Z[L]
        assert (Gm+Gp)==(P-(P+Fraction(1,2))/z)*O-(1-1/z)*J+boundary
        return O,J,Gm+Gp,boundary
    O,J,G,B=ports(Z0)
    assert tuple(residue(a,361) for a in (O,J,G))==(95,323,95)
    assert valuation(B)==1
    for t in range(P):
        O,J,G,B=ports(13+P*t)
        assert residue(O,361)==residue(G,361)==95
    print("PASS: original rational four-face p19; 11 Taylor coefficients; jets",negative,positive)
    print("PASS: ramified root leading x^3/19=15; G/x^2=12; 19 integral lifts")

if __name__=="__main__":run()
