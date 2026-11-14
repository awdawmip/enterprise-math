#!/usr/bin/env python3
"""R749SNY: exact author-side 16-state Walsh minimax triangle certificate.
Frozen input awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389
Stdlib Fraction + integer Bareiss, enumerate every 7-facet active basis.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
import json
MASKS=(3,12,15,1,2,4,8)
ROWS=tuple(tuple(1 if (m&x).bit_count()%2==0 else -1 for m in MASKS) for x in range(16))
CORNER=((F(0),F(0)),(F(1),F(0)),(F(2,5),F(1,5)))

def law(t,s,h=F(0),u=F(0),v=F(0),w=F(0),z=F(0)):
    coeff=(t,s,h,u,v,w,z)
    return tuple((1+sum((a*b for a,b in zip(row,coeff)),F(0)))/16 for row in ROWS)

def tv(a,b):
    return sum((abs(x-y) for x,y in zip(a,b)),F(0))/2

def solve(A,b,indices,n=7):
    M=[list(A[i])+[b[i]] for i in indices]
    last=1
    for j in range(n-1):
        k=next((k for k in range(j,n) if M[k][j]),None)
        if k is None: return None
        if k!=j: M[j],M[k]=M[k],M[j]
        pivot=M[j][j]
        for i in range(j+1,n):
            c=M[i][j]
            for k in range(j+1,n+1):
                z=M[i][k]*pivot-c*M[j][k]
                assert z%last==0
                M[i][k]=z//last
            M[i][j]=0
        last=pivot
    if M[n-1][n-1]==0: return None
    x=[F(0)]*n
    for j in range(n-1,-1,-1):
        x[j]=(F(M[j][n])-sum((M[j][k]*x[k] for k in range(j+1,n)),F(0)))/M[j][j]
    return tuple(x)

def run():
    # y=5(t,s,h,u,v,w,z). Source mass nonnegativity and 3 triangle facets.
    A=list(ROWS)+[(0,1,0,0,0,0,0),(1,-2,0,0,0,0,0),(-1,-3,0,0,0,0,0)]
    b=[-5]*16+[0,0,-5]
    stat=dict(active_bases=0,nonsingular_bases=0,feasible_bases=0,distinct_vertices=0,tight_vertices=0,violations=0,max_excess='')
    seen=set()
    for ix in combinations(range(19),7):
        stat['active_bases']+=1
        raw=solve(A,b,ix)
        if raw is None: continue
        stat['nonsingular_bases']+=1
        if any(sum((ai*yi for ai,yi in zip(row,raw)),F(0))<rhs for row,rhs in zip(A,b)): continue
        stat['feasible_bases']+=1
        seen.add(tuple(z/5 for z in raw))
    stat['distinct_vertices']=len(seen)
    biggest=F(-1)
    for t,s,h,u,v,w,z in seen:
        mu=law(t,s,h,u,v,w,z)
        q=law(t,s)
        assert min(mu)>=0 and min(q)>=0
        gap=tv(mu,q)-(1-s)/2
        biggest=max(biggest,gap)
        stat['tight_vertices']+=int(gap==0)
        stat['violations']+=int(gap>0)
    stat['max_excess']=str(biggest)
    assert stat['active_bases']==comb(19,7)==50388
    assert biggest==0 and len(seen)>0
    for t,s in CORNER:
        q=law(t,s)
        p1=law(t,s,-s,1-s,t+s,0,0)
        p2=law(t,s,-s,-(1-s),-(t+s),0,0)
        assert min(q)>=0 and min(p1)>=0 and min(p2)>=0
        assert tv(p1,p2)==1-s
    return {'research_unit':'R749SNY','status':'PASS','scientific_input_commit':'a72226e2430ffa4786321ac86e7f0c599d5f0389','domain':'s>=0, t>=2s, t+3s<=1 (entire real triangle)','vertices':[list(map(str,v)) for v in CORNER],'area':'1/10','exact_formula':'rho(t,s)=rho_cal(t,s)=(1-s)/2','center':'(1+t*chi_3+s*chi_12)/16','lower_pair':'h=-s, (u,v)=+/- (1-s,t+s), w=z=0','verified_exhaustive_joint_polytope':stat,'independent_review':'NOT_REVIEWED'}

if __name__=='__main__':print(json.dumps(run(),ensure_ascii=False,sort_keys=True,indent=2))
