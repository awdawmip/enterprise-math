#!/usr/bin/env python3
"""R749SOY exact 7D Walsh zero-gap rectangle certificate.
Scientific pin: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389
Integer Bareiss + Fraction, exhaustive finite vertex certificate.
"""
from itertools import combinations
from fractions import Fraction as F
from math import comb
import json

MASKS=(3,12,15,1,2,4,8)
W=[tuple(1 if (k&m).bit_count()%2==0 else -1 for m in MASKS) for k in range(16)]
T0=F(1,4);T1=F(3,10);S0=F(3,5);S1=F(7,10)

def law(t,s,h=0,u=0,v=0,w=0,z=0):
    return tuple((1+sum((a*b for a,b in zip((t,s,h,u,v,w,z),row)),F(0)))/16 for row in W)
def tv(p,q):return sum((abs(a-b) for a,b in zip(p,q)),F(0))/2
def bound(t,s):return (3-t+s)/8

def solve(rows,rhs,idx):
    n=7;a=[list(rows[i])+[rhs[i]] for i in idx];den=1
    for j in range(n-1):
        piv=next((i for i in range(j,n) if a[i][j]),None)
        if piv is None:return None
        if piv!=j:a[j],a[piv]=a[piv],a[j]
        pv=a[j][j]
        for i in range(j+1,n):
            f=a[i][j]
            for k in range(j+1,n+1):
                z=a[i][k]*pv-f*a[j][k]
                assert z%den==0
                a[i][k]=z//den
            a[i][j]=0
        den=pv
    if a[-1][-2]==0:return None
    x=[F(0)]*n
    for j in range(n-1,-1,-1):
        x[j]=(F(a[j][n])-sum((a[j][k]*x[k] for k in range(j+1,n)),F(0)))/a[j][j]
    return tuple(x)

def lower_check():
    sign_corners=[]
    for t,s in ((t,s) for t in (T0,T1) for s in (S0,S1)):
        a=law(t,s,0,t,t,1-t,s)
        b=law(t,s,0,-t,-t,t-1,-s)
        assert min(a)>=0 and min(b)>=0 and sum(a)==sum(b)==1
        assert tv(a,b)==2*bound(t,s)
        sign_corners.append(tuple((x>y)-(x<y) for x,y in zip(a,b)))
    assert all(x*y>=0 for sg in sign_corners[1:] for x,y in zip(sign_corners[0],sg))
    return {'source_pair':'p(t,s,0,+/-t,+/-t,+/-(1-t),+/-s)',
            'pair_TV':'(3-t+s)/4','nonnegative_at_four_corners':True,
            'difference_signs_consistent':True}

def certificate():
    rows=list(W);rhs=[-1]*16
    rows.extend([(4,0,0,0,0,0,0),(-10,0,0,0,0,0,0),
                 (0,5,0,0,0,0,0),(0,-10,0,0,0,0,0)])
    rhs.extend([1,-3,3,-7])
    seen=set();nonsing=feasible=0
    for idx in combinations(range(20),7):
        y=solve(rows,rhs,idx)
        if y is None:continue
        nonsing+=1
        if any(sum((a*b for a,b in zip(row,y)),F(0))<b for row,b in zip(rows,rhs)):
            continue
        feasible+=1;seen.add(y)
    assert seen
    maxex=F(-1);tight=0;endpoints={}
    for v in seen:
        t,s=v[:2];source=law(*v);center=law(t,s)
        assert min(source)>=0 and sum(source)==1
        assert min(center)>=0 and sum(center)==1
        ex=tv(source,center)-bound(t,s)
        assert ex<=0,(str(t),str(s),str(ex))
        if ex==0:tight+=1
        if ex>maxex:maxex=ex
        key=f'{t}|{s}';endpoints[key]=endpoints.get(key,0)+1
    assert maxex==0
    return {'enumerated_seven_facet_bases':comb(20,7),'nonsingular_bases':nonsing,
            'feasible_bases_including_duplicates':feasible,'unique_exact_vertices':len(seen),
            'parameter_endpoints':endpoints,'tight_vertices':tight,
            'maximum_upper_excess':str(maxex)}

def main():
    return {'status':'PASS','research_id':'R749SOY',
      'frozen_scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
      'parameter_rectangle':'1/4<=t<=3/10, 3/5<=s<=7/10',
      'minimax':'rho=rho_cal=(3-t+s)/8',
      'calibrated_center':'p(t,s,0,0,0,0,0)','area':'1/200',
      'lower':lower_check(),'upper':certificate(),
      'all_real_parameter_proof':'complete exact joint-polytope vertices and convexity',
      'review':'AUTHOR_EXACT_NOT_REVIEWED','native_X6':'OPEN'}
if __name__=='__main__':print(json.dumps(main(),sort_keys=True,indent=2))
