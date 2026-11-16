"""Exact region where all six fourth-difference codewords decode after A*s+b.

Uses complete two-dimensional rational line arrangement, testing every
two-dimensional cell, every open edge, and every vertex, including unbounded
pieces. Python standard library.
"""
from fractions import Fraction as Q
from itertools import product,combinations
from math import gcd,lcm
from pathlib import Path
import json

S=((0,0,0),(0,0,-1),(0,-1,1),(-1,1,-1),(1,-1,0),(-1,0,0))
def predicted(A,b):
    return ((Q(1,2)<A<2 and Q(-1,2)<b<min(A-Q(1,2),A/2))
         or (A>=2 and A/2-1<b<A/2))
def bad(A,b):
    den=lcm(A.denominator,b.denominator)
    v,t=int(A*den),int(b*den)
    res=[]
    for a,c in enumerate(S):
        Y=[v*x+t for x in c]
        actual=max(abs(x-den*z) for x,z in zip(Y,c))
        for k,ck in enumerate(S):
            if k==a:continue
            rival=max(abs(x-den*z) for x,z in zip(Y,ck))
            if rival<=actual:
                res.append((a,k,'tie' if rival==actual else 'strict'))
    return res
def canonical(p):
    d=gcd(*p)
    p=tuple(c//d for c in p)
    return p if next(c for c in p if c)>0 else tuple(-c for c in p)
def strata(values):
    v=sorted(set(values));return [v[0]-1]+[x for a,b in zip(v,v[1:]) for x in (a,(a+b)/2)]+[v[-1],v[-1]+1]
def main():
    signed={(h*x,h,-h*y) for x,y,h in product((-1,0,1),(-1,0,1),(-1,1))}
    lines={canonical(tuple(a-b for a,b in zip(f,g))) for f,g in combinations(signed,2) if f[:2]!=g[:2]}
    # Add the boundary of proposed closed-form expression, so both predicates
    # have constant truth over every stratum sampled below.
    lines.update(((1,0,0),(2,0,-1),(1,0,-1),(1,0,-2),(0,2,1),
                  (2,-2,-1),(1,-2,0),(1,-2,-2)))
    xcrit={Q(-c,a) for a,b,c in lines if b==0}
    def eval_y(L,A):a,b,c=L;return -(a*A+c)/b
    for (a,b,c),(u,v,w) in combinations(lines,2):
        det=a*v-u*b
        if det:xcrit.add(Q(b*w-c*v,det))
    count=0
    for A in strata(xcrit):
        if A<=0:continue
        yc={eval_y(L,A) for L in lines if L[1]}
        for b in strata(yc):
            if predicted(A,b)!= (not bad(A,b)):
                raise AssertionError((A,b,predicted(A,b),bad(A,b)))
            count+=1
    print('Complete arrangement verified',len(lines),'lines,',count,'strata representatives')
    for A in (Q(3,4),Q(1),Q(3,2),Q(2),Q(3)):
        lo=Q(-1,2) if A<2 else A/2-1
        hi=min(A-Q(1,2),A/2)
        print('boundary',A,lo,bad(A,lo),hi,bad(A,hi))
if __name__=='__main__':main()
