#!/usr/bin/env python3
"""R749SPI: exact full Walsh diagonal 1/2<=t=s<=1; Fraction and integer Bareiss."""
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
from math import comb
import json
M=(3,12,15,1,2,4,8)
W=tuple(tuple(1 if ((k&m).bit_count()&1)==0 else -1 for m in M) for k in range(16))
# x=(r,h,u,v,w,z), t=s=r. 16 atoms and endpoints r>=1/2, r<=1.
rows=[(a+b,*tail) for a,b,*tail in W]+[(2,0,0,0,0,0),(-1,0,0,0,0,0)]
rhs=[-1]*16+[1,-1]
def law(r,h,u=0,v=0,w=0,z=0):
    coeff=(r,r,h,u,v,w,z)
    return tuple((1+sum(a*b for a,b in zip(coeff,row)))/16 for row in W)
def free_center(r):
    a=(8*r-3)/5;coeff=(F(1),a,a,0,0,0,0)
    return tuple((1+sum(x*y for x,y in zip(coeff,row)))/16 for row in W)
def cal_center(r):return law(r,(18*r-7)/11)
def tv(p,q):return sum(abs(x-y) for x,y in zip(p,q))/2
def solve(indices):
    n=6;a=[list(rows[i])+[rhs[i]] for i in indices];prev=1
    for j in range(n-1):
        pi=next((i for i in range(j,n) if a[i][j]),None)
        if pi is None:return None
        if pi!=j:a[pi],a[j]=a[j],a[pi]
        pivot=a[j][j]
        for i in range(j+1,n):
            mul=a[i][j]
            for k in range(j+1,n+1):
                num=a[i][k]*pivot-mul*a[j][k]
                assert num%prev==0
                a[i][k]=num//prev
            a[i][j]=0
        prev=pivot
    if a[-1][n-1]==0:return None
    x=[F(0)]*n
    for j in range(n-1,-1,-1):
        x[j]=(F(a[j][n])-sum(a[j][i]*x[i] for i in range(j+1,n)))/a[j][j]
    return tuple(x)
def source_minus(r):return law(r,2*r-1,r-1,r-1,r-1,r-1)
def source_a(r):return law(r,F(1))
def check_event_lower(r):
    EA=(7,11,13,14,15);EB=(0,3,5,6,9,10,12,15)
    p=source_minus(r);z=source_a(r);c=cal_center(r)
    for obj in (p,z,c,free_center(r)):
        assert min(obj)>=0 and sum(obj)==1
    assert sum(p[i] for i in EA)==F(5,4)-r
    assert sum(z[i] for i in EB)==1
    h=(18*r-7)/11
    assert sum(p[i]-c[i] for i in EA)==(15-18*r+3*h)/16
    assert sum(z[i]-c[i] for i in EB)==(1-h)/2
    assert (15-18*r+3*h)/16 == 9*(1-r)/11
    assert (1-h)/2 == 9*(1-r)/11
    return {'r':str(r),'free_radius':str(4*(1-r)/5),'cal_radius':str(9*(1-r)/11),'gap':str((1-r)/55)}
def run():
    vertices=set();ns=feas=0
    for inds in combinations(range(18),6):
        x=solve(inds)
        if x is None:continue
        ns+=1
        if any(sum(a*b for a,b in zip(row,x))<b for row,b in zip(rows,rhs)):continue
        feas+=1;vertices.add(x)
    histogram=Counter();maxf=maxc=None;tightf=tightc=0;errors=[]
    for r,h,u,v,w,z in vertices:
        p=law(r,h,u,v,w,z);qf=free_center(r);qc=cal_center(r)
        for v0 in (p,qf,qc):assert min(v0)>=0 and sum(v0)==1
        ef=tv(p,qf)-4*(1-r)/5
        ec=tv(p,qc)-9*(1-r)/11
        maxf=ef if maxf is None else max(maxf,ef)
        maxc=ec if maxc is None else max(maxc,ec)
        tightf+=int(ef==0);tightc+=int(ec==0)
        histogram[str(r)]+=1
        if ef>0 or ec>0:errors.append((str(r),str(ef),str(ec)))
    assert len(vertices)==18 and maxf==maxc==0 and not errors
    endpoints=[check_event_lower(F(1,2)),check_event_lower(F(1))]
    assert histogram=={'1/2':17,'1':1}
    return {'schema':'R749SPI_EXACT_DIAGONAL_WALSH_GAP_V1','status':'PASS',
      'scientific_pin':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
      'domain':'t=s=r; 1/2<=r<=1, all real','free_radius':'4(1-r)/5',
      'calibrated_radius':'9(1-r)/11','calibration_gap':'(1-r)/55',
      'candidate_bases':comb(18,6),'nonsingular_bases':ns,'feasible_bases_with_repeats':feas,
      'distinct_vertices':len(vertices),'projected_vertex_counts':dict(sorted(histogram.items())),
      'tight_free_vertices':tightf,'tight_cal_vertices':tightc,'max_free_excess':str(maxf),
      'max_calibrated_excess':str(maxc),'endpoint_lower_certificates':endpoints,
      'errors':errors,'arithmetic':'exact Integer Bareiss plus Python Fraction',
      'logic':'complete six-dimensional vertex enumeration plus convexity and explicit two-event lower bounds',
      'review':'AUTHOR_EXACT_NOT_REVIEWED','native_transfer':'OPEN'}
if __name__=='__main__':print(json.dumps(run(),ensure_ascii=False,indent=2,sort_keys=True))
