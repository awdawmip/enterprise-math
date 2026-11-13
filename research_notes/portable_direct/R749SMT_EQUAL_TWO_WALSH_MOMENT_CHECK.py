#!/usr/bin/env python3
"""Exact rational finite certificate for R749SMT equal-two-coordinate Walsh fibers."""
from fractions import Fraction as F
from itertools import combinations
import json

C=(1,2,4,8,15)
B=tuple(a for a in range(1,16) if a not in C)

def chi(a,x): return 1 if (a&x).bit_count()%2==0 else -1

def two_rhs_solve(mat,r0,r1):
    n=len(r0); z=[[F(a) for a in row]+[F(r0[i]),F(r1[i])] for i,row in enumerate(mat)]
    for j in range(n):
        k=next((k for k in range(j,n) if z[k][j]!=0),None)
        if k is None:return None
        z[j],z[k]=z[k],z[j]
        d=z[j][j];z[j]=[e/d for e in z[j]]
        for k in range(n):
            if k==j:continue
            d=z[k][j]
            if d:z[k]=[a-d*b for a,b in zip(z[k],z[j])]
    return [(z[i][-2],z[i][-1]) for i in range(n)]

def bounds(aff,lo,hi):
    for a,b in aff:
        if b>0:lo=max(lo,-a/b)
        elif b<0:hi=min(hi,-a/b)
        elif a<0:return None
        if hi<lo:return None
    return (lo,hi)

def q_c(t):
    z=max(F(0),2*abs(t)-1)
    return [(1+t*chi(1,x)+t*chi(2,x)+z*chi(3,x))/16 for x in range(16)]

def q_b(t):
    return [(1+t*chi(3,x)+t*chi(5,x))/16 for x in range(16)]

def tv(x,y):return sum(abs(a-b) for a,b in zip(x,y))/2

def target_c(t):return F(3,4)*min(F(1),2-2*abs(t))

def verify_case(kind):
    if kind=='C':
        rows=[[1]*16]+[[chi(a,x) for x in range(16)] for a in C]
        dim=6; partitions=[(F(-1),F(-1,2)),(F(-1,2),F(1,2)),(F(1,2),F(1))]
    else:
        dim=5; partitions=[(F(-1,2),F(1,2))]
        rows=[[chi(a,x) for a in C] for x in range(16)]
    totals={'bases_enumerated':0,'nonsingular':0,'feasible_intervals':0,'endpoints':0,'max_excess':'0','distinct_endpoints':set()}
    for inds in combinations(range(16),dim):
        totals['bases_enumerated']+=1
        if kind=='C':
            M=[[rows[i][j] for j in inds] for i in range(dim)]
            sol=two_rhs_solve(M,[1,0,0,0,0,0],[0,1,1,0,0,0])
            if sol is None:continue
            aff=[(F(0),F(0)) for _ in range(16)]
            for i,idx in enumerate(inds):aff[idx]=sol[i]
        else:
            M=[rows[j] for j in inds]
            sol=two_rhs_solve(M,[-1]*5,[-chi(3,j)-chi(5,j) for j in inds])
            if sol is None:continue
            aff=[]
            for x in range(16):
                aa=F(1)+sum(s0*chi(a,x) for (s0,s1),a in zip(sol,C))
                bb=F(chi(3,x)+chi(5,x))+sum(s1*chi(a,x) for (s0,s1),a in zip(sol,C))
                aff.append((aa/16,bb/16))
        totals['nonsingular']+=1
        for lo,hi in partitions:
            interval=bounds(aff,lo,hi)
            if interval is None:continue
            totals['feasible_intervals']+=1
            for t in set(interval):
                p=[a+b*t for a,b in aff]
                assert sum(p)==1 and min(p)>=0
                U=C if kind=='C' else B
                for a in U:
                    assert sum(p[x]*chi(a,x) for x in range(16))==(t if a in ( (1,2) if kind=='C' else (3,5)) else 0)
                q=q_c(t) if kind=='C' else q_b(t)
                assert sum(q)==1 and min(q)>=0
                value=tv(p,q)
                goal=target_c(t) if kind=='C' else F(1,2)
                if value>goal:raise AssertionError(f'{kind} TV fail {inds} {t} {value} > {goal}')
                totals['endpoints']+=1
                totals['distinct_endpoints'].add(str(t))
    totals['distinct_endpoints']=sorted(totals['distinct_endpoints'],key=lambda x:F(x))
    return totals

if __name__=='__main__':
    output={'schema':'R749SMT_EXACT_EQUAL_TWO_CHARACTER_FIBERS_V1','status':'PASS','method':'exhaustive rational basic-feasible-source/active-set parameter interval enumeration; convexity of TV on affine pieces','C':verify_case('C'),'B_adjacent_pair':verify_case('B'),'boundary':'C exact upper certificate for all real -1<=t<=1; B adjacent-pair exact upper certificate for all real -1/2<=t<=1/2; lower bounds proved in manuscript; no native V29/V39 event claimed'}
    print(json.dumps(output,indent=2,ensure_ascii=False))
