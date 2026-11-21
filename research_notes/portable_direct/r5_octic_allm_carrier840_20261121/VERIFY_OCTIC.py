#!/usr/bin/env python3
"""Exact primitive-eighth-root coefficient certificate for frozen R5.
Ring Q[z]/(z^4+1); no floating point or external dependencies.
"""
from fractions import Fraction as Q
from functools import lru_cache
from collections import defaultdict
from itertools import combinations
import json

ZERO=(Q(0),)*4
ONE=(Q(1),Q(0),Q(0),Q(0))

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)
def sub(a,b): return add(a,neg(b))
def scale(a,k): return tuple(k*x for x in a)
def mul(a,b):
    v=[Q(0)]*4
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            v[(i+j)%4]+=(-1 if i+j>=4 else 1)*x*y
    return tuple(v)

@lru_cache(None)
def zpow(k):
    k%=8
    return tuple(Q((-1 if k>=4 else 1) if j==k%4 else 0) for j in range(4))

def inv_1_minus_z(k):
    assert k%8 != 0
    # (1-q)*sum_{j=0}^7 j*q^j=-8, for q^8=1 != q.
    out=ZERO
    for j in range(1,8):out=add(out,scale(zpow(k*j),j))
    return scale(out,Q(-1,8))

def series(limit):
    blank=lambda: [ZERO]*limit
    def plus(a,b): return [add(x,y) for x,y in zip(a,b)]
    def minus(a,b): return [sub(x,y) for x,y in zip(a,b)]
    def product(a,b):
        out=blank()
        for i,x in enumerate(a):
            if x==ZERO:continue
            for j in range(limit-i):
                if b[j]!=ZERO:out[i+j]=add(out[i+j],mul(x,b[j]))
        return out
    def times(a,x):return [mul(v,x) for v in a]
    def geo(x,step=1):
        out=blank();out[0]=ONE
        for i in range(step,limit):out[i]=mul(out[i-step],x)
        return out
    def tail(x,step=1):
        v=geo(x,step);v[0]=ZERO;return v
    identity=[ONE]+[ZERO]*(limit-1)
    one_minus_t=[ONE,neg(ONE)]+[ZERO]*(limit-2)
    X,Y=zpow(6),zpow(7)
    common=product(product(geo(ONE),geo(ONE)),product(geo(zpow(1)),geo(zpow(2))))
    fsum=blank()
    for j in (3,4,5):
        Z=zpow(j)
        residue=ONE
        for ell in (3,4,5):
            if ell!=j:residue=mul(residue,inv_1_minus_z(ell-j))
        constant=ZERO
        for k,V in ((6,X),(7,Y),(j,Z)):
            constant=add(constant,mul(V,inv_1_minus_z(k)))
        pair=plus(plus(tail(mul(X,Y)),tail(mul(X,Z))),tail(mul(Y,Z)))
        triple=tail(mul(mul(X,Y),Z),2)
        numerator=plus(identity,product(plus(times(identity,constant),minus(triple,pair)),one_minus_t))
        denominator_inv=product(product(geo(X),geo(Y)),geo(Z))
        fsum=plus(fsum,times(product(numerator,denominator_inv),residue))
    return product(common,fsum)

S=[set(range(214,219)), {214,*range(216,222)},set(range(215,222))]
def independent_dp(m):
    total=ZERO
    for n in (1,2,3):
        for chosen in combinations(range(3),n):
            union=set().union(*(S[i] for i in chosen))
            free=set(range(214,222))-union
            prefactor=ONE
            for p in free:prefactor=mul(prefactor,inv_1_minus_z(p))
            states={(0,)*n:ONE}
            for p in sorted(union):
                members=[i for i,idx in enumerate(chosen) if p in S[idx]]
                new=defaultdict(lambda:ZERO)
                for loads,weight in states.items():
                    bound=min(m-loads[j] for j in members)
                    for k in range(bound):
                        after=tuple(x+(k if j in members else 0) for j,x in enumerate(loads))
                        new[after]=add(new[after],mul(weight,zpow(p*k)))
                states=new
            subtotal=ZERO
            for w in states.values(): subtotal=add(subtotal,w)
            total=add(total,scale(mul(prefactor,subtotal),(-1)**(n+1)))
    return total

def fmt(a): return [str(v) for v in a]

def main():
    L=series(80)
    # Independent DP uses event intersections, not the max-formula.
    for m in range(1,13):assert L[m-1]==independent_dp(m),m
    # Finite regression of analytic denominator (1-t^16)^2.
    for i in range(32,len(L)):
        assert L[i]==sub(scale(L[i-16],2),L[i-32]),i
    # One basis coordinate witnesses nonvanishing for each residue.
    cert=[]
    for r in range(1,17):
        c=L[r-1]; b=sub(L[r+15],c)
        found=next((j for j in range(4) if c[j] and b[j] and c[j]*b[j]>0),None)
        assert found is not None,(r,c,b)
        cert.append(dict(r=r,basis_power=found,constant=str(c[found]),increment=str(b[found])))
    # Unique primitive-16 parameter pole: j=4, 1-z*t^2.
    assert [(j,(13+j)%8) for j in (3,4,5)]==[(3,0),(4,1),(5,2)]
    out={"status":"PASS","field":"Q[z]/(z^4+1)",
         "model":"frozen scalar nonadaptive R5; local prices 214..221; free eighth multiples 224..312",
         "m1_to_32_coefficients":[fmt(v) for v in L[:32]],
         "nonzero_witness_mod16":cert,
         "independent_dp_m":list(range(1,13)),
         "recurrence_checked_m":list(range(1,49)),
         "formal_admission":"NOT_REVIEWED"}
    print(json.dumps(out,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
