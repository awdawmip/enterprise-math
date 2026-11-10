#!/usr/bin/env python3
"""D25 W216 p^5 cubic-Newton countercertificate, original signed blocks.
Two independently coded exact arithmetic paths; author-side, unreviewed.
"""
from math import comb

def split_factor(n, p):
    v=0
    while n%p==0:
        n//=p
        v+=1
    return v,n

def direct_blocks(p):
    mod=p**5
    ib=pow(216,-1,mod)
    power=1
    sums=[0]*4
    anch=[]
    for k in range(4*p):
        a=comb(2*k,k)**2*comb(3*k,k)*power%mod
        if k<4: anch.append(a)
        sums[k//p]=(sums[k//p]+(6*k+1)*a)%mod
        power=power*ib%mod
    assert all(x%p for x in anch)
    return [sums[j]*pow(anch[j],-1,mod)%mod for j in range(4)]

def valuation_unit_blocks(p):
    mod=p**5
    v=0; unit=1; inv36=pow(36,-1,mod)
    sums=[0]*4; anch=[]
    for k in range(4*p):
        a=(p**v*unit)%mod if v<5 else 0
        if k<4: anch.append(a)
        sums[k//p]=(sums[k//p]+(6*k+1)*a)%mod
        if k==4*p-1: break
        for x in (2*k+1,3*k+1,3*k+2):
            e,y=split_factor(x,p)
            v+=e; unit=unit*y%mod
        e,y=split_factor(k+1,p)
        v-=3*e
        assert v>=0
        unit=unit*inv36*pow(y,-3,mod)%mod
    assert all(x%p for x in anch)
    return [sums[j]*pow(anch[j],-1,mod)%mod for j in range(4)]

def exact_witness(p):
    mod=p**5
    c=direct_blocks(p)
    assert c==valuation_unit_blocks(p),p
    q2=(c[2]-2*c[1]+c[0])%mod
    q3=(c[3]-3*c[2]+3*c[1]-c[0])%mod
    defect=(q3-2*q2)%mod
    assert defect%(p**4)==0
    return {"p":p,"p5":mod,"C":c,"q2":q2,"q3":q3,
            "defect":defect,"defect_div_p4":defect//p**4}

if __name__=="__main__":
    expected={13:6,19:14,37:14,43:27,73:33,373:89}
    for p,c in expected.items():
        w=exact_witness(p)
        assert w["defect_div_p4"]==c,(w,c)
        print(w)
    print("PASS: p=13 and p=19 disprove universal q3=2q2 modulo p^5.")
