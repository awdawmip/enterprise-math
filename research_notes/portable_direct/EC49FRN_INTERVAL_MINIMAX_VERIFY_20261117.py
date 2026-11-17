#!/usr/bin/env python3
"""EC49FRN: rational interval-prior minimax theorem tests, frozen original BRC."""
from fractions import Fraction as F
from itertools import product

# (U_R,U_T,M_R,M_T) from inherited EC49FRL native named-state tree replay
T={"A":(6,290,6,751),"B":(5,293,5,704),"C":(5,295,5,685),
   "D":(4,296,4,707),"E":(4,298,4,688)}
BETA=F(620,3299)

def cost(n,x,l):
    ur,ut,mr,mt=T[n]
    return (1-l)*F(ut+x*ur,141)+l*F(mt+x*mr,310)

def value(x,l):
    return min(cost(n,x,l) for n in T)

def slope(n,x):
    return cost(n,x,F(1))-cost(n,x,F(0))

def alpha(x):
    if x>=3: return F(0)
    return F(3-x,141)/(F(3-x,141)+F(x+47,310))

def optimal_interval_policy(x,a,b):
    assert x>=1 and 0<=a<b<=1
    va,vb=value(x,a),value(x,b)
    s=(vb-va)/(b-a)
    knots={a,b}
    for k in (alpha(x),BETA):
        if a<k<b: knots.add(k)
    def gap(k): return value(x,k)-(va+(k-a)*s)
    k=max(sorted(knots),key=gap)
    r=gap(k)
    assert r>=0
    if r==0:
        trees=[n for n in T if cost(n,x,a)==va and cost(n,x,b)==vb]
        assert trees
        return {trees[0]:F(1)},r,k
    active=[n for n in T if cost(n,x,k)==value(x,k)]
    lo=min(active,key=lambda n:slope(n,x))
    hi=max(active,key=lambda n:slope(n,x))
    sl,sh=slope(lo,x),slope(hi,x)
    assert sl<=s<=sh and sl<sh
    q=(s-sl)/(sh-sl)
    p={hi:q,lo:1-q}
    assert all(F(0)<=v<=F(1) for v in p.values())
    return p,r,k

def main():
    xs=[F(1),F(3,2),F(2),F(11,4),F(3),F(7,2),F(10)]
    intervals=[(F(0),F(1)),(F(0),F(1,8)),(F(1,10),F(3,10)),
       (F(0),F(1,3)),(F(1,4),F(1,2)),(F(0),F(1,20)),
       (F(1,10),F(1,5)),(F(1,6),F(1,4)),(F(1,5),F(1)),
       (F(0),BETA),(BETA,F(1)),(F(1,25),F(1,4))]
    checked=0
    for x,(a,b) in product(xs,intervals):
        p,r,k=optimal_interval_policy(x,a,b)
        assert sum(p.values())==1
        for l in (a,b):
            reg=sum(w*cost(n,x,l) for n,w in p.items())-value(x,l)
            assert reg==r,(x,a,b,k,reg,r)
        for l in (a,(3*a+b)/4,(a+b)/2,(a+3*b)/4,b):
            reg=sum(w*cost(n,x,l) for n,w in p.items())-value(x,l)
            assert reg<=r,(x,a,b,l,reg,r)
        if x>=3 and a<BETA<b:
            kappa=F(2,141)+F(19,310)
            assert r==kappa*(BETA-a)*(b-BETA)/(b-a)
        checked+=1
    print("EXACT_INTERVAL_TESTS_PASSED",checked,"rational input triples")

if __name__=="__main__": main()
