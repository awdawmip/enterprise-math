#!/usr/bin/env python3
"""D25 SB4: exact original low-half sum at the 3 R51 exceptional primes.

Reads the untouched integer factorial W/S terms, *not* a simulated native
Hasse/CM source. Finite exhaustive special-prime check, not a general proof.
"""
from fractions import Fraction
from math import isqrt

def isprime(n):
    return n >= 2 and all(n%d for d in range(2, isqrt(n)+1))

def qmod(x,p):
    if isinstance(x,Fraction):
        return x.numerator*pow(x.denominator,-1,p)%p
    return x%p

def a(k):
    return Fraction((6*k+7)*(2*k+1)*(3*k+1)*(3*k+2),36*(6*k+1)*(k+1)**3)

def b(k):
    return Fraction((8*k+9)*(2*k+1)*(4*k+1)*(4*k+3),288*(8*k+1)*(k+1)**3)

def normalized(k,p):
    vals=[];units=[]
    for r in (k,2*k,3*k,4*k):
        fac=1;nu=0
        for q in range(1,r+1):
            while q%p==0:
                q//=p;nu+=1
            fac=fac*q%p
        vals.append(nu); units.append(fac)
    assert vals[1]+vals[2]-5*vals[0]==3
    assert vals[3]-4*vals[0]==3
    u1,u2,u3,u4=units
    w=(6*k+1)*u2*u3*pow(u1**5*pow(216,k,p),-1,p)%p
    s=(8*k+1)*u4*pow(u1**4*pow(2304,k,p),-1,p)%p
    assert w and s
    return w,s

def run(p):
    assert p%6==1 and p>=13 and isprime(p)
    h=(p-1)//2
    mod=p*p
    fs=[1]*(4*h+1)
    for n in range(1,len(fs)):
        fs[n]=fs[n-1]*n%mod
    Lw=Ls=0
    for k in range(h+1):
        denw=pow(fs[k],5,mod)*pow(216,k,mod)%mod
        dens=pow(fs[k],4,mod)*pow(2304,k,mod)%mod
        w=(6*k+1)*fs[2*k]*fs[3*k]*pow(denw,-1,mod)%mod
        s=(8*k+1)*fs[4*k]*pow(dens,-1,mod)%mod
        Lw=(Lw+w)%mod; Ls=(Ls+s)%mod
    assert Lw%p==Ls%p==0,(p,Lw,Ls)
    N=(3*p-1)//4+1
    j=N+1
    W,S=normalized(j,p)
    aj,bj=qmod(a(j),p),qmod(b(j),p)
    dj=(aj-bj)%p
    assert dj!=0,(p,j)
    if p not in (139,199,277):
        return None
    assert Lw==Ls==p,(p,Lw,Ls)
    uw,vs=Lw//p,Ls//p
    c0=((aj*vs*pow(S,-1,p))-(bj*uw*pow(W,-1,p)))*pow(dj,-1,p)%p
    c1=((uw*pow(W,-1,p))-(vs*pow(S,-1,p)))*pow(dj,-1,p)%p
    assert c0 or c1
    W2,S2=normalized(j+1,p)
    assert (c0*(W-S)+c1*(W2-S2))%p == (Lw-Ls)//p%p
    return p,N,j,Lw,Ls,W,S,dj,c0,c1

if __name__=='__main__':
    samples=[p for p in range(13,1000) if p%6==1 and isprime(p)]
    got=[r for p in samples if (r:=run(p)) is not None]
    assert len(samples)==79 and len(got)==3
    expected=[(139,105,106,139,139,84,121,134,130,29),
              (199,150,151,199,199,179,143,94,20,195),
              (277,208,209,277,277,175,133,94,175,218)]
    assert got==expected,(got,expected)
    print('79 original low-half sums checked modulo p^2; exactly three exceptional shifted Green ports certified:')
    for row in got:print(row)
    print('PASS')
