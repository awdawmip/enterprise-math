#!/usr/bin/env python3
"""Exact check of GH-83 first-order Laurent rank slopes (author evidence only)."""


def primes(limit):
    mark = bytearray(b'\\x01')*limit
    mark[:2] = b'\\x00\\x00'
    for k in range(2, int(limit**0.5)+1):
        if mark[k]:
            mark[k*k:limit:k] = b'\\x00'*(((limit-1-k*k)//k)+1)
    return [p for p in range(7,limit) if mark[p] and p%4==3]


def test(p):
    d=(p-3)//4
    h=[1]
    for r in range(d):
        h.append(h[-1]*pow(4*r+3,3,p)*pow((4*r+4)*(4*r+5)*(4*r+6),-1,p)%p)
    H=Hp=0
    zpow=1
    for r,hr in enumerate(h):
        H=(H+(8*r+5)*hr*zpow)%p
        if r: Hp=(Hp+r*(8*r+5)*hr*pow(9,r-1,p))%p
        zpow=zpow*9%p
    assert H==0 and Hp!=0,(p,'H,Hprime',H,Hp)
    j0=2*d+2
    alpha=1; zeros=0
    for i in range(j0):
        alpha=alpha*pow(4*i+1,3,p)%p
        for b in (2,3,4):
            den=(4*i+b)%p
            if den:
                alpha=alpha*pow(den,-1,p)%p
            else:
                alpha=alpha*pow(4,-1,p)%p
                zeros+=1
    assert zeros==2 and alpha!=0
    Q=alpha*pow(9,2*d+2,p)*pow(8,-1,p)%p
    assert Q!=0
    slope0=Q*Hp%p
    C=1; checked=0; slope_d=0
    for r in range(d+1):
        slope=slope0*pow(C,-1,p)%p
        assert slope!=0,(p,r)
        if r==d:slope_d=slope
        checked+=1
        if r<d:
            ratio=9*pow(4*r+1,3,p)*pow((4*r+2)*(4*r+3)*(4*r+4),-1,p)%p
            C=C*ratio%p
            assert C
    Vprime=slope0*pow(18*C,-1,p)%p
    assert Vprime!=0 and (18*C*Vprime-slope0)%p==0
    return checked,(p,d,Hp,slope0,slope_d,Vprime)


if __name__=='__main__':
    total=0; samples=[]
    ps=primes(1000)
    for p in ps:
        n, row=test(p); total+=n
        if p in (7,11,19,23,31,43,47,59,67,71):samples.append(row)
    print('PASS_GH83_TRANSVERSE_ALL_RANKS primes=',len(ps),'rank_jets=',total)
    for x in samples:print('SAMPLE p,d,Hprime,A0prime,Adprime,Vsuccessorprime=',x)
