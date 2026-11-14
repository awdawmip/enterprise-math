#!/usr/bin/env python3
"""R749SON — slanted-cap extension of SOK phase-region centers.
Exact Fraction/Bareiss 7-dimensional joint-polytope verifier. No external packages.
Scientific pin: a72226e2430ffa4786321ac86e7f0c599d5f0389.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb
import json
M=(3,12,15,1,2,4,8)
W=tuple(tuple(1 if (k&m).bit_count()%2==0 else -1 for m in M) for k in range(16))
# P = {t>=3/5, 3t-2s<=1, 5t-4s>=1}; upper t<=1 follows.
A=W+((5,0,0,0,0,0,0),(-3,2,0,0,0,0,0),(5,-4,0,0,0,0,0))
B=(-1,)*16+(3,-1,1)
P=((Q(3,5),Q(2,5)),(Q(1),Q(1)),(Q(3,5),Q(1,2)))
EA=(1,2,4,7,8,11,13,14)
EG=(0,1,2,4,5,6,8,9,10,12)
def solve(ids):
    n=7; a=[list(A[i])+[B[i]] for i in ids];den=1
    for j in range(n-1):
        k=next((i for i in range(j,n) if a[i][j]),None)
        if k is None:return None
        if k!=j:a[k],a[j]=a[j],a[k]
        p=a[j][j]
        for i in range(j+1,n):
            f=a[i][j]
            for l in range(j+1,n+1):
                num=a[i][l]*p-f*a[j][l]
                assert num%den==0
                a[i][l]=num//den
            a[i][j]=0
        den=p
    if not a[-1][-2]:return None
    x=[Q(0)]*n
    for j in range(n-1,-1,-1):
        x[j]=(Q(a[j][n])-sum((a[j][k]*x[k] for k in range(j+1,n)),Q(0)))/a[j][j]
    return tuple(x)
def law(t,s,h,u=0,v=0,w=0,z=0):
    c=(t,s,h,u,v,w,z)
    return tuple((1+sum((a*b for a,b in zip(row,c)),Q(0)))/16 for row in W)
def tv(p,q):return sum((abs(x-y) for x,y in zip(p,q)),Q(0))/2

def run():
    vs=set();ns=feasible=0
    for ids in combinations(range(19),7):
        x=solve(ids)
        if x is None:continue
        ns+=1
        if any(sum((a*b for a,b in zip(row,x)),Q(0))<b for row,b in zip(A,B)):
            continue
        feasible+=1;vs.add(x)
    assert len(vs)>0
    mf=mc=Q(-100);badf=badc=0; free_witness=None;cal_witness=None;ft=ct=0
    for t,s,h,u,v,w,z in vs:
        p=law(t,s,h,u,v,w,z)
        f=law(Q(1),2*t-1,2*t-1)
        c=law(t,s,(9*s-t-3)/5)
        assert all(sum(z)==1 and min(z)>=0 for z in (p,f,c))
        fe=tv(f,p)-(3-t-2*s)/4
        ce=tv(c,p)-(4-2*t-2*s)/5
        if fe>mf:mf=fe;free_witness=(t,s,h,u,v,w,z)
        if ce>mc:mc=ce;cal_witness=(t,s,h,u,v,w,z)
        ft+=int(fe==0);ct+=int(ce==0)
        badf+=int(fe>0);badc+=int(ce>0)
    for t,s in P:
        aa=law(t,s,1+s-t,s-t,s-t)
        gg=law(t,s,t+s-1,s-1,s-1,t-1,t-1)
        zz=law(t,s,t+s-1,1-s,1-s,1-t,1-t)
        assert all(min(z)>=0 and sum(z)==1 for z in (aa,gg,zz))
        assert tv(gg,zz)==(3-t-2*s)/2
        for h in (Q(-1,5),Q(0),Q(1,5)):
            q=law(t,s,h)
            la=sum((q[i]-aa[i] for i in EA),Q(0))
            lg=sum((q[i]-gg[i] for i in EG),Q(0))
            assert (la+4*lg)/5==(4-2*t-2*s)/5
    # Exact geometry and a source-specific invalidity witness beyond the new cap.
    area_p=abs(sum((P[i][0]*P[(i+1)%3][1]-P[(i+1)%3][0]*P[i][1] for i in range(3)),Q(0)))/2
    full_polygon=((Q(1),Q(0)),(Q(3,5),Q(2,5)),(Q(3,5),Q(1,2)),(Q(1),Q(1)))
    area_q=abs(sum((full_polygon[i][0]*full_polygon[(i+1)%4][1]-full_polygon[(i+1)%4][0]*full_polygon[i][1] for i in range(4)),Q(0)))/2
    assert area_p==Q(1,50) and area_q==Q(11,50)
    t=s=Q(3,5)
    f=law(Q(1),2*t-1,2*t-1)
    c=law(t,s,(9*s-t-3)/5)
    src_f=law(t,s,Q(1))
    src_c=law(t,s,Q(1,5),Q(2,5),Q(2,5),Q(2,5),Q(2,5))
    assert min(src_f)>=0 and min(src_c)>=0
    assert tv(f,src_f)==Q(2,5) and tv(c,src_c)==Q(33,100)
    assert tv(f,src_f)-(3-t-2*s)/4==Q(1,10)
    assert tv(c,src_c)-(4-2*t-2*s)/5==Q(1,100)
    return {'unit':'R749SON','status':'PASS' if mf==mc==0 else 'FAIL_FALSIFIED',
        'scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
        'scope':'auxiliary Walsh 16-atom source fiber; all real parameters on positive-side triangle, plus R749SOI zero-side triangle',
        'P_vertices':[[str(z) for z in p] for p in P],
        'whole_polygon':[[str(z) for z in p] for p in full_polygon],
        'positive_area':str(area_p),'total_area':str(area_q),
        'rho':'(3-t-2*s)/4',
        'rho_cal':'max((3-t-2*s)/4,(4-2*t-2*s)/5)',
        'gap':'max(0,1-3*t+2*s)/20',
        'outside_cap_source_witness':{'t':'3/5','s':'3/5','free_excess':'1/10','cal_center_excess':'1/100',
         'scope':'failure of these two explicit candidate centers outside region; no global radius conclusion'},
        'active_bases':comb(19,7),'non_singular_bases':ns,'feasible_bases':feasible,
        'distinct_vertices':len(vs),'tight_free':ft,'tight_cal':ct,
        'bad_free':badf,'bad_cal':badc,'max_free_excess':str(mf),'max_cal_excess':str(mc),
        'max_free_vertex':[str(z) for z in free_witness],
        'max_cal_vertex':[str(z) for z in cal_witness],
        'independent_review':'NOT_REVIEWED'}
if __name__=='__main__': print(json.dumps(run(),ensure_ascii=False,indent=2,sort_keys=True))
