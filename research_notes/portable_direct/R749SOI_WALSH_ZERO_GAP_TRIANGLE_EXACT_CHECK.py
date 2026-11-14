#!/usr/bin/env python3
"""R749SOI exact joint-polytope certificate, stdlib only; 2026-11-14.
Science frozen at awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb
import json

PIN='a72226e2430ffa4786321ac86e7f0c599d5f0389'
MASKS=(3,12,15,1,2,4,8)
ROWS=tuple(tuple(1 if (mask & k).bit_count()%2==0 else -1 for mask in MASKS) for k in range(16))
# joint variables (t,s,h,u,v,w,z), row*variables>=bound
N=7
RESTRICTIONS=tuple(ROWS)+(( -1, 0, 0, 0, 0, 0, 0), (1,1,0,0,0,0,0),(3,-2,0,0,0,0,0))
BOUNDS=(-1,)*16+(-1,1,1)

def exact_solve(rowset, boundset, inds):
    n=len(inds)
    a=[list(rowset[i])+[boundset[i]] for i in inds]
    den=1
    for c in range(n-1):
        pivot_index=next((r for r in range(c,n) if a[r][c]), None)
        if pivot_index is None:return None
        if pivot_index!=c:a[pivot_index],a[c]=a[c],a[pivot_index]
        pivot=a[c][c]
        for r in range(c+1,n):
            factor=a[r][c]
            for j in range(c+1,n+1):
                num=a[r][j]*pivot-factor*a[c][j]
                assert num%den==0, 'Bareiss non-exact division'
                a[r][j]=num//den
            a[r][c]=0
        den=pivot
    if a[n-1][n-1]==0:return None
    ans=[Q(0)]*n
    for i in range(n-1,-1,-1):
        ans[i]=(Q(a[i][n])-sum((a[i][j]*ans[j] for j in range(i+1,n)),Q(0)))/a[i][i]
    return tuple(ans)

def law(t,s,h,u=0,v=0,w=0,z=0):
    c=(t,s,h,u,v,w,z)
    return tuple((1+sum((a*b for a,b in zip(row,c)),Q(0)))/16 for row in ROWS)

def tv(a,b):return sum((abs(x-y) for x,y in zip(a,b)),Q(0))/2

def result():
    assert len(RESTRICTIONS)==19 and len(BOUNDS)==19
    bases=0;non_sing=0;feasible_bases=0
    vertices=set()
    for inds in combinations(range(19),7):
        bases+=1
        x=exact_solve(RESTRICTIONS,BOUNDS,inds)
        if x is None:continue
        non_sing+=1
        if any(sum((p*v for p,v in zip(row,x)),Q(0))<rhs for row,rhs in zip(RESTRICTIONS,BOUNDS)):
            continue
        feasible_bases+=1
        vertices.add(x)
    assert bases==comb(19,7)==50388
    assert vertices
    tight=0; bad=0; greatest=Q(-100)
    for t,s,h,u,v,w,z in vertices:
        center=law(t,s,t+s-1)
        source=law(t,s,h,u,v,w,z)
        assert sum(center)==sum(source)==1 and min(center)>=0 and min(source)>=0
        cap=(3-t-2*s)/4
        excess=tv(center,source)-cap
        greatest=max(greatest,excess)
        if excess==0:tight+=1
        if excess>0:bad+=1
    assert greatest==0 and bad==0
    polygon=((Q(1),Q(0)),(Q(3,5),Q(2,5)),(Q(1),Q(1)))
    for t,s in polygon:
        plus=law(t,s,t+s-1,1-s,1-s,1-t,1-t)
        minus=law(t,s,t+s-1,s-1,s-1,t-1,t-1)
        assert min(plus)>=0 and min(minus)>=0
        assert tv(plus,minus)==(3-t-2*s)/2
    # Exact external witness: extension of this explicit center fails below the oblique edge.
    t0,s0=Q(13,20),Q(1,2)
    x0=t0-s0
    q0=law(t0,s0,t0+s0-1)
    source0=law(t0,s0,1-x0,-x0,-x0,0,0)
    assert min(source0)>=0 and tv(q0,source0)==Q(7,20)
    assert (3-t0-2*s0)/4==Q(27,80)
    assert tv(q0,source0)-(3-t0-2*s0)/4==Q(1,80)
    return {
      'unit':'R749SOI','status':'PASS','scope':'auxiliary 16-state Walsh source-observer fiber, all real parameters in the stated triangle',
      'scientific_pin':PIN,'center':'q=(1+t chi3+s chi12+(t+s-1)chi15)/16',
      'triangle_vertices':[['1','0'],['3/5','2/5'],['1','1']],
      'triangle_area':'1/5',
      'outside_candidate_counterexample':{'parameter':['13/20','1/2'],'witness':'h=17/20, u=v=-3/20, w=z=0','tv':'7/20','diameter_lower':'27/80','center_excess':'1/80','scope':'failure of the stated affine center outside triangle, not all calibrated centers'},
      'domain_halfspaces':['t<=1','t+s>=1','3t-2s>=1'],
      'exact_radius':'rho=rho_cal=(3-t-2s)/4',
      'lower_witness':'source pair h=t+s-1, (u,v,w,z)=+/- (1-s,1-s,1-t,1-t)',
      'upper_certificate':{'inequalities':19,'dimension':7,'active_basis_count':bases,
          'nonsingular_bases':non_sing,'feasible_bases':feasible_bases,
          'distinct_feasible_vertices':len(vertices),'tight_vertices':tight,
          'positive_excess_vertices':bad,'maximum_excess':str(greatest)},
      'independent_review':'NOT_REVIEWED',
      'native_X6_V29_V39_correspondence':'OPEN'
    }
if __name__=='__main__': print(json.dumps(result(),ensure_ascii=False,sort_keys=True,indent=2))
