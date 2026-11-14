#!/usr/bin/env python3
"""R749SOZ: exact triangular zero-gap Walsh certificate.
Frozen scientific source: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389
Pure Python standard library, exact rational arithmetic, no floating-point proof step.
"""
from itertools import combinations
from fractions import Fraction as F
from math import comb
import hashlib,json

MASKS=(3,12,15,1,2,4,8)
W=[tuple(1 if (k&m).bit_count()%2==0 else -1 for m in MASKS) for k in range(16)]
PARAM_VERTICES=((F(3,10),F(1,2)),(F(2,5),F(3,5)),(F(0),F(1)))

def law(t,s,h=0,u=0,v=0,w=0,z=0):
    c=(t,s,h,u,v,w,z)
    return tuple((1+sum((x*y for x,y in zip(c,r)),F(0)))/16 for r in W)

def tv(x,y):return sum((abs(a-b) for a,b in zip(x,y)),F(0))/2

def R(t,s):return (3-t+s)/8

def solve(rows,rhs,idx):
    n=7; a=[list(rows[i])+[rhs[i]] for i in idx];den=1
    for j in range(n-1):
        piv=next((i for i in range(j,n) if a[i][j]),None)
        if piv is None:return None
        if piv!=j:a[j],a[piv]=a[piv],a[j]
        pv=a[j][j]
        for i in range(j+1,n):
            f=a[i][j]
            for k in range(j+1,n+1):
                zz=a[i][k]*pv-f*a[j][k]
                assert zz%den==0
                a[i][k]=zz//den
            a[i][j]=0
        den=pv
    if a[-1][-2]==0:return None
    x=[F(0)]*n
    for j in range(n-1,-1,-1):
        x[j]=(F(a[j][n])-sum((a[j][k]*x[k] for k in range(j+1,n)),F(0)))/a[j][j]
    return tuple(x)

def lower_pair():
    data=[]; signs=[]
    for t,s in PARAM_VERTICES:
        p1=law(t,s,0,t,t,1-t,s)
        p2=law(t,s,0,-t,-t,t-1,-s)
        assert min(p1)>=0 and min(p2)>=0
        assert sum(p1)==sum(p2)==1
        assert tv(p1,p2)==(3-t+s)/4
        signs.append(tuple((a>b)-(a<b) for a,b in zip(p1,p2)))
        data.append({'parameter':[str(t),str(s)],'source_tv':str(tv(p1,p2))})
    assert all(x*y>=0 for base in signs for sg in signs for x,y in zip(base,sg))
    return {'parameter_corners':data,'sign_consistent_at_all_corners':True,
            'TV_pair':'(3-t+s)/4','half_diameter':'(3-t+s)/8'}

def certificate():
    rows=list(W);rhs=[-1]*16
    # 5*t+3*s>=3, s-t>=1/5, t+s<=1.
    rows.extend([(5,3,0,0,0,0,0),(-5,5,0,0,0,0,0),(-1,-1,0,0,0,0,0)])
    rhs.extend([3,1,-1])
    seen=set();nonsingular=feasible=0
    for idx in combinations(range(19),7):
        y=solve(rows,rhs,idx)
        if y is None:continue
        nonsingular+=1
        if any(sum((a*b for a,b in zip(row,y)),F(0))<b for row,b in zip(rows,rhs)):
            continue
        feasible+=1;seen.add(y)
    assert seen
    mx=F(-1); tight=0; endpoints={}
    for x in sorted(seen):
        t,s=x[:2];p=law(*x);q=law(t,s)
        assert min(p)>=0 and sum(p)==1 and min(q)>=0 and sum(q)==1
        delta=tv(p,q)-R(t,s)
        assert delta<=0,(str(t),str(s),str(delta),[str(z) for z in x])
        if delta==0:tight+=1
        mx=max(mx,delta)
        key=f'{t}|{s}';endpoints[key]=endpoints.get(key,0)+1
    assert mx==0
    return {'seven_active_facet_bases':comb(19,7),'nonsingular_bases':nonsingular,
        'feasible_bases_with_multiplicity':feasible,'distinct_vertices':len(seen),
        'tight_vertices':tight,'max_risk_excess':str(mx),'parameter_vertex_counts':endpoints,
        'joint_polytope_dimension':7}

def main():
    return {'status':'PASS','research_id':'R749SOZ','frozen_scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
      'parameter_triangle_vertices':[[str(x),str(y)] for x,y in PARAM_VERTICES],
      'parameter_constraints':'5*t+3*s>=3; 5*(s-t)>=1; t+s<=1',
      'area':'1/25','radii':'rho=rho_cal=(3-t+s)/8','center':'p(t,s,0,0,0,0,0)',
      'lower':lower_pair(),'upper':certificate(),
      'universal_real_parameter_argument':'joint affine source polytope vertex enumeration plus convexity; affine diameter pair with consistent signs',
      'review':'AUTHOR_EXACT_NOT_REVIEWED','native_correspondence':'OPEN'}
if __name__=='__main__':
    print(json.dumps(main(),ensure_ascii=False,sort_keys=True,indent=2))
