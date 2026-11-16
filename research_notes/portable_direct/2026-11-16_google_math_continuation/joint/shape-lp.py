"""Exact minimum infinity separation of all globally-translated template rays,
for any individual |gain|>=1 and known positive / unknown signs.
Enumerates feasible basic optima of a rational LP, with no numerical solver.
"""
from fractions import Fraction as F
from itertools import combinations
from math import gcd
from functools import reduce
G=(20,20,20,-100,140,-100)
def dist(U,V,sgn):
    # At minimum one of two absolute gains is 1, by homogeneity.
    # Anchor U at gain 1 and minimize R=range(U-t*sgn*V)
    # over t>=1; or swap U and V. One convex PL function in 1 variable.
    def anchor(U,V):
        lines=[(U[i]-U[j],sgn*(V[j]-V[i])) for i in range(len(U)) for j in range(len(U))]
        candidates={F(1)}
        for (a,b),(c,d) in combinations(lines,2):
            if b!=d:
                t=F(a-c,d-b)
                if t>=1:candidates.add(t)
        def obj(t):return max(a+b*t for a,b in lines)/2
        return min((obj(t),t) for t in candidates)
    return min((d,t,order) for order,(d,t) in enumerate((anchor(U,V),anchor(V,U))))
def keys(k,pm=False):
    groups={}
    for a in range(6):
        vals=[G[(a+j)%6]-G[a] for j in range(k)]
        z=reduce(gcd,vals,0)
        if pm and next((v for v in vals if v),1)<0:z=-z
        key=tuple(x//z if z else 0 for x in vals)
        groups.setdefault(key,[]).append(a)
    return groups
def window(k):
    s=[tuple(G[(a+j)%6] for j in range(k)) for a in range(6)]
    for signs in [(1,), (1,-1)]:
        allleft=[]
        for a,b in combinations(range(6),2):
            d,t,rev,sgn=min((*dist(s[a],s[b],q),q) for q in signs)
            allleft.append((d,a,b,t,rev,sgn))
        m=min(x[0] for x in allleft)
        print(k,signs,m,[x[1:] for x in allleft if x[0]==m])
if __name__=='__main__':
    for k in range(1,7):window(k)
    for signs in (False,True):
        assert len(keys(3,pm=signs))==6
        assert len(keys(2,pm=signs))<6
    print("PASS six-phase classification")
