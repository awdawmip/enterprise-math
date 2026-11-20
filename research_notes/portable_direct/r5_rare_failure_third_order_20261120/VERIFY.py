#!/usr/bin/env python3
"""R5 third rare-witness failure coefficient; integer and Laurent crosscheck."""
from fractions import Fraction
from itertools import combinations_with_replacement
from math import comb
import hashlib, json, sys, zipfile

A=tuple(range(214,219))
Q=tuple(range(219,315))
s=sum(Q); t=sum(x*x for x in Q)
r=sum(A); v=sum(x*x for x in A)
assert (s,t,r,v)==(25584,6891856,1080,233290)

def choose(n,k): return comb(n,k) if n>=k else 0

def moments(m):
    count=total=total2=0
    for n in range(m):
        for block in combinations_with_replacement(A,n):
            x=sum(block)
            count+=1
            total+=x
            total2+=x*x
    return count,total,total2

def coefficients(m):
    b,c,d,h=[choose(m+4,5),choose(m+4,6),choose(m+4,7),choose(m+6,7)]
    small=(Fraction(s*s,8)-Fraction(t,24))*b-Fraction(s*r*c,2)+Fraction(d*(r*r+v)+c*v,2)
    other=Fraction(219*220*221*h,214)+Fraction(219*220*221*h,215)
    return b,Fraction(s*b,2)-r*c,small,other,small+other

def laurent_independent(m):
    # z=1-q, 1/(1-(1-z)^k)=(k*z)^-1[1+(k-1)z/2+(k^2-1)z^2/12+...]
    b,c1,c2=moments(m)
    alphas=[Fraction(k-1,2) for k in Q]
    e1=sum(alphas, Fraction(0))
    e2=sum((Fraction(k*k-1,12) for k in Q),Fraction(0))
    e2+=(e1*e1-sum((u*u for u in alphas),Fraction(0)))/2
    h95=sum(range(1,96))
    pair95=Fraction(h95*h95-sum(i*i for i in range(1,96)),2)
    h94=sum(range(1,95))
    t1=b*e1-c1
    t2=b*e2-e1*c1+Fraction(c2-c1,2)
    return Fraction(b*pair95,95*94)+Fraction(t1*h94,94)+t2

def verify(archive=None):
    if archive:
        with zipfile.ZipFile(archive) as z:
            raw=z.read('EXACT_R5_ALL_101_BUDGETS.json')
            assert hashlib.sha256(raw).hexdigest()=='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
            assert json.loads(raw)['budget_range']==[214,314]
    samples={}
    for m in [1,2,3,8,17]:
        b,c,d,h=[choose(m+4,5),choose(m+4,6),choose(m+4,7),choose(m+6,7)]
        n,c1,c2=moments(m)
        assert n==b and c1==r*c and c2==d*(r*r+v)+c*v
        first,second,small,other,total=coefficients(m)
        assert small==laurent_independent(m)
        assert other==Fraction(219*220*221*h,215)+Fraction(219*220*221*h,214)
        samples[str(m)]={"N95_num":str(first),"N94_num":str(second),
            "N93_small":str(small),"N93_seven":str(other),
            "N93_total":str(total),"S0_failure_vectors":n}
    return {"schema":"EM_R5_THIRD_FAILURE_ORDER_V1",
        "status":"AUTHOR_EXACT_SYMBOLIC_CHECK_NOT_REVIEWED",
        "frozen_input_sha256":"50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b",
        "archive_sha_verified":bool(archive),"samples":samples,
        "meaning":"all N93 numerators have common denominator 93! * prod(219..314)"}

if __name__=="__main__":
    print(json.dumps(verify(sys.argv[1] if len(sys.argv)>1 else None),indent=2))
