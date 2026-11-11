#!/usr/bin/env python3
"""D25 two-port differential closure: exact symbolic and finite-field verification."""
from fractions import Fraction
from math import comb
import sympy as S

def ports(n,e):
    a=b=Fraction(0)
    for k in range(n+1):
        v=Fraction(comb(n,k)*comb(2*n+e,k),2**k)
        a+=v
        b+=(1-6*e+12*k)*v
    return a,b

def algebraic():
    s=S.symbols("s")
    d=1-s-4*s*s
    z=2*s/((1+2*s)*(1+s)**2)
    Fs=[(1+2*s)*(1+s)**(e+1)/d for e in (0,1)]
    Ps=[1+22*s+89*s*s+56*s**3+16*s**4,
        -5+46*s+119*s*s-40*s**3-80*s**4]
    Gs=[Fs[e]*Ps[e]/d**2 for e in (0,1)]
    D=2*z*z-71*z+16
    for e in (0,1):
        f,g=Fs[e],Gs[e]
        fp=S.diff(f,s)/S.diff(z,s)
        fpp=S.diff(fp,s)/S.diff(z,s)
        if e==0:
            eq=(5-z)*g-(5+11*z)*f-12*(3*z+2)*z*fp
            ode=z*(z-5)*D*fpp+(5*z**3-106*z*z+702*z-40)*fp+(z*z-4*z+80)*f
        else:
            eq=(8-5*z)*g-(169*z-40)*f-204*z*z*fp
            ode=z*(5*z-8)*D*fpp+(35*z**3-782*z*z+1744*z-192)*fp+15*(z*z-8*z+32)*f
        assert S.factor(eq)==0,(e,"diff")
        assert S.factor(ode)==0,(e,"ODE")

def rationals(N=80):
    for e in (0,1):
        AB=[ports(n,e) for n in range(N+1)]
        A=[z[0] for z in AB];B=[z[1] for z in AB]
        for n in range(N+1):
            am=A[n-1] if n>0 else 0
            amm=A[n-2] if n>1 else 0
            bm=B[n-1] if n>0 else 0
            if e==0:
                assert 5*B[n]-bm==(24*n+5)*A[n]+(36*n-25)*am
                if n<N:
                    assert 40*(n+1)*(2*n+1)*A[n+1]==(371*n*n+331*n+80)*A[n]+(-81*n*n+137*n-60)*am+(2*n*n-5*n+3)*amm
            else:
                assert 8*B[n]-5*bm==-40*A[n]+(204*n-35)*am
                if n<N:
                    assert 64*(n+1)*(2*n+3)*A[n+1]==(648*n*n+1096*n+480)*A[n]+(-371*n*n+331*n-80)*am+(10*n*n-15*n+5)*amm

def fast_ports(p):
    e=0 if p%6==1 else 1
    m=(p-1-4*e)//6
    inv=[0]*(2*m+4);inv[1]=1
    for k in range(2,len(inv)):
        inv[k]=(-p//k * inv[p%k])%p if False else (p-(p//k)*inv[p%k]%p)%p
    prev2=prev1=0
    a=1;b=(1 if e==0 else -5)%p
    c=pow(40 if e==0 else 64,-1,p)
    v=pow(5 if e==0 else 8,-1,p)
    for n in range(m):
        if e==0:
            rhs=(371*n*n+331*n+80)*a+(-81*n*n+137*n-60)*prev1+(2*n*n-5*n+3)*prev2
            aa=rhs*c*inv[n+1]*inv[2*n+1]%p
            bb=((24*(n+1)+5)*aa+(36*(n+1)-25)*a+b)*v%p
        else:
            rhs=(648*n*n+1096*n+480)*a+(-371*n*n+331*n-80)*prev1+(10*n*n-15*n+5)*prev2
            aa=rhs*c*inv[n+1]*inv[2*n+3]%p
            bb=(-40*aa+(204*(n+1)-35)*a+5*b)*v%p
        prev2,prev1,a,b=prev1,a,aa,bb
    return a,b

def finite(limit=50000):
    counts={"A_zero":0,"B_zero":0}
    for p in S.primerange(7,limit+1):
        p=int(p)
        a,b=fast_ports(p)
        assert (a==0)!=(b==0),(p,a,b)
        chi=pow(p-6,(p-1)//2,p)
        assert (a==0)==(chi==p-1),(p,a,b,chi)
        counts["A_zero" if a==0 else "B_zero"]+=1
    assert counts=={"A_zero":2583,"B_zero":2547},counts
    return counts

if __name__=="__main__":
    algebraic()
    rationals(80)
    c=finite()
    print("PASS: 2 differential identities, 2 ODE identities, 162 rational port checks,",
          "160 rational ODE recurrence checks, 5130 primes 7..50000, counts",c)
