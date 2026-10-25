#!/usr/bin/env python3
"""Exact rational Clausen/first-p-adic resonance-defect author checker."""
from fractions import Fraction

def prime(n):
    return n >= 2 and all(n % d for d in range(2, int(n ** .5) + 1))

def convolution(a,b,mod=None):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if mod:
                out[i+j]=(out[i+j]+x*y)%mod
            else:
                out[i+j]+=x*y
    return out

def exact_small(p):
    m=(p-1)//6; c=Fraction(2-p,2)
    U=[Fraction(1)];C=[Fraction(1)];T=[Fraction(1)]
    for n in range(m):
        U.append(U[-1]*Fraction((n-m)*(n-2*m),(n+1)**2))
        C.append(C[-1]*Fraction((n-m)*(n-2*m),(n+1)*(n+c)))
    for n in range(2*m):
        T.append(T[-1]*Fraction((n-2*m)*(n-4*m)*(n-3*m),(n+1)*(n+c)*(n+1-p)))
    assert convolution(C,C)==T,(p,"exact Clausen")
    return p

def modular_check(p):
    m=(p-1)//6; q=p*p
    U=[1];C=[1];H=[0];h=0
    for n in range(m):
        a=(n-m)*(n-2*m)
        U.append(U[-1]*a*pow((n+1)**2,-1,q)%q)
        C.append(C[-1]*2*a*pow((n+1)*(2*n+2-p),-1,q)%q)
        h=(h+pow(n+1,-1,q))%q
        H.append(U[-1]*h%q)
    T=[1]
    for n in range(2*m):
        T.append(T[-1]*2*(n-2*m)*(n-4*m)*(n-3*m)*
                 pow((n+1)*(2*n+2-p)*(n+1-p),-1,q)%q)
    U2=convolution(U,U,q);C2=convolution(C,C,q);UH=convolution(U,H,q)
    assert C2==T,(p,"Clausen coefficientwise mod p²")
    assert all((U2[n]+p*UH[n]-T[n])%q==0 for n in range(2*m+1)),(p,"resonant correction")
    inv2=pow(2,-1,q)
    def read(a):
        x=dx=weighted=0; z=1
        for k,b in enumerate(a):
            v=b*z%q;x=(x+v)%q;dx=(dx+k*v)%q;weighted=(weighted+(6*k+1)*v)%q
            z=z*inv2%q
        return x,dx,weighted
    u,du,_=read(U); hh,_,_=read(H); tt,_,ot=read(T)
    u2,_,ou2=read(U2)
    assert (u2-tt+p*u*hh)%q==0
    assert (ou2-ot+p*read(UH)[2])%q==0
    if p%24 in (13,19):
        assert u%p==0 and tt%q==0,(p,"inert strong value")
        assert (ot-ou2-6*p*du*hh)%q==0,(p,"weighted observer defect")
    return (p,u,tt,ou2,ot,du%p,hh%p)

if __name__=="__main__":
    small=[exact_small(p) for p in (7,13,19,31,37,43)]
    cases=[modular_check(p) for p in [*(p for p in range(7,374) if p%6==1 and prime(p)),1327]]
    print("EXACT_CLAUSEN_PASS",small)
    print("MODULAR_RESONANCE_PASS",len(cases))
    print("TARGET_WITNESSES",[r for r in cases if r[0] in (13,19,37,43,373)])
