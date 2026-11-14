#!/usr/bin/env python3
"""R749SOE exact transverse Walsh minimax segment on t in [1/2,9/16], s=1/2.
No floating point; exhaustive active-facet enumeration over 6D polytope.
Frozen scientific model enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
"""
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
from math import comb
import json

MASKS=(3,12,15,1,2,4,8)
SIGNS=[tuple(1 if not ((m&x).bit_count()&1) else -1 for m in MASKS) for x in range(16)]
# y=(16t,16h,16u,16v,16w,16z); s=1/2
ROWS=[tuple(row[j] for j in (0,2,3,4,5,6)) for row in SIGNS]+[(1,0,0,0,0,0),(-1,0,0,0,0,0)]
RHS=[-16-8*row[1] for row in SIGNS]+[8,-9]
EVENT_AD=(1,2,4,7,8,11,13,14)
EVENT_GAMMA_I=(0,1,2,3,4,8,12)
EVENT_GAMMA_II=(0,1,2,3,4,5,6,8,9,10,12)

def solve(ids):
    n=6
    a=[list(ROWS[i])+[RHS[i]] for i in ids]
    prev=1
    for j in range(n-1):
        k=next((k for k in range(j,n) if a[k][j]),None)
        if k is None:return None
        if k!=j:a[j],a[k]=a[k],a[j]
        pivot=a[j][j]
        for i in range(j+1,n):
            below=a[i][j]
            for k in range(j+1,n+1):
                v=a[i][k]*pivot-below*a[j][k]
                assert v%prev==0,(v,prev)
                a[i][k]=v//prev
            a[i][j]=0
        prev=pivot
    if not a[-1][-2]:return None
    out=[F(0)]*n
    for j in range(n-1,-1,-1):
        out[j]=(F(a[j][-1])-sum((a[j][k]*out[k] for k in range(j+1,n)),F(0)))/a[j][j]
    return tuple(out)

def law(t,s,h,u,v,w,z):
    terms=(t,s,h,u,v,w,z)
    return tuple((1+sum((p*r for p,r in zip(terms,row)),F(0)))/16 for row in SIGNS)

def center(a,b,c):return law(a,b,c,F(0),F(0),F(0),F(0))
def tv(p,q):return sum((abs(x-y) for x,y in zip(p,q)),F(0))/2

def analytic_lower():
    # Every event identity is affine in (x,a,b,c). Endpoint/basis checks are exact.
    for x in (F(0),F(1,16)):
        t=F(1,2)+x;s=F(1,2)
        muA=law(t,s,1-x,-x,-x,F(0),F(0))
        muG=law(t,s,x,-F(1,2),-F(1,2),x-F(1,2),x-F(1,2))
        assert min(muA)>=0 and min(muG)>=0
        assert sum(muA)==sum(muG)==1
        for a,b,c in ((F(0),F(0),F(0)),(F(1),F(0),F(0)),(F(0),F(1),F(0)),
                      (F(0),F(0),F(1)),(F(1,2)+x,F(1,2),F(2,11))):
            q=center(a,b,c)
            LA=sum((q[i]-muA[i] for i in EVENT_AD),F(0))
            LGI=sum((q[i]-muG[i] for i in EVENT_GAMMA_I),F(0))
            LGII=sum((q[i]-muG[i] for i in EVENT_GAMMA_II),F(0))
            assert LA==(1-x-c)/2
            assert LGI==(3*a+3*b-c)/16-x/2+F(3,16)
            assert LGII==(-a-b+3*c)/16-x/2+F(7,16)
            assert (LA+LGI+3*LGII)/5==F(2,5)-x/2
            if a==t and b==s:
                assert (3*LA+8*LGII)/11==F(9,22)-F(6,11)*x
    return {'witnesses':'muA=(h=1-x,u=v=-x,w=z=0), muG=(h=x,u=v=-1/2,w=z=x-1/2)',
            'events':{'A':list(EVENT_AD),'GI':list(EVENT_GAMMA_I),'GII':list(EVENT_GAMMA_II)},
            'universal_free_lower':'(LA+LGI+3LGII)/5=2/5-x/2',
            'universal_calibrated_lower':'(3LA+8LGII)/11=9/22-6x/11'}

def exact_upper():
    seen=set();cnt=Counter()
    for ids in combinations(range(18),6):
        cnt['facet_sets']+=1
        y=solve(ids)
        if y is None:continue
        cnt['nonsingular_bases']+=1
        if all(sum((a*b for a,b in zip(row,y)),F(0))>=bound for row,bound in zip(ROWS,RHS)):
            cnt['feasible_bases']+=1
            seen.add(y)
    assert cnt['facet_sets']==comb(18,6)==18564
    max_gap_free=F(-5);max_gap_cal=F(-5)
    free_tight=0;cal_tight=0
    for y in seen:
        t,h,u,v,w,z=(v/16 for v in y)
        x=t-F(1,2)
        mu=law(t,F(1,2),h,u,v,w,z)
        qf=center(F(1),F(1,5),F(1,5))
        qc=center(t,F(1,2),(F(2)+x)/11)
        assert min(mu)>=0 and min(qf)>=0 and min(qc)>=0
        rf=F(2,5)-x/2;rc=F(9,22)-6*x/11
        gf=tv(mu,qf)-rf;gc=tv(mu,qc)-rc
        max_gap_free=max(max_gap_free,gf)
        max_gap_cal=max(max_gap_cal,gc)
        free_tight+=int(gf==0);cal_tight+=int(gc==0)
    assert max_gap_free==0,(max_gap_free,len(seen))
    assert max_gap_cal==0,(max_gap_cal,len(seen))
    return {**cnt,'distinct_vertices':len(seen),'free_tight_vertices':free_tight,'cal_tight_vertices':cal_tight,
            'max_excess_free':str(max_gap_free),'max_excess_cal':str(max_gap_cal),'upper_bound_violations':0}

def main():
    d=analytic_lower()
    q=exact_upper()
    return {'result':'PASS','unit':'R749SOE','scope':'all real t in [1/2,9/16], s=1/2; auxiliary 16-state Walsh fiber; author-side NOT_REVIEWED',
            'scientific_input_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
            'minimax_free':'2/5-(t-1/2)/2',
            'minimax_calibrated':'9/22-6(t-1/2)/11',
            'gap':'1/110-(t-1/2)/22 >= 1/160',
            'free_center':'[1+chi_3+(chi_12+chi_15)/5]/16',
            'calibrated_center':'[1+t chi_3+(1/2)chi_12+((2+t-1/2)/11)chi_15]/16',
            'analytic_lower':d,'exact_joint_polytope_upper':q}

if __name__=='__main__':print(json.dumps(main(),indent=2,sort_keys=True))
